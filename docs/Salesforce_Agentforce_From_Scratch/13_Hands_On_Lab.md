# 13 — Hands-On Lab: Build a Service Agent with a Custom Action

## 🧠 The One Idea

**You learn agents by building the smallest one that actually *does* something.** In this lab you'll
stand up a service agent with **one topic**, give it **one custom Apex action** (look up an order's
status), **ground** it, and **test** it. Small, but it exercises the whole stack: role → topic →
action → grounding → test.

The one-liner: **"Build a one-topic service agent with a custom Apex action, then test its
routing."**

---

## 1. Prerequisites

- An org with **Agentforce** enabled (a **Trailhead Playground** or Agentforce-enabled trial).
- **Agent Builder** (or **Agentforce Builder**) and **Prompt Builder** available.
- Permission to create **Apex** and edit agents. Optional: **Data Cloud** for richer grounding.

---

## 2. Step 1 — Create the Apex action

Create an `@InvocableMethod` the agent can call. Keep it bulk-safe and secure.

```apex
public with sharing class OrderStatusAction {
    public class Request  { @InvocableVariable(required=true) public String orderNumber; }
    public class Response { @InvocableVariable public String status;
                            @InvocableVariable public String eta; }

    @InvocableMethod(label='Get Order Status'
                     description='Returns shipping status and ETA for a given order number')
    public static List<Response> getStatus(List<Request> reqs) {
        List<Response> out = new List<Response>();
        for (Request r : reqs) {
            Response res = new Response();
            // Demo logic — replace with a real query (WITH USER_MODE) or callout.
            res.status = 'Shipped';
            res.eta    = 'Tomorrow by 5pm';
            out.add(res);
        }
        return out;
    }
}
```

The **label/description** are what the agent "reads," so make them clear.

---

## 3. Step 2 — Create the agent

1. **Setup → Agentforce / Agents → New Agent**.
2. Choose a **Service** type (or custom) and give it a **role/persona**:
   *"You are a friendly retail support agent. Be concise. Verify the order number before
   answering. Never share another customer's data."*

---

## 4. Step 3 — Add a topic

Create a topic **"Order Status"** with a sharp **classification description**:

> *"Use when the customer asks about the status, shipping, tracking, or delivery date of an order
> they already placed (they provide an order number)."*

Add **instructions**: *"Ask for the order number if it's missing. Call **Get Order Status**, then
report the status and ETA in one sentence."*

---

## 5. Step 4 — Attach the action & grounding

- Add the **Get Order Status** Apex action to the topic.
- Map the conversation's order number to the action's `orderNumber` input.
- (Optional) Add **grounding** — e.g., the **Order** record or a Data Cloud profile — so replies
  can include customer-specific context.

---

## 6. Step 5 — Test the routing

In the **conversation preview**, try varied phrasings:
- *"Where's my order 1234?"* → should route to **Order Status**, call the action.
- *"Has 1234 shipped yet?"* → same topic.
- *"I want a refund"* → should **not** match (no refund action) → fallback/escalate.

Open the **reasoning trace** each time: confirm the **topic** and **action inputs**. If it
misroutes, **sharpen the topic description**; if inputs are empty, **improve the input
description**.

---

## 7. Stretch goals

- Add a **second topic** ("Returns") with a Flow action and a **fallback/escalate** topic.
- Replace the demo logic with a **real SOQL query** (`WITH USER_MODE`).
- Add a **prompt-template action** to summarize the order in a friendly tone.
- Build a small **Testing Center** set covering happy paths + out-of-scope (Lesson 09).

---

## 🎤 Say this in the interview

- *"I built a one-topic **service agent** with a custom **Apex `@InvocableMethod`** action and
  tested its **routing** with the reasoning trace."*
- *"Most tuning was **wording** — the **topic description** for routing and **input descriptions**
  so the engine fills the action correctly."*
- *"I kept the action **bulk-safe and secure** and added a **fallback/escalate** path for
  out-of-scope requests."*

➡️ **Next:** [14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)
