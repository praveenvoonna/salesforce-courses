# 13 — Hands-On Lab

Reading about Apex isn't enough — **type it**. This lab builds one small, **bulk-safe, tested**
feature end-to-end so every earlier lesson becomes real.

> **Goal:** When an Opportunity is set to **Closed Won**, stamp its parent Account's
> `Last_Won_Date__c` and increment a `Won_Count__c` — done in a **bulk-safe** trigger with a
> handler class and a passing test.

---

## 0. Setup

1. Sign up for a free **Developer Edition org** at developer.salesforce.com.
2. Install **VS Code** + the **Salesforce Extension Pack**, and the **Salesforce CLI (`sf`)**.
3. Authorize the org: `sf org login web`. (Or just use the in-browser **Developer Console**.)

---

## 1. Create the custom fields (clicks)

On **Account**, add two custom fields (Setup → Object Manager → Account → Fields):
- `Last_Won_Date__c` — type **Date**.
- `Won_Count__c` — type **Number** (default 0).

> Notice: this is configuration, not code — *clicks before code* (Lesson 00).

---

## 2. The trigger (thin)

```apex
trigger OpportunityTrigger on Opportunity (after update) {
    new OpportunityTriggerHandler().afterUpdate(Trigger.newMap, Trigger.oldMap);
}
```

---

## 3. The handler (bulk-safe logic)

```apex
public with sharing class OpportunityTriggerHandler {
    public void afterUpdate(Map<Id, Opportunity> news, Map<Id, Opportunity> olds) {
        // 1) find opps that JUST became Closed Won
        Set<Id> acctIds = new Set<Id>();
        for (Opportunity o : news.values()) {
            Opportunity before = olds.get(o.Id);
            Boolean justWon = o.StageName == 'Closed Won'
                              && before.StageName != 'Closed Won'
                              && o.AccountId != null;
            if (justWon) acctIds.add(o.AccountId);
        }
        if (acctIds.isEmpty()) return;

        // 2) ONE query for the parents
        Map<Id, Account> accts = new Map<Id, Account>(
            [SELECT Id, Won_Count__c FROM Account WHERE Id IN :acctIds]);

        // 3) update in memory
        for (Opportunity o : news.values()) {
            if (acctIds.contains(o.AccountId)) {
                Account a = accts.get(o.AccountId);
                a.Last_Won_Date__c = Date.today();
                a.Won_Count__c = (a.Won_Count__c == null ? 0 : a.Won_Count__c) + 1;
            }
        }
        // 4) ONE DML
        update accts.values();
    }
}
```

Check it against Lesson 08: no SOQL in loops, no DML in loops, one query, one DML. ✅

---

## 4. The test (with bulk!)

```apex
@isTest
private class OpportunityTriggerHandlerTest {
    @isTest static void stampsAccountOnWin() {
        Account a = new Account(Name = 'Acme'); insert a;
        List<Opportunity> opps = new List<Opportunity>();
        for (Integer i = 0; i < 200; i++) {                  // bulk!
            opps.add(new Opportunity(Name='O'+i, StageName='Prospecting',
                     CloseDate=Date.today(), AccountId=a.Id));
        }
        insert opps;

        Test.startTest();
        for (Opportunity o : opps) o.StageName = 'Closed Won';
        update opps;                                          // fires the trigger
        Test.stopTest();

        Account result = [SELECT Won_Count__c, Last_Won_Date__c FROM Account WHERE Id = :a.Id];
        Assert.areEqual(200, result.Won_Count__c, 'All 200 wins counted');
        Assert.areEqual(Date.today(), result.Last_Won_Date__c);
    }
}
```

---

## 5. Run & verify

- Deploy: `sf project deploy start` (or save in Developer Console).
- Run tests: `sf apex run test --code-coverage --result-format human`.
- Confirm coverage **≥ 75%** and the assertion passes.

---

## 6. Stretch goals

- Add a **negative test**: an Opportunity that was *already* Closed Won shouldn't double-count.
- Move the recount to **Batch Apex** to backfill historical data (Lesson 09).
- Enforce **`WITH USER_MODE`** on the query (Lesson 11).
- Expose `Won_Count__c` via an **Apex REST** endpoint (Lesson 12).

You've now used objects, triggers, bulkification, testing, and security in one feature. 🎉

➡️ **Next:** [14 — Interview Q&A flashcards](./14_Interview_QA_Flashcards.md)
