# Eval Schema — machine-readable eval sets

SkillForge eval sets are written in the **official Agent Skills `evals.json` format** so they
interoperate with Anthropic's `skill-creator` tooling (executor, grader, `aggregate_benchmark.py`,
eval-viewer) vendored at `_vendor/skill-creator/`. **Canonical source of truth for all field
names: `_vendor/skill-creator/references/schemas.md`.** This doc is the SkillForge-facing summary
plus our two portable extensions.

Prose eval-set docs (`agent_docs/forge-runs/*/eval-set.md`) remain the human narrative; the
`evals.json` beside them is the machine-runnable form. Keep them in sync; the JSON is what the
harness reads.

## Two eval layers (don't conflate them)

| Layer | Question | Format | Tooling |
|-------|----------|--------|---------|
| **Trigger eval** | Does the *description* make Claude fire the skill? | `[{query, should_trigger}]` | `_vendor/.../scripts/run_eval.py` |
| **Behavioral eval** | Does *using* the skill produce better outputs than not? | `evals.json` (`{prompt, expectations[]}`) | executor+grader agents → `aggregate_benchmark.py` → `benchmark.json` |

Tier A of the gate cares about triggering + structure; **Tier B is the behavioral layer** — the real bar.

## `evals.json` (behavioral — the one SkillForge Tier B uses)

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's example task",
      "expected_output": "Human-readable description of success",
      "files": ["evals/files/sample.pdf"],
      "expectations": ["The output includes X", "The skill used script Y"]
    }
  ]
}
```

- `expectations[]` are **verifiable statements** the grader checks against the transcript — the
  behavioral analog of SkillForge's D1..Dn rubric dimensions. Keep each independently checkable.
- `files[]` are optional input paths relative to the skill root.

### SkillForge extensions (portable — runtimes ignore unknown keys)

- `_arm`: `"tuning"` | `"holdout"` — enforces holdout hygiene. The loop may iterate against
  `tuning` items every round; `holdout` items are scored **only at promotion** and kept out of
  iteration context. (Prevents the "memorization dressed as improvement" failure.)
- `_must_pass` (top-level array): non-negotiables that may never regress. A round that lifts the
  average but breaks a must-pass is a **REVERT**, not a promotion. Enforced by `scripts/bench_gate.py`.
- `_frozen`, `_behavioral_question`: provenance/intent, human-facing.

Worked example: `agent_docs/forge-runs/loop-builder/evals.json` (converted from its prose eval-set).

## `benchmark.json` (harness output)

Produced by the two-arm run + `aggregate_benchmark.py`; consumed by the eval-viewer and by our
`scripts/bench_gate.py`. Key shape (full schema in the vendored `schemas.md`):

```json
{
  "metadata": { "skill_name": "...", "evals_run": [1,2], "runs_per_configuration": 3 },
  "runs": [ { "eval_id": 1, "configuration": "with_skill", "run_number": 1,
              "result": {"pass_rate": 0.85, "time_seconds": 42.5, "tokens": 3800, "errors": 0},
              "expectations": [ {"text": "...", "passed": true, "evidence": "..."} ] } ],
  "run_summary": {
    "with_skill":    {"pass_rate": {"mean": 0.85, "stddev": 0.05}, ...},
    "without_skill": {"pass_rate": {"mean": 0.35, "stddev": 0.08}, ...},
    "delta": {"pass_rate": "+0.50", "time_seconds": "+13.0", "tokens": "+1700"}
  }
}
```

**Field names are load-bearing** — the viewer reads `configuration` (exactly `with_skill` /
`without_skill`) and `result.pass_rate` (nested). Generate via the vendored aggregator, don't
hand-roll. `bench_gate.py` turns this into a PROMOTE / HOLD / REVERT verdict against the noise band.
