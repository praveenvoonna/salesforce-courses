# 14 — Interview Q&A Flashcards

Rapid-fire. Cover the answer, say it aloud, then check. Read twice.

---

## Fundamentals

**Q: What is Apex?**
A strongly-typed, case-insensitive, Java-like language that runs **on-platform** with SOQL and
DML built into the syntax.

**Q: Why do governor limits exist?**
Salesforce is **multitenant** — many customers share infrastructure, so per-transaction caps
stop any one tenant from hogging resources.

**Q: Clicks vs code?**
Use declarative tools (Flow, validation rules) first; reach for Apex only when logic is too
complex, high-volume, or needs callouts/transaction control.

---

## Data model

**Q: Lookup vs master-detail?**
Lookup = loose, independent, child survives parent delete. Master-detail = tight, cascade
delete, child inherits sharing, enables **roll-up summaries**.

**Q: How do you model many-to-many?**
A **junction object** with two master-detail relationships.

**Q: What do `__c` and `__r` mean?**
`__c` = custom object/field; `__r` = the related record(s) in relationship queries.

---

## SOQL/DML

**Q: SOQL vs SOSL?**
SOQL = precise query on one object (with relationships); SOSL = full-text search across multiple
objects.

**Q: How do you avoid SOQL injection?**
**Bind variables** (`:var`); fall back to `String.escapeSingleQuotes()` if you must concatenate.

**Q: DML statement vs Database method?**
`insert x;` is all-or-nothing; `Database.insert(x, false)` allows **partial success** with
per-record `SaveResult`.

**Q: What happens on an uncaught exception mid-transaction?**
The **entire transaction rolls back**.

---

## Governor limits / bulkification

**Q: Key sync limits?**
**100 SOQL, 150 DML, 50,000 rows retrieved, 10,000 records per DML, 10,000 ms CPU.**

**Q: What is bulkification?**
Writing code to handle many records at once: query once into a **Map**, loop in memory, **DML
once** on a list; test with 200 records.

**Q: Biggest anti-pattern?**
SOQL or DML **inside a loop**.

---

## Triggers

**Q: before vs after trigger?**
before = modify records in place (validate/default), no DML. after = records saved with Ids;
work with related records.

**Q: Trigger best practices?**
**One trigger per object**, logic in a **handler class**, fully **bulkified**, with a **static
recursion guard**.

**Q: How detect what changed?**
Compare `Trigger.newMap` to `Trigger.oldMap`.

---

## Async

**Q: The four async types?**
**Future** (simple callout), **Queueable** (chainable, complex types), **Batch** (millions, per-chunk
limits), **Scheduled** (cron).

**Q: Why is Batch good for big data?**
Each chunk (`execute`) gets a **fresh set of governor limits**, so you process beyond the 50k-row
cap.

**Q: Future vs Queueable?**
Queueable accepts **sObjects/complex types**, returns a **Job Id**, and supports **chaining**;
Future is `static void` with primitives only.

---

## Testing

**Q: Coverage to deploy to production?**
**≥ 75%** org-wide and all tests pass; every trigger needs >0%.

**Q: What do Test.startTest/stopTest do?**
Give a fresh limit context and force **async jobs to run** at `stopTest()`.

**Q: How test callouts?**
Mock with **`HttpCalloutMock`** via `Test.setMock`.

**Q: How test permissions?**
**`System.runAs(user)`**.

---

## Security

**Q: Default Apex execution mode?**
**System mode** — ignores CRUD/FLS and (without `with sharing`) record access.

**Q: Does `with sharing` enforce FLS?**
No — only **record** access. Enforce CRUD/FLS separately (e.g., **`WITH USER_MODE`**,
`stripInaccessible`, describe checks).

---

## Integration

**Q: How do you authenticate callouts safely?**
**Named Credentials** — endpoint + auth as metadata, no hard-coded secrets.

**Q: Callout-after-DML rule?**
You can't call out after **uncommitted DML** in the same transaction — call out first or go
**async**.

**Q: How does an external system call Salesforce?**
**Apex REST** (`@RestResource`) / **SOAP** services, or standard REST/Bulk/Composite APIs;
event-driven via **Platform Events / CDC**.

---

🎉 That's the Apex course. Loop back to any lesson whose flashcard you couldn't answer cold.
