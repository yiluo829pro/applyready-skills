---
name: target-list-pipeline
description: Use when you need a tiered list of target companies and a simple pipeline tracker so you apply deliberately and can see what's working.
intent: Builds a tiered target company list from your arcs and constraints, then sets up a lightweight pipeline tracker with the columns that matter later (arc used, resume version, referral, stage). Includes a weekly review that turns pipeline data into decisions about where to spend effort.
type: component
---

## Purpose

A job search without a target list drifts toward whatever shows up in your feed. A search without a tracker can't learn: you don't know whether referrals convert better than cold applies, or whether Arc A gets more screens than Arc B. This skill sets up both in under an hour.

---

## Key Concepts

### Tiers

| Tier | Definition | Effort per application |
|---|---|---|
| Tier 1 | Would relocate or take a pay cut for the right role | Full workflow + referral + tailored cover letter |
| Tier 2 | Strong fit, would be happy there | Full workflow, cover letter if requested |
| Tier 3 | Acceptable, good practice or leverage | Triage + light tailoring |

Tiers decide effort, not interest. Keep Tier 1 to a list you can actually work.

### Selection filters

Write these down before building the list:
- **Stage:** e.g. Series B or later, or public
- **Domain:** the problem spaces your arcs are strongest in
- **Role types:** in priority order
- **Location:** remote, specific city, or relocate-for-Tier-1-only

### The columns that matter later

| Date | Company | Tier | Role | Arc | Resume version | Source (cold / referral / recruiter) | Stage | Next action | Notes |

"Arc," "Resume version," and "Source" are the columns that let you learn. Most trackers skip them.

### Weekly review (15 minutes)

1. Response rate by source. If referrals convert 5x better, shift time to outreach.
2. Response rate by arc. If one arc gets no screens, the arc or the targeting is off.
3. Stalled rows. Anything with no next action gets one or gets closed.
4. One change for next week.

---

## Application

### Prompt

```
Use the target-list-pipeline skill.
My arcs: [paste]
Filters: [stage, domain, role types, location]
Companies I already know I want: [list]
```

Claude proposes a tiered list with one line per company on why it fits which arc, then outputs the tracker as a table (or a spreadsheet, if your setup supports one).

Company facts like funding stage and open roles change fast. Claude should look these up rather than rely on memory, and mark anything it couldn't verify.

---

## Examples

### Weak list
> "Top AI companies: OpenAI, Anthropic, Google, Meta, Microsoft..."

No tiers, no fit reasoning, no link to arcs.

### Strong row
> **Tier 1 · Acme Freight** (Series C) · Arc B · They sell a dispatch platform to regional carriers; my pricing API work maps to their core product. Open role: Senior PM, Pricing. Path: ask a former colleague now on their ops team for a referral.

---

## Common Pitfalls

1. **Tier 1 with 100 companies.** That's a wishlist, not a tier.
2. **Tracking applications but not outcomes.** Record stage changes, or the review has nothing to learn from.
3. **No next action.** Every open row needs one.
4. **Unverified company facts.** Funding and hiring change monthly. Check.

---

## References

**Uses:** `career-arc-builder`
**Fed by:** `job-application-workflow` (log rows)
**Feeds:** `outreach-writer` (who to contact), `interviewer-game-plan`
