# 06 — Calculated Insights

## 🧠 The One Idea

**Calculated Insights turn raw data into scoreboard numbers.** A unified profile knows every
purchase; a **Calculated Insight (CI)** rolls those up into a single meaningful metric like
**Lifetime Value**, **average order value**, or **CSAT** — per customer, per segment, or overall.
These metrics then power smarter segments and personalization.

The one-liner: **"A Calculated Insight is a reusable metric/KPI computed over your Data Cloud
data."**

---

## 1. What you can compute

- **Per-profile metrics** — lifetime value, total orders, days since last purchase.
- **Aggregate metrics** — average order value across a segment, top categories.
- **Population-level KPIs** — overall CSAT, churn rate.

The result is stored in a **Calculated Insight Object (CIO)** — itself a DMO you can use
downstream.

---

## 2. Batch vs streaming insights

| | **Batch CI** | **Streaming CI** |
|---|---|---|
| Runs | on a schedule | continuously, over a **rolling time window** |
| Use for | "total customer value", "products over $500" | "click-through rate in the last 30 min" |
| Latency | minutes–hours | near real-time |

Streaming CIs are great for **real-time** reactions (e.g., trigger an offer based on recent
behavior); batch CIs for stable, historical metrics.

---

## 3. How you define them

- Built with a **SQL-like expression** over DMOs (dimensions + measures), or via the UI builder.
- You pick **dimensions** (group by — e.g., Individual, Product) and **measures** (SUM, AVG,
  COUNT…).
- Example idea: `SELECT IndividualId, SUM(Amount) AS LTV FROM SalesOrder GROUP BY IndividualId`.

---

## 4. The lifecycle

1. **Create** the insight (expression + dimensions/measures).
2. It **processes**; status moves from *processing* → *active*.
3. **Review** in **Data Explorer** to sanity-check the numbers.
4. **Use** it in **segmentation**, **activation**, and **personalization**.

A CI isn't usable downstream until it's **active**.

---

## 5. Why CIs matter downstream

- **Segmentation:** "customers with LTV > $5,000 AND no purchase in 90 days."
- **Activation/personalization:** inject the metric into a message ("You've earned 1,200
  points").
- **AI grounding:** Agentforce/Einstein can reference these metrics for better decisions.

CIs convert raw events into the **decision-ready numbers** the business actually wants.

---

## 6. Best practices

- Compute metrics **once as a CI** and reuse, rather than re-deriving in every segment.
- Choose **streaming** only when real-time matters (it costs more); otherwise **batch**.
- **Validate** in Data Explorer before relying on a metric.
- Keep dimensions sensible — overly granular CIs get expensive.

---

## 🎤 Say this in the interview

- *"A **Calculated Insight** is a reusable metric (LTV, AOV, CSAT) computed over DMOs and stored
  as a **CIO** for segments, activation, and AI."*
- *"**Batch** CIs run on a schedule for stable metrics; **streaming** CIs use a **rolling window**
  for real-time KPIs like 30-minute CTR."*
- *"A CI must be **active** before use, and I validate it in **Data Explorer** first."*

➡️ **Next:** [07 — Segmentation](./07_Segmentation.md)
