# 04 — Data Mapping & Transformation

## 🧠 The One Idea

**Mapping is teaching Data Cloud that "cust_email" and "EmailAddr" both mean *email*.** Every
source names things differently. **Data mapping** connects each raw DLO field to the matching
standard **DMO** field, so all your data speaks one language. **Transformation** cleans and
reshapes data on the way through. Without good mapping, unification and segmentation can't work.

The one-liner: **"Mapping links raw DLO fields to standard DMO fields; transformation cleans
them en route."**

---

## 1. Why mapping matters

Downstream features (identity resolution, insights, segments, AI) all read **DMOs**. If a field
isn't mapped to the DMO, it effectively **doesn't exist** for them. Mapping the **key attributes**
— name, email, phone, IDs — is what makes the **unified profile** possible.

---

## 2. How mapping works

- In the **Data Stream / Data Model mapping** UI, you drag/connect each **DLO (source) field** to
  a **DMO (target) field**.
- **Starter bundles** come **pre-mapped** for standard fields; you typically map **custom** and
  **unmapped standard** fields by hand.
- You also pick the **target DMO** (e.g., Individual, Contact Point Email) for each source object.

---

## 3. Key attributes to always map

| Attribute | Why |
|---|---|
| Name (first/last) | matching individuals |
| Email | a primary match key + contact point |
| Phone | match key + contact point |
| Source primary key / IDs | links unified profile back to source records |
| Party/Individual ID | the join across objects |

These feed **identity resolution** (Lesson 05). Garbage in → no unification.

---

## 4. Transformations

You can reshape data as it flows:

- **Formula fields / batch & streaming transforms** — derive new fields (e.g., uppercase email,
  full name, bucket an age).
- **Filtering** — drop rows you don't need.
- **Type/format normalization** — standardize phone/date formats so matching works.
- **Data kits / harmonization helpers** — reusable mapping packages.

Clean, normalized data dramatically improves match rates.

---

## 5. Contact Points

The Customer 360 model splits ways-to-reach-someone into **Contact Point** DMOs:
**Contact Point Email**, **Contact Point Phone**, **Contact Point Address**. You map each source's
email/phone into these, linked to the Individual. This structure lets one person have many emails
and supports **consent** per contact point (Lesson 11).

---

## 6. Mapping best practices

- Map **key attributes first** — they drive unification.
- **Normalize formats** before matching (lowercase emails, E.164 phones).
- Reuse **standard DMOs** for interoperability; extend with custom only when needed.
- Validate in **Data Explorer** after mapping to confirm values landed correctly.

---

## 🎤 Say this in the interview

- *"**Mapping** connects raw **DLO** fields to standard **DMO** fields so everything is
  harmonized; unmapped fields are invisible downstream."*
- *"I always map **key attributes** (name, email, phone, IDs) because they drive **identity
  resolution**, and I store reach-info in **Contact Point** DMOs."*
- *"**Transformations** normalize and derive fields (formats, formulas, filters) to raise match
  quality before unification."*

➡️ **Next:** [05 — Identity resolution](./05_Identity_Resolution.md)
