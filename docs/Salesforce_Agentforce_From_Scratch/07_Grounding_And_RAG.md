# 07 — Grounding with Data Cloud & RAG

## 🧠 The One Idea

**Grounding is giving the AI an open-book exam instead of a closed-book one.** Left alone, an LLM
answers from memory and **makes things up**. **Grounding** hands it the relevant pages — this
customer's profile, their orders, the right knowledge article — right when it answers, so it
responds with **facts**. **RAG** (Retrieval-Augmented Generation) is the technique that does this.

The one-liner: **"Grounding feeds the agent real, retrieved data so it answers from facts, not
guesses."**

---

## 1. The RAG pattern

1. **Retrieve** — find the most relevant data for the question (profile, records, articles).
2. **Augment** — insert that data into the prompt as context.
3. **Generate** — the LLM answers **using** the provided context.

The agent's quality lives or dies on **step 1**: retrieve the right, fresh, minimal context.

---

## 2. Sources of grounding

- **CRM records** — the account/case/opportunity in front of the user.
- **Data Cloud** — the **unified profile**, **calculated insights**, and engagement history (see
  the Data Cloud course).
- **Knowledge / documents** — articles, PDFs, FAQs (unstructured).
- **Action outputs** — fresh values fetched by a Flow/Apex action at runtime.

---

## 3. Structured vs unstructured grounding

- **Structured** — fielded data (profile attributes, insights, order rows). Retrieved via
  queries / **Data Graphs** (fast, pre-joined profile views).
- **Unstructured** — free text (knowledge, docs). Chunked, **embedded as vectors**, and retrieved
  by **semantic search** (meaning, not keywords).

Agentforce can ground on **both** in one answer.

---

## 4. Vector / semantic search

For unstructured content, text is converted to **embeddings** (vectors) and stored in a **search
index** (Data Cloud's vector capability). At query time, the question is embedded and the
**closest** chunks are retrieved — so "how do I return a damaged item?" finds the returns policy
even if it doesn't share keywords.

---

## 5. Why Data Cloud is the ideal grounding layer

- It already **unifies and harmonizes** customer data (one profile, not silos).
- **Data Graphs** give **low-latency** reads so grounding doesn't slow the agent.
- **Consent and governance** travel with the data (Lesson 11 + Data Cloud course).

This is why "Agentforce + Data Cloud" is such a common pairing in interviews.

---

## 6. Grounding best practices

- Retrieve **relevant + minimal** context (more isn't better — it costs tokens and adds noise).
- Keep grounding **fresh** (real-time profile, current order status).
- Instruct the model to **admit when data is missing** rather than invent.
- Respect **consent/security** on every grounded field.

---

## 🎤 Say this in the interview

- *"**Grounding** = open-book AI: I retrieve real data (CRM, **Data Cloud** profile/insights,
  knowledge) and inject it so the agent answers from facts."*
- *"The pattern is **RAG**; unstructured content is **embedded as vectors** and fetched via
  **semantic search**, structured data via queries/**Data Graphs**."*
- *"I keep context **relevant, minimal, fresh, and consented**, and tell the model to **say when
  data is missing**."*

➡️ **Next:** [08 — Building an agent](./08_Building_An_Agent.md)
