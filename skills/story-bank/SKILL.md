---
name: story-bank
description: Use when you are starting a job search and need one canonical record of your work history, metrics, and stories that every resume, cover letter, and interview answer draws from.
intent: Builds and maintains the single source of truth for a job search. Captures each role era, the problems you owned, what you built, verified metrics with their source and caveats, and a story table mapped to competencies. Enforces metrics discipline so numbers never drift between applications, and keeps a public-safe version of each story separate from internal detail.
type: interactive
---

## Purpose

Every job search eventually produces the same failure: three resumes, two LinkedIn versions, and a cover letter that each describe the same project with different numbers. Interviewers notice. So do background checks.

A story bank fixes this by separating two jobs that people usually do at the same time:

1. **Remembering what happened** (slow, needs care, done once)
2. **Writing about it for a specific audience** (fast, done per application)

This skill does the first job. It interviews you about your career, era by era, and produces a document you will paste into a Claude Project or keep next to every application.

---

## Key Concepts

### Eras, not jobs

Organize by era: a stretch of 1 to 3 years where your scope and title were roughly stable. One employer can contain three eras. Eras let you show progression inside a single company, which is the most common thing long-tenured candidates fail to communicate.

### Every metric has a receipt

For each number, record:

| Field | Example |
|---|---|
| Metric | 22% reduction in late-delivery rate |
| Scope | Late deliveries, top 5 metro areas |
| Time window | H2 2024 vs H2 2023 |
| Source | Quarterly business review deck; A/B readout |
| Caveat | Measured on holdout; full rollout not yet confirmed |

**Why it matters:** "22%" with no scope invites the question "of what?" in an interview, and you want the answer on paper before you are asked. When two sources disagree, record both and flag the conflict. Do not silently pick the bigger one.

### Internal vs public framing

Your internal vocabulary (project codenames, tool names, team acronyms) is how you remember the work. It is noise to a recruiter and may be confidential. For each story, keep:

- **Internal label:** what you called it at work (stays in the bank only)
- **Public description:** plain language an outsider understands ("the dispatch pricing tool I built from zero")

### The story table

A compact index that answers "which story do I tell for this question?"

| Story | Era | Competency | Core detail (one line) |
|---|---|---|---|
| Driver app MVP | 2024 | Navigating pushback | Shipped on the existing map SDK instead of waiting for a rebuild |

Aim for 10 to 15 stories covering: ambiguity, conflict, failure, influence without authority, technical tradeoff, crisis, scaling a process, 0-to-1 launch, data-driven decision, and a repeatable pattern across eras.

### The cross-era pattern

The most memorable candidates can name one thing they do repeatedly. Look across eras for it. Example: "I run small pilots in one market, prove the economics, then turn the pilot into a standard playbook." A pattern that shows up in three eras is a career narrative, not a coincidence.

---

## Application

### Session flow

Claude asks, one era at a time:

1. Dates, title on paper, and what you actually did (these often differ, and that difference matters for `career-arc-builder`)
2. The two or three biggest problems you owned
3. For each: what you built or changed, who you worked with, the result
4. For each result: the receipt (scope, window, source, caveat)
5. What you'd call it internally vs how you'd explain it to a stranger

Then Claude drafts the story table and proposes a cross-era pattern for you to accept, edit, or reject.

### Prompt

```
Use the story-bank skill. Interview me one era at a time.
Here's my current resume as a starting point: [paste]
Flag any metric that's missing scope, time window, or source.
```

### Output structure

```
# Story Bank: [Name]

## Summary
[2-3 lines: years of experience, through-line, domains]

## Era 1: [Title on paper] → [Functional role], [Years]
- Problem / What I built / Result (with receipt)
- ...

## Era 2 ...

## Cross-era pattern
[One sentence + where it shows up in each era]

## Story table
[Table]

## Metrics ledger
[Every number, with scope / window / source / caveat / conflicts]

## Jargon map
[Internal label → public description]
```

### Maintenance

Update the bank, not individual resumes. When a number is corrected, correct it here first, then regenerate.

---

## Examples

### Weak entry

> Led the batching redesign. Saved $5M. Worked with eng and data science.

No scope, no window, no source, no specifics on what "led" meant.

### Strong entry

> **Problem:** 30% of late deliveries came from orders batched across stores more than 2 miles apart.
> **What I built:** Added a distance cap to the batching rules, then worked with 2 engineers and a data scientist to A/B test it in 3 metros before rollout.
> **Result:** Late-delivery rate down 18% (3 test metros, Q3 vs Q2 2024, ops dashboard). Annualized savings estimated at $2.1M using finance's cost-per-late-order; caveat: the estimate, not the late-rate reduction, is the projection.
> **Internal label:** "Project Tightrope"  **Public:** "distance-aware order batching"

---

## Common Pitfalls

1. **Writing the bank like a resume.** It's a ledger, not marketing. Put everything in, including caveats.
2. **Rounding up.** If the readout said 18%, the bank says 18%.
3. **Dropping failed projects.** Failure stories are some of the most-asked behavioral prompts. Keep them.
4. **Leaving internal codenames in the public column.** If a stranger wouldn't understand it, it isn't public framing yet.
5. **Never revisiting.** Re-read the bank before every interview loop; you'll catch things you've started to misremember.

---

## References

**Feeds:** every other skill in this repo, plus InterviewReady's `behavioral-story-builder` and `practice-coach`
**Related:** `career-arc-builder` (built from this), `application-writing` (uses the jargon map)
