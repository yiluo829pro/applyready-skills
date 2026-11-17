---
name: role-fit-triage
description: Use when you have a job description and want a fast, honest apply-or-skip call with a fit score, the arc to lead with, and the gaps to address.
intent: A five-minute triage that scores a role on domain, seniority, skills, and logistics, names which career arc to lead with, extracts the JD's weight-bearing keywords, and flags honest gaps. Designed to stop you from tailoring for roles you shouldn't pursue. For a deep diagnostic after you land an interview, use InterviewReady's gap-analysis.
type: component
---

## Purpose

The highest-leverage minute in a job search is the one where you decide not to apply. This skill makes that decision fast and explicit, and when the answer is "apply," it hands the next step a clear brief: which arc, which keywords, which gaps.

---

## Key Concepts

### Four dimensions, scored 1 to 5

| Dimension | 5 looks like | 1 looks like |
|---|---|---|
| Domain match | You've shipped in this exact problem space | No overlap and no transferable angle |
| Seniority alignment | Title, scope, and years match | Two levels off in either direction |
| Skills match | Most "requirements" map to Strong evidence | Most requirements are gaps |
| Logistics | Location, comp, visa, and schedule all work | A hard constraint is violated |

**Logistics is a gate, not an average.** A 1 on logistics means Skip regardless of the other scores, unless you'd actually change the constraint (for example, relocating for a top-tier company).

### Reading the JD for weight

Not all JD lines matter equally. Weight goes to:
- Words in the title and the first paragraph
- Phrases repeated two or more times
- The first three bullets under "requirements"
- Anything under "you must" vs "nice to have"

"Nice to have" gaps rarely sink an application. Gaps in the first three requirements usually do.

### Honest gaps are a feature

Every strong application has one or two gaps. Naming them yourself (in a cover letter line or the recruiter screen) is more persuasive than hoping no one notices. The triage output always includes a "how to address" line per gap.

### Recommendation

- **Apply:** no score below 3, logistics clear
- **Apply with caveat:** one score of 2, with a credible way to address it
- **Skip:** logistics fails, or two or more scores of 2 or below

---

## Application

### Prompt

```
Use the role-fit-triage skill.
JD: [paste or URL]
My arcs: [paste or "in this Project"]
Hard constraints: [location, comp floor, remote, visa]
```

### Output

```
## Fit: [Company] / [Role]
| Dimension | Score | Why |
| Domain | 4 | ... |
| Seniority | 3 | ... |
| Skills | 5 | ... |
| Logistics | 4 | ... |

Recommendation: Apply / Apply with caveat / Skip
Lead arc: Arc X, because [one sentence]

## Weight-bearing keywords (10-15)
| JD phrase | Evidence from story bank | Strong / Partial / Gap |

## Gaps and how to address them
- Gap: ... → Address by: ...

## Assumptions I made
- ...
```

The "Assumptions" section is mandatory. If the JD is vague on level or location, Claude says what it assumed so you can correct it.

---

## Examples

### Contrast

**Weak:** "You're a great fit! Your experience aligns well with the role."
**Strong:** "Skills 5, domain 4, seniority 2: the role is a Senior PM reporting to a Group PM, and you'd be coming in below your current scope. Apply with caveat only if the company is Tier 1 for you; otherwise skip. Gap to address: no B2B sales-assisted motion; one sentence in the cover letter about the enterprise escalation work."

---

## Common Pitfalls

1. **Averaging away a dealbreaker.** Logistics is a gate.
2. **Treating every JD bullet as equal.** Read for weight.
3. **Scoring generously because the company is exciting.** Score the role, then decide separately whether excitement justifies a caveat.
4. **No assumptions section.** Hidden assumptions are where triage goes wrong.

---

## References

**Uses:** `career-arc-builder`, `story-bank`
**Feeds:** `resume-tailoring`, `application-writing`, `target-list-pipeline`
**Related:** InterviewReady `gap-analysis` (deeper, interview-focused)
