---
name: job-application-workflow
description: Use when you have a new job description and want to go from "should I apply?" to a tailored resume and cover letter or application answers in one pass.
intent: Orchestrates the full application pipeline for a single role. Triage the role for fit, pick the career arc to lead with, map JD keywords to evidence, tailor resume bullets without fabricating, and draft the cover letter or application answers in a voice that sounds human. Every step pulls from your story bank so numbers stay consistent across every application you send. Pairs with interview-prep-workflow (InterviewReady Skills) once an interview is scheduled.
type: workflow
---

## Purpose

Most people apply to jobs in one of two broken modes. Spray mode: the same resume to 200 roles, a 1% response rate, and no idea why. Artisan mode: four hours per application, rewriting from scratch every time, numbers drifting between versions until a recruiter notices the same project was "$4M" on one resume and "$6M" on another.

This workflow is the middle path. It front-loads the thinking that should happen once (your story bank and career arcs), then makes each application a fast, repeatable sequence:

```
JD in
  → 1. Role fit triage         (apply / apply with a caveat / skip)
  → 2. Arc selection           (which version of your career story leads)
  → 3. Keyword and gap map     (JD language → your evidence)
  → 4. Resume tailoring        (bullets rewritten, 1 page, no fabrication)
  → 5. Application writing     (cover letter and/or application questions)
  → 6. Pipeline log            (record what you sent, so prep later is fast)
```

Target time once your story bank exists: 30 to 45 minutes per role.

---

## Key Concepts

### Do the expensive thinking once

The story bank and the career arcs are the two assets that make every later application cheap. If you skip them, every application re-derives your career from scratch, and quality depends on how tired you are that day. Build them first with `story-bank` and `career-arc-builder`.

**Why it matters:** consistency is a credibility signal. Recruiters compare your resume, your LinkedIn, your cover letter, and what you say in the screen. A single source of truth keeps all four aligned.

### Triage before you tailor

Tailoring a resume for a role you shouldn't apply to is the most common waste of time in a job search. Step 1 exists so you can stop after five minutes. A "skip" decision is a successful outcome of this workflow.

### Tailor language, never facts

Rewriting "built a routing service" as "designed a real-time decisioning API" is legitimate if it is true and it is the JD's vocabulary. Inventing a metric, a team size, or a technology you didn't use is not. The workflow enforces this by sourcing every bullet from the story bank.

### The output is a package, not a document

An application is a resume, a cover letter or answers, and a log entry. The log entry is what makes interview prep fast three weeks later when the recruiter finally calls and you can't remember which version you sent.

---

## Application

### Inputs

```
Use the job-application-workflow skill.

JD: [paste the full job description, or a URL]
Story bank: [paste, or "it's in this Project"]
Base resume: [paste, or link]
Constraints: [location, comp floor, visa, remote preference, anything that's a hard no]
```

If the story bank doesn't exist yet, stop and run `story-bank` first. Do not let the workflow improvise your history.

### Step 1. Role fit triage

Run `role-fit-triage`. Output: a scored fit across four dimensions, a recommendation (Apply / Apply with caveat / Skip), and the honest gaps.

If **Skip**, write one line in the pipeline log explaining why and stop. That line is valuable: patterns in your skips tell you whether your target list is wrong.

### Step 2. Arc selection

From `career-arc-builder`, pick the one arc that best matches what this team is hiring for. State it in one sentence: "Lead with Arc B (platform PM with API depth) because the role owns an internal developer platform."

Only one arc leads. A second arc may appear as supporting evidence in one or two bullets.

### Step 3. Keyword and gap map

Extract the 10 to 15 phrases that carry the most weight in the JD (repeated terms, terms in the title, terms in the first three bullets of "requirements"). Map each to a story bank entry:

| JD phrase | Your evidence | Strength |
|---|---|---|
| "experimentation" | Checkout A/B program, 14 tests | Strong |
| "ML forecasting" | Demand forecast pilot with data science | Partial: say "owned the product side", not "built the model" |
| "B2B SaaS" | None | Gap: name it honestly in the cover letter |

### Step 4. Resume tailoring

Run `resume-tailoring` with the arc and the keyword map. Output: a clean, copy-ready list of bullets per role, a list of suggested cuts ranked by lowest impact, and a 1-page check.

### Step 5. Application writing

Run `application-writing` for whichever the application asks for: cover letter, "why us", behavioral prompts, or short-form questions.

### Step 6. Pipeline log

Append one row to your tracker:

| Date | Company | Role | Tier | Arc | Resume version | Status | Notes |
|---|---|---|---|---|---|---|---|

The "Arc" and "Resume version" columns are the ones people skip and regret.

---

## Examples

### Weak run

> User pastes a JD. Claude immediately rewrites the whole resume, adds "LLM fine-tuning" because the JD mentions it, and writes a cover letter that opens with "I am excited to apply for..."

What went wrong: no triage, no arc, a fabricated skill, and a generic opener. The candidate now has to defend fine-tuning experience they don't have.

### Strong run

> **Triage:** 4/5 domain, 3/5 seniority (role is Senior, candidate is closer to Staff), 5/5 skills, 4/5 logistics. Apply.
> **Arc:** Arc A, marketplace growth PM. The team owns two-sided marketplace growth; the candidate has run it.
> **Keyword map:** 13 phrases mapped, 2 partial, 1 gap ("Zendesk ecosystem"). Gap gets one honest sentence in the cover letter.
> **Resume:** 6 bullets rewritten into the JD's vocabulary, 2 bullets cut, still 1 page.
> **Cover letter:** opens with the team's problem (resolution rate plateaus after the easy intents are automated), then the candidate's direct evidence.
> **Log:** row added with Arc A and resume version `2026-11-ai-support-v3`.

---

## Common Pitfalls

1. **Skipping triage because the company is exciting.** Excitement is a reason to apply carefully, not a reason to skip the fit check.
2. **Leading with two arcs.** The resume reads as unfocused. Pick one.
3. **Letting Claude fill gaps with plausible fiction.** If the story bank doesn't support it, it doesn't go in.
4. **Not logging the version.** You will be asked about "the resume you sent us" by people who read it more recently than you did.
5. **Polishing the cover letter before the resume.** The resume is read first and more often. Spend time in that order.

---

## References

**Uses:** `role-fit-triage`, `career-arc-builder`, `story-bank`, `resume-tailoring`, `application-writing`
**Feeds:** `target-list-pipeline` (log), `interviewer-game-plan`, and InterviewReady's `interview-prep-workflow` once an interview is booked
**Related:** InterviewReady `gap-analysis` for a deeper JD vs resume diagnostic after you get the interview
