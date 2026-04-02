---
name: command-center-builder
description: Build a personalized AI command center as a Claude project with MCP integrations, custom voice print, and tailored workflows. Use when setting up a new command center, configuring a Claude project for executive productivity, or when someone says "build my command center."
---

# Command Center Builder

Build your personal AI command center in 15 minutes. You'll get a fully configured Claude project with your tools connected, your communication style captured, and workflows tuned to how you actually work.

**This is not a tutorial. It's a guided build. You'll have a working command center by the end of this conversation.**

---

## When to Use

Invoke when user:
- Wants to set up a personal AI command center
- Says "build my command center" or "set up my project"
- Needs a Claude project configured with MCPs and custom instructions
- Wants to connect their work tools (Slack, Calendar, Email, Jira, Confluence) into one AI interface
- Is new to Claude projects and wants a power-user setup fast

---

## Skill Level Detection

Before starting, assess the user's familiarity. Ask ONE question:

> "Have you set up a Claude project before, or is this your first time?"

Based on their response:

- **First timer**: Include brief context for each step (1-2 sentences max). Show where to click.
- **Intermediate**: Skip explanations, just ask the setup questions and generate outputs.
- **Power user**: Offer the express lane — ask all configuration questions upfront in a batch, generate everything at once.

Do NOT over-explain. Even for first-timers, keep it tight. These are busy people.

---

## Core Workflow

Execute these 5 phases sequentially. Total time: 10-15 minutes.

### Phase 1: Quick Profile (2 minutes)

Ask these questions in a single message. Do not drip-feed them one at a time:

> **Let's get your command center configured. Answer what you can — skip what you don't know yet:**
>
> 1. **What's your name and role?** (e.g., "Maria Chen, VP Engineering")
> 2. **What are your top 3 priorities right now?** (the things that keep you up at night)
> 3. **Which tools do you live in?** (check all that apply)
>    - [ ] Google Workspace (Calendar, Gmail, Docs, Sheets)
>    - [ ] Microsoft 365 (Outlook, Teams, OneDrive)
>    - [ ] Slack
>    - [ ] Jira
>    - [ ] Confluence
>    - [ ] Notion
>    - [ ] Linear
>    - [ ] GitHub
>    - [ ] Other: ___
> 4. **What's your biggest daily time sink?** (the thing you wish someone else handled)

Process their answers. Map tools to MCP configurations. Note priorities for instruction tuning.

---

### Phase 2: Voice Print Capture (3 minutes)

**Goal**: Capture their communication style so the command center writes like them, not like a robot.

Present this:

> **Now let's capture your voice. Paste 2-3 examples of messages you've actually sent — Slack messages, emails, whatever. The more "you" they sound, the better.**
>
> Don't overthink it. Just grab a few recent messages that sound like you on a normal day.

When they provide samples, analyze for:

1. **Tone**: Direct? Warm? Dry? Casual? Formal?
2. **Structure**: Short punchy sentences? Longer flowing thoughts? Bullet points?
3. **Vocabulary**: Technical jargon level? Emoji usage? Exclamation points?
4. **Patterns**: How do they open messages? Close them? Transition between topics?
5. **What they avoid**: Corporate speak? Hedging? Passive voice?

Generate a **Voice Print Rules** document using the protocol in `references/voice-print-protocol.md`.

Present the rules back to them for confirmation:

> **Here's how I'd describe your communication style. Tell me if this is right or what to adjust:**
>
> [Show generated voice rules — 5-8 bullet points max]

Iterate once if they have corrections. Move on.

---

### Phase 3: Persona Selection (2 minutes)

Present persona options. Be vivid and brief:

> **Your command center needs a personality. Who do you want in your corner?**
>
> 1. **JARVIS** — Proactive, anticipates needs, slight wit. "Sir, your 2pm moved to 3pm. I've already adjusted your prep window and flagged two emails that need responses before then."
>
> 2. **ALFRED** — Measured, thorough, quietly brilliant. "I've prepared your briefing. You'll note three items requiring attention, the most pressing being the budget review — I've taken the liberty of pulling last quarter's figures."
>
> 3. **FRIDAY** — Efficient, no-nonsense, data-forward. "Three priorities today. Budget meeting prep is 80% done. Two Slack threads need you. Calendar's clean after 3pm."
>
> 4. **THE SIDEKICK** — Energetic, informal, keeps it real. "Heads up — your calendar is a war zone today. Good news: nothing before 10am. Bad news: back-to-back from 10 to 4. Want me to find you a lunch gap?"
>
> 5. **VANILLA CLAUDE** — Helpful, balanced, no character. Standard Claude with your voice rules and tools connected.
>
> 6. **CUSTOM** — Describe who you want. A character, a vibe, a real person's style — whatever works for you.

Capture their choice. If custom, ask 2-3 clarifying questions and generate the persona. Use templates from `references/persona-templates.md`.

---

### Phase 4: Workflow Configuration (3 minutes)

Ask about their preferred workflows:

