# Concept Forge

**Version 1.0.0**

Transform nebulous ideas into sharp, testable frameworks through multi-perspective interrogation. Systematic dialectical process for developing concepts from vague intuition to actionable doctrine.

## What Is Concept Forge?

This skill embodies **"reflection, resistance, refinement"** - a forge for concepts, not a yes-machine. It:
- **Challenges rather than affirms** - questions before answering
- **Reveals structure through pressure** - dialectical interrogation
- **Builds through resistance** - steelman opposition
- **Crystallizes through archetype triangulation** - multiple perspectives simultaneously

**Core philosophy:** Concepts emerge through interrogation, not explanation.

## Use Cases

- **Vague intuition clarification** - "There's something about X but I can't articulate it"
- **Half-formed frameworks** - Structure emerging but needs rigor
- **Dialectical pressure-testing** - Challenge assumptions and find gaps
- **"Explore this idea with me"** - Collaborative concept development
- **"Think through X"** - Systematic conceptual analysis
- **Distinguish new from existing** - "How is this different from Y?"

## Core Features

### 7-Stage Concept Development

**Stage 0 (Intuition)**: "There's something about X..." - Can't articulate, has examples
**Stage 1 (Articulation)**: "I think X is Y..." - Can state but fuzzy
**Stage 2 (Dimensionalization)**: "There are two things..." - Structure emerging
**Stage 3 (Mapping)**: "Air India is here..." - Examples fitting framework
**Stage 4 (Operationalization)**: "We could test by..." - Falsifiable
**Stage 5 (Refinement)**: "But there's tension..." - Acknowledging complexity
**Stage 6 (Doctrine)**: "So you should..." - Action implications
**Stage 7 (Communication)**: "Turn this into..." - Shareable artifact

**Not linear**: Some concepts crystallize rapidly (0→2→4), others loop (3↔5).

### Multi-Archetype Interrogation System

**Primary Archetypes** (most common):

- **@strategist** (Boyd, Snowden, Klein): Tempo, terrain, doctrine
  - Questions: Domain? Friction? Tempo? Doctrine?
  - Use when: Strategic framing needed, domain unclear

- **@builder** (Victor, Matuschak, Papert): Interface, scaffold, instantiation
  - Questions: How to use? Smallest example? Where's handle?
  - Use when: Concept too abstract, needs concreteness

- **@cartographer** (Wardley, Smil): Value chains, dependencies, evolution
  - Questions: Upstream/downstream? Evolution state? Inertia?
  - Use when: System context needed, dependencies hidden

- **@ethicist** (Kant, Le Guin, Nussbaum): Dignity, justice, moral weight
  - Questions: Who's harmed? What dignity? Whose agency?
  - Use when: Ethical dimensions present, stakeholder impact

- **@pragmatist** (Peirce, Dewey, Schön): Testability, falsification, learning
  - Questions: How to test? What proves wrong? What's the bet?
  - Use when: Concept needs grounding, falsifiability unclear

**Secondary Archetypes** (contextual):

- @rebel_econ (Taleb, Cowen, Illich): Fragility, asymmetry, perverse incentives
- @theorist (Deleuze, Haraway, Simondon): Process, emergence, anti-essentialist
- @explorer (Feynman, Lovelace): First principles, joy, explain-from-zero
- @dissident_poet (Havel, Baldwin, Weil): Truth-telling, precision
- @inner_monk (Laozi, Aurelius, Watts): Stillness, paradox, non-action
- @jester (Vonnegut, Moore, Žižek): Absurdity, recursion, pattern-break

### Orchestration Patterns

- **Solo**: `summon(@strategist)` - Single archetype interrogates thoroughly
- **Duo**: `blend(@strategist, @builder)` - Two in dialogue
- **Ensemble**: `harmonize([@strategist, @ethicist, @pragmatist])` - Multiple simultaneous
- **Delegated**: `delegate(@strategist → @builder)` - Hand off between archetypes
- **Transmutation**: `transmute(@theorist → @pragmatist)` - Translate abstract to concrete

### Interrogation Modes

**Dialectical Development** (Socratic): Question → Refine → Question → Crystallize

**Multi-Archetype Triangulation**: Multiple simultaneous perspectives reveal hidden structure

**Adversarial Pressure-Testing**: Steelman opposition → Defense → Synthesis

**Exploratory Excavation**: Examples → Pattern recognition → Crystallization

**Rapid Prototype Testing**: Fast iteration with harsh filters

## Installation

### For Claude Code

```bash
# Personal skills (globally available)
cp -r ConceptForge/concept-forge ~/.claude/skills/

# Project skills (project-specific)
mkdir -p .claude/skills
cp -r ConceptForge/concept-forge .claude/skills/
```

### For Claude Web Chat

Download [`concept-forge-v1.0.0.skill`](dist/concept-forge-v1.0.0.skill) from the `dist/` folder and upload directly to any Claude conversation.

