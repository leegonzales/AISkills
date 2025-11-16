# Context Continuity Guide

Detailed usage examples and workflows for effective context transfer between AI agents.

---

## Table of Contents

1. [Understanding the Two Modes](#understanding-the-two-modes)
2. [When to Transfer Context](#when-to-transfer-context)
3. [Minimal Mode Deep Dive](#minimal-mode-deep-dive)
4. [Full Mode Deep Dive](#full-mode-deep-dive)
5. [The Handshake Protocol](#the-handshake-protocol)
6. [Evolution Tags Explained](#evolution-tags-explained)
7. [Decision Taxonomy](#decision-taxonomy)
8. [Common Scenarios](#common-scenarios)
9. [Troubleshooting](#troubleshooting)

---

## Understanding the Two Modes

### Minimal Mode (~200 words)

**Use when:**
- Task is straightforward with clear next action
- Single or simple decision path
- Short-lived work (hours to days)
- Minimal stakeholder complexity
- Emergency pivot requiring quick capture

**Structure:**
```
TRANSFER: [One-sentence mission]
STATUS: [Symbol + state]
DECIDED: [Decision + rationale + alternatives rejected]
NEXT: [Immediate action]
BLOCKED: [If anything preventing progress]
CONTEXT: [1-2 para critical background]
HUMAN PREFS: [Communication style]
```

**Generation time:** Instant (no reference file reads needed)

### Full Mode (~1000 words)

**Use when:**
- Complex strategic work with multiple decision points
- Long-running project (weeks to months)
- Significant stakeholder dynamics
- High uncertainty or risk
- Multiple open loops requiring tracking
- Iterative transfer chain (3+ transfers)

**Structure:** 8 sections (see artifact-template.md)

**Generation time:** 2-3 minutes (includes context analysis)

### Decision Flow

```
User requests transfer
         ↓
    Claude asks:
    "Minimal or Full?"
         ↓
    ┌─────────┴─────────┐
    │                   │
Minimal              Full
(80% of cases)   (20% of cases)
    │                   │
    ↓                   ↓
Generate            Analyze conversation
immediately         Extract 8 sections
    │                   │
    └─────────┬─────────┘
              ↓
    Present artifact
         Ask: "Which section
         to expand?"
              ↓
    Human reviews & refines
              ↓
    § TRANSFER READY
              ↓
    Paste to new agent
              ↓
    Handshake confirmation
```

---

## When to Transfer Context

### Explicit Transfer Intent

The skill triggers when you say:
- "Transfer this conversation"
- "Create a handoff artifact"
- "Continue this in another chat"
- "Handoff to new session"
- "I need to switch to Claude Code"
- "Summarize for transfer"

### Proactive Transfer Situations

Consider transferring when:

**Context Window Pressure**
- Approaching 180K+ tokens
- Claude's responses getting slower
- Want fresh context for new phase of work

**System Switching**
- Claude.ai → Claude Code (for implementation)
- Claude Code → Claude.ai (for strategic discussion)
- Claude → Other AI (with handshake protocol)

**Work Interruptions**
- Unexpected meeting/call
- End of workday with incomplete work
- Need to delegate to teammate

**Phase Transitions**
- Research phase complete → Implementation begins
- Design approved → Execution starts
- Problem diagnosed → Solution needed

**Quality Maintenance**
- Conversation meandering/losing focus
- Too many tangents diluting context
- Want clean slate with preserved state

---

## Minimal Mode Deep Dive

### Anatomy of a Minimal Transfer

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER — MINIMAL MODE
═══════════════════════════════════════════════════════════════════

**TRANSFER**: Implementing OAuth2 authentication for mobile app

**STATUS**: ⧗ in-progress

**DECIDED**: Using PKCE flow (not implicit grant) because mobile apps can't keep secrets secure
  - Alternatives rejected: Implicit grant (deprecated for mobile), Password grant (requires storing credentials)

**NEXT**: Implement token refresh mechanism with 15-minute expiry window

**BLOCKED**: Need to test with iOS Simulator (currently unavailable)

**CONTEXT**: Building React Native app with Node.js backend. User has security requirements: no tokens in localStorage, must support offline mode, HIPAA compliance needed. Already implemented login flow with access tokens (15-min expiry). Refresh tokens stored in secure storage (iOS Keychain / Android Keystore). Backend validates tokens using JWT verification middleware.

Architecture: React Native (frontend) → Express API (backend) → PostgreSQL (user data)

**HUMAN PREFS**: Code-first communication | TypeScript preferred | Security-conscious

═══════════════════════════════════════════════════════════════════
Generated: 2025-01-20T14:23:00Z | Session: mobile-auth-impl-v1
```

### Field-by-Field Breakdown

**TRANSFER**
- One clear sentence
- What + why it matters (optional)
- Example: "Building payment processing system for e-commerce platform"

**STATUS**
- Use symbols for scannability:
  - ✓ resolved (work complete, just needs handoff)
  - ⧗ in-progress (actively working)
  - ⚠ blocked (stuck on dependency/decision)
  - ↻ iterating (multiple rounds of refinement)

**DECIDED**
- Key decision + rationale (use "because")
- Alternatives rejected (prevents rehashing)
- If multiple decisions, bullet list:
  ```
  - Use Redis for caching because sub-millisecond latency required
  - Deploy to US-East region because 80% of users are East Coast
  ```

**NEXT**
- Immediate next action (not vague "continue working")
- Bad: "Keep implementing auth"
- Good: "Implement token refresh mechanism with 15-minute expiry window"

**BLOCKED**
- If nothing blocking: "None"
- If blocked, state what + why:
  - "Waiting for API key from vendor (requested Monday)"
  - "Need design approval from Sarah before proceeding"

**CONTEXT**
- 1-2 paragraphs of critical background
- Include: constraints, architecture, key insights, what's already done
- Think: "What does receiving agent need to avoid stupid mistakes?"

**HUMAN PREFS**
- Communication style (direct/exploratory, technical/narrative)
- Code preferences (TypeScript/Python, verbose/concise)
- Domain expertise (can assume knowledge of X)

### When Minimal Mode Isn't Enough

Upgrade to Full mode if:
- Your CONTEXT paragraph exceeds 3 paragraphs
- More than 3-4 significant decisions
- Multiple open loops (3+ unresolved questions)
- High uncertainty requiring explicit mapping
- Stakeholder complexity (political/org constraints)

---

## Full Mode Deep Dive

### When to Choose Full Mode

Full mode shines for:

**Complex Strategic Work**
- Multi-week AI transformation projects
- Organizational change initiatives
- Product strategy development with multiple stakeholders

**High-Stakes Decisions**
- Regulatory compliance work (healthcare, finance)
- Security architecture decisions
- Architectural choices with long-term consequences

**Research Synthesis**
- Compiling multiple sources into recommendations
- Gap analysis across frameworks
- Literature reviews for decision-making

**Iterative Project Work**
- Long-running development projects
- Continuous research → implementation cycles
- Projects with 3+ transfer chains

### The 8 Sections Explained

**§ IMMEDIATE ORIENTATION** [Critical - Always Read First]

Mission, status, next action. If truncation occurs, this survives.

```markdown
**MISSION**
Design measurement framework for AI ROI that satisfies CFO (hard metrics) and Product (learning signals)

**STATUS**
Current State: ⧗ in-progress
Progress: Framework designed, validating with stakeholders
Momentum: ↓ stalled (waiting for CFO feedback)

**NEXT ACTION**
Schedule 30-min CFO sync before Friday board meeting
```

**§ DECISION LOG** [Anti-Rehash Protection]

Prevents receiving agent from re-opening settled debates.

| Decision | Rationale | Alternatives Rejected | Tradeoff Accepted | Type |
|----------|-----------|----------------------|-------------------|------|
| Two-tier metrics (North Star + Leading) | CFO needs quarterly; Product needs weekly | Single dashboard (can't bridge time horizons) | More complex tracking | explicit |

Tag with type:
- **explicit** = deliberate choice
- **implicit** = started doing without formal decision
- **emergent** = pattern that evolved

**§ OPEN LOOPS** [Forward Momentum]

What needs attention:

```markdown
**Unresolved Questions**
- [ ] How attribute revenue when AI is one input among many?

**Blockers**
- [ ] CFO hasn't responded (sent Mon, need Thu)

**Pending Inputs**
- [ ] Pilot team selections from VP Eng (promised Wed)

**Hypotheses to Test**
- [ ] Leading indicators will predict ROI with >70% accuracy
```

**§ ARTIFACTS & OUTPUTS** [What Exists]

```markdown
**Created**
- Measurement Framework v2.pdf: Two-tier approach with 5 North Star + 12 leading indicators
- CFO Memo (draft): One-pager on why ROI takes 2 quarters

**Referenced**
- Gartner AI ROI Report 2024: Industry benchmark (18-month payback)

**Tools Used**
- Wardley Mapping: Positioned metrics on evolution axis
```

**§ CRITICAL CONTEXT** [Interpretive Layer]

Why things matter, not just what happened.

```markdown
**Key Insights** [with evolution tags]
- [G] CFO and Product speak different temporal languages—bridge requires dual metrics
- [C] "Time to insight" emerged as universal metric (not initially proposed)

**Constraints**
- Technical: Telemetry only tracks API calls, not workflows
- Resource: $15K budget cap; 2-week deadline
- Political/Org: CFO skeptical of "soft metrics"
- Ethical: Measure outcomes, not keystrokes (avoid surveillance)

**Uncertainty Map**
- Known unknowns: Can we instrument "time to insight" without custom builds?
- Model weakness: Assuming leading → lag correlation (unproven)

**Values at Stake**
- Intellectual honesty (refuse premature ROI claims)
- Team autonomy (metrics that help improve, not just justify)
```

**§ HUMAN CONTEXT** [Receiving Agent Calibration]

```markdown
**Communication Preferences**
- Style: Strategic/exploratory with tactical grounding
- Depth: Detailed analysis with executive summaries
- Archetypes: @strategist, @cartographer, @ethicist

**Assumed Knowledge**
- Deep OODA, Wardley, Cynefin frameworks
- Product management background

**Session Dynamics**
- Trust: Established (3rd conversation)
- Mode: Co-creation (Alex proposes, Claude stress-tests)
- Sensitive: Past initiatives failed; team skeptical
```

**§ CONVERSATION HISTORY** [Optional Depth]

Use `<details>` tag for collapsibility:

```markdown
<details>
<summary>Expand for full narrative</summary>

**Act I: Problem Formation** [messages 1-15]
Started with "Board wants ROI, nothing to show." Pivoted from quick wins to long-term credibility.

**Act II: Exploration** [messages 16-45]
Interviewed stakeholders. Discovered temporal mismatch. "Time to insight" emerged organically.

**Act III: Current State** [messages 46-now]
Framework designed, stalled on CFO buy-in. Need sync before Friday.

**Quotable Moments**
- "I'd rather tell board 'we don't know yet' than make up numbers"
</details>
```

**§ TRANSFER METADATA** [System Level]

```markdown
**Provenance**: Claude Sonnet 4.5 | Session project-ai-001
**Context Window Pressure**: ● constrained (165K tokens)
**Completeness**: [█████████░] 90% — missing detailed pilot criteria
**Verification**: ✓ human reviewed

**Handoff Notes**
- CFO response is critical path
- "Time to insight" depends on 2-week instrumentation build
```

---

## The Handshake Protocol

### Why Handshakes Matter

**Problem:** Receiving agent misinterprets artifact → wastes time on wrong work

**Solution:** Force echo-back of mission/status/next before continuing

### Handshake Template

```
I've reviewed the transfer. Quick confirmation:
- Mission: [Echo in YOUR OWN WORDS]
- Status: [Echo current state]
- Next: [Echo immediate next action]

Ready to [next action]. What's your priority?
```

### Example Handshake (Good)

```
User: [Pastes artifact about JWT authentication]

Claude: I've reviewed the transfer. Quick confirmation:
- Mission: Implementing PKCE OAuth2 flow for React Native app with security-first approach
- Status: Login flow working, now need token refresh before 15-min expiry
- Next: Build automatic token refresh mechanism using secure storage

Ready to implement the refresh logic. Should we use silent refresh (automatic) or prompt user when token nears expiry?
```

**Why this works:**
- Echoes mission in own words (not verbatim)
- Confirms understanding of status
- Shows next action is clear
- Asks clarifying question showing engagement

### Example Handshake (Bad)

```
Claude: Got it! I can see from the context transfer artifact that you're working on authentication. Let me help you implement the OAuth2 flow.
```

**Why this fails:**
- No confirmation of understanding
- Meta-commentary about artifact (should be invisible)
- Doesn't echo mission/status/next
- No clarifying question

### For Generating Agents

After presenting artifact, explicitly instruct receiving agent:

"The receiving agent should confirm understanding with:
- Mission: [echo in own words]
- Status: [echo current state]
- Next: [echo next action]

Then ask a clarifying question before continuing."

---

## Evolution Tags Explained

Evolution tags ([G/C/P/K]) track information maturity using Wardley-inspired concepts.

### The Four Stages

**[G] Genesis** - Novel, first-time discovery
- Insights that weren't obvious at conversation start
- "Aha!" moments that reframed the problem
- Discoveries that changed direction

Examples:
- [G] CFO and Product teams speak different temporal languages
- [G] Unit tests are actually testing implementation, not behavior
- [G] "Time to insight" metric everyone cares about but no one proposed

**[C] Custom** - Emerging pattern, still validating
- Hypotheses being tested
- Patterns appearing but not yet proven
- Approaches that might work but need validation

Examples:
- [C] Leading indicators may predict lag metrics with >70% accuracy
- [C] Token bucket algorithm seems to handle burst traffic better than leaky bucket
- [C] Minimal mode sufficient for 80% of transfers (hypothesis, testing)

**[P] Product** - Established approach, proven
- Techniques that worked reliably
- Validated hypotheses now considered fact
- Reproducible patterns

Examples:
- [P] PKCE flow is standard for mobile OAuth2
- [P] Redis caching reduces latency from 100ms to 5ms
- [P] Wardley mapping helps position metrics on evolution axis

**[K] Commodity** - Common knowledge, standard practice
- Industry best practices
- Well-established patterns
- "Everyone knows this" territory

Examples:
- [K] HIPAA requires data encryption at rest and in transit
- [K] JWT tokens should be short-lived (15-min typical)
- [K] Git commit messages should be descriptive

### Why Tags Matter

**For receiving agents:**
- [G] insights: Treat carefully, may shift strategy
- [C] patterns: Test assumptions before relying on
- [P] approaches: Trust but verify in new context
- [K] knowledge: Accept as baseline, focus on novel work

**For humans:**
- Quickly scan what's new ([G]) vs what's established ([P]/[K])
- Identify which insights to preserve vs which to revisit
- Understand what receiving agent can take for granted

### Tagging Guidelines

**When to use [G]:**
- Insight surprised you
- Reframed how you think about problem
- Emerged from conversation, wasn't planned

**When to use [C]:**
- Pattern seems promising but untested
- Hypothesis you're validating
- Approach that's custom to this situation

**When to use [P]:**
- Technique worked reliably multiple times
- Validated hypothesis now treated as fact
- Would recommend to others in similar situation

**When to use [K]:**
- Industry standard practice
- Well-documented best practice
- "Everyone knows" territory

**When in doubt:** Use [C] (Custom). Better to be conservative about maturity.

### Alternative Tag System (Simplified)

If the Wardley-inspired [G/C/P/K] tags feel unfamiliar, you can use this simpler alternative:

**[New]** - Novel discovery or insight
- Replaces [G] Genesis
- Something you learned during this conversation
- Wasn't obvious at the start

**[Developing]** - Emerging pattern being validated
- Replaces [C] Custom
- Hypothesis you're testing
- Seems promising but unproven

**[Stable]** - Proven approach, works reliably
- Replaces [P] Product
- Validated through use
- Would recommend to others

**[Standard]** - Common knowledge, best practice
- Replaces [K] Commodity
- Industry standard
- Well-documented pattern

**Example comparison:**

Using Wardley tags:
```markdown
**Key Insights**
- [G] CFO and Product speak different temporal languages
- [C] "Time to insight" metric emerged as universal bridge
- [P] PKCE flow standard for mobile OAuth2
- [K] JWT tokens should be short-lived (15-min typical)
```

Using simplified tags:
```markdown
**Key Insights**
- [New] CFO and Product speak different temporal languages
- [Developing] "Time to insight" metric emerged as universal bridge
- [Stable] PKCE flow standard for mobile OAuth2
- [Standard] JWT tokens should be short-lived (15-min typical)
```

Both systems convey the same information. **Choose whichever feels more natural to you.** The receiving agent will understand either system.

**Consistency note:** Pick one system and stick with it throughout the artifact. Don't mix [G] and [New] in the same transfer.

### Tool State Tag [T]

**[T] Tool/Environment State** - Captures active tool or environment context

Optional tag for power users working in Claude Code or environments with active tools/services. Use sparingly—only when tool state is critical to resume work.

**When to use [T]:**
- Active development environment needs to be restored
- Specific tools/services are running and required
- File/repo state is critical context
- Database connections or schemas matter

Examples:
- [T] Git: feature/auth-flow branch, 3 uncommitted files in src/
- [T] Python REPL: pandas/numpy loaded, df from data.csv (500K rows)
- [T] Redis: localhost:6379 connected, 1.2M keys, 'session:*' pattern
- [T] Docker: postgres:14 container running on port 5432
- [T] VSCode: workspace /Users/alex/projects/api-redesign, 4 terminal tabs open

**Usage in artifacts:**

```markdown
**Key Insights** [with evolution and tool tags]
- [G] CFO and Product speak different temporal languages
- [C] "Time to insight" metric emerged as universal bridge
- [T] Git: main branch, src/metrics.py modified (uncommitted)
- [T] Postgres: metrics_dev database, 3 test tables populated
```

**Guidelines:**
- Only include if tool state is **non-obvious** or **hard to recreate**
- Omit standard setup (e.g., "Node.js installed")
- Be specific about versions if they matter (e.g., "Python 3.11.2")
- Include connection strings without secrets (e.g., "localhost:5432" not credentials)

**When NOT to use [T]:**
- Standard development setup everyone has
- Tools mentioned in § ARTIFACTS & OUTPUTS
- State that's obvious from file context
- Information already in § CRITICAL CONTEXT → Constraints

---

## Decision Taxonomy

### The Three Types

**Explicit** - Deliberate choice with clear rationale

Characteristics:
- Discussed alternatives
- Clear "because" reasoning
- Documented tradeoffs

Example:
```
Decision: Use PostgreSQL instead of MongoDB
Rationale: Need ACID transactions for payment processing
Alternatives rejected: MongoDB (eventual consistency too risky)
Tradeoff: Slightly more complex schema design
Type: explicit
```

**Implicit** - Started doing without formal decision

Characteristics:
- No deliberate choice point
- "Just started using X"
- Became default without discussion

Example:
```
Decision: Using OODA loops for strategic framing
Rationale: Started applying it naturally; fits user's thinking style
Alternatives rejected: N/A (not formally considered)
Tradeoff: Assumes user knows OODA framework
Type: implicit
```

**Emergent** - Pattern that evolved over conversation

Characteristics:
- Emerged organically
- Pattern recognized in retrospect
- Became load-bearing without planning

Example:
```
Decision: "Time to insight" as key metric
Rationale: Emerged from stakeholder interviews; everyone lit up when named
Alternatives rejected: Initially proposed "AI adoption %" (vanity metric)
Tradeoff: Harder to instrument than usage counts
Type: emergent
```

### Why Taxonomy Matters

**Prevents fabrication:** Don't create post-hoc rationale for emergent decisions. Mark them honestly as "emergent" and explain how they evolved.

**Signals confidence:** Explicit decisions are deliberate; implicit/emergent may need revisiting.

**Helps receiving agent:** Knows which decisions to treat as settled vs open to reconsideration.

---

## Common Scenarios

### Scenario 1: Context Window Approaching Limit

**Situation:** At 175K tokens, responses slowing, want fresh start

**Recommended:** Full mode (preserve all context)

**Workflow:**
1. Request transfer: "We're near context limit, create comprehensive handoff"
2. Claude generates Full mode artifact
3. Review § Decision Log carefully (most critical to preserve)
4. Paste to fresh chat
5. Wait for handshake before continuing

### Scenario 2: Quick Code Task Handoff

**Situation:** Implementing feature, need to switch to different Claude instance

**Recommended:** Minimal mode

**Workflow:**
1. Request: "Transfer this to Claude Code"
2. Claude asks mode preference → choose Minimal
3. Review DECIDED and NEXT fields
4. Paste to Claude Code
5. Continue implementation

### Scenario 3: Research → Implementation Transition

**Situation:** Finished research phase, ready to build

**Recommended:** Full mode (bridge knowledge gap between phases)

**Workflow:**
1. Request: "Create comprehensive handoff for implementation"
2. Include § Artifacts & Outputs (research findings)
3. § Critical Context captures key insights from research
4. § Decision Log documents framework choices
5. Paste to implementation agent

### Scenario 4: Team Handoff

**Situation:** Delegating work to colleague

**Recommended:** Full mode + customization

**Workflow:**
1. Generate Full mode artifact
2. Enhance § Human Context with colleague's background
3. Add § Stakeholder Map if political complexity
4. Redact sensitive information
5. Send to colleague who pastes to their Claude

### Scenario 5: Emergency Pivot

**Situation:** Conversation derailed, need to restart with focus

**Recommended:** Minimal mode (speed matters)

**Workflow:**
1. Request: "Quick transfer—conversation went off track"
2. Minimal mode captures essentials
3. Start fresh chat immediately
4. Use handshake to confirm direction
5. Maintain focus on NEXT action

---

## Troubleshooting

### Receiving Agent Doesn't Understand Artifact

**Symptoms:**
- Asks questions answered in artifact
- Proposes approaches rejected in Decision Log
- Ignores Open Loops

**Solutions:**
1. Point to specific section: "Check § Decision Log—we rejected that approach"
2. Paste receiver-prompt.md prepend for guidance
3. Request handshake explicitly: "Confirm you understand mission/status/next"
4. If still confused, simplify: Extract key points manually

### Artifact Too Long

**Symptoms:**
- Exceeds 1500 words
- Takes >5 minutes to read
- Human overwhelmed reviewing

**Solutions:**
1. Use Minimal mode instead
2. Collapse § Conversation History using `<details>` tag
3. Trim less critical sections
4. Focus on § Immediate Orientation + § Decision Log + § Open Loops

### Artifact Too Brief

**Symptoms:**
- Receiving agent asks obvious questions
- Missing critical context
- Decisions not explained

**Solutions:**
1. Upgrade Minimal → Full mode
2. Expand CONTEXT section with more background
3. Add evolution tags to insights
4. Include Alternatives Rejected in DECIDED

### Transfer Feels Mechanical

**Symptoms:**
- Receiving agent says "I can see from the artifact..."
- Loses conversational flow
- Feels like reading documentation

**Solutions:**
1. Receiving agent should integrate naturally: "Picking up where we left off..."
2. Don't mention artifact in conversation
3. Use handshake to confirm understanding, then continue naturally
4. Human: Give receiving agent immediate task to engage with

### Multiple Transfers in Chain

**Symptoms:**
- Context degrading across 3+ transfers
- Information loss accumulating
- Evolution tags becoming unclear

**Solutions:**
1. Reference previous artifacts in § Conversation History
2. Consolidate decision log across transfers
3. Update evolution tags as patterns mature
4. Consider single comprehensive transfer instead of iterative chain

### Sensitive Information in Artifact

**Symptoms:**
- API keys, passwords in CONTEXT
- Stakeholder names that should be redacted
- Proprietary information

**Solutions:**
1. Review artifact before pasting
2. Redact: Replace with [REDACTED] or generic descriptions
3. Use § Handoff Notes to warn: "Contains sensitive info—verify before sharing"
4. Consider separate secure channel for sensitive context

---

## Summary

**Two Modes:**
- Minimal (80%): Fast, ~200 words, essentials only
- Full (20%): Comprehensive, ~1000 words, complex transfers

**Core Principles:**
- Antifragile structure (critical info first)
- Dual interface (human + machine readable)
- Forced engagement (ask "which section to expand?")
- Handshake protocol (confirm understanding before continuing)

**Key Practices:**
- Tag insights with evolution stage [G/C/P/K]
- Classify decisions (explicit/implicit/emergent)
- Validate artifacts before pasting
- Integrate naturally (don't mention artifact in conversation)

**When in Doubt:**
- Choose Minimal mode first
- Upgrade to Full if complexity warrants
- Ask receiving agent for handshake
- Point to specific sections if confusion arises

For real-world examples, see [context-continuity/references/examples.md](context-continuity/references/examples.md).

For design rationale, see [Context Continuity Analysis.md](Context%20Continuity%20Analysis.md).
