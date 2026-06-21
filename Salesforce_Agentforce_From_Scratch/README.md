# 🤖 Agentforce From Scratch — A Crash Course (in plain English)

A from-zero deep dive into **Agentforce**, Salesforce's platform for building **autonomous AI
agents**: *what an agent is, how it reasons, how you build one, and how to keep it trustworthy* —
explained in **naive, everyday language** with analogies, then the real mechanics, then
**interview-ready lines**.

> **How to read this:** go in order, 00 → 14. Each lesson starts with a plain-English analogy
> (**"The One Idea"**), then the real details, then **"Say this in the interview"** one-liners
> you can repeat almost verbatim. Don't skip the analogies — they're the hooks that make the
> rest stick.
>
> **Freshness note:** Agentforce evolves fast (Agent Builder, then Agentforce Builder + **Agent
> Script** in late 2025). This course teaches the **durable concepts** — agents, topics, actions,
> grounding, the Trust Layer — and flags newer authoring tools where relevant.

---

## 📂 The lessons (read in order)

### Part A — The mental model
- **[00 — What is Agentforce](./00_What_Is_Agentforce.md)** — agentic AI vs chatbots vs copilots.
- **[01 — The Salesforce AI landscape](./01_AI_Landscape.md)** — Einstein, Prompt Builder,
  Agentforce, the Trust Layer.
- **[02 — Core concepts: agents, topics, actions](./02_Core_Concepts.md)** — the anatomy of an
  agent.

### Part B — How it thinks
- **[03 — The Atlas Reasoning Engine](./03_Atlas_Reasoning_Engine.md)** — how an agent plans and
  acts.
- **[04 — Topics & instructions](./04_Topics_And_Instructions.md)** — scoping what an agent does.
- **[05 — Actions](./05_Actions.md)** — flows, Apex, prompts, standard actions.

### Part C — Grounding & prompts
- **[06 — Prompt Builder & templates](./06_Prompt_Builder.md)** — reusable, grounded prompts.
- **[07 — Grounding with Data Cloud & RAG](./07_Grounding_And_RAG.md)** — feeding the agent facts.

### Part D — Build, test, ship
- **[08 — Building an agent](./08_Building_An_Agent.md)** — Agent/Agentforce Builder end-to-end.
- **[09 — Testing agents](./09_Testing_Agents.md)** — Testing Center & evaluation.
- **[10 — Deployment & channels](./10_Deployment_And_Channels.md)** — where agents run.

### Part E — Trust & operations
- **[11 — The Einstein Trust Layer](./11_Einstein_Trust_Layer.md)** — secure, safe AI.
- **[12 — Governance, monitoring & limits](./12_Governance_And_Monitoring.md)** — running agents
  responsibly.

### Part F — Practice
- **[13 — Hands-on lab](./13_Hands_On_Lab.md)** — build a service agent with a custom action.
- **[14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)** — rapid-fire Q&A.

---

## 🧠 The whole course in three sentences

1. **Agentforce builds *autonomous* AI agents, not just chatbots** — given a goal, an agent
   **reasons** about what to do and **takes real actions** in Salesforce on its own.
2. **You configure an agent declaratively** from **topics** (jobs it can do) and **actions**
   (the concrete steps — flows, Apex, prompts), and the **Atlas Reasoning Engine** decides which
   to use per request.
3. **Trust and grounding make it usable in the enterprise** — **Data Cloud** grounds answers in
   real customer data, and the **Einstein Trust Layer** keeps that data secure and the AI safe.

If you can say those three sentences and explain each, you've got the backbone.

---

## 🛠️ Tools for the lab (Lesson 13)
- An org with **Agentforce** enabled (Trailhead / trial), **Agent Builder** (or Agentforce
  Builder), and **Prompt Builder**.
- Optional: **Data Cloud** for grounding and **Flow/Apex** for custom actions.

You've got this. Start at **[00](./00_What_Is_Agentforce.md)**.
