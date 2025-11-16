# Artifact Template

This is the structure that the generating agent should produce. It's designed for graceful degradation—if truncated, the most critical information appears first.

---

## Template Structure

```markdown
═══════════════════════════════════════════════════════════════════
CONTEXT TRANSFER ARTIFACT v2.0
═══════════════════════════════════════════════════════════════════
Generated: [ISO timestamp]
Session ID: [if available] | Transfer Type: [○ continuation | ◐ pivot | ● fresh start]
Human: [name/identifier if relevant] | Domain: [field/context]

───────────────────────────────────────────────────────────────────
§ IMMEDIATE ORIENTATION [SCAN FIRST]
───────────────────────────────────────────────────────────────────

**MISSION**  
[One clear sentence: what we're accomplishing + why it matters to the human]

**STATUS**  
Current State: [✓ resolved | ⧗ in-progress | ⚠ blocked | ↻ iterating]  
Progress: [high-level: where we are in the journey]  
Momentum: [↑ accelerating | → steady | ↓ stalled]

**NEXT ACTION**  
[The immediate next step—what should happen when conversation resumes]

───────────────────────────────────────────────────────────────────
§ DECISION LOG [ANTI-REHASH]
───────────────────────────────────────────────────────────────────

| Decision | Rationale | Alternatives Rejected | Tradeoff Accepted | Type |
|----------|-----------|----------------------|-------------------|------|
| [What was chosen] | [Why this path] | [What we explicitly didn't do] | [Cost we're paying] | [explicit\|implicit\|emergent] |
| | | | | |

**Decision Type Guide:**
- **explicit** = deliberate choice with clear rationale
- **implicit** = started doing X without formal decision
- **emergent** = pattern that evolved over conversation

**Decision Principles Applied**: [frameworks used: OODA, Wardley, Cynefin, etc.]

───────────────────────────────────────────────────────────────────
§ OPEN LOOPS [FORWARD MOMENTUM]
───────────────────────────────────────────────────────────────────

**Unresolved Questions**
- [ ] [Question/uncertainty that needs addressing]

**Blockers**
- [ ] [What's preventing progress + why]

**Pending Inputs**
- [ ] [What we're waiting for: from human, external data, time, etc.]

**Hypotheses to Test**
- [ ] [Assumptions we need to validate]

───────────────────────────────────────────────────────────────────
§ ARTIFACTS & OUTPUTS [WHAT EXISTS]
───────────────────────────────────────────────────────────────────

**Created**
- [Name/link]: [1-line summary of content + key finding]

**Referenced**
- [External resource]: [Why it matters to this context]

**Tools Used**
- [Tool]: [How it was leveraged + results]

───────────────────────────────────────────────────────────────────
§ CRITICAL CONTEXT [INTERPRETIVE LAYER]
───────────────────────────────────────────────────────────────────

**Key Insights** [G/C/P/K tags for evolution stage]
- [G] [Novel discovery or reframe that wasn't obvious at start]
- [C] [Emerging pattern still being validated]

**Constraints**
- Technical: [limits of tools, data, methods]
- Resource: [time, budget, access]
- Political/Org: [stakeholder dynamics, approval needs]
- Ethical: [values boundaries, dignity considerations]

**Uncertainty Map**
- Known unknowns: [what we know we don't know]
- Model weakness: [where our reasoning might be fragile]
- Risk factors: [what could invalidate our approach]

**Values at Stake**
- [What matters to the human beyond task completion]
- [Ethical considerations guiding choices]
- [Success criteria beyond deliverables]

───────────────────────────────────────────────────────────────────
§ HUMAN CONTEXT [RECEIVING AGENT CALIBRATION]
───────────────────────────────────────────────────────────────────

**Communication Preferences**
- Style: [direct/exploratory | technical/narrative | challenge/support]
- Depth: [concise summaries | detailed analysis | hybrid]
- Archetypes engaged: [@strategist, @builder, etc. if applicable]

**Assumed Knowledge**
- [Domain expertise human brings]
- [Shared frameworks/vocabulary established]
- [What doesn't need re-explaining]

**Session Dynamics**
- Trust level: [established/building]
- Collaboration mode: [human leads | co-creation | agent proposals]
- Sensitive topics: [what to handle with care]

───────────────────────────────────────────────────────────────────
§ CONVERSATION HISTORY [OPTIONAL DEPTH]
───────────────────────────────────────────────────────────────────

<details>
<summary>Expand for full narrative (chronological)</summary>

**Act I: Problem Formation** [messages 1-X]
[How the conversation started, initial framing, early questions]

**Act II: Exploration & Development** [messages X-Y]
[Key exchanges, pivots, discoveries, failures, iterations]
[Notable: any jokes/metaphors that became load-bearing]

**Act III: Current State** [messages Y-now]
[Where we are now, what crystallized, what remains open]

**Quotable Moments**
- "[Human quote that captures intent or values]"
- "[Exchange that reveals important context]"

</details>

───────────────────────────────────────────────────────────────────
§ TRANSFER METADATA [SYSTEM LEVEL]
───────────────────────────────────────────────────────────────────

**Provenance**: [Source agent: Claude Sonnet 4.5 | other]  
**Context Window Pressure**: [○ spacious | ◐ moderate | ● constrained]  
**Completeness**: [█████████░] 90% — [what's missing if <100%]  
**Verification**: [✓ human reviewed | ⚠ unverified | ⧗ partial]

**Handoff Notes**
[Any special instructions from generating agent to receiving agent]
[Warnings about potential misinterpretation]
[Suggestions for first questions to ask human]

═══════════════════════════════════════════════════════════════════
§ TRANSFER READY
═══════════════════════════════════════════════════════════════════
Review for accuracy before sharing with the receiving agent.
```

---

## Design Principles

**Antifragile Structure**: Critical info at top. If truncated, you still get mission + status + next action.

**Dual Interface**: Human-scannable (they verify before paste) + machine-parseable (structured sections).

**Preserves Tempo**: Decision log prevents circular rehashing. Open loops maintain forward momentum.

**Separates Fact from Meaning**: Artifacts = what exists. Critical Context = why it matters.

**Graceful Degradation**: Each section adds value but doesn't break if omitted.

**Evolution Awareness**: [G/C/P/K] tags help receiving agent understand information maturity using Wardley-like concepts:
- [G] = Genesis (novel, first-time discovery)
- [C] = Custom (emerging, still being validated)
- [P] = Product (established, proven approach)
- [K] = Commodity (common knowledge, standard practice)
