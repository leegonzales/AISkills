# Changelog

All notable changes to the Skill Forge skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-06-30

### Added (benchmark harness + skill-creator interop — June field scan)
- **Machine-runnable eval sets:** `references/eval-schema.md` documents the official Agent Skills `evals.json` / `benchmark.json` schemas plus SkillForge's portable extensions (`_arm` tuning/holdout, top-level `_must_pass`). Worked example: `agent_docs/forge-runs/loop-builder/evals.json` (converted from the prose eval-set). `eval-protocol.md` now points authors at it.
- **`scripts/bench_gate.py`** — deterministic, offline promotion gate over `benchmark.json`: PROMOTE/HOLD/REVERT on lift-vs-noise-band, win-rate, must-pass regression, and regression-vs-prior-best. The piece the upstream tooling lacks (it stops at aggregation + viewer). CI-safe (exit 0 = promote). `scripts/test_bench_gate.py` covers all verdict paths (6/6 pass).
- **`scripts/README.md`** — the end-to-end pipeline: `evals.json` → vendored executor/grader → `aggregate_benchmark.py` → `bench_gate.py`. Verified end-to-end against the vendored aggregator.
- **`references/skill-creator-crosswalk.md`** — maps SkillForge concepts to Anthropic's `skill-creator` (vendored at `_vendor/skill-creator/`), delineating engine (theirs) vs. doctrine+gate (ours).

## [1.2.0] - 2026-06-21

### Added (adversarial hardening from skill-forge's own forge run)
- **Value-shape classification (workflow step 1):** declare how the skill's value shows up — (a) artifact-quality lift, (b) reliability/variance reduction, (c) gating/refusal/correctness, (d) routing/selection, (e) interaction/process — and design the eval per type. Fixes a CRITICAL hole: the default mean-lift artifact eval mis-measures safety/gate/variance skills and the loop would "improve" away a safety gate.
- **Baseline-contamination guidance (workflow step 3):** build eval tasks where the base model genuinely struggles; read near-zero lift correctly (skill-useless vs base-already-competent), don't assume 0 lift = worthless. (CRITICAL — empirically seen as strong baselines in both 2026-06-21 forge runs.)

### Fixed
- **Contradiction:** holdout was "sacred, only at promotion" (eval-protocol) but "re-eval every round" (SKILL.md). Reconciled: diagnose from tuning-set + adversarial findings only; touch fresh holdouts only at the promote check; holdout results never feed diagnosis.
- **Illusory stop:** `self-improving champion` was identical to the per-round promote gate. Now distinct: the stop requires a clear margin sustained across ≥2 separate fresh-holdout batches.
- **within-round vs keep-best collision:** promotion now re-scores `best` + candidate in the SAME panel pass (only within-pass deltas are trustworthy), with the margin required to exceed the noise band.
- **Worked example** no longer keeps a per-dimension regression on a net-positive average (the anti-pattern the skill warns against) — it reverts and re-revises narrowly.

### Known backlog (deferred MAJOR findings)
- No cost/length axis; blind panels are length-biased toward the skill arm.
- "External/holdout/bar" asserted not verified — no judge-correlation measurement, no leak/distribution-distance check on holdouts, no floor forcing the pre-committed bar above baseline.
- Selecting-on-noise: diagnosing the weakest of 6+ dimensions at n=5 chases noise (multiple-comparisons).
- No guidance for tool/state/environment-dependent skills; no explicit "skill is net-negative — don't ship at all" exit.

## [1.1.0] - 2026-06-21

### Added
- **Variance & noise handling (E6)** — eval-protocol.md §6 "Trust the signal before you trust the lift" + a 6th mandatory discipline in SKILL.md. Concrete rules: compare arms *within the same panel pass* (absolute scores drift between runs — the observed baseline swing was 3.36-4.00); report judge **spread** not just the mean; treat lift **smaller than the inter-judge spread as inconclusive**; prefer more tasks over more judges; with a 3-5 task eval, label the result directional not conclusive. Surfaced + confirmed by skill-forge dogfooding itself (E6 was the unanimous weakest dimension) and by the loop-builder forge run's eval-noise finding.

## [1.0.0] - 2026-06-20

### Added
- Initial release of the skill-forge skill.
- Two-axis definition of "optimal" (structurally sound + behaviorally lifting) and a 6-step workflow in SKILL.md.
- `references/eval-protocol.md` — Tier A structural gate + Tier B behavioral outcome eval; how to build a non-leaky held-out task set, run two arms, and score externally; eval failure modes.
- `references/refinement-loop.md` — the freeze→diagnose→revise→re-eval→promote→adversarial flywheel, five non-gameable stop conditions, and a worked example (forging a `prd` skill).
- Mandatory disciplines: external scoring (never self-grade), held-out-fresh-at-promotion, keep-best-not-last, one-change-per-round, pre-committed eval + bar.
- Composes with loop-builder (loop design), the skill-evaluation rubric (Tier A), and multiagent-review / peer-review (external panel).
