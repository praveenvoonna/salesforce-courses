# 14 — Interview Q&A Flashcards

Rapid-fire. Cover the answer, say it aloud, then check. Read twice.

---

## Fundamentals

**Q: What is Data Cloud?**
Salesforce's **CDP** (now branded **Data 360**) that **connects, harmonizes, unifies, and
activates** customer data into a **single real-time profile**.

**Q: What problem does it solve?**
**Data silos** — the same customer fragmented across systems with no shared key.

**Q: What's it built on?**
A **lakehouse** (data-lake scale + warehouse query) using open formats.

**Q: What's a Data Space?**
A logical **partition** of Data Cloud by brand/region/BU for isolation and access control.

---

## Data model

**Q: DLO vs DSO vs DMO?**
**DLO** = raw ingested landing object; **DSO** = normalized stream view; **DMO** = harmonized
semantic model the rest of Salesforce queries.

**Q: How do multiple sources become one profile?**
Many **DLOs map into one DMO** (e.g., Individual), then **identity resolution** produces the
**Unified Individual**.

**Q: What are the data categories?**
**Profile** (who), **Engagement** (time-stamped behavior), **Other** (reference data).

**Q: What are Contact Points?**
DMOs for ways to reach someone (email/phone/address), linked to the Individual; consent attaches
here.

---

## Ingestion

**Q: What's a data stream?**
A configured **pipe** ingesting one source into a **DLO**, defining fields, category, refresh, and
primary key.

**Q: Batch vs streaming?**
Batch = scheduled bulk (big/reference data); streaming = near-real-time events (Web/Mobile SDK,
Ingestion API).

**Q: What's zero-copy?**
Querying warehouse data (Snowflake/BigQuery/Databricks) **in place** without copying — both
directions; avoids duplication and stale copies.

---

## Mapping & unify

**Q: What is mapping?**
Connecting **DLO fields → DMO fields** so data is harmonized; unmapped fields are invisible
downstream.

**Q: What's in an identity-resolution ruleset?**
**Match rules** (how records are the same) + **reconciliation rules** (which value wins /
survivorship).

**Q: The core tuning trade-off?**
**Over-merge** (two people become one) vs **under-merge** (one person stays split).

---

## Insights & segments

**Q: What's a Calculated Insight?**
A reusable metric/KPI (LTV, AOV, CSAT) computed over DMOs, stored as a **CIO**; **batch** or
**streaming** (rolling window).

**Q: What's a segment?**
A **filtered, scheduled-refresh audience** of unified profiles, built on attributes, engagement,
and CIs.

**Q: What's activation?**
Publishing a segment + attributes to a **target** (Marketing Cloud, ads, CRM, external) via
**consented contact points**.

---

## Querying & integration

**Q: How do you query Data Cloud?**
**Standard ANSI SQL** (real JOINs/aggregates) via **Data Explorer** or the **Query API** — not
SOQL. DMOs end in `__dlm`, DLOs in `__dll`.

**Q: What's a Data Graph?**
A **pre-joined, denormalized** profile view for **low-latency** reads — used for real-time
personalization and **Agentforce grounding**.

**Q: What's a Data Action?**
An **event** Data Cloud fires on change → Platform Events, Flows, webhooks, Marketing Cloud (makes
it reactive).

---

## Governance & AI

**Q: Key privacy concerns?**
**Consent** (per contact point) and **GDPR/CCPA** rights (access, deletion, opt-out); enforce
**least privilege** and **data minimization**.

**Q: How does Data Cloud power AI?**
It **grounds** Einstein/Agentforce via **RAG** — retrieving unified profile, insights, and
**vector-searched** unstructured content to prevent hallucination.

**Q: Structured vs unstructured grounding?**
Structured = profile fields/insights (via Data Graphs); unstructured = documents/knowledge chunked
and **vectorized** for semantic search.

---

🎉 That's the Data Cloud course. Loop back to any lesson whose flashcard you couldn't answer cold.
