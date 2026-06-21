# 00 — What is Data Cloud (a CDP)

## 🧠 The One Idea

**Data Cloud is a "single brain" that finally remembers your whole customer.** Today a customer's
data is scattered: the website knows their clicks, the call center knows their complaints, the
store knows their purchases, and none of them talk. Data Cloud sucks in **all** of it, figures
out that "J. Smith," "john.smith@email," and loyalty member #4471 are the **same person**, and
builds **one unified profile** every other Salesforce app can use.

The one-liner: **"Data Cloud is Salesforce's CDP — it unifies all customer data into one
real-time profile."**

---

## 1. The problem it solves: data silos

- Marketing, sales, service, commerce, and external systems each hold **part** of the customer.
- The same person appears as **many fragmented records** with no shared key.
- Teams make decisions on **partial, stale** views → bad personalization, duplicated effort.

A **CDP (Customer Data Platform)** exists to fix exactly this: collect everything, unify it,
make it usable.

---

## 2. What Data Cloud actually does (four verbs)

1. **Connect** — ingest data from any source: Salesforce clouds, websites, mobile, data
   warehouses, files, streaming events.
2. **Harmonize** — map all of it onto a **common data model** so "email" means the same thing
   everywhere.
3. **Unify** — **identity resolution** merges duplicates into a single **Unified Individual**.
4. **Activate** — push that unified, enriched profile out to segments, journeys, ads, analytics,
   and AI.

---

## 3. Why it's a big deal now (AI)

AI is only as good as the data it sees. **Agentforce and Einstein** need rich, current, unified
context to give good answers and take correct actions. Data Cloud is the **grounding layer**
(Lesson 12) — the memory that makes AI accurate instead of generic.

---

## 4. Real-time & scale

- Handles **batch** (nightly files) **and streaming** (live web/app events) data.
- Built on a **massively scalable lakehouse** (Lesson 01) so it can hold huge volumes cheaply.
- Profiles update **in near-real-time**, so a click can influence the next interaction.

---

## 5. Where it sits in the Salesforce family

Think of Data Cloud as the **data foundation** under everything: Sales, Service, Marketing,
Commerce, Tableau/CRM Analytics, and Agentforce all **consume** the unified profile. It's not a
separate destination app — it's the shared customer memory the others plug into.

---

## 6. A quick analogy to carry forward

Imagine a detective assembling one case file from a dozen anonymous tip-offs. Each tip
(data source) is partial; the detective (identity resolution) connects them into one suspect
profile (unified individual); then the team acts on it (segmentation/activation). Hold that image
— the rest of the course fills in each step.

---

## 🎤 Say this in the interview

- *"Data Cloud is Salesforce's **CDP**: it **connects, harmonizes, unifies, and activates**
  customer data into a **single real-time profile**."*
- *"It solves **data silos** — the same person fragmented across systems — using **identity
  resolution** to build a **Unified Individual**."*
- *"It's the **grounding/data foundation for AI** (Einstein, Agentforce), handling both **batch
  and streaming** at scale."*

➡️ **Next:** [01 — Architecture & core concepts](./01_Architecture_And_Concepts.md)
