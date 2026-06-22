# 03 — sObjects & the Data Model

## 🧠 The One Idea

**An sObject is a spreadsheet, a record is a row, and a field is a column.** Salesforce's
database is just a collection of tables called **objects**. "Account", "Contact", "Opportunity"
are objects (tables); each saved customer is a **record** (row); each piece of data like
`Name` or `Email` is a **field** (column). In Apex, an **sObject** is the in-memory
representation of one row.

The one-liner: **"An sObject is a typed row of a Salesforce table that I can read and write in
Apex."**

---

## 1. Standard vs custom objects

- **Standard objects** ship with Salesforce: `Account`, `Contact`, `Lead`, `Opportunity`,
  `Case`, `User`.
- **Custom objects** you create end in **`__c`**: `Invoice__c`, `Project__c`.
- Custom **fields** also end in `__c`: `Account.Region__c`.

That `__c` suffix is how you instantly tell "custom" from "standard" in code.

---

## 2. Working with records in Apex

```apex
Account a = new Account(Name = 'Acme', Industry = 'Tech');  // in memory only
insert a;                                                   // now saved; a.Id is set

a.Industry = 'Finance';
update a;

Account fetched = [SELECT Id, Name, Industry FROM Account WHERE Id = :a.Id];
System.debug(fetched.Name);
```

You only get fields you **explicitly query** — touching an unqueried field throws. This forces
you to be deliberate about what you load.

---

## 3. Relationships — how tables connect

Two kinds, and the difference matters in interviews:

| | **Lookup** | **Master-Detail** |
|---|---|---|
| Coupling | loose | tight (child owned by parent) |
| Child without parent? | allowed | **not** allowed (required) |
| Delete parent | child stays (or set null) | child is **deleted too** (cascade) |
| Sharing/security | independent | child **inherits** parent's |
| Roll-up summary fields | ❌ | ✅ |

A **junction object** = a custom object with **two master-detail** relationships, used to model
**many-to-many** (e.g., `Student__c` ↔ `Course__c` via `Enrollment__c`).

---

## 4. Traversing relationships in code

```apex
// Child → parent: use the relationship name and dot down
Contact c = [SELECT Id, Name, Account.Name, Account.Industry
             FROM Contact WHERE Id = :someId];
System.debug(c.Account.Name);            // parent field via dot

// Parent → children: a subquery using the child relationship name
Account acc = [SELECT Id, Name,
                 (SELECT LastName FROM Contacts)
               FROM Account WHERE Id = :accId];
for (Contact child : acc.Contacts) { … }
```

- **Parent** relationship via lookup field: `Account` (custom: `MyParent__r`).
- **Child** relationship name in subqueries: `Contacts` (custom: `MyChildren__r`).

The `__r` suffix means "the related record(s)" for custom relationships.

---

## 5. Describe & dynamic access

You can inspect metadata at runtime ("describe") and access fields dynamically:

```apex
Schema.DescribeSObjectResult d = Account.SObjectType.getDescribe();
Boolean canEdit = d.isUpdateable();
a.put('Name', 'Dynamic');         // set field by API name
Object v = a.get('Industry');     // read field by API name
```

This powers generic, reusable code (and security checks — Lesson 11).

---

## 🌍 Real-World Example

**Modeling course enrollment for a university.** A student can take many courses and a course has
many students — a classic **many-to-many**. You model it with a **junction object**:

- `Student__c` and `Course__c` are the two ends.
- `Enrollment__c` sits between them with **two master-detail** fields (`Student__c`, `Course__c`).

Now you get powerful behavior for free: a **roll-up summary** on `Student__c` can sum
`Credits__c` across all enrollments, and deleting a `Course__c` **cascades** — every related
`Enrollment__c` is removed automatically, so you never leave orphaned rows.

---

## 🔬 Under the Hood (In-Depth)

- **Relationship fields store an Id** — a lookup/master-detail field physically holds the
  18-character Id of the related row; it's a foreign key the platform indexes.
- **Master-detail is a stricter FK** — it adds **required parent**, **ownership/sharing
  inheritance**, and **cascade delete**. Limits: **max 2** master-detail and **up to 40 lookups**
  per object; a junction's *first* MD controls sharing and the detail's owner.
- **Polymorphic relationships** — some fields point to **multiple object types**: `Task.WhatId`
  (Account/Opportunity/…), `OwnerId` (User or Queue). Query them with `TYPEOF` in SOQL.
- **External Ids & upsert** — marking a field as **External Id** lets `upsert` match on it instead
  of the Salesforce Id, which is how integrations sync without storing internal Ids.
- **Only queried fields are populated** — an sObject in memory holds *just* the fields you
  `SELECT`. Touching an unqueried field throws **`SObjectException: SObject row was retrieved via
  SOQL without querying the requested field`** — a very common runtime error.
- **Describe is metadata at runtime** — `Schema.getGlobalDescribe()` and `SObjectType.getDescribe()`
  read the data model live, but they're **expensive**; cache the result rather than calling per row.

---

## 🎤 Say this in the interview

- *"Objects are tables, records are rows, fields are columns; custom ones end in **`__c`** and
  custom relationships in **`__r`**."*
- *"**Master-detail** is a tight, cascade-delete, sharing-inheriting relationship that enables
  **roll-up summaries**; **lookup** is loose and independent."*
- *"Many-to-many is modeled with a **junction object** that has two master-detail
  relationships."*

➡️ **Next:** [04 — SOQL & SOSL](./04_SOQL_And_SOSL.md)
