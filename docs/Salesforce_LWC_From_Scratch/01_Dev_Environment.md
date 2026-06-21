# 01 — Dev Environment & Tooling

## 🧠 The One Idea

**Modern Salesforce dev is "code on your laptop, deploy to the cloud."** Old-school admins
clicked everything in the browser. Modern LWC development uses **source files in VS Code**, the
**Salesforce CLI** to push/pull them, and **scratch orgs** as disposable test environments.
This is called the **Salesforce DX (SFDX)** model — it makes your work versionable in Git.

The one-liner: **"Salesforce DX = local source + CLI + scratch orgs, so UI dev works like normal
software dev."**

---

## 1. The toolkit

- **VS Code** + the **Salesforce Extension Pack** — the IDE with LWC autocomplete, lint, and
  deploy buttons.
- **Salesforce CLI (`sf`)** — the command-line tool to authorize orgs, deploy, and run tests.
- **Node.js** — needed so you can run **Jest** unit tests locally (Lesson 11).
- A **Dev Hub** (a special org capability) to create **scratch orgs**.

---

## 2. Org types you'll use

| Org | What it's for |
|---|---|
| **Developer Edition** | free permanent personal org; easiest to start |
| **Scratch org** | disposable, source-driven org spun up from config; lives days |
| **Sandbox** | a copy of production for dev/test |
| **Production** | the real org |

Scratch orgs embody the SFDX idea: your **source of truth is the files**, not the org.

---

## 3. The commands you'll repeat

```bash
sf org login web                       # authorize an org in the browser
sf project generate --name myApp       # create a DX project
sf org create scratch -f config/project-scratch-def.json -a myScratch
sf project deploy start                # push local source → org
sf project retrieve start              # pull org changes → local
sf apex run test --code-coverage       # run Apex tests
npm run test:unit                      # run LWC Jest tests
```

---

## 4. Project structure

A DX project keeps metadata under `force-app/main/default/`:

```
force-app/main/default/
├── lwc/                    # your Lightning Web Components
│   └── accountList/
│       ├── accountList.html
│       ├── accountList.js
│       └── accountList.js-meta.xml
├── classes/                # Apex
└── objects/                # custom objects/fields
```

Each LWC lives in its **own folder**, and the folder name = the component name.

---

## 5. Creating a component

```bash
sf lightning generate component --type lwc --name accountList \
  --output-dir force-app/main/default/lwc
```

This scaffolds the three core files (next lesson). In VS Code you can also right-click the `lwc`
folder → **SFDX: Create Lightning Web Component**.

---

## 6. Why this matters for interviews

It shows you can work in a **team/CI** way: source-controlled metadata, repeatable scratch orgs,
automated tests. Many shops ask "how do you deploy?" — the modern answer is **`sf project deploy`
from a Git-tracked DX project**, not clicking through change sets.

---

## 🎤 Say this in the interview

- *"I develop with **Salesforce DX**: source in VS Code, the **`sf` CLI** to deploy, and
  **scratch orgs** as disposable environments — all Git-friendly."*
- *"Each LWC is a **folder** with `.html`, `.js`, and `.js-meta.xml`; the folder name is the
  component name."*
- *"I run **Apex tests** and **Jest** tests from the CLI, which slots into CI/CD."*

➡️ **Next:** [02 — Anatomy of a component](./02_Component_Anatomy.md)
