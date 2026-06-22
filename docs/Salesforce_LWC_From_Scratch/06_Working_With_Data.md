# 06 — Working with Salesforce Data

## 🧠 The One Idea

**There are two ways to get data: a vending machine (`@wire`) and a barista (imperative).** With
**`@wire`**, you declare what you want and Salesforce delivers it automatically, **cached** and
**reactive** — like a vending machine that refills itself. With **imperative Apex**, you place an
order and wait for it when *you* decide — like asking a barista, useful when you need control or
to act on a button click.

The one-liner: **"`@wire` = declarative, cached, reactive reads; imperative Apex = on-demand calls
you control."**

---

## 1. `@wire` to an Apex method

```javascript
import { wire } from 'lwc';
import getContacts from '@salesforce/apex/ContactController.getContacts';

@wire(getContacts, { accountId: '$recordId' })
wiredContacts;     // { data, error }
```

```html
<template lwc:if={wiredContacts.data}>
    <template for:each={wiredContacts.data} for:item="c">
        <p key={c.Id}>{c.Name}</p>
    </template>
</template>
```

The Apex method **must be `@AuraEnabled(cacheable=true)`** to be wireable. The `$recordId` makes
it re-run when `recordId` changes.

---

## 2. The Apex side

```apex
public with sharing class ContactController {
    @AuraEnabled(cacheable=true)         // cacheable → wireable, read-only
    public static List<Contact> getContacts(Id accountId) {
        return [SELECT Id, Name FROM Contact WHERE AccountId = :accountId WITH USER_MODE];
    }
}
```

- **`cacheable=true`** = read-only and cached on the client; required for `@wire`.
- For methods that **change data**, omit `cacheable` and call them **imperatively**.

---

## 3. Imperative Apex

```javascript
import getContacts from '@salesforce/apex/ContactController.getContacts';

async handleSearch() {
    try {
        this.contacts = await getContacts({ accountId: this.recordId });
    } catch (e) {
        this.error = e;
    }
}
```

Use imperative when you need to call **on a user action**, **chain logic**, handle errors
manually, or call a method that **modifies** data.

---

## 4. `@wire` to a property vs a function

```javascript
@wire(getContacts, { accountId: '$recordId' }) contacts;   // property

@wire(getContacts, { accountId: '$recordId' })
wiredResult({ data, error }) {                              // function
    if (data) this.records = data;
    if (error) this.error = error;
}
```

Wire to a **function** when you need to **transform** the result or set multiple fields.

---

## 5. Refreshing wired data

Wired data is cached. After a DML, force a refresh:

```javascript
import { refreshApex } from '@salesforce/apex';
// keep the whole wire result, then:
await refreshApex(this.wiredResult);
```

`refreshApex` re-runs the wire and updates the cache — essential after create/update/delete.

---

## 6. `@wire` to Salesforce's built-in adapters

You don't always need custom Apex. LWC ships wire adapters from **`lightning/ui*Api`** and
**`lightning/uiRecordApi`** (e.g., `getRecord`, `getObjectInfo`) — these are **Lightning Data
Service** (Lesson 07), giving cached record access **without Apex**.

---

## 🌍 Real-World Example

**A related-contacts panel that stays in sync for free.** On an Account page, a
`@wire(getContacts, { accountId: '$recordId' })` panel lists the account's contacts. When the user
navigates from Acme to Globex, the `$recordId` change re-fires the wire automatically and the list
updates — no event wiring, no manual fetch. After the user adds a contact through an *imperative*
call, a single `refreshApex` repopulates the cached list so the new row appears immediately instead
of showing stale data.

---

## 🔬 Under the Hood (In-Depth)

- **`cacheable=true` is a contract** — it promises the method is side-effect-free, letting the
  Lightning Data cache store the result keyed by method + parameters; identical calls across
  components are served from cache, not the server.
- **Wires are reactive subscriptions** — the wire service holds the result and pushes new values
  when reactive params change or the cache is invalidated; you never call a wire, it calls you.
- **`refreshApex` invalidates that cache entry** — it re-executes the provisioner and updates every
  component bound to the same wired result, which is why you must keep the *whole* result object,
  not just `.data`.
- **Imperative calls bypass the cache** — they return a Promise and never auto-refresh, so you own
  error handling and refresh timing.
- **Errors are normalized** — wire and Apex errors arrive as a structured object
  (`error.body.message`), so a reusable `reduceErrors` helper is common in production apps.

---

## 🎤 Say this in the interview

- *"`@wire` is **declarative, cached, reactive** and needs **`@AuraEnabled(cacheable=true)`**;
  imperative Apex is for **user-triggered** calls or DML."*
- *"Reactive params use the **`$`** prefix so the wire re-runs when they change."*
- *"After DML I call **`refreshApex`** to bust the cache; for plain record CRUD I prefer
  **Lightning Data Service** over custom Apex."*

➡️ **Next:** [07 — Lightning Data Service & base components](./07_LDS_And_Base_Components.md)
