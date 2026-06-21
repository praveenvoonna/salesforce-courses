# 06 — Classes, OOP & Control Flow

## 🧠 The One Idea

**Classes are blueprints; objects are the houses you build from them.** Apex is
object-oriented like Java: you bundle data and behavior into **classes**, hide details behind
**access modifiers**, and share contracts through **interfaces**. Good Apex apps aren't one
giant trigger — they're small, single-purpose classes that call each other.

The one-liner: **"Apex is class-based OOP — I organize logic into small classes with clear
responsibilities."**

---

## 1. Anatomy of a class

```apex
public with sharing class AccountService {
    private Integer threshold;                    // field

    public AccountService(Integer threshold) {    // constructor
        this.threshold = threshold;
    }

    public List<Account> findBig() {              // method
        return [SELECT Id FROM Account WHERE AnnualRevenue > :threshold];
    }
}
```

- **`with sharing`** (Lesson 11) makes the class respect the running user's record access.
- Instantiate with `new AccountService(1000000)`.

---

## 2. Access modifiers

| Modifier | Visible to |
|---|---|
| `private` | only this class (default) |
| `public` | any Apex in the same **namespace** |
| `global` | any Apex, including other packages/managed code |
| `protected` | this class and its subclasses |

Mark members **as private as possible**; expose only what callers need.

---

## 3. `static` vs instance

```apex
public class Counter {
    public static Integer total = 0;      // shared across the whole transaction
    public Integer mine = 0;              // per-instance
}
```

- **`static`** members belong to the class and **persist for the whole transaction** — handy
  for caching and for "recursion guards" in triggers.
- Instance members belong to one object you `new` up.

---

## 4. Inheritance & polymorphism

```apex
public virtual class Animal {
    public virtual String speak() { return '...'; }
}
public class Dog extends Animal {
    public override String speak() { return 'Woof'; }
}
```

- A class must be **`virtual`** or **`abstract`** to be extended; methods must be **`virtual`**
  /`abstract` to be overridden with **`override`**.
- **`abstract`** classes can declare methods with no body that subclasses must implement.

---

## 5. Interfaces (the contracts Salesforce itself uses)

```apex
public interface Payable { Decimal amountDue(); }
public class Invoice implements Payable {
    public Decimal amountDue() { return 100; }
}
```

Interfaces matter because **the platform's async features are interfaces you implement**:
`Database.Batchable`, `Queueable`, `Schedulable` (Lesson 09). Knowing this connects OOP to the
rest of Apex.

---

## 6. Enums, properties & inner classes

```apex
public enum Season { WINTER, SPRING, SUMMER, FALL }

public class Temp {
    public Integer celsius { get; set; }          // auto-property
    public Integer fahrenheit { get { return celsius * 9/5 + 32; } }  // computed
}
```

**Inner (nested) classes** are great for small wrapper/DTO types used by one outer class — very
common for LWC `@AuraEnabled` return shapes.

---

## 7. Control flow recap

`if/else`, `switch on`, `for`, `for-each`, `while`, `do-while`, `break`, `continue`,
`try/catch/finally`. The **`switch on`** statement is clean for enum/string branching:

```apex
switch on status {
    when 'Open' { … }
    when 'Closed', 'Cancelled' { … }
    when else { … }
}
```

---

## 🌍 Real-World Example

**Enterprise teams structure Apex with the "Enterprise Patterns" (fflib) layering** so logic
stays testable and out of triggers:

- **Selector** — all SOQL for an object lives here (`AccountSelector.selectByIds()`).
- **Domain** — record-level business rules (`Accounts.validate()`), called from the trigger handler.
- **Service** — cross-object use cases (`InvoiceService.generateForOpps()`).

```apex
public with sharing class InvoiceService {
    public static void generateForOpps(Set<Id> oppIds) {
        List<Opportunity> opps = new OpportunitySelector().selectWithLines(oppIds);
        List<Invoice__c> invoices = new List<Invoice__c>();
        for (Opportunity o : opps) invoices.add(buildInvoice(o));   // pure, unit-testable
        insert invoices;
    }
}
```

The trigger calls the **service**, the service calls the **selector** — each class has one job,
so you can unit-test the logic without wiring up a trigger.

---

## 🔬 Under the Hood (In-Depth)

- **`static` initialization & lifetime** — `static` members initialize **once per execution
  context** the first time the class is touched, then persist for the whole transaction. A `static`
  block runs lazily at first reference, not at "program start" (there is none).
- **Inner classes are first-class** — nested classes are commonly used as **DTOs/wrappers** for
  `@AuraEnabled` return shapes and `@InvocableVariable` request/response types; they can be `public`
  for serialization.
- **Properties compile to methods** — `{ get; set; }` generates hidden accessor methods, so you can
  add logic later without breaking callers; a `get`-only property is a computed value.
- **No multiple inheritance** — a class `extends` **one** class but can `implements` **many**
  interfaces; `virtual`/`abstract`/`override` gate the vtable, and methods are *not* virtual by
  default (unlike Java).
- **Interfaces wire you into the platform** — `Database.Batchable`, `Queueable`, `Schedulable`,
  `HttpCalloutMock`, `Comparable`, and `Database.Stateful` are all interfaces *you* implement so
  Salesforce can call *your* code at the right time.
- **`with sharing` is inherited at runtime** — sharing mode is determined by the **outermost** Apex
  in the stack unless a class is `with`/`without`; `inherited sharing` defers to the caller.

---

## 🎤 Say this in the interview

- *"I keep logic in **small, single-responsibility classes** (service/selector/domain), not in
  fat triggers."*
- *"**`static`** members live for the whole **transaction** — useful for caching and recursion
  guards."*
- *"Apex's async features are **interfaces** I implement — `Batchable`, `Queueable`,
  `Schedulable` — so OOP and the platform are tightly linked."*

➡️ **Next:** [07 — Triggers & trigger frameworks](./07_Triggers.md)
