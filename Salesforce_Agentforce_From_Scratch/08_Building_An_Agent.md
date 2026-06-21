# 08 — Building an Agent

## 🧠 The One Idea

**Building an agent is mostly *describing*, not coding.** In **Agent Builder** (and the newer
**Agentforce Builder**) you point-and-click: define the agent's role, add **topics**, attach
**actions**, write **instructions**, connect **grounding**, then test. The hard engineering
(reasoning, orchestration) is Atlas's job — your job is **clear configuration**.

The one-liner: **"You build agents declaratively in Agent Builder — role, topics, actions,
instructions, grounding, test."**

---

## 1. The build workflow

1. **Create the agent** — choose a type (Service, Sales/SDR, custom) and give it a role/persona.
2. **Define topics** — the jobs it handles, each with a sharp description (Lesson 04).
3. **Add actions** to each topic — standard, Flow, Apex, prompt templates (Lesson 05).
4. **Write instructions** — agent-level + topic-level behavior rules.
5. **Connect grounding** — CRM, Data Cloud, knowledge (Lesson 07).
6. **Test** in the conversation preview (Lesson 09).
7. **Activate & deploy** to channels (Lesson 10).

---

## 2. Agent Builder (the canvas)

- A visual workspace listing **topics** and their **actions/instructions**.
- A **conversation preview** panel to chat with the draft agent live.
- Shows the agent's **reasoning/plan** so you can see *why* it picked a topic/action — invaluable
  for debugging.

(Late-2025 **Agentforce Builder** adds **Agent Script** — a portable language compiled to an
**Agent Graph** — for finer, code-like control. Concepts are the same: topics, actions,
instructions.)

---

## 3. Standard vs custom agents

- **Standard agents** (e.g., **Agentforce Service Agent**, **SDR Agent**) come with sensible
  topics/actions — fastest path to value; customize from there.
- **Custom agents** start blank for bespoke processes.

Most real projects **start from a standard agent and extend it**.

---

## 4. Connecting the pieces

- Reuse existing **Flows** and **Apex `@InvocableMethod`s** as actions — no rebuild.
- Reuse **Prompt Builder** templates as generative actions.
- Bind **Data Cloud / records** for grounding.
- Set the **agent user** and its **permissions** (least privilege — it acts as that user).

Agentforce **orchestrates assets you already have** rather than reinventing them.

---

## 5. The iterate loop

Building is iterative:
1. Add/adjust a topic or action.
2. **Chat with it** in preview using realistic phrasings.
3. Read the **reasoning trace** — did it route correctly? fill inputs right?
4. Refine **descriptions/instructions**.
5. Repeat, then move to formal **testing** (Lesson 09).

Most fixes are **wording** (topic descriptions, instructions), not code.

---

## 6. Common pitfalls

- **Vague topic descriptions** → misrouting (Lesson 04).
- **Over-broad actions** or missing input descriptions → wrong/empty inputs.
- **Too many overlapping topics** → ambiguous routing.
- **No fallback/escalation** topic → dead ends.
- **Over-permissioned agent user** → security risk.

---

## 🎤 Say this in the interview

- *"I build agents **declaratively in Agent Builder**: role → **topics** → **actions** →
  **instructions** → **grounding** → test → deploy."*
- *"I **reuse existing Flows, Apex invocables, and prompt templates** as actions — Agentforce
  orchestrates assets I already have."*
- *"I iterate using the **conversation preview + reasoning trace**, and most fixes are **better
  descriptions/instructions**, not code."*

➡️ **Next:** [09 — Testing agents](./09_Testing_Agents.md)
