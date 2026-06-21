# Frozen Eval Set — clean-room prose-polish forge + head-to-head

**Frozen 2026-06-21, before any build/round. Do not edit mid-run.**

## Goal
1. Use skill-forge (hardened v1.2 methodology) to build a **clean-room** prose-polish skill — built from first principles **without ever reading the existing `ProsePolish/` skill**.
2. Compare the two skills: **design/approach** + **behavioral output** on reference essays.

## Value shape (skill-forge v1.2 step 1)
Prose-polish = **(a) artifact-quality lift** — it makes a piece of writing better. The default two-arm mean-lift eval fits. (Not a gate/variance/routing/process skill.)

## Output rubric — score a polished essay 0-4 (per dimension)
| Dim | Dimension | Strong (4) |
|-----|-----------|-----------|
| P1 | **Clarity** | Every sentence is unambiguous; no vagueness or filler ("in today's world", "a lot of things"). |
| P2 | **Concision** | No padding; word count earns its keep; hedges cut unless load-bearing. |
| P3 | **Structure & flow** | Ideas ordered logically; transitions earned; a real arc, not a list. |
| P4 | **Authority / specificity** | Concrete claims, examples, specifics replace generic assertion. |
| P5 | **Voice & register** | Distinct, genre-appropriate voice; not flattened into generic-AI tone. |
| P6 | **Fidelity** | Preserves the author's actual meaning/intent — improves, doesn't replace or fabricate content. |

**Overall** = mean of P1-P6. **Win** = strictly higher overall.

## Must-pass (regression = REVERT / disqualify)
- **MP1 (fidelity):** never invents facts/claims the author didn't make, never changes the author's position. A "better" essay that says something the author didn't is a fail.
- **MP2 (genre-fit):** never homogenizes — a reflective narrative must not be rewritten into a corporate blog, etc.

## Essays (inputs = "before" drafts, in essays/)
- **E1 — opinion/blog** (`essay1-opinion-draft.md`): hedge-heavy, generic, weak structure. **Tuning.**
- **E2 — technical explainer** (`essay2-technical-draft.md`): dense, passive, jargon-bloated. **Tuning.**
- **E3 — personal narrative** (`essay3-narrative-draft.md`): meandering, telling-not-showing. **HOLDOUT** (scored only at promotion + final head-to-head).

## Arms
- **Baseline:** capable agent told "polish this essay," no skill.
- **Clean-room:** same agent + the clean-room prose-polish skill.
- **Existing:** same agent + the existing `ProsePolish/prose-polish` skill. *(Final head-to-head only.)*
All same model/framing. Panel scores blind to arm + authorship; substance not vocabulary.

## Clean-room rule (hard)
The builder + skill-arm agents MUST NOT read `ProsePolish/`. The clean-room skill is an independent implementation. Only the orchestrator (me) sees both, at the final comparison.

## Stops (budget-bounded)
- Budget: 2 refinement rounds on the clean-room skill.
- Early stop: holdout win + clean must-pass, OR diminishing returns (< +0.3).

## Deliverables
1. Clean-room prose-polish skill (in `clean-room-skill/`).
2. **Skill-vs-skill design comparison** (existing vs clean-room) — external panel.
3. **Output head-to-head** on E1/E2/E3: baseline vs existing vs clean-room, scored blind.
4. Report.
