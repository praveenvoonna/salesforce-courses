# 10 — Deployment & Channels

## 🧠 The One Idea

**Build the agent once; meet customers everywhere.** You don't rebuild your agent for the website,
the app, Slack, and WhatsApp. You build it **once**, then **connect it to channels** — the doors
through which people talk to it. Deployment is about **activating** the agent and **plugging it
into** the right surfaces with the right settings.

The one-liner: **"One agent, many channels — you activate it and connect surfaces like web, app,
Slack, and messaging."**

---

## 1. What "a channel" means

A **channel** is a surface where the agent is exposed:
- **Web** — embedded chat on a site or **Experience Cloud** page.
- **In-app / mobile** — inside your Salesforce or custom app.
- **Slack** — agents available right in conversations.
- **Messaging** — WhatsApp, SMS, Facebook Messenger via Service Cloud Messaging.
- **Internal (Salesforce UI)** — an employee-facing assistant inside the org.
- **API** — call the agent programmatically (the **Agent API**) from anything.

The same agent definition powers all of them.

---

## 2. Two big audiences

- **Customer-facing agents** (e.g., **Agentforce Service Agent**) — external users; tighter
  guardrails, identity verification, escalation to human reps.
- **Employee-facing agents** (internal copilots) — run inside Salesforce for staff; grounded in
  internal data with employee permissions.

The build is similar; **permissions, channels, and guardrails** differ.

---

## 3. Environments & the release path

Treat agents like any platform feature:
1. **Develop** in a sandbox / dev org.
2. **Test** in Testing Center (Lesson 09).
3. **Deploy** via **metadata / change sets / DevOps** (e.g., `sf` CLI, packages) to higher orgs.
4. **Activate** in production and connect channels.

Agent configuration is **metadata**, so it moves through normal Salesforce ALM.

---

## 4. The agent user & connections

- An agent runs **as a user** (often a dedicated **integration/agent user**) — its **permissions**
  decide what it can see and do. **Least privilege** here is critical.
- Channels may need **connections**: a **Messaging channel**, a **Slack app**, an **Experience
  Cloud site**, or **connected app/auth** for the API.

---

## 5. Go-live checklist

- ✅ Agent **activated** and assigned the right **agent user / permissions**.
- ✅ **Channel(s)** configured (web snippet, Slack app, messaging number, etc.).
- ✅ **Escalation/hand-off** to human reps wired up.
- ✅ **Grounding sources** connected in the target org (Data Cloud, knowledge).
- ✅ **Monitoring** turned on (Lesson 12).

---

## 6. After go-live

Deployment isn't the finish line. You **monitor** real conversations, feed failures back into your
**test set**, and **iterate** on topics/instructions — the same loop as building, now with
production traffic (Lesson 12).

---

## 🎤 Say this in the interview

- *"I build an agent **once** and expose it on **multiple channels** — web/Experience Cloud,
  in-app, **Slack**, **messaging (WhatsApp/SMS)**, internal UI, and the **Agent API**."*
- *"Agent config is **metadata**, so it follows normal **ALM**: dev → test → deploy → activate,
  and it runs as a **least-privilege agent user**."*
- *"Go-live means wiring **channels, escalation, grounding, and monitoring** — then I iterate on
  real traffic."*

➡️ **Next:** [11 — The Einstein Trust Layer](./11_Einstein_Trust_Layer.md)
