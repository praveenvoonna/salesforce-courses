# 13 — Hands-On Lab

Data Cloud is best understood by walking one record through the **whole pipeline**. This lab takes
two sources, unifies them, computes a metric, builds a segment, and activates it — touching every
earlier lesson.

> **Goal:** Ingest CRM contacts + e-commerce customers → map both to **Individual** → unify into
> one profile → compute **Lifetime Value** → segment "High-value, lapsed" → activate.
>
> **Note:** You need a **Data Cloud–enabled trial/Trailhead org**. Exact menus shift over
> releases; follow the concept even if a label differs.

---

## 0. Setup

1. Launch a **Data Cloud–enabled Trailhead Playground** (or a trial org with Data Cloud).
2. Confirm you can open the **Data Cloud** app and see tabs: Data Streams, Data Explorer,
   Identity Resolution, Calculated Insights, Segments, Activations.
3. Grab two sample CSVs (or use a starter bundle): `crm_contacts.csv`,
   `ecom_customers.csv`, plus `orders.csv`.

---

## 1. Ingest (Lesson 02)

- Create a **Data Stream** for `crm_contacts.csv` → category **Profile**, set primary key =
  contact id, modified date set.
- Repeat for `ecom_customers.csv` (Profile) and `orders.csv` (**Engagement**, with order amount +
  timestamp).
- Each creates a **DLO**. Confirm rows landed in **Data Explorer**.

---

## 2. Map to the data model (Lessons 03–04)

- Map both contact/customer DLOs to the **Individual** DMO: first name, last name, **email**,
  **phone** → and emails/phones into **Contact Point Email/Phone**.
- Map `orders` to a **Sales Order** DMO with `IndividualId`, `GrandTotalAmount`, `OrderDate`.
- **Validate** mapped values in Data Explorer — key attributes must be clean.

---

## 3. Unify (Lesson 05)

- Open **Identity Resolution** and create/confirm a ruleset on **Individual**:
  - **Match rule:** exact **email** OR (exact **phone** + same last name).
  - **Reconciliation:** most recently updated wins.
- Run it. In Data Explorer, open the **Unified Individual** and confirm a CRM + e-com record
  merged into **one** profile linked to both sources.

---

## 4. Calculated Insight (Lesson 06)

Create a **batch CI** for Lifetime Value:

```sql
SELECT IndividualId__c, SUM(GrandTotalAmount__c) AS LTV__c
FROM   SalesOrder__dlm
GROUP  BY IndividualId__c
```

Wait until status = **active**, then check a few LTV values in Data Explorer.

---

## 5. Segment (Lesson 07)

Build a segment on **Unified Individual**:

```
WHERE CalculatedInsight.LTV > 1000
  AND NOT (Sales Order in last 90 days)
```

Check the **estimated size**; refine the threshold so it's not empty.

---

## 6. Activate (Lesson 08)

- Create an **Activation** targeting (e.g.) Marketing Cloud or a test target.
- Payload: email contact point + first name + **LTV** (for personalization).
- Activate on **consented** email only. Confirm members are generated.

---

## 7. Inspect end-to-end (Lesson 09)

Run SQL in **Data Explorer** to see the whole picture:

```sql
SELECT i.FirstName__c, ci.LTV__c
FROM   UnifiedIndividual__dlm i
JOIN   LTV_Insight__dlm ci ON ci.IndividualId__c = i.Id__c
ORDER  BY ci.LTV__c DESC;
```

---

## 8. Stretch goals

- Add a **streaming CI** for "page views in last 30 min" (Lesson 06).
- Tighten match rules and observe **over/under-merge** changes (Lesson 05).
- Add a **Data Action** that fires when LTV crosses a threshold (Lesson 10).
- Ground an **Agentforce** answer on this LTV (Lesson 12 + Agentforce course).

You've now run the full Data Cloud pipeline: ingest → map → unify → insight → segment →
activate. 🎉

➡️ **Next:** [14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)
