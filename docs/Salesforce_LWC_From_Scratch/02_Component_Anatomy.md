# 02 — Anatomy of a Component

## 🧠 The One Idea

**Every LWC is a trio: a face, a brain, and an ID card.** The **HTML** file is the face (what
you see), the **JavaScript** file is the brain (the logic), and the **`.js-meta.xml`** file is
the ID card (where the component is allowed to appear). Three small files, one component.

The one-liner: **"An LWC is HTML (template) + JS (controller) + meta XML (configuration)."**

---

## 1. The three files

For a component named `helloWorld`:

```
helloWorld/
├── helloWorld.html         # template (the UI)
├── helloWorld.js           # controller (the logic)
└── helloWorld.js-meta.xml  # config (visibility & API version)
```

Naming is **camelCase** for the folder/files; in markup it becomes **kebab-case** with a `c-`
namespace: `<c-hello-world>`.

---

## 2. The HTML template

```html
<template>
    <p>Hello, {greeting}!</p>
    <lightning-button label="Click" onclick={handleClick}></lightning-button>
</template>
```

- Everything is wrapped in a single root **`<template>`**.
- **`{greeting}`** binds to a JS property (one-way, from JS → DOM).
- **`<lightning-...>`** are Salesforce's ready-made **base components**.

---

## 3. The JavaScript controller

```javascript
import { LightningElement } from 'lwc';

export default class HelloWorld extends LightningElement {
    greeting = 'World';

    handleClick() {
        this.greeting = 'LWC';   // changing a field re-renders the template
    }
}
```

- The class **extends `LightningElement`** and is the **default export**.
- Public fields are reactive: assigning `this.greeting` re-renders the DOM automatically.

---

## 4. The meta XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LightningComponentBundle xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>62.0</apiVersion>
    <isExposed>true</isExposed>
    <targets>
        <target>lightning__AppPage</target>
        <target>lightning__RecordPage</target>
        <target>lightning__HomePage</target>
    </targets>
</LightningComponentBundle>
```

- **`isExposed`** must be `true` for the component to show in App Builder/Flows.
- **`targets`** declare *where* it can be dropped (record page, app page, home, flow, etc.).
- Without correct meta, your component **won't appear** in the page builder — a classic
  beginner trap.

---

## 5. How it renders

1. The framework instantiates your JS class.
2. It binds the template's `{...}` expressions to class properties.
3. When a reactive property changes, LWC **efficiently re-renders only what changed** (virtual
   DOM diffing) — you never touch the DOM by hand for data updates.

---

## 6. Optional files

A bundle can also include a CSS file (`helloWorld.css`), an SVG icon, and additional JS modules
imported by the controller. Only HTML + JS + meta are required.

---

## 🌍 Real-World Example

**One `addressForm` component, eleven different pages.** A retailer needed an address-entry widget
on the account page, the contact page, a guest-checkout community, and several flows. Because the
bundle's meta XML declared all of those `targets`, admins simply dragged the *same* component onto
every surface in App Builder — no code changes per page. Later, when the address validation rules
changed, the team edited one component and every one of those pages updated at once.

---

## 🔬 Under the Hood (In-Depth)

- **The bundle is the unit of deployment** — Salesforce treats the folder as a single
  `LightningComponentBundle` metadata item; all files (HTML, JS, meta, CSS) deploy together.
- **`isExposed` + `targets` gate visibility** — without `isExposed=true` the component is invisible
  to App Builder/Flow even if the code is flawless; `targets` decide *which* builders see it, and
  `targetConfigs` declare design-time properties admins can set.
- **The default export is the component** — the framework imports your file and instantiates the
  `default` export, which is why exactly one class per `.js` serves as the entry point.
- **Reactive fields are wrapped** — the compiler turns class fields into reactive properties behind
  getter/setter membranes, so an assignment can schedule a re-render.
- **The template compiles to a render function** — the `.html` isn't parsed at runtime; it's
  compiled into a JS function that produces a virtual DOM the engine diffs against the live DOM.

---

## 🎤 Say this in the interview

- *"An LWC bundle is **HTML (template)**, **JS (controller extending `LightningElement`)**, and
  **`.js-meta.xml`** that controls exposure and target surfaces."*
- *"Template bindings `{prop}` are **one-way JS→DOM**; changing a property **auto re-renders**
  only what changed."*
- *"If a component won't appear in App Builder, check **`isExposed`** and **`targets`** in the
  meta file."*

➡️ **Next:** [03 — Templates & directives](./03_Templates_And_Directives.md)
