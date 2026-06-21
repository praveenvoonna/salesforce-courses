# 13 — Hands-On Lab

Time to build. This lab creates a real **Account Search** component: type a name, it calls Apex,
and shows matching accounts in a datatable — touching templates, events, `@wire`/imperative
Apex, and Jest.

> **Goal:** A component with a search box that lists matching Accounts and lets the user click one
> to navigate to its record page.

---

## 0. Setup

1. Have a **Developer Edition / scratch org** authorized (`sf org login web`).
2. Open the DX project in **VS Code** with the **Salesforce Extension Pack**.
3. Run `npm install` so Jest is ready.

---

## 1. The Apex controller

```apex
public with sharing class AccountSearchController {
    @AuraEnabled(cacheable=true)
    public static List<Account> search(String term) {
        String like = '%' + term + '%';
        return [SELECT Id, Name, Industry, AnnualRevenue
                FROM Account
                WHERE Name LIKE :like
                WITH USER_MODE
                ORDER BY Name
                LIMIT 50];
    }
}
```

Note: `cacheable=true` (wireable), bind variable (injection-safe), `WITH USER_MODE` (security).

---

## 2. The component HTML

```html
<template>
    <lightning-card title="Account Search" icon-name="standard:account">
        <div class="slds-p-around_medium">
            <lightning-input label="Search" type="search"
                onchange={handleSearch}></lightning-input>

            <template lwc:if={accounts.data}>
                <lightning-datatable
                    key-field="Id"
                    data={accounts.data}
                    columns={columns}
                    hide-checkbox-column
                    onrowaction={handleRowAction}>
                </lightning-datatable>
            </template>
            <template lwc:if={accounts.error}>
                <p class="slds-text-color_error">Something went wrong.</p>
            </template>
        </div>
    </lightning-card>
</template>
```

---

## 3. The component JS

```javascript
import { LightningElement, wire } from 'lwc';
import { NavigationMixin } from 'lightning/navigation';
import search from '@salesforce/apex/AccountSearchController.search';

export default class AccountSearch extends NavigationMixin(LightningElement) {
    term = '';
    columns = [
        { label: 'Name', fieldName: 'Name' },
        { label: 'Industry', fieldName: 'Industry' },
        { label: 'Revenue', fieldName: 'AnnualRevenue', type: 'currency' },
        { type: 'action', typeAttributes: { rowActions: [{ label: 'Open', name: 'open' }] } }
    ];

    @wire(search, { term: '$term' }) accounts;   // reactive: re-runs when term changes

    handleSearch(event) {
        window.clearTimeout(this.delay);
        const value = event.target.value;
        this.delay = setTimeout(() => { this.term = value; }, 300);  // debounce
    }

    handleRowAction(event) {
        const id = event.detail.row.Id;
        this[NavigationMixin.Navigate]({
            type: 'standard__recordPage',
            attributes: { recordId: id, objectApiName: 'Account', actionName: 'view' }
        });
    }
}
```

---

## 4. The meta XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LightningComponentBundle xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>62.0</apiVersion>
    <isExposed>true</isExposed>
    <targets>
        <target>lightning__AppPage</target>
        <target>lightning__HomePage</target>
    </targets>
</LightningComponentBundle>
```

---

## 5. A Jest test

```javascript
import { createElement } from 'lwc';
import AccountSearch from 'c/accountSearch';

describe('c-account-search', () => {
    afterEach(() => { while (document.body.firstChild) document.body.removeChild(document.body.firstChild); });

    it('renders the search input', () => {
        const el = createElement('c-account-search', { is: AccountSearch });
        document.body.appendChild(el);
        const input = el.shadowRoot.querySelector('lightning-input');
        expect(input).not.toBeNull();
    });
});
```

---

## 6. Deploy & try it

- `sf project deploy start`
- In the org: **Setup → Lightning App Builder**, create/edit a Home page, drag in **Account
  Search**, save, activate.
- Type a name and watch it filter; click **Open** to navigate.

---

## 7. Stretch goals

- Add a **spinner** while loading (track a `isLoading` flag).
- Switch to **imperative** Apex on a button instead of reactive `@wire`.
- Add **pagination** for >50 results.
- Test the **row action** fires navigation (mock `NavigationMixin`).

You've now combined templates, base components, events, Apex, navigation, and tests. 🎉

➡️ **Next:** [14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)
