# 02 — Core Concepts: Agents, Topics, Actions

## 🧠 The One Idea

**An agent is a department, topics are its job roles, and actions are the tasks each role can
do.** You don't program an agent step-by-step. You **describe** what jobs it can handle
(**topics**) and the concrete things it can do (**actions**), and the reasoning engine picks the
right ones for each request. Get this three-level structure and the whole platform clicks.

The one-liner: **"An agent contains **topics** (jobs), and each topic has **actions** (concrete
steps) + instructions."**

---

## 1. The hierarchy

```
Agent  (the whole assistant, with a role/persona)
 ├─ Topic A: "Order Management"
 │    ├─ Instructions (how to behave for this job)
 │    └─ Actions: Get Order Status, Update Address, Issue Refund
 ├─ Topic B: "Returns"
 │    └─ Actions: Start Return, Check Eligibility
 └─ Topic C: "Escalate to Human"
```

The agent routes each user message to the **best-matching topic**, then uses that topic's
**actions**.

---

## 2. The agent (the container)

An agent has:
- **A role/type** — e.g., **Service Agent**, **Sales SDR**, **internal copilot**.
- **A persona/instructions** — tone, scope, what it must/never do.
- **Channels** — where it runs (Lesson 10).
- A set of **topics** it's allowed to handle.

Salesforce ships **standard agents** (e.g., Agentforce Service Agent, SDR) and lets you build
**custom** ones.

---

## 3. Topics (the jobs)

A **topic** scopes one area of responsibility. It has:
- **A name + description** — used by the engine to decide "does this message belong here?"
- **Instructions** — natural-language rules for behaving within this topic.
- **Actions** — the tools available while in this topic.

Topics keep an agent **focused and predictable** — the engine won't issue a refund while handling
a "store hours" topic if you didn't give it that action there.

---

## 4. Actions (the verbs)

An **action** is a concrete capability the agent can invoke. Types (detailed in Lesson 05):
- **Standard actions** — prebuilt (query records, draft email).
- **Flow** actions — run a Salesforce Flow.
- **Apex** actions — call an `@InvocableMethod` (or Apex REST).
- **Prompt template** actions — run a generative prompt.

Each action has **inputs/outputs** the engine maps from the conversation.

---

## 5. Instructions (the glue)

**Instructions** are natural-language guidance at the agent and topic level: *"Always verify the
customer's identity before sharing order details,"* *"Never promise refunds over $500 — escalate."*
The reasoning engine follows them to stay on-rails. Good instructions = good behavior.

---

## 6. How a request flows (preview)

1. User message → agent.
2. Engine selects the **topic** (by description match).
3. Engine reads the topic's **instructions** + available **actions**.
4. Engine **plans and calls** the right action(s), grounding as needed.
5. Engine composes a natural-language reply.

(That "engine" is **Atlas** — next lesson.)

---

## 🌍 Real-World Example

**One agent, three jobs, zero crossed wires.** A retailer built a single Service Agent with three
topics: *Order Management*, *Returns*, and *Escalate to Human*. When a customer wrote *"the jacket I
got is too small, can I swap it?"*, the agent routed to **Returns** (not Order Management), checked
eligibility with the Returns topic's actions, and started the return — it never even *saw* the
"Issue Refund" action because that lived under a different topic it wasn't in. When a customer asked
something off-script ("can you price-match a competitor?"), it hit the **Escalate** topic and handed
off. The three-level structure (agent → topics → actions) is exactly what kept it from doing the
wrong thing.

---

## 🔬 Under the Hood (In-Depth)

- **Topics are scoping boundaries, not just labels** — an action attached to Topic A is *invisible*
  while the agent is reasoning inside Topic B, which is the core safety mechanism of the model.
- **Routing happens on the topic's description** — Atlas matches the user's intent to topic
  *descriptions*, so the description is effectively code that determines behavior (L04 goes deep).
- **Actions are typed contracts** — each declares inputs/outputs, and Atlas maps conversation values
  into those inputs, so vague input labels cause empty or wrong fills.
- **Instructions layer at two levels** — agent-level (global persona/rules) and topic-level
  (job-specific), and Atlas combines both, so you don't repeat global rules in every topic.
- **You describe, the engine orchestrates** — there's no step-by-step script; the same agent handles
  unseen phrasings because Atlas assembles topic + actions per turn at runtime.

---

## 🎤 Say this in the interview

- *"The hierarchy is **Agent → Topics → Actions**: topics are jobs (scoped by description),
  actions are the concrete steps, and **instructions** guide behavior."*
- *"The agent **routes** each message to the best topic, then uses only **that topic's actions** —
  keeping it focused and safe."*
- *"Actions can be **standard, Flow, Apex, or prompt templates**, each with typed inputs/outputs
  the engine maps from the conversation."*

➡️ **Next:** [03 — The Atlas Reasoning Engine](./03_Atlas_Reasoning_Engine.md)
