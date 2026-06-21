# 🌩️ Salesforce Courses — From Scratch to Interview-Ready

A set of **from-zero deep dives** into the four Salesforce skills that show up most on
job descriptions and in interview rounds: **Apex, Lightning Web Components (LWC),
Data Cloud, and Agentforce**. Everything is explained in **naive, everyday language**
first (with analogies), then the real mechanics, then **interview-ready one-liners**.

> 🌐 **Read it online:** **<https://salesforceprep.netlify.app/>** — the friendliest way to
> read these courses (search, dark mode, and easy navigation).

> **How to read this:** pick a course, open its `README.md`, and work the lessons in
> order (00 → end). Every lesson follows the same shape:
> **"The One Idea"** (a plain-English analogy) → real details → **"Say this in the
> interview"** lines you can repeat almost verbatim → a `Next` link. Don't skip the
> analogies — they're the hooks that make the rest stick.

---

## 📚 The four courses

| Course | What it covers | Start here |
|---|---|---|
| **Apex** | Salesforce's backend language: data model, SOQL/DML, triggers, governor limits, async, testing, integration | [Apex](./docs/Salesforce_Apex_From_Scratch/) |
| **LWC** | Lightning Web Components: the modern Salesforce UI framework (HTML/JS/CSS, reactivity, Apex wiring, Jest) | [LWC](./docs/Salesforce_LWC_From_Scratch/) |
| **Data Cloud** | Salesforce's CDP (a.k.a. Data 360): data streams, DLO/DMO, identity resolution, insights, segmentation, activation | [Data Cloud](./docs/Salesforce_Data_Cloud_From_Scratch/) |
| **Agentforce** | Salesforce's agentic AI platform: agents, topics, actions, the Atlas Reasoning Engine, grounding, the Trust Layer | [Agentforce](./docs/Salesforce_Agentforce_From_Scratch/) |

---

## 🧭 Suggested order (if you're starting fresh)

1. **Apex** — the backbone. Almost every other skill assumes you understand the data
   model, SOQL, and governor limits.
2. **LWC** — the modern front end. It calls Apex, so do it second.
3. **Data Cloud** — how Salesforce unifies customer data; increasingly the foundation
   for AI.
4. **Agentforce** — the newest layer. It's far easier once you understand Apex
   (custom actions), LWC (custom UI), and Data Cloud (grounding/RAG).

If you're prepping for a **specific role**, jump straight to the matching course and
finish with its **Interview Q&A Flashcards** lesson.

---

## 🧠 The whole stack in three sentences

1. **Apex is the brain on the server** — it runs your business logic close to the data,
   inside strict "governor limits" that force you to write efficient, bulk-safe code.
2. **LWC is the face** — lightweight web components that render the UI in the browser
   and pull data either declaratively (`@wire`) or imperatively from Apex.
3. **Data Cloud is the memory and Agentforce is the autonomous worker** — Data Cloud
   unifies every customer signal into one profile, and Agentforce reasons over that
   profile to take real actions on your behalf.

---

## 🛠️ Tools you'll want (shared across courses)

- A **Salesforce Developer Edition org** (free, never expires) — sign up at
  developer.salesforce.com.
- **Salesforce CLI (`sf`)** and **VS Code** with the **Salesforce Extension Pack**.
- (For LWC) **Node.js** so you can run **Jest** unit tests locally.
- (For Data Cloud / Agentforce) access to a trial/sandbox that has those features
  enabled — Trailhead Playgrounds and trials are the easiest path.

> Each course's `README.md` lists the exact tools its hands-on lab needs.

You've got this. Pick a course above and start at its **00** lesson. 💪

---

## 🌐 Website & deployment

These courses are published as a website with [MkDocs](https://www.mkdocs.org/) + the
[Material](https://squidfunk.github.io/mkdocs-material/) theme and hosted on **Netlify**:
**<https://salesforceprep.netlify.app/>**.

**Auto-deploy:** Netlify is connected to this repo, so **every push to `main` rebuilds and
redeploys the site automatically** (build settings live in [`netlify.toml`](./netlify.toml)).
Just edit or add a Markdown file under `docs/` and commit — new lessons appear in the navigation
on their own (ordering follows the `00_`, `01_`, … filename prefixes).

**Preview it locally (optional):**

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve        # open http://127.0.0.1:8000
```
