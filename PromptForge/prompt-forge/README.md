# Prompt Forge

A Claude Skill for deliberate practice of prompt engineering craft. Not a tutorial, not a gamified curriculum — a senior practitioner who sits down with you, runs drills on your real work, and helps you get better over structured 30-day cycles.

## What it does

Runs a structured practice session:

1. **Intake** — one-sentence job, growth dimension, 30-day mastery target, current skill level, time available.
2. **Drill** — picks a technique appropriate to where you are, builds a scenario from your real work, runs the drill, gives specific feedback.
3. **Loop** — multiple drills per session. Dimensions and technique names logged after each.
4. **Persist** — saves your learning goals, growth edge, and session history to a `forge-learning-goals.md` file in your workspace so next session picks up where you left off.
5. **Cycle** — every ~30 days, close the cycle with a reflection and start a new one with a new dimension or goal.

## Installing

### Claude Code / personal skills folder

Already installed if you're reading this from `~/.claude/skills/prompt-forge/`. The skill is auto-discovered — no further setup.

### Claude Enterprise / Claude.ai project

Upload `SKILL.md` and all files in `references/` into a Claude project as reference documents. The skill's `SKILL.md` will be found by Claude when you invoke it.

### Triggering

In any conversation where the skill is available, say one of:

- "Run the Prompt Forge"
- "Let's do prompt drills"
- "I want to sharpen my prompt engineering"

Claude will read `SKILL.md` and begin.

## Files

- `SKILL.md` — the skill itself (load order: frontmatter, philosophy, protocol).
- `references/dimensions.md` — the five growth dimensions.
- `references/techniques.md` — the curriculum map (Level 1–5) and the meta-prompting five-skill progression.
- `references/drill-patterns.md` — the eight drill types with examples.
- `references/learning-goals-template.md` — the exact markdown for the `forge-learning-goals.md` file.

## Good times to run it

- You have a repeating task (quarterly update, investment memo, post-project review) and want a sharper reusable prompt.
- You're getting mediocre output and want structured practice diagnosing why.
- You have 15–60 minutes of focused time and want deliberate practice rather than another how-to video.

## Bad times

- You're mid-deliverable with a clock ticking. Finish the work first.
- You have less than 10 minutes. The loop needs room to breathe.
- You want validation, not critique. The Forge will push back.
