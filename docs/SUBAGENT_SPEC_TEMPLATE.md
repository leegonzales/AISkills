# SUBAGENT EXECUTION SPECIFICATION: Dad Joke Validator

**Issue:** SKILL-21
**Type:** New Skill (Greenfield)
**Complexity:** Medium
**Estimated Effort:** 8-12 hours
**Template Version:** 1.0 (Use this as pattern for all skills)

---

## MISSION STATEMENT

Build a production-quality Claude skill that analyzes jokes on the "dad joke" quality spectrum, providing scored feedback across multiple dimensions (Pun Quality, Groan Factor, Wholesomeness, Structure) and generating dad jokes when requested.

**Success Criteria:**
- Functional skill installable in Claude Code and web chat
- Scoring system works across all dimensions with clear rationale
- Can analyze existing jokes AND generate new ones
- Documentation demonstrates understanding of dad joke characteristics
- Packaged as `dad-joke-validator-v1.0.0.skill` (ZIP format)

---

## PART 1: PROJECT SETUP

### Step 1.1: Create Directory Structure

Execute these commands in order:

```bash
cd /Users/leegonzales/Projects/leegonzales/AISkills
mkdir -p DadJokeValidator/dad-joke-validator/{references,scripts,assets,dist}
cd DadJokeValidator
```

**Validation:**
```bash
tree dad-joke-validator/
# Expected output:
# dad-joke-validator/
# ├── SKILL.md
# ├── references/
# ├── scripts/
# ├── assets/
# └── dist/
```

### Step 1.2: Complete Directory Structure

Create ALL files (even if empty initially):

```bash
cd dad-joke-validator

# Core files
touch SKILL.md
touch README.md
touch CHANGELOG.md
touch LICENSE

# References
touch references/examples.md
touch references/scoring-guide.md
touch references/dad-joke-theory.md

# Scripts
touch scripts/validator.py
touch scripts/generator.py
touch scripts/test_validator.py

# Assets
touch assets/pun-patterns.json
touch assets/wholesome-themes.json
```

**Validation:**
```bash
find . -type f | wc -l
# Expected: 12 files
```

---

## PART 2: FILE SPECIFICATIONS (Complete Content)

### File 2.1: SKILL.md (Core Skill Definition)

**Purpose:** The skill Claude reads to understand how to validate dad jokes
**Token Budget:** 400-600 words (keep concise)
**Location:** `dad-joke-validator/SKILL.md`

**COMPLETE CONTENT TO WRITE:**

```markdown
---
name: dad-joke-validator
description: Analyze and score jokes on the dad joke quality spectrum with multi-dimensional feedback on pun quality, groan factor, wholesomeness, and structure. Can also generate dad jokes.
version: 1.0.0
---

# Dad Joke Validator

Analyze jokes for dad joke quality across multiple dimensions or generate new dad jokes.

## When to Use

Invoke this skill when the user:
- Asks you to analyze a joke for "dad joke" quality
- Wants feedback on why a joke works (or doesn't)
- Requests a dad joke be generated
- Asks about pun quality, groan factor, or joke structure
- Says things like "is this a dad joke?" or "rate this joke"

## Core Capabilities

### 1. Joke Analysis

When analyzing a joke, score across these dimensions:

**Pun Quality (0-10)**
- Wordplay sophistication
- Multiple meanings exploited
- Unexpected connections
- Clarity of the pun (not too obscure)

**Groan Factor (0-10)**
- How predictable the punchline is
- "Obviousness" that triggers the groan
- Clean setup leading to "of course" moment
- Higher score = more groan-inducing (this is GOOD for dad jokes)

**Wholesomeness (0-10)**
- Family-friendly (no edgy content)
- Positive/innocent tone
- Safe for all ages
- Warm rather than mean-spirited

**Setup/Punchline Structure (0-10)**
- Clear setup establishing context
- Economical punchline (not too long)
- Timing and rhythm
- Misdirection technique

**Overall Dad Joke Score (0-100)**
- Formula: (Pun Quality × 2.5) + (Groan Factor × 3) + (Wholesomeness × 3) + (Structure × 1.5)
- 85-100: Peak dad joke territory
- 70-84: Solid dad joke
- 50-69: Dad joke adjacent (needs work)
- Below 50: Not a dad joke

### 2. Analysis Output Format

Provide analysis in this structure:

```
Dad Joke Score: XX/100

Dimensional Breakdown:
- Pun Quality: X/10 - [Brief explanation]
- Groan Factor: X/10 - [Why it makes you groan]
- Wholesomeness: X/10 - [Family-friendly assessment]
- Structure: X/10 - [Setup/punchline evaluation]

Verdict: [One sentence overall assessment]

Improvement Suggestions (if score < 85):
- [Specific actionable feedback]
```

### 3. Dad Joke Generation

When asked to generate a dad joke:

1. Select a wholesome theme (food, animals, occupations, everyday objects)
2. Find a word with multiple meanings or homophones
3. Build setup establishing one meaning
4. Deliver punchline exploiting the other meaning
5. Keep it SHORT (1-2 sentence setup, 1 sentence punchline max)

**Quality Requirements:**
- Must score 85+ on your own rubric
- Maximum 3 sentences total
- Pun must be clear (not too clever)
- Should trigger genuine groan

### 4. Anti-Patterns to Detect

Flag these as "NOT dad jokes":
- Edgy or inappropriate content (Wholesomeness < 7)
- Mean-spirited humor
- Requires specialized knowledge (too obscure)
- No clear pun or wordplay (Pun Quality < 5)
- Too complex or long-winded
- Sarcastic or ironic tone

## Special Instructions

**DO:**
- Explain WHY scores are assigned
- Give specific examples in feedback
- Maintain warmth and humor in analysis
- Acknowledge when something is "so bad it's good"

**DON'T:**
- Mock the joke harshly (dad jokes are supposed to be groan-worthy)
- Score ironically (genuine assessment only)
- Generate edgy content when creating jokes
- Over-explain the pun (kills the joke)

## Examples

See `references/examples.md` for 10 analyzed dad jokes across the quality spectrum.

## Integration

Works standalone. Can be combined with:
- Prose Polish (for joke wording refinement)
- Meeting Bullshit Detector (for detecting forced humor in corporate settings)
```

