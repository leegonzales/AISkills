---
name: prose-polish
description: Polish writing to professional excellence through systematic craft analysis with multi-layer assessment of rhythm, voice, and commitment. Use when refining drafts, analyzing text for AI patterns or craft weaknesses, generating quality content, or teaching writing principles. Handles all writing types including long-form, business, technical, academic, and creative content.
---

# Prose Polish

Elevate writing to professional excellence through systematic craft analysis. Multi-layer assessment of rhythm, voice, and commitment with targeted remediation using proven frameworks.

## Quick Start

**Detection:** Analyze text → Load `detection-patterns.md` → Generate scored report with specific issues

**Elevation:** Improve text → Load `detection-patterns.md` + `remediation-strategies.md` → Apply fixes → Provide rewritten version with explanations

**Prevention:** Generate content → Load `prevention-prompts.md` → Build anti-cliché prompt → Create quality text from start

## Core Capabilities

### 1. Detection & Analysis
**When:** User asks to "analyze," "detect," "check," or "score" text for AI patterns

**Process:**
1. Load `references/detection-patterns.md`
2. Perform multi-layer analysis:
   - **Lexical:** Banned word density, hedge phrases, transitions
   - **Structural:** Sentence variance, paragraph uniformity, templates
   - **Rhetorical:** Commitment level, specificity, authority claims
   - **Voice:** Embodiment, vernacular, risk-taking
3. Generate diagnostic report

**Report Format:**
```
AI WRITING ANALYSIS
Overall Score: [X/100] - [Interpretation]

LEXICAL ISSUES (Score: X/40)
- [Issue]: [Count] instances - Lines [X, Y, Z]
- Severity: [High/Medium/Low]

STRUCTURAL ISSUES (Score: X/30)
- Sentence length variance: [StdDev] words (need >8)
- [Other issues]

RHETORICAL ISSUES (Score: X/30)
- [Issues with examples]

VOICE ASSESSMENT:
- [Observations]

TOP 5 PRIORITY FIXES:
1. [Specific, actionable]
2. [...]
```

**Score Interpretation:**
- 0-20: Likely human
- 21-40: Possibly AI-assisted
- 41-60: Probably AI-generated
- 61-80: Very likely AI
- 81-100: Almost certainly unedited AI

**Real-World Context:** Content marketing and business copy frequently scores 60-80+. Technical and creative writing with specific details typically scores lower. High scores indicate pattern density, not necessarily deception—sometimes AI patterns reflect genre conventions in corporate communication.

### 2. Elevation & Remediation
**When:** User asks to "improve," "fix," "elevate," or "rewrite" text

**Process:**
1. Detect issues (brief analysis)
2. Load `references/remediation-strategies.md`
3. Choose approach by severity:
   - Light (20-40): Surgical fixes only
   - Moderate (41-60): Surgical + structural
   - Aggressive (61+): Comprehensive rewrite
4. Apply Three-Pass Remediation:
   - **Round 1 - Rhythm:** Sentence variance, structure breaks
   - **Round 2 - Commitment:** Remove hedges, add specificity
   - **Round 3 - Voice:** Add embodiment, personality, risk

**Output:**
```
ELEVATED VERSION:
[Rewritten text]

KEY CHANGES:
1. Rhythm: [Sentence variation details]
2. Commitment: [Hedge removal, specificity additions]
3. Voice: [Personality injections]

BEFORE/AFTER EXAMPLES:
Before: "[Original]"
After: "[Rewritten]"
Why: [Principle violated → principle applied]

[3-5 examples of key transformations]
```

**Aggressiveness Levels:**
- **Conservative:** Suggest alternatives, user decides
- **Moderate (DEFAULT):** Rewrite with explanations
- **Aggressive:** Complete rewrite, brief explanation

### 3. Prevention & Generation
**When:** User asks to "write" or "generate" with quality emphasis

