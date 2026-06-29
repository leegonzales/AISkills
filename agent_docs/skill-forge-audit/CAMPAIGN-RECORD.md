# Skill-Forge Campaign — Record

**Window:** 2026-06-21 → 2026-06-29 · **Driver:** Pike (BravePike @ AISkills)
**Goal:** Test-and-improve the whole skill library (52 skills) using the forge methodology, the way the ProsePolish hardening was done.
**Library health:** **52/52 validate clean** · latest `main` after the bloat-trim sweep (PRs #56/#57/#59 merged).

---

## 1. What was built first (the instruments)

The campaign needed measuring tools before it could improve anything. Both were built from scratch and then forged through themselves (dogfooded):

| Instrument | What it does | Shipped |
|---|---|---|
| **loop-builder** v1.3 | Design agent loops with sound stop conditions (esp. non-deterministic): 10-family stop taxonomy, 14 failure modes, 57-loop library | PR #45 |
| **skill-forge** v1.2 | Drive a skill toward optimal: value-shape taxonomy (a–e), two-tier eval (structural ≥85 + behavioral 2-arm), refinement loop, baseline-contamination guidance | PR #46 |

**ProsePolish proof-of-concept** — the pattern that seeded the whole campaign: a clean-room rebuild (PR #47) *beat* the curated skill on fidelity (3.83 vs 2.95), exposing that ProsePolish **fabricated citations/numbers on low-source input**. The fix — a **Fidelity Firewall** (no edit may introduce a citation/stat/number/date/name/quote/fact absent from the source; honest fallbacks = sharpen-from-source / `comment`-for-author / soften-claim) — shipped as ProsePolish v1.2.0 (PR #48).

---

## 2. The audit

A 52-skill audit (`audit-2026-06.md`) tiered every skill and found the dominant defect was **one family**: *confabulation on thin evidence* — fabricating the specifics a skill is asked to produce when the grounding isn't actually present. ~15 skills shared it. Epic: **SKILL-zam**, label `forge-campaign`.

---

## 3. What shipped (all merged to `main`)

| PR | Scope | Skills |
|---|---|---|
| #49 | **Bug-sweep** — 12 confirmed concrete bugs | build-timeline, claimify validator-wire, dead paths, `reference/`→`references/`, model de-pinning, symlink, etc. |
| #50 | **Redline** Fidelity Firewall | prose-polish-redline (fixed the `insert`-citation schema example that taught fabrication) |
| #51 | **HIGH Cluster A** — Fidelity Firewall ×8 | claimify, research-to-essay, writing-partner, unix-review, excel-auditor, essay-to-speech, silicon-doppelganger, opportunity-scanner |
| #52 | **HIGH Cluster B** — degraded-mode gate ×3 | gemini-peer-review, aws-cdk-development, aws-cost-operations |
| #54 | **HIGH Cluster C** — security ×2 | git-secure (verification gate), moltbook-enclave (honest-control + real red-team) |
| #53 | **Infra sweep** | validator 2 bugs fixed + 17 LICENSEs + CLAUDE.md path → library 52/52 |

**The one rule, four costumes** (applied only to the fabrication-class cluster, not all 52):
- **Fidelity firewall** — assert no citation/number/quote without a source the user gave.
- **Degraded-mode gate** — a fact from a tool you didn't run isn't yours to assert; tool absent → "unavailable", never confabulate.
- **Verification gate** (git-secure) — don't claim "secure" without checking.
- **Honest-control** (moltbook) — don't claim a safety property the artifact lacks.

---

## 4. The two empirical findings (the part that matters)

Per Lee's challenge — *"are you testing these, or just applying rules?"* — two real **with/without, two-arm** behavioral tests were run on `main` versions:

### B — fabrication firewalls (Class-1): **correct + safe, but low measured lift**
5 skills × {baseline, hardened}, fabrication-bait tasks. **4 of 5 baselines were already clean** — Opus refuses obvious bait without the skill. Only **silicon-doppelganger** showed a clear behavioral win (baseline invented a labeled persona; hardened refused + gap-marked). This is the **baseline-contamination / near-zero-lift** case skill-forge documents. The firewalls' real value is the cases where fabrication *actually* occurred (prose-polish, redline, moltbook's 8/10 sanitizer bypass, excel-auditor's `confidence:1.0` bug) + cheap insurance against model/prompt drift. **Not big quality lift on a strong base.**

### Class-2 — unenforced central promise: **real measured lift**
3 skills × {baseline, hardened}, does-the-skill-do-its-job tasks:
- **mcp-builder** — baseline omitted any evaluation; skill ran the **Phase-4 eval harness**. Clear win.
- **claude-project-docs** — baseline ~90 lines *with* style-rule anti-patterns; skill ~45 lines + progressive disclosure. Clear win.
- **concept-forge** — baseline already challenges; skill adds explicit falsifiability. Modest.
- **All 3 work as-is → validation, not repair.**

**Meta-conclusion:** when a skill is *invoked*, it largely delivers. The library is in better shape than the audit's worst case implied. The highest-leverage *remaining* levers are **bloat trims** (so skills aren't ignored/diluted — GeminiPeerReview is 1,205 lines) and **substrate/code fixes** (excel `confidence` math, flywheel `TeamCreate` migration) — **not** more firewalls.

Full test logs: `forge-runs/high-tier/` (clusterA/B/C, classB-unenforced-promise). All verdicts **directional** (shared-base-model panels, small evals); conclusive cross-model runs tracked in **SKILL-t77**.

---

## 5. Bead status at close

**Epic SKILL-zam · 19 closed / 26 open.**
- **Closed:** redline + 8 Cluster A + 3 Cluster B + 2 Cluster C + infra-hygiene (SKILL-j0z) + 3 Class-2 validated (mcp-builder, claude-project-docs, concept-forge).
- **Open HIGH (2):** context-continuity (SKILL-k6b), context-continuity-code (SKILL-d5g) — fabrication gate not yet done (bug-sweep only fixed their paths).
- **Open MED (~23):** mostly hygiene/staleness/**bloat**/routing.
- **Open LOW (1):** SKILL-dji (6-skill control spot-check).

## 6. Recommended next moves (in leverage order)
1. **Bloat trims** — GeminiPeerReview 1,205→~300, codex-peer-review 741, aws-serverless-eda 747. Testable: does trimming preserve behavior while improving instruction-following?
2. **Substrate fixes** — excel-auditor `confidence` math; flywheel-scan `TeamCreate`→`Agent` migration.
3. **Finish 2 HIGH leftovers** (context-continuity pair).
4. MED staleness/routing; LOW controls.

**Standing caveat (preserve):** forge results are directional, not conclusive — shared-base-model panels and small evals. Cross-model conclusive runs are SKILL-t77.

---

## 7. Bloat-trim sweep (2026-06-27 → 06-29)

Acted on recommendation #1. Trimmed the 7 longest skills via progressive disclosure — keep skill-specific + load-bearing inline (rules/firewalls, exact commands/flags, routing, workflow skeleton), move/delete base-redundant + already-duplicated content to `references/`.

| Skill | Lines | PR |
|-------|-------|----|
| gemini-peer-review | 1205→251 | #56 |
| aws-serverless-eda | 747→63 | #57 |
| codex-peer-review | 741→149 | #57 |
| nano-banana | 698→221 | #57 |
| ffmpeg | 569→327 | #59 |
| build-timeline | 476→326 | #59 |
| second-brain | 427→115 | #59 |

All merged to `main`, all validate clean, all behavior-preserved. Beads closed: SKILL-tq4/amh/yn4/ckl (+ the Class-2-validated trio earlier). Logs: `agent_docs/forge-runs/bloat-trims/`.

**What the eval established (honest):**
- **Token economy + behavior-preservation: proven.** ~3,400 lines of always-loaded SKILL.md context removed across 7 skills with no behavior lost.
- **Instruction-following *lift*: not demonstrated** — the gemini pilot's moved content was base-model-redundant; the critical rules were already top-placed. Same null as the fabrication firewalls.
- **Progressive disclosure genuinely fires** for skill-specific moved content — conclusively shown for nano (brand hexes), build-timeline (card HTML/CSS), second-brain (`daemons.yml` keys), codex (synthesis templates), ffmpeg (`palettegen` filtergraph): trimmed agents reproduced ref-only unguessable tokens via verified ref reads.

**Two methodology lessons (now standard):**
1. **The eval must run against frozen, commit-extracted paths in an isolated worktree — never a mutable shared tree.** The first batch-2 eval was *compromised* by a concurrent-agent branch switch mid-run (reported a confident ~88% off uncontrolled inputs; caught only when Lee asked "are you making this up?"). Re-run in frozen worktrees with hand-grep verification of ref-only tokens → trustworthy.
2. **Eyeball every trim before applying — the validator misses real defects.** Batch-3 caught a stray `</content>` tag (second-brain) and a dangling-pointer risk (ffmpeg's new `references/` dir failed to copy) that `validate-skill.sh` passed.

**Two-agents-one-working-dir collision** recurred (stranded commits twice, compromised one eval). Worktree-per-agent is the fix; worth making default if concurrent agents run in this repo regularly.

### Still open after the sweep
- ~~2 HIGH leftovers~~ and ~~the 2 substrate fixes~~ — **done, see §8.**
- Smaller bloat (diminishing returns): fabric-patterns (417), slide-builder (321); prose-polish/opportunity-scanner are firewall-hardened — trim carefully or leave.
- MED staleness/routing tail; LOW controls (SKILL-dji).

---

## 8. HIGH leftovers + substrate fixes — closed (2026-06-29, PR #60)

The load-bearing tail. Code fixes were **run/grepped by me**, not trusted from agent self-report.

| Fix | Bead | Verified |
|-----|------|----------|
| **context-continuity** Fidelity Firewall (record only observed state) | SKILL-k6b | self-test + validate (prose, insurance-grade) |
| **context-continuity-code** Verification Gate (code-state only from commands run) | SKILL-d5g | self-test + validate (prose) |
| **excel-auditor** `confidence:1.0` bug → recalibrated, clamped `[0.1,0.95]` | (Cluster A skill) | **ran the function: weak single-signal 1.0→0.100, strong →0.950, schema intact** |
| **flywheel-scan** deprecated `TeamCreate`→`Agent` tool pattern | SKILL-2yd | **grep-confirmed zero `TeamCreate`/`TeamDelete`/`team_name` remain** |

**HIGH tier fully closed.** Campaign at 26 closed / 19 open. The substrate fixes are the campaign's strongest-evidence work — measured by running code, not panel opinion. Remaining (19 beads) is the lower-yield MED staleness/routing tail + LOW controls + the standing **SKILL-t77** cross-model caveat (every forge verdict is still single-model/directional). Natural stopping line for the load-bearing work. Log: `agent_docs/forge-runs/high-tier/high-leftovers-and-substrate.md`.
