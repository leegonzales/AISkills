# Detection Patterns for Writing Quality

Comprehensive patterns for evaluating writing effectiveness across six dimensions: Craft, Coherence, Authority, Purpose, Voice, and Genre Fitness.

**Philosophy Shift (v2):** We evaluate *effectiveness*, not just "AI-ness." Good writing can use transitions; bad writing can avoid them. Context matters. Genre matters.

---

## Genre Detection (Do This First)

Before scoring, identify the genre:
- **Technical:** API docs, tutorials, guides, specs
- **Business:** Reports, proposals, memos, executive summaries
- **Academic:** Papers, essays, literature reviews
- **Creative:** Fiction, narrative nonfiction, personal essays
- **Personal:** Reflections, memoirs, opinion pieces
- **Journalistic:** News, profiles, analysis

**Why First:** A technical doc using consistent sentence length is appropriate; a personal essay doing the same is suspicious.

## Structural Tells

### Sentence Rhythm Issues
**AI Pattern:** Uniform sentence length (20-25 words consistently)
**Human Pattern:** High variance - mix of short (5-10 words) and long (35+ words) sentences
**Detection:** Calculate standard deviation of sentence lengths per paragraph
- Low variance (<5 words) = AI likely
- High variance (>10 words) = Human likely

### Paragraph Templates
**Three-Paragraph Reflex:**
- Introduction → Body → Conclusion even when inappropriate
- Equal-length paragraphs
- Predictable structure regardless of content

**Bullet Point Gravity:**
- Lists used as cognitive escape valve
- Bulleted phrases with bolded titles that restate content
- Format: **Title**: Sentence repeating the title

### Parallel Construction Compulsion
Excessive use of:
- "Not only X, but also Y"
- "Both X and Y"
- "X as well as Y"
- All in same section

## Rhetorical Tells

### Olympian Neutrality
**Pattern:** Refusal to commit to perspective
- Every claim hedged
- "May," "might," "could potentially" in every sentence
- No definitive statements

### Both-Sides Theater
**Pattern:** False balance where none warranted
- "On one hand... on the other hand..." for settled questions
- Equal weight to unequal arguments

### Enthusiasm Simulation
**Pattern:** Generic excitement without specificity
- "Exciting," "fascinating," "remarkable" with no earned detail
- Adjectives unsupported by concrete examples

### Authority Cosplay
**Pattern:** Vague gestures toward expertise
- "Research shows" (no citation)
- "Experts agree" (no experts named)
- "Studies indicate" (no studies specified)

### Empathy Pivot
**Pattern:** Mechanical acknowledgment of humanity
- "It's important to remember that people have feelings"
- Inserted concern that feels performative
- Emotional intelligence without emotional authenticity

### Corporate Opening Gambit
**Pattern:** Business-speak temporal framing (85%+ AI detection rate)
- "In today's rapidly evolving [X] landscape..."
- "In the modern [X] environment..."
- "As we navigate the [X] landscape..."
- "In an increasingly [X] world..."
**Detection:** Opening sentence with temporal vagueness + "landscape/environment/ecosystem" metaphor
**Why it fails:** Generic setup that avoids specific context or timeframe

### Recursive Qualification
**Pattern:** Never stating X without immediately softening X
- Every assertion followed by hedge
- Commitment immediately undermined

## Lexical Tells

### Modifier Inflation
Calculate density of these patterns:
- Adjectives like "comprehensive," "robust," "multifaceted"
- Adverbs like "significantly," "particularly," "notably"
**Threshold:** >3 per 100 words = AI likely

### Hedge Density
Count qualifying phrases per paragraph:
- "It's worth noting"
- "It should be mentioned"
- "It appears that"
**Threshold:** >2 per paragraph = AI likely

### Formal Transition Saturation
Count transitions:
- "Moreover," "Furthermore," "Additionally," "Consequently"
**Threshold:** >1 per 150 words = AI likely

## Punctuation Tells

### Em Dash Overuse
**AI Pattern:** Uses em dashes (—) formulaically
- Where humans use commas or parentheses
- To create false emphasis
- In "punched up" sales-like writing
**Human Pattern:** Uses em dashes sparingly, contextually

### Quotation Mark Style
**AI Tell:** Curly quotes (""'') when straight quotes ("") expected
**Context:** Wikipedia and certain technical contexts

### Semicolon Absence
**AI Pattern:** Rarely uses semicolons
**Human Pattern:** Uses semicolons, colons, variety of punctuation

## Content Tells

