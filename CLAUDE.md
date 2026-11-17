# CLAUDE.md

Instructions for Claude when collaborating on the ApplyReady Skills repository.

## What this repo is

A library of Claude skills for the application side of a job search: story bank, career arcs, role triage, resume tailoring, application writing, outreach, pipeline tracking, and per-interviewer loop prep. It is a companion to InterviewReady Skills and follows the same format.

## Governing principles

- **One source of truth.** Skills must source facts from the user's story bank. Never invent metrics, titles, tools, or scope.
- **Honest over flattering.** Score fit honestly, name gaps, and recommend Skip when warranted.
- **Teach the why.** Every Key Concept explains why it matters, not just what to do.
- **No personal data in the repo.** Examples use fictional people, companies, and numbers.

## Skill file standards

```yaml
---
name: kebab-case-matching-folder   # ≤64 characters
description: Use when ...          # ≤200 characters
intent: fuller purpose             # repo-facing
type: component | interactive | workflow
---
```

Required sections, in order: `## Purpose`, `## Key Concepts`, `## Application`, `## Examples`, `## Common Pitfalls`, `## References`.

Examples must include a weak and a strong case. References must list what the skill uses and feeds.

Run `python3 scripts/validate.py` after any edit.

## Writing style for skill content

- No em dashes
- No real employer codenames or real candidate metrics
- Specific, realistic, fictional examples over abstract placeholders
