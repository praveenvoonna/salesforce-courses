# 09 — Querying (SQL & Query API)

## 🧠 The One Idea

**Data Cloud speaks SQL, not just SOQL.** Because it's a lakehouse, you explore its data with
familiar **ANSI SQL** — in the UI (**Data Explorer** / Query Workspace) or programmatically via
the **Query API**. This is how analysts sanity-check mappings, build calculated insights, and how
other tools pull unified data out.

The one-liner: **"You query Data Cloud DMOs with standard SQL — via Data Explorer or the Query
API."**

---

## 1. Data Explorer (the UI)

- Browse **DMOs, DLOs, Unified profiles, and Calculated Insights** by data space and object.
- **Spot-check** that mapped values look right and that unification merged correctly.
- The first place to debug "why isn't my segment matching?" — look at the actual data.

---

## 2. SQL over DMOs

Unlike SOQL (Apex), Data Cloud uses **standard SQL** with joins, aggregates, and window
functions:

```sql
SELECT i.Id__c, i.FirstName__c, SUM(o.GrandTotalAmount__c) AS lifetime_value
FROM   UnifiedIndividual__dlm i
JOIN   SalesOrder__dlm o ON o.IndividualId__c = i.Id__c
GROUP  BY i.Id__c, i.FirstName__c
HAVING SUM(o.GrandTotalAmount__c) > 5000;
```

DMO API names typically end in **`__dlm`** (and DLOs in **`__dll`**). Real SQL means real
**JOINs** — a big difference from SOQL.

---

## 3. The Query API

For programmatic access (apps, ETL, notebooks):

- **Query API (v2)** — run **synchronous** ANSI SQL queries against Data Cloud and get rows back
  via REST.
- Useful for dashboards, exports, and integrating Data Cloud data into custom apps.
- Authenticated like other Salesforce APIs (OAuth).

---

## 4. Where queries power features

- **Calculated Insights** are essentially saved SQL aggregations (Lesson 06).
- **Segmentation** generates queries under the hood from your filters.
- **Profile API** / **Data Graphs** expose a person's full unified profile to apps and AI quickly.

---

## 5. Data Graphs (fast profile reads)

A **Data Graph** pre-joins related DMOs into a single, denormalized JSON-like view of a profile
(individual + orders + engagements + insights). It's optimized for **low-latency reads** — exactly
what real-time personalization and **Agentforce grounding** need, so you don't run a big JOIN on
every request.

---

## 6. Querying best practices

- Explore in **Data Explorer** before writing automation.
- Select **only needed columns**; lakehouse scans cost compute.
- Use **Data Graphs** for real-time profile lookups instead of ad-hoc joins.
- Remember API names: **`__dlm`** (DMO) vs **`__dll`** (DLO).

---

## 🎤 Say this in the interview

- *"Data Cloud uses **standard ANSI SQL** (with real JOINs/aggregates), via **Data Explorer** or
  the **Query API** — not SOQL."*
- *"**Calculated Insights** and **segments** compile to SQL under the hood; DMOs are **`__dlm`**,
  DLOs **`__dll`**."*
- *"For **real-time** profile reads (personalization, **Agentforce grounding**) I use a
  pre-joined **Data Graph** instead of querying joins live."*

➡️ **Next:** [10 — Data actions & integrations](./10_Data_Actions_And_Integrations.md)
