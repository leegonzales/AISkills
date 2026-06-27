# Class-2 Forge — "Unenforced central promise" (test-first, 2026-06-27)

Per the B-test lesson (don't assume; measure), ran a real with/without two-arm test on 3 Class-2 skills BEFORE changing anything — to see whether the skill actually delivers its distinctive behavior or the base model already does it (or neither does, which would be the defect).

| Skill | Promise | Baseline (no skill) | Skill arm | Verdict |
|-------|---------|---------------------|-----------|---------|
| **mcp-builder** (SKILL-br3) | Evaluation-driven dev (Phase-4 eval harness) | Built a solid server but **omitted any evaluation phase** — stopped at MCP Inspector + "add tools once verified" | Ran **Phase 4**: wrote 10 read-only/verifiable questions, solved each, `scripts/evaluation.py` accuracy report, iterated on tool descriptions; `evaluation.xml` in deliverables; "workflows not endpoints" | **WORKS — clear lift.** Skill delivers the eval gate the base model skips. No fix needed. |
| **claude-project-docs** (SKILL-1b8) | Lean (~60 lines), no task-specific/style content, progressive disclosure | Produced ~90 lines **including code-style rules** (ruff/line-length/ESLint — the exact anti-pattern), no `agent_docs/` split | **~45 lines**, explicitly excluded style rules + versions per its anti-patterns, used `agent_docs/` progressive disclosure | **WORKS — clear lift.** Lean+specific vs generic bloat. No fix needed. |
| **concept-forge** (SKILL-p84) | Challenge, don't affirm; falsifiability | Already challenged well (Facebook-retired-motto, reversibility, offered a better framework) | Challenged + added **explicit falsifiability test** ("right now it can't be falsified") baseline omitted | **WORKS — modest lift.** Base model already challenges on a strong model; skill adds the falsifiability/structure increment. |

## Conclusion
**Class-2 skills produce real behavioral lift** — 2/3 do something the base model genuinely skips (eval phase; lean discipline), unlike the fabrication firewalls (Class-1) where the strong base already did the right thing. **All 3 tested deliver their promise when invoked and need no changes** — this is validation, not repair. The audit's "might skip eval / might bloat" hypotheses don't materialize *when the skill is applied*; preventing exactly those is the skill's job.

**Strategic implication:** the library's skills largely deliver when invoked. The residual risks are (a) skills being *ignored or diluted* (→ the bloat trims matter, esp. GeminiPeerReview's 1205 lines), and (b) the genuine defects (fixed in the merged forge work). Both are higher-leverage than blanket-firewalling more skills.

Caveat: single-task, self-evident outcomes I classified directly (the differences are unambiguous — eval-phase-present vs absent, 45 vs 90 lines); not a blind panel. Directional, consistent with the campaign's standard.
