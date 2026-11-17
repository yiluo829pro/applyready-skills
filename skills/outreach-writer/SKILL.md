---
name: outreach-writer
description: Use when you need a short networking, referral, or recruiter message that gets a reply: former colleagues, hiring managers, or people at a target company.
intent: Drafts short outreach messages for LinkedIn, email, or text, matched to the relationship (warm, lukewarm, cold) and the ask (referral, informational call, intro to hiring manager, reply to a recruiter). Keeps messages under 120 words, makes the ask specific, and makes saying yes easy.
type: component
---

## Purpose

Referrals convert far better than cold applications at most companies, but most outreach messages fail for the same reasons: too long, no clear ask, and all about the sender. This skill writes messages that respect the reader's time.

---

## Key Concepts

### Match the message to the relationship

| Relationship | Lead with | Ask |
|---|---|---|
| Warm (worked together) | Shared context, one line | Direct: "Would you refer me for X?" |
| Lukewarm (met once, alumni, mutual) | The connection | Small: 15-minute call or a pointer |
| Cold (no connection) | Something specific about their work | Smallest: a question they can answer in one reply |
| Recruiter inbound | Interest + one fit line | Next step and timing |

### The three-part message

1. **Why you, why now** (one sentence)
2. **The ask** (one sentence, specific: role link, time length)
3. **Make it easy** (one line: "Happy to send a blurb you can forward")

Under 120 words. Under 60 for a LinkedIn connection note.

### The forwardable blurb

For referrals, include a 2 to 3 sentence blurb about yourself written in third person that the referrer can paste into an internal referral form. This removes the most effort from their side.

### Follow up once

One follow-up after 5 to 7 business days. Then stop. Persistence beyond that reads as pressure.

---

## Application

### Prompt

```
Use the outreach-writer skill.
Recipient: [name, role, company, how I know them]
Ask: [referral / call / intro / recruiter reply]
Role: [link or title]
Lead arc: [from career-arc-builder]
Channel: [LinkedIn / email / text]
```

Claude drafts the message. For anything that will be sent, you review and send it yourself.

---

## Examples

### Cold, weak
> "Hi! I'm a PM with lots of experience, passionate about tech. I'd love to pick your brain about your company and any opportunities. Let me know!"

### Cold, strong
> "Hi Sam, I read your post on ETA accuracy in rural zones. I've hit the same issue with sparse GPS data on a grocery delivery app. Did you end up adding a fallback model or widening the delivery windows? I'm also applying for the Routing PM role, but mainly curious about your answer."

### Warm referral, strong
> "Hi Priya, I'm applying for the Senior PM role on Acme's dispatch platform team (link). It's close to the batching work we did together. Would you be open to referring me? Blurb below if it helps. Thanks either way.
> *Blurb:* Jordan is a PM with six years in delivery marketplaces, most recently shipping a dispatch pricing system across 40 metro areas."

---

## Common Pitfalls

1. **"Pick your brain."** Vague asks get no reply.
2. **Your resume in the message.** Link it; don't paste it.
3. **Asking a stranger for a referral.** Earn a conversation first.
4. **Following up three times.** Once.

---

## References

**Uses:** `career-arc-builder`, `target-list-pipeline`
**Related:** `application-writing` (voice checklist applies here too)
