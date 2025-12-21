# Silicon Doppelganger

Create psychometrically accurate "Digital Twins" of business principals to forecast outcomes, team dynamics, and strategic alignment.

## Overview

The Silicon Doppelganger Protocol transforms subjective personality assessment into structured, portable persona data that AI can use to simulate realistic team interactions and predict business outcomes.

**Key Innovation:** Token-efficient XML persona encoding creates a "save file" for each personality that prevents AI drift during extended simulations.

## Features

- **Structured Extraction** - Systematic 30-45 minute interview protocol covering psychometrics, heuristics, and narrative identity
- **Portable Persona Schema** - XML format that captures personality in a way AI can reliably reproduce
- **Multi-Persona Simulation** - Run realistic team discussions with algorithmic fidelity to each persona
- **Scenario Testing** - Pre-built event cards for common business decisions
- **Drift Prevention** - Persona encoding maintains character consistency across sessions

## Use Cases

### Team Formation Analysis
- Predict friction points before partnerships form
- Identify missing skills/temperaments in founding teams
- Test compatibility of potential co-founders

### Decision Forecasting
- Simulate how a team will respond to strategic pivots
- Test product decisions against stakeholder personalities
- Predict resistance to organizational changes

### Hiring Strategy
- Define psychometric profiles for ideal candidates
- Test how new hires will interact with existing team
- Identify gaps that need filling

## Workflow

### Phase 1: Extraction (30-45 min per person)

Each principal completes a structured interview:

1. **Hardware (Psychometrics)**
   - CliftonStrengths top 5
   - VIA Character Strengths top 5
   - Communication sample analysis

2. **Operating System (Heuristics)**
   - "Good Work" definition
   - Friction triggers
   - Risk/reward preferences
   - Information filter preferences

3. **Narrative Identity (Soul)**
   - Professional origin story/failure
   - Shadow self behavior under stress
   - Unpopular industry opinions

### Phase 2: Encoding

The interview data is compiled into a structured Persona Schema:

```xml
<persona_profile>
    <name>Alex Chen</name>
    <psychometrics>
        <clifton>Strategic, Ideation, Futuristic, Command, Self-Assurance</clifton>
        <via>Creativity, Curiosity, Perspective, Leadership, Bravery</via>
    </psychometrics>
    <linguistic_fingerprint>
        Short, punchy sentences. Uses tech metaphors. Occasionally profane.
        Prefers bullet points over paragraphs. Direct and confident tone.
    </linguistic_fingerprint>
    <core_drivers>
        <primary_motivation>Impact</primary_motivation>
        <primary_fear>Irrelevance</primary_fear>
    </core_drivers>
    <decision_logic>
        <risk_tolerance>High - Prefers bold bets over incremental gains</risk_tolerance>
        <data_preference>Gut/Expert - Trusts pattern recognition over spreadsheets</data_preference>
        <blind_spots>Over-indexes on optimism, underestimates operational drag</blind_spots>
    </decision_logic>
    <conflict_style>Aggressive debater, enjoys intellectual combat, respects pushback</conflict_style>
    <narrative_anchors>
        Failed startup in 2018 taught that speed beats perfection.
        Now enforces "ship fast, iterate faster" on everyone.
    </narrative_anchors>
</persona_profile>
```

### Phase 3: Simulation

Load persona schemas into a new chat session and run multi-party simulations:

- AI strictly adheres to each persona's decision logic
- Internal monologue shows how values align with topics
- Dynamic interaction with natural interruptions and disagreements

### Phase 4: Scenario Testing

Drop "Event Cards" into the simulation to test specific decisions:

- **Soul of the Company** - Consulting vs. research choices
- **Team Implosion** - Predict future conflicts
- **Project Fit** - Rate ideas against each persona

## Installation

### For Claude Code

```bash
# From the AISkills repository root:
cp -r SiliconDoppelganger/silicon-doppelganger ~/.claude/skills/
```

### For Claude Projects

Upload the skill files to your Claude Project's knowledge base.

## Quick Start

1. **Start Extraction:**
   ```
   Run the Silicon Doppelganger extraction interview for [Person Name]
   ```

2. **Generate Schema:**
   ```
   Compile the interview into a Persona Schema
   ```

3. **Load Simulation:**
   ```
   Start a simulation with these personas: [paste XML blocks]
   ```

4. **Run Scenario:**
   ```
   [Paste an Event Card from references/scenarios.md]
   ```

## Documentation

- **[SKILL.md](SKILL.md)** - Core skill definition (read by Claude)
- **[references/extraction-protocol.md](references/extraction-protocol.md)** - Full interview script
- **[references/persona-schema.md](references/persona-schema.md)** - Schema format and fields
- **[references/simulation-guide.md](references/simulation-guide.md)** - How to run simulations
- **[references/scenarios.md](references/scenarios.md)** - Event card library

## Theory

### Why Encoding Matters

Previous approaches relied on the AI "remembering" long conversations. This failed because:
- Context windows have limits
- AI drifts out of character over time
- Personality details get lost or conflated

The Persona Schema creates a compressed, structured representation that:
- Fits in minimal tokens
- Provides rigid behavioral constraints
- Can be saved and reloaded across sessions

### Psychometric Foundation

The protocol draws from established frameworks:
- **CliftonStrengths** - How people naturally think, feel, and behave
- **VIA Character Strengths** - Core values that drive motivation
- **Narrative Identity Theory** - Stories people tell that shape behavior

### Algorithmic Fidelity

The simulation enforces strict adherence to persona constraints:
- Risk-averse personas MUST reject risky ideas
- Conflict styles determine interaction patterns
- Blind spots consistently affect judgment

## Limitations

- Accuracy depends on interview quality and honesty
- Complex personalities may not fit neatly into schema
- Simulation is prediction, not prophecy
- Works best with 2-4 personas; more becomes unwieldy

## Best Practices

1. **Interview Separately** - Each person in isolation to avoid influence
2. **Get Specific Examples** - Push past generic answers with "give me an example"
3. **Save the XML** - Store persona files for future sessions
4. **Start Simple** - Test with 2 personas before adding more
5. **Trust the Constraints** - Don't override persona logic for "better" outcomes

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## License

MIT License - see [LICENSE](LICENSE) for details.

---

Built with Claude Code | Part of [AISkills Collection](https://github.com/leegonzales/AISkills)
