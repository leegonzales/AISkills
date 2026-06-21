I have enough authoritative material across all source areas. The Forward Future library is captured in full, spec-driven frameworks (Spec Kit, OpenSpec, BMAD) are confirmed, and the agentic patterns literature is verified. I'll now compose the complete loop library.

Here is the complete `references/loop-library.md` content, ready to save:

---

# Loop Library

A reference catalog of **agent loops** — repeatable, iterative agent workflows that drive toward a goal and *know when to stop*. Each loop pairs a **body** (the steps that repeat) with one or more **stop conditions**. The hardest and most valuable part of loop design is the stop condition: a loop that never stops burns budget and drifts; a loop that stops too early ships garbage. This library deliberately emphasizes **non-deterministic stops** — stops that require *judgment* ("is the architecture good enough?", "do both reviewers approve?", "have we hit diminishing returns?") rather than a mechanical predicate (`coverage == 100%`). Non-deterministic stops are where loop design is an art: you must define a proxy for "good enough," guard against the model grading its own homework, and always pair judgment with a **budget ceiling** so a loop that can't converge still terminates.

**Stop-condition families** (referenced throughout):

| Family | What ends the loop |
|---|---|
| **deterministic-predicate** | A mechanical, checkable condition (tests pass, count == 0, metric < threshold) |
| **judge-gate** | An evaluator (LLM-as-judge, rubric, or human) must pass/approve the output |
| **convergence** | Successive iterations stop changing meaningfully |
| **mutual-approval** | Two or more independent reviewers must agree on the *same* version |
| **diminishing-returns** | Marginal gain per iteration falls below a worthwhile threshold |
| **streak** | N consecutive successes/clean passes required |
| **saturation (loop-until-dry)** | Repeat until the discovery queue is empty — "no actionable items remain" |
| **holdout-generalization** | A change is kept only if it wins on held-out / unseen cases |
| **budget-ceiling** | Hard cap on iterations, time, tokens, or cost |
| **human-checkpoint** | A person must review/approve before continuing or shipping |
| **epistemic-stopping-point** | Stop when further work won't change the decision / no new information appears |

> **Determinism flag:** Each loop is tagged **DETERMINISTIC stop** (mechanically checkable) or **NON-DETERMINISTIC stop** (judgment-based). Non-deterministic loops are this skill's focus and are marked ⚖️. Many production loops are **hybrid** — a judgment stop with a deterministic budget-ceiling backstop; those are flagged ⚖️ and noted.

---

## Summary Table

| # | Loop | Category | Determinism | Primary stop family |
|---|---|---|---|---|
| 1 | Reflection / Self-Critique | Refinement/Quality | ⚖️ Non-det | convergence |
| 2 | Plan-Execute-Replan | Planning/Spec | ⚖️ Non-det | epistemic-stopping-point |
| 3 | ReAct (Reason+Act) | Discovery/Research | ⚖️ Non-det | epistemic-stopping-point |
| 4 | Evaluator-Optimizer | Refinement/Quality | ⚖️ Non-det | judge-gate |
| 5 | Best-of-N / Sampling-and-Select | Creative/Generative | ⚖️ Non-det | judge-gate |
| 6 | Tree-of-Thought Search | Discovery/Research | ⚖️ Non-det | judge-gate |
| 7 | Multi-Agent Debate | Review/Critique | ⚖️ Non-det | convergence |
| 8 | Generator-Discriminator | Refinement/Quality | ⚖️ Non-det | judge-gate |
| 9 | Devil's-Advocate / Red-Team | Review/Critique | ⚖️ Non-det | saturation |
| 10 | Reflexion (memory-augmented retry) | Self-improvement | ⚖️ Non-det | streak |
| 11 | Map-Reduce / Fan-Out-Gather | Discovery/Research | Det | deterministic-predicate |
| 12 | Multi-LLM Convergence | Review/Critique | ⚖️ Non-det | mutual-approval |
| 13 | LLM-as-Judge Gate | Review/Critique | ⚖️ Non-det | judge-gate |
| 14 | TDD Red-Green-Refactor | Testing/Validation | Det | deterministic-predicate |
| 15 | Test Stabilizer (de-flake) | Testing/Validation | Det/Hybrid | streak |
| 16 | 100% Coverage Loop | Testing/Validation | Det | deterministic-predicate |
| 17 | Test-Suite Speed Loop | Testing/Validation | ⚖️ Non-det | diminishing-returns |
| 18 | Quality Streak Loop | Testing/Validation | ⚖️ Non-det | streak |
| 19 | Full Product Evaluation | Testing/Validation | ⚖️ Non-det | judge-gate |
| 20 | CI-Fix Loop | Testing/Validation | Det | deterministic-predicate |
| 21 | Ticket-to-PR-Ready | Refinement/Quality | Hybrid | deterministic-predicate |
| 22 | Spec Kit (Specify→Plan→Tasks→Implement) | Planning/Spec | Hybrid | human-checkpoint |
| 23 | OpenSpec (Propose→Apply→Archive) | Planning/Spec | Hybrid | human-checkpoint |
| 24 | BMAD (Agentic Agile) | Planning/Spec | Hybrid | human-checkpoint |
| 25 | Goal Forge (SPEC/GOAL preflight) | Planning/Spec | ⚖️ Non-det | human-checkpoint |
| 26 | Completion-Contract Loop | Planning/Spec | Det | deterministic-predicate |
| 27 | Prepare-a-New-Project | Planning/Spec | ⚖️ Non-det | mutual-approval |
| 28 | Architecture Satisfaction Loop | Refinement/Quality | ⚖️ Non-det | judge-gate |
| 29 | Builder-Reviewer (Autonomy) | Review/Critique | Hybrid | mutual-approval |
| 30 | Clodex/Codex Adversarial Review | Review/Critique | ⚖️ Non-det | judge-gate |
| 31 | PR Review Feedback Loop | Review/Critique | Hybrid | mutual-approval |
| 32 | Docs Sweep | Docs | ⚖️ Non-det | saturation |
| 33 | Nightly Changelog | Docs | Det | deterministic-predicate |
| 34 | Product-Update Podcast | Docs | ⚖️ Non-det | epistemic-stopping-point |
| 35 | Research→Synthesize→Verify | Discovery/Research | ⚖️ Non-det | epistemic-stopping-point |
| 36 | Draft→Critique→Revise | Creative/Generative | ⚖️ Non-det | judge-gate |
| 37 | Claim-Extraction→Verification | Discovery/Research | Det/Hybrid | saturation |
| 38 | Loop-Until-Dry Discovery | Ops/Monitoring | Det | saturation |
| 39 | Production Error Sweep | Ops/Monitoring | Det | saturation |
| 40 | Recent-Feedback Sweep | Refinement/Quality | Det | saturation |
| 41 | Promise-to-Proof | Testing/Validation | ⚖️ Non-det | saturation |
| 42 | Propagation Compliance | Ops/Monitoring | Det | saturation |
| 43 | Housekeeper (dead-code) | Refinement/Quality | Hybrid | saturation |
| 44 | Repository Cleanup | Ops/Monitoring | ⚖️ Non-det | epistemic-stopping-point |
| 45 | Five-Minute Maintainer (polling) | Ops/Monitoring | Det | saturation |
| 46 | Self-Improving Champion | Self-improvement | ⚖️ Non-det | holdout-generalization |
| 47 | Versioned-Experiment (Revolve) | Self-improvement | ⚖️ Non-det | diminishing-returns |
| 48 | Migration Loop | Refinement/Quality | Det | deterministic-predicate |
| 49 | Perf-Threshold Loop (Sub-50ms / Cold-Load) | Refinement/Quality | Det | deterministic-predicate |
| 50 | UI/UX Score Loop | UX | ⚖️ Non-det | diminishing-returns |
| 51 | Visual-Fidelity Loop (747 / Frontend Recon) | UX | ⚖️ Non-det | judge-gate |
| 52 | Easy-Onboarding / Fresh-Clone | UX | ⚖️ Non-det | streak |
| 53 | Accessibility Repair | UX | Hybrid | saturation |
| 54 | Pixel-Safe Trim (CSS) | Refinement/Quality | Det | saturation |
| 55 | Infinite Thumbnail / Creative-Concept | Creative/Generative | ⚖️ Non-det | judge-gate |
| 56 | Subagent Arena (Axelrod) | Self-improvement | Det | deterministic-predicate |
| 57 | Customer Deployment Loop | Ops/Monitoring | ⚖️ Non-det | judge-gate |

