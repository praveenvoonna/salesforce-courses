# 11 — The Einstein Trust Layer

## 🧠 The One Idea

**The Trust Layer is a security checkpoint that every AI request passes through — both ways.** Think
airport security wrapped around the model: before your data reaches the LLM it's **screened**
(sensitive data masked, the prompt logged), and before the answer comes back it's **screened
again** (toxicity checked, masked data restored). The model never gets to keep your data, and
nothing unsafe slips through.

The one-liner: **"The Einstein Trust Layer secures every AI call — masking, grounding, zero
retention, toxicity scoring, and auditing — in both directions."**

---

## 1. Why it exists

Enterprises won't send customer data to an LLM without guarantees: *Will my data leak? Will the
model train on it? Will it say something harmful or made-up?* The Trust Layer answers all three so
generative AI is **safe to use on real CRM data**.

---

## 2. What happens on the way *in* (request)

1. **Secure data retrieval / grounding** — pull only data the user is **allowed** to see.
2. **Dynamic grounding** — inject that real context into the prompt.
3. **Data masking** — detect and **mask PII/sensitive fields** before the prompt leaves the
   platform (the model sees placeholders, not real SSNs/emails).
4. **Prompt defense** — system guardrails that resist **prompt-injection** / jailbreaks.

---

## 3. What happens on the way *out* (response)

5. **Toxicity / safety scoring** — the response is scored for harmful, biased, or unsafe content.
6. **Demasking** — the masked placeholders are **restored** to real values for the authorized user.
7. **Audit trail & feedback** — the prompt, response, and safety scores are **logged** for
   monitoring and compliance.

---

## 4. Zero data retention

A headline guarantee: with Salesforce's LLM partners, prompts and responses are **not stored by
the model provider** and are **not used to train** their models. The data does its job and is gone
— this is what makes it enterprise-grade.

---

## 5. The pieces, named

- **Secure data retrieval** — respects sharing/permissions.
- **Dynamic grounding** — real, permitted context.
- **Data masking / demasking** — PII protection round-trip.
- **Toxicity detection** — safety scoring of output.
- **Zero retention** — provider doesn't keep/train on your data.
- **Audit trail** — logged for governance (feeds Lesson 12).

These apply to **all** Salesforce generative AI — Prompt Builder, Einstein features, **and
Agentforce**.

---

## 6. Why it matters for agents

Agents act **autonomously** on real data, so trust is non-negotiable. Because Agentforce runs on
the Trust Layer, every prompt, grounded fact, and generated reply is **masked, defended, scored,
and audited** automatically — you get safety **by default**, not as an add-on.

---

## 🎤 Say this in the interview

- *"The **Einstein Trust Layer** wraps every AI call **both ways**: **secure grounding + PII
  masking + prompt defense** in, **toxicity scoring + demasking + audit** out."*
- *"It guarantees **zero data retention** — partner LLMs don't store or train on our data."*
- *"It applies to **all** Salesforce GenAI including **Agentforce**, so agents get safety,
  masking, and auditing **by default**."*

➡️ **Next:** [12 — Governance, monitoring & limits](./12_Governance_And_Monitoring.md)
