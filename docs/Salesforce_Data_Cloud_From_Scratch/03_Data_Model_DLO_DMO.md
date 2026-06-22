# 03 — The Data Model: DLO, DSO & DMO

## 🧠 The One Idea

**Data goes through three rooms: a messy receiving dock (DLO), a sorting table (DSO), and a
labeled showroom (DMO).** Raw data lands exactly as-is in a **DLO**. A **DSO** is a normalized
view of it. Then you **map** it into a **DMO** — the clean, standardized model that the rest of
Salesforce actually uses. This three-letter trio is the single most-asked Data Cloud topic.

The one-liner: **"DLO = raw landing, DSO = normalized stream, DMO = harmonized model everyone
queries."**

---

## 1. DLO — Data Lake Object (raw)

- The **storage container** for data ingested by a data stream.
- **Schema-preserved**: fields look like the source ("cust_email", "fname").
- One data stream → (typically) one DLO.
- You rarely segment/activate directly on DLOs — they're the raw layer.

Naming you'll see: a CRM Contact stream might create something like `CRM_Contact__dll`.

---

## 2. DSO — Data Stream Object (normalized)

- A **normalized representation** of a DLO that Data Cloud auto-creates to feed downstream
  processing.
- Think of it as the bridge between the raw DLO and the harmonized DMO.
- You'll often **map from the DSO/DLO fields to DMO fields** (Lesson 04).

(Some UIs/docs emphasize DLO→DMO and treat the DSO as an internal step — know it exists and what
it's for.)

---

## 3. DMO — Data Model Object (harmonized)

- The **semantic, standardized** object that the rest of Salesforce — Segmentation, Activation,
  Calculated Insights, **Agentforce grounding**, Einstein — actually queries.
- Part of the **Customer 360 Data Model** (Individual, Contact Point Email, Sales Order…).
- **Many DLOs can map into one DMO**: CRM Contacts, e-commerce Customers, and loyalty Members all
  map to the single **Individual** DMO.

This is the magic: downstream features query **one** `Individual`, not three source tables.

---

## 4. Unified DMO (after identity resolution)

After **identity resolution** (Lesson 05) merges duplicates, you get a **Unified DMO** — e.g., the
**Unified Individual** — containing one record per real person, linked to all their source
records. Segmentation and AI usually target the **unified** profile.

---

## 5. A concrete flow

```
CRM Contacts ─┐
E-com Customers├─► (each lands in its own DLO)
Loyalty Members┘
        │  map fields
        ▼
   Individual DMO   ◄── all three mapped here (harmonized)
        │  identity resolution
        ▼
 Unified Individual DMO  ◄── one record per real person
        │
        ▼  queried by Segmentation, CIs, Activation, Agentforce
```

---

## 6. Custom vs standard DMOs

- Use **standard DMOs** from the Customer 360 model wherever possible (interoperability).
- Create **custom DMOs** for concepts the standard model doesn't cover.
- Map thoughtfully — **key attributes** (name, email, phone, IDs) are what make unification work
  (Lesson 04–05).

---

## 🌍 Real-World Example

**Three "customer" tables become one queryable person.** A bank had retail customers in core
banking, applicants in a loan system, and card holders in a third platform — three DLOs with three
different schemas. Mapping all three into the single **Individual** DMO meant an analyst could
finally write *one* query for "all our customers," and a segment could target a person regardless of
which system first knew them.

---

## 🔬 Under the Hood (In-Depth)

- **The layers have distinct API suffixes** — DLOs end in `__dll`, DMOs in `__dlm`; you query DMOs
  downstream, and the suffix is a quick way to tell which layer a SQL query touches.
- **Mapping moves metadata, not (much) data** — a DLO→DMO mapping tells the engine how to *present*
  the harmonized view; it's a transformation definition, not a second physical copy you maintain by
  hand.
- **Many-to-one is the whole point** — multiple DLOs collapsing into one DMO is what creates
  harmonization; the DMO becomes the single semantic object every feature reads.
- **Unified DMOs are produced by a process** — the Unified Individual isn't mapped manually;
  identity resolution generates it and maintains link records back to each source.
- **Custom DMOs extend, they don't replace** — adding a custom DMO is fine, but reusing standard
  ones preserves out-of-the-box interoperability with Marketing Cloud, CRM, and Agentforce.

---

## 🎤 Say this in the interview

- *"**DLO** is the **raw** landing object, **DSO** the **normalized** stream view, and **DMO** the
  **harmonized** model the rest of Salesforce queries."*
- *"**Many DLOs map into one DMO** (e.g., CRM/e-com/loyalty → **Individual**), then identity
  resolution produces the **Unified Individual**."*
- *"Downstream features (segments, insights, **Agentforce grounding**) query **DMOs**, not source
  tables — that's the whole point of harmonization."*

➡️ **Next:** [04 — Data mapping & transformation](./04_Mapping_And_Transformation.md)
