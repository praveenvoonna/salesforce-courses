# 07 — Segmentation

## 🧠 The One Idea

**A segment is a smart guest list built from filters.** Once profiles are unified and enriched,
**segmentation** lets you carve out exactly the people you care about — "VIP customers in California
who haven't purchased in 90 days" — by stacking filters on profile attributes and calculated
insights. The segment is the audience you'll then **activate** (Lesson 08).

The one-liner: **"A segment is a filtered, refreshable audience of unified profiles."**

---

## 1. What you filter on

- **Profile attributes** — country, age, loyalty tier (from DMOs).
- **Related/engagement data** — "opened an email," "viewed product X."
- **Calculated insights** — "LTV > $5,000," "orders in last 30 days."
- **Nested logic** — AND/OR groups, includes/excludes.

You're querying the **unified individual** plus its related objects and CIs.

---

## 2. Segment membership & refresh

- A segment has a **population** (which object/profile it counts — usually Individual).
- It **refreshes on a schedule** (e.g., every 12/24 hours) or on demand, so membership stays
  current as data changes.
- You can see the **estimated size** as you build — handy to avoid empty or huge audiences.

---

## 3. Build it with filters (example logic)

```
Population: Unified Individual
WHERE Country = 'US'
  AND Loyalty_Tier = 'Gold'
  AND CalculatedInsight.LTV > 5000
  AND NOT (Purchase in last 90 days)
```

The UI is drag-and-drop; under the hood it's filter logic over DMOs and CIs.

---

## 4. Related attributes & engagement

Segments shine because they can filter on **behavior over time**:
- "Clicked a link in the last 7 days."
- "Abandoned a cart this week."
- "Attended ≥ 2 events this year."

This is why **Engagement** data and the right **mapping/category** (Lesson 02) matter.

---

## 5. Nested segments & exclusions

- **Include** one segment and **exclude** another ("VIPs but not employees").
- **Reuse** segments as building blocks.
- Combine with **CIs** for value-based targeting.

---

## 6. Best practices

- Lead with **calculated insights** for value/behavior rather than re-deriving math each time.
- Keep segments **purpose-named** and reusable.
- Watch **refresh frequency** vs freshness needs (real-time vs daily).
- **Preview/estimate size** before activating to avoid surprises.

---

## 🌍 Real-World Example

**A win-back campaign that excludes the wrong people automatically.** A retailer built "Gold-tier US
customers with LTV over $5,000 who haven't purchased in 90 days," then *excluded* a suppression
segment of employees and recent complainers. The drag-and-drop filters quietly compiled into a SQL
query over the unified profile and its calculated insights — the marketer never wrote SQL, but got a
precise, refreshable audience ready to activate.

---

## 🔬 Under the Hood (In-Depth)

- **Filters compile to SQL** — the visual builder generates a query over DMOs and CIs; complex
  AND/OR nesting is just boolean logic in that generated SQL.
- **The population defines the grain** — choosing Unified Individual as the population means one row
  per person; related/engagement filters become joins against that population.
- **Membership is refreshed, not live** — a segment recomputes on its schedule (or on demand), so
  freshness is a deliberate trade-off between cost and recency.
- **Estimated size uses sampling** — the size preview is computed efficiently so you can iterate
  without fully materializing the audience each time.
- **CIs keep segments cheap** — filtering on a precomputed LTV insight is far cheaper than
  re-aggregating orders inside every segment evaluation.

---

## 🎤 Say this in the interview

- *"A **segment** is a filtered, scheduled-refresh audience of **unified profiles**, built on
  profile attributes, **engagement** data, and **calculated insights**."*
- *"I can **nest** segments and use **include/exclude** logic, and I lean on **CIs** for
  value/behavior filters."*
- *"Segments stay current via **refresh schedules**, and I check **estimated size** before
  activating."*

➡️ **Next:** [08 — Activation](./08_Activation.md)
