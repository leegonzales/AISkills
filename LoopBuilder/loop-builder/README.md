# Loop Builder

A skill for designing and building **robust agent loops** — iterative workflows that drive toward a goal and *know when to stop*. It specializes in the hard case: loops **without deterministic stop conditions**, where "done" is a judgment ("good enough?", "found them all?", "do the reviewers agree?") rather than a checkable predicate.

## What it does

Given any iterative process you want an agent to run, Loop Builder helps you:

- Decide whether the stop is **deterministic** (write the predicate) or **non-deterministic** (build a trustworthy evaluator).
- Pick the right **stop-condition family** — judge-gate, convergence, mutual-approval, diminishing-returns, streak, saturation (loop-until-dry), holdout-generalization, human-checkpoint, or epistemic-stopping-point.
- Choose a proven **loop shape** from a catalog of 57 loops across 10 categories.
- Add the **mandatory guardrails** that keep loops safe: a hard budget under every soft stop, an external (not self-grading) evaluator, keep-best-not-last, and diverse-not-correlated judges.
- **Red-team** the design against 14 known failure modes (runaway, degradation, oscillation, self-declared-done, sycophantic convergence, Goodhart, overfitting, silent truncation, context rot, cost blowup, and more).

## When to use

- Building any repeated agent process: refine-until-good, search-until-found, review-until-approved, improve-until-converged, discover-until-dry, monitor-and-act.
- Choosing or comparing loop patterns.
- Diagnosing a loop that runs away, gets worse over time, oscillates, never finishes, or declares itself done falsely.

## The one idea to take away

> A loop is a **body** plus a **stop**. A deterministic stop is a predicate; if you can write it, write it. When you can't — because "done" is a judgment — you replace the predicate with an **evaluator**, make that evaluator *external* to the generator, and **always** pair it with a hard budget ceiling so a judgment that never fires still terminates.

## Structure

```
loop-builder/
  SKILL.md                              # source of truth: model, workflow, guardrails
  references/
    non-deterministic-stops.md          # the stop-condition taxonomy + design rules (the core)
    loop-failure-modes.md               # 14 failure modes, detection + defense (red-team checklist)
    loop-library.md                     # 57 cataloged loops by category, tagged by stop family
  README.md
  CHANGELOG.md
  LICENSE
```

## Installation

Copy `loop-builder/` into your Claude skills directory (or symlink it). The skill activates on triggers like "build a loop", "iterate until", "when should it stop", or "this loop won't terminate".

## Composes with

`multiagent-review`, `gemini-peer-review`, `codex-peer-review` (external/diverse evaluators for judge-gate and mutual-approval loops), `prose-polish` and `claimify` (quality scoring), the `ralph-wiggum` loop engine, and `Beads` (`bd`) for cross-session task state.

## License

MIT — see [LICENSE](LICENSE).
