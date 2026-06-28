# Changelog

All notable changes to the `fleet-pr-review` skill are documented here.

## [0.1.0] — 2026-06-28

Initial release. Extracted from a one-off poster used to attribute fleet
persona reviews on a real PR, then built TDD-style (baseline RED → skill GREEN →
refactor) per the `writing-skills` discipline.

### Added
- `SKILL.md` — orchestration workflow: surface → fan-out → merge → post.
- `references/reviewer-prompt.md` — persona-subagent prompt template enforcing
  the no-`gh`, return-text-only constraint and the JSON comment contract.
- `scripts/post_fleet_comments.py` — hardened poster:
  - resolves PR head SHA as `commit_id` automatically;
  - validates each RIGHT-side anchor against the actual diff hunks (SKIPs
    invalid lines with a hint instead of mis-posting);
  - prefixes `**[Agent]**` attribution (GitHub author is the orchestrator token);
  - posts each comment independently with per-comment OK/FAIL/SKIP reporting;
  - pipes a JSON object to `gh api --input -` to avoid `-F/-f` integer-typing
    fragility on the `line` field;
  - `--dry-run` validates and previews payloads without posting.

### Known gaps (hardening backlog)
- Merged-PR comment behavior documented but not specially handled.
- Mixed-diff RIGHT-side line numbering for personas relies on the validator as
  safety net rather than a generated numbered diff.
- LEFT-side anchor validation is best-effort.
- Persona roster resolution is delegated to the `agent` skill, not re-tested here.
