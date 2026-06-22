# 09 — Lifecycle Hooks

## 🧠 The One Idea

**Lifecycle hooks are the stages of a component's life: born, shown, updated, and gone.** LWC
calls specific methods at each stage so you can run code at the right moment — fetch data when
it's inserted, clean up timers when it's removed. Using the wrong hook (or doing too much in one)
is a top source of bugs.

The one-liner: **"Lifecycle hooks let me run code at create, render, and destroy time."**

---

## 1. The hooks in order

| Hook | When it fires | Use it for |
|---|---|---|
| `constructor()` | component created | set defaults; **DOM not ready, no `@api` values yet** |
| `connectedCallback()` | inserted into the DOM | **fetch data**, subscribe, read `@api` props |
| `renderedCallback()` | after **every** render | DOM-dependent work; **guard it!** |
| `disconnectedCallback()` | removed from the DOM | **clean up** timers/subscriptions |
| `errorCallback(err, stack)` | a child throws | error boundary / logging |

---

## 2. `constructor()` — earliest, most limited

```javascript
constructor() {
    super();           // REQUIRED first line
    // ❌ can't access @api props or this.template here
}
```

Avoid heavy work here. `@api` values aren't set yet, and the DOM doesn't exist.

---

## 3. `connectedCallback()` — the workhorse

```javascript
connectedCallback() {
    // @api props ARE available; good place to load data or subscribe
    this.loadData();
    this.subscription = subscribe(/* ... LMS ... */);
}
```

This is where most initialization belongs (network calls, LMS subscriptions).

---

## 4. `renderedCallback()` — careful!

```javascript
renderedCallback() {
    if (this._initialized) return;     // guard against infinite loops
    this._initialized = true;
    // safe DOM measurement / 3rd-party library init here
}
```

⚠️ It runs **after every re-render**, and changing reactive state inside it **causes another
render** → potential infinite loop. Always **guard with a flag** and never use it for data
fetching.

---

## 5. `disconnectedCallback()` — clean up

```javascript
disconnectedCallback() {
    clearInterval(this.timerId);       // stop timers
    unsubscribe(this.subscription);    // stop LMS subscriptions
}
```

Forgetting cleanup causes memory leaks and "zombie" subscriptions firing after the component is
gone.

---

## 6. Parent/child order (interview detail)

- **Creation:** parent `constructor` → child `constructor` → child `connectedCallback` → child
  `renderedCallback` → parent `renderedCallback`. (Children render before the parent finishes.)
- **`errorCallback`** only catches errors from **descendant** components — it's LWC's error
  boundary, ideal for graceful fallback UI.

---

## 🌍 Real-World Example

**The dashboard that slowly ate the browser.** A real-time chart started a `setInterval` poll in
`connectedCallback` but never cleared it. Each time a user opened and closed the tab, another timer
kept running against a destroyed component — by afternoon the page had dozens of zombie pollers and
ground to a halt. Adding `clearInterval` in `disconnectedCallback` fixed the leak. This
create/destroy symmetry — set up in connect, tear down in disconnect — is the whole point of
lifecycle hooks.

---

## 🔬 Under the Hood (In-Depth)

- **Hooks fire in a guaranteed order** — parent `constructor` → child `constructor` → child
  `connectedCallback` → child `renderedCallback` → parent `renderedCallback`; children complete
  before the parent's render finishes.
- **`renderedCallback` runs after *every* render** — setting reactive state there unconditionally
  schedules another render, creating an infinite loop; a one-time guard flag is the standard fix.
- **`@api` props aren't ready in the constructor** — the framework sets public props *after*
  construction, so any initialization that reads them belongs in `connectedCallback`.
- **`errorCallback` is an error boundary** — it catches errors thrown in the render/lifecycle of
  *descendant* components (not its own event handlers or async callbacks), enabling graceful
  fallback UI.
- **Disconnect can be followed by reconnect** — moving a node within the DOM can fire disconnect
  then connect again, so cleanup logic must be idempotent.

---

## 🎤 Say this in the interview

- *"I fetch data and subscribe in **`connectedCallback`** (where `@api` props are ready), clean
  up in **`disconnectedCallback`**."*
- *"**`renderedCallback`** runs after **every** render, so I **guard it with a flag** and never
  set reactive state unconditionally there — that causes infinite loops."*
- *"**`errorCallback`** is LWC's **error boundary** for catching errors from child components."*

➡️ **Next:** [10 — Styling, SLDS & the shadow DOM](./10_Styling_And_Shadow_DOM.md)
