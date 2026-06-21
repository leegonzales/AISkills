# Build Plan

How to assemble the evaluated pieces ([01](01-landscape-evaluation.md)) into a working "define software projects in loops" capability that enforces the quality bars ([02](02-artifact-quality-bars.md)). Fleet-wide / commercial-safe.

---

## Architecture — a layered stack, not one skill

```
┌─ PLAN LAYER ───────────────────────────────────────────────────────────┐
│ spec-driven-planning skill                                              │
│   port GitHub Spec Kit loop (constitution→specify→clarify→plan→tasks    │
│   →analyze) + BMAD doc-sharding into self-contained work units          │
├─ ARTIFACT LAYER ───────────────────────────────────────────────────────┤
│ pr-faq  →  prd  →  trd   (3 skills sharing a base rubric + traceability)│
│   each: clarify-gate → draft → external-verified score → revise → gate  │
├─ GATE LAYER ───────────────────────────────────────────────────────────┤
│ artifact-review  — externally-verified rubric scoring                   │
│   reuses multiagent-review + gemini/codex peer review; NEVER self-grades │
├─ ENGINE LAYER ─────────────────────────────────────────────────────────┤
│ ralph-wiggum loop (installed)  — autonomous execution downstream        │
├─ TASK DB ──────────────────────────────────────────────────────────────┤
│ Beads (bd)  — dependency graph, ready/blocked, cross-session            │
└────────────────────────────────────────────────────────────────────────┘
```

**Design principles (from the evaluation):**
1. **Compose, don't reinvent** — port MIT methodology (Spec Kit, BMAD, DivikWu, arun-mosai), wrap existing engines (ralph, Beads), reuse internal skills (prose-polish, claimify, multiagent-review).
2. **The gate is external, never self-graded** — every score routes through a separate reviewer pass (the `multi-LLM convergence` loop / multiagent-review). This is the #1 differentiator over published skills.
3. **Traceability is the backbone** — stable IDs + the PRD-metric→TRD-observability coverage check ([02 §4](02-artifact-quality-bars.md#4-the-cross-artifact-traceability-chain-the-backbone)).
4. **Right-size verbosity** — the universal real-world complaint about SDD tools is artifact bloat. Tier output to project size; a one-pager mode and a full mode.

---

## Loop design (with explicit termination conditions)

Borrowing the [Forward Future](https://signals.forwardfuture.ai/loop-library/) termination conditions — the part most skills get wrong:

| Layer / skill | Loop pattern | **Stop condition** |
|---------------|--------------|--------------------|
| Each artifact skill | clarify-then-generate (snarktank/ralph) → draft → score → revise | Rubric score ≥ bar **AND** all `[NEEDS CLARIFICATION]` resolved |
| Artifact gate | **multi-LLM convergence** (Gemini + Codex) | *Both approve the same unchanged version* |
| TRD / new-project | **prepare-a-new-project** (independent reviewers) | *Reviewers materially agree AND every artifact is testable* |
| Architecture decisions | **devil's-advocate** red-team (BMAD adversarial) | Objections resolved or explicit accepted-stalemate, logged in `redteam.md` |
| Cross-artifact check | traceability coverage scan | Zero orphan requirements; every PRD metric has a TRD observability entry |
| Skill self-improvement | **self-improving champion** | New version beats baseline on held-out example docs without weakening must-pass checks |

---

## Licensing guardrails (fleet-wide = strictest)

| Action | Sources |
|--------|---------|
| **Lift directly** (MIT/Apache) | Spec Kit, BMAD, OpenSpec, DivikWu, arun-mosai, alirezarezvani, snarktank, pm-skills, Cline |
| **Clean-room only** (idea, not code — AGPL) | myclaude weighted-gate pattern |
| **Avoid entirely** (not commercial-safe) | claude-task-master (Commons-Clause), deanpeters Product-Manager-Skills (CC BY-NC-SA), Kiro (proprietary — borrow EARS *notation*, which is unencumbered) |

Every new skill ships **MIT** (AISkills collection default) so it's reusable across personal / Catalyst / fleet.

---

## Sequenced build phases

**Phase 0 — Foundations (shared primitives).** Build the base rubric module ([02 §5](02-artifact-quality-bars.md#5-shared-quality-dna-meta-rubric--common-base-layer)) + the traceability/stable-ID convention + the `artifact-review` gate skill (wraps multiagent-review for external scoring). Everything else depends on these.

**Phase 1 — Pilot vertical slice (one chain end-to-end).** `pr-faq` → `prd` → `trd` on ONE real example, with the gate + traceability check wired. Validates the loop before scaling. *(This is the "pilot" option from the proceed question — recommended whenever build starts.)*

**Phase 2 — The plan layer.** `spec-driven-planning` skill: port Spec Kit's gated phase-loop + BMAD sharding; emit Beads issues; hand work units to ralph.

**Phase 3 — Adapt the high-value published skills.** Port DivikWu (PRD lean gate), arun-mosai validator-subagent pattern (TRD design-doc validators); fold in EARS + delta-spec borrows.

**Phase 4 — Harden & self-improve.** Run the self-improving-champion loop on held-out example docs; right-size verbosity; register all in SKILLS.md; pass the 85/100 gate.

Each phase is independently shippable. Phase 1 is the fastest path to something usable.

---

## The two net-new gap builds (no good published source)
1. **`pr-faq`** — Amazon Working-Backwards. Clean build ([02 §1](02-artifact-quality-bars.md#1-amazon-prfaq--6-pager-narrative) rubric); the best existing content (deanpeters) is NC-licensed and unusable, so this is genuinely net-new value.
2. **`trd`** — first-class RFC/TRD design-doc with the alternatives/failure-modes/rollback hard-floors + EARS + the observability-coverage gate. Only narrow ADR skills exist published.

---

## Internal-skill reuse map (compound, don't consume)

| Need | Reuse (don't rebuild) |
|------|----------------------|
| Discovery / elicitation interview | `process-mapper`, `presentation-partner` |
| Research grounding | `research-brief`, `deep-research`, `research-to-essay` |
| Assumption / contradiction audit | `claimify` |
| Writing quality pass | `prose-polish`, `prose-polish-redline` (edit schema, tiered merge, tracked-changes) |
| Dialectical pressure-test | `concept-forge` |
| External-verified gate | `multiagent-review`, `gemini-peer-review`, `codex-peer-review` |
| Execution engine | `ralph-wiggum` (installed) |
| Task dependency DB | Beads (`bd`) |
| Pipeline pattern to mirror | `write-script` (4-phase: Architecture→Drafting→Multi-Model Review→Revision) |

The artifact skills are the **missing scaffolding** between "requirements elicited" and "work executed" — everything around them already exists.

---

## Success criteria (Pike's gate on the suite)
- Every artifact skill: passes `validate-skill.sh`, ≥85/100, lean SKILL.md with `references/` progressive disclosure, MIT.
- The gate never self-grades — scores come from a separate reviewer pass.
- The traceability chain is machine-checked (stable IDs; PRD-metric→TRD-observability coverage = 100% or flagged).
- A pilot run produces a PR-FAQ→PRD→TRD chain where an independent reviewer agrees the TRD is testable and traces cleanly to the proposal.
- Loops have explicit, non-gameable termination conditions (convergence / mutual-approval / streak / holdout), not "looks done."
