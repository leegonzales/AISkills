# Bloat-Trim Batch 2 — dynamic workflow (2026-06-27)

Ran the validated pilot recipe across the next 3 longest skills via a `bloat-trim-batch` workflow:
pipeline of **trim → eval** per skill, eval by a SEPARATE agent (cross-agent discipline), trim done on
a `/tmp` copy (no repo edits → no conflicts); only passing trims applied afterward.

| Skill | Lines | Verdict | Refs genuinely read? | Changed |
|-------|-------|---------|----------------------|---------|
| aws-serverless-eda | 747->63 (91%) | preserved / ship | yes (webhook 29s timeout + 202 constants) | SKILL.md + serverless-patterns.md |
| codex-peer-review | 741->149 (80%) | preserved / ship | yes (synthesis templates + transparency phrasing) | SKILL.md |
| nano-banana | 698->221 (68%) | preserved / ship | yes (Catalyst brand hexes — not base-guessable) | SKILL.md |

## What's better than the pilot
In the GeminiPeerReview pilot the moved content was base-model-redundant (the ref was never strictly
needed). Here the eval agents verified the moved content is **genuinely skill-specific** — webhook
constants, synthesis scaffolding, exact brand hexes that can't be guessed — so progressive disclosure is
doing **real** work: the trimmed skill must open the ref to match the bloated behavior, and the named
pointers reliably trigger that read. Before/after equivalent (or better — refs were sometimes supersets).

## Honesty notes
- The eval caught one small overstatement in the nano-banana trim (claimed an "uncanny valley" pitfall
  lived in prompting-guide.md; it doesn't — but the operative mitigation is retained inline, so no loss).
- aws-serverless-eda at 63 lines was eyeballed: not a stub — keeps the 5 MCP servers, all 7 design
  principles WITH guidance, operational cues (batchItemFailures/DLQ/X-Ray), and explicit routing.
- Eval arms self-classified by the (separate) eval agent; single-run; directional.

**Validated recipe holds.** Same caveat: token economy + behavior-preservation proven; instruction-following
lift not separately measured. The genuine win is context economy with intact recall via strong named pointers.
