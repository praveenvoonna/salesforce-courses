# ⚙️ Apex From Scratch — A Crash Course (in plain English)

A from-zero deep dive into **Apex**, Salesforce's server-side programming language: *what it
is, where it runs, and how to write it well* — explained in **naive, everyday language** with
analogies, then the real mechanics, then **interview-ready lines**.

> **How to read this:** go in order, 00 → 14. Each lesson starts with a plain-English analogy
> (**"The One Idea"**), then the real details, then **"Say this in the interview"** one-liners
> you can repeat almost verbatim. Don't skip the analogies — they're the hooks that make the
> rest stick.

---

## 📂 The lessons (read in order)

### Part A — The mental model (don't skip)
- **[00 — What is Salesforce & the platform](./00_What_Is_Salesforce.md)** — orgs, metadata,
  multitenancy, and why Apex even exists.
- **[01 — What is Apex & when to use it](./01_What_Is_Apex.md)** — Java-like, on-platform,
  and "clicks vs code".

### Part B — The language
- **[02 — Apex language basics](./02_Language_Basics.md)** — types, variables, collections,
  loops, and conditionals.
- **[03 — sObjects & the data model](./03_sObjects_And_Data_Model.md)** — objects, fields,
  records, and relationships.

### Part C — Talking to the database
- **[04 — SOQL & SOSL](./04_SOQL_And_SOSL.md)** — querying records the Salesforce way.
- **[05 — DML & transactions](./05_DML_And_Transactions.md)** — insert/update/delete, savepoints,
  rollbacks.

### Part D — Structuring real code
- **[06 — Classes, OOP & control flow](./06_Classes_And_OOP.md)** — interfaces, inheritance,
  access modifiers.
- **[07 — Triggers & trigger frameworks](./07_Triggers.md)** — reacting to data changes the
  right way.

### Part E — The hard parts (where interviews live)
- **[08 — Governor limits & bulkification](./08_Governor_Limits.md)** — the #1 Apex topic.
- **[09 — Asynchronous Apex](./09_Asynchronous_Apex.md)** — Future, Queueable, Batch, Scheduled.
- **[10 — Testing Apex](./10_Testing_Apex.md)** — test classes, mocks, the 75% rule.
- **[11 — Security & sharing](./11_Security_And_Sharing.md)** — `with sharing`, CRUD/FLS, injection.
- **[12 — Integration & callouts](./12_Integration_And_Callouts.md)** — REST/SOAP, inbound &
  outbound.

### Part F — Practice
- **[13 — Hands-on lab](./13_Hands_On_Lab.md)** — build a small, bulk-safe, tested feature.
- **[14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)** — rapid-fire questions
  with crisp answers.

---

## 🧠 The whole course in three sentences

1. **Apex is a Java-like language that runs *inside* Salesforce's servers, right next to the
   database** — so querying and saving records is built into the language.
2. **Because thousands of customers share the same servers (multitenancy), Salesforce enforces
   strict "governor limits"** — your code must be **bulk-safe** (handle many records at once)
   or it will fail.
3. **You can't ship Apex to production without tests** — at least 75% code coverage — so testing
   and writing efficient, secure code are first-class skills, not afterthoughts.

If you can say those three sentences and explain each, you've got the backbone.

---

## 🛠️ Tools for the lab (Lesson 13)
- A **Salesforce Developer Edition org** (free) and the **Salesforce CLI (`sf`)**.
- **VS Code** with the **Salesforce Extension Pack**, or the in-browser **Developer Console**.

You've got this. Start at **[00](./00_What_Is_Salesforce.md)**.
