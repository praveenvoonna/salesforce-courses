# 10 — Data Actions & Integrations

## 🧠 The One Idea

**Data Cloud isn't a dead-end warehouse — it can *react* and it can *borrow*.** **Data Actions**
let Data Cloud fire events when something interesting happens (a profile crosses a threshold),
triggering flows or external webhooks in near real-time. **Zero-copy** integrations let Data Cloud
**use** data sitting in your warehouse **without copying it**. Together they make Data Cloud an
active hub.

The one-liner: **"Data Actions push events out on change; zero-copy lets Data Cloud query
external data in place."**

---

## 1. Data Actions (event-driven output)

- Trigger on **events/changes** — e.g., a calculated insight crosses a value, a new engagement
  arrives, a profile enters a state.
- **Targets:** publish to the **Platform Event** bus, call a **Flow**, send to **Marketing Cloud**,
  or hit an external **webhook** (e.g., via Amazon EventBridge / MuleSoft).
- Use case: real-time triggers like "high-value cart abandoned → notify sales / start a journey."

This makes Data Cloud **reactive**, not just analytical.

---

## 2. Flows & automation

Data Cloud integrates with **Salesforce Flow**:
- **Data Cloud-triggered flows** run when Data Cloud events fire.
- Flows can read unified profiles/insights and take action in CRM.
- Low-code path to operationalize Data Cloud signals without Apex.

---

## 3. Zero-copy (use data without moving it)

The headline modern capability: **query data in Snowflake, BigQuery, Databricks, Redshift
directly** — Data Cloud reads it **in place** instead of ingesting a copy.

- **Pros:** no duplication, no sync lag, single source of truth, lower storage cost.
- **Two directions:** bring external warehouse data *in* (federation/external DMOs), and **share
  Data Cloud data out** to those warehouses (data sharing).

Expect interview questions on **why zero-copy matters** (governance + avoiding stale copies).

---

## 4. APIs & SDKs (round-up)

| Tool | Purpose |
|---|---|
| **Ingestion API** | stream/bulk data **in** |
| **Query API** | run SQL to read data **out** |
| **Profile API** | fetch a unified profile fast |
| **Web/Mobile SDK** | capture site/app behavior |
| **Connect/Metadata APIs** | manage Data Cloud config |

---

## 5. Other Salesforce integrations

- **Marketing Cloud** — segments/activations into journeys.
- **CRM (Sales/Service)** — surface unified profile + insights on records.
- **Tableau / CRM Analytics** — analytics on Data Cloud data.
- **MuleSoft** — connect arbitrary systems.
- **Agentforce / Einstein** — grounding (Lesson 12).

---

## 6. Best practices

- Use **Data Actions** for real-time triggers; don't poll.
- Prefer **zero-copy** when data already lives in a governed warehouse.
- Keep payloads minimal and **consent-aware**.
- Pick the **right API** for the job (Ingestion in, Query out, Profile for real-time reads).

---

## 🎤 Say this in the interview

- *"**Data Actions** make Data Cloud reactive — fire events to **Platform Events, Flows,
  webhooks, Marketing Cloud** on change."*
- *"**Zero-copy** lets Data Cloud query Snowflake/BigQuery/Databricks **in place** (both
  directions), avoiding duplication and stale copies."*
- *"For integration I use the **Ingestion API** (in), **Query API** (out), and **Profile API**
  for fast real-time reads."*

➡️ **Next:** [11 — Privacy, consent & governance](./11_Privacy_And_Governance.md)
