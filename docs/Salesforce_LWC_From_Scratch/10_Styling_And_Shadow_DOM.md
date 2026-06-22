# 10 — Styling, SLDS & the Shadow DOM

## 🧠 The One Idea

**Each component lives in its own soundproof room (the shadow DOM), so its styles never leak.**
CSS you write for one component **can't accidentally restyle another** — and outside styles can't
sneak in. This isolation is great for safety but means you can't just "reach in" and style a
child; you cooperate via **CSS custom properties** and SLDS.

The one-liner: **"Shadow DOM scopes each component's CSS; you share styling via SLDS and CSS
custom properties."**

---

## 1. Component-scoped CSS

A `myCmp.css` file in the bundle is **automatically scoped** to that component:

```css
/* myCmp.css — applies ONLY inside myCmp */
.title { font-weight: bold; color: #16325c; }
p { margin: 0; }
```

No class-name collisions across components — the shadow DOM guarantees isolation.

---

## 2. SLDS — the Salesforce design system

**SLDS (Salesforce Lightning Design System)** is the official CSS framework. Use its utility
classes directly in markup for consistent, on-brand, accessible styling:

```html
<div class="slds-card slds-p-around_medium">
    <h2 class="slds-text-heading_small slds-m-bottom_small">Accounts</h2>
</div>
```

Prefer **SLDS utility classes** and **base components** over custom CSS — it stays consistent and
upgrade-safe.

---

## 3. Why shadow DOM blocks global CSS

Because styles are encapsulated:
- A global stylesheet **won't** restyle your component's internals.
- You **can't** target a child component's internal elements with a CSS selector from the
  parent.

This is intentional encapsulation, not a bug.

---

## 4. Sharing styles across components

Three sanctioned ways:

1. **CSS custom properties (variables)** pierce the shadow boundary:
   ```css
   :host { --brand: #1589ee; }
   .btn { background: var(--brand); }
   ```
2. **SLDS Styling Hooks** — Salesforce-provided `--slds-*` variables you can override.
3. **A shared CSS module** imported into multiple components' CSS via `@import`.

---

## 5. The `:host` selector

`:host` styles the component's **own** root element:

```css
:host { display: block; padding: 8px; }
:host(.highlighted) { border: 2px solid gold; }
```

Use it to control the component's outer box and react to host classes/attributes.

---

## 6. Light DOM (the escape hatch)

Some cases (global styling, certain 3rd-party libs, SEO in Experience Cloud) need styles to
reach in. LWC supports **Light DOM** (`static renderMode = 'light'`) to **opt out** of shadow
encapsulation for a component. Use it deliberately — you lose isolation.

---

## 🌍 Real-World Example

**The third-party theme that politely failed.** A marketing team dropped a global CSS theme onto a
page hoping to recolor an embedded LWC's buttons. Nothing changed — and that was the *correct*
behavior: the shadow DOM kept the component's internals isolated from outside styles. To actually
theme it, the team used the component's exposed CSS custom properties (`--brand`) and SLDS styling
hooks, recoloring it **intentionally** instead of by accident.

---

## 🔬 Under the Hood (In-Depth)

- **Synthetic vs native shadow** — by default Salesforce uses a JS "synthetic shadow" polyfill that
  scopes styles by adding generated attributes to elements; orgs can enable native shadow where the
  browser enforces isolation directly, which is faster.
- **Scoping is per-component** — the compiler rewrites your selectors so `.title` only matches
  elements inside that component's template, guaranteeing no cross-component class collisions.
- **Custom properties pierce the boundary** — CSS variables inherit *through* shadow roots by
  design, which is exactly why theming uses `--vars` and SLDS styling hooks rather than reaching
  into a component's internals.
- **`:host` targets the element itself** — it styles the custom element's outer box and can react to
  host classes/attributes (`:host(.active)`).
- **Light DOM opts out** — `static renderMode = 'light'` renders without a shadow root so global CSS
  and some libraries/SEO crawlers can reach in, at the cost of isolation.

---

## 🎤 Say this in the interview

- *"Each LWC's CSS is **scoped by the shadow DOM**, so styles don't leak and class names never
  collide."*
- *"I style with **SLDS utilities and base components** first; to theme across the boundary I use
  **CSS custom properties** / **SLDS styling hooks**."*
- *"For cases needing global styling I can opt into **Light DOM**, trading isolation for
  reach."*

➡️ **Next:** [11 — Testing with Jest](./11_Testing_With_Jest.md)