### Absence of Specificity
**AI Pattern:**
- Generic examples
- No named sources
- Abstract categories instead of concrete instances
- "Research shows" not "Johnson et al. (2023) found"

**Human Pattern:**
- Specific names, dates, places
- Concrete examples
- Proper nouns
- Numbers and statistics

### Temporal Vagueness
**AI Pattern:**
- "In recent years"
- "Increasingly"
- "Nowadays"
- "In the modern landscape"

**Human Pattern:**
- Specific dates
- Clear timeframes
- Historical context

### Data Injection Pattern
**AI Pattern:** Real data embedded in AI prose
- Specific numbers, names, or facts present BUT:
- Surrounding sentences use AI patterns (hedges, transitions, vagueness)
- Data feels "dropped in" rather than integrated
- Structural/rhetorical patterns remain robotic despite concrete details

**Example:**
"The Tesla Model Y offers impressive capabilities. With 330 miles of range and 384 horsepower, it accelerates 0-60 in 4.8 seconds. Moreover, the vehicle's comprehensive feature set showcases Tesla's commitment to innovation. The multifaceted approach to design underscores the importance of user experience."

**Detection:** Data points (330 miles, 384 hp, 4.8 sec) are specific, but "comprehensive," "showcases," "multifaceted," "underscores" reveal AI generation around human-provided data.

**Scoring adjustment:** Presence of specific data lowers lexical score, but structural/rhetorical patterns may still score high. Consider separately: (1) Data specificity, (2) Prose quality around that data.

### Fake Depth
**AI Pattern:** Polish without substance
- Smooth transitions covering shallow analysis
- Perfect structure masking lack of insight
- Grammatically correct but intellectually empty

## Contextual Tells

### Register Flattening
**AI Pattern:** Mixing academic, corporate, casual without purpose
- Business jargon in creative writing
- Academic formality in emails
- Inconsistent tone within single piece

### Metaphor Mixing
**AI Pattern:** Multiple incompatible metaphors
- "Navigate the landscape of challenges"
- "Delve into the ecosystem of solutions"
- Mixed without awareness

### Missing Vernacular
**AI Pattern:**
- No regionalisms
- No idioms
- No slang
- No dialect markers
- Perfect standardized English

## Detection Workflow

1. **Quick Scan** (30 seconds):
   - Count em dashes
   - Check for "delve," "robust," "showcase"
   - Look for uniform sentence length
   - Spot bullet points with bolded titles

2. **Structural Analysis** (2 minutes):
   - Calculate sentence length variance
   - Check paragraph uniformity
   - Identify template adherence
   - Count transitions per 100 words

3. **Rhetorical Analysis** (3 minutes):
   - Assess commitment level
   - Check for hedge stacking
   - Look for both-sides theater
   - Evaluate specificity of claims

4. **Voice Analysis** (5 minutes):
   - Read aloud - does it breathe?
   - Check for personal markers
   - Look for productive wrongness
   - Assess risk-taking

## Scoring System

**Lexical Score (0-40 points):**
- Banned word density: 0-10 pts
- Hedge phrase density: 0-10 pts
- Transition word density: 0-10 pts
- Modifier inflation: 0-10 pts

**Structural Score (0-30 points):**
- Sentence variance: 0-10 pts
- Paragraph uniformity: 0-10 pts
- Template adherence: 0-10 pts

**Rhetorical Score (0-30 points):**
- Commitment level: 0-10 pts (inverse)
- Specificity: 0-10 pts (inverse)
- Authority claims: 0-10 pts

**Total AI Likelihood:**
- 0-20: Likely human
- 21-40: Possibly AI-assisted
- 41-60: Probably AI-generated
- 61-80: Very likely AI
- 81-100: Almost certainly AI

## False Positives to Avoid

**Not AI Indicators:**
- Perfect grammar (humans can write well too)
- Em dash usage alone (many humans love em dashes)
- Single instance of "robust" or "delve"
- Formal academic writing (legitimately formal)
- Clear, well-organized structure

**Context Matters:**
- Technical documentation appropriately uses "robust," "optimize"
- Academic writing legitimately uses formal transitions
- Business writing may need certain corporate terms
- ESL writers may use different patterns than native speakers

---

## Coherence Patterns (NEW in v2)

Coherence measures whether ideas connect logically, not just syntactically.

### Decorative Specificity

**Pattern:** Precise details that don't advance understanding

**Red Flags:**
- Dates/numbers with no significance ("March 14th" when any date would work)
- Names dropped for texture, not meaning
- Statistics that decorate rather than prove
- Sensory details unconnected to theme

