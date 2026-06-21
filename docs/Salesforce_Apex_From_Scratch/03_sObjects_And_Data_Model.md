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

## 🎤 Say this in the interview

- *"Objects are tables, records are rows, fields are columns; custom ones end in **`__c`** and
  custom relationships in **`__r`**."*
- *"**Master-detail** is a tight, cascade-delete, sharing-inheriting relationship that enables
  **roll-up summaries**; **lookup** is loose and independent."*
- *"Many-to-many is modeled with a **junction object** that has two master-detail
  relationships."*

➡️ **Next:** [04 — SOQL & SOSL](./04_SOQL_And_SOSL.md)
