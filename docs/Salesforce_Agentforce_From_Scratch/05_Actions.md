# 05 — Actions

## 🧠 The One Idea

**Actions are the agent's hands.** Reasoning (Atlas) decides *what* to do; **actions** are *how* it
actually does things — look up an order, run a calculation, draft an email, update a record. An
agent with no actions can only talk; actions are what let it **act**.

The one-liner: **"An action is a typed capability (Flow, Apex, prompt, or standard) the agent can
invoke to do real work."**

---

## 1. The action types

| Type | What it is | Use when |
|---|---|---|
| **Standard** | prebuilt Salesforce actions | common tasks (query records, draft/send email, knowledge answers) |
| **Flow** | runs an autolaunched **Flow** | low-code multi-step business logic |
| **Apex** | calls an `@InvocableMethod` (or Apex REST) | complex logic, callouts, heavy data work |
| **Prompt template** | runs a generative **prompt** | summarize, generate text, classify |

Most custom behavior is built as **Flow** or **Apex** actions.

---

## 2. Inputs & outputs (the contract)

Every action declares **typed inputs and outputs**. Atlas **maps conversation values into inputs**
and uses **outputs** in its next step or response. Example: a "Get Order Status" action takes
`orderNumber` (input) and returns `status`, `eta` (outputs). Clear input/output **labels and
descriptions** help the engine fill them correctly.

---

## 3. Apex actions (`@InvocableMethod`)

```apex
public with sharing class OrderActions {
    public class Request  { @InvocableVariable public String orderNumber; }
    public class Response { @InvocableVariable public String status; }

    @InvocableMethod(label='Get Order Status'
                     description='Returns the shipping status for an order number')
    public static List<Response> getStatus(List<Request> reqs) {
        // query, call out, etc. — returns a Response per Request
    }
}
```

- The **`label`/`description`** are what the agent "sees" — write them for the LLM.
- Bulk-friendly signature (`List` in/out), same Apex rules as the Apex course (governor limits,
  security, `WITH USER_MODE`).

---

## 4. Flow actions

A reusable, autolaunched **Flow** becomes an action: great for admins to build **multi-step,
low-code** processes (create a case, run approvals, update related records) without Apex. The
Flow's input/output variables become the action's contract.

---

## 5. Prompt-template actions

A **Prompt Builder** template (Lesson 06) can be an action — e.g., "summarize this case," "draft a
reply in the customer's tone." These are **generative** actions, automatically **grounded** with
the record/data you bind into the template.

---

## 6. Action design best practices

- **Single responsibility** per action — small, composable verbs.
- **Descriptive labels/descriptions** — the engine selects and fills actions from these.
- **Validate inputs** and handle errors gracefully (return a clear message, don't crash).
- **Least privilege**: enforce CRUD/FLS in Apex actions; agents act as a (often integration)
  user — scope their permissions tightly.
- Prefer **declarative (Flow)** for simple logic; **Apex** for complex/integration work.

---

## 🎤 Say this in the interview

- *"Actions are the agent's **hands** — **Standard, Flow, Apex (`@InvocableMethod`), and prompt
  templates** — each with **typed inputs/outputs** Atlas maps from the conversation."*
- *"**Labels/descriptions** matter because the engine **selects and fills** actions from them; I
  keep actions **single-purpose**."*
- *"Apex actions follow normal Apex rules — **bulkified, secure (CRUD/FLS), least privilege** — and
  I use **Flow** for low-code logic."*

➡️ **Next:** [06 — Prompt Builder & templates](./06_Prompt_Builder.md)
