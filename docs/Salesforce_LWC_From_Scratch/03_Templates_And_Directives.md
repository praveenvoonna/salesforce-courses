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

## 🎤 Say this in the interview

- *"Bindings are **one-way** (JS→DOM); for conditionals I use **`lwc:if/elseif/else`**, for
  loops **`for:each`** with a **unique, stable `key`** (never the index)."*
- *"Templates can't run expressions, so I compute values in **getters**, which re-run when their
  reactive inputs change."*
- *"**Slots** let a parent inject markup into a child for reusable, composable components."*

➡️ **Next:** [04 — Reactivity & properties](./04_Reactivity_And_Properties.md)