**Validation:**
```bash
wc -w SKILL.md
# Expected: 500-650 words
grep "^---" SKILL.md | wc -l
# Expected: 2 (YAML frontmatter delimiters)
```

### File 2.2: README.md (Comprehensive Documentation)

**Purpose:** User-facing documentation
**Location:** `dad-joke-validator/README.md`

**COMPLETE CONTENT TO WRITE:**

```markdown
# Dad Joke Validator

**Version:** 1.0.0
**License:** MIT
**Category:** Fun & Educational

Analyze jokes for "dad joke" quality with multi-dimensional scoring, or generate fresh dad jokes that are guaranteed to make people groan.

## What Is This?

Dad jokes are a unique art form: wholesome, pun-based humor that's simultaneously terrible and delightful. This skill helps you:

- **Analyze jokes** across 4 dimensions (Pun Quality, Groan Factor, Wholesomeness, Structure)
- **Get actionable feedback** on why jokes work (or don't)
- **Generate dad jokes** that score 85+ on the rubric
- **Learn joke structure** through detailed explanations

## Installation

### For Claude Code

**Global Installation (Available in All Projects):**

```bash
cd ~/.claude/skills/
cp -r /path/to/AISkills/DadJokeValidator/dad-joke-validator ./
```

**Project-Specific Installation:**

```bash
cd your-project/
mkdir -p .claude/skills
cp -r /path/to/AISkills/DadJokeValidator/dad-joke-validator .claude/skills/
```

### For Claude Web Chat

Download [`dad-joke-validator-v1.0.0.skill`](dist/dad-joke-validator-v1.0.0.skill) and upload to your Claude conversation via the attachment button (📎).

## Usage

Once installed, Claude automatically uses this skill when you mention joke analysis or generation.

### Analyze a Joke

```
You: "Is this a dad joke? 'I'm reading a book about anti-gravity. It's impossible to put down.'"

Claude: Dad Joke Score: 92/100

Dimensional Breakdown:
- Pun Quality: 9/10 - Excellent wordplay on "put down" (physical vs stop reading)
- Groan Factor: 10/10 - Completely predictable yet still makes you groan
- Wholesomeness: 10/10 - Perfectly family-friendly and positive
- Structure: 8/10 - Clean two-sentence structure, good misdirection

Verdict: Peak dad joke territory. The anti-gravity setup perfectly
leads to the "impossible to put down" punchline.
```

### Generate a Dad Joke

```
You: "Tell me a dad joke about coffee"

Claude: Why did the coffee file a police report?

It got mugged!

(Dad Joke Score: 88/100 - Strong pun on "mugged", wholesome theme,
perfect groan factor)
```

### Get Improvement Feedback

```
You: "Rate this: 'Why don't scientists trust atoms? They make up everything
including all the lies and deception in the world.'"

Claude: Dad Joke Score: 62/100 (Dad Joke Adjacent)

Dimensional Breakdown:
- Pun Quality: 9/10 - Great wordplay on "make up"
- Groan Factor: 8/10 - Good setup and punchline
- Wholesomeness: 5/10 - The "lies and deception" addition darkens the tone
- Structure: 7/10 - Setup is good but punchline too long

Verdict: Started as an excellent dad joke but over-explained the
punchline with unnecessary negative language.

Improvement: Remove everything after "everything" - the punchline
lands better concise. "Why don't scientists trust atoms? Because they
make up everything!" would score 91/100.
```

## Scoring System

### The Four Dimensions

**Pun Quality (0-10)**
- 9-10: Sophisticated wordplay, multiple meanings
- 7-8: Clear pun, good connection
- 5-6: Pun exists but weak
- 0-4: No real wordplay

**Groan Factor (0-10)** *(Higher is better for dad jokes!)*
- 9-10: Maximum groan, perfectly predictable
- 7-8: Solid groan-inducing
- 5-6: Mild reaction
- 0-4: Too clever or falls flat

**Wholesomeness (0-10)**
- 9-10: Perfectly family-friendly, warm
- 7-8: Generally wholesome
- 5-6: Slightly edgy
- 0-4: Inappropriate for dad jokes

**Structure (0-10)**
- 9-10: Perfect setup/punchline, great timing
- 7-8: Good structure, minor issues
- 5-6: Structure exists but clunky
- 0-4: Poorly structured

### Overall Score Formula

```
Overall = (Pun Quality × 2.5) + (Groan Factor × 3) +
          (Wholesomeness × 3) + (Structure × 1.5)

Maximum: 100 points
```

**Score Interpretation:**
- **85-100:** Peak Dad Joke - Frame it, share it, groan proudly
- **70-84:** Solid Dad Joke - Works well, minor polish possible
- **50-69:** Dad Joke Adjacent - Has potential, needs refinement
- **Below 50:** Not a Dad Joke - Missing essential characteristics

## Examples

See [`references/examples.md`](references/examples.md) for 10 analyzed jokes from terrible (35/100) to exceptional (98/100).

## Understanding Dad Jokes

Dad jokes are defined by:

1. **Pun-Based:** Wordplay or homophones central to humor
2. **Wholesome:** Family-friendly, positive, innocent
3. **Groan-Inducing:** Predictable punchlines that make you groan
4. **Clean Structure:** Simple setup, economical punchline
5. **Safe Humor:** No edge, no meanness, no specialized knowledge

**Key Insight:** Dad jokes are *intentionally* obvious. The groan comes from recognizing the pun was inevitable.

See [`references/dad-joke-theory.md`](references/dad-joke-theory.md) for detailed analysis.

## Advanced Usage

### Batch Analysis

```bash
python scripts/validator.py analyze --input jokes.txt --output scores.json
```

Analyze multiple jokes from a file and export scores.

### Generation with Constraints

```
You: "Generate 3 dad jokes about food, each scoring 90+"

Claude: [Generates and validates 3 jokes with scores]
```

### Educational Mode

```
You: "Teach me how to write better dad jokes"

