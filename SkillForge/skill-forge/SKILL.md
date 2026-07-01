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
4. RE-EVAL    — re-run on the frozen TUNING set, score externally (holdouts touched only at step 5)
5. PROMOTE?   — on a fresh holdout, re-score `best` + candidate in the SAME pass; keep ONLY if it beats `best` by a margin exceeding the noise band AND regresses no must-pass (else revert). Holdout results do NOT feed diagnosis.
6. ADVERSARIAL— red-team: try to make the skill fail / rationalize around it
   repeat 2-6 until a non-gameable stop fires
```

This is a non-deterministic loop, so it obeys `loop-builder`'s rules. **Termination (any one fires):**
- **self-improving champion** — *(distinct from the per-round promote gate)* the skill beats baseline by a **clear margin sustained across ≥2 *separate* fresh-holdout batches**, not just one promoting round. (A single promotion is the gate; a repeated, multi-batch win is the *stop*.)
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
6. **Trust the signal before the lift.** LLM-judge scores are noisy (±0.5-1.0 is common). Compare arms **within the same panel pass** (absolute scores drift between runs — never compare a candidate to a separately-scored baseline); report judge **spread**, not just the mean; treat any lift **smaller than the inter-judge spread as inconclusive**, not a win; and prefer more *tasks* over more *judges* for reliability. With a small eval (3-5 tasks), say the result is directional, not conclusive. See [references/eval-protocol.md](references/eval-protocol.md) §6.

## Workflow

1. **Scope + classify the skill's VALUE SHAPE.** Name the skill, its job, and the real tasks — then declare **how its value shows up**, because that determines the whole eval design. The default Tier-B model (better artifact, same task, mean-lift, artifact-quality panel) only fits one shape. Pick:
   - **(a) Artifact-quality lift** (writes a better PRD/commit/doc) → the default two-arm mean-lift eval below.
   - **(b) Reliability / variance reduction** (improves the *worst case*, prevents the bad output) → **tail-weighted** eval; score worst-case and failure-rate, NOT the mean (a small happy-path set will show ~0 lift and falsely fail it).
   - **(c) Gating / refusal / correctness** (refuses to fabricate, escalates, says TBD) → **trigger-conditional** eval: tasks that *should* fire the behavior; score "did it correctly gate," and **warn the panel that the correct output may be shorter/absent** — an artifact-quality panel will otherwise penalize the right answer.
   - **(d) Routing / selection** (picks the right downstream action) → score the *decision*, not a prose artifact.
   - **(e) Interaction / process** (elicitation, brainstorming) → score the *trajectory / changed state* over turns, not one output.
   Getting this wrong is the cardinal error: the default eval will tell you a working safety skill is worthless, and the loop will "improve" it by deleting the gate. (Surfaced in skill-forge's own forge run, 2026-06-21.)
2. **Tier A gate.** Run `validate-skill.sh` + score against the rubric. Fix structural blockers first (cheap).
3. **Build the frozen eval — on tasks where the base model genuinely struggles.** 5-10 held-out tasks + the output rubric + must-pass checks, pre-committed. **Beware baseline contamination:** a capable base model already does much of what a good skill prescribes, so on easy/happy-path tasks the no-skill baseline scores high and lift compresses to ~0 — making a genuinely good skill look worthless. Deliberately build tasks where the baseline *fails or wobbles* (the skill's reason to exist). And read **near-zero lift correctly**: it means *either* the skill adds nothing *or* the base model is already competent and the skill's value is reliability under harder/shifted inputs — distinguish these by checking the baseline's absolute quality and testing harder tasks, never by assuming "0 lift = useless."
4. **Design the loop** with `loop-builder` (pick stop families, set the budget, wire the external panel).
5. **Run the flywheel** (steps 1-6 above) until a stop fires.
6. **Report the lift curve** — baseline → final, per-dimension, with the stop reason. Register only on a clean pass.

## Composes with
- **loop-builder** — designs this skill's own refinement loop and its stop conditions (Skill Forge *is* a loop-builder loop).
- **`docs/skill-evaluation-rubric.md`** — Tier A structural rubric.
- **The benchmark harness** — write eval sets in the official `evals.json` format ([references/eval-schema.md](references/eval-schema.md)); run the two arms + aggregate with the vendored engine (`_vendor/skill-creator/`), then gate the result with `scripts/bench_gate.py` (PROMOTE/HOLD/REVERT on lift-vs-noise + must-pass). Pipeline: [scripts/README.md](scripts/README.md). Engine↔doctrine map: [references/skill-creator-crosswalk.md](references/skill-creator-crosswalk.md).
- **multiagent-review** / **gemini-peer-review** / **codex-peer-review** — the external reviewer panel for Tier B (diverse, independent → real convergence, not sycophantic agreement).
- **writing-skills** — the adversarial / rationalization-resistance test (step 6).
- **prose-polish**, **claimify** — dimension scorers for written-artifact outputs.

## What good looks like
A forged skill ships with: a frozen eval set, a documented baseline-vs-final lift curve (per dimension), the externally-verified final score, the stop reason, and a passed adversarial round. If you can't show the lift, you have a validated skill — not an optimal one.
