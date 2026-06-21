# Landscape Evaluation

Evaluated 2026-06-20 via 3 parallel web-research scouts + internal inventory + the [Forward Future Loop Library](https://signals.forwardfuture.ai/loop-library/). Verdicts use Pike's gate: **ADOPT** (use directly) / **ADAPT** (port into a SKILL.md) / **BORROW** (steal the methodology only) / **SKIP**. Licensing is judged **commercial-safe / fleet-wide** — MIT/Apache may be lifted; AGPL must be clean-roomed; Commons-Clause and NC are avoided entirely.

---

## A. External frameworks & toolkits

| Tool | What it gives | License | Verdict |
|------|--------------|---------|---------|
| **GitHub Spec Kit** ([repo](https://github.com/github/spec-kit)) | De-facto SDD standard (~114k★, 30+ agents). Loop: `constitution → specify → clarify → plan → tasks → analyze → implement`. `/clarify` asks ≤5 targeted Qs and encodes answers; `/analyze` is a read-only cross-artifact consistency check with severity ratings. Already community-ported into Claude skills. | **MIT** | **ADAPT** — the strongest single foundation; port the gated phase-loop |
| **BMAD-METHOD** ([repo](https://github.com/bmad-code-org/BMAD-METHOD)) | Role-decomposed planning (Analyst/PM/Architect → PRD + architecture), then a Scrum Master **shards docs into self-contained story files** carrying full context; adversarial red-team review gate. ~49k★. | **MIT** | **ADAPT** — software analog of the write-script pipeline; maps to the fleet's personas. Port methodology, skip the npx/IDE ceremony |
| **OpenSpec** ([repo](https://github.com/Fission-AI/OpenSpec)) | `propose → apply → archive` with **delta specs** (sections marked ADDED/MODIFIED/REMOVED vs a baseline) and archive-as-audit-trail. Great for brownfield concurrency. ~56k★. | **MIT** | **BORROW** — the delta-spec + archive pattern; don't adopt whole when Spec Kit is the better skeleton |
| **AWS Kiro** ([docs](https://kiro.dev/docs/specs/)) | Agentic IDE: requirements/design/tasks split; **EARS** notation (`WHEN [condition] THE SYSTEM SHALL [behavior]`); steering files. GA Nov 2025. | **Proprietary** | **BORROW** — EARS for testable, machine-parseable requirements + the tri-artifact split. Skip the IDE (wrong substrate, AWS lock-in) |
| **claude-task-master** ([repo](https://github.com/eyaltoledano/claude-task-master)) | `parse-prd → tasks.json → analyze-complexity → expand → next`. Task DAG + complexity scoring. ~28k★. | **MIT + Commons-Clause** ⚠️ | **BORROW** methodology only — Commons-Clause is **not** commercial-safe; redundant with Beads anyway. Lift the complexity-scoring *idea*, emit Beads issues |
| **Cline "Memory Bank"** ([docs](https://docs.cline.bot/features/memory-bank)) | 6-file markdown project-memory convention the agent reads each task. | Apache 2.0 | **SKIP** (redundant with `.servitor/` + CLAUDE.md); BORROW only if formalizing per-project memory |
| **Agent OS** ([repo](https://github.com/buildermethods/agent-os)) | v2 had `plan-product → create-spec → execute-tasks`; **v3 (2026) deliberately dropped orchestration** and defers to native Plan Mode. | MIT | **BORROW** v2's mission/roadmap/tech-stack templates; SKIP v3 (it deconverged toward what Claude Code already has) |
| **Tessl** ([blog](https://tessl.io/blog/)) | Pivoted from spec-as-source to a skills registry/eval layer on the open SKILL.md standard. | mixed | **SKIP** — nothing to adopt Lee doesn't already have; watch the build→evaluate→optimize lifecycle idea |
| **snarktank/ai-dev-tasks** ([repo](https://github.com/snarktank/ai-dev-tasks)) | 3 markdown files: `create-prd → generate-tasks → process-task-list` (one task at a time w/ human approval). ~8k★. | Apache 2.0 | **BORROW** — cleanest minimal PRD→tasks→one-at-a-time reference |

**Signal worth noting:** Agent OS v3 and buildermethods both pivoted *away* from heavyweight orchestration toward native plan mode in 2026 — lightweight composition beats ceremony. Our stack already has the native loop (Claude Code plan mode + subagents); we're adding the *artifact discipline* and *external-verified gates* on top, not a parallel orchestrator.

---

## B. Published Claude skills (the directly-portable layer)

| Skill | Coverage | License | Verdict |
|-------|----------|---------|---------|
| **DivikWu/product-requirement-craft** ([repo](https://github.com/DivikWu/product-requirement-craft)) | Problem Framing → SRD → PRD. Lean **129-line SKILL.md** w/ proper `references/`, traffic-light completeness gate, refuses to fabricate (marks TBD), retrospective loop. | **MIT** | **ADOPT/ADAPT** — closest to AISkills house standard; trim bilingual, install |
| **arun-mosai/claude-code-slice-skills** ([repo](https://github.com/arun-mosai/claude-code-slice-skills)) | Idea → 11 design docs, each with a **validator sub-agent** (pass/warn/fail); "nothing proceeds until the slice PASSes." | MIT | **BORROW** — validator-per-doc-type is the most Pike-aligned pattern (external review, not self-grading) |
| **GitHub Spec Kit templates** | ID-labeled `FR-###`, measurable `SC-###`, `[NEEDS CLARIFICATION]` flags, requirement→task traceability, the `/analyze` 5-pass rubric. | MIT | **BORROW→ADAPT** — best spec/plan/task templates in the field |
| **alirezarezvani/claude-skills** (`spec-driven-workflow`, `code-to-prd`) | RFC-2119 FRs, measurable NFRs, Given/When/Then ACs, contracts; hard gate "NO CODE WITHOUT AN APPROVED SPEC". | MIT | **ADAPT** — real depth; rebuild to Pike gate, don't vendor the 345-skill mega-repo |
| **snarktank/ralph** (`/prd`) ([repo](https://github.com/snarktank/ai-dev-tasks)) | Cleanest **clarify-then-generate** loop — 3-5 lettered multiple-choice Qs before generating; verifiable-AC rubric. | MIT | **BORROW** — lift the clarify-question gate + verifiable-AC rubric |
| **product-on-purpose/pm-skills** ([repo](https://github.com/product-on-purpose/pm-skills)) | 67 skills, Triple Diamond, `deliver-prd`, solution-brief, lean-canvas. Mostly one-shot. | **Apache 2.0** | **BORROW** — safest commercial license; mine PRD rubric + taxonomy |
| **cexll/myclaude** (`product-requirements`) | 100-pt weighted rubric (BizValue 30/Functional 25/UX 20/Tech 15/Scope 10), hard **≥90 gate**, clarifies on lowest dimension. | **AGPL-3.0** ⚠️ + Chinese-output | **BORROW (clean-room)** — re-implement the weighted-gate pattern; **fix its fatal flaw: the score is self-assessed** → route through a separate reviewer |
| **anthropics/skills** (official) | Document-format + dev tooling only. | — | **N/A** — ships **zero** planning/definition skills (confirmed gap) |

**Licensing landmines (fleet-wide = avoid):** `myclaude` (AGPL), `claude-task-master` (Commons-Clause), `deanpeters/Product-Manager-Skills` (CC BY-NC-SA — best PR-FAQ content but **non-commercial, do not reuse**). For these, take the *idea* via clean-room only.

---

## C. Loop-pattern catalog

### C.1 — The converged SDD loop (the spine)
```
constitution → specify → CLARIFY → plan → tasks → ANALYZE → implement → VERIFY
```
Human gate at each phase; revision = edit the upstream artifact; value concentrates in the three named gates. This is what every serious 2025-26 tool implements; we adopt it as the backbone.

### C.2 — Forward Future Loop Library (Lee-supplied; [source](https://signals.forwardfuture.ai/loop-library/))
The most useful contribution here is **explicit termination conditions** — the hard part of "in loops." The planning/refinement-relevant loops:

| Loop | Shape | **Termination condition** (the key bit) |
|------|-------|------------------------------------------|
| **prepare-a-new-project** | Review requirements/design/tasks/test-strategy → find largest gaps/contradictions → validate with independent reviewers | *"Stop when independent reviewers materially agree AND every artifact is testable"* — **convergence + testability** |
| **Goal Forge** | Interview → write `SPEC.md` (what to build/exclude) + `GOAL.md` (plan, scorecard, checks) → validate readiness | Approval gate before implementation |
| **multi-LLM convergence** | Model A reviews vs quality bar → fix → Model B reviews the *same* version | *"Succeed only when both approve the same unchanged version"* — **dual-model mutual approval** |
| **devil's-advocate** | Critic argues against the plan → builder fixes/documents → repeat | Until objections resolved or explicit stalemate; tracked in `redteam.md` |
| **self-improving champion** | Improve one element → test on fresh holdouts → promote only if beats baseline by margin | **Holdout-beating without weakening must-pass checks** |
| **Revolve versioned-experiment** | Freeze tests+scoring → checkpoint baseline → one hypothesis/round | **Keep only regression-free wins**; new revision if criteria change |
| **quality streak** | Test scenarios → on failure, add regression coverage + fix → restart | **Stop after N successful cases in a row** |
| **fresh-clone / easy-onboarding** | Clean environment → follow only the README/entry point → record gaps → fix → discard & retry | **Carry nothing between attempts** (validates "can someone pick this up cold") |
| **full product evaluation** | Realistic scenarios covering capabilities → success criteria → run → fix → rerun | Consistent pass/fail or rubric across runs |

**Why this matters for us:** the convergence/mutual-approval/streak/holdout conditions are exactly the *anti-self-grading* mechanisms Pike requires. `multi-LLM convergence` ≈ our Gemini+Codex peer-review gate; `devil's-advocate` ≈ BMAD adversarial review ≈ our `multiagent-review`; `prepare-a-new-project`'s "independent reviewers materially agree" is the right termination for a TRD loop.

### C.3 — Internal loop infrastructure already in the repo
- **write-script** — 4-phase pipeline (Architecture → Drafting → Multi-Model Review → Revision) with human approval gates. The proven prose analog of the SDD loop.
- **prose-polish-redline** — parallel-kata agents → shared JSON edit schema → tiered merge → tracked-changes/HTML replay. Reusable redline engine + edit schema + tier-priority conflict resolution.
- **prose-polish** — two-phase remediation (structure before style) + 6-dimension scoring + genre calibration.
- **multiagent-review** — fan-out to 5-8 parallel reviewers (Codex/Gemini/specialist Claude), duplicates preserved as confidence signal. **This is the external-verification gate.**
- **gemini-peer-review / codex-peer-review** — external-model second opinion (the dual-model convergence primitive).
- **pr-review-loop** — push → fetch comments → address each → mandatory one-more-loop before merge.
- **claimify** — extract claims → map relationships → find contradictions/gaps. The assumption-auditor for any artifact.

---

## D. Internal reuse inventory (what Lee already has)

**Reuse-ready in a PM pipeline:** prose-polish (quality gate on any doc), claimify (assumption/contradiction audit), process-mapper (discovery before requirements), presentation-partner (interview-first elicitation), concept-forge (dialectical pressure-test), research-to-essay / research-brief / deep-research (grounding), multiagent-review + gemini/codex peer review (the external gate), Beads (`bd`, dependency task DB), ralph-wiggum (execution engine, installed).

**Confirmed GAP:** no PM-spec *scaffolding* — nothing that drafts a proposal, PRD, or TRD. The pipeline currently ends at "requirements elicited" with no structured artifact generator.

---

## E. The two genuine build gaps (no good published skill)
1. **Amazon Working-Backwards PR-FAQ / 6-pager narrative** — the best content (deanpeters) is NC-licensed and unusable; everything else is thin. Clean net-new build warranted.
2. **First-class RFC / TRD design-doc with a quality loop** — only narrow ADR skills exist; no design-doc skill with alternatives/failure-modes/rollback rigor + an iterative gate.

Both fill the confirmed gap and would be genuinely higher-quality than anything published.
