# 10 — Testing Apex

## 🧠 The One Idea

**In Salesforce, tests are the toll you pay to ship.** You literally **cannot deploy Apex to
production** unless your code has at least **75% test coverage** and all tests pass. So testing
isn't optional polish — it's a gate. The good news: Apex testing is built into the platform, and
tests run against **isolated, fake data** so they never touch real records.

The one-liner: **"Apex tests are mandatory (75% to deploy) and run against isolated test data."**

---

## 1. A test class

```apex
@isTest
private class AccountServiceTest {
    @isTest
    static void ratesHighRevenueAsHot() {
        // Arrange: create test data
        Account a = new Account(Name = 'Acme', AnnualRevenue = 2000000);
        insert a;

        // Act
        Test.startTest();
        new AccountService().rate(new List<Id>{ a.Id });
        Test.stopTest();

        // Assert — this is the part that matters
        Account result = [SELECT Rating FROM Account WHERE Id = :a.Id];
        System.assertEquals('Hot', result.Rating, 'High revenue should be Hot');
    }
}
```

Mark classes/methods **`@isTest`**; test methods are **`static`**.

---

## 2. Test data isolation

- Tests **don't see real org data** by default — you **create your own** in the test.
- Need real data (rare)? `@isTest(SeeAllData=true)` — **avoid it**; it makes tests fragile.
- Use a **`@testSetup`** method to build shared data once per test class:

```apex
@testSetup
static void makeData() { insert new Account(Name = 'Base'); }
```

---

## 3. `Test.startTest()` / `Test.stopTest()`

This pair does two jobs:
1. Code between them gets a **fresh set of governor limits** (so setup doesn't eat your budget).
2. **Async jobs** (future/queueable/batch) enqueued before `stopTest()` **run synchronously**
   at `stopTest()`, so you can assert their results.

---

## 4. Assert, don't just run

Coverage ≠ correctness. A test that runs code but asserts nothing is "coverage theater."
Always verify behavior:

```apex
System.assertEquals(expected, actual, 'message');
Assert.areEqual(expected, actual);     // newer Assert class
Assert.isTrue(condition);
```

Test the **happy path, edge cases, bulk (200+ records), and the failure path** (use
`try/catch` + `Assert.fail()` patterns to confirm exceptions).

---

## 5. Mocking callouts

You can't make real HTTP callouts in tests — you **mock** them:

```apex
@isTest
class CalloutTest {
    @isTest static void getsData() {
        Test.setMock(HttpCalloutMock.class, new MyMock());   // fake the response
        Test.startTest();
        String r = MyService.fetch();
        Test.stopTest();
        Assert.areEqual('ok', r);
    }
}
```

Implement **`HttpCalloutMock`** (or `WebServiceMock` for SOAP) to return canned responses.

---

## 6. Coverage rules (interview facts)

- **Overall org ≥ 75%** to deploy to production; **every trigger needs >0%**.
- Coverage is per-**class/trigger**; aim **higher than 75%** in practice.
- `@isTest` code **doesn't count** toward your org's Apex character/coverage totals.

---

## 7. Best practices

- One behavior per test method; descriptive names.
- Use a **TestDataFactory** class to build records consistently.
- Run with **`runAs(user)`** to test sharing/permissions (Lesson 11).
- Never rely on existing org data or specific record Ids.

---

## 🎤 Say this in the interview

- *"Production deploys need **≥75% coverage** and passing tests — testing is a hard gate, not
  optional."*
- *"Tests run on **isolated data** I create; I use **`@testSetup`** for shared data and
  **`Test.startTest/stopTest`** for fresh limits and to force async to run."*
- *"I **assert behavior** (happy path, bulk, failure) and **mock callouts** with
  `HttpCalloutMock` — coverage without assertions is meaningless."*

➡️ **Next:** [11 — Security & sharing](./11_Security_And_Sharing.md)
