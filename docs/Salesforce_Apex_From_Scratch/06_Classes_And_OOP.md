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

## 🎤 Say this in the interview

- *"I keep logic in **small, single-responsibility classes** (service/selector/domain), not in
  fat triggers."*
- *"**`static`** members live for the whole **transaction** — useful for caching and recursion
  guards."*
- *"Apex's async features are **interfaces** I implement — `Batchable`, `Queueable`,
  `Schedulable` — so OOP and the platform are tightly linked."*

➡️ **Next:** [07 — Triggers & trigger frameworks](./07_Triggers.md)
