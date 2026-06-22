# 00 — What is Agentforce

## 🧠 The One Idea

**Agentforce is the difference between a vending machine and an employee.** A chatbot is a vending
machine: press a button, get a canned response. An **agent** is like a junior employee: you give
it a **goal** ("resolve this customer's billing issue"), and it figures out the steps, looks up
the data, takes actions, and only asks you when it's stuck. That autonomy — **reason, then act** —
is what "agentic AI" means.

The one-liner: **"Agentforce builds autonomous AI agents that reason about a goal and take real
actions in Salesforce."**

---

## 1. Chatbot vs copilot vs agent

| | **Chatbot** | **Copilot / assistant** | **Agent (Agentforce)** |
|---|---|---|---|
| Behavior | scripted replies | helps a human, on request | **acts autonomously** toward a goal |
| Who drives | rigid decision tree | the human | **the agent** plans steps |
| Takes actions? | limited | suggests | **yes — executes** (with guardrails) |

The leap: agents **decide what to do**, not just **what to say**.

---

## 2. What makes something "agentic"

Four ingredients (you'll meet each later):
1. **A goal/role** — what the agent is for.
2. **Reasoning** — the **Atlas Reasoning Engine** plans which step to take (Lesson 03).
3. **Actions** — concrete capabilities it can invoke (flows, Apex, prompts — Lesson 05).
4. **Grounding + guardrails** — real data (Data Cloud) + safety limits (Trust Layer).

---

## 3. A day in the life of an agent

A customer says *"Where's my order and can I change the address?"* A service agent:
1. **Understands** intent (track + update order).
2. **Grounds** on Data Cloud/CRM to find the order.
3. **Acts**: calls a "get shipping status" action, then an "update address" action.
4. **Responds** in natural language, citing the real order.
5. **Escalates** to a human if it's outside its guardrails.

No human wrote that exact script — the agent **assembled** it.

---

## 4. Why this matters now

- **Scale:** agents handle routine work 24/7 across service, sales, marketing, commerce.
- **Built into Salesforce:** they act on your **real CRM + Data Cloud** data, not a separate silo.
- **Career signal:** "Agentforce" is the most-hyped recent Salesforce skill — knowing the
  concepts (not just buzzwords) stands out.

---

## 5. What you'll build

By the end you'll understand how to assemble an agent from **topics** and **actions**, **ground**
it in data, **test** it, **deploy** it to a channel, and keep it **trustworthy** — and you'll
build a small service agent in the lab.

---

## 🌍 Real-World Example

**A telecom that cut handle time without cutting staff.** A mobile carrier's support line was
drowning in "where's my order / change my plan / why is my bill high" tickets. They deployed an
Agentforce Service Agent on web chat and WhatsApp. For *"my bill jumped this month,"* the agent
grounded on the customer's real usage and plan, explained the overage in plain language, offered a
better plan, and applied it after confirmation — no rep involved. Anything outside its guardrails
(a disputed charge over a threshold) was escalated to a human with the full context attached. The
routine 70% it handled end-to-end; the human team focused on the hard 30%.

---

## 🔬 Under the Hood (In-Depth)

- **"Goal → plan" is the whole leap** — a chatbot maps an utterance to a scripted branch; an agent
  takes a *goal* and lets Atlas assemble the steps at runtime, so it handles requests no one
  scripted.
- **Autonomy is bounded, not unlimited** — the agent can only call the actions you attached and
  must obey its instructions, so "autonomous" means *plans freely within a fenced yard*, not "does
  anything."
- **It runs on your real data** — because agents sit inside Salesforce, grounding reads live CRM and
  Data Cloud, which is what makes the actions (refund, address change) real rather than simulated.
- **Escalation is a first-class outcome** — a well-built agent treats "hand to a human" as a valid
  success path, not a failure, which is what makes autonomy safe to ship.
- **The four ingredients map to four lessons** — goal/role (this lesson), reasoning (Atlas, L03),
  actions (L05), grounding + guardrails (L07 + L11) — keep that map and the course stays coherent.

---

## 🎤 Say this in the interview

- *"Agentforce builds **autonomous agents** that, given a **goal**, **reason** about the steps and
  **take real actions** — beyond a scripted chatbot or a human-driven copilot."*
- *"An agent = **role + reasoning (Atlas) + actions + grounding/guardrails**."*
- *"It acts on **real CRM and Data Cloud** data and **escalates** when it hits its guardrails."*

➡️ **Next:** [01 — The Salesforce AI landscape](./01_AI_Landscape.md)
