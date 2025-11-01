# Detection Patterns for AI Writing

Comprehensive patterns for identifying AI-generated or AI-influenced text.

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
