# Examples: Full Transformations

Complete examples showing the transformation from essay-to-speech output to Talk Track v5 format.

---

## Example: Theory of Mind Research

A complete walkthrough transforming essay-to-speech output into a Talk Track v5 presentation with image prompts.

---

### INPUT: Essay-to-Speech Output

```markdown
# Theory of Mind Predicts AI Success: Presentation Version

**Source**: Research paper on ToM and AI collaboration
**Chunks**: 5 sections
**Generated**: 2026-01-19
**Mode**: Full transformation

---

## Section 1: Opening Hook

### Original
The study found ToM strongly predicted collaborative ability with AI (coefficient: 0.65, 95% CI: 0.01-1.29). Translation: higher Theory of Mind scores meant better AI collaboration, and we can be 95% confident this relationship is real—the confidence interval stays positive.

### Talk Track
[HOOK] What if I told you the number one predictor of AI collaboration success isn't technical skill at all?

[PAUSE]

It's a social skill.

[KEY_POINT] Theory of Mind—the ability to understand what others are thinking and feeling—turns out to be the secret weapon for working with AI.

[EVIDENCE] A recent study found a strong, statistically significant link. Higher Theory of Mind means better AI results. And this isn't a maybe—the statistics are clear.

### Images
- `correlation-scatter.png`: ADAPT - Axis labels need plain English ("ToM Score" → "Social Skill", "κ" → "AI Success")
- `coefficient-table.png`: RECREATE - Convert statistical table to simple callout visual

### Slide Ideas
- Single insight slide: "Social Skill → AI Success"
- Key stat callout with big number
- Hook slide: provocative question

---

## Section 2: The Research

### Original
The research team tested 667 participants across diverse industries and job functions. Participants completed Theory of Mind assessments and then collaborated with AI systems on complex tasks. The correlation between ToM scores and successful AI collaboration was measured using validated instruments.

### Talk Track
[TRANSITION] Let me tell you about the study.

[EVIDENCE] Nearly 700 people were tested—across industries, across roles, across experience levels. This wasn't a narrow sample.

[EVIDENCE] Each person took a Theory of Mind assessment. Then they worked with AI on real tasks. The researchers measured what happened.

[KEY_POINT] The pattern was unmistakable.

### Images
- `methodology-diagram.png`: USE - Clear process flow, readable at projection size

### Slide Ideas
- Process diagram showing study methodology
- "N = 667" big number slide
- Three-column: "Assess → Collaborate → Measure"

---

## Section 3: Why It Works

### Original
Theory of Mind may facilitate AI collaboration because it enables users to form more accurate mental models of AI capabilities and limitations. Users with higher ToM scores were better at predicting when AI would succeed or fail, and adjusted their collaboration strategies accordingly. They treated AI as a partner with distinct strengths rather than either a magic oracle or a broken tool.

### Talk Track
[TRANSITION] But why? Why would understanding other minds help you work with machines?

[KEY_POINT] Because you build better mental models. People with high Theory of Mind don't anthropomorphize AI—but they don't dismiss it either.

[EVIDENCE] They predict where AI will succeed. They anticipate where it will fail. And they adjust.

[KEY_POINT] They treat AI as a collaborator with distinct strengths. Not a magic oracle. Not a broken tool. A partner.

[PAUSE]

### Images
- `mental-model-diagram.png`: ADAPT - Simplify to three states: Oracle → Partner → Tool

### Slide Ideas
- Spectrum visual: Oracle ← Partner → Tool
- Quote slide: "A partner with distinct strengths"
- Before/after collaboration patterns

---

## Section 4: The Implications

### Original
These findings suggest that organizations seeking to improve AI adoption should consider Theory of Mind development alongside technical training. Traditional AI training focuses on prompting techniques and tool features, but this research indicates that interpersonal skills may be equally or more important for successful AI collaboration outcomes.

### Talk Track
[TRANSITION] So what does this mean for you—and for your organization?

[KEY_POINT] If you want better AI results, don't just train on prompts. Train on people skills.

[EVIDENCE] The organizations getting the most from AI aren't the ones with the fanciest tools. They're the ones whose people understand how to collaborate—period.

[CALLBACK] Remember: the correlation was stronger for Theory of Mind than for technical expertise.

### Images
- None in original

### Slide Ideas
- Two-column contrast: "Technical Training" vs. "ToM Development"
- Callout: "People skills > Prompt skills"
- Organization comparison visual

---

## Section 5: The Takeaway

### Original
In conclusion, this research demonstrates that human social-cognitive abilities remain central even as AI becomes more capable. Theory of Mind—a distinctly human capacity—may be the key differentiator in human-AI collaboration success.

### Talk Track
[LANDING] Here's the bottom line.

[KEY_POINT] As AI gets smarter, the human skills that matter aren't getting less important. They're getting more important.

[PAUSE]

[CTA] So ask yourself: are you developing the social intelligence to be a great AI collaborator? Or just learning to type better prompts?

[LANDING] The research is clear. Theory of Mind predicts success. The most human skill is also the most valuable one.

### Images
- None in original

### Slide Ideas
- Closing statement: "The most human skill is the most valuable"
- CTA slide with question
- Final insight with big typography
```

