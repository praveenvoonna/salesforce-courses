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

## 🌍 Real-World Example

**An airline finally recognizes its own frequent flyer.** The same traveler booked on the website
as "Jonathan Smith," used the mobile app as "jon.smith@email," and held loyalty card #4471 — three
disconnected records across three systems. After Data Cloud unified them, a single delayed-flight
alert could trigger a personalized rebooking offer that *knew* he was Platinum tier with 180k miles.
Before, each channel treated him as a stranger; now every Salesforce app sees one person.

---

## 🔬 Under the Hood (In-Depth)

- **CDP ≠ CRM ≠ CDW** — a CRM stores operational records a rep edits; a data warehouse stores
  analytics; a **CDP** specializes in unifying *customer* data into a real-time, activatable
  profile. Data Cloud blurs the line by being a CDP built on a lakehouse.
- **The unified profile is a graph, not a row** — identity resolution links many source records to
  one Unified Individual while keeping the links, so you can always trace a value back to its
  origin.
- **Near-real-time, not magic** — streaming sources update profiles in seconds; batch sources on a
  schedule. "Real-time" describes the ingestion + activation path, not every computation.
- **Multitenant at lakehouse scale** — separating cheap columnar storage from compute is why it can
  hold billions of engagement events without a traditional database's cost.
- **It's a foundation, not a destination** — there's no end-user "Data Cloud app"; its value
  appears when Sales, Service, Marketing, and Agentforce consume the profile.

---

## 🎤 Say this in the interview

- *"Data Cloud is Salesforce's **CDP**: it **connects, harmonizes, unifies, and activates**
  customer data into a **single real-time profile**."*
- *"It solves **data silos** — the same person fragmented across systems — using **identity
  resolution** to build a **Unified Individual**."*
- *"It's the **grounding/data foundation for AI** (Einstein, Agentforce), handling both **batch
  and streaming** at scale."*

➡️ **Next:** [01 — Architecture & core concepts](./01_Architecture_And_Concepts.md)
