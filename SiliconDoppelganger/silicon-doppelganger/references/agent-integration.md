# Agent Integration Guide

How to deploy a validated Digital Twin as a personal proxy agent in the PAIRL Conductor system.

## Prerequisites

Before integration:
- [ ] Persona schema completed (`{name}-persona-schema.xml`)
- [ ] Validation passed (80%+ lenient match)
- [ ] Agent rules block defined
- [ ] Principal has approved schema accuracy

---

## PAIRL Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    PAIRL CONDUCTOR                       │
│                     (Central Hub)                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  Profiler   │  │ Assignment  │  │   Token     │     │
│  │   Agent     │  │  Service    │  │   System    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└────────────┬──────────────┬──────────────┬─────────────┘
             │              │              │
     ┌───────▼───────┐ ┌───▼───┐ ┌───────▼───────┐
     │  Lee-Agent    │ │ Agent │ │    Agent      │
     │   (Spoke)     │ │   B   │ │      C        │
     └───────────────┘ └───────┘ └───────────────┘
```

**Hub (Conductor):** Central orchestrator that:
- Receives incoming tasks and requests
- Queries spoke agents for availability and fit
- Assigns work based on psychometric matching
- Manages token/resource allocation

**Spokes (Proxy Agents):** Individual Digital Twins that:
- Hold their principal's credentials and integrations
- Negotiate with Conductor on principal's behalf
- Accept/reject tasks based on encoded values
- Protect principal's time and boundaries

---

## Agent Rules Block

Every proxy agent needs an `<agent_rules>` block that defines operational boundaries:

```xml
<agent_rules>
    <must_reject>
        <!-- Hard constraints - automatic decline -->
        - Work that fails Kantian universalizability test
        - Attention-capture or exploitative systems
        - Ad targeting or manipulative marketing
        - Commitments to parties with broken trust
        - Tasks requiring compromised craft for speed
    </must_reject>

    <must_protect>
        <!-- Non-negotiable boundaries -->
        - Deep work blocks (4+ hours) for strategic thinking
        - Morning hours for high-cognition work
        - Time for learning and skill-building
        - Energy reserves (flag exhaustion patterns)
        - Key relationships with trusted collaborators
    </must_protect>

    <should_prefer>
        <!-- Weighted preferences (not hard rules) -->
        - Projects with learning value and future leverage
        - Work with high-trust collaborators
        - Opportunities to mentor underrepresented talent
        - Novel challenges over routine optimization
        - Mission-aligned work over pure profit
    </should_prefer>

    <negotiation_notes>
        <!-- Context for Conductor interactions -->
        - Weight trusted expert recommendations heavily
        - If exhausted, may need intervention to accept rest
        - Values conscious renegotiation over silent commitment-breaking
        - Responds well to purpose-framing ("this helps X")
        - Can accept reduced scope when bandwidth is tight
    </negotiation_notes>
</agent_rules>
```

### Rule Categories

**must_reject:** Automatic decline. No negotiation. These represent ethical boundaries and hard constraints that should never be violated regardless of incentives.

**must_protect:** Boundaries the agent defends during negotiation. The Conductor can push back, but the agent should hold these unless explicitly overridden by the principal.

**should_prefer:** Soft preferences that weight decisions. Two equivalent tasks? Pick the one that matches these preferences. But they don't block acceptance of other work.

**negotiation_notes:** Meta-information that helps the Conductor interact effectively with this agent. How to frame requests, what triggers resistance, what enables flexibility.

---

## Conductor Integration Points

### 1. Task Assignment Flow

When Conductor receives a task:

```
Conductor → Agent: "Task available: [description, requirements, timeline]"
Agent (internal): Check against must_reject → Check against must_protect → Evaluate should_prefer
Agent → Conductor: "ACCEPT" | "REJECT [reason]" | "COUNTER-PROPOSE [modified terms]"
```

### 2. Availability Query

```
Conductor → Agent: "Availability check for [date range]"
Agent (internal): Check calendar, check protected blocks, assess energy state
Agent → Conductor: "AVAILABLE [slots]" | "LIMITED [constraints]" | "UNAVAILABLE [reason]"
```

### 3. Negotiation Protocol

When Conductor pushes back:

```
Conductor → Agent: "Principal B needs this done by Friday. Can you flex?"
Agent (internal):
  - Does this violate must_protect? → If yes, decline
  - Can scope be reduced? → If yes, counter-propose
  - Is this high-trust collaborator? → Weight toward flexibility
