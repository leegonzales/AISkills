# Artifact Quality Bars

The scoreable rubrics each artifact skill must enforce. These become the gate rubrics in the build (03). All grounded in primary sources (cited).

**Lineage note:** Amazon's canonical artifacts are the **~1-page PR/FAQ** and the **6-page narrative memo** — there is **no canonical "5-pager."** Bezos's 2004 ban-PowerPoint memo said "4-page"; teams converged on 6 (fits a ~20-min silent read). "5-pager" = an org-local relaxation of the 6-pager. Keep PR/FAQ and the narrative as distinct artifacts that share principles (narrative prose, customer obsession, silent reading).

---

## 1. Amazon PR/FAQ + 6-pager narrative

**PR/FAQ skeleton:** Headline · Subheadline (who + benefit) · Summary para · Problem (customer's voice, concrete) · Solution (experience-level, name the differentiator) · Leader quote · Customer quote · Call to action · **FAQ** (External: price/how/availability/vs-alternatives; Internal: exact customer segment, TAM, unit economics/P&L, hardest problems, dependencies, feasibility, **top 3 reasons this fails**, adoption/behavior-change, success criteria).

**6-pager skeleton:** Purpose/intro · Goals (few, measurable) · **Tenets** (ordered guiding principles; "how we decide," +UYKBO) · Current state (data) · Proposed approach (reasoned backward from customer) · FAQ · Risks & dependencies · Appendix (data — *outside* the 6-page limit). Body ≤6pp, ~3 min/page.

**Rubric (score 1-5 each):** Customer specificity (one precise segment, not "everyone") · Working-backwards integrity (starts from end-state experience, not the tech) · "So what?" / differentiation · **Narrative quality — no bullet-smuggling** · Clarity & concision (page limit as forcing function) · Evidence & intellectual honesty (assumptions labeled as assumptions; no "robust/seamless/world-class") · Metrics (few, measurable, baselined) · Economics & feasibility (TAM, unit economics) · **FAQ candor (names the thing most likely to kill it)** · Tenets quality (6-pager) · Appendix discipline.

**Gate question:** *Could a stranger read this in silence and understand it with no author present? Does the PR make a reader want the product? Does the FAQ name what kills it?*

**Top failure modes:** bullet-smuggling · "everyone" customer · weasel words · assumptions as facts · vague/too-many goals · ignoring competition · soft FAQ that dodges · good prose hiding a bad idea · page-count cheating.

**Sources:** *Working Backwards* (Bryar & Carr 2021) · [workingbackwards.com PR/FAQ](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/) · [Colin Bryar on Coda](https://coda.io/@colin-bryar/working-backwards-how-write-an-amazon-pr-faq) · [AWS Startups — narrative](https://aws.amazon.com/blogs/startups/startup-advice-how-to-write-a-narrative/) · [Commoncog](https://commoncog.com/working-backwards/) · [CNBC — 6-page memos](https://www.cnbc.com/2018/04/23/what-jeff-bezos-learned-from-requiring-6-page-memos-at-amazon.html).

---

## 2. PRD (Product Requirements Document)

**Framing:** Modern PRD is a lean, living alignment tool capturing the *why* and *what*, deliberately leaving *how* to design/eng. Right-size: 1-pager/brief (should-we-invest) vs full PRD (cross-functional execution).

**Skeleton:** Title & metadata (DRI, reviewers, status, version, change history) · **Problem statement** (who hurts, why now, evidence — the load-bearing section) · Goals & objectives (ladder to strategy) · **Success metrics** (specific, measurable, time-bound; primary + guardrails; how instrumented) · Target users/personas · Requirements/user stories (functional + non-functional, each with **acceptance criteria**) · **Scope & NON-GOALS** (excluded AND why) · UX (links not embeds) · Dependencies · Assumptions · Constraints · Risks & mitigations · Open questions (with owners) · Timeline/rollout · Analytics/instrumentation.

**Rubric (★ = weight heavily):** ★Problem clarity (why-before-what) · ★Measurable time-bound metrics (baseline+direction+deadline) · ★Explicit non-goals · ★Traceability (every requirement → a goal; every metric → an objective) · ★Testability (acceptance criteria, objectively checkable) · Prioritization (P0/P1/P2) · Avoids premature solutioning · Non-functional coverage (perf/security/scale/a11y) · Personas grounded in evidence · Single source of truth/freshness · Conciseness · Collaboration (co-reviewed, not a defensive contract).

**Top failure modes:** vanity/unmeasurable metrics · no non-goals/open scope · solution masquerading as problem · untestable requirements · no personas · orphan requirements (no traceability) · premature solutioning · no prioritization · stale/forked doc · missing NFRs.

**AI-era caveat:** the *10-page exhaustive spec* is dead; the *PRD* is not. Reward the strategic core (problem/metrics/non-goals/risks); do **not** penalize absence of exhaustive implementation detail (now a prototype + acceptance criteria). NFRs remain a written responsibility.

**Sources:** [Cagan/SVPG — Revisiting the Product Spec](https://www.svpg.com/revisiting-the-product-spec/) · [Lenny — PRDs & 1-pagers](https://www.lennysnewsletter.com/p/prds-1-pagers-examples) · [Atlassian](https://www.atlassian.com/agile/product-management/requirements) · [Aha! PRD best practices](https://www.aha.io/roadmapping/guide/requirements-management/what-is-a-prd-(product-requirements-document)) · [Aakash Gupta — Are PRDs Dead?](https://www.aakashg.com/are-prds-dead/).

---

## 3. TRD / design doc (and RFC / ADR)

**Framing:** TRD/TDD/EDD all live in the "design doc" category. RFC = circulated for feedback *before* a decision; Design Doc = the engineering design once approved; ADR = short record of *one* decision + consequences. Same DNA: state the problem, state the decision, justify against alternatives, record consequences.

**Skeleton:** Title & metadata (authors, named reviewers/approvers, status DRAFT/ACCEPTED/IMPLEMENTED/OBSOLETE, links to PRD/tickets) · Context/background (neutral facts, why now) · **Goals & NON-GOALS** (3-5 sentences) · Proposed design/architecture (context diagram, data flow) · Data model & schema · APIs/interfaces (shape + backward compat) · **★Alternatives + tradeoffs (≥2 real, incl. "do nothing"; explicit why-chosen)** · Cross-cutting: security/privacy · scalability/perf · reliability · **observability (logs/metrics/traces/alerts)** · Testing strategy · **Rollout/migration + ROLLBACK path** · Backwards compat · Cost · **Risks & failure modes (blast radius, detection, mitigation)** · Open questions · Ownership · Appendix. Length: "as short as possible, as long as necessary."

**Rubric (★ = double-weight; HARD-FLOOR fail on Alternatives, Failure modes, or Rollback):** ★Alternatives & tradeoffs · ★Goals & non-goals · ★Reviewer-friendliness / disagree-ability (a competent dissenter can pinpoint *where* to disagree) · ★Failure modes & risk · ★Testability · ★Security & privacy · ★Observability (tied to failure modes + SLOs) · ★Migration/rollback (reversible) · Right altitude (strategy + key decisions, not a code dump) · Architecture concreteness · Decisions justified not asserted · Metadata/status hygiene. Score 0-3 each, double-weight ★, **fail any doc scoring 0 on a hard-floor dimension regardless of total.**

**Requirements notation:** use **EARS** (borrowed from Kiro) — `WHEN [trigger] THE SYSTEM SHALL [behavior]` — for testable, machine-parseable requirements.

**Top failure modes:** no/strawmanned alternatives (most common, most damaging) · no non-goals · hand-wavy architecture · ignores failure modes · no rollback · security as afterthought · no observability · wrong altitude · decisions asserted not justified · not reviewer-friendly · stale/oversized.

**Cultural test (rubric preamble):** design docs exist to *change behavior and timing*, not produce paper — surface disagreement early when change is cheap. The highest-order test: *could a competent reviewer who disagrees pinpoint exactly where and why, and could a maintainer in two years reconstruct the reasoning?*

**Sources:** [Design Docs at Google — Malte Ubl](https://www.industrialempathy.com/posts/design-docs-at-google/) · [ADRs — Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) · [ADR — Martin Fowler](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) · [Scaling via RFCs — Gergely Orosz](https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/) · [EARS — Alistair Mavin](https://alistairmavin.com/ears/).

---

## 4. The cross-artifact traceability chain (the backbone)

This is what makes the suite a *pipeline*, not three disconnected generators. Each downstream artifact is checkable *against* the upstream one.

```
CUSTOMER/PROBLEM →  PR-FAQ problem+customer →  PRD problem statement+personas →  TRD context
GOALS           →  PR-FAQ goals →  PRD goals/objectives →  TRD goals   (refinement, never contradiction)
SUCCESS METRICS →  PR-FAQ success criteria →  PRD measurable KPIs →  TRD observability  ★critical check
NON-GOALS/SCOPE →  PR-FAQ "what's out" →  PRD non-goals →  TRD non-goals   (scope narrows MONOTONICALLY)
RISKS           →  PR-FAQ "top 3 reasons it fails" →  PRD risks →  TRD failure modes
ECONOMICS       →  PR-FAQ unit economics/TAM →  PRD constraints/appetite →  TRD cost
```

**Mechanics for the AI loop:**
1. **Stable IDs** — give each goal/metric/requirement/non-goal a stable ID (G1, M1, R1, NG1) at the PRD stage; reference them in the TRD → machine-checkable traceability.
2. **Monotonic scope** — scope narrows or holds across stages; silent expansion is a flag.
3. **Decisions flow down, not up** — flag when a later doc re-opens a decision its upstream settled without an explicit "revising upstream decision X because…" note.
4. **Coverage checks the loop runs:**
   - Every PRD requirement → addressed by a TRD design element? (no orphans)
   - **★ Every PRD success-metric → has a TRD observability/instrumentation entry?** *(the single highest-value automated gate — if the PRD says "increase activation 8%" and the TRD logs nothing for activation, the metric is unmeasurable and the chain is broken)*
   - Every PR-FAQ "top-3 failure reason" → reflected in PRD risks or TRD failure modes?
   - Non-goals consistent and non-contradicting across all three?

## 5. Shared quality DNA (meta-rubric / common base layer)
All three reward the same virtues — make these a shared base the artifact skills inherit:
- **Explicit non-goals / bounded scope** (top discriminator in all three)
- **Measurability** (PR-FAQ criteria → PRD KPIs → TRD observability)
- **Intellectual honesty about failure** (top-3-reasons ≈ risks ≈ failure-modes)
- **Reviewer-friendliness / disagree-ability** (silent reading; named approvers; "can a dissenter pinpoint where?")
- **Right altitude / concision** (page discipline; "as short as possible, as long as necessary")
