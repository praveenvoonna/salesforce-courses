# 07 — Triggers & Trigger Frameworks

## 🧠 The One Idea

**A trigger is a tripwire on a table: "whenever a record is saved, run this code."** You don't
call a trigger — the platform fires it automatically on `insert`/`update`/`delete`/`undelete`.
The catch: triggers fire on **batches of records at once**, so they must be written to handle
**200 records** as easily as 1.

The one-liner: **"A trigger is automatic Apex that runs on DML events — and it must be
bulk-safe."**

---

## 1. The shape of a trigger

```apex
trigger AccountTrigger on Account (before insert, before update, after insert) {
    for (Account a : Trigger.new) {
        if (Trigger.isBefore && Trigger.isInsert) {
            a.Rating = (a.AnnualRevenue > 1000000) ? 'Hot' : 'Warm';
        }
    }
}
```

A trigger is named, tied to **one object**, and lists the **events** it cares about.

---

## 2. before vs after

- **before** triggers: modify the records **in place** (`Trigger.new`) — no DML needed, the
  values save automatically. Use for **validation and defaulting**.
- **after** triggers: records already have **Ids** and are saved — use to create/update
  **related** records, send notifications, or do roll-ups not possible declaratively.

You can't change `Trigger.new` fields in an **after** trigger (it's read-only there).

---

## 3. Context variables

| Variable | Meaning |
|---|---|
| `Trigger.new` | new versions (insert/update) |
| `Trigger.old` | previous versions (update/delete) |
| `Trigger.newMap` | `Map<Id, sObject>` of new |
| `Trigger.oldMap` | `Map<Id, sObject>` of old |
| `Trigger.isBefore/isAfter` | timing |
| `Trigger.isInsert/isUpdate/...` | the event |

The classic pattern: compare `Trigger.oldMap.get(a.Id)` to `a` to detect **what changed**.

---

## 4. The cardinal rules

1. **One trigger per object.** Multiple triggers on the same object have **no guaranteed order**
   — consolidate.
2. **No SOQL/DML in loops.** Bulkify (Lesson 08).
3. **Keep logic out of the trigger.** The trigger should just **delegate** to a handler class.

```apex
trigger AccountTrigger on Account (before insert, after update) {
    new AccountTriggerHandler().run();   // logic lives in the handler
}
```

---

## 5. The handler / framework pattern

A **trigger framework** routes each context to a method and keeps triggers thin:

```apex
public class AccountTriggerHandler {
    public void run() {
        if (Trigger.isBefore && Trigger.isInsert) beforeInsert(Trigger.new);
        if (Trigger.isAfter  && Trigger.isUpdate) afterUpdate(Trigger.newMap, Trigger.oldMap);
    }
    private void beforeInsert(List<Account> news) { … }
    private void afterUpdate(Map<Id,Account> n, Map<Id,Account> o) { … }
}
```

This makes logic **testable** (you can call the handler directly) and **ordered**.

---

## 6. Recursion control

A trigger that does DML can re-fire itself. Guard with a **static flag**:

```apex
public class TriggerGuard { public static Boolean ran = false; }
// in handler:
if (TriggerGuard.ran) return;
TriggerGuard.ran = true;
```

Because `static` lives for the whole transaction, this stops infinite loops.

---

## 🎤 Say this in the interview

- *"**One trigger per object**, logic in a **handler class**, and everything **bulkified** for
  200 records."*
- *"**before** = validate/default in place; **after** = work with saved records that have Ids
  and touch related data."*
- *"I detect changes via **`Trigger.oldMap`** and prevent re-entry with a **static recursion
  flag**."*

➡️ **Next:** [08 — Governor limits & bulkification](./08_Governor_Limits.md)