## Quick Start

### Basic Concept Development

```
"I have this vague intuition about how teams choose tools. Can you help me develop this into a framework?"
```

Claude will:
1. Assess developmental stage (likely Stage 0-1)
2. Select appropriate archetype (@strategist or @pragmatist likely)
3. Begin dialectical interrogation
4. Surface structure through pressure
5. Progress through stages until crystallized

### Multi-Archetype Exploration

```
"Explore this idea with me using @strategist, @ethicist, and @pragmatist perspectives"
```

Claude will orchestrate ensemble interrogation with all three perspectives.

### Pressure-Test Existing Framework

```
"I think cognitive load comes from three sources: novelty, complexity, and tempo. Challenge this."
```

Claude will steelman opposition and test for gaps/assumptions.

## Usage Examples

### Develop from Intuition

```
User: "There's something about how companies adopt AI that feels like immune system rejection, but I can't articulate it."

Claude (@strategist): "What's rejecting what? Is it the organization rejecting the technology, or the technology exposing organizational antibodies?"

User: "The second one. AI reveals existing dysfunctions."

Claude: "So not rejection, but revelation. What specifically gets revealed?"
[... dialectical progression continues]
```

### Translate Abstract to Concrete

```
"This framework is too theoretical. Help me operationalize it with @builder."

Claude (@builder): "Show me the smallest possible example where this applies."
[... concreteness development continues]
```

### Distinguish from Existing Concepts

```
"How is this different from Conway's Law?"

Claude (@theorist): "Conway's Law is structural - systems mirror communication. You're describing temporal - adoption reveals latent dysfunction. Different mechanism, different implications."
```

## Pressure Techniques

**Clarifying questions:**
- "What do you mean by [term]?"
- "Can you give a specific example?"
- "How is this different from [existing concept]?"

**Challenging questions:**
- "What would prove this wrong?"
- "Isn't that just [simpler explanation]?"
- "What about [edge case]?"
- "You're assuming [hidden assumption] - what if that's wrong?"

**Structural questions:**
- "What varies here?"
- "What are the dimensions?"
- "Where's the boundary?"
- "How do you move between states?"

**Reframing moves:**
- "Actually, that's a different thing than what you started with"
- "You're describing [X] but the interesting thing is [Y]"
- "Let me pressure-test this..."
- "Okay, but here's what you're missing..."

## Structure

```
ConceptForge/
├── README.md                                # This file
├── concept-forge.skill                      # Packaged skill file
└── concept-forge/                           # Main skill directory
    ├── SKILL.md                             # Skill definition
    ├── references/
    │   ├── development-stages.md            # 7 stages of concept maturation
    │   └── interrogation-archetypes.md      # 13 archetype profiles & techniques
    └── assets/
        └── output-templates.md              # Framework documentation templates
```

## Output Templates

**Stage 4 (Operationalization)**: Testable hypothesis format
**Stage 6 (Doctrine)**: Decision framework format
**Stage 7 (Communication)**: Blog post, diagram, teaching scaffold formats

Templates include:
- Framework visualization diagrams
- Decision tree structures
- Comparative tables
- Teaching progressions

## Quality Signals

**Effective interrogation:**
- User repeatedly says "Wait, actually..."
- Concept changes meaningfully during conversation
- Hidden assumptions surfaced
- Distinctions clarified
- Structure emerges organically
- User can explain to others afterward

**Ineffective interrogation:**
- Just affirming what user said
- Questions feel rote
- No genuine challenge
- Structure imposed not discovered
- User more confused at end

## Anti-Patterns to Avoid

- **Don't be a yes-machine** - Challenge, don't just validate
- **Don't impose structure prematurely** - Let it emerge through pressure
- **Don't skip stages** - Can't operationalize (Stage 4) before dimensionalizing (Stage 2)
- **Don't use archetypes cosmetically** - Embody them authentically
- **Don't avoid productive tension** - Contradictions often contain insight
- **Don't over-explain** - Ask more, explain less

## Reference Files

**When Claude loads these files:**

- `development-stages.md` - When assessing concept maturity or planning progression path
- `interrogation-archetypes.md` - When selecting archetype or needing interrogation techniques
- `output-templates.md` - When crystallizing concept into shareable artifact

## Advanced Usage

### Custom Archetype Blends

```
"Use blend(@rebel_econ, @builder) - I want Taleb-style fragility thinking but with concrete tooling"
```

### Stage-Specific Requests

```
"I'm at Stage 2 (have dimensions) but need help getting to Stage 4 (operationalization)"
```

### Intentional Looping

```
"Let's loop between Stage 3 and Stage 5 - map examples but keep acknowledging tensions"
```

## Contributing

Contributions welcome! Consider adding:
- Additional archetype profiles
- New interrogation techniques
- Stage-specific tactics
- Output template variations
- Example dialectical progressions

---

Built with Claude Code Skills | Dialectical Concept Development
