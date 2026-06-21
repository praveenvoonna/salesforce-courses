# 🗄️ Data Cloud From Scratch — A Crash Course (in plain English)

A from-zero deep dive into **Salesforce Data Cloud** (recently rebranded **Data 360**), the
platform's customer data platform (CDP): *what it is, how data flows through it, and how it powers
segmentation, analytics, and AI* — explained in **naive, everyday language** with analogies, then
the real mechanics, then **interview-ready lines**.

> **How to read this:** go in order, 00 → 14. Each lesson starts with a plain-English analogy
> (**"The One Idea"**), then the real details, then **"Say this in the interview"** one-liners
> you can repeat almost verbatim. Don't skip the analogies — they're the hooks that make the
> rest stick.
>
> **Naming note:** Salesforce now brands this **Data 360**; most people (and most interviews)
> still say **Data Cloud**. This course uses them interchangeably.

---

## 📂 The lessons (read in order)

### Part A — The mental model
- **[00 — What is Data Cloud (a CDP)](./00_What_Is_Data_Cloud.md)** — the problem of scattered
  customer data.
- **[01 — Architecture & core concepts](./01_Architecture_And_Concepts.md)** — the lakehouse,
  data spaces, the pipeline.

### Part B — Getting data in & modeling it
- **[02 — Data streams & ingestion](./02_Data_Streams_And_Ingestion.md)** — connectors, batch vs
  streaming.
- **[03 — The data model: DLO, DSO & DMO](./03_Data_Model_DLO_DMO.md)** — the three object layers.
- **[04 — Data mapping & transformation](./04_Mapping_And_Transformation.md)** — harmonizing to
  the Customer 360 model.

### Part C — Unify & enrich
- **[05 — Identity resolution](./05_Identity_Resolution.md)** — building the unified profile.
- **[06 — Calculated insights](./06_Calculated_Insights.md)** — metrics & KPIs (LTV, CSAT).

### Part D — Act on the data
- **[07 — Segmentation](./07_Segmentation.md)** — building audiences.
- **[08 — Activation](./08_Activation.md)** — sending segments to where they're used.
- **[09 — Querying (SQL & Query API)](./09_Querying.md)** — exploring data.
- **[10 — Data actions & integrations](./10_Data_Actions_And_Integrations.md)** — events, flows,
  zero-copy.

### Part E — Trust & AI
- **[11 — Privacy, consent & governance](./11_Privacy_And_Governance.md)** — doing it responsibly.
- **[12 — Data Cloud + Einstein & Agentforce](./12_Data_Cloud_And_AI.md)** — grounding AI in your
  data.

### Part F — Practice
- **[13 — Hands-on lab](./13_Hands_On_Lab.md)** — ingest → map → unify → segment → activate.
- **[14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)** — rapid-fire Q&A.

---

## 🧠 The whole course in three sentences

1. **Data Cloud unifies scattered customer data into one profile** — it ingests from every
   source, harmonizes it to a common model, and uses **identity resolution** to merge duplicates
   into a single **unified individual**.
2. **The data model has three layers** — raw **DLOs** (ingested), **DSOs** (normalized streams),
   and harmonized **DMOs** (the shared Customer 360 model the rest of Salesforce queries).
3. **Once unified, you act on it** — compute **calculated insights**, build **segments**, and
   **activate** them to marketing, sales, ads, and **ground AI** (Einstein/Agentforce) in real
   customer context.

If you can say those three sentences and explain each, you've got the backbone.

---

## 🛠️ Tools for the lab (Lesson 13)
- A **Data Cloud–enabled org or trial** (Trailhead provides hands-on orgs).
- Sample CSV/data and access to **Data Explorer**, **Segmentation**, and **Activation** UIs.

You've got this. Start at **[00](./00_What_Is_Data_Cloud.md)**.
