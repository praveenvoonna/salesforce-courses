# 05 — Identity Resolution

## 🧠 The One Idea

**Identity resolution is the detective that says "these five records are all the same person."**
After mapping, you still have John from CRM, john.smith from the website, and member #4471 from
loyalty as **separate** records. Identity resolution applies **rules** to **match** them and
**merge** them into **one Unified Individual** — the single source of truth every other feature
uses.

The one-liner: **"Identity resolution uses match + reconciliation rules to merge duplicate
records into one unified profile."**

---

## 1. The two kinds of rules

A **ruleset** (defined on an object like **Individual**) contains:

1. **Match rules** — *how do we decide two records are the same?*
   - e.g., "same email" OR "same phone + same last name" OR "fuzzy name + same address."
   - Can be **exact** or **fuzzy** (handles typos/nicknames).
2. **Reconciliation rules** — *when records merge, which value wins?*
   - e.g., "most recently updated wins," or "value from the most trusted source wins."

---

## 2. The output: Unified Individual

- Matched source records collapse into **one Unified Individual** record.
- The unified profile keeps **links back** to every contributing source record.
- Downstream (segments, insights, AI) target the **unified** profile so you act on the whole
  person, not a fragment.

---

## 3. Match rules in practice

| Match strategy | Example | Risk |
|---|---|---|
| Exact email | same email → same person | misses people with multiple emails |
| Exact phone | same phone | shared family phones over-merge |
| Composite | last name + address + DOB | stronger, fewer false merges |
| Fuzzy | "Bob" ≈ "Robert" | catches more, risks false positives |

Tuning is a **trade-off**: too loose → **over-merge** (two people become one); too strict →
**under-merge** (one person stays split). This trade-off is a favorite interview point.

---

## 4. Reconciliation (the survivorship question)

When records merge, conflicting fields need a winner. Common policies:
- **Last updated wins** (recency).
- **Source priority** (CRM > web form).
- **Most frequent value**.

This is sometimes called **survivorship** — deciding which attribute value "survives" the merge.

---

## 5. How it runs

- Identity resolution runs as a **process on a schedule** (and reprocesses as new data arrives).
- It produces/updates the **Unified DMO**.
- You can **inspect** results in **Data Explorer** to see which sources merged into a profile.

---

## 6. Getting it right

- Map and **normalize key attributes** first (Lesson 04) — match quality depends on it.
- Start with **conservative exact** rules, then add fuzzy/composite carefully.
- **Monitor** match rates and spot-check merged profiles for over/under-merging.
- Different objects can have different rulesets (e.g., Individual vs Account).

---

## 🎤 Say this in the interview

- *"Identity resolution uses **match rules** (how records are the same) and **reconciliation
  rules** (which value wins) to produce a **Unified Individual**."*
- *"The core tension is **over-merge vs under-merge** — I tune match rules and normalize key
  attributes to balance it."*
- *"Reconciliation/**survivorship** picks winners by recency or source priority; I verify results
  in **Data Explorer**."*

➡️ **Next:** [06 — Calculated insights](./06_Calculated_Insights.md)
