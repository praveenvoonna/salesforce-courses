# 11 — Testing with Jest

## 🧠 The One Idea

**LWC tests run on your laptop, not in Salesforce.** Apex tests run in the org; LWC tests run in
**Node.js using Jest** — fast, offline, and component-focused. You render a component into a fake
DOM, poke at it, and assert what shows up. Salesforce wires (Apex, LDS) are **mocked** so tests
stay isolated and quick.

The one-liner: **"LWC components are unit-tested with `sfdx-lwc-jest` in Node — render, interact,
assert, with all wires mocked."**

---

## 1. Setup

```bash
npm install                 # installs @salesforce/sfdx-lwc-jest (in a DX project)
npm run test:unit           # runs all *.test.js files
```

Tests live in a **`__tests__`** folder inside the component bundle:
`lwc/myCmp/__tests__/myCmp.test.js`.

---

## 2. A first test

```javascript
import { createElement } from 'lwc';
import MyCmp from 'c/myCmp';

describe('c-my-cmp', () => {
    afterEach(() => {
        while (document.body.firstChild) document.body.removeChild(document.body.firstChild);
    });

    it('renders the greeting', () => {
        const el = createElement('c-my-cmp', { is: MyCmp });
        el.name = 'Alice';                  // set @api props
        document.body.appendChild(el);      // triggers render

        const p = el.shadowRoot.querySelector('p');
        expect(p.textContent).toBe('Hello, Alice!');
    });
});
```

You query inside **`el.shadowRoot`** because of shadow DOM (Lesson 10).

---

## 3. Async rendering

DOM updates are asynchronous after you change a property. Await a microtask:

```javascript
el.name = 'Bob';
return Promise.resolve().then(() => {
    const p = el.shadowRoot.querySelector('p');
    expect(p.textContent).toBe('Hello, Bob!');
});
```

A common gotcha: asserting **before** the re-render. Always await first.

---

## 4. Testing events

```javascript
const handler = jest.fn();
el.addEventListener('select', handler);
el.shadowRoot.querySelector('button').click();
expect(handler).toHaveBeenCalled();
expect(handler.mock.calls[0][0].detail.id).toBe('001');
```

---

## 5. Mocking Apex & wires

```javascript
import getContacts from '@salesforce/apex/ContactController.getContacts';
jest.mock('@salesforce/apex/ContactController.getContacts', () => ({
    default: jest.fn()
}), { virtual: true });

getContacts.mockResolvedValue([{ Id: '1', Name: 'Acme' }]);   // imperative

// For @wire, use the wire adapter emit API:
import { getContactsAdapter } from '...';   // or registerLdsTestWireAdapter / emit()
```

`@salesforce/sfdx-lwc-jest` provides **wire adapter mocks** so you can `emit()` fake data or
errors into a `@wire`.

---

## 6. What to test (and not)

- ✅ Rendering given inputs, event dispatch, conditional UI, error states.
- ✅ That the right Apex call was made with the right args.
- ❌ Don't test the framework itself or hit a real org.
- Aim for meaningful **assertions**, like Apex tests — coverage alone isn't the goal.

---

## 🎤 Say this in the interview

- *"LWC uses **Jest via `sfdx-lwc-jest`** in **Node**: I `createElement`, set `@api` props, append
  to the DOM, then query **`shadowRoot`** and assert."*
- *"DOM updates are **async**, so I await a `Promise.resolve()` before asserting."*
- *"I **mock Apex and wire adapters** (`emit` for `@wire`) to keep tests isolated and fast."*

➡️ **Next:** [12 — Performance & best practices](./12_Performance_And_Best_Practices.md)
