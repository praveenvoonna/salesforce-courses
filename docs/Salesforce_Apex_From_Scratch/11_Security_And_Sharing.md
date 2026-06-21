# 11 — Security & Sharing

## 🧠 The One Idea

**By default, Apex is a master key — and that's dangerous.** Unlike the UI, Apex normally runs
in **system mode**: it ignores who the user is and can see/edit *everything*. Security in Apex
is about **deliberately putting the locks back on** so your code only does what the **running
user** is actually allowed to do. Salesforce security has three layers: **records** (sharing),
**objects** (CRUD), and **fields** (FLS).

The one-liner: **"Apex runs in system mode by default; I re-impose record, object, and
field-level security explicitly."**

---

## 1. The three layers

| Layer | Question | Controlled by |
|---|---|---|
| **Record (sharing)** | *Which rows* can this user see? | org-wide defaults, role hierarchy, sharing rules |
| **Object (CRUD)** | Can they Create/Read/Update/Delete this object? | profiles & permission sets |
| **Field (FLS)** | Can they see/edit *this field*? | profiles & permission sets |

---

## 2. `with sharing` vs `without sharing`

```apex
public with sharing class SafeService { … }      // respects the user's record access
public without sharing class AdminJob  { … }      // ignores sharing (system mode)
public inherited sharing class Flexible { … }      // takes caller's sharing mode
```

- **`with sharing`** = enforce who-can-see-which-records (sharing rules).
- **`without sharing`** = bypass sharing (use sparingly, on purpose).
- **`inherited sharing`** = safe default for reusable libraries: behaves as the caller does.

> ⚠️ `with sharing` enforces **record** access only — it does **not** enforce CRUD/FLS. You
> handle those separately.

---

## 3. Enforcing CRUD & FLS

**Option A — `WITH USER_MODE` / `WITH SECURITY_ENFORCED` in SOQL:**

```apex
List<Account> a = [SELECT Id, Name FROM Account WITH USER_MODE];   // checks CRUD+FLS+sharing
```

**Option B — `Database` operations in user mode:**

```apex
List<Account> a = Database.query(q, AccessLevel.USER_MODE);
Database.insert(records, AccessLevel.USER_MODE);
```

**Option C — `Security.stripInaccessible()`** removes fields the user can't access:

```apex
SObjectAccessDecision d = Security.stripInaccessible(AccessType.READABLE, records);
List<SObject> safe = d.getRecords();
```

**Option D — manual describe checks:** `Schema.sObjectType.Account.isCreateable()` etc.

`USER_MODE` (modern) is the cleanest — it enforces **CRUD, FLS, and sharing** together.

---

## 4. SOQL/SOSL injection

Concatenating user input into a dynamic query is the classic vulnerability:

```apex
// ❌ vulnerable
String q = 'SELECT Id FROM Account WHERE Name = \'' + userInput + '\'';
// ✅ use bind variables
String q = 'SELECT Id FROM Account WHERE Name = :userInput';
// ✅ or escape if you must concatenate
String safe = String.escapeSingleQuotes(userInput);
```

Prefer **bind variables**; fall back to `escapeSingleQuotes()` only when forced.

---

## 5. Other security notes

- **`@AuraEnabled` Apex** (called from LWC) runs as the user but **still defaults to ignoring
  CRUD/FLS** — enforce them yourself.
- Store secrets in **Named Credentials** / **Protected Custom Metadata**, never hard-coded.
- Test security with **`System.runAs(user)`** to simulate a real user's permissions.

---

## 🎤 Say this in the interview

- *"Apex defaults to **system mode**, so I enforce security explicitly: **sharing** for records,
  **CRUD/FLS** for objects/fields — increasingly via **`WITH USER_MODE`** / `AccessLevel.USER_MODE`."*
- *"**`with sharing`** only enforces **record** access, not CRUD/FLS — that's a common gotcha."*
- *"I prevent SOQL injection with **bind variables**, falling back to **`escapeSingleQuotes`**,
  and I test permissions with **`runAs`**."*

➡️ **Next:** [12 — Integration & callouts](./12_Integration_And_Callouts.md)
