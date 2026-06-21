# 04 — Topics & Instructions

## 🧠 The One Idea

**Topics are the agent's table of contents; instructions are the rules of the house.** A **topic**
tells the agent *"this kind of request belongs to this job."* **Instructions** tell it *"and here's
exactly how to behave while doing that job."* Together they turn a vague AI into a focused,
predictable worker.

The one-liner: **"Topics scope *what* an agent handles; instructions govern *how* it behaves."**

---

## 1. Anatomy of a topic

A topic has four parts:
1. **Name** — short label ("Order Management").
2. **Classification description** — *the most important field*: it's how Atlas decides whether a
   message belongs to this topic. Write it clearly and specifically.
3. **Instructions** — natural-language behavior rules for this topic.
4. **Actions** — the tools available within this topic.

---

## 2. Why the description matters so much

Atlas routes by **matching the user's intent to topic descriptions**. Vague descriptions cause
**misrouting** (the agent picks the wrong job). Compare:

- ❌ "Handles stuff about orders."
- ✅ "Use when the customer asks about an existing order's status, shipping, delivery date, or
  wants to change/cancel an order they already placed."

Specific scope + example phrasings = accurate routing.

---

## 3. Writing good instructions

Instructions are plain English, but treat them like **policy**:
- Be **imperative and specific**: *"Always confirm the order number before making changes."*
- State **boundaries**: *"Never issue a refund over $500 — use the Escalate action."*
- Define **sequence** when order matters: *"First verify identity, then retrieve the order."*
- Reference **actions by name** so the engine knows what to call.

Vague instructions → unpredictable agents. Tight instructions → reliable ones.

---

## 4. Standard vs custom topics

- **Standard topics** ship with standard agents (e.g., the Service Agent has common service
  topics) — fast start.
- **Custom topics** you author for your business processes.
- You can **mix**: keep useful standard topics, add custom ones.

---

## 5. Keeping topics from overlapping

If two topics have **similar descriptions**, Atlas may route ambiguously. Best practices:
- Make each topic's scope **distinct and non-overlapping**.
- Use a dedicated **"fallback / escalate to human"** topic for anything unmatched.
- Test routing with varied phrasings (Lesson 09) and refine descriptions.

---

## 6. Instructions at two levels

- **Agent-level** instructions: global persona, tone, universal rules ("be concise, never share
  internal IDs").
- **Topic-level** instructions: rules specific to that job.

The engine combines both — global guardrails plus job-specific behavior.

---

## 🎤 Say this in the interview

- *"A **topic** = name + **classification description** (drives routing) + **instructions** +
  **actions**; the description quality directly determines routing accuracy."*
- *"**Instructions** are policy in plain English — specific, bounded, sequenced, and referencing
  actions by name."*
- *"I keep topic scopes **distinct**, add a **fallback/escalate** topic, and combine **agent-level**
  and **topic-level** instructions."*

➡️ **Next:** [05 — Actions](./05_Actions.md)
