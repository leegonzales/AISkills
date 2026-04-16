# forge-learning-goals.md Template

Give the user this exact content to paste into a new file called `forge-learning-goals.md` in their current project/workspace. The Forge reads this file at the start of every session so it can pick up where the user left off.

---

## First-session template

When the user finishes the full intake, have them create `forge-learning-goals.md` with this content (substitute their answers for the `{bracketed}` values):

```markdown
# Forge Learning Goals
*Personal learning plan for the Prompt Forge*

## The Work
{one-sentence restatement of the work they named}

## Starting Level
{A / B / C / D with label}

## Current 30-Day Cycle

**Cycle number:** 1
**Started:** {today's date}
**Target end:** {today's date + 30 days}

### Growth Edge
Primary dimension: {dimension they chose}
Why this dimension matters for their work: {one-sentence rationale}

### 30-Day Mastery Target
{their specific mastery description, cleaned up into one clear sentence}

### Techniques To Focus On This Cycle
- {technique 1}
- {technique 2}
- {technique 3}
- {technique 4 — optional}

### Session History (this cycle)
*(empty — will grow across this cycle)*

## Completed Cycles
*(empty — will grow as cycles complete)*
```

Tell the user:

> "Paste that into a new file called `forge-learning-goals.md`. I'll read it at the start of every session so we always pick up where we left off. The structure is built around 30-day cycles — each cycle targets one dimension and one mastery goal. When you hit 30 days or the goal feels landed, we close the cycle and start a new one."

---

## Session-history entry (append after every session or on `/recap`)

Append to the "Session History (this cycle)" section:

```markdown
#### Session {date}
- Techniques practiced: {list}
- Drills run: {count}
- Dimensions exercised: {list}
- What got sharper: {one or two specific observations}
- Next time focus: {your suggestion}
```

---

## Cycle transition (archive and begin next cycle)

When closing a cycle, move the current cycle into "Completed Cycles" with this structure:

```markdown
### Cycle {N} — Completed {date}
- Growth edge: {dimension}
- Target: {mastery target}
- Outcome: {hit / close / pivoted — one sentence of reflection}
- Key techniques that stuck: {2–3 techniques they now own}
- Session count: {total drills in the cycle}
```

Then update "Current 30-Day Cycle" with the new cycle number, dates, dimension, mastery target, and technique list.

---

## Why keep this file

The file is how the Forge remembers — across sessions, weeks, and months. Without it, every session starts from scratch. With it, cycles compound. Users who run the Forge for six months end up with a real developmental arc they can look back on, not just a pile of disconnected practice.

The file lives in the user's project or workspace, not in the skill. That's intentional — it belongs to them.
