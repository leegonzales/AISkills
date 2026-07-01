# SOP — Biweekly Skills Field Scan

**Status:** Active
**Adopted:** 2026-06-30, by Lee's direct order (research session, Wake #306): *"lets do the scan every 2 weeks, and lets also update your operations based on these findings."*

## Why this exists

The Agent Skills field moves in quarters, not days — spec revisions, eval tooling, ecosystem/marketplace shifts, competitive skills. Our doctrine drifts silently against it (the June 2026 scan found "500 words" propagated through the whole template system, a stale `GEMINI.md` registry pointer, and — the other direction — that `SkillForge` had *parallel-invented* skill-creator 2.0's evals before we noticed). A guardian who never looks up ships a gate calibrated to last year's field. This SOP is the standing look-up.

The discipline it fights is the May bonsai lesson inverted: over-scanning is depletion (treading water in research-territory), so the cadence is deliberately *low frequency* and *positive-null-valid*. The scan earns its keep by changing real gate decisions, not by producing documents.

## Trigger

- **Cadence:** Every ~2 weeks (biweekly). Rotate the lens each cycle:
  1. **Spec** — SKILL.md frontmatter, structure, validation rules
  2. **Eval tooling** — skill-creator, benchmark/A-B methodology, judge frameworks
  3. **Ecosystem** — marketplace, plugins, distribution, portability standards
  4. **Competitive skills** — notable public skills worth adopting or learning from
- **Also fires when:** a platform change or a review surfaces a capability gap that can't wait for the next slot.

## Procedure

1. **Orient.** Re-read the current standards (`.servitor/soul.md` Standards, `agent_docs/quality.md`, `docs/skill-evaluation-rubric.md`, `agent_docs/creating-skills.md`) so the scan measures against something real. Read the prior scan memo.
2. **Scan.** Web-search the cycle's lens. Prefer primary sources (Anthropic docs/engineering/blog, the anthropics/skills repo, the agentskills.io spec). Pull 2-3 primary sources in full, not just search snippets.
3. **Reconcile.** For each finding, classify: (a) **we already have it** — record so future-me doesn't rebuild; (b) **safe cleanup** — factual/format drift I fix without asking; (c) **doctrine change** — evaluation criteria / thresholds / architecture, which route to Lee via the weekly soul-proposal DM.
4. **Verify on state.** Every claim about repo state gets grep/read confirmation before it's written (Wake #275 discipline — no confabulated findings, and no "fixing" false positives like the SlideBuilder `version:` code-block).
5. **Act on (b).** Make the safe corrections. Run `validate-skill.sh` against a known-good skill to confirm no regression.
6. **Emit.** Write a dated memo `agent_docs/skills-field-scan-YYYY-MM.md`: TL;DR, primary sources, where we already align, cleanup punch-list (fixed/open/not-a-problem), doctrine items for Lee. At most a short proposal list — never a doc dump.
7. **Log.** Journal the cycle. Route any (c) items into `soul-proposals.md` for the weekly DM.

## Success criteria

- The scan fires on cadence and produces a dated memo each cycle (or an honest positive-null).
- Findings are verified-on-state, not from memory.
- Safe cleanup lands; doctrine changes route through Lee, never self-applied.
- The gate stays calibrated to the current field, and what we already lead on is recorded, not rebuilt.

## Anti-patterns

- **Manufacturing findings** to justify the wake — positive-null ("nothing earned a change this cycle") is a valid, honest outcome.
- **Over-scanning** — biweekly is the ceiling, not a floor to beat. The field doesn't move fast enough to reward daily looking.
- **Doc-dumping** — a 2,000-word memo nobody acts on is consumption, not compounding. Lead with what changed and what to do.
- **Confident unverified claims** — assert repo state only after re-running the check on the artifact.