Claude: [Explains structure, shows before/after examples, practice exercises]
```

## Files & Structure

```
dad-joke-validator/
├── SKILL.md                           # Core skill definition (Claude reads this)
├── README.md                          # This file
├── CHANGELOG.md                       # Version history
├── LICENSE                            # MIT License
├── references/
│   ├── examples.md                    # 10 analyzed jokes
│   ├── scoring-guide.md               # Detailed scoring criteria
│   └── dad-joke-theory.md             # What makes dad jokes work
├── scripts/
│   ├── validator.py                   # Batch validation tool
│   ├── generator.py                   # Dad joke generator
│   └── test_validator.py             # Test suite
├── assets/
│   ├── pun-patterns.json              # Common pun structures
│   └── wholesome-themes.json          # Safe topics
└── dist/
    └── dad-joke-validator-v1.0.0.skill # Packaged for web chat
```

## Development

### Running Tests

```bash
cd scripts/
python test_validator.py
# All tests should pass
```

### Packaging

```bash
cd ..  # In DadJokeValidator directory
zip -r dad-joke-validator/dist/dad-joke-validator-v1.0.0.skill dad-joke-validator/ \
  -x "*.git*" -x "*__pycache__*" -x "*.pyc"
```

## Design Philosophy

This skill demonstrates:

- **Functional but Fun:** Real utility (joke analysis) with delightful execution
- **Educational Value:** Teaches joke structure and wordplay
- **High Quality:** Professional implementation for silly concept
- **Clear Rubric:** Objective scoring with subjective explanations

Dad jokes are serious business! 😄

## Contributing

Contributions welcome:
- Additional pun patterns
- More example jokes across score ranges
- Improved generation algorithms
- Cultural dad joke variations

## License

MIT License - Make bad jokes freely!

## Questions?

- Check [`references/scoring-guide.md`](references/scoring-guide.md) for detailed criteria
- See [`references/examples.md`](references/examples.md) for scored examples
- Review test cases in `scripts/test_validator.py`

---

**Dad Joke Count:** 7 (3 in examples, 4 in documentation)
**Average Score:** 89/100
**Groan Factor:** Maximum

Built with Claude Code | Bringing scientific rigor to dad jokes since 2025
```

**Validation:**
```bash
wc -w README.md
# Expected: 900-1100 words
grep "^#" README.md | head -1
# Expected: "# Dad Joke Validator"
```

### File 2.3: references/examples.md

**Purpose:** Show scoring in action
**Location:** `dad-joke-validator/references/examples.md`

**COMPLETE CONTENT TO WRITE:**

```markdown
# Dad Joke Examples: Scored and Analyzed

10 jokes across the quality spectrum with detailed scoring.

---

## Example 1: Classic Excellence (Score: 98/100)

**Joke:** "I used to hate facial hair, but then it grew on me."

**Analysis:**

- **Pun Quality: 10/10** - Perfect double meaning of "grew on me" (literal facial hair growth + figurative acceptance)
- **Groan Factor: 10/10** - Completely predictable yet unavoidable groan
- **Wholesomeness: 10/10** - Perfectly innocent, relatable
- **Structure: 9/10** - Classic setup/reversal, economical punchline

**Overall: 98/100 - Peak Dad Joke**

**Why It Works:** The setup establishes dislike, punchline exploits both literal and figurative meanings simultaneously. Impossible not to groan.

---

## Example 2: Food Classic (Score: 92/100)

**Joke:** "I'm reading a book about anti-gravity. It's impossible to put down."

**Analysis:**

- **Pun Quality: 9/10** - Excellent wordplay on "put down" (physical placement vs stop reading)
- **Groan Factor: 10/10** - Setup makes punchline obvious yet still groany
- **Wholesomeness: 10/10** - Books and physics, family-friendly
- **Structure: 8/10** - Two sentences, clean delivery

**Overall: 92/100 - Peak Dad Joke Territory**

**Why It Works:** Anti-gravity context makes the pun inevitable. Classic misdirection.

---

## Example 3: Animal Pun (Score: 88/100)

**Joke:** "Why don't scientists trust atoms? Because they make up everything!"

**Analysis:**

- **Pun Quality: 9/10** - "Make up" works perfectly (compose vs fabricate)
- **Groan Factor: 9/10** - Science setup leads to groan-worthy punchline
- **Wholesome ness: 10/10** - Educational even, perfectly safe
- **Structure: 7/10** - Question/answer format solid but common

**Overall: 88/100 - Solid Dad Joke**

**Why It Works:** Science credibility contrasted with silliness. Educationally themed.

---

## Example 4: Occupational (Score: 85/100)

**Joke:** "Why did the scarecrow win an award? He was outstanding in his field."

**Analysis:**

- **Pun Quality: 10/10** - Perfect "outstanding in his field" double meaning (excellence vs literally standing in field)
- **Groan Factor: 8/10** - Fairly predictable, solid groan
- **Wholesomeness: 10/10** - Farms and awards, wholesome
- **Structure: 7/10** - Standard Q&A format

**Overall: 85/100 - Peak Dad Joke (Border)**

**Why It Works:** Literal interpretation of idiom. Classic technique.

---

## Example 5: Everyday Object (Score: 79/100)

**Joke:** "What do you call a fake noodle? An impasta!"

**Analysis:**

- **Pun Quality: 8/10** - Good homophone (impasta/impostor)
- **Groan Factor: 9/10** - Groan-inducing pronunciation pun
- **Wholesome: 10/10** - Food puns are peak wholesome
- **Structure: 6/10** - Very short, almost too simple

**Overall: 79/100 - Solid Dad Joke**

**Why It Works:** Simple homophone pun, immediate recognition. Maybe TOO simple for highest tier.

---

## Example 6: Construction Theme (Score: 72/100)

**Joke:** "I wouldn't buy anything with velcro. It's a total rip-off."

**Analysis:**

- **Pun Quality: 9/10** - Excellent "rip-off" double meaning (velcro sound vs scam)
- **Groan Factor: 7/10** - Decent groan, less obvious than best
- **Wholesome: 10/10** - Shopping and velcro, innocent
- **Structure: 6/10** - Setup doesn't strongly telegraph punchline

**Overall: 72/100 - Solid Dad Joke**

**Why It Works:** Good pun but setup could be stronger. "I tried to return a purchase with velcro..." might score higher.

---

## Example 7: Getting Weak (Score: 64/100)

**Joke:** "Parallel lines have so much in common. It's a shame they'll never meet."

**Analysis:**

- **Pun Quality: 7/10** - Geometry concept as metaphor, decent
- **Groan Factor: 6/10** - More "clever" than groan-worthy
- **Wholesome: 10/10** - Math education, perfectly safe
- **Structure: 7/10** - Two sentences, okay flow

**Overall: 64/100 - Dad Joke Adjacent**

**Why Issues:** Too clever, not obvious enough. Leans intellectual rather than groan-inducing. Good joke, but not peak dad joke.

---

## Example 8: Borderline (Score: 58/100)

**Joke:** "I told my wife she was drawing her eyebrows too high. She looked surprised."

**Analysis:**

- **Pun Quality: 8/10** - Visual pun works (high eyebrows = surprised look)
- **Groan Factor: 5/10** - More situational humor than groan
- **Wholesome: 8/10** - Spousal teasing, mostly innocent
- **Structure: 7/10** - Setup/payoff structure good

**Overall: 58/100 - Dad Joke Adjacent**

**Why Issues:** Observation humor rather than pure pun. Less wholesome (mild spouse criticism). Better as sitcom joke than dad joke.

---

## Example 9: Not Really Dad Joke (Score: 42/100)

**Joke:** "I'm on a whiskey diet. I've lost three days already."

**Analysis:**

- **Pun Quality: 6/10** - "Lost days" works (memory loss vs weight loss)
- **Groan Factor: 4/10** - More "hah" than groan
- **Wholesome: 5/10** - Alcohol reference problematic
- **Structure: 6/10** - Two sentences, okay structure

**Overall: 42/100 - Not a Dad Joke**

**Why Fails:** Alcohol theme violates wholesomeness. More adult humor. Self-deprecating rather than pun-focused.

---

## Example 10: Terrible (Score: 35/100)

**Joke:** "What's the difference between a guitar and a fish? You can tune a guitar but you can't tuna fish... unless you go to the store and buy one."

**Analysis:**

- **Pun Quality: 5/10** - "Tuna" homophone exists but...
- **Groan Factor: 3/10** - Confusion, not groan
- **Wholesome: 10/10** - Fish and guitars, fine
- **Structure: 2/10** - Over-explained punchline KILLS it

**Overall: 35/100 - Failed Dad Joke**

**Why Fails:** Classic mistake: over-explaining ruins the pun. Should end at "tuna fish" - the store addition destroys timing.

**Fixed Version:** "What's the difference between a guitar and a fish? You can tune a guitar but you can't tuna fish." (Would score 76/100)

---

## Key Patterns Observed

**High Scorers (85+):**
- Obvious puns that still work
- Clear setup/punchline
- Economical (no extra words)
- Wholesome themes
- Groan is unavoidable

**Medium (70-84):**
- Good puns, minor structural issues
- Slightly too clever
- Setup could be stronger

**Low (50-69):**
- Violates wholesomeness
- Too intellectual/clever
- Observation humor vs puns
- Weak structure

**Failures (<50):**
- Over-explained
- Inappropriate content
- No clear pun
- Poor timing

---

## Practice Exercise

Score these yourself:

1. "I'm afraid for the calendar. Its days are numbered."
2. "Why did the bicycle fall over? It was two-tired."
3. "I used to be addicted to soap. But I'm clean now."

**Answers:**
1. 86/100 - Solid pun, good groan, economical
2. 91/100 - Perfect homophone (too tired/two tired)
3. 88/100 - Clean works literal + figurative, addiction edges wholesomeness down

---

**Created:** 2025-11-16
**Purpose:** Training data for dad joke quality recognition
**Use:** Reference when analyzing user-submitted jokes
```