**Non-deterministic (judgment-based) loops — the skill's focus:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 17, 18, 19, 25, 27, 28, 30, 32, 34, 35, 36, 41, 44, 46, 47, 50, 51, 52, 55, 57 (plus the hybrids 15, 21, 22, 23, 24, 29, 31, 37, 43, 53, which carry a judgment component backed by a deterministic backstop).

---

## Planning / Spec Loops

### Plan-Execute-Replan
- **Intent:** Decompose a goal into a plan, execute step by step, and revise the plan when reality diverges from expectations.
- **Category:** Planning/Spec
- **Body (steps):** 1) Produce an ordered plan from the goal. 2) Execute the next step. 3) Observe the result. 4) If the result invalidates remaining steps, re-plan from current state; else continue. 5) Repeat.
- **Stop condition(s):** **epistemic-stopping-point** — stop when the goal is satisfied and no remaining plan steps add value; backed by a **budget-ceiling** (max replans) to prevent thrashing.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (the "goal satisfied / no useful steps remain" judgment).
- **When to use / when NOT:** Use when the task is multi-step and the full decomposition is unknowable upfront. NOT for fully-known pipelines (use a static plan) or trivial single-shot tasks.
- **Cautions:** Plan thrashing — endlessly re-planning without progress; mitigate with a replan budget and a "no-progress" detector.
- **Source:** Agentic planning pattern; ReWOO/Plan-and-Execute literature ([theaiengineer.substack.com](https://theaiengineer.substack.com/p/the-4-single-agent-patterns)).

### Spec Kit Loop (Specify → Plan → Tasks → Implement)
- **Intent:** Drive a feature from product intent to working code through gated artifact phases, each feeding the next.
- **Category:** Planning/Spec
- **Body (steps):** 1) **Specify** — write the feature spec (users, problem, flows). 2) **Plan** — define stack, architecture, APIs, testing strategy, constraints. 3) **Tasks** — break the plan into ordered, dependency-aware tasks with parallel markers. 4) **Implement** — build in small validated increments. Each phase produces a Markdown artifact reviewed before the next begins.
- **Stop condition(s):** **human-checkpoint** at each phase gate (spec approved → plan approved → tasks approved → implementation accepted); implementation backed by **deterministic-predicate** (tests pass per increment).
- **Determinism:** Hybrid — human gates per phase, deterministic checks within implementation.
- **When to use / when NOT:** Use for greenfield features where upfront clarity pays off. NOT for tiny fixes or highly exploratory brownfield work (heavyweight).
- **Cautions:** Spec rot if artifacts aren't kept in sync with code; over-specification slowing trivial work.
- **Source:** [github/spec-kit](https://github.com/github/spec-kit); [Spec Kit docs](https://github.github.com/spec-kit/).

### OpenSpec Loop (Propose → Apply → Archive)
- **Intent:** Add fluid spec discipline to brownfield work via a minimal three-state machine before code is written.
- **Category:** Planning/Spec
- **Body (steps):** 1) **Propose** — create a change folder: `proposal.md` (why/what), `specs/` (requirements + scenarios), `design.md` (approach), `tasks.md` (checklist). 2) **Apply** — implement the tasks. 3) **Archive** — move the completed change to `archive/` and fold its deltas into the canonical specs.
- **Stop condition(s):** **human-checkpoint** (proposal approved before apply; change archived when complete) plus **deterministic-predicate** (all `tasks.md` items checked).
- **Determinism:** Hybrid.
- **When to use / when NOT:** Use for iterative brownfield changes needing lightweight traceability without rigid phase gates. NOT when heavy governance/sign-off is mandatory (use BMAD/Spec Kit).
- **Cautions:** Skipping archive leaves specs stale; under-specified proposals leak scope into apply.
- **Source:** [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec); [openspec.pro](https://openspec.pro/).

### BMAD Loop (Agentic Agile, Breakthrough Method of Agile AI-Driven Development)
- **Intent:** Run an agile delivery cycle using specialized agent personas (analyst, PM, architect, scrum master, dev, QA) with rigorous phase workflows.
- **Category:** Planning/Spec
- **Body (steps):** 1) Analyst/PM produce a PRD. 2) Architect produces architecture docs. 3) Scrum-master shards work into stories with embedded context. 4) Dev agent implements a story. 5) QA agent reviews. 6) Loop to next story.
- **Stop condition(s):** **human-checkpoint** at each persona handoff; per-story **deterministic-predicate** (acceptance criteria met) and **judge-gate** (QA persona approves).
- **Determinism:** Hybrid (heavily gated by humans + QA agent judgment).
- **When to use / when NOT:** Use for larger, multi-agent projects needing structure and role separation. NOT for small solo tasks (high ceremony).
- **Cautions:** Process overhead; persona-handoff context loss; rigidity in brownfield work.
- **Source:** BMAD-Method ([Thoughtworks Radar / framework comparisons](https://www.thoughtworks.com/en-us/radar/tools/openspec)).

### Goal Forge Loop
- **Intent:** Produce the planning files a long-running autonomous agent needs *before* it starts, so it has a stable target.
- **Category:** Planning/Spec
- **Body (steps):** 1) Interview the user about intent and constraints. 2) Draft `SPEC.md`. 3) Draft `GOAL.md` (definition of done). 4) Validate internal consistency and completeness; surface missing requirements.
- **Stop condition(s):** **human-checkpoint** — "when ready for approval, or missing requirements are found." (Judgment: are the planning docs sufficient to launch?)
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (sufficiency judgment).
- **When to use / when NOT:** Use before kicking off long unattended agent runs. NOT for short interactive tasks where you stay in the loop.
- **Cautions:** A weak GOAL.md produces an agent that "completes" the wrong thing; under-interviewing leaves gaps.
- **Source:** Forward Future Loop Library #35 ([signals.forwardfuture.ai](https://signals.forwardfuture.ai/loop-library/)).

### Completion-Contract Loop
- **Intent:** Pin down explicit completion criteria up front so long-running work has an unambiguous done-test.
- **Category:** Planning/Spec
- **Body (steps):** 1) Define a checklist of requirements with proof criteria. 2) Act toward them. 3) After each pass, mark each requirement **proved** or **missing**. 4) Continue on the missing ones.
- **Stop condition(s):** **deterministic-predicate** — all requirements marked proved (or blocked).
- **Determinism:** DETERMINISTIC stop.
- **When to use / when NOT:** Use to keep long autonomous runs honest and bounded. NOT when criteria genuinely can't be enumerated ahead of time.
- **Cautions:** Requirements that can't be objectively "proved" reintroduce judgment; gaming via weak proof criteria.
- **Source:** Forward Future Loop Library #28.

