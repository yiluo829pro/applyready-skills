---
name: resume-tailoring
description: Use when you need resume bullets rewritten for a specific role, kept to one page, with no invented facts and no internal jargon.
intent: Rewrites resume bullets into the target role's vocabulary using only facts from your story bank. Enforces verb + what + measurable outcome, translates internal jargon to plain language, strengthens weak signals (technical depth, metrics context), ranks cuts to hold one page, and runs a grammar audit with specific corrections.
type: component
---

## Purpose

A recruiter spends seconds on the first pass. In that time they are looking for three things: does the title and scope match, do the top bullets use the language of this job, and is there a number that proves it. This skill optimizes for that pass without crossing into fabrication.

---

## Key Concepts

### The bullet formula

**Strong verb + what you built or changed + measurable outcome (+ scope if needed)**

> Launched dynamic dispatch pricing across 40 metro areas, cutting cost per delivery 9% and saving $4M annualized.

Every bullet should survive the question "so what?" If it doesn't have an outcome, either find one in the story bank or cut the bullet.

### Vocabulary, not facts

You may change:
- Verbs and nouns to match the JD ("pricing service" → "real-time decisioning API" if accurate)
- Order of bullets and emphasis
- Which metric leads

You may not change:
- Numbers, scope, team size, dates, or tools used
- Your role in the work ("led" vs "contributed")

### Metrics need context

Bare numbers invite skepticism. Add the minimum context to make them credible:
- "98% reliability" → "99.5% uptime SLA across 5 consuming services"
- "$40M impact" → "$40M estimated support value (A/B-measured deflection × cost per contact)"
- "Grew to 2M" → "0 to 2M subscribers across 30 markets in 18 months"

### Kill the jargon

Internal names (project codenames, tool acronyms) mean nothing outside your company and can be confidential. Use the story bank's jargon map. Test: would a smart person at another company understand the bullet without asking?

### Strengthen weak signals

Common signals that recruiters look for and candidates under-show:
- Technical depth: APIs, data pipelines, SQL/Python, system scale
- Experimentation: A/B design, holdouts, guardrail metrics
- Domain metrics: e.g. for marketplaces, liquidity, utilization, take rate; for support roles, CSAT and resolution rate
- Cross-functional scope: number of teams or functions aligned

### One page, ranked cuts

When over a page, cut by lowest impact first:
1. Bullets with no outcome
2. Oldest era's third and later bullets
3. Skills section items that duplicate bullets
4. Second bullets about the same project

---

## Application

### Prompt

```
Use the resume-tailoring skill.
JD: [paste]
Lead arc: [from role-fit-triage]
Keyword map: [from role-fit-triage]
Current resume: [paste or link]
Story bank: [paste or "in this Project"]
```

### Output

1. **Tailored bullets**, as a clean list per role, ready to copy
2. **What changed and why**, one line per bullet
3. **Suggested cuts**, ranked by lowest impact
4. **Grammar and language audit**: specific corrections only, e.g. "Bullet 3: 'leaded' → 'led'; 'utilize' → 'use'"
5. **Flags**: any bullet where the JD pushed toward something the story bank doesn't support

Note: if you are reading the resume through a text-only tool, Claude can't see page length or layout. Check the 1-page fit in the actual document.

---

## Examples

### Before → after (fictional)

**Before:** Responsible for the pricing system and worked with multiple teams to improve it.
**After:** Built and scaled a dispatch pricing API handling 400K requests/day across 5 consuming services at 99.5% SLA, enabling $12M in annualized operational savings.

**Before:** Drove Compass adoption across MktOps.
**After:** Built the supply-gap alerting layer covering 35 of 40 metros, later used as the input to the courier incentive models.

---

## Common Pitfalls

1. **Keyword stuffing.** Copying JD phrases into bullets where they don't fit reads as fake to a human reviewer.
2. **Upgrading your role.** "Led" when you "supported" will come out in the interview.
3. **Dropping the number to fit the line.** Cut words, not outcomes.
4. **Ignoring the summary line.** It's the most-read line on the page. Write it from the lead arc.
5. **Trusting a text-only tool on length.** Verify the page count visually.

---

## References

**Uses:** `story-bank`, `career-arc-builder`, `role-fit-triage`
**Feeds:** `application-writing`, `target-list-pipeline` (version log)
