# Sample Story Bank: Jordan Rivera (fictional)

> Everything in this file is invented to illustrate the `story-bank` format. Jordan, the companies, and the numbers are not real.

## Summary

Six years in delivery marketplaces, from city operations to platform product work. Through-line: runs small pilots in one market, proves the economics, then turns the pilot into a standard playbook.

## Era 1: Operations Analyst → de facto ops PM, 2020 to 2022

**Problem:** City teams found courier shortages hours late, after delivery times had already slipped.
**What I built:** A supply-gap alerting layer that flagged metros where open orders outpaced active couriers; ran a weekly review with 3 city teams to agree on thresholds.
**Result:** Live in 35 of 40 metros vs a goal of 30 (ops analytics, Q4 2022). Later used as the input to the courier incentive models.
- Internal label: "Compass" · Public: "the supply-gap alerting layer"

## Era 2: Program Manager → de facto PM, Fulfillment, 2022 to 2024

**Problem:** 30% of late deliveries came from orders batched across stores more than 2 miles apart.
**What I built:** A distance cap in the batching rules, A/B tested in 3 metros with 2 engineers and a data scientist.
**Result:** Late-delivery rate down 18% (3 test metros, Q3 vs Q2 2024, ops dashboard). Estimated $2.1M annualized savings (finance model; projection).
- Internal label: "Tightrope" · Public: "distance-aware order batching"

## Era 3: Product Manager, Dispatch Pricing, 2024 to present

**Problem:** Flat courier pay left peak hours understaffed and quiet hours overpaid.
**What I built:** A dynamic dispatch pricing API, with a merchant-facing ETA promise; 4 engineers, 1 designer, 1 data scientist.
**Result:** Cost per delivery down 9% across 40 metros (A/B vs flat-pay holdout). $4M annualized savings (projection).
**Caveat:** Courier earnings per hour held flat; measured separately so the savings didn't come from lower pay.
- Internal label: "Metronome" · Public: "dynamic dispatch pricing"

## Cross-era pattern

Pilot in one market, prove the economics, turn it into a playbook. Compass (2020), Tightrope (2022), Metronome (2024).

## Story table

| Story | Era | Competency | Core detail |
|---|---|---|---|
| Supply-gap alerting 0→1 | 1 | Platform thinking | Built the signal later used by incentive models |
| Distance-aware batching | 2 | Systems diagnosis | Found the root cause before changing the rules |
| Driver app MVP | 3 | Navigating pushback | Shipped on the existing map SDK instead of waiting for a rebuild |
| Dynamic dispatch pricing | 3 | 0→1 shipping | 9% lower cost per delivery, A/B tested |
| Two-metro outage | 3 | Crisis / XFN leadership | Paused rollout within an hour, owned the fix list |
| Missed launch date | 2 | Failure | Slipped 3 weeks on a dependency; what I changed after |

## Metrics ledger

| Metric | Scope | Window | Source | Caveat / conflict |
|---|---|---|---|---|
| 35 of 40 metros | Alerting coverage | Q4 2022 | Ops analytics | none |
| 18% late-rate reduction | 3 test metros | Q3 vs Q2 2024 | Ops dashboard | none |
| $2.1M savings | 3 test metros, scaled | Annualized | Finance model | projection |
| 9% cost per delivery | 40 metros | Launch +2Q | A/B readout | QBR deck says 10%; A/B says 9%. Use A/B. |

## Jargon map

| Internal | Public |
|---|---|
| Compass | supply-gap alerting layer |
| Tightrope | distance-aware order batching |
| Metronome | dynamic dispatch pricing |
| MktOps | marketplace operations team |