**Example:**
"Margaret, who'd lived at 2847 Oleander Drive for thirty-seven years, noticed the okra hadn't bloomed since March 14th."

**Why it fails:** The address and exact date create specificity *signaling* without specificity *function*. Nothing depends on these details.

**Contrast with functional specificity:**
"The Tesla Model Y delivers 330 miles of range—enough for a Denver-to-Albuquerque trip without charging."
Here, 330 miles *means* something concrete.

### Causal Incoherence

**Pattern:** Claimed cause-effect relationships that don't hold

**Examples:**
- "Her hands were cracked from decades of teaching calculus" (teaching ≠ manual labor)
- "The window was cold, despite the Austin heat reaching 94 degrees" (interior/exterior mismatch)
- "He became CEO because he worked hard" (correlation presented as causation)

**Detection:** Ask "does Y actually follow from X?" for every because/due to/from/since claim.

### Thematic Non-Sequitur

**Pattern:** Conclusions disconnected from preceding content

**Example:**
[Paragraph about garden stagnation] → [Philosophical aside about weeds and poetry]

**Why it fails:** The observation about weeds isn't *earned* by the preceding emotional content. It's a writerly flex, not a character thought.

### Mechanical Variance

**Pattern:** Sentence length varied for its own sake

**What it looks like:**
- Short. Then a longer sentence that adds detail. Short again. Then another deliberately lengthened sentence with additional clauses.

**Why it fails:** Variance should serve rhythm and emphasis, not just meet a metric. The *pattern* of variance matters, not just the StdDev.

### Floating Claims

**Pattern:** Assertions without anchoring

**Example:**
"Digital transformation fails when companies buy expensive software and hope for magic."

**If this is the opening:** Where does this claim come from? What grounds it?
**If preceded by evidence:** Earned and powerful.

**Detection:** For each bold claim, ask "what earned this?"

---

## Authority Patterns (NEW in v2)

Authority measures whether expertise is demonstrated or performed.

### Earned Authority Signals

**Pattern:** Expertise visible through specific knowledge

**Indicators:**
- Insider terminology used correctly (NRR, churn, not just "revenue")
- Tradeoff awareness ("X gives you Y but costs Z")
- Acknowledging limitations without undermining point
- Specific failures/lessons learned
- Consequential details (things only experts would know matter)

**Example:**
"Net revenue retention at 118% means existing customers are spending more—growth without sales costs."

**Why it works:** Interpretation demonstrates understanding, not just data.

### Delegated Authority

**Pattern:** Authority borrowed from external sources

**Indicators:**
- "Research shows..." (no specific research)
- "Best practices recommend..." (which practices? why?)
- Heavy citation without synthesis
- Institutional voice ("it is recommended that...")
- Numbers without interpretation

**Not always bad:** Academic writing legitimately cites. But citation ≠ synthesis.

### False Authority

**Pattern:** Expertise performed without substance

