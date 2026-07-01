# SkillForge scripts — the benchmark harness

SkillForge's Tier B (behavioral outcome lift) runs on the **vendored `skill-creator` tooling**
(`_vendor/skill-creator/`) plus one SkillForge-native gate. We don't reinvent the executor/grader
— we reuse them and add the promotion discipline on top.

## The pipeline

```
evals.json  ──►  executor+grader (agent-orchestrated)  ──►  aggregate_benchmark.py  ──►  bench_gate.py
(this repo)      _vendor/skill-creator/agents/*.md          _vendor/.../scripts/         SkillForge (here)
                 run each eval task twice: with_skill        per-run grading.json         PROMOTE / HOLD /
                 vs without_skill; grade expectations        → benchmark.json (+ .md)      REVERT verdict
```

1. **Author `evals.json`** in the official format — see `../references/eval-schema.md`. Include the
   `_arm` tuning/holdout split and top-level `_must_pass`.
2. **Run the two arms + grade.** Drive the vendored `skill-creator` executor/grader agents (see its
   `SKILL.md` Benchmark mode) to run each eval `with_skill` and `without_skill` and write a
   `grading.json` per run into the `eval-N/<config>/run-M/` layout.
3. **Aggregate:** `python3 _vendor/skill-creator/scripts/aggregate_benchmark.py <benchmark_dir> --skill-name <name>`
   → produces `benchmark.json` (+ `benchmark.md`). Open it in `_vendor/skill-creator/eval-viewer/`.
4. **Gate:** `python3 bench_gate.py <benchmark_dir>/benchmark.json --evals path/to/evals.json`
   → PROMOTE / HOLD / REVERT with lift-vs-noise-band, win-rate, and must-pass enforcement.

## bench_gate.py — the piece upstream doesn't have

Upstream stops at aggregation + a viewer. `bench_gate.py` turns `benchmark.json` into a
**non-gameable verdict**, encoding SkillForge's stop discipline (deterministic, offline, CI-safe):

- **PROMOTE** — lift clears `max(noise_band, --min-margin)` **and** win-rate ≥ `--min-win-rate`.
- **HOLD** — lift within the noise band (inconclusive: "you measured nothing"), or win-rate too low.
- **REVERT** — a must-pass expectation regressed, or the candidate dropped vs a `--baseline` best.

```bash
python3 bench_gate.py candidate.json --baseline best.json --evals evals.json --history history.json
```

Exit code 0 on PROMOTE, 1 otherwise — drop it into CI. Must-pass statements that match no
expectation are surfaced as "confirm by red-team", never silently passed.

## Tests

`python3 test_bench_gate.py` — offline assertions over all verdict paths (no model calls).

## Note on the vendored trigger eval

`_vendor/skill-creator/scripts/run_eval.py` is a *trigger* eval (does the description fire the
skill?) — a separate, cheaper layer that belongs to Tier A / description tuning, not Tier B lift.
Use it when hardening a skill's `description`; use this pipeline when proving behavioral lift.
