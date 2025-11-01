# Prevention Through Prompt Engineering

Systematic approaches to generating better text from the start, avoiding AI clichés before they appear.

## Core Prevention Principles

1. **Negative Examples**: Tell AI what NOT to do
2. **Voice Anchoring**: Provide specific style references
3. **Constraint Specification**: Define boundaries
4. **Commitment Requirements**: Demand perspective
5. **Specificity Mandates**: Require concrete details

---

## Anti-Cliché Prompt Template

### Basic Structure
```
[CONTEXT]
[CONSTRAINTS - what to avoid]
[REQUIREMENTS - what to include]
[SUCCESS CRITERIA - what good looks like]
[VOICE SPECIFICATION - how it should sound]
```

### Full Template
```
Write [TYPE] about [TOPIC] for [AUDIENCE].

CRITICAL - AVOID THESE PATTERNS:
- Never use: delve, robust, showcase, leverage, comprehensive, multifaceted, nuanced
- No hedge stacking: avoid "may potentially," "might possibly," "could arguably"
- No false precision: don't use "this speaks to," "this underscores"
- No meta-commentary: don't narrate what you're doing, just do it
- No both-sides theater on settled questions
- No generic transitions: limit "moreover," "furthermore," "additionally"
- No temporal vagueness: use specific dates, not "in recent years"
- No authority cosplay: if citing research, name the study, or don't cite

REQUIRED ELEMENTS:
- Sentence length variance: mix 5-word punches with 35+ word explorations
- At least ONE specific example with names/numbers/dates per section
- Take a clear position, even if qualified
- Use "because" more than "however"
- Include at least one concrete detail that could only come from domain expertise
- Vary paragraph length (50-200 words per paragraph)

VOICE:
- [SPECIFY: conversational, academic, technical, narrative, etc.]
- Contractions acceptable: [yes/no]
- First person acceptable: [yes/no]
- Fragments for emphasis acceptable: [yes/no]

SUCCESS CRITERIA:
- Reads naturally when spoken aloud
- Contains at least one claim that risks being wrong
- No sentence is interchangeable with generic corporate copy
- Specific enough that domain experts would recognize expertise
```

---

## Domain-Specific Prevention Prompts

### Technical Documentation
```
Write technical documentation for [FEATURE].

BANNED: delve, robust, seamless, intuitive, powerful, flexible, comprehensive
REQUIRED: 
- Specific code examples
- Actual error messages
- Concrete version numbers
- Real file paths
- Step-by-step instructions with expected outputs

VOICE: Clear, direct, assume intelligent reader
ANTI-PATTERN: Don't explain WHY something is good, show HOW to use it
```

### Business Writing
```
Write [MEMO/PROPOSAL/EMAIL] about [TOPIC].

BANNED: synergy, leverage, value-add, game-changer, cutting-edge, paradigm shift, thought leadership
REQUIRED:
- Specific numbers (revenue, costs, timeline)
- Named stakeholders
- Clear action items with owners
- Concrete success metrics

VOICE: Professional but human
- Use "we" and "you"
- Say "use" not "utilize"
- Say "help" not "facilitate"
- Aim for 8th grade reading level
```

### Academic Writing
```
Write [PAPER/ESSAY] on [TOPIC].

ACCEPTABLE: moreover, furthermore (but max 1 per 200 words)
BANNED: 
- Vague citations ("research shows" - name the research)
- Overgeneralization ("always," "never" without qualification)
- Lazy transitions ("as mentioned above")

REQUIRED:
- Specific citations with years
- Concrete examples
- Clear thesis statement
- Logical argument structure
- Acknowledgment of limitations

VOICE: Formal but readable
- Vary sentence length
- Use active voice in results section
- Passive voice acceptable in methods only when appropriate
```

### Creative/Narrative Writing
```
Write [STORY/ESSAY] about [TOPIC].

BANNED: 
- Adjective stacking ("beautiful, majestic, awe-inspiring")
- Cliché metaphors ("time stood still," "heart sank")
- Telling instead of showing
- Perfect grammar that kills voice

REQUIRED:
- Sensory details (what it looked/smelled/sounded like)
- Specific objects, places, times
- Dialogue that sounds like actual speech
- At least one sentence that breaks a grammar rule for effect
- Risk an unconventional metaphor

VOICE: [Specify: literary, pulp, journalistic, confessional, etc.]
```

---

## Negative Prompting Techniques

### Method 1: Explicit Bans
```
NEVER use these words: [list]
NEVER use these phrases: [list]
NEVER use these constructions: [list]
```

### Method 2: Bad Example + Good Example
```
BAD: "The comprehensive implementation of the robust system leverages cutting-edge technology to deliver value-add solutions."

GOOD: "The new system uses machine learning to cut processing time by 60%. We tested it on 10,000 transactions. It works."

Write like the GOOD example, not the BAD example.
```

### Method 3: Failure Mode Description
```
FAILURE MODE TO AVOID:
Your text should NOT sound like:
- A corporate press release
- A LinkedIn influencer post
- An academic abstract generator
- A chatbot trying to sound smart

Instead it should sound like:
- [Specify what it SHOULD sound like]
```

---

## Voice Anchoring Techniques

### Method 1: Style Sample
```
Match the style of this example:
[Paste 200 words of desired style]

Key elements to match:
- Sentence rhythm
- Formality level
- Vocabulary range
- Use of examples
```

### Method 2: Writer Reference
```
Write in the style of [WRITER]:
- [Writer]'s sentence rhythm: [describe]
- [Writer]'s vocabulary: [describe]
- [Writer]'s use of examples: [describe]
- [Writer]'s perspective: [describe]

NOT: Copy their content
BUT: Match their craft
```

