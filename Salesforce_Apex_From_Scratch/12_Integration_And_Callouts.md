# 12 — Integration & Callouts

## 🧠 The One Idea

**Integration is Salesforce making phone calls (outbound) and answering them (inbound).** Real
apps rarely live alone — they talk to payment gateways, ERPs, and other clouds. **Callouts** are
Salesforce dialing *out* to an external API; **Apex web services** are Salesforce *picking up*
when an external system calls *in*.

The one-liner: **"Apex integrates two ways — callouts go out, Apex REST/SOAP services let
others call in."**

---

## 1. Outbound: HTTP callouts

```apex
public class WeatherService {
    public static String getTemp(String city) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('callout:Weather_API/temp?city=' + EncodingUtil.urlEncode(city, 'UTF-8'));
        req.setMethod('GET');
        HttpResponse res = new Http().send(req);
        if (res.getStatusCode() == 200) {
            Map<String, Object> body =
                (Map<String, Object>) JSON.deserializeUntyped(res.getBody());
            return String.valueOf(body.get('temp'));
        }
        throw new CalloutException('Status ' + res.getStatusCode());
    }
}
```

Note **`callout:Weather_API`** — that's a **Named Credential** (next section).

---

## 2. Named Credentials (the right way to auth)

Never hard-code URLs, usernames, tokens, or API keys. A **Named Credential** stores the
endpoint + authentication (Basic, OAuth, etc.) as **metadata**, and Apex just references it by
name. Benefits: secrets stay out of code, auth/token refresh is handled for you, and you can
swap endpoints per environment.

---

## 3. The callout rules

- **Whitelist the endpoint**: add a **Remote Site Setting** or use a Named Credential.
- **No callout after uncommitted DML** in the same transaction → do callouts first, or move to
  `@future(callout=true)` / Queueable (Lesson 09).
- **Timeout** default 10s, max 120s; **callout limit** 100 per transaction.
- In tests, you **must mock** callouts with `HttpCalloutMock` (Lesson 10).

---

## 4. Parsing JSON

```apex
// Untyped (quick): Map<String, Object>
Map<String, Object> m = (Map<String, Object>) JSON.deserializeUntyped(body);

// Typed (robust): into an Apex class with matching fields
public class Quote { public Decimal price; public String symbol; }
Quote q = (Quote) JSON.deserialize(body, Quote.class);

String out = JSON.serialize(q);   // object → JSON
```

Typed deserialization is cleaner for stable APIs; untyped is fine for quick/variable payloads.

---

## 5. Inbound: exposing Apex as a service

**Apex REST** — your own endpoint at `/services/apexrest/...`:

```apex
@RestResource(urlMapping='/accounts/*')
global with sharing class AccountApi {
    @HttpGet
    global static Account getIt() {
        String id = RestContext.request.requestURI.substringAfterLast('/');
        return [SELECT Id, Name FROM Account WHERE Id = :id];
    }
    @HttpPost
    global static Id createIt(String name) {
        Account a = new Account(Name = name);
        insert a; return a.Id;
    }
}
```

Annotations: `@HttpGet`, `@HttpPost`, `@HttpPut`, `@HttpPatch`, `@HttpDelete`. **Apex SOAP**
services use `webservice static` methods exposed via WSDL.

---

## 6. Other integration patterns (know the names)

- **Platform Events** — publish/subscribe event bus for near-real-time, decoupled integration.
- **Change Data Capture (CDC)** — stream record changes to external systems.
- **Outbound Messages / External Services** — declarative options.
- **Bulk API / REST API / Composite API** — Salesforce's standard data APIs for big loads.

---

## 🎤 Say this in the interview

- *"Outbound = **HTTP callouts** authenticated via **Named Credentials** (no hard-coded
  secrets); inbound = **Apex REST/SOAP** services."*
- *"You **can't call out after uncommitted DML** — do the callout first or go **async**; and
  callouts must be **mocked** in tests."*
- *"For event-driven, decoupled integration I use **Platform Events** or **Change Data
  Capture**, and Bulk/Composite APIs for large data."*

➡️ **Next:** [13 — Hands-on lab](./13_Hands_On_Lab.md)
