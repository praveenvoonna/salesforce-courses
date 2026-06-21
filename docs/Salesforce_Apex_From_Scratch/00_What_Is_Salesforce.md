# 00 — What is Salesforce & the Platform

## 🧠 The One Idea

**Salesforce is a giant apartment building, and your company rents one furnished apartment in
it.** You don't own the building, the plumbing, or the electricity — Salesforce does. You just
move into your unit, rearrange the furniture (configuration), and occasionally build a custom
room (code). Thousands of other companies live in the **same building**, sharing the same
foundation but never seeing each other's stuff. This "shared building" is called
**multitenancy**, and it explains almost everything weird about how Apex works.

The one-liner: **"Salesforce is a multitenant cloud platform — you configure and extend it,
you don't host it."**

---

## 1. CRM first, platform second

Salesforce started as a **CRM** (Customer Relationship Management) — software to track
customers, sales deals, and support cases. Over time it grew into a **platform** (sometimes
called the "Salesforce Platform" or historically Force.com / Lightning Platform) where you can
build whole custom business apps. Apex is the code part of that platform.

---

## 2. The org — your apartment

- An **org** (short for *organization*) is your company's single instance of Salesforce: its
  data, users, settings, and customizations.
- Types you'll hear about: **Production** (the real one), **Sandboxes** (copies for
  dev/testing), **Developer Edition** (a free personal org — what you'll use to learn), and
  **Scratch orgs** (disposable, source-driven dev orgs).

---

## 3. Metadata — everything is a setting

This is the big mental shift: **almost everything in Salesforce is *metadata*** — a
description, not hand-written infrastructure. Your custom objects, fields, page layouts,
validation rules, **and even your Apex classes** are metadata stored by the platform.

- You build by **declaring** what you want; Salesforce provisions it.
- This is why you can move customizations between orgs as **metadata files** (with the CLI).

---

## 4. Multitenancy — the reason for limits

Because many tenants share the same hardware and database, **no single tenant is allowed to
hog resources**. Salesforce enforces **governor limits** (Lesson 08): caps on how many queries,
records, CPU-milliseconds, etc. your code can use per transaction. A runaway loop in *your*
code must never slow down your neighbor's org — so the platform simply stops it.

> If you remember one thing: *governor limits exist because the building is shared.*

---

## 5. Clicks vs code (configuration vs customization)

Salesforce's mantra is **"clicks, not code"** — do as much as possible with point-and-click
tools (Flows, validation rules, formula fields). You reach for **Apex** only when declarative
tools can't express the logic. Interviewers love candidates who know *when not to write code*.

---

## 🌍 Real-World Example

**Northern Trail Outfitters (a retailer) runs its entire business in one org.** Sales reps track
deals on `Opportunity`, support agents handle `Case` records, and marketers run campaigns — all
on the **same instance**, sharing the same servers as thousands of other companies.

On Black Friday, a junior developer ships a trigger with an accidental query inside a loop. In a
single-tenant world that could slow the whole server. Here, the platform simply throws a
**`LimitException`**, kills *that one transaction*, and rolls it back — **neighbouring orgs never
even notice**. That isolation is multitenancy quietly doing its job, and it's exactly why the
limits in Lesson 08 exist.

---

## 🔬 Under the Hood (In-Depth)

- **Instances & Hyperforce** — your org physically lives on an *instance* (e.g., `NA235`).
  Modern Salesforce runs these on public-cloud infrastructure (AWS/GCP) called **Hyperforce**,
  not on Salesforce's own data centers.
- **Row-level tenant isolation** — every row in the shared database carries an **`OrgId`**. The
  multitenant **query optimizer** silently adds that `OrgId` filter to *every* query, so you can
  only ever touch your own tenant's data.
- **Metadata-driven kernel** — there is no per-customer compiled application. The platform reads
  your metadata at **runtime** to render layouts, run validation rules, and execute Apex. This is
  why a config change appears instantly with no redeploy.
- **Release cadence & API versions** — Salesforce ships **three releases a year** (Spring,
  Summer, Winter). Each metadata component is pinned to an **API version** (e.g., `60.0`) so old
  code keeps behaving predictably across upgrades.
- **Editions** — Essentials / Professional / Enterprise / Unlimited gate which features (and even
  some limits, like the number of custom objects) are available.

---

## 🎤 Say this in the interview

- *"Salesforce is a **multitenant** cloud platform — many customers share the same
  infrastructure, which is exactly why **governor limits** exist."*
- *"Almost everything is **metadata**, including Apex classes — so I can version and deploy
  customizations as source."*
- *"I follow **clicks-then-code**: declarative tools first, Apex only when the logic can't be
  done declaratively."*

➡️ **Next:** [01 — What is Apex & when to use it](./01_What_Is_Apex.md)
