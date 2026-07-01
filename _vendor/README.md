# `_vendor/` — Upstream reference copies

Third-party code vendored **read-only for reference and interop**. Nothing here is an
AISkills-authored skill: these files are **excluded from the SKILLS.md registry and the
skill count**, and are not held to our 85/100 gate (they're upstream artifacts, evaluated
on their own terms).

## Contents

| Path | Source | Why it's here |
|------|--------|---------------|
| `skill-creator/` | `anthropics/skills` → `skills/skill-creator` | Anthropic's official skill-authoring + eval/benchmark tooling. Companion to our `SkillForge/skill-forge` (which parallel-invented the behavioral-eval loop). We adopt its `evals.json` / `benchmark.json` schemas for interop and reuse its executor/grader/aggregator + eval-viewer. |
| `agent-skills-spec.md` | `anthropics/skills` → `spec/agent-skills-spec.md` | Upstream's **pointer stub** — the canonical spec now lives at <https://agentskills.io/specification> (a living doc, not vendored). The concrete, load-bearing schema we actually run against is `skill-creator/references/schemas.md`. |

See `skill-creator/PROVENANCE.md` for the pinned source commit and re-sync instructions,
and `SkillForge/skill-forge/references/skill-creator-crosswalk.md` for how the two systems map.

**Do not edit vendored files.** Fixes go upstream; local needs are met by wrappers in
`SkillForge/skill-forge/scripts/`.
