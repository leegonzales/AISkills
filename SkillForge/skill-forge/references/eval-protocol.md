# Eval Protocol

How to measure whether a skill is good — structurally *and* behaviorally. Read this when setting up the eval for a skill before forging it.

## Tier A — Structural gate (fast, static, necessary-not-sufficient)

Run first; it's cheap and filters obvious problems.

1. `./SkillTemplate/scripts/validate-skill.sh <SkillDir>/<slug>` — required files, frontmatter, encoding, placeholders.
2. Score against `docs/skill-evaluation-rubric.md` — 6 categories, 100 points: Core Value (25), Documentation (20), Technical Structure (20), Production Readiness (15), Ecosystem Fit (10), Innovation (10). Gate: **≥85**.
3. Structural smells to fix before spending on Tier B: SKILL.md bloat (push detail to `references/`), missing progressive disclosure, redundancy with an existing skill, unresolved placeholders.

**Tier A passing means the skill is well-formed. It says nothing about whether it works.** That's Tier B.

## Tier B — Behavioral outcome eval (the real bar)

The question: *does an agent using this skill produce measurably better outputs than one without it, reliably, on tasks it hasn't been tuned against?*

### 1. Build the eval set (the most important step)

- **5-10 real tasks** the skill is meant to help with. Real > synthetic — pull from actual use, issues, or representative jobs.
- **Diverse** — span the skill's intended range (easy/hard, common/edge). A skill that only helps on the happy path isn't optimal.
- **Split into tuning vs holdout.** The loop may see the tuning tasks every round; the **holdout is sacred** — checked only at promotion, never in the loop's working context. Holdout leakage silently turns "improvement" into "memorization."
- **Pre-commit it in writing** before the loop runs. An eval set you adjust mid-loop measures nothing.

### 2. Define the output rubric + must-pass checks

- The **output rubric** is the artifact's quality bar — reuse the artifact's own rubric where one exists (e.g., for PM artifacts, `agent_docs/pm-planning-skills/02-artifact-quality-bars.md`; for prose, `prose-polish`'s dimensions). Score each dimension 0-N.
- **Must-pass checks** are non-negotiables that may never regress (e.g., "never fabricates a metric," "always lists non-goals"). A round that lifts the average but breaks a must-pass is a **revert**, not a promotion.

### 3. Run two arms

For each eval task, generate the output **twice**:
- **Baseline arm** — a capable agent doing the task *without* the skill.
- **Skill arm** — the same agent *with* the skill invoked.

Hold everything else constant (same model, same task framing, same budget). The delta is the skill's contribution.

### 4. Score externally — never self-grade

- Use an **external reviewer panel**: `multiagent-review`, or `gemini-peer-review` + `codex-peer-review` for genuinely independent models. The agent that produced the output does **not** score it.
- **Blind where possible** — don't tell the scorer which arm is which; it removes a confirmation bias.
- **Diverse, not redundant** — two copies of the same judge ≈ one judge (effective-n). Different models/lenses give real convergence; identical ones give sycophantic agreement.

### 5. Compute lift

- **Magnitude:** mean(skill-arm score) − mean(baseline-arm score), per dimension and overall.
- **Reliability:** variance/worst-case across the set. A skill that helps a lot on 3 tasks and hurts on 2 is not yet good — consistency is part of optimal.
- **Win rate:** fraction of tasks where the skill arm strictly beats baseline.

A skill is **behaviorally optimal** when, on the **holdout**, it shows positive lift with low variance and a high win rate, and breaks no must-pass check.

## Common eval failures (guard against)

| Failure | Symptom | Fix |
|---------|---------|-----|
| Self-grading | Skill/agent scores its own output | External panel |
| Holdout leakage | Great on tuning set, fails on new tasks | Keep holdout out of loop context; rotate |
| Synthetic-only eval | Looks great, fails in real use | Use real tasks |
| Single judge | Confident but wrong | Diverse panel (effective-n) |
| Moving the eval | "Improvement" that's just a redefined target | Pre-commit eval + rubric in writing |
| Average hides regressions | Mean up, a must-pass broke | Must-pass checks gate promotion independently |
| Happy-path-only set | Optimal on easy, useless on hard | Diverse, edge-inclusive eval set |

See [refinement-loop.md](refinement-loop.md) for how this eval drives the improvement loop, and `loop-builder`'s `references/non-deterministic-stops.md` for the stop-condition theory.
