# 05 — DML & Transactions

## 🧠 The One Idea

**DML is the "Save" button in code.** SOQL *reads* the database; **DML** (Data Manipulation
Language) *changes* it: `insert`, `update`, `delete`, `upsert`, `undelete`, `merge`. And every
execution runs as a **transaction** — like a shopping cart that either checks out completely or
not at all. If anything fails partway, the whole thing **rolls back** so you never get
half-saved data.

The one-liner: **"DML writes records; the whole execution is one all-or-nothing transaction."**

---

## 1. The DML statements

```apex
Account a = new Account(Name = 'Acme');
insert a;                       // create

a.Industry = 'Tech';
update a;                       // modify

upsert a Account.Id;            // insert or update by Id (or an external Id)

delete a;                       // recycle bin (recoverable)
undelete a;                     // restore from recycle bin
```

**`upsert`** is the handy one: "create if new, update if it already exists" — often keyed on an
**External Id** field for integrations.

---

## 2. Always do DML in bulk

The single biggest beginner mistake:

```apex
// ❌ BAD: DML inside a loop → hits the 150-statement limit fast
for (Account a : accounts) { update a; }

// ✅ GOOD: collect, then one DML on the whole list
List<Account> toUpdate = new List<Account>();
for (Account a : accounts) { a.Rating = 'Hot'; toUpdate.add(a); }
update toUpdate;                 // one DML for all records
```

Limit: **150 DML statements** per transaction, but each statement can handle **up to 10,000
records**. So operate on **lists**, not single records.

---

## 3. Statements vs the Database methods

Two ways to do DML:

```apex
insert accounts;                              // throws on ANY failure (all-or-nothing)

Database.SaveResult[] rs =
    Database.insert(accounts, false);         // allOrNone = false → partial success
for (Database.SaveResult r : rs) {
    if (!r.isSuccess()) { /* inspect r.getErrors() */ }
}
```

- **DML statement** (`insert x;`) → all-or-nothing; one bad record fails the batch.
- **`Database.insert(x, false)`** → **partial success**; good records save, you inspect
  failures per-record. Great for integrations.

---

## 4. Transactions, savepoints & rollback

Everything in one execution context shares **one transaction**. You can set a **savepoint** and
roll back to it:

```apex
Savepoint sp = Database.setSavepoint();
try {
    insert bigChange;
} catch (Exception e) {
    Database.rollback(sp);      // undo to the savepoint
}
```

An **uncaught exception** rolls back the *entire* transaction automatically — including DML
already done earlier in the same context.

---

## 5. The order of execution (why "saved" is complex)

When you save a record, Salesforce runs a long **order of execution**: validation rules,
**before triggers**, system validations, **after triggers**, assignment/auto-response/workflow
rules, **flows**, roll-up summaries, then commit. Knowing roughly this order explains
mysterious behavior like "why did my field value change after the trigger?"

---

## 6. DML you can't mix freely

- You can't perform DML on **setup objects** (e.g., `User`, `Group` membership) in the same
  transaction as non-setup objects without care (mixed DML error) — split into async.
- DML and **callouts** can't be interleaved carelessly: do callouts **before** uncommitted DML,
  or use async (Lesson 12).

---

## 🌍 Real-World Example

**A nightly integration syncs 10,000 orders from an ERP.** Some rows have bad data. If you used a
plain `insert orders;`, **one bad record fails all 10,000**. Instead, use partial success so good
records still save and you log the failures for a retry queue:

```apex
Database.SaveResult[] results = Database.insert(orders, false);   // allOrNone = false
List<Error_Log__c> failures = new List<Error_Log__c>();
for (Integer i = 0; i < results.size(); i++) {
    if (!results[i].isSuccess()) {
        failures.add(new Error_Log__c(
            Payload__c = JSON.serialize(orders[i]),
            Message__c = results[i].getErrors()[0].getMessage()));
    }
}
if (!failures.isEmpty()) insert failures;
```

This is the standard pattern for resilient integrations: **partial save + dead-letter log**.

---

## 🔬 Under the Hood (In-Depth)

- **The order of execution** — on save, Salesforce runs a fixed sequence: system validation →
  **before** triggers → custom validation rules → duplicate rules → save (not committed) →
  **after** triggers → assignment/auto-response/workflow field updates → **flows** → roll-up
  summaries → **commit**. Knowing this explains "why did my value change after my trigger ran?"
- **Workflow field updates re-fire triggers** — a workflow/flow field update **re-runs** before &
  after triggers (once), a frequent source of recursion.
- **Governor cost** — the limit is **150 DML *statements***, not records; one statement can touch
  **10,000 rows**. So `update bigList;` is one statement — `update` in a loop is the killer.
- **Savepoints aren't free** — each `Database.setSavepoint()` consumes from the DML-statement
  limit and snapshots state; rolling back restores records but **not** `static` variables or sent
  emails.
- **Mixed DML** — you can't DML **setup objects** (`User`, `Group`, `PermissionSetAssignment`) and
  non-setup objects in the same transaction; split the setup DML into a `@future`/Queueable.
- **Implicit rollback** — an **uncaught** exception rolls the *entire* transaction back; a
  **caught** one does not, so already-done DML stays unless you roll back to a savepoint.

---

## 🎤 Say this in the interview

- *"DML writes records and runs as **one all-or-nothing transaction**; an uncaught exception
  **rolls everything back**."*
- *"I **bulkify**: build a list and do **one DML on the list**, never DML in a loop (150-stmt
  limit)."*
- *"For partial success I use **`Database.insert(list, false)`** and inspect each
  **SaveResult**; for transactional safety I use **savepoints**."*

➡️ **Next:** [06 — Classes, OOP & control flow](./06_Classes_And_OOP.md)
