# Crosswalk — SkillForge ⇄ skill-creator

SkillForge and Anthropic's `skill-creator` converged on the same idea from different directions:
a skill isn't good because it's well-formed, it's good because an agent *using* it produces
measurably better outputs. `skill-creator` (vendored at `_vendor/skill-creator/`) ships the
tooling; SkillForge supplies the discipline. This maps the two so you can move between them.

## Concept map

| SkillForge concept | skill-creator equivalent | Notes |
|--------------------|--------------------------|-------|
| Tier A — structural gate | `quick_validate.py` + our `validate-skill.sh` + rubric | Same role: cheap pre-filter, necessary-not-sufficient. |
| Tier B — behavioral outcome lift | Benchmark mode (`evals.json` → executor/grader → `benchmark.json`) | The real bar in both systems. |
| Frozen held-out set (`_arm: holdout`) | Eval set in `evals.json` | skill-creator has no formal holdout/tuning split — SkillForge adds `_arm`. |
| Two arms (skill vs baseline) | `with_skill` / `without_skill` configurations | Identical concept and field names. |
| External reviewer panel, blind | `agents/grader.md`, `agents/comparator.md` (blind A/B) | skill-creator's comparator is a single blind judge; SkillForge favors a diverse multi-model panel (`multiagent-review`, gemini+codex) to cut effective-n. |
| Lift ± noise band; "inside band = inconclusive" | *(absent)* — reports delta only | **SkillForge-only.** `bench_gate.py` enforces the noise floor. |
| Must-pass checks (regression = REVERT) | *(absent)* | **SkillForge-only.** `bench_gate.py` enforces; unmatched must-pass flagged for red-team. |
| Champion-promotion loop, non-gameable stops | `run_loop.py` + `history.json` (version progression) | Both track a current-best; SkillForge adds the multi-batch-sustained-win *stop* distinct from the per-round *gate*. |
| Adversarial red-team round | *(absent)* | **SkillForge-only** (refinement-loop step 6). |
| Description hardening | `run_eval.py` (trigger eval) + `improve_description.py` | Trigger layer — Tier A / discovery, not Tier B. |
| Packaging | `package_skill.py` | Parallel to our `SkillPackager`. |
| Results viewer | `eval-viewer/` + `assets/eval_review.html` | Reused as-is; our `benchmark.json` is viewer-compatible. |

## Who owns what

- **Use `skill-creator` for:** running the executor/grader arms, aggregating to `benchmark.json`,
  the eval-viewer, trigger evals, description improvement, packaging. It's the engine.
- **Use SkillForge for:** the eval *design* discipline (holdout hygiene, must-pass, diverse panel),
  the noise-band verdict (`bench_gate.py`), the refinement loop's non-gameable stops, and the
  adversarial round. It's the doctrine + the gate.

## Practical rule

Run `skill-creator` Benchmark mode to produce `benchmark.json`; run `bench_gate.py` to decide what
the numbers *mean*. Neither replaces the other — the engine without the gate promotes noise; the
gate without the engine has nothing to score.
