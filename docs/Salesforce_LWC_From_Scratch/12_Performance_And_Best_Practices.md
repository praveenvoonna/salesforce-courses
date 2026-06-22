# 12 — Performance & Best Practices

## 🧠 The One Idea

**A fast LWC fetches little, fetches once, and renders only what changed.** Most LWC slowness
comes from too many server calls, fetching data the wrong way, or accidentally re-rendering big
lists. The platform gives you caching tools — your job is to use them and avoid the classic
traps.

The one-liner: **"Cache aggressively, minimize server calls, and keep renders cheap."**

---

## 1. Prefer cached, declarative data

- Use **`@wire` with `cacheable=true`** and **Lightning Data Service** — both cache on the
  client, cutting round-trips and respecting limits.
- Reserve **imperative Apex** for user actions and writes.
- Don't fetch the same record in five components — LDS shares one cached copy.

---

## 2. Lazy-load and paginate

- Don't load 10,000 rows into a `lightning-datatable`. **Paginate** or use **infinite scroll**.
- Defer heavy or rarely-seen components with **conditional rendering** (`lwc:if`) so they only
  mount when needed.

---

## 3. Keep renders cheap

- **Reassign arrays** instead of mutating (`this.items = [...]`) so diffing works correctly.
- Always use a **stable, unique `key`** in `for:each` (never the index) — wrong keys cause full
  re-renders.
- Keep **getters cheap and pure**; they run on every render.
- Never set reactive state unconditionally in **`renderedCallback`** (infinite loop — Lesson 09).

---

## 4. Debounce expensive work

For search-as-you-type, **debounce** so you don't call Apex on every keystroke:

```javascript
handleKeyup(event) {
    window.clearTimeout(this.delay);
    const term = event.target.value;
    this.delay = setTimeout(() => this.search(term), 300);
}
```

---

## 5. Security & robustness

- Apex called from LWC defaults to **system mode** — enforce **CRUD/FLS** server-side
  (`WITH USER_MODE`, Apex Lesson 11).
- Never trust client input; validate on the server.
- Handle the **error** branch of every wire/imperative call and show a friendly message.
- Clean up subscriptions/timers in **`disconnectedCallback`**.

---

## 6. Maintainability

- **Small, single-purpose components**; compose with **slots**.
- Data **down** via `@api`, changes **up** via events — don't mutate `@api` props.
- Import fields via **`@salesforce/schema`** for safe refactors and deploy dependencies.
- Use **labels** (`@salesforce/label`) for translatable text, not hard-coded strings.

---

## 7. Common interview pitfalls to name

- DML/SOQL-style "in a loop" thinking carried into Apex controllers — **bulkify** the Apex too.
- Forgetting **`refreshApex`** after a write, so the UI shows stale cached data.
- Mutating arrays in place and wondering why the UI doesn't update.
- Doing data fetches in **`renderedCallback`** instead of `connectedCallback`.

---

## 🌍 Real-World Example

**The report page that froze the laptop.** A `lightning-datatable` was loading 10,000 rows at once
and a search box called Apex on every keystroke. The page took eight seconds to render and stuttered
while typing. The team paginated to 50 rows, added a 300 ms **debounce** on the search, and switched
repeated reads to cached `@wire`. Render time dropped to under a second and the keystroke lag
vanished — same data, just disciplined fetching.

---

## 🔬 Under the Hood (In-Depth)

- **Two cache layers cut round-trips** — `cacheable=true` Apex and LDS both cache on the client
  keyed by inputs, so repeated identical reads never hit the server or count against limits.
- **Diffing cost scales with the DOM you touch** — stable `key`s and array reassignment let LWC
  update only the changed nodes; index keys or in-place mutation can force re-creating entire lists.
- **Debounce vs throttle** — debounce waits for a pause (ideal for search-as-you-type); throttle
  caps frequency (ideal for scroll/resize). Picking the right one avoids needless Apex calls.
- **Client checks are UX, not security** — Apex from LWC runs in **system mode** by default, so
  CRUD/FLS must be enforced server-side (`WITH USER_MODE`); client validation only improves the
  experience.
- **Getters run every render** — keep them pure and cheap; expensive computation belongs in
  precomputed/memoized fields, not in a getter the diff engine calls on every render.

---

## 🎤 Say this in the interview

- *"I default to **cached, declarative** data (`@wire` cacheable + LDS), keep imperative Apex for
  actions/writes, and **`refreshApex`** after DML."*
- *"I keep renders cheap: **reassign arrays**, **stable keys**, cheap getters, **debounced**
  search, and lazy-load big lists."*
- *"I enforce **CRUD/FLS server-side**, handle **error** branches, and clean up in
  **`disconnectedCallback`**."*

➡️ **Next:** [13 — Hands-on lab](./13_Hands_On_Lab.md)
