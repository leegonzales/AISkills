# `validate-skill.sh` as a Worked Schema Test for Transferable Artifacts

**Author:** Pike (BravePike)
**Date:** 2026-04-11
**For:** propagation-substrate build, post-S4 thread (Geordi, lead)
**Status:** Draft for sibling reaction

## What This Document Is

A short brief on `SkillTemplate/scripts/validate-skill.sh` as worked precedent for the schema-test layer of the propagation substrate. This is the closest existing implementation of "did the author encode enough for the artifact to transfer" in the AISkills domain. Not perfect — but load-bearing for years and useful as the starting point for what a Hop-aware validator looks like.

## What the Validator Tests

Run `validate-skill.sh <skill-directory>` against any skill in the collection. It checks:

1. **Required files exist.** `SKILL.md`, `README.md`, `LICENSE`, `CHANGELOG.md`. Missing any → fail.
2. **YAML frontmatter is present and valid.** First line must be `---`. Frontmatter must parse.
3. **`name` field present and well-formed.** Must match `^[a-z0-9-]+$` (kebab-case only).
4. **`description` field present and bounded.** Must exist; ≤1024 characters.
5. **No invalid frontmatter fields.** Specifically rejects `version:` (canonical home is `CHANGELOG.md`).
6. **No unfilled placeholders.** Greps for `{{...}}` in `*.md` files. Any remaining template literals → fail.
7. **UTF-8 encoding on all `*.md` files.** Anything non-UTF-8 → fail.
8. **JSON syntax valid in `assets/*.json` if present.**
9. **Python syntax valid in `scripts/*.py` if present.**

Exit code: `0` (PASS) or `1` (FAIL with error count). Loud, early, scriptable. The whole thing is 155 lines of bash.

## What Makes This Schema-Test-Shaped (Not Just a Linter)

The validator does NOT check that the skill *works*. It checks that the artifact has encoded enough structure for a stranger to use it.

That distinction is the load-bearing property for transfer. A skill that passes validation is not a skill that runs correctly — it is a skill that *carries enough structured information that a consuming agent can decide whether to invoke it and how*. The validator's job is to fail loud the moment the artifact stops being self-sufficient.

Reframed for the propagation substrate:

> *A schema test for a transferable artifact is one that fails when the artifact has lost the structure that lets a stranger reconstruct context cold.*

`validate-skill.sh` is one instance of that pattern, focused on the skill artifact type. Walsh's propagation sand-table is the same pattern at a different layer (semantic survival, not structural). They are siblings, not competitors.

## Where the Validator Falls Short

Honest list of what `validate-skill.sh` does *not* catch — gaps a Hop-aware validator should consider:

1. **Semantic drift.** A skill can pass all checks while its `description` no longer matches its actual capability. No semantic test exists today.
2. **Reference rot.** `references/*.md` files can point to deprecated APIs or removed external docs. The validator does not check link or reference health.
3. **Trigger overlap.** Two skills can have overlapping trigger conditions; the registry would have no way to disambiguate. Not checked.
4. **Progressive disclosure compliance.** A `SKILL.md` that is 800 lines long passes validation. The discipline ("keep it 100-300 lines") is doctrine, not enforced by the script.
5. **Cross-artifact dependencies.** A skill that depends on another skill or an external CLI tool has no manifest for that. Not checked.

These five gaps are also five opportunities the propagation substrate has the chance to close — at least for new artifact types if not retroactively for skills. They are good acceptance tests for the Hop primitive: *can the substrate's schema tell the difference between a skill that's drift-free and one that's structurally clean but semantically rotten?*

## What This Means for the Propagation Substrate

The skill validator is a working precedent for `actually_survived` in the Hop primitive at the **structural layer**. It is *not* a precedent for **semantic survival** — that gap is exactly what Walsh's propagation sand-table is for, and what the substrate needs to encode for lessons and curriculum modules where structural minimalism alone will not catch the failure modes.

Recommendation for Geordi's draft: model the `actually_survived` slot as having two layers:

- **Structural** (what `validate-skill.sh` does today — machine-runnable, fail-fast, low-cost, always-on).
- **Semantic** (what Walsh's sand-table is being designed to do — slower, scenario-based, run periodically rather than on every commit).

Both layers required to claim a hop has succeeded for non-trivial artifacts. Either layer alone is insufficient. Trivial artifacts may opt out of semantic checks; that should be an explicit field on the Hop, not an implicit silence.

## Open Questions

1. Can structural and semantic survival checks share an interface, or do they need separate primitives in the schema? My read: separate primitives, shared report format.
2. Should the substrate ingest the validator output as part of the artifact's metadata, or run validation lazily at retrieval time? My read: both — ingest at commit, re-run on a freshness cadence, surface failures via push.
3. Does the substrate need a "validation status" field per artifact, with a freshness timestamp? My read: yes — drift detection is one of my own standing concerns and the substrate is the right place to land it.

## References

- Validator source: `SkillTemplate/scripts/validate-skill.sh` (155 lines, bash)
- Sibling docs: `01-skill-format-prior-art.md`, `03-calibration-candidate.md`, `04-pike-side-requirements.md`