### Prepare-a-New-Project Loop
- **Intent:** Strengthen requirement/design/task/test docs until implementation is unambiguous.
- **Category:** Planning/Spec
- **Body (steps):** 1) Verify requirements, design, tasks, and tests for completeness. 2) Fix gaps. 3) Request independent reviews. 4) Revise. 5) Repeat.
- **Stop condition(s):** **mutual-approval** — "when reviewers agree materially, or a decision point is reached" (human-checkpoint).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use before committing to a build to de-risk ambiguity. NOT for throwaway prototypes.
- **Cautions:** Analysis paralysis; reviewers rubber-stamping. Cap review rounds.
- **Source:** Forward Future Loop Library #43.

---

## Refinement / Quality Loops

### Reflection / Self-Critique Loop
- **Intent:** Improve an output by having the model critique its own work and revise.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Generate a draft. 2) Switch to critic mode: check accuracy, constraints, logical gaps. 3) Revise per critique. 4) Repeat.
- **Stop condition(s):** **convergence** — two consecutive revisions are near-identical / critique finds no material issue; backed by a **budget-ceiling** (max reflection rounds, typically 2–3).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for reasoning, writing, and code where a second look catches errors. NOT for tasks needing external ground truth the model lacks (reflection alone can't fix unknown facts).
- **Cautions:** Self-critique without external signal can entrench errors or oscillate; "yes-machine" critiques that approve everything. Add a rubric or external check.
- **Source:** Reflection pattern ([machinelearningmastery.com](https://machinelearningmastery.com/7-must-know-agentic-ai-design-patterns/)).

### Evaluator-Optimizer Loop
- **Intent:** Iteratively refine output against an explicit evaluator until it passes.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Generate candidate. 2) Run a separate evaluator (rubric/LLM/tests) producing a score + actionable feedback. 3) Optimize the candidate using the feedback. 4) Re-evaluate.
- **Stop condition(s):** **judge-gate** — evaluator score ≥ threshold; backed by **budget-ceiling**.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (unless the evaluator is a deterministic test).
- **When to use / when NOT:** Use when you can articulate quality criteria but not generate perfect output first try. NOT when no meaningful evaluator exists.
- **Cautions:** Reward hacking — output optimizes to the evaluator's blind spots; keep evaluator and generator separated, vary the evaluator.
- **Source:** Evaluator-Optimizer pattern ([sitepoint.com](https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/)).

### Generator-Discriminator Loop
- **Intent:** A generator proposes, a discriminator judges high/low quality; the generator improves against the discriminator's signal.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Generator produces candidate(s). 2) Discriminator labels quality / picks winners. 3) Generator conditions on the discriminator's reasoning to produce better candidates. 4) Repeat.
- **Stop condition(s):** **judge-gate** — discriminator accepts; backed by **budget-ceiling**.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for quality-sensitive generation (code, copy, designs) where "I know it when I see it" beats hard specs. NOT when the discriminator is weak or correlated with the generator (collapses to self-approval).
- **Cautions:** Discriminator capture; mode collapse. Use an independent or stronger discriminator model.
- **Source:** Self-play / generator-discriminator survey ([arxiv 2406.01252](https://arxiv.org/pdf/2406.01252)).

### Architecture Satisfaction Loop
- **Intent:** Refactor architecture through tested checkpoints until it meets the bar.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Refactor a slice. 2) Live-test. 3) Run autoreview. 4) Commit. 5) Track progress. 6) Repeat.
- **Stop condition(s):** **judge-gate** — "until you are happy with the architecture" (human/agent judgment); backed by **budget-ceiling**.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop — the canonical fuzzy stop; define a rubric (coupling, clarity, testability) to make "happy" concrete.
- **When to use / when NOT:** Use for structural improvement with passing tests as a safety net. NOT when behavior isn't covered by tests (risk of silent regressions).
- **Cautions:** Endless gold-plating; "happy" never arrives. Pre-commit to a rubric and a round cap.
- **Source:** Forward Future Loop Library #2.

### Ticket-to-PR-Ready Loop
- **Intent:** Turn a bug ticket into a review-ready minimal patch.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Reproduce the failure. 2) Prove the root cause. 3) Make the minimal fix. 4) Re-test. 5) Open PR.
- **Stop condition(s):** **deterministic-predicate** — reproduction passes after fix; bounded by "after reproduction succeeds **or two attempts fail**" (**budget-ceiling**).
- **Determinism:** Hybrid (deterministic test stop + attempt cap).
- **When to use / when NOT:** Use for well-scoped bugs. NOT for vague feature requests lacking a reproduction.
- **Cautions:** Fixing symptoms without proving root cause; the "two attempts then escalate" rule prevents grinding.
- **Source:** Forward Future Loop Library #16.

### Housekeeper Loop (Dead-Code / Stale-File Cleanup)
- **Intent:** Remove dead code and stale files via low-risk, proven-safe deletions.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Find dead code / stale files. 2) Prove the cleanup is safe (references, tests). 3) Run tests. 4) Commit. 5) Repeat.
- **Stop condition(s):** **saturation (loop-until-dry)** — no safe candidates remain; backed by "or progress stalls."
- **Determinism:** Hybrid (deterministic tests gate each deletion; "safe candidate" judgment).
- **When to use / when NOT:** Use for hygiene passes with good test coverage. NOT in codebases with reflection/dynamic dispatch where "unreferenced" is unreliable.
- **Cautions:** Deleting code that's used dynamically; require proof, not just absence of static references.
- **Source:** Forward Future Loop Library #41.

### Migration Loop
- **Intent:** Move a codebase from old API/framework/version to new, file by file, keeping it green throughout.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Enumerate sites using the old pattern. 2) Migrate the next site. 3) Run tests/typecheck. 4) Commit. 5) Repeat over remaining sites.
- **Stop condition(s):** **deterministic-predicate** — zero remaining old-pattern sites AND full suite green (a **saturation** queue drained with a hard correctness gate).
- **Determinism:** DETERMINISTIC stop.
- **When to use / when NOT:** Use for mechanical, enumerable migrations with test coverage. NOT for migrations requiring behavioral redesign per site.
- **Cautions:** Partial migrations leaving two patterns coexisting; codemod false matches.
- **Source:** Common engineering pattern (general).

### Perf-Threshold Loop (Sub-50ms / Cold-Load Trimmer)
- **Intent:** Drive a measurable performance metric below a target across all relevant surfaces.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Record baseline metric per page/path. 2) Make one change (defer/remove/compress). 3) Re-measure across all surfaces. 4) Verify no behavior change. 5) Repeat on the worst remaining surface.
- **Stop condition(s):** **deterministic-predicate** — "every page < 50 ms" (or no safe candidate remains, a **saturation** variant); behavioral safety via regression checks.
- **Determinism:** DETERMINISTIC stop (measured threshold).
- **When to use / when NOT:** Use when the target is measurable and behavior is test-guarded. NOT when "fast enough" is subjective (use diminishing-returns instead).
- **Cautions:** Optimizing measured pages while regressing unmeasured ones; metric gaming. Hold behavior tests constant.
- **Source:** Forward Future Loop Library #3, #37.

