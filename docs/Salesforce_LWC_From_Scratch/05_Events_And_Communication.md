# 05 — Events & Component Communication

## 🧠 The One Idea

**Components talk like a family: parents pass down allowance (properties), kids shout up when
they need something (events).** Data flows **down** via `@api` properties; notifications flow
**up** via **events**. For unrelated components that aren't parent/child, you use a **message
channel** (a group chat).

The one-liner: **"Props flow down, events flow up, and the Lightning Message Service connects
the unrelated."**

---

## 1. Parent → child: properties

```html
<!-- parent.html -->
<c-child item-name={selectedName}></c-child>
```

```javascript
// child.js
@api itemName;     // kebab-case in HTML ↔ camelCase in JS
```

HTML attribute **`item-name`** maps to JS property **`itemName`**.

---

## 2. Child → parent: custom events

```javascript
// child.js — fire an event
handleSelect() {
    this.dispatchEvent(new CustomEvent('select', {
        detail: { id: this.recordId }      // payload travels in `detail`
    }));
}
```

```html
<!-- parent.html — listen with on<eventname> -->
<c-child onselect={handleSelect}></c-child>
```

```javascript
// parent.js
handleSelect(event) { console.log(event.detail.id); }
```

- Event names are **lowercase, no camelCase**, no spaces (`'select'`, not `'onSelect'`).
- The listener attribute is **`on` + event name** (`onselect`).

---

## 3. Event propagation: bubbles & composed

```javascript
new CustomEvent('select', { detail, bubbles: true, composed: true });
```

- **`bubbles`** — event travels up the DOM tree (default false).
- **`composed`** — event crosses **shadow DOM** boundaries (default false).
- Default (both false) keeps events **local** — usually what you want for clean encapsulation.

---

## 4. Calling a child method (less common)

A parent can grab a child and call its `@api` method directly:

```javascript
this.template.querySelector('c-child').refresh();
```

Prefer events for decoupling; use direct calls for imperative actions (e.g., "focus this").

---

## 5. Unrelated components: Lightning Message Service (LMS)

For components in **different parts of the page** (not parent/child), use a **Message Channel**:

```javascript
import { publish, subscribe, MessageContext } from 'lightning/messageService';
import SAMPLE from '@salesforce/messageChannel/SampleChannel__c';

@wire(MessageContext) messageContext;
publish(this.messageContext, SAMPLE, { recordId: '001...' });   // sender
subscribe(this.messageContext, SAMPLE, (msg) => { ... });        // receiver
```

LMS works **across LWC, Aura, and Visualforce** on the same page — the modern pub/sub.

---

## 6. Choosing the right channel

| Relationship | Mechanism |
|---|---|
| Parent → child | **`@api` property** |
| Child → parent | **CustomEvent** |
| Siblings via shared parent | events up, props down (parent mediates) |
| Unrelated / cross-DOM | **Lightning Message Service** |
| Cross-tab/global state | LMS or a service component |

---

## 🌍 Real-World Example

**A filter sidebar and a results grid that don't know each other exist.** On a property-search page,
the filter component and the results component sit in different regions of the Lightning page, so
they're not parent and child. When a user picks "3 bedrooms," the filter component **publishes** to
a Lightning Message Channel; the results grid is **subscribed** and re-queries. Neither component
holds a reference to the other — they communicate purely through the channel, so either can be
moved, removed, or reused elsewhere without touching the other.

---

## 🔬 Under the Hood (In-Depth)

- **Events are real DOM events** — `CustomEvent` rides the browser's event system; `bubbles` lets it
  climb the DOM tree and `composed` lets it cross shadow boundaries. Both default to `false` to
  keep components encapsulated.
- **The `detail` payload should be primitive/serializable** — across the shadow boundary LWC may
  hand objects by reference, so passing immutable copies avoids parents accidentally mutating child
  state.
- **Listener naming is fixed** — the framework maps `on<eventname>` attributes to listeners at
  compile time, which is why event names must be lowercase with no camelCase.
- **LMS is a singleton bus** — the Lightning Message Service is page-scoped and bridges LWC, Aura,
  and Visualforce; `MessageContext` ties a subscription to the component's lifecycle so it can be
  cleaned up.
- **Subscriptions must be released** — an LMS subscription kept past `disconnectedCallback` becomes
  a zombie listener firing into a dead component (see Lesson 09).

---

## 🎤 Say this in the interview

- *"**Properties down, events up.** Child fires a **`CustomEvent`** with a `detail` payload; parent
  listens with **`on<eventname>`**."*
- *"`bubbles`/`composed` control whether events climb the DOM and cross **shadow boundaries** —
  I keep them local by default."*
- *"For **unrelated** components I use the **Lightning Message Service**, which also bridges Aura
  and Visualforce."*

➡️ **Next:** [06 — Working with Salesforce data](./06_Working_With_Data.md)