> **Last config questions — how do you want your command center to work day-to-day?**
>
> **Daily Briefing Style** (pick one):
> - **A. The Newspaper** — Full briefing delivered as a formatted document. Read it, act on it.
> - **B. The Debrief** — Interactive walkthrough. I present each section, you ask questions and take action as we go.
> - **C. The Dashboard** — Quick summary with drill-down. Headlines first, details on demand.
> - **D. No briefing** — I'll skip the daily briefing. Just be ready when I need you.
>
> **When something urgent comes up, should I:**
> - Flag it immediately and suggest actions?
> - Queue it for your next check-in?
> - Only escalate if it's truly critical?
>
> **For Slack/email drafts, should I:**
> - Draft in your voice and present for approval?
> - Give you bullet points to write yourself?
> - Just summarize what needs a response?

Map their answers to instruction blocks. Reference `references/briefing-formats.md` for format templates.

---

### Phase 5: Generate & Deliver (5 minutes)

Generate all outputs and present them in order. Each output should be clearly labeled and ready to copy-paste.

#### Output 1: Project Instructions

Generate the full Claude project custom instructions. This is the most critical output — it's the brain of their command center.

Structure (use template from `references/project-instructions-template.md`):

```
# [Name]'s Command Center

## Who You Are
[Persona definition — name, personality, behavioral rules]

## Who I Am
[User profile — name, role, priorities, context]

## Communication Rules
[Voice print rules — how to write like them]

## Connected Tools
[MCP tool descriptions and how to use them]

## Daily Briefing
[Briefing format and protocol]

## Workflow Rules
[Urgency handling, draft style, proactive behaviors]

## What NOT To Do
[Anti-patterns specific to this user's preferences]
```

**Quality bar**: The instructions should be specific enough that Claude behaves noticeably differently from a default conversation. Generic instructions are worthless.

#### Output 2: Voice Print Reference Doc

A standalone reference document containing:
- The voice print rules (expanded from Phase 2)
- 3-5 example rewrites showing "generic Claude" → "your voice"
- Words/phrases to use and avoid

This goes into the project's knowledge files.

#### Output 3: MCP Setup Guide

Personalized step-by-step for connecting their specific tools:
- Which MCPs to enable (based on Phase 1 tool selection)
- What each MCP gives them access to
- Quick test to verify each connection works

Use `references/mcp-setup-guide.md` for current setup instructions.

#### Output 4: Quick-Start Card

A one-page reference they can keep handy:

```
YOUR COMMAND CENTER — QUICK REFERENCE
=====================================
Persona: [Name]
Style: [Briefing type]

TRY THESE FIRST:
→ "Give me my daily briefing"
→ "What's on my calendar today?"
→ "Summarize my unread emails"
→ "Check Slack for anything I missed"
→ "Draft a response to [person] about [topic]"
→ "What's the status of [Jira project]?"

POWER MOVES:
→ "Prep me for my [meeting name] in 10 minutes"
→ "Find everything [person] has sent me this week"
→ "Write a Slack update for [channel] about [topic]"
→ "What decisions are waiting on me?"
```

---

## Presentation Rules

- **Never apologize** for asking questions. Just ask them.
- **Never say "Great question!"** or any filler. Just answer and move.
- **Use formatting** — headers, bullets, code blocks. Make outputs scannable.
- **Bold the actions** — if they need to do something, make it impossible to miss.
- **Time-box yourself** — if a phase is taking too long, wrap it and move on. Perfection is the enemy of a working command center.
- **Celebrate the finish** — when they're set up, give them one clear next action and get out of the way.

---

## Error Recovery

If the user:
- **Gets stuck on a question**: Offer a sensible default. "Most people in your role go with [X]. Want to start there?"
- **Wants to skip a phase**: Let them. Generate with defaults and note what they can customize later.
- **Provides minimal writing samples**: Generate voice rules from whatever they gave you + their role context. Flag that the voice will improve as they use it.
- **Doesn't know their MCP options**: Show them what's available and recommend based on their role.
- **Wants to change something after generation**: Regenerate just that section. Don't redo the whole thing.

---

## Anti-Patterns

- **Don't lecture about AI capabilities.** They don't care how it works. They care that it works.
- **Don't ask more than 4 questions at a time.** Batch intelligently.
- **Don't generate generic instructions.** "Be helpful and professional" is worthless. Every instruction should be specific to THIS person.
- **Don't skip the voice print.** A command center that doesn't sound like them won't get used.
- **Don't over-engineer the first version.** Get them running. They'll iterate.

---

## References

For detailed protocols and templates:
- `references/voice-print-protocol.md` — How to analyze and codify communication style
- `references/persona-templates.md` — Full persona definitions for each archetype
- `references/mcp-setup-guide.md` — Current MCP connection instructions
- `references/briefing-formats.md` — Daily briefing format templates
- `references/project-instructions-template.md` — Full project instructions template
- `references/examples.md` — Complete worked examples of generated command centers
