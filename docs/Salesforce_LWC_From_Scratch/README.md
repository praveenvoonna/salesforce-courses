# ⚡ LWC From Scratch — A Crash Course (in plain English)

A from-zero deep dive into **Lightning Web Components (LWC)**, Salesforce's modern UI framework:
*what it is, how a component is built, and how it talks to Salesforce data* — explained in
**naive, everyday language** with analogies, then the real mechanics, then **interview-ready
lines**.

> **How to read this:** go in order, 00 → 14. Each lesson starts with a plain-English analogy
> (**"The One Idea"**), then the real details, then **"Say this in the interview"** one-liners
> you can repeat almost verbatim. Don't skip the analogies — they're the hooks that make the
> rest stick.

---

## 📂 The lessons (read in order)

### Part A — The mental model
- **[00 — What is LWC & the UI landscape](./00_What_Is_LWC.md)** — Aura vs LWC, Web Components,
  why LWC is fast.
- **[01 — Dev environment & tooling](./01_Dev_Environment.md)** — SFDX, VS Code, scratch orgs,
  the CLI.

### Part B — Building a component
- **[02 — Anatomy of a component](./02_Component_Anatomy.md)** — the HTML/JS/meta trio.
- **[03 — Templates & directives](./03_Templates_And_Directives.md)** — `if:true`, `for:each`,
  data binding.
- **[04 — Reactivity & properties](./04_Reactivity_And_Properties.md)** — `@api`, `@track`,
  getters, reactivity rules.

### Part C — Making it talk
- **[05 — Events & component communication](./05_Events_And_Communication.md)** — parent↔child,
  pub/sub, LMS.
- **[06 — Working with Salesforce data](./06_Working_With_Data.md)** — `@wire`, imperative Apex,
  LDS.
- **[07 — Lightning Data Service & base components](./07_LDS_And_Base_Components.md)** — record
  forms without Apex.
- **[08 — Navigation & the NavigationMixin](./08_Navigation.md)** — moving around the app.

### Part D — Polish & quality
- **[09 — Lifecycle hooks](./09_Lifecycle_Hooks.md)** — `connectedCallback`, `renderedCallback`,
  etc.
- **[10 — Styling, SLDS & the shadow DOM](./10_Styling_And_Shadow_DOM.md)** — CSS scoping.
- **[11 — Testing with Jest](./11_Testing_With_Jest.md)** — `sfdx-lwc-jest`.
- **[12 — Performance & best practices](./12_Performance_And_Best_Practices.md)** — caching,
  pitfalls.

### Part E — Practice
- **[13 — Hands-on lab](./13_Hands_On_Lab.md)** — build a real account-search component.
- **[14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)** — rapid-fire Q&A.

---

## 🧠 The whole course in three sentences

1. **LWC is built on real web standards (Web Components)** — so it's lightweight and fast, and
   what you learn transfers beyond Salesforce.
2. **A component is three files (HTML + JS + meta)** that render UI, react to data changes, and
   communicate up via **events** and down via **public `@api` properties**.
3. **You get Salesforce data two ways** — **declaratively with `@wire`** (cached, reactive) or
   **imperatively** by calling Apex — and for simple record CRUD, **Lightning Data Service**
   means no Apex at all.

If you can say those three sentences and explain each, you've got the backbone.

---

## 🛠️ Tools for the lab (Lesson 13)
- A **Salesforce Developer Edition / scratch org** and the **Salesforce CLI (`sf`)**.
- **VS Code** + **Salesforce Extension Pack**, and **Node.js** (for Jest tests).

You've got this. Start at **[00](./00_What_Is_LWC.md)**.
