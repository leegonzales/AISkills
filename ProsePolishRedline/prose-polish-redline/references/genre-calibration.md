# Genre Calibration -- Prose Polish Redline

Genre detection happens BEFORE scoring. Different genres have different rules -- penalizing a technical document for neutral voice or an academic paper for hedging produces false positives.

---

## Genre Detection

Detect genre from the document's content, structure, and context before applying any katas. When ambiguous, ask the user or default to the closest match.

**Supported genres:** Technical, Business, Academic, Creative, Personal, Journalistic

---

## Calibration Thresholds

| Genre        | Sentence Variance | Hedge Tolerance        | Passive Voice | Template Tolerance     | Voice Expectation      |
|--------------|-------------------|------------------------|---------------|------------------------|------------------------|
| Technical    | 5+ StdDev         | Higher (precision)     | Higher        | Expected               | Neutral authority      |
| Business     | 6+ StdDev         | Standard               | Lower         | Structure OK           | Professional human     |
| Academic     | 6+ StdDev         | Higher (epistemic)     | Moderate      | If fresh content       | Measured expertise     |
| Creative     | 8+ StdDev         | Low                    | Low           | = Failure              | Distinctive required   |
| Personal     | 8+ StdDev         | Low                    | Low           | Must be organic        | Strongly embodied      |
| Journalistic | 7+ StdDev         | Standard               | Low           | Lead structure OK      | Clear but present      |

### Reading the Table

- **Sentence Variance:** Minimum standard deviation of sentence word counts before flagging rhythm as flat. Higher = more variation expected.
- **Hedge Tolerance:** How aggressively to flag hedges. "Higher" means many hedges are genre-appropriate (e.g., epistemic hedging in academia).
- **Passive Voice:** How much passive construction is acceptable. Technical and academic writing tolerates more.
- **Template Tolerance:** Whether formulaic structure is acceptable. Technical docs expect templates; creative writing that feels templated has failed.
- **Voice Expectation:** How much authorial personality is expected. Ranges from "neutral authority" (technical) to "strongly embodied" (personal).

---

## Effectiveness Dimension Weights

The overall Effectiveness score is a genre-weighted average of five dimensions. These weights determine what matters most for each genre.

| Genre        | Craft | Coherence | Authority | Purpose | Voice |
|--------------|-------|-----------|-----------|---------|-------|
| Technical    | 25%   | 30%       | 20%       | 15%     | 10%   |
| Business     | 20%   | 25%       | 25%       | 20%     | 10%   |
| Academic     | 20%   | 30%       | 20%       | 15%     | 15%   |
| Creative     | 15%   | 20%       | 10%       | 15%     | 40%   |
| Personal     | 15%   | 20%       | 20%       | 15%     | 30%   |
| Journalistic | 20%   | 25%       | 20%       | 20%     | 15%   |

### Weight Interpretation

- **Technical:** Coherence dominates (30%). Logic and flow matter most. Voice is least important (10%).
- **Business:** Authority and Coherence share the lead (25% each). Credibility and logical flow are equally critical.
- **Academic:** Coherence dominates (30%). Argument structure is paramount. Voice matters more than in business (15%).
- **Creative:** Voice dominates (40%). Distinctiveness is the primary quality signal. Authority matters least (10%).
- **Personal:** Voice leads (30%) with Authority second (20%). The person behind the writing must be visible and credible.
- **Journalistic:** Balanced across Coherence, Authority, and Purpose (20-25% each). Clear, credible, purposeful reporting.

---

## Genre-Specific Signals

How katas should adjust their behavior per genre.

### Technical Documentation

- **Allow:** "certain," "particular," "specific" -- these are precision language, not hedging
- **Allow:** Consistent sentence length -- clarity over rhythm, not robotic
- **Require:** Explains WHY, not just HOW -- rationale behind technical choices
- **Authority source:** Demonstrated through insider terminology and tradeoff awareness
- **Kata adjustments:**
  - `rhythm-variance`: Relax threshold to 5+ StdDev
  - `hedge-cowardly`: Reclassify precision words as protective
  - `voice-personality`: Light touch -- one human moment per section, not per paragraph
  - `authority-delegated`: Accept "best practices" if followed by specific tradeoff analysis

