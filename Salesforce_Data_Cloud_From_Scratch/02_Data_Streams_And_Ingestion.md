# 02 — Data Streams & Ingestion

## 🧠 The One Idea

**A data stream is a pipe from a source into Data Cloud.** Each source — your CRM, your website,
a data warehouse, a CSV — gets its own pipe that defines *what* data comes in, *how often*, and
*what shape* it has. Ingestion is the first station on the assembly line, and getting it right
makes everything downstream easier.

The one-liner: **"A data stream is a configured pipe that ingests one source's data into a
DLO."**

---

## 1. What a data stream defines

- **Source/connector** — where the data comes from.
- **Object/fields** — which records and columns to bring.
- **Category** — Profile, Engagement, or Other (matters for modeling/unification).
- **Refresh** — how it updates (full refresh, upsert, streaming).
- **Primary key** & **record modified field** — so Data Cloud knows identity and recency.

The output of a data stream is a **DLO** (Data Lake Object) — the raw landing table.

---

## 2. The three data categories

| Category | Meaning | Examples |
|---|---|---|
| **Profile** | who the person/company is | Individual, Account, Contact |
| **Engagement** | time-stamped behavior/events | email opens, web clicks, purchases |
| **Other** | reference/lookup data | product catalog, store list |

**Engagement** data is time-series (has an event timestamp); **Profile** data describes
entities. This choice affects insights and segmentation.

---

## 3. Connectors (where data comes from)

- **Salesforce CRM connector** — Sales/Service objects (Accounts, Contacts, Cases…).
- **Marketing Cloud** connectors.
- **Web & Mobile SDK** — capture site/app behavior in real time.
- **Cloud storage / ingestion API** — Amazon S3, Google Cloud Storage, files, the **Ingestion
  API** (streaming + bulk) for any system.
- **Data warehouse / zero-copy** — Snowflake, BigQuery, Databricks, Redshift **without
  physically copying** the data (Lesson 10).

---

## 4. Batch vs streaming

- **Batch** — scheduled bulk loads (e.g., nightly CRM sync, daily file). Good for large reference
  and profile data.
- **Streaming** — near-real-time events via the Web/Mobile SDK or Ingestion API. Good for
  behavior that should influence the *next* interaction.

Many real setups mix both.

---

## 5. Starter bundles

Salesforce provides **starter data bundles** for common sources (e.g., CRM) that come with
**pre-built streams and pre-mapped fields**, so you're not modeling from scratch. You still map
custom fields yourself (Lesson 04).

---

## 6. Ingestion best practices

- Bring in **only the fields you need** — storage and processing cost money.
- Set the correct **primary key** and **modified date** so upserts and recency work.
- Choose the right **category** up front — it's painful to change later.
- For high-volume behavior, prefer **streaming**; for big historical loads, **batch**.

---

## 🎤 Say this in the interview

- *"A **data stream** ingests one source into a **DLO**, defining fields, **category** (Profile /
  Engagement / Other), refresh, and primary key."*
- *"Connectors include CRM, Marketing Cloud, Web/Mobile SDK, the **Ingestion API**, and
  **zero-copy** to warehouses like Snowflake."*
- *"I pick **batch** for big/reference loads and **streaming** for real-time behavior, ingesting
  only the fields I need."*

➡️ **Next:** [03 — The data model: DLO, DSO & DMO](./03_Data_Model_DLO_DMO.md)