**Process:**
1. Load `references/prevention-prompts.md`
2. Construct anti-cliché prompt based on:
   - Content type (technical/business/academic/creative)
   - Audience and register
   - Specific requirements
3. Generate with constraints:
   - Banned words avoided
   - Sentence variance required
   - Specificity mandated
   - Commitment required
   - Voice specified
4. Self-verify against standards
5. Refine if needed

**Prompt Template (from prevention-prompts.md):**
```
Write [TYPE] about [TOPIC] for [AUDIENCE].

AVOID: [banned patterns]
REQUIRE: [structural + content requirements]
VOICE: [register specification]
SUCCESS CRITERIA: [quality checks]
```

### 4. Training & Teaching
**When:** User wants to learn pattern recognition

**Process:**
1. Load appropriate reference files
2. Provide annotated examples
3. Explain WHY patterns fail (not just THAT they fail)
4. Give comparative analysis
5. Offer practice exercises

**Focus:** Build judgment, not just pattern matching

## Register-Specific Guidelines

### Technical Documentation
- **Allow:** "robust," "optimize," "architecture" (contextually)
- **Ban:** "delve," "comprehensive," unnecessary adjectives
- **Require:** Code examples, version numbers, concrete steps
- **Voice:** Clear, direct, assume intelligent reader

### Business Writing
- **Ban:** Synergy, leverage, value-add, thought leadership, paradigm shift
- **Require:** Numbers, names, dates, specific owners, action items
- **Voice:** Professional but human (use "we/you", contractions OK)
- **Target:** 8th grade reading level

### Academic Writing
- **Allow:** "Moreover," "furthermore" (max 1 per 200 words)
- **Ban:** Vague citations, overgeneralization
- **Require:** Specific citations with years, concrete examples, clear thesis
- **Voice:** Formal but readable, active voice in results

### Creative/Narrative
- **Ban:** Adjective stacking, cliché metaphors, telling vs showing
- **Require:** Sensory details, specific objects/places/times, natural dialogue
- **Voice:** Match genre while maintaining personality
- **Allow:** Grammar breaks for effect

## Quality Standards

Every output must pass:

**Read-Aloud Test:** Sounds like human breath and thinking?
**Surprise Test:** Contains ≥1 unexpected sentence?
**Specificity Test:** Includes concrete details (names/numbers/dates)?
**Risk Test:** Makes ≥1 contestable claim?
**Embodiment Test:** Feels like it came from someone with body and experiences?

## Workflow Decision Tree

```
User Request
├─ "Analyze this" → Mode 1: Detection
│   └─ Load detection-patterns.md → Generate report
│
├─ "Fix/improve this" → Mode 2: Elevation
│   └─ Load detection + remediation → Diagnose → Fix → Explain
│
├─ "Write X" (quality focus) → Mode 3: Prevention
│   └─ Load prevention-prompts → Build constraints → Generate → Verify
│
└─ "Teach me about patterns" → Mode 4: Training
    └─ Load relevant references → Examples → Explanations → Practice
```

## Reference Files

**When to Load:**
- **ai-vocabulary.md:** Detecting lexical patterns, need banned word lists
- **detection-patterns.md:** Analyzing text, performing diagnosis (ALWAYS for detection/remediation)
- **remediation-strategies.md:** Fixing issues, improving text (ALWAYS for remediation)
- **prevention-prompts.md:** Generating new content, building prompts (ALWAYS for prevention)

**Loading Strategy:**
- Detection: detection-patterns.md
- Remediation: detection-patterns.md + remediation-strategies.md
- Prevention: prevention-prompts.md
- Teaching: Whichever relevant to lesson

## Critical Principles

1. **Quality Over Undetectability:** Goal is excellent writing, not bypassing detectors. Optimize for craft: voice, commitment, specificity, rhythm.

2. **Context Matters:** Different registers have different rules. Technical ≠ creative ≠ business.