### Pixel-Safe Trim Loop (CSS / Bundle)
- **Intent:** Remove styling/code while preserving exact visual identity.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Capture reference screenshots of all pages. 2) Remove one declaration/rule. 3) Rebuild. 4) Re-screenshot and diff. 5) Keep if pixel-identical (within tolerance), else revert. 6) Repeat.
- **Stop condition(s):** **saturation (loop-until-dry)** — no removable candidate remains without visual change; or **human-checkpoint** when a removal needs sign-off.
- **Determinism:** DETERMINISTIC stop (pixel-diff gate per candidate).
- **When to use / when NOT:** Use for dead-CSS/bundle reduction with visual regression tooling. NOT without reliable screenshot diffing.
- **Cautions:** Responsive/interaction states not captured in screenshots; diff tolerance hiding real changes.
- **Source:** Forward Future Loop Library #38.

### Recent-Feedback Sweep
- **Intent:** Turn one user correction into a project-wide audit that fixes every instance of the same class of problem.
- **Category:** Refinement/Quality
- **Body (steps):** 1) Collect recent user corrections. 2) Generalize each into an issue class. 3) Audit the whole project for that class. 4) Fix all instances. 5) Repeat per correction.
- **Stop condition(s):** **saturation (loop-until-dry)** — all instances fixed; backed by **budget-ceiling**.
- **Determinism:** DETERMINISTIC stop (instance count → 0).
- **When to use / when NOT:** Use to compound a single fix into systemic improvement ("compound, don't consume"). NOT when the correction is genuinely one-off.
- **Cautions:** Over-generalizing a narrow correction into incorrect mass edits.
- **Source:** Forward Future Loop Library #31.

---

## Review / Critique Loops

### Multi-Agent Debate Loop
- **Intent:** Have multiple agents argue competing answers to surface the strongest one.
- **Category:** Review/Critique
- **Body (steps):** 1) Each agent states an answer + reasoning. 2) Agents read others' arguments and rebut/revise. 3) Repeat rounds. 4) Aggregate or have a judge pick the consensus.
- **Stop condition(s):** **convergence** — agents agree / answers stabilize across a round (adaptive stability detection); backed by **budget-ceiling** (max rounds).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for hard reasoning/judgment questions where single-shot is unreliable. NOT for simple factual lookups (expensive overkill).
- **Cautions:** Premature consensus / herding; persuasive-but-wrong agents winning. Use a judge and stability detection.
- **Source:** Multi-agent debate for LLM judges ([arxiv 2510.12697](https://arxiv.org/html/2510.12697v1)).

### Devil's-Advocate / Red-Team Loop
- **Intent:** Attack a design/plan until objections are resolved or explicitly accepted.
- **Category:** Review/Critique
- **Body (steps):** 1) Critic argues the strongest flaws/attack vectors. 2) Record objections by impact. 3) Builder fixes or justifies each. 4) Repeat.
- **Stop condition(s):** **saturation** — no high-impact objection remains; or **convergence** — "two rounds repeat the same objections" (budget-ceiling).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for high-stakes designs, security, and risky decisions. NOT for low-stakes reversible choices (over-deliberation).
- **Cautions:** Bikeshedding on low-impact objections; critic with no off-switch. Rank by impact; require justification, not just fixes.
- **Source:** Forward Future Loop Library #24; red-team pattern.

### Multi-LLM Convergence Loop
- **Intent:** Get two *independent* AI systems to approve the **same unchanged version**.
- **Category:** Review/Critique
- **Body (steps):** 1) Review with system A; revise. 2) Review with system B; revise. 3) Re-submit the revised version to A. 4) Repeat until one version survives both unchanged.
- **Stop condition(s):** **mutual-approval** — both systems approve the identical version; backed by **budget-ceiling** (pass limit).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use when one model's blind spots need a second model's coverage (the key anti-self-approval move). NOT when models are too similar to add independent signal.
- **Cautions:** Ping-pong where each model undoes the other's changes — never converges; cap passes and detect oscillation.
- **Source:** Forward Future Loop Library #34.

### LLM-as-Judge Gate
- **Intent:** Use an LLM evaluator as a quality gate that output must clear before shipping.
- **Category:** Review/Critique
- **Body (steps):** 1) Produce output. 2) Judge scores it against an explicit rubric (optionally self-consistency: sample N judgments, average). 3) If pass, ship; if fail, return feedback and regenerate. 4) Repeat.
- **Stop condition(s):** **judge-gate** — judge score ≥ threshold; backed by **budget-ceiling**.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use to scale subjective quality checks. NOT as sole gate for safety-critical correctness (pair with deterministic tests).
- **Cautions:** Judge bias (position, verbosity, self-preference), prompt-injectable rubrics. Use a strong/most-capable judge model, randomize order, sample multiple judgments.
- **Source:** LLMs-as-Judges survey ([arxiv 2412.05579](https://arxiv.org/html/2412.05579v2)).

### Builder-Reviewer (Autonomy) Loop
- **Intent:** Pass code between a builder and a reviewer role until both verify the change.
- **Category:** Review/Critique
- **Body (steps):** 1) Builder makes a bounded change *with a test that proves it*. 2) Reviewer independently verifies (runs tests, inspects). 3) If reviewer rejects, return with findings. 4) Repeat.
- **Stop condition(s):** **mutual-approval** — both passes verify; or protected/out-of-scope work identified (human-checkpoint).
- **Determinism:** Hybrid (deterministic test proof + reviewer judgment).
- **When to use / when NOT:** Use for autonomous code changes needing a second set of eyes. NOT for changes without a clear verifying test.
- **Cautions:** Builder and reviewer being the same model/context (loses independence); scope creep. Keep changes bounded.
- **Source:** Forward Future Loop Library #27.

### Codex/Clodex Adversarial-Review Loop
- **Intent:** Use a separate code agent to adversarially review PRs until it approves.
- **Category:** Review/Critique
- **Body (steps):** 1) Plan. 2) Implement. 3) Open PR. 4) Adversarial agent reviews and files findings. 5) Fix findings. 6) Re-request review.
- **Stop condition(s):** **judge-gate** — reviewing agent approves; or **budget-ceiling** (max iterations) or stalled-progress detection.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use to raise PR quality with an independent reviewer. NOT when the reviewer model lacks the context to judge (noise).
- **Cautions:** Endless nit-picking; reviewer hallucinating issues. Cap iterations; require the reviewer to rank severity.
- **Source:** Forward Future Loop Library #19.

### PR Review Feedback Loop
- **Intent:** Cycle a PR through CI + multiple review bots, fixing until checks are green and reviewers approve.
- **Category:** Review/Critique
- **Body (steps):** 1) Push changes. 2) Monitor CI checks. 3) Fetch review comments (Gemini, Cursor, Claude, custom reviewers). 4) Triage by priority. 5) Fix. 6) Re-push. 7) Repeat.
- **Stop condition(s):** **mutual-approval** — all reviewers approve AND CI green; backed by **budget-ceiling** (2–3 review cycles per PR).
- **Determinism:** Hybrid (deterministic CI + reviewer-approval judgment).
- **When to use / when NOT:** Use for any PR with bot/human reviewers. NOT for trivial changes with no review requirement.
- **Cautions:** Reviewer rate-limits; conflicting feedback across bots; infinite nit loops. Cap cycles; reconcile conflicts explicitly.
- **Source:** PR-review-loop pattern (general practice).

---

## Discovery / Research Loops

