# Skill Forge

A meta-skill that drives a skill toward **optimal** through measured, iterative refinement — not a one-pass rubric check, but a behavioral eval-and-improve loop. A static rubric tells you a skill is *well-formed*; Skill Forge tells you it *works*, and improves it until it does.

## The core idea

> Optimal has two axes: **structurally sound** (passes the rubric, lean, validates) and **behaviorally lifting** (on held-out real tasks, an agent *using* the skill beats the no-skill baseline, reliably). Most skill QA only checks the first. Skill Forge measures the second and refines against it.

## What it does

1. **Tier A — structural gate:** `validate-skill.sh` + the 100-pt rubric (≥85). Cheap pre-filter.
2. **Tier B — behavioral eval:** run the skill vs a no-skill baseline on a frozen, held-out task set; score the *outputs* with an **external** reviewer panel; measure **lift** (magnitude, reliability, win-rate).
3. **Refinement loop:** diagnose the weakest dimension → make one targeted change → re-eval on fresh holdouts → promote only if it beats baseline without regressing a must-pass → adversarial red-team → repeat until a non-gameable stop fires.
4. **Report the lift curve:** baseline → final, per dimension, with the stop reason.

## When to use

- Building a new skill and wanting it genuinely good, not just valid.
- Hardening or tuning an existing skill.
- Deciding if a skill is good enough to ship/register.
- Proving a specific change actually improved a skill (vs. felt better).

## The disciplines that make it real (not a checklist)

- **External scoring, never self-grading** — the agent that made the output doesn't grade it.
- **Held-out, fresh at promotion** — defeats overfitting.
- **Keep-best, not keep-last** — skills can degrade across rounds.
- **One change per round** — attributable lift.
- **Pre-commit the eval + bar in writing** — a movable target measures nothing.

## Structure

```
skill-forge/
  SKILL.md                       # source of truth: two-tier eval, refinement loop, disciplines, workflow
  references/
    eval-protocol.md             # how to measure a skill (Tier A + Tier B, building the eval set)
    refinement-loop.md           # the flywheel + stop conditions + a worked example
  README.md
  CHANGELOG.md
  LICENSE
```

## Composes with

- **loop-builder** — Skill Forge *is* a non-deterministic loop; loop-builder designs its loop and stop conditions.
- **`docs/skill-evaluation-rubric.md`** — the Tier A structural rubric.
- **multiagent-review**, **gemini-peer-review**, **codex-peer-review** — the external, diverse reviewer panel for Tier B.
- **writing-skills** — the adversarial / rationalization-resistance test.
- **prose-polish**, **claimify** — dimension scorers for written outputs.

## License

MIT — see [LICENSE](LICENSE).
