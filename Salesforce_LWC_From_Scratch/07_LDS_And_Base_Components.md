# 07 — Lightning Data Service & Base Components

## 🧠 The One Idea

**Lightning Data Service (LDS) is a shared, smart cache for records — so you can do CRUD without
writing Apex.** Instead of every component querying the same record separately, LDS keeps one
cached copy, keeps all components in sync, and handles field-level security for you. **Base
components** (`lightning-*`) are the pre-built, accessible UI widgets that sit on top.

The one-liner: **"LDS gives no-Apex, cached, FLS-aware record CRUD; base components are the
ready-made UI."**

---

## 1. Why LDS exists

- **No Apex** for single-record read/create/update/delete.
- **Cached + synchronized**: change a record in one component, others update automatically.
- **Respects FLS and sharing** out of the box.
- **Fewer server round-trips** → faster pages and fewer governor-limit worries.

---

## 2. `lightning-record-form` (the easiest)

```html
<lightning-record-form
    record-id={recordId}
    object-api-name="Account"
    fields={fields}
    mode="edit">
</lightning-record-form>
```

One tag = a full editable form with save/cancel, validation, and FLS. Great for quick CRUD; less
layout control.

---

## 3. `record-view-form` / `record-edit-form` (more control)

```html
<lightning-record-edit-form record-id={recordId} object-api-name="Account"
        onsuccess={handleSuccess}>
    <lightning-input-field field-name="Name"></lightning-input-field>
    <lightning-input-field field-name="Industry"></lightning-input-field>
    <lightning-button type="submit" label="Save"></lightning-button>
</lightning-record-edit-form>
```

You lay out fields yourself but still get LDS caching, validation, and FLS.

---

## 4. The wire adapters (`lightning/uiRecordApi`)

For programmatic access without Apex:

```javascript
import { getRecord, getFieldValue, updateRecord, createRecord, deleteRecord }
    from 'lightning/uiRecordApi';
import NAME_FIELD from '@salesforce/schema/Account.Name';

@wire(getRecord, { recordId: '$recordId', fields: [NAME_FIELD] })
account;

get name() { return getFieldValue(this.account.data, NAME_FIELD); }
```

Importing fields via **`@salesforce/schema/...`** gives compile-time checking and auto-includes
the field in deployments.

---

## 5. Base components you'll use constantly

| Component | Purpose |
|---|---|
| `lightning-button` | buttons |
| `lightning-input` | text/number/checkbox/date inputs |
| `lightning-datatable` | rich, sortable, inline-edit tables |
| `lightning-card` | a titled container |
| `lightning-spinner` | loading indicator |
| `lightning-icon` | SLDS icons |
| `lightning-combobox` | dropdown |

They're **accessible, responsive, and SLDS-styled** for free — prefer them over hand-rolled HTML.

---

## 6. When to still use Apex

LDS is for **single records**. Use **Apex (`@wire`/imperative)** when you need: **multiple
records / complex SOQL**, **aggregations**, **transactions across objects**, or **business logic**
the UI APIs can't express. Many real apps mix both.

---

## 🎤 Say this in the interview

- *"**LDS** gives cached, synchronized, **FLS-aware CRUD without Apex** — via
  `lightning-record-form`/`-edit-form` or the **`uiRecordApi`** wire adapters."*
- *"I import fields with **`@salesforce/schema`** for compile-time safety and deployment
  dependencies."*
- *"LDS is **single-record**; I switch to **Apex** for multi-record queries, aggregates, or
  cross-object logic."*

➡️ **Next:** [08 — Navigation & the NavigationMixin](./08_Navigation.md)