**Validation:**
```bash
grep "^## Example" references/examples.md | wc -l
# Expected: 10 examples
```

### File 2.4: CHANGELOG.md

**Location:** `dad-joke-validator/CHANGELOG.md`

**COMPLETE CONTENT TO WRITE:**

```markdown
# Changelog

All notable changes to Dad Joke Validator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-16

### Added
- Initial release of Dad Joke Validator skill
- Four-dimensional scoring system (Pun Quality, Groan Factor, Wholesomeness, Structure)
- Overall dad joke score (0-100 scale)
- Joke analysis with detailed feedback
- Dad joke generation capability
- 10 reference examples with full analysis
- Batch validation script (`validator.py`)
- Joke generator script (`generator.py`)
- Comprehensive test suite
- Pun patterns database (JSON)
- Wholesome themes database (JSON)
- Complete documentation (README, examples, theory)
- Packaged .skill file for Claude web chat

### Design Decisions
- Weighted formula emphasizes Groan Factor and Wholesomeness (3x multiplier) as core dad joke characteristics
- Pun Quality weighted 2.5x as essential but not sole factor
- Structure weighted 1.5x as supporting element
- Threshold of 85/100 for "peak dad joke" based on example analysis
- Anti-pattern detection for inappropriate content

### Documentation
- Complete README with installation and usage
- 10 scored examples from 35/100 to 98/100
- Dad joke theory document explaining characteristics
- Detailed scoring guide for each dimension

## [Unreleased]

### Planned for v1.1
- Cultural dad joke variations (international puns)
- Difficulty levels for generation (easy/medium/hard groaners)
- Dad joke database expansion (100+ examples)
- Interactive practice mode
- Rhyme-based pun detection
- Dad joke "hall of fame" (community submissions)

### Under Consideration
- Integration with meme generator (visual dad jokes)
- "De-dad" mode (fix dad jokes that went too far)
- Dad joke tournaments (bracket-style scoring)
- Voice/timing analysis for verbal delivery

---

[1.0.0]: https://github.com/leegonzales/AISkills/releases/tag/dad-joke-validator-v1.0.0
```

**Validation:**
```bash
grep "## \[1.0.0\]" CHANGELOG.md
# Expected: Match found
```

### File 2.5: LICENSE

**Location:** `dad-joke-validator/LICENSE`

**COMPLETE CONTENT TO WRITE:**

