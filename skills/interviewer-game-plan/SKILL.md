---
name: interviewer-game-plan
description: Use when an interview loop is scheduled and you want predicted questions plus a per-interviewer plan: their focus, likely questions, which story to use, and what to ask them.
intent: A two-stage prep method. Stage 1 predicts the most likely questions by mining question banks and reported interviews at the company and its closest comparables. Stage 2 builds a per-interviewer dossier from the loop schedule, mapping each interviewer's role to their likely focus, your best story, an answer structure, and smart questions that show you understand their part of the business.
type: workflow
---

## Purpose

Generic prep treats a five-person loop as five copies of the same interview. It isn't. The engineering manager is checking whether you can work with their team. The design lead is checking product taste. The skip-level is checking judgment and scope. Preparing per interviewer means each conversation feels like you already understand their world, which is often the difference between "solid" and "hire."

This skill extends InterviewReady's `interview-day-brief` with a per-person layer.

---

## Key Concepts

### Stage 1: Predict, don't memorize

Question banks have thousands of questions. You need the 20 most likely. To narrow:

1. Pull reported questions for this company and role (interview review sites, public question banks, recruiter guidance).
2. Pull the same for 2 to 3 comparable companies in the same domain.
3. Cluster by theme: product sense, strategy, execution/metrics, behavioral, technical/analytical.
4. Rank by frequency and by fit with the JD's emphasis.

**Why it matters:** recurring themes across comparable companies are a strong signal of what this company's interviewers were trained on.

### Stage 2: The per-interviewer dossier

For each person on the schedule:

| Field | Source |
|---|---|
| Role and team | Schedule + their public profile |
| Likely focus | What someone in that role needs to know about you |
| 2-3 likely questions | From Stage 1, filtered by focus |
| Answer structure | The framework that fits (e.g. product sense template, STAR, metrics tree) |
| Best story | From your story bank |
| 2-3 questions to ask them | About their part of the business, not generic culture questions |

### Questions that show understanding

Weak: "What's the culture like?"
Strong: "Your same-day delivery expansion seems to be pushing courier utilization down in smaller metros. Is the team optimizing for coverage first and density later, or holding launches until density is there?"

Good questions reference something specific (a launch, a metric, a known tradeoff) and ask about a decision, not a fact you could look up.

---

## Application

### Stage 1 prompt

```
Use the interviewer-game-plan skill, Stage 1.
Company: [name]   Role: [title]   Domain: [e.g. logistics marketplaces]
Comparables: [2-3 companies]
Sources to mine: [question banks or sites you have access to]
```

Output: 15 to 25 predicted questions grouped by theme, each with a likelihood (high / medium) and why.

### Stage 2 prompt

```
Use the interviewer-game-plan skill, Stage 2.
Schedule: [name, title, time for each interviewer]
Stage 1 output: [paste]
Story bank and resume: [paste or "in this Project"]
```

Output: one section per interviewer using the table above, plus a short "risk areas" list for the whole loop.

### Privacy note

Research interviewers only through their professional, public information (title, team, public writing or talks). Don't go further than that.

---

## Examples

### Weak dossier entry
> **Alex (Eng Manager):** Will ask technical questions. Be prepared.

### Strong dossier entry (fictional)
> **Alex Chen, Engineering Manager, Routing Platform**
> **Likely focus:** can you scope work an engineering team can actually ship, and do you understand accuracy vs latency tradeoffs?
> **Likely questions:** "Tell me about a time you cut scope with engineering." "How would you decide between a more accurate ETA model and a faster one?"
> **Structure:** STAR for the first; tradeoff matrix (quality, latency, cost, risk) for the second.
> **Story:** Driver app MVP: shipped on the existing map SDK instead of waiting for a rebuild; live in 6 weeks.
> **Ask Alex:** "How does the team decide when a model regression blocks a launch vs ships behind a flag?"

---

## Common Pitfalls

1. **Same prep for every interviewer.** The point is differentiation.
2. **Stage 2 without Stage 1.** You'll guess at questions instead of predicting them.
3. **Questions you could Google.** Ask about decisions and tradeoffs.
4. **Over-researching people.** Professional and public only.

---

## References

**Uses:** `story-bank`, InterviewReady `company-research-brief`, `interview-type-advisor`
**Feeds:** InterviewReady `practice-coach`, `interview-day-brief`
