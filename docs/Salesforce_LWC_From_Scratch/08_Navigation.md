# 08 — Navigation & the NavigationMixin

## 🧠 The One Idea

**`NavigationMixin` is the GPS of Lightning Experience.** You don't hard-code URLs (they differ
per org and surface). Instead you describe *where* you want to go — "the record page for this
Account," "a new Contact form," "this custom tab" — and Salesforce builds the correct URL and
navigates there.

The one-liner: **"`NavigationMixin` navigates by describing a *page reference*, not a hard-coded
URL."**

---

## 1. Mixing it in

```javascript
import { LightningElement } from 'lwc';
import { NavigationMixin } from 'lightning/navigation';

export default class Nav extends NavigationMixin(LightningElement) {
    // now this[NavigationMixin.Navigate](...) is available
}
```

`NavigationMixin` wraps your class to add navigation methods — note the unusual
`NavigationMixin(LightningElement)` mixin syntax.

---

## 2. Navigate to a record

```javascript
this[NavigationMixin.Navigate]({
    type: 'standard__recordPage',
    attributes: {
        recordId: this.accountId,
        objectApiName: 'Account',
        actionName: 'view'        // 'view' | 'edit'
    }
});
```

---

## 3. Common page reference types

| Goal | `type` |
|---|---|
| A record's detail page | `standard__recordPage` |
| New-record form | `standard__objectPage` (actionName `new`) |
| A list view | `standard__objectPage` |
| A custom tab/component | `standard__navItemPage` |
| An external URL | `standard__webPage` |
| A Lightning component | `standard__component` |

```javascript
// New Contact form
this[NavigationMixin.Navigate]({
    type: 'standard__objectPage',
    attributes: { objectApiName: 'Contact', actionName: 'new' }
});
```

---

## 4. Generate a URL (instead of navigating)

```javascript
this[NavigationMixin.GenerateUrl]({
    type: 'standard__recordPage',
    attributes: { recordId: id, objectApiName: 'Account', actionName: 'view' }
}).then(url => { this.recordUrl = url; });   // put in an <a href>
```

Use this to render real links (right-click, open-in-new-tab friendly).

---

## 5. Passing state / parameters

`pageReference.state` carries query parameters; on the destination you read them via the
**`CurrentPageReference`** wire:

```javascript
import { CurrentPageReference } from 'lightning/navigation';
@wire(CurrentPageReference) pageRef;   // pageRef.state.c__myParam
```

Custom params must be prefixed with **`c__`**.

---

## 6. Why not just use URLs?

Hard-coded URLs **break** across orgs, sandboxes, communities, and mobile. Page references are
**portable and surface-aware** — the same code navigates correctly in Lightning Experience,
the mobile app, and Experience Cloud sites.

---

## 🎤 Say this in the interview

- *"I navigate with **`NavigationMixin`** using a **page reference** (type + attributes), never a
  hard-coded URL — it's portable across orgs and surfaces."*
- *"`Navigate` goes there; **`GenerateUrl`** gives a real link for `<a href>`."*
- *"I read incoming params via the **`CurrentPageReference`** wire, with custom params prefixed
  **`c__`**."*

➡️ **Next:** [09 — Lifecycle hooks](./09_Lifecycle_Hooks.md)