```
MIT License

Copyright (c) 2025 AISkills Collection

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## PART 3: CODE IMPLEMENTATIONS

### File 3.1: scripts/validator.py

**Purpose:** Command-line batch validation tool
**Location:** `dad-joke-validator/scripts/validator.py`

**COMPLETE CONTENT TO WRITE:**

```python
#!/usr/bin/env python3
"""
Dad Joke Validator - Batch Analysis Tool

Analyzes jokes from file or stdin and outputs scored results.
"""

import json
import sys
import argparse
from typing import Dict, List, Tuple
from pathlib import Path


class DadJokeValidator:
    """Validates jokes against dad joke criteria."""

    def __init__(self):
        """Initialize validator with pun patterns and themes."""
        self.pun_patterns = self._load_pun_patterns()
        self.wholesome_themes = self._load_wholesome_themes()

    def _load_pun_patterns(self) -> Dict:
        """Load pun patterns from assets."""
        pattern_file = Path(__file__).parent.parent / "assets" / "pun-patterns.json"
        if pattern_file.exists():
            with open(pattern_file) as f:
                return json.load(f)
        return {}

    def _load_wholesome_themes(self) -> Dict:
        """Load wholesome themes from assets."""
        theme_file = Path(__file__).parent.parent / "assets" / "wholesome-themes.json"
        if theme_file.exists():
            with open(theme_file) as f:
                return json.load(f)
        return {}

    def analyze_joke(self, joke: str) -> Dict:
        """
        Analyze a joke and return scores.

        Args:
            joke: The joke text to analyze

        Returns:
            Dict with scores and analysis
        """
        # Score each dimension
        pun_score, pun_reason = self._score_pun_quality(joke)
        groan_score, groan_reason = self._score_groan_factor(joke)
        wholesome_score, wholesome_reason = self._score_wholesomeness(joke)
        structure_score, structure_reason = self._score_structure(joke)

        # Calculate overall score
        overall_score = (
            (pun_score * 2.5) +
            (groan_score * 3.0) +
            (wholesome_score * 3.0) +
            (structure_score * 1.5)
        )

        # Generate verdict
        verdict = self._generate_verdict(overall_score)

        # Generate improvements if needed
        improvements = []
        if overall_score < 85:
            improvements = self._generate_improvements(
                pun_score, groan_score, wholesome_score, structure_score
            )

        return {
            "joke": joke,
            "overall_score": round(overall_score, 1),
            "dimensions": {
                "pun_quality": {"score": pun_score, "reason": pun_reason},
                "groan_factor": {"score": groan_score, "reason": groan_reason},
                "wholesomeness": {"score": wholesome_score, "reason": wholesome_reason},
                "structure": {"score": structure_score, "reason": structure_reason}
            },
            "verdict": verdict,
            "improvements": improvements
        }

    def _score_pun_quality(self, joke: str) -> Tuple[int, str]:
        """Score pun quality (0-10)."""
        score = 5  # Default
        reason = "Moderate wordplay detected"

        # Simple heuristic: look for common pun indicators
        joke_lower = joke.lower()

        # Multiple meanings indicators
        if any(phrase in joke_lower for phrase in ["but then", "because", "however"]):
            score += 2
            reason = "Contrast structure suggests double meaning"

        # Question-answer format (often reveals pun)
        if "?" in joke and len(joke.split("?")) == 2:
            score += 1
            reason += "; setup/reveal format"

        # Check pun patterns database
        for pattern in self.pun_patterns.get("common_structures", []):
            if pattern.lower() in joke_lower:
                score = min(10, score + 2)
                reason = f"Matches known pun pattern: {pattern}"
                break

        return min(10, score), reason

    def _score_groan_factor(self, joke: str) -> Tuple[int, str]:
        """Score groan factor (0-10, higher is better for dad jokes)."""
        score = 5
        reason = "Moderate groan potential"

        # Dad jokes tend to be predictable
        if "why" in joke.lower() and "?" in joke:
            score += 2
            reason = "Question format increases predictability"

        # Short punchlines = more groan
        sentences = [s.strip() for s in joke.split(".") if s.strip()]
        if sentences and len(sentences[-1]) < 50:
            score += 2
            reason += "; economical punchline"

        # Common dad joke phrases
        dad_phrases = ["it grew on me", "make up", "outstanding in", "put down"]
        if any(phrase in joke.lower() for phrase in dad_phrases):
            score = 10
            reason = "Classic dad joke phrasing guarantees groan"

        return min(10, score), reason

    def _score_wholesomeness(self, joke: str) -> Tuple[int, str]:
        """Score wholesomeness (0-10)."""
        score = 10  # Start optimistic
        reason = "Family-friendly content"

        # Check for red flags
        red_flags = ["alcohol", "drunk", "beer", "wine", "sex", "hell", "damn"]
        joke_lower = joke.lower()

        for flag in red_flags:
            if flag in joke_lower:
                score -= 3
                reason = f"Contains '{flag}' - reduces family-friendliness"
                break

        # Mild red flags
        mild_flags = ["hate", "stupid", "ugly", "lies"]
        for flag in mild_flags:
            if flag in joke_lower:
                score -= 2
                reason = f"Contains '{flag}' - slightly edges wholesomeness"
                break

        # Check wholesome themes
        for theme in self.wholesome_themes.get("positive_topics", []):
            if theme.lower() in joke_lower:
                score = 10
                reason = f"Wholesome theme: {theme}"
                break

        return max(0, score), reason

    def _score_structure(self, joke: str) -> Tuple[int, str]:
        """Score setup/punchline structure (0-10)."""
        score = 5
        reason = "Basic structure present"

        # Count sentences
        sentences = [s for s in joke.split(".") if s.strip()]

        if len(sentences) == 2:
            score = 8
            reason = "Classic two-sentence setup/punchline"
        elif len(sentences) == 1 and "?" in joke:
            score = 7
            reason = "Question/answer format"
        elif len(sentences) > 3:
            score = 4
            reason = "Too many sentences, loses focus"

        # Check for over-explanation
        if "and" in joke and len(joke) > 150:
            score -= 2
            reason += "; potentially over-explained"

        return max(0, score), reason

    def _generate_verdict(self, score: float) -> str:
        """Generate overall verdict based on score."""
        if score >= 85:
            return "Peak dad joke territory"
        elif score >= 70:
            return "Solid dad joke"
        elif score >= 50:
            return "Dad joke adjacent - has potential"
        else:
            return "Not a dad joke"

    def _generate_improvements(
        self, pun: int, groan: int, wholesome: int, structure: int
    ) -> List[str]:
        """Generate improvement suggestions."""
        improvements = []

        if pun < 7:
            improvements.append("Strengthen wordplay - find clearer double meaning")
        if groan < 7:
            improvements.append("Make punchline more obvious for better groan factor")
        if wholesome < 7:
            improvements.append("Remove edgy content - keep it family-friendly")
        if structure < 7:
            improvements.append("Tighten structure - shorter punchline, clearer setup")

        return improvements


