# 14 — Interview Q&A Flashcards

Rapid-fire questions with crisp, repeatable answers. Cover the card's answer, say yours, then
check. Aim to deliver each in **2–3 sentences**.

---

## Fundamentals

**Q: What is Agentforce?**
A: Salesforce's platform for building **autonomous AI agents** that, given a goal, **reason** about
the steps and **take real actions** in Salesforce — beyond a scripted chatbot or a human-driven
copilot.

**Q: Chatbot vs copilot vs agent?**
A: A **chatbot** gives scripted replies; a **copilot** assists a human on request; an **agent**
**acts autonomously** toward a goal, planning and executing steps with guardrails.

**Q: What makes something "agentic"?**
A: A **goal/role**, **reasoning** (Atlas), **actions** it can invoke, and **grounding + guardrails**
— it decides *what to do*, not just *what to say*.

---

## Architecture

**Q: What's the core hierarchy?**
A: **Agent → Topics → Actions.** Topics are scoped jobs (chosen by their description), actions are
the concrete steps, and **instructions** guide behavior at agent and topic level.

**Q: What is the Atlas Reasoning Engine?**
A: The agent's "brain." Each turn it **interprets → routes to a topic → grounds → acts → reflects →
responds**, looping if needed — not just predicting text.

**Q: What is hybrid reasoning?**
A: Atlas mixes **deterministic** steps (predictable routing/tool-calls, no LLM) with
**probabilistic** LLM judgment — so agents are both **controllable and smart**.

**Q: What are Agent Script and Agent Graph?**
A: Newer (late-2025) authoring: **Agent Script** is a portable, code-like language compiled into an
**Agent Graph** that Atlas executes — finer control over the same topics/actions/instructions.

---

## Topics, Actions & Prompts

**Q: Why is a topic's description so important?**
A: Atlas routes by **matching user intent to topic descriptions**, so vague descriptions cause
**misrouting**. Specific scope + example phrasings = accurate routing.

**Q: What action types exist?**
A: **Standard** (prebuilt), **Flow** (low-code), **Apex** (`@InvocableMethod`, complex/integration),
and **prompt-template** (generative) — each with **typed inputs/outputs** Atlas maps from the
conversation.

**Q: How does an agent call Apex?**
A: Via an **`@InvocableMethod`** with `@InvocableVariable` inputs/outputs; the **label/description**
are what the engine reads, and normal Apex rules apply (bulkified, CRUD/FLS, least privilege).

**Q: What is Prompt Builder?**
A: A tool to create **reusable, grounded prompt templates** — placeholders resolved with **real
record/Data Cloud data** before hitting the LLM; templates can double as **agent actions**.

---

## Grounding & Trust

**Q: What is grounding / RAG?**
A: **Grounding** feeds the agent **real retrieved data** so it answers from facts. **RAG** =
**Retrieve → Augment → Generate**: find relevant context, inject it, then the LLM answers using it.

**Q: Structured vs unstructured grounding?**
A: **Structured** = fielded data via queries/**Data Graphs**; **unstructured** = free text
**embedded as vectors** and fetched by **semantic search**. Agentforce can use both at once.

**Q: Why pair Agentforce with Data Cloud?**
A: Data Cloud provides a **unified, harmonized profile** with **low-latency Data Graphs** and
**consent/governance** baked in — the ideal grounding layer.

**Q: What is the Einstein Trust Layer?**
A: A security wrapper on **every** AI call, **both directions**: **secure grounding + PII masking +
prompt defense** in; **toxicity scoring + demasking + audit** out — plus **zero data retention**.

---

## Build, Test, Run

**Q: How do you build an agent?**
A: **Declaratively** in Agent Builder: role → **topics** → **actions** → **instructions** →
**grounding** → test → deploy — reusing existing Flows, Apex invocables, and prompt templates.

**Q: How do you test an agent?**
A: On **behavior and outcomes** (right topic/action/result), not exact strings, across **many
phrasings** — using the **conversation preview + reasoning trace** and **Agentforce Testing
Center** for batch/regression runs.

**Q: How do agents reach users?**
A: One agent, **many channels** — web/Experience Cloud, in-app, **Slack**, **messaging
(WhatsApp/SMS)**, internal UI, and the **Agent API**. Config is **metadata**, so it follows normal
ALM.

**Q: How do you govern and monitor agents?**
A: **Least-privilege agent user**, scoped topics/actions, instructions-as-policy; monitor
**transcripts, reasoning traces, analytics (deflection/escalation)** and the **Trust Layer audit
trail**, feeding failures back into regression tests.

**Q: What about cost and limits?**
A: Usage is **metered** by conversations/actions (so volume = cost), and Apex/Flow actions still
obey **governor limits** — so keep grounding **minimal** and actions **well-scoped**.

---

## The 30-second summary

*"Agentforce builds **autonomous agents** = **Agent → Topics → Actions**, run by the **Atlas**
reasoning engine. You build them **declaratively**, **ground** them in **Data Cloud/CRM**, secure
every call with the **Einstein Trust Layer**, **test** on behavior in Testing Center, deploy across
**channels**, and **monitor + govern** them like a managed product."*

🎉 **You've finished the Agentforce course.** Back to the [course index](./README.md).
