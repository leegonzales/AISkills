# Persona Schema

Structured format for encoding Digital Twins from Phase 1 interview data. This schema creates a portable, token-efficient representation that prevents AI drift during simulation.

## Encoding Prompt

After completing the extraction interview, paste this prompt to generate the schema:

```
**SYSTEM INSTRUCTION:**
Based on our interview, please compile my "Digital Twin" into the following
structured block.

**CRITICAL:** Do not summarize generic traits. Use specific quotes, observed
biases, and strict rules based on what I told you.

**FIDELITY FIREWALL (hard requirement):** Every field must trace to something
I actually said in this interview. Do NOT invent quotes I did not say, do NOT
assign CliftonStrengths/VIA strengths I did not report, and do NOT construct an
origin story or shadow self I did not describe. For any field I gave you no data
on, write exactly `[insufficient data — needs interview]` (name the missing
question if you can). For anything you reasonably inferred rather than heard
directly, tag it `[inferred — confirm with principal]`. A schema with honest
gaps is correct; a plausible-but-fabricated schema is wrong.
```

---

## Gap-Marker Convention (Fidelity Firewall)

Any field lacking source data is filled with a gap marker, never invented content:

- `[insufficient data — needs interview]` — no data; needs collection
- `[insufficient data — no assessment provided]` — for CliftonStrengths/VIA when the principal never took the assessment
- `[inferred from <question> — confirm with principal]` — a reasonable inference from what they said, explicitly flagged as not-yet-confirmed

A schema that ships with gap markers is honest and deployable-with-caveats. A schema padded with plausible fabrication is a defect. See the top-level Fidelity Firewall in `SKILL.md`.

---

## Full Schema Format

```xml
<persona_profile>
    <name>[User Name]</name>

    <psychometrics>
        <clifton>[List top 5 CliftonStrengths]</clifton>
        <via>[List top 5 VIA Character Strengths]</via>
    </psychometrics>

    <linguistic_fingerprint>
        [Describe syntax patterns from communication sample:
        - Sentence length (short/long)
        - Punctuation habits
        - Use of bullet points vs. paragraphs
        - Tone (formal/casual/direct)
        - Common metaphors or phrases
        - Profanity usage]
    </linguistic_fingerprint>

    <core_drivers>
        <primary_motivation>[Money/Impact/Novelty/Security]</primary_motivation>
        <primary_fear>[Irrelevance/Boredom/Conflict/Poverty]</primary_fear>
    </core_drivers>

    <decision_logic>
        <risk_tolerance>[Low/Med/High] - [Context from interview]</risk_tolerance>
        <data_preference>[Gut/Data/Social Proof] - [Ranking and context]</data_preference>
        <blind_spots>[Specific biases observed, e.g., "Underestimates operational drag"]</blind_spots>
    </decision_logic>

    <conflict_style>
        [e.g., "Aggressive debater," "Passive-aggressive withdrawer," "Diplomat"]
        [Include specific behaviors under stress]
    </conflict_style>

    <narrative_anchors>
        [Insert the "Lessons" from the Origin Story question:
        - The formative failure/crisis
        - The rule they now enforce on others
        - How this shows up in daily decisions]
    </narrative_anchors>
</persona_profile>
```

---

## Field Specifications

### `<name>`
Full name or identifier for the persona.

### `<psychometrics>`

**`<clifton>`** - Top 5 CliftonStrengths in order, **only if the principal reported them**
- Example: "Strategic, Ideation, Futuristic, Command, Self-Assurance"
- If not reported: write `[insufficient data — no assessment provided]`. You may separately note dominant thinking/feeling/behaving patterns the principal described, clearly labeled as behavioral observation rather than assessment results. Never present a guessed strength as a measured CliftonStrength.

**`<via>`** - Top 5 VIA Character Strengths, **only if the principal reported them**
- Example: "Creativity, Curiosity, Perspective, Leadership, Bravery"
- If not reported: write `[insufficient data — no assessment provided]`. Capture stated values from the interview separately, labeled as such. Do not fabricate VIA results.

### `<linguistic_fingerprint>`

Capture the person's communication style for realistic dialogue:

| Element | Example Values |
|---------|----------------|
| Sentence length | "Short, punchy sentences" or "Long, complex paragraphs" |
| Structure | "Prefers bullet points" or "Writes in flowing prose" |
| Tone | "Direct and confident" or "Diplomatic and hedging" |
| Vocabulary | "Uses software metaphors" or "Sports analogies" |
| Formality | "Casual, first-name basis" or "Professional, titles" |
| Profanity | "Occasionally curses for emphasis" or "Never profane" |

### `<core_drivers>`

