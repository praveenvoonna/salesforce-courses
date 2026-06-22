# 03 — Templates & Directives

## 🧠 The One Idea

**Directives are special HTML attributes that give your markup superpowers.** Plain HTML can't
say "show this only if X" or "repeat this for each item." LWC adds **directives** —
`if:true`, `for:each`, etc. — that let the template react to your data without you writing DOM
code by hand.

The one-liner: **"Directives are LWC's template superpowers for conditionals, loops, and
binding."**

---

## 1. Data binding (one-way)

```html
<p>{message}</p>                       <!-- text -->
<img src={imageUrl} />                  <!-- attribute -->
<p class={computedClass}></p>           <!-- computed via a getter -->
```

Bindings are **one-way** (JS → template). To handle user input back, you use **events** (next
section), not two-way binding.

---

## 2. Conditional rendering

Modern syntax (`lwc:if` / `lwc:elseif` / `lwc:else`):

```html
<template lwc:if={isLoading}>
    <lightning-spinner></lightning-spinner>
</template>
<template lwc:elseif={hasData}>
    <p>Loaded {count} records.</p>
</template>
<template lwc:else>
    <p>No data.</p>
</template>
```

(Older code uses `if:true={x}` / `if:false={x}` — know both; `lwc:if` is the current best
practice.)

---

## 3. Looping with `for:each`

```html
<template for:each={contacts} for:item="contact">
    <li key={contact.Id}>{contact.Name}</li>
</template>
```

- **`for:item`** names the current element; **`for:index`** is available for the index.
- **`key={...}`** is **required and must be unique** — it lets LWC track items efficiently. Use a
  stable id, **never the array index**.

---

## 4. The `iterator` directive (first/last)

When you need to know if an item is first or last (e.g., to style separators):

```html
<template iterator:it={contacts}>
    <li key={it.value.Id} class={it.first ? 'top' : ''}>
        {it.value.Name}
    </li>
</template>
```

`it.value`, `it.index`, `it.first`, `it.last` are available.

---

## 5. Getters for computed values

Templates can't run expressions like `{a + b}`. Put logic in a **getter**:

```javascript
get fullName() {
    return `${this.first} ${this.last}`;
}
get hasData() {
    return this.records && this.records.length > 0;
}
```

```html
<p>{fullName}</p>
```

Getters re-evaluate whenever their underlying reactive fields change.

---

## 6. Slots — letting parents inject markup

```html
<!-- child.html -->
<div class="card">
    <slot name="header">Default header</slot>
    <slot></slot>            <!-- default slot -->
</div>
```

```html
<!-- parent.html -->
<c-child>
    <h1 slot="header">My Title</h1>
    <p>Body content goes in the default slot.</p>
</c-child>
```

Slots make components **composable** — the parent supplies content into named holes.

---

## 🌍 Real-World Example

**A support queue that never flickers.** A case-list component shows a spinner while loading, the
list when data arrives, and a friendly "You're all caught up" when empty — all via
`lwc:if/elseif/else`. Each row uses `key={case.Id}`. When an agent closes a case and the list
refreshes, only that one row disappears; the other 40 rows stay put with no flicker and the
agent's scroll position is preserved — because LWC matched the surviving rows by their **stable
keys** instead of rebuilding the whole list.

---

## 🔬 Under the Hood (In-Depth)

- **Keys drive reconciliation** — during diffing LWC matches old and new items by `key`; a stable
  id lets it move or remove a single node, while the array index *changes* when items shift,
  forcing wholesale re-creation and losing input focus and scroll state.
- **Directives are compile-time** — `for:each`, `lwc:if`, and `iterator` aren't runtime attributes;
  the template compiler turns them into loops and conditionals inside the generated render function.
- **No arbitrary expressions by design** — templates allow only property/getter references, not
  `{a + b}`, both to keep rendering predictable and to reduce the injection surface; logic lives in
  getters.
- **The root `<template>` emits no node** — it's the render boundary, not an element in the DOM.
- **Slots are projection, not copying** — slotted content stays owned (and styled) by the parent;
  the child only declares *where* it lands.

---

## 🎤 Say this in the interview

- *"Bindings are **one-way** (JS→DOM); for conditionals I use **`lwc:if/elseif/else`**, for
  loops **`for:each`** with a **unique, stable `key`** (never the index)."*
- *"Templates can't run expressions, so I compute values in **getters**, which re-run when their
  reactive inputs change."*
- *"**Slots** let a parent inject markup into a child for reusable, composable components."*

➡️ **Next:** [04 — Reactivity & properties](./04_Reactivity_And_Properties.md)
