# 11 — Privacy, Consent & Governance

## 🧠 The One Idea

**Unifying everyone's data is powerful — and a legal responsibility.** The moment you build one
profile of a person from many sources, you must honor their **consent** (what they agreed to),
respect **privacy laws** (GDPR, CCPA), and control **who can see what**. Governance is what keeps
Data Cloud's superpower from becoming a liability.

The one-liner: **"Data Cloud unifies data *with* consent, privacy, and access controls built
in."**

---

## 1. Consent management

- The Customer 360 model has **consent objects** tied to **contact points** (email/phone).
- Activations should **only target consented channels** — e.g., don't email someone who opted out
  of email but did opt into SMS.
- Consent travels with the unified profile so **every** downstream use respects it.

---

## 2. Privacy regulations (GDPR / CCPA)

Key rights you must support:
- **Right to access** — produce what data you hold on a person.
- **Right to be forgotten / deletion** — remove their data on request.
- **Right to restrict/opt-out** — stop processing/sale of data.

Data Cloud provides **data rights / privacy request** handling so deletes and restrictions
propagate across the unified profile and its sources.

---

## 3. Access control & security

- **Data Spaces** isolate data by brand/region/BU (Lesson 01) so teams only see their slice.
- **Permission sets / user access** govern who can view objects, build segments, or activate.
- **Field-level** controls limit sensitive attributes.
- Encryption and standard Salesforce trust controls apply.

---

## 4. Data minimization

Good governance = **collect and keep only what you need**:
- Ingest only required fields (Lesson 02).
- Activate only needed attributes (Lesson 08).
- Set **data retention** so old/raw data doesn't linger forever.

Less data = less risk and lower cost.

---

## 5. Lineage & trust

- **Data lineage** — trace a value back through DMO → DSO → DLO → source. Vital for debugging and
  audits.
- **Auditability** — know who changed mappings, rules, segments.
- Trustworthy data is the prerequisite for trustworthy **AI** (next lesson).

---

## 6. Governance best practices

- Map **consent** early and enforce it in **every** activation.
- Honor **deletion/opt-out** requests promptly and verify propagation.
- Use **Data Spaces + permissions** for least-privilege access.
- Practice **data minimization** and set **retention** policies.

---

## 🎤 Say this in the interview

- *"Because Data Cloud builds **one profile per person**, I treat **consent** (per contact point)
  and **privacy rights** (GDPR/CCPA: access, deletion, opt-out) as first-class."*
- *"I enforce **least privilege** with **Data Spaces** and permissions, and practice **data
  minimization** with retention policies."*
- *"**Data lineage** lets me trace any value back to its source — essential for audits and for
  trustworthy AI."*

➡️ **Next:** [12 — Data Cloud + Einstein & Agentforce](./12_Data_Cloud_And_AI.md)
