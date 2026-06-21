# 09 — Asynchronous Apex

## 🧠 The One Idea

**Async Apex is mailing a parcel instead of handing it over in person.** Synchronous code makes
the user wait while it runs. **Asynchronous** code says "I'll handle this later, in the
background," freeing the user immediately and giving you **higher governor limits** and the
ability to make **callouts** without blocking. The cost: you don't control exactly *when* it
runs.

The one-liner: **"Async Apex runs work in the background with higher limits — at the price of
guaranteed timing."**

---

## 1. The four flavors (know when to use each)

| Type | Use it for | Key trait |
|---|---|---|
| **Future** | quick fire-and-forget; a callout from a trigger | `@future` static void method, primitives only |
| **Queueable** | chainable jobs, complex objects, sequencing | implements `Queueable`; returns a Job Id |
| **Batch** | huge data volumes (millions of records) | processes in **chunks**, own limits per chunk |
| **Scheduled** | run on a schedule (cron) | implements `Schedulable` |

---

## 2. Future methods

```apex
public class Notifier {
    @future(callout=true)
    public static void ping(Set<Id> ids) {     // params: primitives/collections only
        // make a callout, do light work
    }
}
```

- Must be **`static void`**, params are **primitives/collections of primitives** (no sObjects).
- **You can't chain** futures or monitor them easily — that's why Queueable largely replaced
  them.

---

## 3. Queueable (the modern default)

```apex
public class RecalcJob implements Queueable {
    private List<Id> ids;
    public RecalcJob(List<Id> ids) { this.ids = ids; }
    public void execute(QueueableContext ctx) {
        // do work; can accept sObjects and complex types
        if (needMore) System.enqueueJob(new RecalcJob(moreIds));  // chaining!
    }
}
// kick it off:
Id jobId = System.enqueueJob(new RecalcJob(ids));
```

Queueable accepts **complex types**, returns a **Job Id** you can monitor, and supports
**chaining** for sequential steps.

---

## 4. Batch Apex (for big data)

```apex
public class CleanupBatch implements Database.Batchable<sObject> {
    public Database.QueryLocator start(Database.BatchableContext bc) {
        return Database.getQueryLocator('SELECT Id FROM Account');  // up to 50M rows
    }
    public void execute(Database.BatchableContext bc, List<Account> scope) {
        // runs per chunk (default 200); each chunk gets fresh governor limits
    }
    public void finish(Database.BatchableContext bc) { /* send summary email */ }
}
// run with a batch size:
Database.executeBatch(new CleanupBatch(), 200);
```

The magic: **`start` defines the dataset, `execute` runs per chunk with its own limits**, so you
can process millions of records without blowing the 50k-row cap.

---

## 5. Scheduled Apex

```apex
public class NightlyJob implements Schedulable {
    public void execute(SchedulableContext sc) {
        Database.executeBatch(new CleanupBatch());   // often schedules a batch
    }
}
// schedule with cron (sec min hour day month weekday):
System.schedule('Nightly', '0 0 2 * * ?', new NightlyJob());
```

---

## 6. Rules & gotchas

- **DML before callout** problem? Move the callout to `@future(callout=true)` or Queueable.
- Limits: e.g. **50 jobs** added to the async queue per transaction; Batch allows **5 concurrent**
  batches; Future has a daily cap.
- **Testing async**: wrap the call between **`Test.startTest()` / `Test.stopTest()`** — the job
  runs synchronously when `stopTest()` is reached (Lesson 10).

---

## 🎤 Say this in the interview

- *"Four async tools: **Future** (simple callout), **Queueable** (chainable, complex types),
  **Batch** (millions of records in chunks), **Scheduled** (cron)."*
- *"**Batch** gives each chunk **fresh governor limits**, so it's how I process huge volumes;
  **Queueable** replaced Future for chaining and sObject params."*
- *"I test async by forcing execution inside **`Test.startTest()/stopTest()`**."*

➡️ **Next:** [10 — Testing Apex](./10_Testing_Apex.md)