**Indicators:**
- Stereotypes as insider knowledge
- Generic specificity (sounds precise but isn't domain-specific)
- "Experts agree..." (no experts named)
- Confident tone with empty content
- Authority cosplay ("As someone who understands X...")

**Example (fiction):**
"The cubicle smelled like old coffee and desperation."

**Why it fails:** This is *cultural shorthand* for corporate malaise, not authentic observed detail. Anyone could write it; it reveals no insider perspective.

---

## Hedge Classification (NEW in v2)

Not all hedges are bad. Classify before penalizing.

### Cowardly Hedges (PENALIZE)

**Purpose:** Avoid taking a position

**Patterns:**
- "Some might say..." "It could be argued..."
- "In a sense..." "In many ways..."
- "Somewhat," "fairly," "rather," "quite"
- "Perhaps," "maybe" for opinion avoidance
- Multiple hedges stacked: "might potentially somewhat"

### Protective Hedges (PRESERVE)

**Purpose:** Epistemic honesty or precision

**Patterns:**
- "The evidence suggests..." (genuine uncertainty)
- "Current research indicates..." (temporal qualification)
- "Appears to," "likely" (probabilistic accuracy)
- "Certain," "particular," "specific" (precision, not vagueness)
- "In this context..." (scope limitation)

### Classification Rule

Ask: "Is this hedge avoiding opinion or expressing genuine uncertainty?"

- "It could be argued that climate change is real" → COWARDLY (settled question)
- "Early data suggests the treatment is effective" → PROTECTIVE (genuinely uncertain)
- "Some people prefer chocolate" → COWARDLY (why not just say it?)
- "Approximately 40% of participants..." → PROTECTIVE (precision)

---

## Purpose Patterns (NEW in v2)

Purpose measures whether writing has clear intent and stakes.

### Clear Purpose Indicators

- Stakes are explicit (what happens if reader doesn't act/understand?)
- Audience is clear (writing calibrated to specific reader)
- "Why now?" is answered
- Action is implicit or explicit

### Unclear Purpose Indicators

- Could apply to anyone, anytime
- No implicit or explicit action
- No stakes visible
- Reads as performative
- Describes without implying "so what?"

### Purpose Assessment Questions

1. What does the writer want the reader to DO or BELIEVE after reading?
2. Why should the reader care about this NOW?
3. What's at stake if the message fails?
4. Who specifically is this for?

---

## Information Density Patterns (NEW in v2)

Per Gemini critique: AI writing often has uniform medium-density.

### Density Variance

**Quality writing:** Varies density strategically
- Dense sections for important concepts
- Sparse sections for emphasis or rest
- Density serves communication, not fills space

**AI Pattern:** Uniform medium-density
- Every paragraph roughly equally packed
- No sparse moments
- No dense-then-explanation rhythm

### Detection

Read three consecutive paragraphs. Do they vary in density? Or does each have roughly the same information-per-sentence ratio?

---

## Updated Scoring System (v2)

**6-Dimension Framework:**

### Craft Score (0-100)
- Lexical patterns: 0-40 pts (banned words, hedge density, transitions)
- Structural patterns: 0-30 pts (sentence variance, paragraph uniformity)
- Rhetorical patterns: 0-30 pts (commitment, specificity quality)

### Coherence Score (0-100)
- Logical flow: 0-40 pts (ideas connect?)
- Specificity function: 0-30 pts (relevant vs decorative?)
- Transition authenticity: 0-30 pts (earned vs mechanical?)

### Authority Score (0-100)
- Earned signals: 0-40 pts (insider knowledge, tradeoff awareness)
- Delegated handling: 0-30 pts (citation with synthesis?)
- False authority absence: 0-30 pts (no stereotypes as expertise?)

### Purpose Score (0-100)
- Intent clarity: 0-40 pts (what is this FOR?)
- Audience calibration: 0-30 pts (appropriate for reader?)
- Stakes: 0-30 pts (why should reader care?)

### Voice Score (0-100)
- Distinctiveness: 0-40 pts (recognizable author?)
- Embodiment: 0-30 pts (feels like a person?)
- Register appropriateness: 0-30 pts (matches genre?)

### Effectiveness Score
Genre-weighted average of above dimensions.

---

## Genre-Calibrated Thresholds

| Genre | Sentence Variance | Hedge Tolerance | Passive Voice | Template OK | Voice Expectation |
|-------|-------------------|-----------------|---------------|-------------|-------------------|
| Technical | 5+ StdDev | Higher (precision) | Higher | Expected | Neutral authority |
| Business | 6+ StdDev | Standard | Lower | Structure OK | Professional human |
| Academic | 6+ StdDev | Higher (epistemic) | Moderate | If fresh content | Measured expertise |
| Creative | 8+ StdDev | Low | Low | = Failure | Distinctive required |
| Personal | 8+ StdDev | Low | Low | Must be organic | Strongly embodied |
| Journalistic | 7+ StdDev | Standard | Low | Lead structure OK | Clear but present |

---

## Detection Workflow (v2)

1. **Genre Detection** (30 seconds):
   - Identify: Technical / Business / Academic / Creative / Personal / Journalistic
   - Load appropriate thresholds

2. **Quick Scan** (1 minute):
   - Obvious lexical tells (delve, robust, showcase)
   - Uniform sentence length
   - Template structure

3. **Coherence Analysis** (3 minutes):
   - Do ideas connect logically?
   - Is specificity functional or decorative?
   - Are transitions earned?

4. **Authority Analysis** (3 minutes):
   - Is expertise demonstrated or claimed?
   - Are claims grounded?
   - Any false authority patterns?

5. **Craft Analysis** (3 minutes):
   - Lexical density issues
   - Structural patterns
   - Rhetorical execution

6. **Voice/Purpose Analysis** (2 minutes):
   - Distinctive author present?
   - Clear intent?
   - Appropriate register?

7. **Dimension Gap Diagnosis** (1 minute):
   - High craft + low coherence = decorative writing
   - High voice + low authority = personality without substance
   - High authority + low voice = institutional but competent
