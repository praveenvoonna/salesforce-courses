# 02 — Apex Language Basics

## 🧠 The One Idea

**Apex is "Java with the boring parts removed and a database bolted on."** If you can read
basic Java, JavaScript, or C#, you already know 80% of Apex. The trick is learning the few
Salesforce-specific flavors: its three workhorse **collections** (List, Set, Map) and the fact
that everything is **case-insensitive**.

The one-liner: **"Apex is a strongly-typed, case-insensitive, Java-like language."**

---

## 1. Variables & primitive types

```apex
Integer count = 5;
Decimal price = 19.99;        // exact — use for money
Double ratio = 0.5;           // floating point
String name = 'Alice';
Boolean isActive = true;
Date today = Date.today();
Datetime now = Datetime.now();
Id recordId = '001xx000003D…';  // a special 15/18-char Salesforce key
```

- Use **`Decimal`** for currency (no floating-point rounding surprises).
- **`Id`** is its own type — a record's primary key.
- Apex is **case-insensitive**: `Account` and `account` are the same identifier.

---

## 2. Collections — the three you must know

| Type | Analogy | Use when |
|---|---|---|
| **List** | a numbered shopping list (ordered, duplicates OK) | you have many records in order |
| **Set** | a guest list (unique, unordered) | you need uniqueness / fast "contains" |
| **Map** | a phone book (key → value) | you need fast lookup by a key |

```apex
List<String> names = new List<String>{ 'A', 'B', 'A' };  // [A, B, A]
Set<Id> ids = new Set<Id>();                              // no duplicates
Map<Id, Account> byId = new Map<Id, Account>();           // key → record
```

> **Map keyed by Id** is the single most useful pattern in Apex — you'll use it constantly to
> relate parent and child records without extra queries.

---

## 3. Control flow

```apex
for (Account a : accounts) {        // "for-each" — the common form
    if (a.AnnualRevenue > 1000000) {
        a.Rating = 'Hot';
    } else {
        a.Rating = 'Warm';
    }
}

Integer i = 0;
while (i < 10) { i++; }
```

Apex also has the classic `for (Integer i=0; i<n; i++)` and a special **SOQL for-loop** that
streams query results in batches (great for limits — Lesson 08).

---

## 4. Strings, math & useful built-ins

```apex
String s = 'Hello World';
s.toLowerCase(); s.contains('World'); s.split(' ');
Math.max(3, 7); Math.round(2.6);
System.debug('value = ' + s);   // prints to the debug log
```

`System.debug()` is your `console.log` — it writes to the **debug log**, the main way you
inspect what code did.

---

## 5. Exceptions

```apex
try {
    insert new Account();           // missing required Name → error
} catch (DmlException e) {
    System.debug('Failed: ' + e.getMessage());
}
```

Common types: **`DmlException`**, **`NullPointerException`**,
**`QueryException`**, **`LimitException`** (governor limit hit — *cannot* be caught usefully
and rolled back like normal errors). You can define custom exceptions:
`public class MyException extends Exception {}`.

---

## 6. A few gotchas

- A SOQL query returning **zero rows assigned to a single sObject** throws — use a `List`.
- `null` is everywhere; guard before dereferencing (`a?.Owner?.Name` safe navigation helps).
- Integer division truncates: `5 / 2 == 2`; use `Decimal` for fractions.

---

## 🌍 Real-World Example

**Deduplicating a marketing list of 50,000 Leads before a campaign.** The data team loads leads
from three sources and needs to keep only the newest record per email:

```apex
Map<String, Lead> latestByEmail = new Map<String, Lead>();
for (Lead l : incomingLeads) {
    if (l.Email == null) continue;
    String key = l.Email.toLowerCase();                 // normalize
    Lead seen = latestByEmail.get(key);
    if (seen == null || l.CreatedDate > seen.CreatedDate) {
        latestByEmail.put(key, l);                       // keep the newest
    }
}
List<Lead> deduped = latestByEmail.values();
```

Picking the **right collection** (a `Map` keyed by email) turns what would be an O(n²)
nested-loop scan — which would blow the **CPU limit** at 50k records — into a single O(n) pass.

---

## 🔬 Under the Hood (In-Depth)

- **Value vs reference types** — primitives (`Integer`, `Boolean`, `Date`) are passed **by value**;
  sObjects and collections are passed **by reference**, so a method that mutates a `List` argument
  changes the caller's list too.
- **`Decimal` vs `Double`** — `Decimal` is arbitrary-precision (backed by Java `BigDecimal`) and
  tracks **scale**, so `19.99` stays exact for money. `Double` is IEEE-754 floating point and can
  produce rounding drift — never use it for currency.
- **Strings are immutable** — every concatenation creates a new object on the **heap** (6 MB
  limit), so building big strings in a loop is a hidden heap/CPU cost; use a `List<String>` +
  `String.join`.
- **`Map`/`Set` semantics** — they rely on `hashCode`/`equals`. For sObjects, equality compares
  **all loaded fields**, which is why a `Set<Account>` can behave surprisingly; prefer
  `Set<Id>`/`Map<Id, …>`.
- **Integer math** — division truncates (`5/2 == 2`) and overflow silently **wraps** at 2³¹; use
  `Long`/`Decimal` for large or fractional values.

---

## 🎤 Say this in the interview

- *"The three collections are **List** (ordered), **Set** (unique), and **Map** (key→value);
  a **Map<Id, sObject>** is my go-to for relating records without extra queries."*
- *"I use **Decimal** for money to avoid floating-point errors, and **Id** is a first-class
  type."*
- *"A **LimitException** signals a governor limit and effectively ends the transaction — you
  design to avoid it, not catch it."*

➡️ **Next:** [03 — sObjects & the data model](./03_sObjects_And_Data_Model.md)
