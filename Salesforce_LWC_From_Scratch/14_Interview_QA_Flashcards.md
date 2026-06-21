# 14 — Interview Q&A Flashcards

Rapid-fire. Cover the answer, say it aloud, then check. Read twice.

---

## Fundamentals

**Q: What is LWC and how is it different from Aura?**
LWC is Salesforce's modern UI framework built on **native Web Components** (standards-based, fast,
lightweight). Aura is the older, heavier, custom framework — now legacy. Build new in LWC.

**Q: What three files make a component?**
**HTML** (template), **JS** (controller extending `LightningElement`), and **`.js-meta.xml`**
(exposure + targets).

**Q: Why won't my component show in App Builder?**
`isExposed` isn't `true`, or the right **`targets`** aren't declared in the meta XML.

---

## Templates & reactivity

**Q: Conditional and loop directives?**
**`lwc:if/elseif/else`** for conditionals; **`for:each`** (with a unique, stable **`key`**) or
`iterator:` for loops.

**Q: Are bindings one-way or two-way?**
**One-way** (JS → DOM). User input comes back via **events**.

**Q: What does `@track` actually do now?**
Fields are reactive on **reassignment** by default; `@track` only adds reactivity to **mutations
inside** objects/arrays. Reassigning with spread is usually cleaner.

**Q: What is `@api`?**
Exposes a **public** property/method; the parent sets it. Treat it as **read-only** in the child;
data flows **down**.

---

## Communication

**Q: How do components communicate?**
**Props down** (`@api`), **events up** (`CustomEvent` with `detail`), and **Lightning Message
Service** for unrelated components.

**Q: What do `bubbles` and `composed` do?**
`bubbles` = climb the DOM; `composed` = cross **shadow DOM** boundaries. Both default false.

---

## Data

**Q: `@wire` vs imperative Apex?**
`@wire` = declarative, **cached**, reactive reads (Apex must be **`cacheable=true`**). Imperative =
you call on demand, needed for **writes** and user actions.

**Q: How make a wire parameter reactive?**
Prefix with **`$`** (e.g., `'$recordId'`).

**Q: How refresh stale wired data after DML?**
**`refreshApex(wiredResult)`**.

**Q: What is Lightning Data Service?**
A shared, cached, **FLS-aware** record layer for **CRUD without Apex** — via
`lightning-record-form`/`-edit-form` or **`uiRecordApi`** wires.

---

## Navigation & lifecycle

**Q: How do you navigate?**
**`NavigationMixin`** with a **page reference** (type + attributes) — never a hard-coded URL.

**Q: Where do you fetch data — which hook?**
**`connectedCallback`** (`@api` props ready). Clean up in **`disconnectedCallback`**.

**Q: Why is `renderedCallback` dangerous?**
It runs after **every** render; setting reactive state there can cause an **infinite loop** —
guard with a flag.

---

## Styling

**Q: What does the shadow DOM do to CSS?**
**Scopes** each component's styles so they don't leak in or out.

**Q: How share styling across the boundary?**
**SLDS** utilities/base components, **CSS custom properties**, and **SLDS styling hooks**; opt
into **Light DOM** only when you must.

---

## Testing & performance

**Q: How do you test LWC?**
**Jest via `sfdx-lwc-jest`** in Node: `createElement`, set props, append, query **`shadowRoot`**,
assert. Await a microtask for async renders; **mock** Apex/wires.

**Q: Top performance practices?**
Cache (`@wire`/LDS), minimize server calls, **debounce** search, **reassign arrays**, stable
**keys**, lazy-load big lists.

**Q: Security note for LWC's Apex?**
Apex from LWC defaults to **system mode** — enforce **CRUD/FLS server-side**
(`WITH USER_MODE`).

---

🎉 That's the LWC course. Loop back to any lesson whose flashcard you couldn't answer cold.
