# 08 — Governor Limits & Bulkification

## 🧠 The One Idea

**Governor limits are speed bumps in a shared parking lot.** Because thousands of customers
share Salesforce's servers, no one is allowed to floor it. Salesforce caps how many queries,
DML statements, records, and CPU-milliseconds *each transaction* may use. **Bulkification** is
simply driving within those bumps: write code once that handles **many records together**
instead of one-at-a-time.

The one-liner: **"Governor limits cap per-transaction resource use; bulkification is how I stay
under them."**

---

## 1. The limits you must memorize (synchronous)

| Resource | Limit |
|---|---|
| SOQL queries | **100** |
| Records retrieved by SOQL | **50,000** |
| DML statements | **150** |
| Records processed by DML | **10,000** |
| SOSL queries | 20 |
| Callouts | 100 |
| CPU time | **10,000 ms** |
| Heap size | 6 MB |

> **Asynchronous** contexts (Batch/Queueable/Future) get **higher** limits — e.g., 200 SOQL,
> 60,000 ms CPU. That's a key reason to go async (Lesson 09).

---

## 2. Why limits exist (say this)

Multitenancy. Your runaway loop must never degrade a neighbor's org, so the platform **kills**
your transaction with a **`LimitException`** the moment you cross a cap — and rolls it back.
You can't catch your way out of it; you **design** your way out.

---

## 3. The #1 anti-pattern: work inside loops

```apex
// ❌ BAD — a query AND a DML per record. 200 contacts → 200 queries, 200 DMLs.
for (Contact c : Trigger.new) {
    Account a = [SELECT Id, Name FROM Account WHERE Id = :c.AccountId]; // query in loop!
    c.Description = a.Name;
}
```

This works for 1 record in a demo and **explodes in production**.

---

## 4. The bulkified version

**Pattern: query once into a Map, loop in memory, DML once.**

```apex
// 1) collect the parent Ids
Set<Id> acctIds = new Set<Id>();
for (Contact c : Trigger.new) acctIds.add(c.AccountId);

// 2) ONE query, keyed by Id
Map<Id, Account> byId = new Map<Id, Account>(
    [SELECT Id, Name FROM Account WHERE Id IN :acctIds]);

// 3) loop in memory, no DML/SOQL inside
for (Contact c : Trigger.new) {
    Account a = byId.get(c.AccountId);
    if (a != null) c.Description = a.Name;
}
// (before trigger → no DML needed; otherwise collect a list and DML once)
```

One query and (at most) one DML, **no matter how many records**.

---

## 5. CPU time & heap

- **CPU time (10s)** is the sneaky one: nested loops over large collections burn it. Prefer
  **Maps for O(1) lookups** over nested `for` loops (O(n²)).
- **Heap (6 MB)** fills if you load too many big records at once — use **SOQL for-loops** that
  chunk results, or move to **Batch Apex**.

```apex
for (Account a : [SELECT Id FROM Account]) { … }  // streams in chunks of 200
```

---

## 6. A bulkification checklist

- ✅ No SOQL inside loops. ✅ No DML inside loops.
- ✅ Use **Maps** to relate records, not nested loops.
- ✅ Build a **List**, then one DML.
- ✅ Test with **200+ records**, not just 1.
- ✅ For huge volumes or higher limits → **async** (Lesson 09).

---

## 🌍 Real-World Example

**A data migration imports 500,000 Contacts and a trigger silently kills it.** The `ContactTrigger`
had a single innocent-looking line — a SOQL query inside the loop to fetch each Contact's Account.
For 1 record in a sandbox demo it worked; at 200 records per batch it hit **101 SOQL queries** and
threw `System.LimitException: Too many SOQL queries: 101`, failing the entire load.

The fix is the bulkified pattern from §4: collect the `AccountId`s, run **one** query into a
`Map<Id, Account>`, then loop in memory. The same trigger now processes the full 500k import
without ever crossing a limit — because each 200-record batch uses exactly **1** query.

---

## 🔬 Under the Hood (In-Depth)

- **Limits are per-execution-context, not per-org** — each trigger invocation, batch chunk, or web
  request gets a **fresh** counter. This is why Batch Apex (Lesson 09) can process millions of rows:
  every `execute()` chunk resets the budget.
- **Sync vs async caps** — async contexts roughly **double** several limits (e.g., 200 SOQL,
  **60,000 ms** CPU, **12 MB** heap). Moving heavy work async is often the cleanest fix.
- **CPU time excludes waiting** — the 10,000 ms CPU clock counts **your** code (loops, parsing,
  serialization) but **not** time spent waiting on SOQL/DML/callouts. Nested loops and big JSON
  parses are the usual culprits.
- **`Limits` class for self-defense** — defensive code checks `Limits.getQueries()` vs
  `Limits.getLimitQueries()` to bail out or re-queue before hitting a wall.
- **Map lookups are O(1)** — replacing a nested `for` (O(n²)) with a `Map.get()` is the single
  biggest CPU win; at 200×200 that's 40,000 iterations vs 200.
- **Heap holds live objects** — large query results, big strings, and base64 blobs accumulate;
  SOQL for-loops chunk results to 200 to keep heap flat.

---

## 🎤 Say this in the interview

- *"Governor limits exist because Salesforce is **multitenant**; the big ones are **100 SOQL,
  150 DML, 50k rows, 10k CPU ms** per sync transaction."*
- *"**Bulkification** = query once into a **Map**, loop in memory, DML once on a **List** — and
  test with 200 records."*
- *"Hitting a limit throws a **LimitException** that I can't catch around; I move heavy work to
  **async**, which has higher limits."*

➡️ **Next:** [09 — Asynchronous Apex](./09_Asynchronous_Apex.md)
