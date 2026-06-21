# 01 — What is Apex & When to Use It

## 🧠 The One Idea

**Apex is Java that lives inside the database.** In a normal app you write code on one server
and reach across the network to a database somewhere else. In Apex, your code runs *on
Salesforce's servers, right next to the data* — so querying and saving records is part of the
language itself, not a separate library. Think of it as a chef who lives **inside the pantry**:
ingredients are always within arm's reach.

The one-liner: **"Apex is Salesforce's strongly-typed, Java-like language that runs on-platform,
with the database built in."**

---

## 1. What Apex looks like

If you know Java or C#, Apex will feel familiar: classes, interfaces, `if/else`, `for` loops,
strong typing, exceptions. A tiny example:

```apex
public class Greeter {
    public String hello(String name) {
        return 'Hello, ' + name + '!';
    }
}
```

The superpower is that **SOQL queries and DML are first-class syntax**:

```apex
List<Account> accts = [SELECT Id, Name FROM Account WHERE Industry = 'Tech'];
accts[0].Name = 'Renamed';
update accts;   // saves to the database — no ORM, no connection string
```

---

## 2. Where Apex runs (execution contexts)

Apex doesn't run "whenever." It runs inside a **trigger** of some kind, called an
*execution context*:

- **Triggers** — automatically when records are saved (Lesson 07).
- **Controllers / `@AuraEnabled` methods** — when an LWC/Aura component calls the server.
- **REST/SOAP web services** — when an external system calls in (Lesson 12).
- **Asynchronous jobs** — Batch, Queueable, Future, Scheduled (Lesson 09).
- **Anonymous Apex** — ad-hoc scripts you run in the Developer Console.

Each context starts fresh and gets **its own set of governor limits**.

---

## 3. When to use Apex (and when not to)

Use Apex when:
- Logic is too complex for **Flow** or formula fields (loops, recursion, complex branching).
- You need to process **large volumes** in bulk (Batch Apex).
- You're **integrating** with an external system (callouts, web services).
- You need **transaction control** beyond what declarative tools offer.

Prefer **clicks (Flow, validation rules)** when the logic is simple — it's easier to maintain
and doesn't need test classes.

---

## 4. Versioning, compilation & saving

- Apex is **compiled and stored as metadata** in your org; Salesforce manages the runtime.
- Each class is pinned to an **API version**, so old code keeps behaving predictably as the
  platform evolves.
- You **cannot deploy Apex to production without 75% test coverage** (Lesson 10) — a hard
  platform rule, not a team policy.

---

## 5. Apex vs the languages you know

- Like **Java**: classes, generics-ish collections, exceptions, strong typing.
- **Unlike** Java: it's **case-insensitive**, runs in a sandboxed multitenant runtime, has
  **no `main()`**, and you can't spin up arbitrary threads or open sockets — only governed
  callouts.

---

## 🌍 Real-World Example

**A subscription business auto-invoices when a deal closes.** The moment an `Opportunity` flips
to *Closed Won*, an Apex trigger:

1. Creates an `Invoice__c` record from the deal's line items (DML, next to the data).
2. Calls the **Stripe API** with a callout to charge the customer's card.
3. Generates a PDF and emails it to the billing contact.

All of this runs **server-side in one transaction**, inches from the database. Doing the same
thing from a browser would mean shipping records back and forth across the network for every step
— slower, less secure, and impossible to wrap in a single rollback-safe unit.

---

## 🔬 Under the Hood (In-Depth)

- **Compilation pipeline** — when you save a class, Apex is **compiled to bytecode** and stored as
  metadata in your org. At run time the platform executes that bytecode in a **sandboxed,
  interpreted runtime** — there's no `main()`, no threads you can spawn, and no file-system access.
- **Execution-context lifecycle** — each entry point (trigger, `@AuraEnabled` method, batch chunk,
  REST call) spins up a **fresh context** with its own **governor-limit counters** reset to zero.
  When the context ends, `static` variables are discarded.
- **`static` lives for the transaction** — a `static` variable persists across all code in the
  same execution context (used for caching and trigger recursion guards), then vanishes.
- **One transaction, many actors** — your Apex shares the request with validation rules, flows,
  roll-up summaries, and other automation in a strict **order of execution** (Lesson 05).
- **API-version pinning** — a class compiled against API `45.0` keeps its old behaviour even after
  the org upgrades, which is how Salesforce avoids breaking your code three times a year.

---

## 🎤 Say this in the interview

- *"Apex is a **strongly-typed, Java-like** language that runs **on-platform**, with SOQL and
  DML built into the syntax."*
- *"Every entry point is an **execution context** with its own governor limits — triggers,
  controllers, web services, async jobs, and anonymous Apex."*
- *"I reach for Apex only when **declarative tools** can't do the job, and I remember
  production needs **75% coverage**."*

➡️ **Next:** [02 — Apex language basics](./02_Language_Basics.md)