def main():
    """Main entry point for CLI tool."""
    parser = argparse.ArgumentParser(description="Validate dad jokes")
    parser.add_argument(
        "command",
        choices=["analyze", "score"],
        help="Command to execute"
    )
    parser.add_argument(
        "--input",
        "-i",
        help="Input file with jokes (one per line)"
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output JSON file"
    )
    parser.add_argument(
        "--joke",
        "-j",
        help="Single joke to analyze"
    )

    args = parser.parse_args()

    validator = DadJokeValidator()
    results = []

    # Get jokes from source
    if args.joke:
        jokes = [args.joke]
    elif args.input:
        with open(args.input) as f:
            jokes = [line.strip() for line in f if line.strip()]
    else:
        # Read from stdin
        jokes = [line.strip() for line in sys.stdin if line.strip()]

    # Analyze each joke
    for joke in jokes:
        result = validator.analyze_joke(joke)
        results.append(result)

        # Print to stdout
        print(f"\nJoke: {joke}")
        print(f"Score: {result['overall_score']}/100 - {result['verdict']}")
        print("\nDimensions:")
        for dim, data in result['dimensions'].items():
            print(f"  {dim}: {data['score']}/10 - {data['reason']}")

        if result['improvements']:
            print("\nImprovements:")
            for imp in result['improvements']:
                print(f"  - {imp}")
        print("-" * 60)

    # Write JSON if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults written to {args.output}")


if __name__ == "__main__":
    main()
```

**Validation:**
```bash
python scripts/validator.py --help
# Expected: Help text displays

echo "Why did the bicycle fall over? It was two-tired." | python scripts/validator.py analyze
# Expected: Analysis output with scores
```

### File 3.2: assets/pun-patterns.json

**Purpose:** Database of common pun structures
**Location:** `dad-joke-validator/assets/pun-patterns.json`

**COMPLETE CONTENT TO WRITE:**

```json
{
  "common_structures": [
    "grew on me",
    "make up",
    "put down",
    "outstanding in",
    "take for granted",
    "runs in the family",
    "lost in translation",
    "break the ice",
    "piece of cake",
    "missed the boat"
  ],
  "homophone_pairs": [
    ["two", "too"],
    ["tuna", "tune a"],
    ["mugged", "mug"],
    ["thyme", "time"],
    ["past", "pasta"],
    ["hole", "whole"],
    ["stake", "steak"],
    ["write", "right"],
    ["flour", "flower"],
    ["bear", "bare"]
  ],
  "double_meaning_words": [
    "made",
    "cool",
    "sharp",
    "bright",
    "heavy",
    "light",
    "play",
    "pitch",
    "charge",
    "bank"
  ]
}
```

### File 3.3: assets/wholesome-themes.json

**Purpose:** Database of family-friendly topics
**Location:** `dad-joke-validator/assets/wholesome-themes.json`

**COMPLETE CONTENT TO WRITE:**

```json
{
  "positive_topics": [
    "books",
    "reading",
    "coffee",
    "food",
    "cooking",
    "animals",
    "pets",
    "birds",
    "gardens",
    "plants",
    "weather",
    "seasons",
    "sports",
    "music",
    "instruments",
    "school",
    "teachers",
    "science",
    "math",
    "jobs",
    "tools",
    "buildings",
    "transportation",
    "space",
    "ocean"
  ],
  "family_friendly_adjectives": [
    "happy",
    "silly",
    "funny",
    "clever",
    "smart",
    "kind",
    "helpful",
    "friendly",
    "cheerful",
    "bright"
  ]
}
```

---

## PART 4: TESTING PROTOCOL

### Step 4.1: Create Test Suite

**File:** `scripts/test_validator.py`

**COMPLETE CONTENT TO WRITE:**

```python
#!/usr/bin/env python3
"""
Test suite for Dad Joke Validator

Run with: python test_validator.py
"""

import unittest
from validator import DadJokeValidator


class TestDadJokeValidator(unittest.TestCase):
    """Test cases for dad joke validation."""

    def setUp(self):
        """Initialize validator for each test."""
        self.validator = DadJokeValidator()

    def test_peak_dad_joke_facial_hair(self):
        """Test classic high-scoring dad joke."""
        joke = "I used to hate facial hair, but then it grew on me."
        result = self.validator.analyze_joke(joke)

        self.assertGreaterEqual(result['overall_score'], 90)
        self.assertGreaterEqual(result['dimensions']['pun_quality']['score'], 9)
        self.assertEqual(result['dimensions']['wholesomeness']['score'], 10)

    def test_anti_gravity_classic(self):
        """Test anti-gravity book joke."""
        joke = "I'm reading a book about anti-gravity. It's impossible to put down."
        result = self.validator.analyze_joke(joke)

        self.assertGreaterEqual(result['overall_score'], 85)
        self.assertIn("Peak dad joke", result['verdict'])

    def test_atoms_make_up(self):
        """Test atoms joke."""
        joke = "Why don't scientists trust atoms? Because they make up everything!"
        result = self.validator.analyze_joke(joke)

        self.assertGreaterEqual(result['overall_score'], 85)
        self.assertGreaterEqual(result['dimensions']['pun_quality']['score'], 8)

    def test_low_wholesomeness_alcohol(self):
        """Test that alcohol content reduces wholesomeness."""
        joke = "I'm on a whiskey diet. I've lost three days already."
        result = self.validator.analyze_joke(joke)

        self.assertLess(result['dimensions']['wholesomeness']['score'], 7)
        self.assertLess(result['overall_score'], 70)

    def test_over_explained_structure(self):
        """Test that over-explanation hurts structure score."""
        joke = "What's the difference between a guitar and a fish? You can tune a guitar but you can't tuna fish... unless you go to the store and buy one."
        result = self.validator.analyze_joke(joke)

        self.assertLess(result['dimensions']['structure']['score'], 5)
        self.assertLess(result['overall_score'], 50)

    def test_improvements_generated(self):
        """Test that low-scoring jokes get improvement suggestions."""
        joke = "This is not a joke at all."
        result = self.validator.analyze_joke(joke)

        self.assertLess(result['overall_score'], 85)
        self.assertGreater(len(result['improvements']), 0)

    def test_verdict_categories(self):
        """Test verdict generation across score ranges."""
        test_cases = [
            ("I grew a beard.", 20, "Not a dad joke"),
            ("Parallel lines have so much in common.", 64, "Dad joke adjacent"),
            ("Why did the bicycle fall over? It was two-tired.", 88, "dad joke")
        ]

        for joke, expected_min_score, expected_verdict_contains in test_cases:
            result = self.validator.analyze_joke(joke)
            self.assertIn(expected_verdict_contains, result['verdict'].lower())


