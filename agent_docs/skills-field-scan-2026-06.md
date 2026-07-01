# Skills Field Scan — June 2026

**Author:** Pike (BravePike) · **Date:** 2026-06-30 · **Type:** Research memo / doctrine-reconcile input

> **Follow-on (same day): eval system adopted.** Beyond the doctrine reconcile below, Lee directed
> full adoption of the skill-creator eval system. Done: **(a)** official `evals.json`/`benchmark.json`
> schema adopted (`SkillForge/skill-forge/references/eval-schema.md`; loop-builder eval-set converted
> to `evals.json`); **(b)** upstream `skill-creator` vendored read-only at `_vendor/skill-creator/`
> (pinned commit `35414756`, integrity-verified) + `_vendor/agent-skills-spec.md`; **(c)** thin
> benchmark harness `SkillForge/skill-forge/scripts/bench_gate.py` — the PROMOTE/HOLD/REVERT gate
> upstream lacks (6/6 tests, verified end-to-end against the vendored aggregator) + crosswalk doc.
> The honest correction that triggered this: my first-pass report adopted the *methodology* but not
> the *tooling*; Lee caught it. Now both are in.

A scan of current (mid-2026) thinking on Agent Skills, measured against our own methods and the AISkills repo. Purpose: find what's genuinely new and worth incorporating into the quality gate, and separate **safe cleanup** (act without asking) from **doctrine changes** (route through the weekly soul-proposal / Lee's call).

---

## TL;DR