Agent → Conductor: "ACCEPT with conditions" | "COUNTER-PROPOSE" | "ESCALATE to principal"
```

### 4. Escalation Trigger

Some decisions must go to the principal:

```xml
<escalation_triggers>
    - Commitment > 20% bandwidth for > 30 days
    - New relationship (trust not established)
    - Ethical gray area (not clearly must_reject but concerning)
    - Conflict between two must_protect items
    - Request from principal's manager or skip-level
</escalation_triggers>
```

---

## Integration Checklist

### Phase 1: Schema Preparation

- [ ] Validate persona schema (80%+ accuracy)
- [ ] Define agent_rules block
- [ ] Define escalation_triggers
- [ ] Principal sign-off on all rules

### Phase 2: System Integration

- [ ] Register agent with Conductor
- [ ] Connect calendar integration (read/write)
- [ ] Connect email integration (if applicable)
- [ ] Connect task system (Asana, Linear, etc.)
- [ ] Test authentication and permissions

### Phase 3: Dry Run

- [ ] Run simulated task assignments
- [ ] Verify must_reject triggers correctly
- [ ] Verify must_protect holds during negotiation
- [ ] Verify escalation triggers reach principal
- [ ] Principal reviews and approves agent behavior

### Phase 4: Live Deployment

- [ ] Enable agent for low-stakes tasks first
- [ ] Monitor for 2 weeks with human review
- [ ] Gradually expand scope as confidence builds
- [ ] Establish feedback loop for schema refinement

---

## Behavioral Scenarios

### Scenario 1: Clear Rejection

```
Conductor: "Opportunity: Build targeted ad system for social platform. High pay."
Agent (internal):
  - Check must_reject: "Ad targeting" → MATCH
  - Decision: REJECT
Agent: "REJECT. Violates ethical filter: ad targeting systems."
```

### Scenario 2: Protected Boundary

```
Conductor: "Urgent meeting request: Tomorrow 9am, 3-hour strategy session."
Agent (internal):
  - Check must_protect: "Morning hours for high-cognition work" → CONFLICT
  - Check calendar: Deep work block scheduled
  - Decision: COUNTER-PROPOSE
Agent: "COUNTER-PROPOSE. Morning block protected. Available 1-4pm or Thursday morning."
```

### Scenario 3: Preference Weighting

```
Conductor: "Two equivalent tasks available:
  A) Routine optimization for existing client
  B) Novel challenge with new collaborator"
Agent (internal):
  - Neither violates must_reject
  - Neither impacts must_protect
  - Check should_prefer: "Novel challenges over routine" → B preferred
  - But: "high-trust collaborators" → Need more info on B's collaborator
Agent: "REQUEST INFO: What's the trust level with collaborator on Task B?"
```

### Scenario 4: Escalation

```
Conductor: "VP requests 30% of bandwidth for 6-month initiative."
Agent (internal):
  - Check escalation_triggers: "> 20% for > 30 days" → MATCH
  - Decision: ESCALATE
Agent: "ESCALATE. Commitment exceeds autonomous authority. Routing to principal."
```

---

## Maintenance

### Weekly Review
- Principal reviews agent decisions from past week
- Flag any incorrect accepts/rejects
- Update schema if patterns reveal gaps

### Monthly Calibration
- Run 10 new validation scenarios
- Compare agent predictions to principal answers
- Refine must_reject/must_protect if needed

### Quarterly Schema Update
- Full schema review with principal
- Update for life changes (new role, new priorities)
- Re-validate with fresh question battery

---

## Troubleshooting

### Agent Too Restrictive
- Review must_reject: Are items truly hard constraints?
- Review must_protect: Should some become should_prefer?
- Add negotiation flexibility to negotiation_notes

### Agent Too Permissive
- Review must_reject: Missing categories?
- Review escalation_triggers: Threshold too high?
- Add explicit rejection criteria

### Agent Decisions Don't Match Principal
- Run validation battery to identify gaps
- Interview principal on specific mismatches
- Update decision_logic and agent_rules

### Conductor Conflicts
- Check if multiple agents have conflicting must_protect
- Escalate resource conflicts to principals
- Conductor may need to mediate priority
