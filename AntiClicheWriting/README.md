# Anti-Cliché Writing

Comprehensive detection, prevention, and remediation of AI writing clichés. Elevate text to human-quality or better through systematic analysis and targeted interventions.

## What Is Anti-Cliché Writing?

This skill helps you identify and eliminate robotic AI writing patterns through:
- **Detection**: Multi-layer analysis scoring text for AI tells
- **Remediation**: Systematic elevation using the Three Pillars framework
- **Prevention**: Prompt engineering to generate quality text from the start
- **Training**: Teaching pattern recognition and craft principles

## Use Cases

- **Polish AI-Generated Content**: Remove robotic patterns and add craft
- **Analyze Writing Quality**: Systematic scoring with actionable feedback
- **Generate Better Content**: Anti-cliché constraints built into prompts
- **Teach Writing Skills**: Help others recognize and fix AI patterns
- **Client Deliverables**: Ensure professional, high-quality outputs

## Core Capabilities

### 1. Detection & Analysis

Analyze text for AI writing patterns across four layers:

**Lexical Layer (40 points)**
- Banned word density ("delve," "meticulous," "robust")
- Hedge phrase frequency ("It's worth noting," "arguably")
- Transition overuse

**Structural Layer (30 points)**
- Sentence length variance (humans vary more)
- Paragraph uniformity (AI loves consistency)
- Template detection (bullet points, em-dashes)

**Rhetorical Layer (30 points)**
- Commitment level (hedging vs. claiming)
- Specificity (vague vs. concrete)
- Authority claims without evidence

**Voice Assessment (qualitative)**
- Embodiment (does the writer exist in the text?)
- Vernacular (conversational vs. academic drone)
- Risk-taking (safe vs. opinionated)

**Output**: Scored report (0-100) with severity levels and top 5 priority fixes

### 2. Elevation & Remediation

Three-pass framework for systematic improvement:

**Pass 1 - Rhythm**
- Vary sentence length (target StdDev > 8 words)
- Break structural uniformity
- Remove template patterns

**Pass 2 - Commitment**
- Delete hedge phrases
- Add specific details
- Replace vague with concrete

**Pass 3 - Voice**
- Inject personality
- Add embodiment
- Take calculated risks

**Output**: Rewritten text with before/after examples and explanations

### 3. Prevention

Generate quality content from the start using anti-cliché prompts:

**5-Component Template**
1. Context (what you're creating)
2. Constraints (what to avoid)
3. Requirements (what to include)
4. Success criteria (how to measure quality)
5. Voice specification (how it should sound)

**Output**: Optimized prompt that prevents AI patterns

### 4. Training

Build pattern recognition skills through:
- Comparative analysis (before/after examples)
- WHY explanations (not just what's wrong)
- Quality standards (Read-aloud, Surprise, Specificity, Risk, Embodiment tests)
- Practice exercises

## Quick Start

### Detect AI Patterns

```
"Analyze this text for AI writing patterns"
```

Claude will load detection patterns and provide a scored report.

### Improve Existing Text

```
"Elevate this text - aggressive rewrite"
```

Claude will apply the Three Pillars framework and rewrite with explanations.

### Generate Quality Content

```
"Help me write [topic] with anti-cliché prevention"
```

Claude will build an optimized prompt to generate better text from the start.

### Learn Pattern Recognition

```
"Teach me to recognize AI writing clichés"
```

Claude will provide examples, explanations, and training exercises.

## Installation

### For Claude Code

```bash
# Personal skills (globally available)
cp -r AntiClicheWriting/anti-cliche-writing ~/.claude/skills/

# Project skills (project-specific)
mkdir -p .claude/skills
cp -r AntiClicheWriting/anti-cliche-writing .claude/skills/
```

### For General Claude Conversations

Upload `AI Writing Clichés Guide.skill` directly to any Claude conversation.

## Features

### Research-Backed Detection

Incorporates findings from:
- Wikipedia's AI writing pattern catalog
- GPTZero frequency analysis (20x multipliers for "showcases," "underscores")
- Academic studies on sentence variance and pronoun usage

### Register-Specific Guidelines

Different rules for different contexts:

**Technical Documentation**
- "Robust" is acceptable
- Specificity required
- Less personality needed

**Business Writing**
- Professional but not robotic
- Confidence without hedging
- Results-focused

**Academic Writing**
- Rigorous but not lifeless
- Evidence-based claims
- Appropriate hedging (sometimes)

**Creative/Narrative**
- Voice paramount
- Risk-taking encouraged
- Show, don't tell

### Quality-First Philosophy

**Not about bypassing AI detectors**

Focus on craft principles:
- Voice and embodiment
- Commitment and specificity
- Rhythm and variation
- Risk and personality

The goal is excellent writing, not undetectable AI output.

## Structure

```
AntiClicheWriting/
├── README.md                                      # This file
├── AI Writing Clichés Review.md                   # Goal alignment assessment
├── AI Writing Clichés Guide.skill                 # Packaged skill file
└── anti-cliche-writing/                           # Main skill directory
    ├── SKILL.md                                   # Skill definition
    └── references/
        ├── ai-vocabulary.md                       # Banned words with frequency data
        ├── detection-patterns.md                  # Multi-layer analysis patterns
        ├── prevention-prompts.md                  # Prompt engineering templates
        └── remediation-strategies.md              # Three Pillars framework
```

## Examples

### Detection Report

```
AI WRITING ANALYSIS
Overall Score: 58/100 - Probably AI-generated

LEXICAL ISSUES (Score: 24/40)
- "Delve": 3 instances - Lines 2, 15, 23
- "Robust": 2 instances - Lines 8, 19
- Hedge phrases: 7 instances
Severity: High

TOP 5 PRIORITY FIXES:
1. Remove "delve" (3x) - use specific action verbs
2. Delete hedge phrases - commit to claims
3. Vary sentence length (current StdDev: 4.2, need >8)
4. Add concrete examples (currently all abstract)
5. Inject personality - text has no author presence
```

### Remediation Example

**Before:**
"It's worth noting that the implementation showcases a robust approach to the challenge, particularly in terms of scalability."

**After:**
"The system scales. Three load tests confirm it handles 10x traffic without failures."

**Why:**
- Removed hedge ("It's worth noting")
- Deleted cliché words ("showcases," "robust")
- Added specificity (3 tests, 10x metric)
- Shortened from 19 to 11 words
- Made falsifiable claim

## Best Practices

1. **Start with Prevention**: Use anti-cliché prompts when generating new content
2. **Detect Before Remediate**: Understand what's wrong before fixing
3. **Choose Appropriate Aggressiveness**: Light touch for polish, aggressive for rewrites
4. **Learn the Patterns**: Use training mode to build your own judgment
5. **Context Matters**: Apply register-specific rules

## Advanced Usage

### Custom Aggressiveness Levels

```
"Elevate this - conservative suggestions only"
"Elevate this - moderate rewrite" (default)
"Elevate this - aggressive complete rewrite"
```

### Specific Layer Focus

```
"Analyze just the lexical layer"
"Fix only structural issues"
"Add voice without changing content"
```

### Register-Specific Analysis

```
"Analyze this technical doc for AI patterns"
"Elevate this business proposal - keep it professional"
"Make this creative piece more embodied"
```

## Limitations

**V1 does not include:**
- Machine learning detection (statistical only)
- User preference learning over time
- Voice exemplar training from samples
- Interactive practice exercises
- Batch document processing

These are reasonable V2 enhancements but V1 provides complete, usable functionality.

## Design Philosophy

This skill follows research-backed, quality-first principles:

1. **Comprehensive**: Only system with detection + remediation + prevention + training
2. **Systematic**: Clear frameworks (Three Pillars, Multi-Layer Analysis)
3. **Research-Backed**: Incorporates Wikipedia, GPTZero, academic findings
4. **Pedagogical**: Explains WHY, not just WHAT
5. **Quality-Focused**: Craft over evasion
6. **Practical**: Concrete templates and examples

## Contributing

Contributions welcome! Consider adding:
- Additional detection patterns
- Register-specific guidelines for new domains
- Before/after examples
- Training exercises
- Voice exemplar libraries

## Questions?

- Check [AI Writing Clichés Review.md](AI%20Writing%20Clichés%20Review.md) for design rationale
- See individual reference files for detailed patterns and strategies
- Ask Claude to explain any analysis or recommendation

---

Built with Claude Code Skills | Quality-First AI Writing