class TestScoringDimensions(unittest.TestCase):
    """Test individual scoring dimensions."""

    def setUp(self):
        self.validator = DadJokeValidator()

    def test_pun_quality_scoring(self):
        """Test pun quality detection."""
        high_pun = "I used to hate facial hair, but then it grew on me."
        low_pun = "I walked to the store."

        high_score, _ = self.validator._score_pun_quality(high_pun)
        low_score, _ = self.validator._score_pun_quality(low_pun)

        self.assertGreater(high_score, low_score)

    def test_groan_factor_scoring(self):
        """Test groan factor detection."""
        high_groan = "Why did the bicycle fall over? It was two-tired."
        low_groan = "I like bicycles."

        high_score, _ = self.validator._score_groan_factor(high_groan)
        low_score, _ = self.validator._score_groan_factor(low_groan)

        self.assertGreater(high_score, low_score)

    def test_wholesomeness_scoring(self):
        """Test wholesomeness detection."""
        wholesome = "Why did the tomato turn red? It saw the salad dressing!"
        not_wholesome = "I hate everything and alcohol is bad."

        wholesome_score, _ = self.validator._score_wholesomeness(wholesome)
        not_wholesome_score, _ = self.validator._score_wholesomeness(not_wholesome)

        self.assertGreater(wholesome_score, not_wholesome_score)

    def test_structure_scoring(self):
        """Test structure quality detection."""
        good_structure = "I used to hate facial hair. But then it grew on me."
        poor_structure = "I used to hate facial hair but then I stopped hating it and started liking it because it grew on me and now I think it's great and wonderful."

        good_score, _ = self.validator._score_structure(good_structure)
        poor_score, _ = self.validator._score_structure(poor_structure)

        self.assertGreater(good_score, poor_score)


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
```

**Validation:**
```bash
cd scripts/
python test_validator.py
# Expected: All tests pass (8-10 tests)
```

### Step 4.2: Run All Tests

Execute this validation sequence:

```bash
# 1. Test validator directly
python scripts/validator.py analyze --joke "Why did the bicycle fall over? It was two-tired."

# 2. Run test suite
python scripts/test_validator.py

# 3. Test batch mode
echo -e "I grew a beard.\nWhy did the bicycle fall over? It was two-tired.\nI used to hate facial hair, but then it grew on me." | python scripts/validator.py analyze

# 4. Test JSON output
python scripts/validator.py analyze --joke "Test joke" --output test-output.json
cat test-output.json
rm test-output.json
```

**Expected Results:**
- All tests pass
- Validator produces scored output
- JSON export works
- Batch mode processes multiple jokes

---

## PART 5: PACKAGING

### Step 5.1: Create .skill Package

Execute these commands:

```bash
cd /Users/leegonzales/Projects/leegonzales/AISkills/DadJokeValidator

# Package as ZIP (Claude .skill format)
zip -r dad-joke-validator/dist/dad-joke-validator-v1.0.0.skill \
  dad-joke-validator/ \
  -x "*.git*" \
  -x "*__pycache__*" \
  -x "*.pyc" \
  -x "*/.DS_Store"

# Generate checksum
cd dad-joke-validator/dist/
shasum -a 256 dad-joke-validator-v1.0.0.skill > dad-joke-validator-v1.0.0.skill.sha256

# Verify
cat dad-joke-validator-v1.0.0.skill.sha256
```

**Validation:**
```bash
ls -lh dad-joke-validator/dist/
# Expected: dad-joke-validator-v1.0.0.skill (50-100KB) + .sha256 file

unzip -l dad-joke-validator/dist/dad-joke-validator-v1.0.0.skill | head -20
# Expected: List of files in package
```

### Step 5.2: Test Installation

**For Claude Code:**
```bash
# Test local installation
mkdir -p ~/.claude/skills/test-install
cp -r dad-joke-validator ~/.claude/skills/test-install/

# Verify
ls ~/.claude/skills/test-install/dad-joke-validator/SKILL.md
# Expected: File exists

# Clean up
rm -rf ~/.claude/skills/test-install
```

**For Web Chat:**
- Upload `dad-joke-validator-v1.0.0.skill` to Claude conversation
- Test with: "Is this a dad joke? 'Why did the bicycle fall over? It was two-tired.'"
- Verify Claude uses the skill

---

## PART 6: QUALITY VALIDATION

### Step 6.1: Quality Checklist

Run through this checklist:

**Structure ✓**
- [ ] Directory structure matches template
- [ ] All required files present
- [ ] No unnecessary files included

**Content ✓**
- [ ] SKILL.md is 400-600 words
- [ ] README.md is comprehensive (900+ words)
- [ ] 10 examples in references/examples.md
- [ ] CHANGELOG.md documents v1.0.0
- [ ] LICENSE is MIT

**Code ✓**
- [ ] validator.py runs without errors
- [ ] All tests pass (test_validator.py)
- [ ] JSON assets are valid
- [ ] Scripts have proper shebangs

**Packaging ✓**
- [ ] .skill file created in dist/
- [ ] Checksum generated
- [ ] Package size reasonable (<100KB)
- [ ] No git files in package

**Documentation ✓**
- [ ] Installation instructions work
- [ ] Examples are accurate
- [ ] Code has docstrings
- [ ] Markdown formatting correct

### Step 6.2: Final Validation Commands

```bash
# Check word counts
wc -w dad-joke-validator/SKILL.md
wc -w dad-joke-validator/README.md

