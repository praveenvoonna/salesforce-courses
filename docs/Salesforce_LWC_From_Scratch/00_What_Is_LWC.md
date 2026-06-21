# 00 — What is LWC & the UI Landscape

## 🧠 The One Idea

**LWC is "building with LEGO bricks that the browser already understands."** Instead of a heavy,
custom Salesforce-only framework, Lightning Web Components are built on **native web standards**
(the same Web Components, JavaScript classes, and DOM your browser ships with). That makes them
**fast, lightweight, and familiar** to any modern web developer.

The one-liner: **"LWC is Salesforce's modern UI framework, built on standard Web Components."**

---

## 1. The two UI frameworks (Aura vs LWC)

Salesforce has had two component frameworks:

| | **Aura** (older) | **LWC** (modern) |
|---|---|---|
| Era | 2014+ | 2019+ |
| Built on | custom Salesforce framework | **web standards** (Web Components) |
| Performance | heavier | **lighter, faster** |
| Today | legacy / maintenance | **the recommended default** |

They **interoperate** — Aura can contain LWC (not the reverse, easily) — so big orgs run both.
Build new things in **LWC**.

---

## 2. What "Web Components" means

LWC stands on four browser standards:
- **Custom Elements** — define your own HTML tags (`<c-my-component>`).
- **Shadow DOM** — each component's markup/CSS is **encapsulated** (scoped), so styles don't
  leak (Lesson 10).
- **Templates** — reusable chunks of markup.
- **Modules** — standard `import`/`export` JavaScript.

Because it's standards-based, **the JS/HTML/CSS you learn here is transferable** beyond
Salesforce.

---

## 3. Where LWC runs

LWC renders in the **browser** (client side), inside the **Lightning Experience**, in
**Communities/Experience Cloud sites**, on **mobile (Salesforce app)**, on Lightning **record/app/home
pages**, in **flows**, as **quick actions**, and even on **Open Source** outside Salesforce
(LWC OSS). The same component can be reused in many surfaces.

---

## 4. The mental model: components all the way down

A Lightning page is a **tree of components**. A page contains components, which contain child
components, and so on — like nesting boxes. Data generally flows **down** (parent → child via
properties) and notifications flow **up** (child → parent via events). Keep that picture; it
explains Lesson 05.

---

## 5. Why interviewers ask about LWC vs Aura

It signals you know the platform's **current** direction. The expected answer: *"LWC is the
modern, standards-based, faster framework; Aura is legacy. I build new components in LWC and only
touch Aura to maintain existing code or use the few features only Aura has."*

---

## 🎤 Say this in the interview

- *"LWC is Salesforce's modern UI framework built on **native Web Components** — custom elements,
  shadow DOM, templates, ES modules — so it's lightweight and standards-based."*
- *"**Aura is legacy**; LWC is the default. They interoperate, but I build new components in
  LWC."*
- *"A Lightning page is a **tree of components**: data flows **down** via properties, events flow
  **up**."*

➡️ **Next:** [01 — Dev environment & tooling](./01_Dev_Environment.md)
