# 04 — SOQL & SOSL

## 🧠 The One Idea

**SOQL is SQL that already knows your tables and only lets you SELECT.** It looks like SQL but
there's no `SELECT *`, no arbitrary JOINs, and no `UPDATE/DELETE` (that's DML's job — Lesson
05). You always name the object and the exact fields. **SOSL** is the other tool: a
full-text **search** box across many objects at once — like Google for your org.

The one-liner: **"SOQL queries one object's records precisely; SOSL searches text across many
objects."**

---

## 1. SOQL basics

```apex
List<Account> accts = [
    SELECT Id, Name, Industry, AnnualRevenue
    FROM Account
    WHERE Industry = 'Tech' AND AnnualRevenue > 1000000
    ORDER BY AnnualRevenue DESC
    LIMIT 50
];
```

- You **must** list fields — there is **no `SELECT *`**.
- The query returns a `List<Account>`; assigning to a single `Account` requires **exactly one**
  row or it throws.

---

## 2. Bind variables (the safe way to inject values)

```apex
String target = 'Tech';
List<Account> a = [SELECT Id FROM Account WHERE Industry = :target];
Set<Id> ids = new Set<Id>{ id1, id2 };
List<Contact> c = [SELECT Id FROM Contact WHERE AccountId IN :ids];
```

The **`:variable`** syntax is a **bind variable** — it's parameterized and immune to SOQL
injection. Always prefer it over string concatenation.

---

## 3. Relationship queries

```apex
// Parent fields via dot (child → parent)
SELECT Name, Account.Name, Account.Owner.Name FROM Contact

// Child records via subquery (parent → children)
SELECT Name, (SELECT LastName FROM Contacts) FROM Account
```

You can go **up to 5 levels** up via parent dots, and include subqueries for children. This
replaces most SQL JOINs.

---

## 4. Aggregates & grouping

```apex
List<AggregateResult> r = [
    SELECT Industry, COUNT(Id) total, AVG(AnnualRevenue) avgRev
    FROM Account
    GROUP BY Industry
    HAVING COUNT(Id) > 5
];
for (AggregateResult ar : r) {
    System.debug(ar.get('total'));
}
```

Aggregate queries return **`AggregateResult`**, not your sObject — read values with `.get()`.

---

## 5. Dynamic SOQL

When the query is built at runtime:

```apex
String q = 'SELECT Id FROM Account WHERE Name = :name';   // still bindable
List<Account> a = Database.query(q);
```

If you must concatenate user input, escape it with `String.escapeSingleQuotes()` — but **bind
variables are safer**. This is a classic security question (Lesson 11).

---

## 6. SOSL — searching text

```apex
List<List<SObject>> results = [
    FIND 'Acme*' IN NAME FIELDS
    RETURNING Account(Id, Name), Contact(Id, LastName)
];
List<Account> foundAccts = (List<Account>) results[0];
```

Use **SOSL** when you don't know which object holds the text, or you need fast full-text search
across many objects. Use **SOQL** when you know the object and want precise filters.

---

## 7. Querying & governor limits (preview of Lesson 08)

- **Max 100 SOQL queries** per synchronous transaction; **50,000 rows** returned total.
- The golden rule: **never put a SOQL query inside a loop.** Query once into a Map/List, then
  loop over the results in memory.

---

## 🌍 Real-World Example

**A support dashboard that finds "all open cases for a customer and their contacts."** Instead of
querying Cases, then looping to fetch each Contact, you do it in **one relationship query**:

```apex
Account a = [
    SELECT Id, Name,
           (SELECT Id, Subject, Status FROM Cases WHERE Status != 'Closed'),
           (SELECT Id, Name, Email FROM Contacts)
    FROM Account
    WHERE Id = :recordId
];
Integer openCases = a.Cases.size();
```

When a support agent types "Acme" into global search and isn't sure whether it's an Account,
Contact, or Case, **SOSL** is what runs behind the scenes — one full-text search across many
objects at once.

---

## 🔬 Under the Hood (In-Depth)

- **The query optimizer & selectivity** — every SOQL goes through Salesforce's **cost-based
  optimizer**. A filter is **selective** if it hits an **indexed** field returning a small
  fraction of rows. Non-selective filters on large objects throw
  **`QueryException: Non-selective query against large object type`** (the 200k-row guardrail).
- **Standard vs custom indexes** — Id, Name, OwnerId, lookups, External Ids, and `CreatedDate`
  are indexed by default. You can request **custom indexes**; `!=`, `NOT`, leading `%` wildcards,
  and formula fields generally **can't** use them.
- **Bind variables are pre-parsed** — `:var` is bound *before* execution, so it's immune to
  injection and lets the optimizer plan the query. String concatenation defeats both.
- **SOQL for-loops chunk results** — `for (Account a : [SELECT … ])` streams rows in batches of
  **200**, keeping heap low; a plain `List<Account> x = [ … ]` loads everything at once.
- **`QueryLocator` vs list** — `Database.getQueryLocator` (Batch Apex) can address up to **50
  million** rows, far beyond the 50k synchronous retrieval cap.
- **SOSL specifics** — search runs against a separate **search index** (eventually consistent, so
  brand-new records may lag), returns a `List<List<SObject>>` in `RETURNING` order, and caps at
  2,000 rows.

---

## 🎤 Say this in the interview

- *"SOQL has **no `SELECT *`** — I list fields explicitly and use **bind variables (`:var`)**
  to stay injection-safe and bulk-friendly."*
- *"**SOQL** = precise query on one object with relationships; **SOSL** = full-text search
  across multiple objects."*
- *"Aggregates return **AggregateResult**, and I **never query inside a loop** to respect the
  100-query limit."*

➡️ **Next:** [05 — DML & transactions](./05_DML_And_Transactions.md)
