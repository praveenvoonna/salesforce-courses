# 04 — Reactivity & Properties

## 🧠 The One Idea

**Reactivity means "change the data, and the screen updates itself."** You never manually edit
the DOM to show a new value — you change a property in JS, and LWC re-renders the affected parts
automatically. The decorators **`@api`**, **`@track`**, and **`@wire`** control *how* properties
behave and who can see them.

The one-liner: **"Change a reactive field and the UI re-renders; decorators control visibility
and behavior."**

---

## 1. Fields are reactive by default

```javascript
export default class Counter extends LightningElement {
    count = 0;                      // reactive: reassigning re-renders
    increment() { this.count++; }   // template updates automatically
}
```

Reassigning a **primitive** field triggers a re-render. No `setState`, no manual refresh.

---

## 2. `@api` — public properties (parent → child)

```javascript
import { api, LightningElement } from 'lwc';
export default class Greeting extends LightningElement {
    @api name;          // parent can set this
    @api recordId;      // auto-populated on record pages
}
```

```html
<c-greeting name="Alice"></c-greeting>
```

- **`@api`** exposes a property/method as the component's **public API**.
- **Treat `@api` props as read-only inside the child** — never mutate them; emit an **event**
  instead.
- **`@api` methods** let a parent call a child function via `this.refs`/`querySelector`.

---

## 3. `@track` — deep reactivity for objects/arrays

```javascript
import { track } from 'lwc';
@track address = { city: 'NYC' };
// this.address.city = 'LA';  re-renders WITH @track
```

Since Spring '20, **fields are reactive by default even without `@track`** when you **reassign**
them. You only need **`@track`** to make LWC react to **mutations *inside* an object/array** (changing
a nested property without reassigning the whole thing). Often the cleaner fix is to **reassign**:
`this.records = [...this.records, newItem]`.

---

## 4. `@wire` — reactive data from Salesforce

```javascript
import { wire } from 'lwc';
import getContacts from '@salesforce/apex/ContactController.getContacts';

@wire(getContacts, { accountId: '$recordId' })
contacts;          // auto-populated, re-fetches when recordId changes
```

The **`$`** prefix makes a parameter **reactive** — when `recordId` changes, the wire re-runs.
(Full data story in Lesson 06.)

---

## 5. The reactivity gotchas

- **Mutating an array in place** (`this.items.push(x)`) may **not** re-render — reassign instead:
  `this.items = [...this.items, x]`.
- `@api` properties shouldn't be mutated by the child; data flows **down**, changes flow **up**.
- Getters are recomputed on render, so keep them **cheap and side-effect free**.

---

## 6. Public methods

```javascript
@api refreshData() { /* parent calls myChild.refreshData() */ }
```

```javascript
// in parent JS
this.template.querySelector('c-child').refreshData();
```

Use sparingly — events (Lesson 05) are usually the better, more decoupled choice.

---

## 🌍 Real-World Example

**The classic "the screen won't update" bug.** A developer built a settings panel that mutated
`this.config.theme = 'dark'` directly and couldn't understand why the live preview didn't change.
Reassigning the whole object — `this.config = { ...this.config, theme: 'dark' }` — or adding
`@track` fixed it instantly. This exact symptom is one of the most common LWC questions on
developer forums, and it traces straight back to *how* LWC observes changes.

---

## 🔬 Under the Hood (In-Depth)

- **Reactivity via a membrane** — LWC wraps reactive fields; a top-level reassignment is observed,
  but a deep mutation inside a non-tracked object isn't, because the engine only sees the top-level
  setter fire.
- **`@track` adds deep observation** — it wraps the object/array in a reactive Proxy so nested
  changes are detected; modern guidance is to prefer immutable reassignment with spreads for
  clarity and predictability.
- **`@api` is one-way and enforced** — public props are set by the parent; mutating them in the
  child is overwritten on the next parent render and breaks the unidirectional data-flow contract.
- **The `$` makes wire params reactive** — `'$recordId'` subscribes the wire to that field, so any
  change re-invokes the adapter; a literal value wires only once.
- **Re-renders are batched and async** — multiple property changes in one tick coalesce into a
  single render on the microtask queue, which is exactly why Jest tests must `await` before
  asserting.

---

## 🎤 Say this in the interview

- *"Fields are **reactive by default** on reassignment; **`@api`** exposes public, read-only-in-child
  properties (data flows **down**)."*
- *"**`@track`** is only needed to react to **mutations inside** objects/arrays — usually I just
  **reassign** with the spread operator instead."*
- *"**`@wire`** with a **`$reactive`** parameter re-fetches automatically when that property
  changes."*

➡️ **Next:** [05 — Events & component communication](./05_Events_And_Communication.md)
