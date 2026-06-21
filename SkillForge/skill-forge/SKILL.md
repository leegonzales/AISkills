---
name: skill-forge
description: Drive a skill toward optimal through measured, iterative refinement — not a one-pass rubric check but a behavioral eval-and-improve loop. Use when building a new skill, hardening an existing one, deciding if a skill is good enough to ship, or proving a change actually improved a skill. Runs a two-tier eval (structural gate + behavioral outcome lift on held-out tasks, externally scored) inside a champion-promotion loop with non-gameable stops. Triggers include "make this skill optimal", "is this skill good enough", "harden/tune this skill", "did my change improve the skill", "evaluate this skill properly", or "build a skill to 85/100 and beyond".
---

# Skill Forge

Take a skill from *passable* to *optimal* by measuring whether it actually makes an agent's outputs better, then refining against that measurement. A static rubric tells you if a skill is well-formed; Skill Forge tells you if it **works** — and improves it until it does.

## When to use

- Building a new skill and wanting it genuinely good, not just structurally valid.
- Hardening or tuning an existing skill.
- Deciding whether a skill is good enough to ship (or register).
- Proving a specific change to a skill actually improved it (vs. felt better).

If you only need a one-pass structural judgment, use `docs/skill-evaluation-rubric.md` directly — that's Tier A below. Skill Forge is for when you want the behavioral loop.

## What "optimal" means — two axes

A skill is optimal when **both** hold:

- **Structurally sound** — passes the 100-pt rubric ≥85, lean SKILL.md, progressive disclosure, validates. *Necessary, not sufficient: a skill can be beautifully structured and behaviorally useless.*
- **Behaviorally lifting** — on held-out real tasks, an agent **using** the skill reliably produces outputs that **beat the no-skill baseline** and clear the artifact quality bar. *This is the axis everyone skips, and the one that matters.*

## The eval — two tiers

**Tier A · Structural gate (fast, static).** The existing 6-category, 100-pt rubric (`docs/skill-evaluation-rubric.md`) + `validate-skill.sh`. A cheap pre-filter. Necessary, not sufficient.

**Tier B · Behavioral outcome eval (the real bar).**
1. Build a **frozen held-out task set** — 5-10 real tasks the skill should help with.
2. Run **two arms**: agent *with* the skill vs *without* (baseline).
3. Score the **outputs** (not the skill's self-report) with an **external reviewer panel** against the relevant artifact rubric.
4. The metric is **lift** — how much better, and how *reliably* (variance across the set), the skill arm beats baseline.

Full protocol, including how to build a non-leaky held-out set and run the panel: **[references/eval-protocol.md](references/eval-protocol.md)**.

## The refinement loop (the flywheel)

```
0. FREEZE the eval set + rubric + must-pass checks            (do once, up front)
1. BASELINE   — run skill on the frozen set, score externally
2. DIAGNOSE   — find the single weakest dimension / recurring failure
3. REVISE     — make ONE targeted change addressing it
4. RE-EVAL    — re-run on the frozen set + FRESH holdouts, score externally
5. PROMOTE?   — keep ONLY if it beats baseline by margin AND regresses no must-pass check (else revert)
6. ADVERSARIAL— red-team: try to make the skill fail / rationalize around it
   repeat 2-6 until a non-gameable stop fires
```

This is a non-deterministic loop, so it obeys `loop-builder`'s rules. **Termination (any one fires):**
- **self-improving champion** — beats baseline on *fresh* holdouts without weakening a must-pass check.
- **quality streak** — N consecutive held-out tasks clear the bar.
- **multi-LLM convergence** — two independent reviewers approve the same unchanged version.
- **diminishing returns** — last K rounds produced < threshold lift → ship.
- **budget ceiling** — hard cap on rounds; on cap, report the gap (never silent).

Full loop mechanics + worked example: **[references/refinement-loop.md](references/refinement-loop.md)**.

## Mandatory disciplines (inherited from loop-builder)

1. **External scoring, never self-grading.** The skill (or the agent that wrote it) does not grade its own outputs. Use a separate panel/model/human. Self-graded gates are gameable — this is the #1 thing that separates Skill Forge from a checklist.
2. **Held-out, fresh at promotion.** Defeats overfitting to the eval set. Keep the holdout out of the loop's context entirely.
3. **Keep-best, not keep-last.** Track the best version across rounds; revert regressions.
4. **One change per round.** So you know what caused the lift.
5. **Pre-commit the bar and the eval set in writing** before the loop runs.

## Workflow

1. **Scope.** Name the skill, its job, and the real tasks it should help with.
2. **Tier A gate.** Run `validate-skill.sh` + score against the rubric. Fix structural blockers first (cheap).
3. **Build the frozen eval.** 5-10 held-out tasks + the output rubric + must-pass checks. Pre-commit.
4. **Design the loop** with `loop-builder` (pick stop families, set the budget, wire the external panel).
5. **Run the flywheel** (steps 1-6 above) until a stop fires.
6. **Report the lift curve** — baseline → final, per-dimension, with the stop reason. Register only on a clean pass.

## Composes with
- **loop-builder** — designs this skill's own refinement loop and its stop conditions (Skill Forge *is* a loop-builder loop).
- **`docs/skill-evaluation-rubric.md`** — Tier A structural rubric.
- **multiagent-review** / **gemini-peer-review** / **codex-peer-review** — the external reviewer panel for Tier B (diverse, independent → real convergence, not sycophantic agreement).
- **writing-skills** — the adversarial / rationalization-resistance test (step 6).
- **prose-polish**, **claimify** — dimension scorers for written-artifact outputs.

## What good looks like
A forged skill ships with: a frozen eval set, a documented baseline-vs-final lift curve (per dimension), the externally-verified final score, the stop reason, and a passed adversarial round. If you can't show the lift, you have a validated skill — not an optimal one.