### ReAct Loop (Reason + Act)
- **Intent:** Interleave reasoning with tool actions, using observations to guide the next step.
- **Category:** Discovery/Research
- **Body (steps):** 1) Think about what's needed. 2) Take an action (tool/search/code). 3) Observe the result. 4) Reason about it. 5) Repeat until the answer is grounded.
- **Stop condition(s):** **epistemic-stopping-point** — the agent has enough grounded information to answer; backed by **budget-ceiling** (max steps).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Default for complex, unpredictable tasks needing tools and transparency. NOT for tasks solvable in one shot (latency overhead).
- **Cautions:** Looping on the same failing action; rationalized "enough info" when it isn't. Detect repeated actions; cap steps.
- **Source:** ReAct pattern ([servicesground.com](https://servicesground.com/blog/agentic-reasoning-patterns/)).

### Tree-of-Thought Search Loop
- **Intent:** Explore multiple reasoning branches, scoring and expanding the most promising.
- **Category:** Discovery/Research
- **Body (steps):** 1) From the current node, generate several candidate next steps. 2) Score each (often via LLM-as-judge). 3) Expand the best branch(es); prune the rest. 4) Repeat (BFS/DFS/beam).
- **Stop condition(s):** **judge-gate** — a leaf reaches an accepted solution; backed by **budget-ceiling** (depth/breadth/node cap).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for problems with many viable paths and a scorable intermediate state (puzzles, planning, search). NOT for linear tasks (wasteful).
- **Cautions:** Combinatorial blowup; unreliable branch scoring. Use beam width + a validator agent.
- **Source:** ToT + validator-agent work ([arxiv 2409.11527](https://arxiv.org/html/2409.11527v2)).

### Map-Reduce / Fan-Out-Gather Loop
- **Intent:** Split a large task across parallel workers, then aggregate their outputs.
- **Category:** Discovery/Research
- **Body (steps):** 1) Partition the input (files/chunks/subquestions). 2) Fan out independent workers (one per partition). 3) Each worker returns a structured result. 4) Reduce/merge into a final answer. 5) Optionally re-fan-out on gaps.
- **Stop condition(s):** **deterministic-predicate** — all partitions processed and merged (the queue is empty).
- **Determinism:** DETERMINISTIC stop (the reduce step is judgment, but the loop terminates on partition exhaustion).
- **When to use / when NOT:** Use for large corpora / embarrassingly parallel work (doc review, multi-file search). NOT when subtasks share state or depend on each other (use sequential).
- **Cautions:** Worker collisions on shared resources (use git worktrees per agent); merge conflicts; lost-in-reduce detail. Wave-based execution for dependent work.
- **Source:** Orchestrator-worker / map-reduce agent pattern (general).

### Research → Synthesize → Verify Loop
- **Intent:** Gather sources, synthesize a claim/answer, then verify it against evidence — looping when verification fails.
- **Category:** Discovery/Research
- **Body (steps):** 1) Search/gather sources. 2) Synthesize an answer. 3) Verify each load-bearing claim against sources (adversarially). 4) If unsupported, re-research that claim. 5) Repeat.
- **Stop condition(s):** **epistemic-stopping-point** — every load-bearing claim is supported and new searches surface no new material; backed by **budget-ceiling**.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for fact-sensitive research and briefs. NOT for opinion/creative tasks without ground truth.
- **Cautions:** Stopping when searches feel exhausted but coverage is biased; citing sources that don't actually support the claim. Verify with a separate pass.
- **Source:** Deep-research / research→synthesize→verify pattern (general).

### Claim-Extraction → Verification Loop
- **Intent:** Decompose a document into atomic claims and verify each independently.
- **Category:** Discovery/Research
- **Body (steps):** 1) Extract atomic, checkable claims. 2) For each claim, gather evidence. 3) Label supported / refuted / unverifiable. 4) Loop over all claims; flag/fix the document's unsupported claims.
- **Stop condition(s):** **saturation (loop-until-dry)** — every extracted claim is labeled; per-claim verification may be **deterministic** (source match) or judgment-based.
- **Determinism:** Det/Hybrid stop (claim queue drained; labeling can require judgment).
- **When to use / when NOT:** Use for fact-checking, claim audits, and Claimify-style analysis. NOT for purely subjective text.
- **Cautions:** Bad atomic decomposition (claims too coarse to check); over-trusting a single source. 
- **Source:** Claim-extraction/verification (MAV-C Claimify pattern).

---

## Testing / Validation Loops

### TDD Red-Green-Refactor Loop
- **Intent:** Drive implementation from failing tests to passing, then clean up.
- **Category:** Testing/Validation
- **Body (steps):** 1) **Red** — write a failing test for the next behavior. 2) **Green** — write the minimal code to pass it. 3) **Refactor** — improve structure with tests green. 4) Repeat per behavior.
- **Stop condition(s):** **deterministic-predicate** — all desired-behavior tests written and green.
- **Determinism:** DETERMINISTIC stop.
- **When to use / when NOT:** Use for well-specified logic. NOT for exploratory spikes where the interface is unknown.
- **Cautions:** Writing tests that pass trivially; refactoring without re-running tests.
- **Source:** Classic TDD; agentic TDD skill (general).

### Test Stabilizer (De-Flake) Loop
- **Intent:** Eliminate flaky tests by fixing root causes, not by retrying.
- **Category:** Testing/Validation
- **Body (steps):** 1) Run the suite N times. 2) Identify tests that pass inconsistently. 3) Diagnose and fix the root cause (timing, ordering, shared state). 4) Re-run N times. 5) Repeat.
- **Stop condition(s):** **streak** — N consecutive clean full-suite passes; backed by stalled-progress and human-checkpoint backstops.
- **Determinism:** Det/Hybrid (streak is mechanical; root-cause diagnosis is judgment).
- **When to use / when NOT:** Use before trusting a suite as a gate. NOT as a substitute for fixing the underlying nondeterminism (never paper over with retries).
- **Cautions:** "Fixing" flakes by adding sleeps or retries; declaring stable after too few runs.
- **Source:** Forward Future Loop Library #44.

### 100% Coverage Loop
- **Intent:** Reach complete test coverage by systematically adding tests.
- **Category:** Testing/Validation
- **Body (steps):** 1) Measure coverage. 2) Find the largest uncovered region. 3) Add meaningful tests. 4) Re-measure. 5) Repeat.
- **Stop condition(s):** **deterministic-predicate** — coverage == 100% (or agreed target).
- **Determinism:** DETERMINISTIC stop.
- **When to use / when NOT:** Use for critical libraries where coverage gaps are unacceptable. NOT as a vanity metric — coverage ≠ correctness.
- **Cautions:** Coverage-gaming with assertion-free tests; chasing the last % on trivial code.
- **Source:** Forward Future Loop Library #5.

### Test-Suite Speed Loop
- **Intent:** Make the suite run faster without reducing coverage.
- **Category:** Testing/Validation
- **Body (steps):** 1) Profile the suite. 2) Optimize the slowest tests (parallelize, mock, dedupe). 3) Re-run, confirming coverage unchanged. 4) Repeat.
- **Stop condition(s):** **diminishing-returns** — further optimization yields negligible speedup ("as fast as possible without reducing coverage"); backed by budget-ceiling.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (the "negligible / not worth it" judgment).
- **When to use / when NOT:** Use when slow CI hurts iteration. NOT when the suite is already fast (premature optimization).
- **Cautions:** Speedups that quietly drop coverage or introduce flakiness. Hold coverage as an invariant.
- **Source:** Forward Future Loop Library #11.

