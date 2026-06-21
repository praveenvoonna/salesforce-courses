# 01 — The Salesforce AI Landscape

## 🧠 The One Idea

**Salesforce AI is a layer cake, and Agentforce is the top layer.** At the bottom are **models**
and the **Trust Layer**; in the middle are **prompts** and **Einstein** features; on top sit
**autonomous agents**. Knowing which layer does what stops the buzzwords (Einstein, Copilot,
Prompt Builder, Agentforce) from blurring together.

The one-liner: **"Models + Trust Layer at the base, Prompt Builder/Einstein in the middle,
Agentforce on top."**

---

## 1. The layers

| Layer | What it is |
|---|---|
| **Foundation models** | LLMs (Salesforce's own + partners like OpenAI/Anthropic) via the **Einstein/models** gateway |
| **Einstein Trust Layer** | security/safety wrapper around every AI call (Lesson 11) |
| **Prompt Builder** | reusable, grounded **prompt templates** (Lesson 06) |
| **Einstein features** | predictions, generative replies, summaries baked into clouds |
| **Agentforce** | autonomous **agents** that reason and act (the focus of this course) |

Agentforce **sits on top of** and **uses** everything below it.

---

## 2. The names you'll hear (decoded)

- **Einstein** — the umbrella brand for Salesforce AI (predictive + generative).
- **Einstein Copilot** — the earlier **assistant** inside Salesforce; conceptually rolled into the
  Agentforce era as an **assistant-style agent**.
- **Prompt Builder** — admin tool to create grounded prompt templates.
- **Model Builder / Einstein Studio** — bring/train models, BYO LLM.
- **Agentforce** — build and run **autonomous agents**.
- **Atlas Reasoning Engine** — the "brain" that powers agent reasoning (Lesson 03).

---

## 3. Predictive vs generative vs agentic

- **Predictive AI** — scores/forecasts (lead scoring, churn) — classic Einstein.
- **Generative AI** — creates text/content (email drafts, summaries) — prompts + LLMs.
- **Agentic AI** — **reasons and acts** toward goals — Agentforce.

Agents often **use** generative and predictive pieces as actions.

---

## 4. How the pieces fit in one request

```
User → Agent (Agentforce)
         │  Atlas reasons: which topic? which action?
         ├─► Action: a Flow / Apex / Prompt template (generative)
         ├─► Grounding: Data Cloud / CRM (real facts)
         └─► every model call wrapped by the Einstein Trust Layer
```

That single picture connects all four prior names.

---

## 5. Where data fits (Data Cloud)

AI is only as good as its context. **Data Cloud** (the other course) provides the **grounding** —
unified profiles, insights, and knowledge — so Einstein and Agentforce answer from **real**
customer data instead of guessing (Lesson 07).

---

## 6. Why interviewers test this

Candidates often parrot "Agentforce = AI." The differentiator is explaining **the stack**: that
agents **orchestrate** prompts, actions, grounding, and models, all under the **Trust Layer**.

---

## 🎤 Say this in the interview

- *"Salesforce AI is layered: **foundation models + Einstein Trust Layer** at the base, **Prompt
  Builder/Einstein** in the middle, **Agentforce agents** on top."*
- *"**Predictive** (scores), **generative** (content), **agentic** (reason + act) — agents
  orchestrate the first two as actions."*
- *"Every model call is wrapped by the **Trust Layer**, and **Data Cloud** supplies grounding."*

➡️ **Next:** [02 — Core concepts: agents, topics, actions](./02_Core_Concepts.md)
