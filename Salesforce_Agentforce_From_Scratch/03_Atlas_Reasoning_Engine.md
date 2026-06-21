# 03 — The Atlas Reasoning Engine

## 🧠 The One Idea

**Atlas is the agent's brain — and it's smarter than "just an LLM."** A raw LLM guesses the next
word. **Atlas** is a **reasoning engine** that, on every turn, figures out the user's intent,
picks the right **topic** and **action**, gathers **grounding** data, executes, checks the result,
and loops if needed. It blends **deterministic** steps (predictable code) with **probabilistic**
LLM reasoning — so it's reliable *and* flexible.

The one-liner: **"Atlas is Agentforce's reasoning engine: it plans, retrieves, acts, and
evaluates each turn — not just predicts text."**

---

## 1. Why not "just an LLM"?

A bare LLM is creative but unpredictable — bad for taking real business actions. Atlas wraps the
LLM in a **structured loop** with guardrails so the agent **does the right thing**, consistently,
and stays inside the boundaries you defined.

---

## 2. The reasoning loop (the heart of it)

Each turn, roughly:
1. **Interpret** — what does the user actually want?
2. **Plan / route** — which **topic** fits? which **action(s)**?
3. **Retrieve / ground** — pull facts from Data Cloud/CRM/knowledge (Lesson 07).
4. **Act** — execute the chosen action(s).
5. **Evaluate / reflect** — did it work? is more needed? loop or finish.
6. **Respond** — compose a grounded, natural-language answer.

It can **iterate** (reflective loops) and **coordinate** across topics/subagents.

---

## 3. Hybrid reasoning (deterministic + probabilistic)

A key modern point: Atlas separates **deterministic execution** (predictable, code-like routing
and tool calls) from **probabilistic reasoning** (LLM judgment).
- **Deterministic** steps (which node to run, guard clauses) **don't** involve the LLM →
  predictable.
- **Probabilistic** steps (understanding language, choosing among options) **do**.

This "hybrid reasoning" is why agents can be both **controllable** and **smart**. (Newer authoring
uses **Agent Script** compiled into an **Agent Graph** that Atlas executes — you define the
boundaries, the engine respects them.)

---

## 4. Grounding is part of reasoning

Atlas doesn't reason in a vacuum — it **injects retrieved context** (profile, records, knowledge)
into its decisions. That's what stops hallucination and lets it act on **this** customer's real
situation.

---

## 5. Guardrails & escalation

Atlas enforces the **instructions** and **scope** you set: it won't invoke actions a topic doesn't
have, it follows "never do X" rules, and it **escalates to a human** when confidence is low or the
request is out of bounds. Safety isn't bolted on — it's part of the loop.

---

## 6. What you control vs what Atlas does

- **You** define: topics, actions, instructions, grounding sources, guardrails.
- **Atlas** decides at runtime: intent, routing, which actions to call, when to loop/escalate.

You shape the **boundaries**; the engine handles the **orchestration**.

---

## 🎤 Say this in the interview

- *"**Atlas** is the reasoning engine: each turn it **interprets → routes to a topic → grounds →
  acts → reflects → responds**, looping if needed — not just predicting text."*
- *"It uses **hybrid reasoning**: deterministic routing/tool-calls (predictable) plus
  probabilistic LLM judgment — so agents are controllable *and* smart."*
- *"**Grounding and guardrails are part of the loop**: it injects real data and **escalates** when
  out of scope."*

➡️ **Next:** [04 — Topics & instructions](./04_Topics_And_Instructions.md)
