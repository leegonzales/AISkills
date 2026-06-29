# HIGH leftovers + substrate fixes (2026-06-29)

Closes the load-bearing tail of the forge campaign: the 2 remaining HIGH-tier skills and the 2 substrate (code, not prose) fixes. Done in an isolated worktree; code fixes were **run/verified by me**, not just self-reported.

## HIGH leftovers — fabrication/verification gates (prose)
| Skill | Bead | Gate |
|-------|------|------|
| **context-continuity** | SKILL-k6b | Fidelity Firewall: a continuity record contains only what actually happened / is in the real state; never invent decisions, progress, file changes, test results, or rationale; record gaps honestly ("not started"/"unknown"). Template guards added. |
| **context-continuity-code** | SKILL-d5g | Verification Gate: every code-state claim (branch, SHA, what changed, tests, build) must come from a command actually run this session; absent → run it or mark `[unverified]` with the confirm command; never recall/infer. |

Both self-tested PASS, validate clean. Same honest caveat as the other firewalls: insurance-grade (instruction-following lift not separately measured); the value is preventing a confident-but-false handoff that corrupts the next session.

## Substrate fixes — code, verified by running it
**excel-auditor `confidence:1.0` bug** (`scripts/extract_formulas.py`, `infer_purpose_detailed`):
- Defect: `confidence = winner_score / total` → pins to **1.0** whenever only one purpose category scored (a single weak signal), and was *inverted* (a rich multi-signal financial model scored only 0.8 < a thin guess's 1.0).
- Fix: `confidence = evidence_strength × corroboration × dominance`, clamped to **[0.1, 0.95]** — so a spurious 1.0 is now impossible *by construction*, and certainty requires multiple corroborating signals.
- **Verified by running the actual function myself** (not the agent's report): weak single-`id`-header → **0.100** (was 1.0); strong financial model (many signals) → **0.950**; schema unchanged (`purpose/confidence/reasoning/all_scores`); py_compile passes.

**flywheel-scan deprecated `TeamCreate`** (`SKILL.md`):
- Migrated all 7 `TeamCreate`/`TeamDelete`/`team_name` references to the current **Agent** tool pattern (parallel subagents via multiple Agent calls in one message; `SendMessage` for follow-up; dropped the team lifecycle). Orchestration intent preserved (parallel scouts → gather → doppelganger synthesis → reports).
- **Verified myself:** `grep` confirms zero `TeamCreate`/`TeamDelete`/`team_name` remain anywhere in the skill; validates clean.

## Campaign status after this
HIGH tier fully closed. Load-bearing work (fabrication-class HIGH + the 2 substrate fixes that compound into code) done. Remaining is the lower-yield MED staleness/routing tail + LOW controls + the cross-model conclusive-eval caveat (SKILL-t77).
