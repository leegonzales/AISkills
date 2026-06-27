# Skill-Forge Campaign — Record

**Window:** 2026-06-21 → 2026-06-27 · **Driver:** Pike (BravePike @ AISkills)
**Goal:** Test-and-improve the whole skill library (52 skills) using the forge methodology, the way the ProsePolish hardening was done.
**Library health at close:** **52/52 validate clean** · `main` @ `27151ed`

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