1. **The field formalized while we were heads-down.** Agent Skills now has a published frontmatter spec (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`) and an official authoring best-practices guide with concrete, testable rules. Several of our internal docs predate it and have drifted.
2. **The single biggest external development: skill-creator 2.0 ships a real eval framework** — skill-vs-no-skill A/B, blind LLM-judge against assertions, benchmark mode (pass rate / tokens / time). This is the thing we lacked at the front door.
3. **We already half-built it.** `SkillForge/skill-forge` independently implements the same idea (Tier A structural gate + Tier B behavioral outcome lift on a frozen held-out set, externally scored, in a champion-promotion loop with non-gameable stops). Our thinking was directionally right. The work is **reconciliation**, not invention.
4. **Real internal drift exists and some is already fixed this session.** See Cleanup Punch-List.

---

## What the field says now (primary sources)

- **Anthropic, "Skill authoring best practices"** (platform.claude.com/docs/.../agent-skills/best-practices)
- **Anthropic engineering, "Equipping agents for the real world with Agent Skills"**
- **Anthropic/Claude blog, "Improving skill-creator: test, measure, and refine Agent Skills"**
- **Community spec, agentskills.io / anthropics/skills** (portability standard)

### Frontmatter spec (the portable standard)
- **Required:** `name` (≤64 chars, lowercase/numbers/hyphens, no XML tags, no reserved words `anthropic`/`claude`), `description` (non-empty, ≤1024 chars, no XML tags, **third person**, says *what it does + when to use it*).
- **Optional standard:** `license`, `compatibility` (env requirements), `metadata` (arbitrary k-v — **this is where `version`, `owner`, `reviewed_at` now legitimately live**), `allowed-tools` (space-delimited pre-approved tools; experimental; **security-relevant**).
- **Portability rule:** spec-compliant runtimes ignore unrecognized keys. Everything beyond the standard is a Claude Code extension.

### Authoring rules worth adopting (concrete, testable)
- **SKILL.md body < 500 lines** (not words). Split at the limit.
- **Progressive disclosure, references one level deep** from SKILL.md (Claude partial-reads nested refs → incomplete info). ToC at top of any reference file > 100 lines.
- **Degrees of freedom:** match specificity to task fragility — high freedom (prose) for open fields, low freedom (exact scripts, "do not modify") for narrow bridges.
- **Descriptions in third person**, specific, key-term-rich — it's injected into the system prompt and drives selection among 100+ skills.
- **Gerund naming** preferred (`processing-pdfs`), avoid `helper`/`utils`/`tools`.
- **No time-sensitive info** in body; use a collapsed "old patterns" section.
- **Code:** "solve, don't punt" (handle errors in scripts, don't kick to Claude); no voodoo constants; make **execute-vs-read-as-reference** intent explicit; prefer pre-made utility scripts; "plan → validate → execute" with verifiable intermediate outputs for batch/destructive ops.
- **MCP tools:** always fully-qualified `Server:tool_name`.
- **Test across all target models** (Haiku/Sonnet/Opus): what Opus infers, Haiku needs spelled out.

### Evaluation methodology (the new front door)
- **Build evals BEFORE writing extensive docs.** Baseline-first: run Claude on representative tasks *without* the skill, document the specific gaps, write minimal instructions to close them, iterate against the eval.
- **Eval object:** `{skills, query, files, expected_behavior[]}` — test prompt + success assertions.
- **skill-creator 2.0:** writes evals for you, runs **skill vs. no-skill** (and version-vs-version) under a **blind comparator agent**, **benchmark mode** tracks pass rate / token usage / elapsed time, parallel sub-agents in isolated contexts. Rerun after every model update to catch regressions and to detect when the base model has *superseded* the skill.
- **Claude A / Claude B loop:** one Claude authors the skill, a fresh Claude uses it on real tasks, observed gaps feed back. Watch real navigation (unexpected read order, missed references, ignored files).

---

## Where we already align (don't rebuild)

| Our asset | Status vs. field |
|---|---|
| `SkillForge/skill-forge` | **Ahead of curve.** Tier A structural gate + Tier B behavioral lift on frozen held-out set, external reviewer panel, champion-promotion with non-gameable stops, multi-LLM convergence. Parallel-invented skill-creator 2.0's evals. |
| `validate-skill.sh` | Already enforces: frontmatter present, `name` format, `description` ≤1024, **rejects top-level `version:`**, UTF-8, JSON/Python syntax. Aligned with spec. |
| 85/100 rubric + kaelib quarantine + (a)/(b) audit + developmental verdicts | Sound and more sophisticated than anything public. Keep. |
| Progressive disclosure via `references/` | Already doctrine. |

**The honest read:** our gate is strong on *structure/docs* and our SkillForge is strong on *behavioral lift* — but the two aren't wired together, and the front-door creation docs don't point authors at SkillForge or at eval-first development.

---

## Cleanup Punch-List (internal drift)

**Fixed this session:**
- ✅ `agent_docs/creating-skills.md` — registry step said `GEMINI.md`; corrected to `SKILLS.md`.
- ✅ `SkillTemplate/skill-template/SKILL.md.template` — "under 500 **words**" → "under 500 **lines**" (the propagating source of the words/lines error).

**Verified NOT a problem (recorded so future-me doesn't "fix" it):**
- `SlideBuilder/slide-builder/SKILL.md:110` `version: 5` is inside a *Talk Track* frontmatter code block (example data), not the skill's own frontmatter. Clean.

**Open — safe corrections (factual/format; act without asking):**
- "500 words" still appears in `SkillTemplate/CUSTOMIZATION_GUIDE.md`, `INTEGRATION_RUNBOOK.md`, `HOW_TO_USE_TEMPLATE.md`, `README.md`. Same words→lines correction. (Per-skill CHANGELOG mentions are historical — leave.)
- `docs/SKILL-8-SPEC.md` is a historical planning doc carrying `version: 1.0.0` in frontmatter and the old "Settings > Capabilities" upload flow. Mark as archived/superseded rather than rewrite.
- `agent_docs/quality.md` says SKILL.md < **400** lines; official ceiling is 500. 400 is a defensible local raise — keep, but note it's intentional, not the spec number.

**Open — validator upgrades (changes gate behavior → propose, don't silently ship):**
- Add checks to `validate-skill.sh`: `name` ≤64 chars; reserved-word rejection (`anthropic`/`claude`); **500-line body ceiling** (warn); optional-field whitelist awareness so `license`/`metadata`/`allowed-tools`/`compatibility` are recognized, not flagged. Add as **warnings** first to avoid newly-failing existing skills.

---

## Doctrine changes to route through Lee (not mine to set)

1. **Rubric: add a behavioral-lift dimension.** Today "Testing (5 pts)" = "documented validation results." The field (and our own SkillForge) treats **skill-vs-no-skill behavioral lift** as the real bar. Proposal: make Tier-B lift evidence the spine of Production-Readiness, or add an explicit dimension. Reallocating points = changing evaluation criteria = command call.
2. **Wire SkillForge in as the official Tier-B companion to the 85/100 gate** — gate = Tier A; SkillForge = Tier B; "ready for the fleet" means both. Cross-repo architecture decision.
3. **Adopt eval-first creation** in `creating-skills.md` — instruct authors to baseline-without-skill and write the `{query, expected_behavior[]}` eval before docs. (Mostly doc work; flagging because it changes the prescribed workflow.)
4. **Frontmatter doctrine update:** "never version" → "no *top-level* `version`; version belongs under `metadata:`"; add `allowed-tools` to the security-config review surface (it's literally pre-approved tool execution — Pike's lane).

---

## Cadence proposal (per Lee, 2026-06-30)

If this proves fruitful, fold a field scan into wakes on a **staggered, low-frequency** schedule — the field moves in quarters, not days, and over-scanning is depletion (cf. the May "stop iterating, start cultivating" bonsai lesson). Recommended: **one focused field-scan wake ~every 4-6 weeks**, rotating the lens (spec changes → eval tooling → ecosystem/marketplace → competitive skills). Each produces a dated memo like this one and, at most, a short proposal list — never a doc dump. Positive-null ("nothing earned a change this cycle") is a valid, honest outcome.

---

*Read the swell before consulting the chart. The field finally drew a chart that matches the swell we'd been reading — and in one place (SkillForge) we'd already charted ahead of it. — Pike*
