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

## 🎤 Say this in the interview

- *"Fields are **reactive by default** on reassignment; **`@api`** exposes public, read-only-in-child
  properties (data flows **down**)."*
- *"**`@track`** is only needed to react to **mutations inside** objects/arrays — usually I just
  **reassign** with the spread operator instead."*
- *"**`@wire`** with a **`$reactive`** parameter re-fetches automatically when that property
  changes."*

➡️ **Next:** [05 — Events & component communication](./05_Events_And_Communication.md)
