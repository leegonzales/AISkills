---
name: silicon-doppelganger
description: Create psychometrically accurate Digital Twins of business principals to forecast outcomes, team dynamics, and strategic alignment. Use when building team simulations, predicting partnership friction, or testing decisions against personality profiles.
---

# Silicon Doppelganger

Create high-fidelity "Digital Twins" of business principals using structured personality extraction and persona simulation for forecasting team dynamics and business decisions.

## When to Use

Invoke when user:
- Wants to simulate team decision-making dynamics
- Needs to predict partnership friction or alignment
- Is building personality profiles for business forecasting
- Asks to create a "digital twin" or persona model
- Wants to test business scenarios against team personalities

## Core Workflow

### Phase 1: Extraction (Data Collection)

Interview each principal individually (30-45 min per person):
1. **Hardware** - Collect psychometrics (CliftonStrengths, VIA Character Strengths, communication samples)
2. **Operating System** - Map decision heuristics (good work definition, friction triggers, risk tolerance, information preferences)
3. **Narrative Identity** - Capture origin stories, shadow behaviors, and unpopular opinions

See `references/extraction-protocol.md` for full interview script.

### Phase 2: Encoding (Persona Schema)

Compile interview data into structured XML persona profile:
- Psychometrics and linguistic fingerprint
- Core drivers (motivation/fear)
- Decision logic (risk, data preference, blind spots)
- Conflict style and narrative anchors

See `references/persona-schema.md` for full schema.

### Phase 3: Simulation Engine

Load multiple personas into simulation:
1. **Algorithmic Fidelity** - Strictly adhere to each persona's decision logic
2. **Internal Monologue** - Think through how values align before speaking
3. **Dynamic Interaction** - Allow natural interruption, agreement, argument

See `references/simulation-guide.md` for setup instructions.

### Phase 4: Scenario Testing

Run event cards to forecast outcomes:
- **Soul of the Company** - Research vs. consulting decisions
- **Team Implosion** - Gap analysis and friction prediction
- **Project Fit** - Competence and joy ratings per persona

See `references/scenarios.md` for event card library.

## Output Format

**Persona Schema (XML):**
```xml
<persona_profile>
    <name>Principal Name</name>
    <psychometrics>...</psychometrics>
    <linguistic_fingerprint>...</linguistic_fingerprint>
    <core_drivers>...</core_drivers>
    <decision_logic>...</decision_logic>
    <conflict_style>...</conflict_style>
    <narrative_anchors>...</narrative_anchors>
</persona_profile>
```

**Simulation Output:**
Each persona speaks in character with internal reasoning, following their decision logic strictly.

## Key Principle

Token-efficient persona encoding prevents AI drift. The XML schema acts as a "save file" that maintains character consistency across sessions.
