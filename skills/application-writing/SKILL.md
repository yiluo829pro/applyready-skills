---
name: application-writing
description: Use when you need a cover letter, a "why us" answer, or written behavioral answers that sound like you, lead with the team's problem, and avoid AI tells.
intent: Drafts cover letters and application question answers from your story bank and the target role. Covers the problem-first cover letter structure, decision-first STAR for written behavioral prompts, short-form answers, and a voice checklist that removes the patterns readers now associate with AI-generated text.
type: component
---

## Purpose

Hiring teams now read a lot of AI-written applications, and they have learned the tells. A cover letter that opens with "I am thrilled to apply" and closes with "I would welcome the opportunity" signals that no one was home. This skill produces writing that is specific enough that it could only have been written by you, for this team.

---

## Key Concepts

### Problem-first cover letters

Structure (250 to 350 words):

1. **Their problem** (2-3 sentences). What is this team trying to solve right now? Use the JD, the company's recent launches, and their public writing. "Same-day delivery margins tend to collapse outside dense metros; the next gains come from smarter batching and courier supply planning."
2. **Your direct evidence** (1 paragraph). The one or two stories from your lead arc that map most closely, with numbers.
3. **Why this team specifically** (2-3 sentences). Something you could not say about their competitor.
4. **The honest gap, if any** (1 sentence), and how you'd close it.
5. **Close** (1 sentence). Plain. No "I would welcome the opportunity."

### Decision-first STAR for written prompts

In writing, the reader wants the point immediately. Reorder STAR:

- **Action/decision first:** what you decided or did
- **Situation and task second:** the minimum context
- **Result last:** quantified

Use "I" for your actions. "We" hides ownership. Target 350 to 400 words for a 3-minute spoken equivalent; shorter if the form has a limit.

### Short-form answers

For 100 to 200 word fields: three to five sentences. One claim, one piece of evidence, one link to the company. Then stop.

### Voice checklist

Remove before sending:
- **Em dashes.** Many readers now treat them as an AI tell. Use periods or commas.
- **Stock openers and closers:** "I am excited/thrilled to apply," "I would welcome the opportunity," "In today's fast-paced world."
- **Inflated adjectives:** "passionate," "dynamic," "results-driven," "cutting-edge"
- **Rule-of-three padding:** "innovative, scalable, and impactful"
- **Internal jargon:** project codenames, tool acronyms. Use the story bank's public descriptions.
- **Sentences starting with "I"** three times in a row

Then read it aloud. If you wouldn't say it to a hiring manager over coffee, rewrite it.

### Iterate, don't regenerate

The best results come from you writing a rough version and asking Claude to tighten it, or Claude drafting and you editing. Asking for five fresh drafts produces five versions of the same average.

---

## Application

### Prompt

```
Use the application-writing skill.
Write: [cover letter / "why us" / behavioral prompt: paste it / short answers]
Role and JD: [paste]
Lead arc and keyword map: [from role-fit-triage]
Story bank: [paste or "in this Project"]
Length limit: [if any]
```

### Output

- The draft, as clean copy-ready prose
- A one-line note on which stories it uses
- Any claim that needed a story bank fact it couldn't find, flagged

---

## Examples

### Opening, weak → strong

**Weak:** "I am thrilled to apply for the Product Manager role at Acme. With years of experience, I am passionate about building products that delight users."

**Strong:** "Acme now delivers in under an hour in its ten biggest metros. The harder problem is the next thirty, where order density is too low for the same courier model to break even. That's the problem I've spent the last two years on."

### Behavioral, "we" → "I"

**Weak:** "We noticed the outage and we set up meetings to fix it."
**Strong:** "I paused the rollout in the two affected metros within an hour, set up a daily check-in with engineering and city ops, and owned the fix list until all three causes were closed."

---

## Common Pitfalls

1. **Opening with yourself.** Open with their problem.
2. **Restating the resume.** The cover letter should add the why and the connection, not repeat bullets.
3. **Generic "why us."** If the sentence works for their top competitor, it isn't specific enough.
4. **Over-length.** Hiring managers skim. Shorter, more specific wins.
5. **Leaving AI tells in.** Run the voice checklist every time.

---

## References

**Uses:** `story-bank`, `career-arc-builder`, `role-fit-triage`, `resume-tailoring`
**Related:** InterviewReady `behavioral-story-builder` (for spoken delivery), `outreach-writer`