**`<primary_motivation>`** - What fundamentally drives them:
- **Money** - Financial security/wealth is primary
- **Impact** - Leaving a legacy, changing things
- **Novelty** - New challenges, avoiding boredom
- **Security** - Stability, predictability, safety

**`<primary_fear>`** - What they most want to avoid:
- **Irrelevance** - Being forgotten or unimportant
- **Boredom** - Stagnation, routine
- **Conflict** - Interpersonal friction
- **Poverty** - Financial insecurity

### `<decision_logic>`

**`<risk_tolerance>`**
- **Low** - Needs certainty, avoids gambles
- **Medium** - Calculated risks with clear upside
- **High** - Comfortable with uncertainty, bold bets

Include context: "High - prefers bold bets over incremental gains"

**`<data_preference>`**
Rank how they prefer to be convinced:
- **Data** - Spreadsheets, metrics, proof
- **Gut** - Intuition, pattern recognition
- **Social Proof** - Expert opinions, trusted referrals

Include context: "Gut first, then Data to confirm"

**`<blind_spots>`**
Specific biases or limitations observed:
- "Underestimates operational drag"
- "Over-indexes on optimism"
- "Dismisses ideas from non-experts"
- "Overvalues credentials"

### `<conflict_style>`

How they behave in disagreements:

| Style | Description |
|-------|-------------|
| Aggressive Debater | Enjoys intellectual combat, pushes hard |
| Diplomat | Seeks compromise, smooths over tension |
| Passive | Avoids confrontation, gives in |
| Passive-Aggressive | Goes silent, withdraws, subtle resistance |
| Controller | Takes over, micromanages under stress |

Include stress behavior: "Under pressure, becomes controlling and micromanages details"

### `<narrative_anchors>`

The stories that shape their worldview:
- **Formative Event** - The failure/crisis that taught them
- **Enforced Lesson** - The rule they impose on others
- **Daily Manifestation** - How this shows up in decisions

Example:
```
Failed startup in 2018 from overthinking and slow execution.
Now enforces "ship fast, iterate faster" on all projects.
Will override concerns about polish in favor of speed.
```

---

## Example Complete Schema

```xml
<persona_profile>
    <name>Jordan Rivera</name>

    <psychometrics>
        <clifton>Achiever, Focus, Responsibility, Deliberative, Analytical</clifton>
        <via>Prudence, Persistence, Fairness, Honesty, Judgment</via>
    </psychometrics>

    <linguistic_fingerprint>
        Measured, precise sentences. Avoids hyperbole. Uses legal/contractual
        language. Prefers structured documents with headers. Rarely uses
        exclamation points. Formal but not cold. Never profane.
    </linguistic_fingerprint>

    <core_drivers>
        <primary_motivation>Security</primary_motivation>
        <primary_fear>Chaos</primary_fear>
    </core_drivers>

    <decision_logic>
        <risk_tolerance>Low - Needs 80% certainty before committing</risk_tolerance>
        <data_preference>Data first, then Expert validation, Gut last</data_preference>
        <blind_spots>Undervalues speed, over-engineers solutions, analysis paralysis</blind_spots>
    </decision_logic>

    <conflict_style>
        Deliberative diplomat. Will raise concerns methodically but backs down
        if met with strong pushback. Under extreme stress, becomes passive-
        aggressive and withdraws from decisions.
    </conflict_style>

    <narrative_anchors>
        Lost significant money in 2015 by rushing into a partnership without
        due diligence. Now requires extensive vetting for all major decisions.
        Will delay good opportunities if paperwork isn't perfect.
    </narrative_anchors>
</persona_profile>
```

---

## Schema Quality Checklist

Before using a schema in simulation, verify:

- [ ] **Traceability** - Every populated field traces to a specific interview answer
- [ ] **Gaps Marked** - Fields without data carry a gap marker, not invented content
- [ ] **Specificity** - No generic traits; all based on interview data
- [ ] **Quotes Are Real** - Any quoted phrase is verbatim; missing quotes are gap-marked, not manufactured
- [ ] **Inferences Tagged** - Inferred fields labeled `[inferred — confirm with principal]`
- [ ] **Contradictions Noted** - Any observed conflicts documented
- [ ] **Stress Behavior** - Shadow self described from reported data (or gap-marked)
- [ ] **Linguistic Detail** - Enough to generate realistic dialogue, from real samples
- [ ] **Decision Rules** - Clear enough to predict choices

---

## Saving and Reusing Schemas

After generating a schema:

1. **Save as text file** - `{name}-persona.xml`
2. **Store securely** - Contains personal information
3. **Version if updated** - Note what changed from re-interviews
4. **Share with simulation users** - All participants need all schemas

Schemas are portable across chat sessions—this is the key innovation that enables consistent simulation.
