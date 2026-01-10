# Persona Schema Integration

How to use a SiliconDoppelganger persona schema for enhanced voice calibration.

---

## Overview

A **persona schema** is a structured XML file created using the SiliconDoppelganger skill. It encodes:
- Psychometric data (CliftonStrengths, VIA Character Strengths)
- Linguistic fingerprint (tone, vocabulary, sentence patterns)
- Core drivers (motivations, fears)
- Decision logic (how the person thinks and reasons)
- Conflict style and communication preferences

When available, this data significantly enhances WritingPartner's ability to match your authentic voice.

---

## What a Persona Schema Contains

```xml
<persona_profile>
    <psychometrics>
        <clifton>Top 5-10 CliftonStrengths</clifton>
        <via>Top 5-10 VIA Character Strengths</via>
    </psychometrics>
    <linguistic_fingerprint>
        Sentence structure, vocabulary patterns, tone, formality level
    </linguistic_fingerprint>
    <core_drivers>
        <primary_motivation>Impact | Security | Novelty | Money</primary_motivation>
        <primary_fear>Irrelevance | Boredom | Conflict | Poverty</primary_fear>
    </core_drivers>
    <decision_logic>
        Risk tolerance, data preferences, blind spots
    </decision_logic>
    <conflict_style>
        Communication patterns under normal and stress conditions
    </conflict_style>
    <narrative_anchors>
        Origin story, shadow self, unpopular opinions
    </narrative_anchors>
</persona_profile>
```

---

## How WritingPartner Uses Persona Data

### During Interview Mode

**Core drivers** inform question selection:
- If motivation = Impact → probe for "who will this help?"
- If motivation = Novelty → probe for "what's new here?"
- If fear = Irrelevance → surface "why does this matter now?"

**Narrative anchors** provide context:
- Origin story themes may connect to essay topics
- Unpopular opinions suggest contrarian angles worth exploring

### During Drafting Mode

**Linguistic fingerprint** guides prose generation:
- Match sentence structure patterns (varied? punchy? flowing?)
- Use vocabulary consistent with domain expertise
- Apply appropriate formality level
- Include characteristic phrase patterns

**Decision logic** shapes argument structure:
- Risk tolerance affects how boldly claims are stated
- Data preferences influence what evidence to emphasize
- Blind spots suggest what counterarguments to address

### During Calibration Mode

**Conflict style** informs tone checking:
- Debater style → more direct assertions acceptable
- Diplomat style → softer framing preferred
- Check stress patterns don't leak into normal prose

**Psychometrics** provide authenticity markers:
- Strategic thinker → expect pattern recognition, future orientation
- Learner → expect curiosity, "I wonder" openings
- Honesty strength → expect directness, truth-seeking tone

---

## Setup

### If You Have a Persona Schema

Place your persona schema where WritingPartner can find it:

**Option 1: In working directory**
```
your-project/
├── WritingSamples/           # Voice samples
├── persona-schema.xml        # Your Digital Twin
└── ...
```

**Option 2: Reference external location**
```
Tell WritingPartner: "Load persona from ~/Projects/SiliconDoppelgangerActual/silicon-doppelganger-actual/data/lee-gonzales-persona-schema.xml"
```

### If You Don't Have a Persona Schema

You can create one using the **SiliconDoppelganger** skill:
1. Invoke SiliconDoppelganger
2. Complete the extraction interview (45-60 min)
3. Generate the persona schema XML
4. Use with WritingPartner for enhanced voice matching

Or skip it—WritingPartner works well with just WritingSamples and blocklist.

---

## Integration Layers

WritingPartner uses multiple layers for voice calibration, each adding fidelity:

| Layer | Source | What It Provides |
|-------|--------|------------------|
| 1. Blocklist | `references/blocklist.md` | AI patterns to avoid |
| 2. prose-polish | External skill | AI detection scoring |
| 3. WritingSamples | `WritingSamples/` directory | Actual prose examples |
| 4. Persona Schema | `persona-schema.xml` | Psychometric + cognitive patterns |

**With all four layers:** Maximum voice fidelity
**With layers 1-3:** Excellent voice matching
**With layers 1-2 only:** Good AI detection, generic voice
**With layer 1 only:** Basic blocklist protection

---

## Persona Schema + WritingSamples

These complement each other:

| Aspect | Persona Schema | WritingSamples |
|--------|----------------|----------------|
| **Provides** | The "why" | The "how" |
| **Captures** | Motivations, thinking patterns | Actual prose rhythm |
| **Format** | Structured XML | Raw markdown |
| **Created by** | Interview extraction | Collecting existing writing |
| **Updates** | Quarterly validation | As you write more |

**Best practice:** Use both when available. Persona explains the mind; samples show the voice.

---

## Example Usage

**User:** "Let's work on an essay about AI in education"

**WritingPartner (with persona loaded):**

*Interview informed by persona:*
> "Your CliftonStrengths show Strategic and Learner in top 5. Are you approaching this from a pattern-recognition angle (what you see happening) or a learning angle (what you're discovering)?"

*Drafting informed by persona:*
> Loading linguistic fingerprint: varied sentences, technical vocabulary, direct tone, occasional philosophical references...

*Calibration informed by persona:*
> Checking against Honesty strength—this passage hedges more than your typical directness. Consider: "AI will transform education" instead of "AI might potentially transform education."

---

## Creating a Persona Schema

If you want to build one, use the **SiliconDoppelganger** skill:

```
Invoke: "Create a persona schema for me"
```

The skill will guide you through:
1. **Hardware extraction** — Psychometric assessments
2. **Operating System mapping** — Decision heuristics
3. **Narrative Identity capture** — Origin story, shadow self
4. **Schema encoding** — Compile into XML format
5. **Validation** — Test against real behavior

See the SiliconDoppelganger skill for full methodology.

---

## Privacy Note

Persona schemas contain sensitive personal data:
- Keep in private repositories
- Don't commit to public repos
- The schema is your "psychological fingerprint"

WritingPartner references the schema but never exposes its contents.

---

**See also:**
- SiliconDoppelganger skill for persona creation
- `integrations/writing-samples.md` for prose examples
- `references/blocklist.md` for AI pattern detection