### Business Writing

- **Require:** Friction acknowledgment -- what challenges exist? What could go wrong?
- **Require:** Clear ownership and next steps -- who does what by when?
- **Watch:** Institutional hiding -- "it is recommended" vs. "I recommend"
- **Authority source:** Numbers with interpretation, not just data dumps
- **Kata adjustments:**
  - `authority-institutional`: Flag passive recommendations aggressively
  - `coherence-floating-claims`: Require grounding for ROI/impact claims
  - `voice-personality`: Professional warmth, not casual -- avoid first-name-basis tone
  - `hedge-cowardly`: Standard threshold applies

### Academic Writing

- **Require:** Synthesis over summarization -- connect sources, don't just list them
- **Require:** Clear contribution statement -- what does this add to the field?
- **Allow:** "It appears that" as epistemic honesty -- genuine uncertainty is a feature
- **Authority source:** Citation genealogy, not just name-dropping -- show how sources relate
- **Kata adjustments:**
  - `hedge-cowardly`: Raise threshold significantly -- most academic hedges are protective
  - `authority-delegated`: Distinguish citation-with-synthesis from citation-as-shield
  - `voice-personality`: Measured expertise -- personality through argument quality, not informality
  - `rhythm-variance`: Accept longer mean sentence length; still flag zero variance

### Creative / Narrative

- **Require:** Surprise -- at least one unexpected element per section
- **Require:** Sensory embodiment -- physical or experiential reality
- **Require:** Specificity that reveals character, not decorates -- functional details
- **Watch:** Generic emotional beats -- "hollow ache" without texture
- **Authority source:** Earned through embodied experience
- **Kata adjustments:**
  - `rhythm-variance`: Enforce aggressively (8+ StdDev) -- rhythm IS the craft
  - `voice-personality`: Required, not optional -- invisible author = failure
  - `coherence-decorative`: Recalibrate -- creative specificity serves character, not just argument
  - `craft-precision`: Replace generic emotional language with sensory grounding

### Personal Writing

- **Require:** Distinctive voice -- the reader should recognize this author
- **Require:** Embodied experience -- physical details, sensory memory, felt knowledge
- **Watch:** Performance of vulnerability vs. real stakes
- **Authority source:** Lived experience, demonstrated through specifics only the author would know
- **Kata adjustments:**
  - `voice-embodiment`: Enforce strictly -- missing embodiment is a MUST_FIX
  - `voice-personality`: Full expression -- controlled informality is baseline, not ceiling
  - `authority-stakes`: Require visible skin in the game
  - `hedge-cowardly`: Low tolerance -- personal writing that hedges its own experience rings false

### Journalistic Writing

- **Allow:** Inverted pyramid structure (lead structure) -- not a template failure
- **Require:** Source attribution -- claims need named or described sources
- **Require:** Clear but present voice -- not neutral wire copy
- **Watch:** False balance on settled questions
- **Authority source:** Access, named sources, on-the-ground reporting
- **Kata adjustments:**
  - `authority-delegated`: Require specific attribution, not "sources say"
  - `coherence-transitions`: Allow topic jumps if following inverted pyramid
  - `voice-personality`: Present but restrained -- the story, not the journalist, leads
  - `hedge-cowardly`: Standard threshold; flag both-sides theater separately

---

## Using Genre Calibration in Agents

Every kata agent receives the detected genre as part of its input context. Agents must:

1. **Read the genre** from the input before processing any text
2. **Adjust thresholds** per the tables and signals above
3. **Tag genre-specific allowances** in edit comments (e.g., "Allowed: academic epistemic hedge")
4. **Never penalize genre-appropriate conventions** -- a technical document with neutral voice is not a voice failure
