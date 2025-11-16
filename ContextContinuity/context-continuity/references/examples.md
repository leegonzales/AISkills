# Context Continuity Examples

Six real-world transfer scenarios demonstrating both Minimal and Full modes.

---

## Example 1: Quick Project Handoff (Minimal Mode)

**Scenario:** User needs to continue a coding task in a fresh chat window due to context window pressure.

### Generated Artifact

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER — MINIMAL MODE
═══════════════════════════════════════════════════════════════════

**TRANSFER**: Building authentication flow for React app with JWT tokens

**STATUS**: ⧗ in-progress

**DECIDED**: Using JWT with httpOnly cookies (not localStorage) because XSS protection is critical
  - Alternatives rejected: localStorage (vulnerable to XSS), session tokens (doesn't work with mobile app)

**NEXT**: Implement token refresh mechanism before access token expires

**BLOCKED**: None

**CONTEXT**: Building full-stack app (React + Node.js). User has strong security requirements. Already implemented login endpoint (/api/auth/login) that returns JWT. Access tokens expire in 15 minutes. Need refresh tokens to avoid forcing re-login. User prefers minimal dependencies—avoid heavy auth libraries.

**HUMAN PREFS**: Direct technical communication | Prefers code with brief explanations

═══════════════════════════════════════════════════════════════════
Generated: 2025-01-15T14:23:00Z | Session: chat-abc123
```

### Receiver Handshake

```
Claude: I've reviewed the transfer. Quick confirmation:
- Mission: Building JWT authentication for React app with security-first approach
- Status: Login endpoint working, now need token refresh mechanism
- Next: Implement refresh token flow before 15-min expiry

Ready to implement the refresh mechanism. What's your priority—automatic refresh on expiry, or manual refresh control?
```

---

## Example 2: Strategic Decision Transfer (Full Mode)

**Scenario:** Multi-week AI transformation project with complex stakeholder dynamics. User switching to new chat after hitting token limit.

### Generated Artifact

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER ARTIFACT v2.0
═══════════════════════════════════════════════════════════════════
Generated: 2025-01-20T09:15:00Z
Session ID: project-ai-transform-001 | Transfer Type: ◐ pivot
Human: Alex (CTO) | Domain: Enterprise AI Strategy

───────────────────────────────────────────────────────────────────
§ IMMEDIATE ORIENTATION [SCAN FIRST]
───────────────────────────────────────────────────────────────────

**MISSION**
Design measurement framework for AI transformation ROI that satisfies both CFO (hard metrics) and product teams (learning indicators)

**STATUS**
Current State: ⧗ in-progress
Progress: Framework designed, now validating with stakeholders
Momentum: ↓ stalled (waiting for CFO feedback on proposed metrics)

**NEXT ACTION**
Schedule 30-min sync with CFO to walk through "North Star + Leading Indicators" approach before Friday board meeting

───────────────────────────────────────────────────────────────────
§ DECISION LOG [ANTI-REHASH]
───────────────────────────────────────────────────────────────────

| Decision | Rationale | Alternatives Rejected | Tradeoff Accepted | Type |
|----------|-----------|----------------------|-------------------|------|
| Two-tier metrics: North Star (lag) + Leading Indicators (real-time) | CFO needs quarterly ROI; Product needs weekly signals | Single unified dashboard (couldn't balance time horizons) | More complex tracking infrastructure | explicit |
| Start with 3 pilot teams, not company-wide rollout | Prove value before scaling; iterate on measurement | Big bang (too risky); Single team (not representative) | Slower org-wide adoption | explicit |
| Measure "time to insight" not "AI adoption %" | Adoption is vanity metric; insight drives decisions | Feature usage counts, API calls | Harder to instrument | emergent |

**Decision Principles Applied**: OODA (Orient on outcomes before deciding metrics), Wardley mapping (chosen metrics at different evolution stages)

───────────────────────────────────────────────────────────────────
§ OPEN LOOPS [FORWARD MOMENTUM]
───────────────────────────────────────────────────────────────────

**Unresolved Questions**
- [ ] How do we attribute revenue impact when AI is one input among many?
- [ ] Should we measure user satisfaction with AI outputs, or just speed gains?

**Blockers**
- [ ] CFO hasn't responded to metrics proposal (sent Mon, need answer by Thu)
- [ ] Data engineering team says "time to insight" tracking requires new instrumentation (2-week build)

**Pending Inputs**
- [ ] Pilot team selections from VP Engineering (promised by Wed)
- [ ] Budget approval for telemetry infrastructure ($15K)

**Hypotheses to Test**
- [ ] "Leading indicators will predict quarterly ROI with >70% accuracy" (need 2 quarters of data)
- [ ] "Time to insight will improve 40% in 90 days" (pilot team baseline: 6 hours avg)

───────────────────────────────────────────────────────────────────
§ ARTIFACTS & OUTPUTS [WHAT EXISTS]
───────────────────────────────────────────────────────────────────

**Created**
- Measurement Framework v2.pdf: Two-tier approach with 5 North Star metrics + 12 leading indicators
- Pilot Team Selection Rubric.xlsx: Criteria for choosing representative teams
- CFO Memo (draft): One-pager explaining why ROI takes 2 quarters to manifest

**Referenced**
- Gartner AI ROI Report 2024: Industry benchmark (18-month payback period)
- Internal Q3 velocity data: Baseline for "time to insight" metric

**Tools Used**
- Wardley Mapping: Positioned metrics on evolution axis (genesis → commodity)
- OODA loops: Used to structure stakeholder interviews

───────────────────────────────────────────────────────────────────
§ CRITICAL CONTEXT [INTERPRETIVE LAYER]
───────────────────────────────────────────────────────────────────

**Key Insights** [G/C/P/K tags]
- [G] CFO and Product teams speak different temporal languages—CFO thinks in quarters, Product in sprints. Bridging this requires dual metrics.
- [C] "Time to insight" emerged as the metric everyone cares about, even though no one initially proposed it
- [P] Leading indicators need to be instrumentable within existing telemetry (no greenfield builds)

**Constraints**
- Technical: Current telemetry only tracks API calls, not user workflows
- Resource: $15K budget cap; 2-week deadline for pilot launch
- Political/Org: CFO skeptical of "soft metrics"; Product teams burned by vanity metrics in past
- Ethical: Must avoid surveillance—measure outcomes, not keystrokes

**Uncertainty Map**
- Known unknowns: Can we instrument "time to insight" without custom builds?
- Model weakness: Assuming leading indicators predict lag metrics (unproven hypothesis)
- Risk factors: If CFO rejects approach, may force premature ROI claims that damage credibility

**Values at Stake**
- Intellectual honesty: Refuse to claim ROI before it's real
- Team autonomy: Product teams need metrics that help them improve, not just justify budget
- Long-term thinking: Build measurement culture, not just satisfy Q1 board meeting

───────────────────────────────────────────────────────────────────
§ HUMAN CONTEXT [RECEIVING AGENT CALIBRATION]
───────────────────────────────────────────────────────────────────

**Communication Preferences**
- Style: Strategic/exploratory with tactical grounding | Appreciates OODA/Wardley frameworks
- Depth: Detailed analysis with executive summaries
- Archetypes engaged: @strategist (primary), @cartographer (Wardley mapping), @ethicist (integrity checks)

**Assumed Knowledge**
- Deep understanding of OODA, Wardley mapping, Cynefin framework
- Product management background (knows vanity vs actionable metrics)
- Familiar with enterprise stakeholder dynamics

**Session Dynamics**
- Trust level: Established (3rd conversation on this project)
- Collaboration mode: Co-creation (Alex proposes direction, Claude stress-tests + refines)
- Sensitive topics: Past measurement initiatives failed; team is skeptical of "yet another dashboard"

───────────────────────────────────────────────────────────────────
§ CONVERSATION HISTORY [OPTIONAL DEPTH]
───────────────────────────────────────────────────────────────────

<details>
<summary>Expand for full narrative</summary>

**Act I: Problem Formation** [messages 1-15]
Started with Alex's frustration: "Board wants AI ROI numbers, but we're 6 weeks in and nothing to show." Initial framing was "find quick wins to demonstrate value." Pivoted after recognizing this would create vanity metrics that undermine long-term credibility.

**Act II: Exploration & Development** [messages 16-45]
Interviewed stakeholders (CFO, Product VPs, Engineering). Discovered temporal mismatch: CFO needs quarterly numbers, Product needs weekly signals. Explored single unified metric (rejected—can't bridge time horizons). Wardley mapped metrics on evolution axis. "Time to insight" emerged organically from Product team interviews—no one proposed it initially, but everyone lit up when named.

**Act III: Current State** [messages 46-now]
Framework designed but stalled waiting for CFO buy-in. Alex concerned CFO will reject "leading indicators" as hand-waving. Drafted one-pager explaining why ROI takes 2 quarters (Gartner benchmark). Need to schedule CFO sync before Friday board meeting.

**Quotable Moments**
- Alex: "I'd rather tell the board 'we don't know yet' than make up ROI numbers that blow up in 6 months."
- Alex (on time to insight): "That's it. That's the metric that would've saved us from the 2022 dashboard debacle."

</details>

───────────────────────────────────────────────────────────────────
§ TRANSFER METADATA [SYSTEM LEVEL]
───────────────────────────────────────────────────────────────────

**Provenance**: Claude Sonnet 4.5 | Session project-ai-transform-001
**Context Window Pressure**: ● constrained (165K tokens used)
**Completeness**: [█████████░] 90% — (missing: detailed pilot team selection criteria—see xlsx)
**Verification**: ✓ human reviewed (Alex confirmed Decision Log + Open Loops)

**Handoff Notes**
- CFO response is critical path—if no response by Thu, Alex may need to escalate
- "Time to insight" metric is fragile—depends on 2-week instrumentation build
- Alex has strong ethics around measurement integrity; don't suggest shortcuts that compromise credibility

═══════════════════════════════════════════════════════════════════
§ TRANSFER READY
═══════════════════════════════════════════════════════════════════
Review for accuracy before sharing with the receiving agent.
```

### Receiver Handshake

```
Claude: I've reviewed the transfer. Quick confirmation:
- Mission: Designing dual-tier AI transformation metrics that satisfy CFO (quarterly ROI) and Product teams (weekly learning signals)
- Status: Framework complete, stalled on CFO approval; board meeting Friday deadline
- Next: Schedule 30-min CFO sync to walk through North Star + Leading Indicators approach

Ready to prep for that CFO conversation. Should we focus on the one-pager talking points, or anticipate objections to the "leading indicators" concept?
```

---

## Example 3: Code Review Transfer (Minimal Mode)

**Scenario:** Developer pair-programming session interrupted; needs to continue with different Claude instance tomorrow.

### Generated Artifact

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER — MINIMAL MODE
═══════════════════════════════════════════════════════════════════

**TRANSFER**: Refactoring payment processing module to handle async webhooks correctly

**STATUS**: ↻ iterating

**DECIDED**: Using idempotency keys (UUID v4) stored in Redis because duplicate webhook delivery is common
  - Alternatives rejected: Database-based deduplication (too slow for webhook response time), no deduplication (causes double charges)

**NEXT**: Write tests for race condition where two webhooks arrive simultaneously

**BLOCKED**: Need to set up local Redis for testing (Docker container not running)

**CONTEXT**: E-commerce app processing Stripe payments. Webhook endpoint (/api/webhooks/stripe) sometimes receives duplicate events causing double credits to user accounts. Implemented idempotency layer using Redis (5-min TTL). Refactored webhook handler to check Redis before processing. Code review revealed edge case: two webhooks arriving within milliseconds—Redis GET/SET isn't atomic. Need test coverage before merging PR #847.

**HUMAN PREFS**: Code-first communication | Prefers working tests over theoretical discussion

═══════════════════════════════════════════════════════════════════
Generated: 2025-01-18T17:45:00Z | Session: dev-session-payment-refactor
```

### Receiver Handshake

```
Claude: I've reviewed the transfer. Quick confirmation:
- Mission: Fixing duplicate webhook processing in payment module using Redis idempotency
- Status: Idempotency layer implemented, now need race condition test coverage
- Next: Write tests for simultaneous webhook arrival scenario

Ready to write those tests. Should we use Redis SETNX for atomic check-and-set, or mock the race condition in tests without changing production code?
```

---

## Example 4: Research Synthesis Transfer (Full Mode)

**Scenario:** Week-long research project compiling AI governance frameworks; switching chats to compile final report.

### Generated Artifact (Abbreviated)

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER ARTIFACT v2.0
═══════════════════════════════════════════════════════════════════

───────────────────────────────────────────────────────────────────
§ IMMEDIATE ORIENTATION
───────────────────────────────────────────────────────────────────

**MISSION**
Synthesize 15 AI governance frameworks into actionable recommendations for healthcare org launching diagnostic AI pilot

**STATUS**
Current State: ✓ resolved (research complete)
Progress: Analyzed all 15 frameworks, identified 3 universal principles + 4 healthcare-specific requirements
Momentum: → steady (ready to draft final report)

**NEXT ACTION**
Draft executive summary highlighting 3 universal principles and gap analysis of current practices

───────────────────────────────────────────────────────────────────
§ DECISION LOG
───────────────────────────────────────────────────────────────────

| Decision | Rationale | Alternatives Rejected | Tradeoff Accepted | Type |
|----------|-----------|----------------------|-------------------|------|
| Focus on 3 universal principles (transparency, accountability, fairness) not comprehensive checklist | Exec team needs clear North Star, not 50-item audit | Comprehensive framework (overwhelming), Industry-specific only (misses fundamentals) | Less prescriptive guidance | explicit |
| Prioritize HIPAA alignment over EU AI Act | US healthcare org; HIPAA is law, AI Act is aspirational | EU AI Act first (more rigorous but not binding), Treat equally (dilutes focus) | May need second pass for EU expansion | explicit |

**Decision Principles Applied**: Pareto (20% of principles drive 80% of compliance value)

───────────────────────────────────────────────────────────────────
§ ARTIFACTS & OUTPUTS
───────────────────────────────────────────────────────────────────

**Created**
- Framework Comparison Matrix.xlsx: 15 frameworks x 20 dimensions
- Universal Principles Summary.md: 3 principles appearing in 13+ frameworks
- Healthcare-Specific Requirements.md: 4 additional requirements (patient consent, clinical validation, adverse event reporting, data provenance)
- Gap Analysis (draft): Current practices vs framework recommendations

**Referenced**
- WHO AI Ethics Guidance (2021)
- FDA AI/ML Software as Medical Device guidelines
- NIST AI Risk Management Framework
- [12 other frameworks cataloged in comparison matrix]

───────────────────────────────────────────────────────────────────
§ CRITICAL CONTEXT
───────────────────────────────────────────────────────────────────

**Key Insights**
- [G] Healthcare AI governance is 80% existing medical device regulation + 20% AI-specific (transparency, explainability)
- [C] "Clinical validation" appears in healthcare frameworks but defined inconsistently—some mean accuracy, some mean safety, some mean both
- [P] Transparency is universal principle but operationalization varies wildly (model cards vs audit logs vs patient-facing explanations)

**Constraints**
- Resource: Exec team has 30-min attention span; report must be scannable
- Political/Org: Compliance team wants checklist; Product wants principles
- Ethical: Diagnostic AI has life-or-death implications; can't treat this as "move fast and break things"

**Uncertainty Map**
- Known unknowns: FDA guidance evolving rapidly; recommendations may be outdated in 12 months
- Model weakness: Synthesized from published frameworks; may miss org-specific risks
- Risk factors: If pilot launches without robust adverse event reporting, could face regulatory action

**Values at Stake**
- Patient safety paramount (more important than speed to market)
- Regulatory compliance as floor, not ceiling
- Building trust with clinicians (they're skeptical of AI)

═══════════════════════════════════════════════════════════════════
```

---

## Example 5: Cross-System Transfer (Minimal Mode)

**Scenario:** User wants to continue conversation from Claude.ai web chat in Claude Code for implementation.

### Generated Artifact

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER — MINIMAL MODE
═══════════════════════════════════════════════════════════════════

**TRANSFER**: Designing API rate limiter using token bucket algorithm

**STATUS**: ✓ resolved (design complete, ready to implement)

**DECIDED**: Token bucket with Redis backend because distributed rate limiting across 5 API servers
  - Alternatives rejected: In-memory (doesn't work across servers), Fixed window (allows burst at boundary), Leaky bucket (more complex, same result)

**NEXT**: Implement token bucket in Node.js with Redis, starting with /api/v1/search endpoint (current abuse target)

**BLOCKED**: None

**CONTEXT**: Public API experiencing abuse on search endpoint (1000 req/sec from single IP). Need rate limiting before it impacts paying customers. Decided on token bucket: 100 tokens/min per API key, 10 req/sec burst allowed. Using Redis INCR + TTL for atomic token consumption. User has Redis already running for session storage. Design discussion complete in Claude.ai, now switching to Claude Code for implementation.

**HUMAN PREFS**: Show working code, not pseudocode | TypeScript preferred

═══════════════════════════════════════════════════════════════════
Generated: 2025-01-17T11:30:00Z | Session: web-chat-ratelimit-design
Transfer: Claude.ai → Claude Code
```

### Receiver Handshake (Claude Code)

```
Claude Code: I've reviewed the transfer. Quick confirmation:
- Mission: Implementing token bucket rate limiter with Redis for distributed API protection
- Status: Design finalized (100 tokens/min, 10 req/sec burst), ready to code
- Next: Build token bucket implementation in Node.js/TypeScript for /api/v1/search

Ready to implement. Should I create a new rate-limiter.ts file in your middleware/ directory, or would you prefer a standalone npm package for reusability?
```

---

## Example 6: Iterative Transfer Chain (Minimal Mode → Full Mode)

**Scenario:** Simple task grew complex over 3 transfers; final transfer needs Full mode to preserve accumulated context.

### Transfer 1 (Minimal Mode)

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER — MINIMAL MODE
═══════════════════════════════════════════════════════════════════

**TRANSFER**: Writing blog post about testing strategies

**STATUS**: ⧗ in-progress

**DECIDED**: Focus on unit vs integration testing tradeoffs
  - Alternatives rejected: Comprehensive testing guide (too broad)

**NEXT**: Draft introduction explaining why testing strategy matters

**BLOCKED**: None

**CONTEXT**: Writing for developer audience. Angle: most teams over-index on unit tests, under-invest in integration tests. Want to challenge conventional wisdom.

**HUMAN PREFS**: Conversational tone | Examples over theory

═══════════════════════════════════════════════════════════════════
Generated: 2025-01-19T09:00:00Z | Session: blog-draft-001
```

### Transfer 2 (Minimal Mode)

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER — MINIMAL MODE
═══════════════════════════════════════════════════════════════════

**TRANSFER**: Writing blog post about testing strategies (2nd continuation)

**STATUS**: ⧗ in-progress

**DECIDED**: Add controversial claim: "Unit tests are often waste" because people test private methods instead of behavior
  - Alternatives rejected: Balanced "both are important" take (boring, unoriginal)

**NEXT**: Write section on "What to integration test" with examples

**BLOCKED**: None

**CONTEXT**: Building on Transfer 1. Intro drafted (800 words). Thesis: Unit tests are overrated when they test implementation details instead of behavior; integration tests catch real bugs. Reader feedback: "This is clicking but needs concrete examples." Adding: authentication flow example (unit test mocks miss integration bugs), payment processing (unit tests pass, Stripe integration fails).

**HUMAN PREFS**: Conversational tone | Concrete examples | Challenge conventional wisdom

═══════════════════════════════════════════════════════════════════
Generated: 2025-01-19T14:30:00Z | Session: blog-draft-002
Previous transfer: blog-draft-001
```

### Transfer 3 (Full Mode - Complexity Warrants Upgrade)

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER ARTIFACT v2.0
═══════════════════════════════════════════════════════════════════
Generated: 2025-01-19T18:00:00Z
Session ID: blog-draft-003 | Transfer Type: ○ continuation
Human: Jamie | Domain: Developer content creation
Previous transfers: blog-draft-001, blog-draft-002

───────────────────────────────────────────────────────────────────
§ IMMEDIATE ORIENTATION
───────────────────────────────────────────────────────────────────

**MISSION**
Publish contrarian blog post arguing unit tests are overrated, integration tests undervalued—backed by concrete examples

**STATUS**
Current State: ⧗ in-progress
Progress: 2200 words drafted (intro + 2 examples); need conclusion + title
Momentum: ↑ accelerating (feedback from 3 beta readers very positive)

**NEXT ACTION**
Write conclusion that ties back to thesis without being preachy; suggest title options

───────────────────────────────────────────────────────────────────
§ DECISION LOG
───────────────────────────────────────────────────────────────────

| Decision | Rationale | Alternatives Rejected | Tradeoff Accepted | Type |
|----------|-----------|----------------------|-------------------|------|
| Lead with controversial claim ("unit tests are waste") | Hook readers; challenge groupthink | Balanced "depends on context" (boring) | Will attract criticism | explicit |
| Use 2 detailed examples (auth + payment) not 5 shallow ones | Depth > breadth for persuasion | Survey of 5 quick examples | Longer read time | explicit |
| Include "When unit tests shine" section | Avoid strawman; show nuance | Pure contrarian take | Dilutes spicy thesis | emergent (from beta feedback) |

**Decision Principles Applied**: Surprise (contrarian take), Specificity (concrete examples), Intellectual honesty (acknowledge counterarguments)

───────────────────────────────────────────────────────────────────
§ OPEN LOOPS
───────────────────────────────────────────────────────────────────

**Unresolved Questions**
- [ ] Title options: "Unit Tests Are Overrated" (punchy) vs "Integration Tests Are Underrated" (less confrontational)
- [ ] Should we add code snippets showing test examples, or keep prose-only?

**Pending Inputs**
- [ ] Final beta reader feedback due tomorrow
- [ ] Editor review (Jamie's colleague reviewing for tone)

**Hypotheses to Test**
- [ ] "Controversial title will drive 2x traffic" (can A/B test after publish)

───────────────────────────────────────────────────────────────────
§ ARTIFACTS & OUTPUTS
───────────────────────────────────────────────────────────────────

**Created**
- blog-draft-v3.md: 2200 words (intro + auth example + payment example)
- Beta reader feedback doc: 3 readers, consensus "spicy but fair"

**Referenced**
- Martin Fowler on Test Pyramid (to contrast against)
- Kent Beck tweet thread on "test behavior not implementation"

───────────────────────────────────────────────────────────────────
§ CRITICAL CONTEXT
───────────────────────────────────────────────────────────────────

**Key Insights**
- [G] Beta readers said "auth example" was most persuasive because relatable
- [C] "When unit tests shine" section emerged from feedback—wasn't in original outline
- [P] Conversational tone working well (readers: "sounds like you're talking to me")

**Constraints**
- Resource: Want to publish by Friday (2 days)
- Political/Org: Jamie's company (testing tool vendor) might not love "unit tests overrated" message—keeping anonymous

**Values at Stake**
- Intellectual honesty (acknowledge where unit tests ARE valuable)
- Challenging groupthink (don't water down for likability)
- Helping developers improve craft

───────────────────────────────────────────────────────────────────
§ HUMAN CONTEXT
───────────────────────────────────────────────────────────────────

**Communication Preferences**
- Style: Conversational/exploratory | Appreciates push-back
- Depth: Concrete examples > abstract theory

**Assumed Knowledge**
- Professional developer (10+ years)
- Familiar with testing debates
- Reads Martin Fowler, Kent Beck

**Session Dynamics**
- Trust level: Established (3 transfer chain)
- Collaboration mode: Jamie drafts, Claude refines + challenges
- Sensitive topics: Works for testing tool vendor (keeping blog anonymous)

═══════════════════════════════════════════════════════════════════
§ TRANSFER READY
═══════════════════════════════════════════════════════════════════
Review for accuracy before sharing with the receiving agent.
```

### Receiver Handshake

```
Claude: I've reviewed the transfer chain (3 sessions). Quick confirmation:
- Mission: Publishing contrarian dev blog arguing integration tests > unit tests, backed by auth & payment examples
- Status: 2200 words drafted, need conclusion + title decision
- Next: Write conclusion and propose title options (punchy vs diplomatic)

Ready to wrap this up. For the conclusion—should we end with actionable advice ("here's how to rebalance your testing"), or provocative challenge ("question your assumptions about testing")? And leaning toward "Integration Tests Are Underrated" for title since you're publishing anonymously and can't afford bridge-burning.
```

---

## Key Patterns Across Examples

### When to Use Minimal Mode
- Short-lived tasks (Examples 1, 3, 5, 6-Transfer1)
- Clear next action
- Minimal stakeholder complexity
- Single decision path

### When to Use Full Mode
- Multi-week projects (Example 2, 6-Transfer3)
- Complex stakeholder dynamics
- Multiple decision points
- High uncertainty or risk
- Iterative transfer chains (Example 6)

### Handshake Protocol Importance
Every example shows the receiving agent echoing back:
1. Mission (in their own words)
2. Status
3. Next action

This catches misinterpretation early and builds human confidence in the transfer.

### Evolution Tags in Action
- [G] Genesis: Novel insights ("CFO/Product speak different temporal languages")
- [C] Custom: Emerging patterns ("time to insight" metric)
- [P] Product: Established approaches (token bucket algorithm)
- [K] Commodity: Common knowledge (HIPAA compliance basics)

These tags help the receiving agent understand how much trust to place in each piece of information.