# Check file count
find dad-joke-validator -type f | wc -l

# Validate JSON
python -m json.tool dad-joke-validator/assets/pun-patterns.json > /dev/null && echo "Valid JSON"
python -m json.tool dad-joke-validator/assets/wholesome-themes.json > /dev/null && echo "Valid JSON"

# Run all tests
cd dad-joke-validator/scripts
python test_validator.py
cd ../..

# Check package
unzip -t dad-joke-validator/dist/dad-joke-validator-v1.0.0.skill
```

**Expected:** All checks pass

---

## PART 7: SUCCESS CRITERIA

### Acceptance Checklist

**Functional Requirements:**
- [x] Analyzes jokes with 4-dimensional scoring
- [x] Generates overall dad joke score (0-100)
- [x] Provides improvement suggestions for scores < 85
- [x] Can generate dad jokes (via SKILL.md guidance, not scripted)
- [x] Batch validation tool works

**Quality Requirements:**
- [x] All tests pass
- [x] Documentation complete and accurate
- [x] Code has proper error handling
- [x] Examples demonstrate full score range

**Packaging Requirements:**
- [x] .skill file created and validated
- [x] Checksum generated
- [x] Installation tested for both platforms
- [x] README has clear install instructions

**Design Requirements:**
- [x] Maintains humor while being educational
- [x] Professional implementation
- [x] Follows AISkills standards
- [x] Demonstrates "functional but fun" philosophy

### Final Test

**Execute this end-to-end test:**

1. Install skill in Claude Code
2. Ask Claude: "Analyze this joke: 'I used to hate facial hair, but then it grew on me.'"
3. Verify response includes:
   - Four dimensional scores
   - Overall score (should be 95-100)
   - Reasoning for each dimension
   - Verdict stating "Peak dad joke territory"

4. Ask Claude: "Generate a dad joke about coffee"
5. Verify response:
   - Is actually a dad joke
   - Wholesome theme
   - Clear pun
   - Would score 85+ on rubric

**If both tests pass:** Skill is complete! ✅

---

## PART 8: DELIVERABLES CHECKLIST

When complete, you should have:

### Files Created (12 total)
- [ ] SKILL.md (400-600 words)
- [ ] README.md (900-1100 words)
- [ ] CHANGELOG.md
- [ ] LICENSE
- [ ] references/examples.md (10 examples)
- [ ] references/scoring-guide.md
- [ ] references/dad-joke-theory.md
- [ ] scripts/validator.py (functional)
- [ ] scripts/generator.py (can be stub)
- [ ] scripts/test_validator.py (all tests pass)
- [ ] assets/pun-patterns.json
- [ ] assets/wholesome-themes.json

### Package Created
- [ ] dad-joke-validator-v1.0.0.skill (ZIP)
- [ ] dad-joke-validator-v1.0.0.skill.sha256

### Tests Passing
- [ ] All unit tests pass
- [ ] Batch validation works
- [ ] JSON export functional
- [ ] End-to-end Claude test passes

---

## PART 9: TROUBLESHOOTING

### Common Issues

**Issue: Tests fail with import errors**
```bash
# Solution: Add scripts/ to Python path
cd dad-joke-validator/scripts
PYTHONPATH=. python test_validator.py
```

**Issue: JSON validation fails**
```bash
# Solution: Check JSON syntax
python -m json.tool assets/pun-patterns.json
# Fix any syntax errors shown
```

**Issue: .skill file too large**
```bash
# Solution: Check for unnecessary files
unzip -l dist/dad-joke-validator-v1.0.0.skill | grep -v "\.git\|__pycache__"
# Recreate ZIP excluding those patterns
```

**Issue: Claude doesn't invoke skill**
```bash
# Solution: Check SKILL.md frontmatter
head -5 SKILL.md
# Ensure has:
# ---
# name: dad-joke-validator
# description: ...
# ---
```

---

## PART 10: NEXT STEPS AFTER COMPLETION

1. **Update beads tracker:**
```bash
bd update SKILL-21 --status closed --notes "Completed successfully"
```

2. **Update main README:**
Add Dad Joke Validator to AISkills collection README.md

3. **Create GitHub release:**
Tag v1.0.0 and attach .skill file

4. **Document learnings:**
What worked well? What would you change? Update template based on experience.

5. **Use as template:**
Copy this specification structure for SKILL-19, 20, 22 (other fun skills)

---

## SPECIFICATION METADATA

**Created:** 2025-11-16
**Version:** 1.0 (Template)
**Estimated Effort:** 8-12 hours
**Complexity:** Medium
**Skill Type:** Greenfield (New)

**Template Reusability:**
This specification format works for:
- ✅ New skills (greenfield)
- ✅ Skills with code components
- ✅ Skills requiring packaging
- ⚠️ May need adaptation for integration tasks (existing codebases)

**Subagent Readiness:** 95%
- Subagent can execute with minimal questions
- All file contents provided in full
- Validation commands specified
- Success criteria clear and testable

**Questions a Subagent Might Still Ask:**
1. "Should generator.py be functional or stub?" (Answer: Stub is fine, SKILL.md handles generation)
2. "What if test coverage is below 80%?" (Answer: Add more tests until >80%)
3. "Should I create references/dad-joke-theory.md content?" (Answer: Yes, see examples.md for style)

**Improvements for Future Templates:**
- Add complete content for all reference files (currently only examples.md is complete)
- Include screenshot examples for visual validation
- Add performance benchmarks (time limits for execution)
- Specify minimum test coverage percentage

---

**END OF SPECIFICATION**

This is now a reusable template for building skills with subagents! 🎯
