# 09 — Testing Agents

## 🧠 The One Idea

**Testing an agent is like interviewing a new hire before giving them the keys.** With normal
code, the same input always gives the same output, so testing is easy. An agent is
**probabilistic** — it can phrase things differently or reason down a slightly different path
each time. So you don't test exact strings; you test **behavior**: did it pick the right topic,
call the right action, stay in bounds, and reach the right outcome?

The one-liner: **"You test agents on *behavior and outcomes*, not exact wording — across many
phrasings."**

---

## 1. Why agent testing is different

- **Non-deterministic output** — wording varies; assert on **intent/action**, not text.
- **Routing is the risk** — most failures are the agent picking the **wrong topic** or
  **mis-filling an action's inputs**.
- **Many phrasings** — real users ask the same thing ten ways; you must cover that variety.

---

## 2. The testing tools

| Tool | What it's for |
|---|---|
| **Conversation preview** (in Builder) | quick, manual "chat with the draft" + see the reasoning trace |
| **Agentforce Testing Center** | run **test cases at scale**, batch evaluations, regression runs |
| **Agent API / scripts** | automated/CI-style testing with many utterances |

The preview is for **exploring**; Testing Center is for **proving** it works repeatably.

---

## 3. What a test case looks like

A test case typically specifies:
- **Utterance** — the user input ("where's my order #1234?").
- **Expected topic** — which job should handle it.
- **Expected action(s)** — what it should call.
- **Expected outcome** — the result/behavior (e.g., returns a status, escalates, refuses).

You run many of these and measure **pass rate**, then fix the misses.

---

## 4. The reasoning trace (your debugger)

Every turn, the agent exposes **why** it did what it did: the chosen topic, the plan, the actions
called, and the inputs it mapped. When something's wrong, read the trace to localize it:
- Wrong **topic**? → fix the topic **description**.
- Right topic, wrong/empty **inputs**? → fix the action's **input descriptions**.
- Right action, bad **answer**? → fix **grounding** or **instructions**.

---

## 5. Build a test set that mirrors reality

- **Happy paths** — the common requests, in **many phrasings**.
- **Edge cases** — missing data, ambiguous asks, multiple intents in one message.
- **Out-of-scope** — things it should **refuse or escalate**.
- **Adversarial** — prompt-injection / "ignore your rules" attempts (Trust Layer, Lesson 11).

Aim for coverage of **every topic** and every **escalation** path.

---

## 6. The test → fix loop

1. Run the test set in **Testing Center**.
2. Triage failures with the **reasoning trace**.
3. Fix the **wording** (descriptions/instructions) or the **action**.
4. **Re-run** to catch regressions.
5. Repeat until pass rate is acceptable, then keep the set for **regression** on every change.

Most fixes are **configuration**, not code.

---

## 🎤 Say this in the interview

- *"Agents are **probabilistic**, so I test **behavior and outcomes** — right **topic**, right
  **action**, right result — across **many phrasings**, not exact strings."*
- *"I use the **conversation preview + reasoning trace** to debug and **Agentforce Testing
  Center** to run **batch test cases** and **regressions**."*
- *"My test set covers **happy paths, edge cases, out-of-scope escalations, and adversarial
  prompts**, and most fixes are **descriptions/instructions**, not code."*

➡️ **Next:** [10 — Deployment & channels](./10_Deployment_And_Channels.md)