### Method 3: Register Specification
```
REGISTER: [journalistic / academic / conversational / technical / literary]

For [REGISTER], this means:
- Sentence length range: [X-Y words]
- Acceptable contractions: [yes/no]
- Acceptable fragments: [yes/no]
- Jargon level: [none/minimal/moderate/specialized]
- Personal pronouns: [yes/no]
- Acceptable informality: [none/mild/moderate/high]
```

---

## Constraint Engineering

### Structural Constraints
```
STRUCTURE REQUIREMENTS:
- Sentence length range: 5-35 words
- Paragraph length range: 50-200 words
- No more than 2 bullet lists in entire piece
- No parallel constructions ("not only... but also")
- At least 3 sentence structures per paragraph
- Maximum 1 transition word per 100 words
```

### Content Constraints
```
CONTENT REQUIREMENTS:
- At least 1 specific example per 200 words
- At least 1 named source per major claim
- At least 1 concrete number per section
- Zero generic examples ("many companies," "research shows")
- Zero temporal vagueness ("recently," "in modern times")
```

### Voice Constraints
```
VOICE REQUIREMENTS:
- Read aloud test: must sound natural
- Specificity test: domain experts must recognize expertise
- Risk test: at least 1 claim that could be contested
- Embodiment test: must feel like a human thinking, not a database reporting
```

---

## Commitment Forcing

### Position Requirement
```
You MUST take a clear position on [ISSUE].

NOT ACCEPTABLE: "There are advantages and disadvantages to both approaches."
ACCEPTABLE: "Approach A is better for [context] because [specific reasons]. Approach B fails when [specific failure mode]."

Qualification is fine, but neutrality is not.
```

### Specificity Forcing
```
For EVERY claim, provide:
- At least one concrete example
- At least one specific number, name, or date
- At least one detail that demonstrates domain knowledge

Generic claims will be rejected and must be rewritten.
```

### Certainty Calibration
```
Hedge ONLY when uncertainty is genuine:
- Limited data → hedge + explain data limitations
- Context dependency → state boundary conditions
- Genuine ambiguity → explain source of ambiguity

Do NOT hedge out of:
- Politeness
- Fear of being wrong
- Desire to cover all bases
```

---

## Iteration Prompts

### Round 1: First Draft
```
Write [CONTENT] following anti-cliché guidelines above.
```

### Round 2: Rhythm Fix
```
Rewrite with more aggressive sentence length variation:
- Add at least 3 sentences under 10 words
- Add at least 2 sentences over 30 words
- Break up uniform middle-length sentences
```

### Round 3: Commitment Injection
```
Rewrite with stronger commitments:
- Remove 50% of hedges
- Add specific examples to generic claims
- Take a clearer position where waffling
```

### Round 4: Voice Enhancement
```
Add voice without losing clarity:
- Add 1 colloquialism per 200 words
- Include 1 personal marker per 300 words
- Let 1 sentence be grammatically imperfect for emphasis
```

---

## Quality Verification Prompts

### Self-Check Prompt
```
Review your own output:
1. Count instances of banned words. If >0, rewrite.
2. Count "however" vs "because". Ratio should favor "because".
3. Check sentence length variance. Standard deviation >8 words?
4. Read aloud. Does it sound like human breath or robot?
5. List the specific examples. Are there any? If <1 per 200 words, add more.
```

### Meta-Improvement Prompt
```
You just wrote [CONTENT].

Now critique it:
- What clichés slipped through?
- Where did you hedge unnecessarily?
- Which sentences are interchangeable with generic content?
- What specific details are missing?

Then rewrite addressing these issues.
```

---

## Examples: Before & After

### Example 1: Technical
**Generic Prompt:** "Write about API design"

**Anti-Cliché Prompt:**
```
Write 300 words about REST API design for backend engineers.

BANNED: robust, seamless, powerful, flexible, scalable
REQUIRED:
- Specific HTTP methods and status codes
- At least one code example
- At least one concrete antipattern with explanation

VOICE: Technical, direct, assume smart reader
```

### Example 2: Business
**Generic Prompt:** "Write a memo about the new policy"

**Anti-Cliché Prompt:**
```
Write a 200-word memo announcing the remote work policy change.

BANNED: leverage, synergy, going forward, moving forward
REQUIRED:
- Specific effective date
- Specific number of required office days
- Specific person to contact with questions
- Concrete reason for change (budget number or survey result)

VOICE: Professional but human, use "you" and "we"
```

### Example 3: Creative
**Generic Prompt:** "Write a story about a musician"

**Anti-Cliché Prompt:**
```
Write 400 words about a jazz drummer in 1960s Harlem.

BANNED: 
- Generic adjectives ("beautiful," "amazing")
- Telling emotions ("she felt sad")
- Cliché metaphors ("music was her life")

REQUIRED:
- Specific venue name
- Specific song or musician reference
- Sensory detail (what the club smelled like, what the drums sounded like)
- One sentence that breaks grammar for rhythm

VOICE: Literary but accessible, show don't tell
```

---

## Prevention Checklist

Before generating, ensure prompt includes:

- [ ] Explicit banned words list
- [ ] Structural requirements (sentence/paragraph variance)
- [ ] Specificity requirements (examples, numbers, names)
- [ ] Voice specification (register, formality, perspective)
- [ ] Commitment requirements (take a position)
- [ ] Quality criteria (read aloud test, specificity test, risk test)
- [ ] Negative examples (what NOT to sound like)
- [ ] Success criteria (what good looks like)
