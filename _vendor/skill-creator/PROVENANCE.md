# Provenance — skill-creator (vendored)

- **Source repo:** https://github.com/anthropics/skills
- **Source path:** `skills/skill-creator/`
- **Pinned commit:** `35414756ca55738e050562e272a6bbc6273aa926`
- **Commit date:** 2026-06-27
- **Vendored:** 2026-06-30 (Wake #306, by Pike, at Lee's direction)
- **License:** see `LICENSE.txt` in this directory (upstream MIT/Anthropic terms)

## What this is

Anthropic's official `skill-creator` skill, including its eval + benchmark tooling:

- `scripts/run_eval.py` — trigger eval (does the *description* fire the skill?)
- `scripts/run_loop.py` — the improve loop (version progression, `history.json`)
- `scripts/aggregate_benchmark.py` — aggregate per-run `grading.json` → `benchmark.json` (+ `.md`)
- `scripts/{quick_validate,package_skill,generate_report,improve_description,utils}.py`
- `agents/{analyzer,comparator,grader}.md` — executor/judge subagent prompts
- `eval-viewer/` + `assets/eval_review.html` — browser viewer for benchmark/eval output
- `references/schemas.md` — the canonical `evals.json` / `benchmark.json` / `grading.json` schemas

## Re-sync procedure

```bash
# from repo root
BASE="https://raw.githubusercontent.com/anthropics/skills/main"
# refresh the pinned commit first:
curl -sSL https://api.github.com/repos/anthropics/skills/commits/main | python3 -c "import json,sys;print(json.load(sys.stdin)['sha'])"
# then re-fetch each file under skills/skill-creator/ into _vendor/skill-creator/
# and spec/agent-skills-spec.md into _vendor/agent-skills-spec.md,
# and update the pinned commit above.
```

Integrity was verified at vendor time (fetched bytes identical to inspected copies; all
Python scripts compile with `python3 -m py_compile`). Do not edit these files locally —
they are a pinned mirror. Our extensions live in `SkillForge/skill-forge/scripts/`.
