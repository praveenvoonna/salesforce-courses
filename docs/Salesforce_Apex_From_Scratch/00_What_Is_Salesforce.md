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

## 🎤 Say this in the interview

- *"Salesforce is a **multitenant** cloud platform — many customers share the same
  infrastructure, which is exactly why **governor limits** exist."*
- *"Almost everything is **metadata**, including Apex classes — so I can version and deploy
  customizations as source."*
- *"I follow **clicks-then-code**: declarative tools first, Apex only when the logic can't be
  done declaratively."*

➡️ **Next:** [01 — What is Apex & when to use it](./01_What_Is_Apex.md)
