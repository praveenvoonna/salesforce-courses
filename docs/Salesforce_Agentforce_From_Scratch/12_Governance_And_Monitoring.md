# 12 — Governance, Monitoring & Limits

## 🧠 The One Idea

**An agent is an employee you must manage, not a gadget you switch on.** Once it's live it keeps
acting on real data with real customers, so you need the same things you'd give a new hire:
**clear permissions**, a **manager watching the work**, **performance reviews**, and **a budget**.
That's governance (rules + permissions), monitoring (watching live behavior), and limits (the
budget/quotas it runs within).

The one-liner: **"Govern with permissions and guardrails, monitor with analytics and logs, and
respect usage limits."**

---

## 1. Governance — who can do what

- **Agent user & permissions** — the agent acts **as a user**; scope it with **least privilege**
  so it can only touch what it needs.
- **Topic/action scope** — it can only do actions you attached; absent capabilities can't be
  invoked.
- **Instructions as policy** — explicit "always/never" rules and **escalation** paths.
- **Change control** — agent config is **metadata**, so changes go through **sandbox → test →
  deploy** with reviews (Lesson 10).

---

## 2. Monitoring — watch the live work

- **Conversation transcripts / history** — what users asked and how the agent responded.
- **Reasoning traces** — *why* it chose a topic/action (the same trace used in testing).
- **Agentforce analytics / dashboards** — volumes, **deflection/resolution**, escalation rate,
  topic usage, satisfaction.
- **Trust Layer audit trail** — prompts, responses, masking, and **toxicity scores** (Lesson 11).

You watch these to catch drift, misrouting, and unhappy outcomes early.

---

## 3. The feedback loop (prod → improvement)

1. **Spot failures** in transcripts/analytics (misroutes, dead-ends, low satisfaction).
2. **Diagnose** with the reasoning trace.
3. **Fix** the topic descriptions, instructions, actions, or grounding.
4. **Add the case** to your **regression test set** (Lesson 09).
5. **Redeploy** and keep watching.

Production traffic is your richest source of test cases.

---

## 4. Limits & cost

- **Usage is metered** — Agentforce is commonly licensed by **conversations/actions**
  (e.g., "Flex" credit-style consumption), so **volume = cost**.
- **Platform limits still apply** — Apex/Flow actions obey normal **governor limits**; callouts
  have timeouts; grounding/queries have their own limits.
- **Design for efficiency** — minimal grounding, well-scoped actions, and avoiding needless model
  calls keep both **latency and cost** down.

---

## 5. Responsible-AI practices

- **Keep a human in the loop** for high-risk actions (refunds over a threshold, data deletion).
- **Be transparent** — let users know they're talking to an AI and offer a human hand-off.
- **Review the audit trail** regularly for bias/safety issues.
- **Honor consent & privacy** on every grounded field (ties to Data Cloud governance).

---

## 6. The operating mindset

Building the agent is ~20% of the lifecycle; **running it well** is the rest. The teams that
succeed treat it like a managed product: **measure, diagnose, refine, repeat** — continuously.

---

## 🎤 Say this in the interview

- *"I **govern** with a **least-privilege agent user**, scoped topics/actions, and instructions as
  policy, all under **metadata change control**."*
- *"I **monitor** transcripts, **reasoning traces**, **Agentforce analytics** (deflection,
  escalation), and the **Trust Layer audit trail**, feeding failures back into regression tests."*
- *"I respect **usage-based cost** and **platform/governor limits**, and keep a **human in the
  loop** for high-risk actions."*

➡️ **Next:** [13 — Hands-on lab](./13_Hands_On_Lab.md)