### Quality Streak Loop
- **Intent:** Fix product failures until you achieve a streak of consecutive successful cases.
- **Category:** Testing/Validation
- **Body (steps):** 1) Run a test scenario. 2) On failure, document it, add coverage, fix, and **reset the streak counter**. 3) On success, increment the streak. 4) Repeat.
- **Stop condition(s):** **streak** — N successful cases in a row; backed by budget-ceiling.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (scenario "success" often requires judgment).
- **When to use / when NOT:** Use to ensure stability under varied inputs, not just one happy path. NOT when scenarios aren't representative.
- **Cautions:** Cherry-picking easy scenarios to build a hollow streak; reset discipline is essential.
- **Source:** Forward Future Loop Library #9.

### Full Product Evaluation Loop
- **Intent:** Test every major capability against an explicit quality bar and fix until all meet it.
- **Category:** Testing/Validation
- **Body (steps):** 1) Enumerate capabilities → scenarios. 2) Define success criteria per scenario. 3) Run all. 4) Fix failures. 5) Re-test. 6) Repeat.
- **Stop condition(s):** **judge-gate** — every scenario meets the original quality bar; backed by budget-ceiling.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for release-readiness evaluation. NOT mid-development when capabilities are still churning.
- **Cautions:** Moving the quality bar to declare done; scenario coverage gaps. Freeze the bar before starting.
- **Source:** Forward Future Loop Library #10.

### CI-Fix Loop
- **Intent:** Get a red pipeline green.
- **Category:** Testing/Validation
- **Body (steps):** 1) Read the CI failure. 2) Reproduce locally. 3) Fix. 4) Push. 5) Re-run CI. 6) Repeat per failing check.
- **Stop condition(s):** **deterministic-predicate** — all CI checks pass; backed by budget-ceiling (escalate after N attempts).
- **Determinism:** DETERMINISTIC stop.
- **When to use / when NOT:** Use whenever CI is red. NOT for masking failures by disabling checks.
- **Cautions:** Fixing one check while breaking another; flaky CI mistaken for real failures (combine with Test Stabilizer).
- **Source:** Common engineering pattern (general).

### Promise-to-Proof Loop
- **Intent:** Verify customer-facing claims actually match product behavior.
- **Category:** Testing/Validation
- **Body (steps):** 1) List public promises/marketing claims. 2) Compare each to real behavior. 3) Label supported/unsupported, ranked by risk. 4) Fix the riskiest unsupported promise (or correct the claim). 5) Repeat.
- **Stop condition(s):** **saturation** — no high-risk unsupported promise remains.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop ("does behavior satisfy the promise?" is judgment).
- **When to use / when NOT:** Use before launches and for trust/compliance audits. NOT for internal-only tooling.
- **Cautions:** Interpreting vague marketing language too charitably; missing implicit promises.
- **Source:** Forward Future Loop Library #32.

---

## Docs Loops

### Docs Sweep Loop
- **Intent:** Bring documentation back into alignment with the current codebase.
- **Category:** Docs
- **Body (steps):** 1) Review the codebase. 2) Identify stale/missing docs. 3) Update them. 4) Verify against code. 5) Open PR. (Repeat across doc surfaces.)
- **Stop condition(s):** **saturation (loop-until-dry)** — no stale docs remain; "whenever a doc pass is needed" (recurring trigger).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop ("stale" requires judgment of code-vs-doc drift).
- **When to use / when NOT:** Use after feature waves or before releases. NOT continuously (batch it).
- **Cautions:** Documenting intended behavior instead of actual; missing undocumented surfaces.
- **Source:** Forward Future Loop Library #1.

### Nightly Changelog Loop
- **Intent:** Keep a changelog current with each day's changes.
- **Category:** Docs
- **Body (steps):** 1) Each night, diff the day's merged changes. 2) Summarize user-facing items. 3) Append to changelog.
- **Stop condition(s):** **deterministic-predicate** — the day's commits are all reflected; recurring (per night).
- **Determinism:** DETERMINISTIC stop.
- **When to use / when NOT:** Use for active products with frequent merges. NOT for low-activity repos (batch weekly).
- **Cautions:** Logging commits verbatim instead of user-facing impact.
- **Source:** Forward Future Loop Library #8.

### Product-Update Podcast/Episode Loop
- **Intent:** Turn meaningful product changes into a verified narrative artifact (podcast/episode/post).
- **Category:** Docs
- **Body (steps):** 1) Review recent changes. 2) Verify them against docs/reality. 3) Write the script. 4) Check accuracy.
- **Stop condition(s):** **epistemic-stopping-point** — "if nothing meaningful shipped, produce nothing"; otherwise stop when the script is accurate.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop ("meaningful" + accuracy judgment).
- **When to use / when NOT:** Use to auto-generate release comms. NOT when changes are trivial (the loop should no-op).
- **Cautions:** Manufacturing content from nothing; hyping minor changes. The "no episode" branch is the discipline.
- **Source:** Forward Future Loop Library #18.

---

## UX Loops

### UI/UX Score Loop
- **Intent:** Improve a user flow by completing it from a fresh state and fixing the weakest screen.
- **Category:** UX
- **Body (steps):** 1) Complete the flow from a clean state. 2) Score each screen against a rubric. 3) Improve the lowest-scoring screen. 4) Re-run the flow. 5) Repeat.
- **Stop condition(s):** **diminishing-returns** — "two passes without gain"; or success, or blocked access.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (screen scoring is judgment).
- **When to use / when NOT:** Use to polish a flow holistically. NOT for micro-tweaks with no end-to-end flow.
- **Cautions:** Optimizing screens in isolation, breaking flow continuity; subjective scoring drift. Use a fixed rubric.
- **Source:** Forward Future Loop Library #36.

### Visual-Fidelity Loop (747 Benchmark / Frontend Reconstruction)
- **Intent:** Iteratively improve a visual artifact toward a fidelity target by rendering, comparing, and fixing the weakest aspect.
- **Category:** UX
- **Body (steps):** 1) Build/render the artifact. 2) Capture it from multiple angles/states (e.g., nine views; static + moving). 3) Identify the weakest feature vs. the reference. 4) Fix it. 5) Re-render and compare. 6) Repeat.
- **Stop condition(s):** **judge-gate** — visual quality threshold reached; or stalled progress / budget-ceiling.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (visual "good enough" is judgment, even with diffs).
- **When to use / when NOT:** Use for generative visual/3D/UI work with a reference target. NOT when there's no clear visual goal.
- **Cautions:** Local-optimum thrashing (fixing one view breaks another); subjective fidelity. Compare across all views each round.
- **Source:** Forward Future Loop Library #21, #22.

### Easy-Onboarding / Fresh-Clone Loop
- **Intent:** Verify a newcomer can get to a working state using only the README — no tribal knowledge.
- **Category:** UX
- **Body (steps):** 1) Start from a fresh clone / fresh-user state. 2) Follow only the documented steps. 3) When something fails, fix the gap (docs or setup). 4) Start over from scratch. 5) Repeat.
- **Stop condition(s):** **streak** — one fully clean run to ready-state with no manual intervention; backed by budget-ceiling.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop ("obstacle" identification is judgment); the clean-run gate itself is observable.
- **When to use / when NOT:** Use before open-sourcing or onboarding new contributors. NOT for mature internal tooling everyone already knows.
- **Cautions:** Carrying hidden state between attempts (must truly start fresh); fixing symptoms not doc gaps.
- **Source:** Forward Future Loop Library #25, #39.

