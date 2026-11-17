# ApplyReady Skills

**Claude skills for the application side of a job search: from "should I apply?" to a tailored resume, cover letter, outreach, and a per-interviewer game plan.**

[![Skills](https://img.shields.io/badge/skills-9-informational?style=flat-square)](#the-9-skills)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

Designed to pair with an interview-prep skill library (for example, InterviewReady Skills). That library covers prep once you have an interview. ApplyReady covers everything before that, plus the per-interviewer layer of loop prep.

---

## Why this exists

Two problems cost most job seekers the most time:

1. **Every application re-derives your career from scratch.** Numbers drift between resume versions, and your best stories get described differently each time.
2. **Official titles often undersell scope.** Many strong candidates need an honest, repeatable way to show product work their titles don't reflect.

The fix is to do the expensive thinking once (a story bank and a few named career arcs), then make each application a fast, repeatable pipeline. For interviews, preparing per interviewer, not per company, is what makes each conversation feel like you already understand that person's part of the business.

These skills package that system so anyone can use it.

---

## Start here

1. Run **`story-bank`** once. It interviews you era by era and builds your single source of truth.
2. Run **`career-arc-builder`** once. It gives you 2 to 4 named versions of your story.
3. For every job description, run **`job-application-workflow`**.

Optional but recommended: paste [`templates/claude-project-instructions.md`](templates/claude-project-instructions.md) into a Claude Project and upload your story bank, so Claude knows your background in every conversation.

See [START_HERE.md](START_HERE.md) for the 60-second version.

---

## The 9 skills

### Foundation (do once)

| Skill | What it does |
|---|---|
| **[story-bank](skills/story-bank/SKILL.md)** | Canonical work history: eras, stories, a metrics ledger with sources, and an internal-to-public jargon map |
| **[career-arc-builder](skills/career-arc-builder/SKILL.md)** | 2 to 4 named career narratives, plus an honest method for reframing titles that lag your scope |

### Per application

| Skill | What it does |
|---|---|
| **[job-application-workflow](skills/job-application-workflow/SKILL.md)** | Workflow: triage → arc → keywords → resume → cover letter → log |
| **[role-fit-triage](skills/role-fit-triage/SKILL.md)** | Five-minute apply/skip call with 4-dimension scoring and honest gaps |
| **[resume-tailoring](skills/resume-tailoring/SKILL.md)** | Bullet rewrites in the JD's vocabulary, no fabrication, ranked cuts to hold one page |
| **[application-writing](skills/application-writing/SKILL.md)** | Problem-first cover letters, decision-first STAR, and a voice checklist that removes AI tells |

### Pipeline and network

| Skill | What it does |
|---|---|
| **[target-list-pipeline](skills/target-list-pipeline/SKILL.md)** | Tiered target list and a tracker with the columns you'll want later |
| **[outreach-writer](skills/outreach-writer/SKILL.md)** | Short referral, networking, and recruiter messages matched to the relationship |

### Once a loop is scheduled

| Skill | What it does |
|---|---|
| **[interviewer-game-plan](skills/interviewer-game-plan/SKILL.md)** | Workflow: predicted questions from comparables, then a per-interviewer dossier |

---

## How the skills connect

```
story-bank ──► career-arc-builder
     │                 │
     ▼                 ▼
job-application-workflow
  ├── role-fit-triage
  ├── resume-tailoring
  ├── application-writing
  └── log ──► target-list-pipeline ──► outreach-writer
                                   │
                    interview booked
                                   ▼
                   interviewer-game-plan
                                   ▼
          InterviewReady: practice-coach, interview-day-brief
```

---

## Install

**Claude (web or desktop):** zip a skill folder (or run `scripts/build_zips.sh`) and upload it in Claude's Skills settings.

**Claude Project:** paste the project template into Project instructions and upload the SKILL.md files you use most as Project files.

**Claude Code:**
```bash
git clone https://github.com/your-username/applyready-skills.git
cp -r applyready-skills/skills/* ~/.claude/skills/
```

---

## Example

[`examples/sample-story-bank.md`](examples/sample-story-bank.md) is a complete story bank for a fictional candidate. Use it to see the format before building your own.

---

## Design principles

- **One source of truth.** Every number comes from the story bank. Arcs change emphasis, never facts.
- **Triage before effort.** A fast "skip" is a good outcome.
- **Honest framing.** Reframe scope, never the official record. Name your gaps before someone else finds them.
- **Sound like a person.** No stock phrases, no em dashes, no internal jargon.

---

## Contributing

Issues and PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/validate.py` before opening a PR.

## License

[CC BY-NC-SA 4.0](LICENSE). Free for personal use and sharing with attribution; non-commercial; share-alike.
