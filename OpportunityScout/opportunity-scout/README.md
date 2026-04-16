# Opportunity Scout

A Claude Skill for finding high-leverage AI opportunities in your actual work, then turning the strongest one into a 4-week launch plan.

## What it does

Runs a five-stage discovery session:

1. **Opening** — 4 questions: your job, your biggest work frustration, what you're already doing with AI that works, and how ambitious you want this session to be.
2. **Terrain** — 2–3 follow-up questions that surface the hidden structure of your work, watching for signals of the four transformation patterns.
3. **Map** — 5–7 specific candidate moves, ranked internally on feasibility × impact, with variety across transformation patterns.
4. **Ember** — you pick the one that makes you lean forward; the Scout names the transformation pattern and surfaces constraints.
5. **Blueprint + 4-Week Plan** — first-version design, then a week-by-week plan with one action, one decision, one evaluation per week.

You leave with a four-line summary: pattern, move, first step (next 24 hours), evaluation (4 weeks).

## Installing

### Claude Code / personal skills folder

Already installed if you're reading this from `~/.claude/skills/opportunity-scout/`. The skill is auto-discovered.

### Claude Enterprise / Claude.ai project

Upload `SKILL.md` and all files in `references/` into a Claude project as reference documents.

### Triggering

In a conversation where the skill is available, say one of:

- "Run the Opportunity Scout"
- "Where can I use AI in my work?"
- "Help me find AI opportunities"
- "Let's scout for leverage"

## Files

- `SKILL.md` — the skill itself (five-stage protocol, operating stance, rules).
- `references/transformation-patterns.md` — the four patterns (Impossible-to-Possible, Days-to-Hours, Hours-to-Minutes, Invisible-to-Visible) with recognition signals and examples.
- `references/scout-modes.md` — the four session modes (Efficiency, Workflow, Frontier, Wild) tied to the ambition answer.
- `references/scoring-rubric.md` — feasibility × impact scoring for ranking candidate opportunities.
- `references/blueprint-templates.md` — first-version design starting points per transformation pattern.
- `references/sample-output.md` — a full example session showing the expected level of specificity.

## Good times to run it

- Quarterly planning — when priorities shift and you want to re-scan for leverage.
- After a big project closes and bandwidth opens.
- When your team asks "how else could we be using AI?" and you want real answers.
- When a direct report is exploring AI and you want to coach them through structured discovery.

## Bad times

- You already know exactly what to build. Just build it.
- You're underwater on deliverables this week. The Scout is planning, not execution.
- You're looking for validation of an idea you already love. The Scout will push back.