### Accessibility Repair Loop
- **Intent:** Remove accessibility barriers in priority order against a standard (e.g., WCAG).
- **Category:** UX
- **Body (steps):** 1) Scan for issues (automated + manual). 2) Confirm each is real. 3) Rank by user harm. 4) Fix the highest-impact issue. 5) Re-scan. 6) Repeat.
- **Stop condition(s):** **saturation** — no blocker remains; or human-checkpoint when a fix needs approval.
- **Determinism:** Hybrid (automated scans deterministic; harm-ranking + manual confirmation judgment).
- **When to use / when NOT:** Use for any user-facing product. NOT as a one-time checkbox (re-run on UI changes).
- **Cautions:** Trusting automated scanners alone (they miss context); fixing easy issues over high-harm ones.
- **Source:** Forward Future Loop Library #40.

---

## Ops / Monitoring Loops

### Loop-Until-Dry Discovery Loop
- **Intent:** Generic pattern — repeatedly discover and process actionable items until none remain.
- **Category:** Ops/Monitoring
- **Body (steps):** 1) Scan for actionable items. 2) If none, stop. 3) Otherwise, process the highest-value item. 4) Re-scan (new items may have appeared). 5) Repeat.
- **Stop condition(s):** **saturation (loop-until-dry)** — "if no actionable items remain, stop"; backed by budget-ceiling for safety.
- **Determinism:** DETERMINISTIC stop (item count → 0), assuming "actionable" is a clear predicate.
- **When to use / when NOT:** The base template for sweeps (errors, lint, TODOs, queue drains). NOT when items regenerate faster than processed (will never dry — add a budget).
- **Cautions:** Self-regenerating queues causing infinite loops; "actionable" being too fuzzy.
- **Source:** General pattern; underlies many Forward Future loops.

### Production Error Sweep Loop
- **Intent:** Find and fix actionable production errors from logs.
- **Category:** Ops/Monitoring
- **Body (steps):** 1) Review error logs. 2) Trace root cause of the top error. 3) Fix. 4) Verify. 5) Open PR. 6) Re-scan logs.
- **Stop condition(s):** **saturation** — "if no actionable errors are present, stop."
- **Determinism:** DETERMINISTIC stop (no actionable errors).
- **When to use / when NOT:** Use for triage/on-call hygiene. NOT for noisy logs full of non-actionable warnings (filter first).
- **Cautions:** Treating noise as signal; fixing symptoms not root causes.
- **Source:** Forward Future Loop Library #4.

### Propagation Compliance Loop
- **Intent:** After changing a canonical value, find and update every stale copy across the project.
- **Category:** Ops/Monitoring
- **Body (steps):** 1) Change the canonical value. 2) Search the project for old values. 3) Fix each stale instance. 4) Re-search. 5) Repeat.
- **Stop condition(s):** **saturation (loop-until-dry)** — zero stale values; or regeneration detected (an item reappears → escalate).
- **Determinism:** DETERMINISTIC stop (stale count → 0).
- **When to use / when NOT:** Use after config/version/constant changes (model IDs, URLs, ports). NOT when values are intentionally varied.
- **Cautions:** Regenerating sources (codegen) re-introducing old values; over-matching unrelated strings.
- **Source:** Forward Future Loop Library #33.

### Repository Cleanup Loop
- **Intent:** Recover valuable abandoned work and remove stale branches/PRs/commits.
- **Category:** Ops/Monitoring
- **Body (steps):** 1) Inspect branches, PRs, commits. 2) Recover anything valuable. 3) Clean stale items. 4) Repeat until organized.
- **Stop condition(s):** **epistemic-stopping-point** — "until the repository is current and organized" (judgment).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use periodically for repo hygiene. NOT without backups before deleting branches.
- **Cautions:** Deleting branches with unmerged valuable work; ask before destructive ops.
- **Source:** Forward Future Loop Library #12.

### Five-Minute Maintainer (Polling) Loop
- **Intent:** Keep repo work moving by waking periodically, triaging, and assigning the highest-value task without disrupting active agents.
- **Category:** Ops/Monitoring
- **Body (steps):** 1) Wake every five minutes. 2) Triage open items. 3) Assign/do the highest-value task that won't collide with active work. 4) Sleep. 5) Repeat.
- **Stop condition(s):** **saturation** — every item landed, blocked, or no work remains.
- **Determinism:** DETERMINISTIC stop (work queue empty/blocked).
- **When to use / when NOT:** Use for continuous background maintenance. NOT for urgent work needing immediate attention (polling latency).
- **Cautions:** Collisions with active agents (use isolation); busy-waiting cost. Skip if no work.
- **Source:** Forward Future Loop Library #30.

### Customer Deployment Loop
- **Intent:** Move a customer AI workflow from definition through validation to production.
- **Category:** Ops/Monitoring
- **Body (steps):** 1) Define the priority workflow. 2) Dry-run. 3) Fix problems. 4) Release in a staged rollout. 5) Monitor. 6) Iterate.
- **Stop condition(s):** **judge-gate** — outcome proven and confirmed with a customer update; backed by monitoring + human-checkpoint.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop ("outcome proven" is judgment).
- **When to use / when NOT:** Use for staged customer-facing rollouts. NOT for internal experiments (skip the staged ceremony).
- **Cautions:** Declaring success before monitoring confirms; skipping the dry-run.
- **Source:** Forward Future Loop Library #17.

---

## Self-Improvement Loops

### Reflexion Loop (Memory-Augmented Retry)
- **Intent:** Learn from failed attempts by writing verbal self-reflections to memory and retrying with that context.
- **Category:** Self-improvement
- **Body (steps):** 1) Attempt the task. 2) Get feedback (test/eval/env signal). 3) Write a reflection on *why* it failed into episodic memory. 4) Retry, conditioned on accumulated reflections. 5) Repeat.
- **Stop condition(s):** **streak** / success — task succeeds (or a success streak); backed by budget-ceiling (max trials).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (unless success is a deterministic test).
- **When to use / when NOT:** Use for tasks with a feedback signal where naive retry doesn't learn. NOT when there's no usable feedback to reflect on.
- **Cautions:** Reflections that misdiagnose the failure entrench it; memory bloat. Keep reflections concrete and tied to evidence.
- **Source:** Reflexion ([theaiengineer.substack.com](https://theaiengineer.substack.com/p/the-4-single-agent-patterns)).

### Self-Improving Champion Loop
- **Intent:** Improve a prompt/policy by promoting changes only when they beat the current champion on held-out cases.
- **Category:** Self-improvement
- **Body (steps):** 1) Change exactly one thing (challenger). 2) Evaluate challenger vs. champion on a **holdout** set. 3) Promote the challenger only if it wins. 4) Repeat.
- **Stop condition(s):** **holdout-generalization** — challenger must win on unseen cases to be kept; loop ends at target, budget-ceiling, or no-progress.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (win on holdout is measured but the target/"good enough" is judgment).
- **When to use / when NOT:** Use for prompt/policy optimization where overfitting to a dev set is the enemy. NOT without a true holdout (you'll just overfit).
- **Cautions:** Holdout leakage; changing multiple things at once (can't attribute the win). One change per iteration.
- **Source:** Forward Future Loop Library #23.

### Versioned-Experiment Loop (Revolve)
- **Intent:** Improve prompts/code through comparable, checkpointed experiments, keeping only clear wins.
- **Category:** Self-improvement
- **Body (steps):** 1) Freeze the test set. 2) Checkpoint current state. 3) Form a hypothesis and run the experiment. 4) Compare to the checkpoint. 5) Keep clear wins; revert the rest. 6) Repeat.
- **Stop condition(s):** **diminishing-returns** — on success, no further progress, a blocker, or exhausted budget.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop ("clear win" + "worth continuing" judgment).
- **When to use / when NOT:** Use for systematic optimization needing reproducibility. NOT for one-off tweaks.
- **Cautions:** Comparing against a moving test set; ambiguous-but-kept changes accumulating regressions. Freeze tests; demand *clear* wins.
- **Source:** Forward Future Loop Library #29.

