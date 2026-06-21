# 06 — Prompt Builder & Templates

## 🧠 The One Idea

**A prompt template is a fill-in-the-blanks form for the AI.** Instead of writing a fresh prompt
every time, you build a **reusable template** with placeholders ("Summarize case {Case.Subject}
for {Contact.FirstName}") that Salesforce **fills with real record data** before sending it to the
LLM. It's how admins create reliable, grounded generative features without code.

The one-liner: **"Prompt Builder creates reusable, data-grounded prompt templates for generative
AI."**

---

## 1. Why templates beat ad-hoc prompts

- **Consistency** — same structure every time → predictable output.
- **Grounding built in** — merge **real record/Data Cloud fields** so output is about *this*
  customer.
- **Reusable** — one template powers many records, flows, and **agent actions**.
- **Governed** — versioned, testable, and wrapped by the **Trust Layer**.

---

## 2. The prompt template types

| Type | Produces | Example |
|---|---|---|
| **Sales/Field Generation** | text for a field | a generated email-body field |
| **Email** | a draft email | personalized outreach |
| **Record Summary** | a summary of a record | "summarize this account/case" |
| **Flex / freeform** | general-purpose prompt | classify, extract, custom tasks |

(Names evolve across releases; the idea — typed, reusable templates — is stable.)

---

## 3. Grounding a template (the key skill)

You insert **merge fields / resources** into the template:
- **Record fields** — `{!Contact.Name}`, related records.
- **Data Cloud** — unified profile attributes, calculated insights.
- **Flow / Apex** resources — pull computed values.
- **Knowledge / retrieval** — relevant articles (RAG, Lesson 07).

At runtime, Salesforce **resolves** these to actual values, so the LLM sees facts, not
placeholders.

---

## 4. Building & testing in Prompt Builder

1. Pick a **type** and a **target object**.
2. Write the prompt with **merge fields** and clear instructions.
3. **Preview** against a real record to see the resolved prompt and the model's output.
4. Iterate on wording; **save/version**.
5. Use it — in a record page, a Flow, or as an **agent action**.

The **preview-on-real-data** loop is what makes prompts reliable.

---

## 5. Prompt engineering tips (that interviewers like)

- **Be explicit** about format ("3 bullet points, under 50 words").
- **Give the model only relevant grounding** — too much context dilutes/raises cost.
- **Set tone/persona** ("professional, empathetic").
- **Constrain** ("If data is missing, say so — don't invent").
- Iterate using **preview** with varied records.

---

## 6. How this connects to agents

A saved prompt template can be a **prompt-template action** (Lesson 05). So Agentforce reuses the
same governed, grounded prompts your admins built — the agent just **invokes** them. Prompt Builder
is the **generative content factory**; Agentforce is the **autonomous consumer**.

---

## 🎤 Say this in the interview

- *"**Prompt Builder** makes **reusable, grounded prompt templates** — placeholders resolved with
  **real record/Data Cloud data** before hitting the LLM."*
- *"I **ground** with merge fields (records, insights, knowledge), **preview on real data**, and
  **version** templates."*
- *"Templates double as **agent actions**, so Agentforce reuses governed prompts under the **Trust
  Layer**."*

➡️ **Next:** [07 — Grounding with Data Cloud & RAG](./07_Grounding_And_RAG.md)