---

### OUTPUT: Talk Track v5

```yaml
---
version: 5
title: "Theory of Mind Predicts AI Success"
author: "Lee Gonzales"
target_minutes: 10
audio_voice: "af_heart"
generated: "2026-01-19"

sections:
  - id: opening
    name: "Opening"
    color: "#557373"
  - id: research
    name: "The Research"
    color: "#6B8E6B"
  - id: why
    name: "Why It Works"
    color: "#8B6B6B"
  - id: implications
    name: "Implications"
    color: "#6B6B8E"
  - id: takeaway
    name: "Takeaway"
    color: "#8E8B6B"
---

## Slides

| # | Slug | Title | Image | Section |
|---|------|-------|-------|---------|
| 1 | hook | The Secret Skill | hook-question.png | opening |
| 2 | insight | Theory of Mind Link | tom-insight.png | opening |
| 3 | evidence | The Statistics | evidence-strong-link.png | opening |
| 4 | methodology | Study Design | methodology-diagram.png | research |
| 5 | sample | Nearly 700 People | sample-size.png | research |
| 6 | pattern | The Pattern | pattern-unmistakable.png | research |
| 7 | why-question | Why Does It Work? | why-question.png | why |
| 8 | mental-models | Better Mental Models | mental-models-spectrum.png | why |
| 9 | partner | AI as Partner | partner-visual.png | why |
| 10 | org-implications | What This Means | implications-contrast.png | implications |
| 11 | people-skills | People Skills Matter | people-over-prompts.png | implications |
| 12 | landing | The Bottom Line | landing-statement.png | takeaway |
| 13 | cta | The Question | cta-question.png | takeaway |
| 14 | closing | The Most Human Skill | closing-insight.png | takeaway |

---

## [hook] The Secret Skill

![What predicts AI collaboration success?](images/hook-question.png)

<!-- AUDIO -->
[HOOK] What if I told you the number one predictor of AI collaboration success isn't technical skill at all?

[PAUSE]

It's a social skill.
<!-- /AUDIO -->

**Speaker Notes:**
Let the question land. Pause after "at all" for effect. The reveal—"social skill"—should feel like a plot twist.

---

## [insight] Theory of Mind Link

![Theory of Mind: Your Secret Weapon](images/tom-insight.png)

<!-- AUDIO -->
[KEY_POINT] Theory of Mind—the ability to understand what others are thinking and feeling—turns out to be the secret weapon for working with AI.
<!-- /AUDIO -->

**Speaker Notes:**
Define Theory of Mind briefly but clearly. Emphasize "secret weapon"—this is the core insight of the entire talk.

---

## [evidence] The Statistics

![Strong, Statistically Significant Link](images/evidence-strong-link.png)

<!-- AUDIO -->
[EVIDENCE] A recent study found a strong, statistically significant link. Higher Theory of Mind means better AI results. And this isn't a maybe—the statistics are clear.
<!-- /AUDIO -->

**Speaker Notes:**
Confidence here. Don't hedge. The data supports this claim strongly—convey that certainty.

---

## [methodology] Study Design

![Study Process: Assess, Collaborate, Measure](images/methodology-diagram.png)

<!-- AUDIO -->
[TRANSITION] Let me tell you about the study.
<!-- /AUDIO -->

**Speaker Notes:**
Quick transition. The visual does most of the work here—just orient the audience.

---

## [sample] Nearly 700 People

![N = 667](images/sample-size.png)

<!-- AUDIO -->
[EVIDENCE] Nearly 700 people were tested—across industries, across roles, across experience levels. This wasn't a narrow sample.
<!-- /AUDIO -->

**Speaker Notes:**
Emphasize diversity and scale. This addresses the "but was it a representative sample?" skeptic.

---

## [pattern] The Pattern

![Unmistakable Pattern](images/pattern-unmistakable.png)

<!-- AUDIO -->
[EVIDENCE] Each person took a Theory of Mind assessment. Then they worked with AI on real tasks. The researchers measured what happened.

[KEY_POINT] The pattern was unmistakable.
<!-- /AUDIO -->

**Speaker Notes:**
Build to the punch line. "Unmistakable" should land with weight.

---

## [why-question] Why Does It Work?

![Why would understanding minds help with machines?](images/why-question.png)

<!-- AUDIO -->
[TRANSITION] But why? Why would understanding other minds help you work with machines?
<!-- /AUDIO -->

**Speaker Notes:**
Rhetorical question—voice it as genuine curiosity. This is the pivot to explanation.

---

## [mental-models] Better Mental Models

![Oracle ← Partner → Tool](images/mental-models-spectrum.png)

<!-- AUDIO -->
[KEY_POINT] Because you build better mental models. People with high Theory of Mind don't anthropomorphize AI—but they don't dismiss it either.

[EVIDENCE] They predict where AI will succeed. They anticipate where it will fail. And they adjust.
<!-- /AUDIO -->

**Speaker Notes:**
The spectrum visual grounds this. Point to it as you explain the middle ground.

---

## [partner] AI as Partner

![Not an Oracle. Not a Tool. A Partner.](images/partner-visual.png)

<!-- AUDIO -->
[KEY_POINT] They treat AI as a collaborator with distinct strengths. Not a magic oracle. Not a broken tool. A partner.

[PAUSE]
<!-- /AUDIO -->

**Speaker Notes:**
Let "partner" resonate. The pause gives the audience time to internalize the reframe.

---

## [org-implications] What This Means

![Technical Training vs. ToM Development](images/implications-contrast.png)

<!-- AUDIO -->
[TRANSITION] So what does this mean for you—and for your organization?

[KEY_POINT] If you want better AI results, don't just train on prompts. Train on people skills.
<!-- /AUDIO -->

**Speaker Notes:**
Actionable insight. This is where leaders in the audience start taking notes.

---

## [people-skills] People Skills Matter

![People Skills > Prompt Skills](images/people-over-prompts.png)

<!-- AUDIO -->
[EVIDENCE] The organizations getting the most from AI aren't the ones with the fanciest tools. They're the ones whose people understand how to collaborate—period.

[CALLBACK] Remember: the correlation was stronger for Theory of Mind than for technical expertise.
<!-- /AUDIO -->

**Speaker Notes:**
The callback reinforces the data. "Period" should be definitive.

---

## [landing] The Bottom Line

![As AI gets smarter, human skills matter more](images/landing-statement.png)

<!-- AUDIO -->
[LANDING] Here's the bottom line.

[KEY_POINT] As AI gets smarter, the human skills that matter aren't getting less important. They're getting more important.

[PAUSE]
<!-- /AUDIO -->

**Speaker Notes:**
This is the thesis restated as conclusion. Let it breathe.

---

## [cta] The Question

![Are you developing social intelligence?](images/cta-question.png)

<!-- AUDIO -->
[CTA] So ask yourself: are you developing the social intelligence to be a great AI collaborator? Or just learning to type better prompts?
<!-- /AUDIO -->

**Speaker Notes:**
Challenge the audience directly. Make eye contact. This isn't rhetorical—you want them to actually reflect.

---

## [closing] The Most Human Skill

![The Most Human Skill is the Most Valuable One](images/closing-insight.png)

<!-- AUDIO -->
[LANDING] The research is clear. Theory of Mind predicts success. The most human skill is also the most valuable one.
<!-- /AUDIO -->

**Speaker Notes:**
Final statement. Let the paradox land: human skills for machine collaboration. End with confidence.

---
```