### Subagent Arena Loop (Axelrod Tournament)
- **Intent:** Evaluate agent strategies by running them in a fixed-rules repeated-game tournament.
- **Category:** Self-improvement
- **Body (steps):** 1) Define strategies and a fixed scoring rule. 2) Run the full round-robin of matches. 3) Compare scores against baselines. 4) (Iterate strategies for the next tournament.)
- **Stop condition(s):** **deterministic-predicate** — the full match schedule completes (e.g., all 18 matches; a partial run is *incomplete*, not a stop).
- **Determinism:** DETERMINISTIC stop.
- **When to use / when NOT:** Use to compare agent strategies/cooperation empirically. NOT for single-agent quality tasks.
- **Cautions:** Reporting partial tournaments as results; baseline omission. Require the complete schedule.
- **Source:** Forward Future Loop Library #42.

---

## Creative / Generative Loops

### Best-of-N / Sampling-and-Select Loop
- **Intent:** Generate N independent candidates and select the best.
- **Category:** Creative/Generative
- **Body (steps):** 1) Generate N candidates (diverse temperature/prompts). 2) Score each (judge/rubric/self-consistency vote). 3) Select the winner (optionally refine it). 4) Optionally re-sample around the winner.
- **Stop condition(s):** **judge-gate** — best candidate clears the bar; or fixed N with selection (a one-shot budget-ceiling variant).
- **Determinism:** ⚖️ NON-DETERMINISTIC stop (selection is judgment unless scored by a deterministic metric).
- **When to use / when NOT:** Use when quality variance is high and you can score outputs (code with tests, copy, designs). NOT when generation is expensive and single-shot is reliable.
- **Cautions:** Reward hacking the scorer; N too small to matter. Use an independent scorer.
- **Source:** Best-of-N / self-consistency ([arxiv 2406.01252](https://arxiv.org/pdf/2406.01252)).

### Draft → Critique → Revise Loop
- **Intent:** Iteratively improve a piece of writing through critique and revision.
- **Category:** Creative/Generative
- **Body (steps):** 1) Draft. 2) Critique against a genre/quality rubric (ideally a separate pass or model). 3) Revise. 4) Repeat.
- **Stop condition(s):** **judge-gate** — rubric thresholds met; backed by **convergence** (revisions stop changing) and budget-ceiling.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for essays, posts, docs, copy. NOT for purely factual extraction (use verification loops).
- **Cautions:** Critique drift (rubric reinterpreted each round); over-revision flattening voice. Fix the rubric; cap rounds.
- **Source:** Reflection applied to writing (prose-polish pattern; general).

### Infinite Creative-Concept Loop (Thumbnails / Variants)
- **Intent:** Generate many creative concepts, score them, and iterate on the top few until one clears a quality threshold.
- **Category:** Creative/Generative
- **Body (steps):** 1) Generate ~10 concepts. 2) Score them. 3) Improve the top 3. 4) Re-score. 5) Repeat.
- **Stop condition(s):** **judge-gate** — a concept clears the quality threshold; backed by budget-ceiling.
- **Determinism:** ⚖️ NON-DETERMINISTIC stop.
- **When to use / when NOT:** Use for high-variance creative output (thumbnails, headlines, hero images). NOT when there's a single correct answer.
- **Cautions:** Scorer that doesn't predict real-world performance (CTR ≠ aesthetic score); infinite generation without a ceiling.
- **Source:** Forward Future Loop Library #26.

---

## Designing a Good Stop Condition (cheat sheet)

When building any loop, especially a non-deterministic one:

1. **Name the family.** Pick from the 11 families above. If you can't, your stop is underspecified.
2. **Make "good enough" concrete.** Replace "until happy" with a rubric, threshold, or holdout test. Judgment stops need an explicit proxy.
3. **Keep the judge independent.** Never let the generator grade its own work as the sole gate — use a separate pass, a different model (Multi-LLM Convergence), or held-out cases.
4. **Always add a budget-ceiling backstop.** Every non-deterministic loop gets a hard cap (iterations/time/tokens) so a non-converging loop still terminates.
5. **Detect non-progress.** Track whether iterations are actually improving; stop on stall (diminishing-returns / convergence) rather than burning the whole budget.
6. **Watch for self-regenerating queues** in saturation loops (codegen, noisy logs) — pair loop-until-dry with a regeneration detector and a ceiling.
7. **Gate the irreversible.** Put a human-checkpoint before anything destructive or customer-facing, regardless of how confident the loop is.

---

**Primary sources:** Forward Future Loop Library ([signals.forwardfuture.ai/loop-library](https://signals.forwardfuture.ai/loop-library/)); GitHub Spec Kit ([github.com/github/spec-kit](https://github.com/github/spec-kit)); OpenSpec ([github.com/Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)); BMAD-Method; agentic-pattern literature on Reflection/ReAct/Reflexion/Evaluator-Optimizer ([sitepoint.com](https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/), [servicesground.com](https://servicesground.com/blog/agentic-reasoning-patterns/), [theaiengineer.substack.com](https://theaiengineer.substack.com/p/the-4-single-agent-patterns)); LLM-as-judge / debate / self-play surveys ([arxiv 2412.05579](https://arxiv.org/html/2412.05579v2), [arxiv 2510.12697](https://arxiv.org/html/2510.12697v1), [arxiv 2406.01252](https://arxiv.org/pdf/2406.01252)); Tree-of-Thought validator work ([arxiv 2409.11527](https://arxiv.org/html/2409.11527v2)).

---

**Report:** I compiled the complete `references/loop-library.md` above (returned as my final message, not written to disk per instructions). It contains **57 distinct loops** across all 10 categories, exceeding the 30–50 target.

Key facts:
- **Coverage:** All 44 Forward Future loops are represented (most consolidated 1:1; a few near-duplicates merged, e.g., 747 + Frontend Reconstruction → "Visual-Fidelity Loop", Fresh-Clone + Easy-Onboarding → one entry, Sub-50ms + Cold-Load → "Perf-Threshold Loop"), plus loops the brief explicitly requested that FF lacked: ReAct, Tree-of-Thought, Best-of-N, Multi-Agent Debate, Generator-Discriminator, Reflexion, Map-Reduce, LLM-as-Judge, TDD, CI-Fix, Migration, Research→Synthesize→Verify, Claim-Extraction→Verification, plus the three spec frameworks (Spec Kit, OpenSpec, BMAD).
- **Structure:** One-paragraph intro, a stop-family glossary table, a 57-row summary table (loop | category | deterministic? | primary stop family), entries grouped under the 10 category headings using the exact required schema, and a closing "Designing a Good Stop Condition" cheat sheet.
- **Non-deterministic emphasis:** Every loop is flagged DETERMINISTIC / NON-DETERMINISTIC (⚖️), hybrids are called out, and the non-deterministic set is explicitly listed after the table. Each stop condition is classified by family with a concrete trigger, and judgment stops are paired with budget-ceiling backstops.
- **Sourcing:** Inline citations throughout (Forward Future entry numbers; Spec Kit / OpenSpec / BMAD repos; agentic-pattern articles; LLM-as-judge / debate / ToT / self-play arXiv surveys), consolidated in a sources footer.

To save it: write the content above to `/Users/leegonzales/Projects/leegonzales/AISkills/<LoopBuilderSkill>/references/loop-library.md`.
