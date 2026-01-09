# Silicon Doppelganger

Build psychometrically accurate personal proxy agents ("Digital Twins") for the PAIRL Conductor system. Extract personality, decision heuristics, and values into portable schemas that enable AI agents to negotiate, filter, and act on a principal's behalf.

## Overview

The Silicon Doppelganger Protocol transforms subjective personality assessment into structured, portable persona data. These "Digital Twins" serve as **spokes** in the PAIRL Conductor hub-and-spoke architecture, negotiating and filtering on behalf of their principals.

**Key Innovation:** Token-efficient XML persona encoding creates a "save file" that maintains fidelity across sessions, models, and deployment contexts (simulation vs. live agent proxy).

## Features

- **Structured Extraction** - Systematic 45-60 minute interview protocol covering psychometrics, heuristics, and narrative identity
- **Portable Persona Schema** - XML format that captures personality in a way AI can reliably reproduce
- **Agent Rules Block** - Define must_reject, must_protect, should_prefer for automated decision-making
- **PAIRL Integration** - Deploy as spoke agents in the Conductor hub-and-spoke architecture
- **Behavioral Validation** - Question battery testing with 80%+ accuracy target
- **Multi-Persona Simulation** - Run realistic team discussions with algorithmic fidelity
- **Drift Prevention** - Persona encoding maintains character consistency across sessions and systems

## Use Cases

### Primary: Personal Proxy Agent
Build a spoke for PAIRL Conductor that represents you in automated workflows:
- Task acceptance/rejection based on encoded values and ethical filters
- Calendar negotiation with other agents
- Filtering incoming requests before they reach you
- Protecting time, energy, and boundaries automatically

### Secondary: Team Simulation
Load multiple proxies to forecast team dynamics:
- Predict friction points before partnerships form
- Test strategic decisions against personality profiles
- Surface unspoken tensions and misalignments

### Tertiary: Self-Knowledge Tool
The extraction process itself is valuable:
- Articulate your own decision patterns
- Surface blind spots and shadow behaviors
- Create documentation of "how I work" for collaborators

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

### For Claude Code (Terminal)

```bash
# From the AISkills repository root:
cp -r SiliconDoppelganger/silicon-doppelganger ~/.claude/skills/
```

The skill will be available via `skill: "silicon-doppelganger"` in your Claude Code sessions.

### For Claude Chat (Web/Desktop)

**Download the packaged skill:**
- [silicon-doppelganger-v1.0.0.skill](../dist/silicon-doppelganger-v1.0.0.skill)

**Option 1: Claude Project**
1. Create a new Project at [claude.ai](https://claude.ai)
2. Extract the .skill file (it's a zip archive)
3. Upload these files to the Project Knowledge:
   - `SKILL.md` (required)
   - `references/extraction-protocol.md`
   - `references/persona-schema.md`
   - `references/simulation-guide.md`
   - `references/scenarios.md`
4. Start a conversation in the Project

**Option 2: Direct Paste**
1. Extract the .skill file and open `SKILL.md`
2. Copy the contents and paste at the start of a new conversation
3. For detailed protocols, paste reference files as needed during the session

**Note:** The skill works best with Claude's most capable models (Opus, Sonnet) due to the complexity of multi-persona simulation.

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
- **[references/agent-integration.md](references/agent-integration.md)** - PAIRL Conductor deployment guide
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