---

### IMAGE PROMPTS OUTPUT

Generated prompts for images that need to be created (RECREATE ratings and new slides).

#### `prompts/recreate-images.md`

```markdown
# Image Recreation Prompts

Generated from essay-to-speech image ratings and slide requirements.

---

## RECREATE: coefficient-table.png → tom-insight.png

**Original**: Statistical table showing coefficient 0.65 with 95% CI: 0.01-1.29
**Problem**: Tables don't work on slides; statistical notation confuses audiences
**Target**: Simple insight callout

**Nano Banana Prompt:**
```
A clean presentation slide with centered text "Theory of Mind" with an arrow
pointing to "Your Secret Weapon" below it. Modern minimalist design.
Dark charcoal background (#1a1a1a). Teal accent color (#557373) for the arrow
and subtle glow effect. Sans-serif typography, bold weight.
Professional corporate aesthetic. No decorative elements or icons.

Aspect ratio: 16:9
Avoid: logos, watermarks, complex graphics, photographs
```

---

## ADAPT: correlation-scatter.png → evidence-strong-link.png

**Original**: Scatter plot with axis labels "ToM Score" and "κ (Collaborative Ability)"
**Problem**: Technical axis labels; Greek letters don't work in presentations
**Action**: Recreate with plain English labels

**Nano Banana Prompt:**
```
A simple scatter plot visualization showing a positive correlation trend.
X-axis labeled "Social Skill (Theory of Mind)" in clear sans-serif text.
Y-axis labeled "AI Collaboration Success" in matching typography.
Dots following a clear upward trend from bottom-left to top-right.
Subtle trend line in teal (#557373). Dark background (#0d0d0d).
Clean, minimal style. No gridlines. Large, readable labels.
Data visualization aesthetic, not academic chart style.

Aspect ratio: 16:9
Avoid: complex legends, small text, decorative elements
```

---

## ADAPT: mental-model-diagram.png → mental-models-spectrum.png

**Original**: Complex diagram showing mental model formation process
**Problem**: Too detailed for projection; needs simplification
**Target**: Simple three-state spectrum

**Nano Banana Prompt:**
```
A horizontal spectrum visualization with three labeled positions.
Left side: "Magic Oracle" in lighter gray text.
Center: "Partner" in bold teal (#557373), highlighted as the ideal.
Right side: "Broken Tool" in lighter gray text.
Gradient bar connecting all three, brightest at center.
Dark background (#0d0d0d). Modern minimalist style.
Clean sans-serif typography. No icons or decorative elements.

Aspect ratio: 16:9
Avoid: clipart, photographs, complex graphics
```

---

## NEW: hook-question.png

**Purpose**: Opening slide visual for the hook question
**Target**: Provocative question typography

**Nano Banana Prompt:**
```
Large typography slide with the text "What predicts AI success?"
centered on screen. Question mark emphasized and slightly larger.
Modern sans-serif font, white text on dark charcoal background (#1a1a1a).
Subtle teal (#557373) gradient glow behind the text.
Clean, minimal, high-contrast. Presentation slide aesthetic.

Aspect ratio: 16:9
Avoid: images, icons, decorative elements
```

---

## NEW: sample-size.png

**Purpose**: Big number impact slide
**Target**: "667" as hero element

**Nano Banana Prompt:**
```
Large number "667" centered on slide in bold sans-serif typography.
Below it, smaller text: "participants tested"
Number in white, subtext in gray (#888888).
Dark background (#0d0d0d). Subtle teal accent line above the number.
Clean, minimal, corporate presentation style.
Number should dominate the visual hierarchy.

Aspect ratio: 16:9
Avoid: photographs, icons, complex graphics
```

---

## NEW: people-over-prompts.png

**Purpose**: Key insight callout
**Target**: Comparison statement

**Nano Banana Prompt:**
```
Typography-focused slide with text "People Skills > Prompt Skills"
Greater-than symbol in teal (#557373) and larger than surrounding text.
White sans-serif text on dark charcoal background (#1a1a1a).
Clean, bold, minimal. Statement should feel definitive.
Professional presentation aesthetic.

Aspect ratio: 16:9
Avoid: photographs, icons, decorative elements
```

---

## NEW: closing-insight.png

**Purpose**: Final slide statement
**Target**: Memorable closing visual

**Nano Banana Prompt:**
```
Centered typography: "The Most Human Skill" on first line,
"is the Most Valuable One" on second line.
First line in teal (#557373), second line in white.
Dark background (#0d0d0d). Modern sans-serif, medium weight.
Clean, minimal, powerful. Closing slide aesthetic.
Should feel like a thesis statement.

Aspect ratio: 16:9
Avoid: photographs, icons, complex graphics
```
```

---

### KEY TRANSFORMATION DECISIONS

#### 1. Section-to-Slide Mapping

Not every section becomes a single slide. The transformation expands based on:

| Essay-to-Speech Section | Talk Track v5 Slides | Reasoning |
|-------------------------|----------------------|-----------|
| Section 1: Opening Hook | 3 slides | Hook, insight, and evidence each deserve visual anchors |
| Section 2: The Research | 3 slides | Methodology, sample size, and pattern finding |
| Section 3: Why It Works | 3 slides | Question, explanation, and conclusion |
| Section 4: Implications | 2 slides | Contrast and callout |
| Section 5: Takeaway | 3 slides | Landing, CTA, and closing |

**Principle**: One semantic tag moment = one potential slide. Not every moment needs a slide, but key `[HOOK]`, `[KEY_POINT]`, `[EVIDENCE]`, `[CTA]`, and `[LANDING]` tags often do.

#### 2. Image Rating Actions

| Rating | Original Asset | Action Taken | Result |
|--------|---------------|--------------|--------|
| ADAPT | correlation-scatter.png | Regenerate with plain English | evidence-strong-link.png |
| ADAPT | mental-model-diagram.png | Simplify to spectrum | mental-models-spectrum.png |
| RECREATE | coefficient-table.png | Convert to typography | tom-insight.png |
| USE | methodology-diagram.png | Copy directly | methodology-diagram.png |

#### 3. Audio Block Boundaries

Each `<!-- AUDIO -->` block contains exactly what gets spoken for that slide:

```markdown
<!-- AUDIO -->
[TAG] Spoken content here.

More content if needed.
<!-- /AUDIO -->
```

**Rules**:
- One slide = one audio block
- Include `[PAUSE]` markers inside the block
- Semantic tags (`[HOOK]`, `[KEY_POINT]`, etc.) stay in audio blocks
- Delivery markup (`[SLOW]`, `*emphasis*`) also goes inside

#### 4. Speaker Notes Purpose

Speaker notes serve different functions than the audio:

| Audio Block | Speaker Notes |
|-------------|---------------|
| What to say verbatim | How to say it |
| The script | The direction |
| Words for TTS | Guidance for human delivery |

**Example**:
- Audio: `"The pattern was unmistakable."`
- Notes: `Build to the punch line. "Unmistakable" should land with weight.`

#### 5. Section Color Assignment

Colors are assigned for visual organization in the slides table and any downstream HTML/video generation:

```yaml
sections:
  - id: opening
    color: "#557373"  # Teal - establishes brand
  - id: research
    color: "#6B8E6B"  # Sage - factual/evidence tone
  - id: why
    color: "#8B6B6B"  # Dusty rose - explanation
  - id: implications
    color: "#6B6B8E"  # Muted purple - forward-looking
  - id: takeaway
    color: "#8E8B6B"  # Olive - conclusion/action
```

**Principle**: Muted, professional tones that work on dark backgrounds. Avoid saturated primaries.

#### 6. Slide Slug Naming

Slugs should be:
- Descriptive but concise (1-2 words)
- Unique within the presentation
- Related to content, not position

**Good**: `hook`, `insight`, `methodology`, `landing`
**Bad**: `slide1`, `section1-part1`, `the-first-thing`

---

### DOWNSTREAM PIPELINE

After Talk Track v5 is generated:

```
Talk Track v5 (this output)
       ↓
  ┌────┴────┐
  ↓         ↓
Images    Audio
  ↓         ↓
  └────┬────┘
       ↓
HTML Presentation / Remotion Video
```

1. **Images**: Use Nano Banana prompts to generate missing visuals
2. **Audio**: Process `<!-- AUDIO -->` blocks through Kokoro TTS (draft) or ElevenLabs (publish)
3. **Assembly**: HTML engine or Remotion combines slides + audio + images