3. **Taste Over Rules:** Rules guide but don't dictate. Sometimes "delve" is fine (rarely). Sometimes hedging is appropriate (genuine uncertainty).

4. **Pedagogy Matters:** When teaching, explain WHY not just WHAT. Build judgment, not pattern matching.

5. **Embodiment Is Key:** Best writing feels like a human thinking, breathing, risking. That's the target.

## Examples

### Detection Example

**Input:** "In today's rapidly evolving digital landscape, organizations must leverage robust solutions to achieve comprehensive transformation. This underscores the pivotal importance of strategic alignment."

**Output:**
```
AI WRITING ANALYSIS
Overall Score: 78/100 - Very Likely AI-Generated

LEXICAL ISSUES (35/40):
- "leverage" (line 1) - AI overuse
- "robust solutions" (line 1) - Generic phrase
- "comprehensive" (line 1) - Modifier inflation
- "underscores" (line 2) - False precision (18x)
- "pivotal" (line 2) - AI overuse marker
Severity: HIGH

STRUCTURAL (25/30):
- Sentence length: 14, 12 words - Low variance (need >8 StdDev)
- Corporate template detected
Severity: MEDIUM

RHETORICAL (18/30):
- Zero specificity (no names/numbers/dates)
- "This underscores" - Meta-commentary
- No concrete claims
Severity: HIGH

TOP 5 FIXES:
1. Replace "leverage robust solutions" with specific action + tool
2. Add concrete example with actual numbers
3. Remove "underscores the pivotal importance"
4. State actual claim directly
5. Add sentence variance (5-word punch + 30+ word exploration)
```

### Elevation Example

**Same input as above**

**Output:**
```
ELEVATED VERSION:
Digital transformation fails when companies buy expensive software and hope for magic. Here's what actually works: Pick one process—customer onboarding, for example. Map every step. Identify the three biggest bottlenecks. Fix those first with the simplest tool that addresses the actual problem. Salesforce used this approach to cut onboarding time from 6 weeks to 8 days.

KEY CHANGES:
1. Rhythm: Added 5-word punch ("Here's what actually works"), varied length (5-25 words), StdDev jumped from 1 to 8
2. Commitment: Direct position ("fails when"), removed all hedges, added specific example (Salesforce, 6 weeks → 8 days, named process)
3. Voice: Conversational, direct address, specific advice, slight informality ("hope for magic")

BEFORE/AFTER:
Before: "In today's rapidly evolving digital landscape, organizations must leverage robust solutions"
After: "Digital transformation fails when companies buy expensive software and hope for magic"
Why: Removed temporal vagueness + corporate jargon + hedge ("must") → Added direct position + specificity + voice
```

### Prevention Example

**User Request:** "Write about API design for backend engineers"

**Anti-Cliché Prompt Constructed:**
```
Write 300 words about REST API design for backend engineers.

BANNED: robust, seamless, powerful, flexible, scalable, comprehensive
REQUIRED:
- Specific HTTP methods and status codes
- At least one code example
- At least one concrete antipattern with explanation
- Sentence variance: 5-35 word range
- At least one specific number or stat

VOICE: Technical, direct, assume smart reader
- No meta-commentary
- Active voice
- Contractions acceptable
- Aim for 10th grade reading level despite technical content
```

**Generated Output:**
[Would then generate API design content following these constraints]

## Success Metrics

**Objective:**
- AI likelihood score ↓ by 40+ points
- Sentence length std dev ↑ by 5+ words
- Hedge phrase density ↓ by 70%
- Specific examples added (≥1 per 200 words)

**Subjective:**
- Reads naturally when spoken aloud
- User recognizes improvement immediately
- Text feels distinctly non-AI
- Domain experts recognize authentic expertise

## Notes

- This skill scaffolds judgment, doesn't replace it
- Rules are guidelines, not laws
- Best results from understanding principles, not memorizing lists
- Goal: Writing that matters—specific, committed, embodied
