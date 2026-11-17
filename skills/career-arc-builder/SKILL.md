---
name: career-arc-builder
description: Use when your career can be told several ways and you need 2-4 named narratives to choose from per role, including when your official titles undersell what you actually did.
intent: Turns a story bank into a small set of named career arcs, each a coherent version of your history aimed at a type of role. Includes a title-reframing method for people whose official titles lag their real scope (ops to PM, analyst to PM, IC to lead) that stays honest under a background check.
type: component
---

## Purpose

You are not one candidate. A person with six years across operations, platform work, and marketplace products is a strong fit for at least three different kinds of roles, but only if each application tells the version of the story that role cares about.

An arc is that version. It decides which eras are expanded, which are compressed, which metrics lead, and how you describe yourself in the first line of a resume or a cover letter.

Without arcs, people either write one muddled resume that tries to fit everything, or they rewrite their identity from scratch for each application and lose consistency.

---

## Key Concepts

### What an arc contains

| Field | Example (fictional) |
|---|---|
| Name | Arc A: Marketplace growth PM |
| For roles like | Delivery, mobility, and commerce marketplaces |
| One-line identity | "PM who has grown both sides of a delivery marketplace across 40 metros" |
| Lead eras | 2022 to present |
| Lead stories | Dispatch pricing launch, courier supply pilot, batching redesign |
| Lead metrics | Order growth, courier utilization, cost per delivery |
| Compressed | Early analytics years (one bullet) |
| Honest gaps | No B2B experience; frame merchant onboarding work as the closest evidence |

Most people need two or three arcs. Four is the ceiling; beyond that you are describing different careers.

### Title lag and how to reframe honestly

Many strong candidates have official titles that trail their real scope by years. "Program Manager" who owned a roadmap. "Operations Analyst" who shipped product. Recruiters screen on titles, so this costs interviews.

The honest reframe has three parts:

1. **Describe the work in the bullets, not the title.** Roadmap ownership, prioritization, experiment design, engineering partnership, launches. If the bullets read as PM work, the reader concludes PM.
2. **Use a functional descriptor carefully.** Some candidates write "Product Manager (official title: Operations Lead)" or "Operations Lead, Product" on the resume. Pick a form you can defend in a background check, where the official title is what gets verified.
3. **Say it out loud early.** One sentence in the cover letter or the recruiter screen: "My title was Operations Lead, but since 2024 I've owned the roadmap and shipped with a dedicated engineering team." Addressed proactively, it reads as confidence. Discovered later, it reads as hiding.

**Why it matters:** the goal is for the reader to understand your real scope, not to mislead them about your title. Background checks verify titles and dates; your framing has to survive that.

### Arcs share facts

Every arc pulls from the same story bank. Arcs change emphasis, order, and vocabulary. They never change numbers.

---

## Application

### Prompt

```
Use the career-arc-builder skill.
Story bank: [paste or "in this Project"]
Target role types: [e.g. marketplace PM, platform PM, product ops]
My official titles vs what I actually did: [list]
```

### Steps

1. Claude clusters your stories by the kind of employer that would value them most.
2. Proposes 2 to 4 arcs using the table above.
3. For each arc, drafts: a resume summary line, a 2-sentence "tell me about yourself" opener, and the eras to expand vs compress.
4. If titles lag scope, drafts the reframing sentence for the resume, the cover letter, and the recruiter screen.
5. Lists which arc to use for each company tier on your target list.

---

## Examples

### Weak

> "Experienced professional with a background in operations, program management, analytics, and product, passionate about AI and platforms."

Every arc at once. Nobody remembers it.

### Strong (fictional, three arcs from one history)

- **Arc A, marketplace growth PM:** "PM who has grown both sides of a delivery marketplace, with order and utilization metrics to show for it."
- **Arc B, platform PM:** "PM who builds internal platforms and APIs that other teams depend on: 400K pricing calls a day, 5 consuming services."
- **Arc C, ops-to-PM veteran:** "Six years of de facto product work, the last two as PM in everything but title; here's what I owned in each era."

Each one is true. Each one leads with different evidence.

---

## Common Pitfalls

1. **Arcs that are just keyword swaps.** If Arc A and Arc B lead with the same three stories, you have one arc.
2. **Overstating the title.** Reframe the scope, not the official record.
3. **Hiding the earliest era.** Compress it; don't delete it. Gaps in dates raise more questions than an old analyst role.
4. **Choosing the arc by what's trendy.** Choose it by what the specific team is hiring for.

---

## References

**Built from:** `story-bank`
**Feeds:** `role-fit-triage`, `resume-tailoring`, `application-writing`, `outreach-writer`
