# Semantic Tags Guide

When and how to use semantic tags in `<!-- AUDIO -->` blocks for effective presentation narration.

---

## Purpose

Semantic tags serve two functions:
1. **Structure:** Help the author organize narrative flow
2. **Generation:** Guide timing and emphasis in audio/video output

Tags are metadata—they're stripped from TTS input but inform pacing and visual cues.

---

## Tag Reference

### [HOOK]

**Purpose:** Grab attention in the opening seconds.

**When to use:**
- First slide, first 1-2 sentences only
- After a major section transition (rare)
- When re-engaging after a demo or break

**When NOT to use:**
- Every slide (dilutes impact)
- For general "interesting" statements

**Example:**
```markdown
<!-- AUDIO -->
[HOOK] What if writing code felt less like fighting with syntax and more like having a conversation?

Welcome everyone. Today we're exploring...
<!-- /AUDIO -->
```

**Pattern:** Question, surprising stat, bold claim, or vivid scenario.

---

### [KEY_POINT]

**Purpose:** Mark the core takeaway for a slide.

**When to use:**
- Once per slide (ideally)
- The one thing the audience should remember from this slide
- After setup, before elaboration

**When NOT to use:**
- Multiple times per slide (pick one)
- For supporting points (those are just text)

**Example:**
```markdown
<!-- AUDIO -->
The data tells a clear story.

[KEY_POINT] Developers spend only 30% of their time writing new code.

The rest goes to debugging, documentation, and context switching.
<!-- /AUDIO -->
```

**Pattern:** Single sentence, clear claim, quotable.

---

### [EVIDENCE]

**Purpose:** Mark data, research, or proof.

**When to use:**
- Citing statistics or studies
- Referencing specific examples
- Providing proof for claims

**When NOT to use:**
- Vague references ("studies show...")
- Hypothetical examples
- Unverifiable claims

**Example:**
```markdown
<!-- AUDIO -->
[EVIDENCE] According to Stack Overflow's 2025 Developer Survey, 78% of developers now use AI assistants daily—up from 44% just two years ago.

This isn't a trend. It's a transformation.
<!-- /AUDIO -->
```

**Pattern:** Specific source, concrete numbers, verifiable.

---

### [STORY]

**Purpose:** Mark narrative examples or case studies.

**When to use:**
- Personal anecdotes
- Customer/user stories
- Case studies
- Before/after scenarios

**When NOT to use:**
- Fabricated examples (ground truth only)
- Generic scenarios
- "Imagine if..." constructions

**Example:**
```markdown
<!-- AUDIO -->
[STORY] Last month, a team I work with shipped a feature in 3 days that would have taken 3 weeks before. Same team, same skills—different tools.

They didn't work longer hours. They worked smarter.
<!-- /AUDIO -->
```

**Pattern:** Real people, real outcomes, concrete details.

---

### [TRANSITION]

**Purpose:** Connect major sections or narrative beats.

**When to use:**
- Moving between sections (problem → solution)
- Shifting gears (setup → demo)
- After major points, before new topic

**When NOT to use:**
- Every slide (use sparingly)
- Mid-thought (that's just prose)

**Example:**
```markdown
<!-- AUDIO -->
[TRANSITION] Now that we've seen the problem, let's talk about what's changing.

The shift to AI-native development isn't incremental.
<!-- /AUDIO -->
```

**Pattern:** Backward glance + forward motion. Bridges two ideas.

---

### [CALLBACK]

**Purpose:** Reference an earlier point for reinforcement.

**When to use:**
- Connecting current point to earlier slide
- Building cumulative argument
- Creating "aha" moments by linking ideas

**When NOT to use:**
- If the audience won't remember the reference
- Forced connections
- Within the same slide

**Example:**
```markdown
<!-- AUDIO -->
Watch as I describe intent and the AI handles the boilerplate.

[CALLBACK] Remember that 70% we talked about? This is how we reclaim it.
<!-- /AUDIO -->
```

**Pattern:** Reference + relevance. "Remember X? This is Y."

---

### [LANDING]

**Purpose:** Deliver the closing emotional beat.

**When to use:**
- Final slide of main content
- End of a major section (sometimes)
- The feeling you want them to carry out

**When NOT to use:**
- Multiple times (one landing per talk)
- Mid-presentation
- Appendix slides

**Example:**
```markdown
<!-- AUDIO -->
[LANDING] The future of software development isn't AI versus humans.

It's what humans can accomplish when AI has their back.

Thank you.
<!-- /AUDIO -->
```

**Pattern:** Emotional resonance, memorable phrasing, complete thought.

---

### [CTA]

**Purpose:** Tell them what to do next.

**When to use:**
- Near the end
- After making the case
- When you have a specific ask

**When NOT to use:**
- Multiple CTAs (one clear action)
- Vague suggestions
- Beginning of the talk

**Example:**
```markdown
<!-- AUDIO -->
[CTA] I want you to try one thing this week. Take your most tedious coding task and see if an AI assistant can help.

Start small. Build confidence. Then expand.
<!-- /AUDIO -->
```

**Pattern:** Specific, actionable, timebound if possible.

---

### [PAUSE:ms]

**Purpose:** Insert intentional silence for effect.

**When to use:**
- After a hook (let it land)
- After a key point (emphasis)
- Before a reveal
- Rhetorical questions

**When NOT to use:**
- Excessive pauses (audience checks phones)
- Every few sentences
- During dense content

**Typical values:**
- `[PAUSE:300]` - Brief beat (breath)
- `[PAUSE:500]` - Standard dramatic pause
- `[PAUSE:1000]` - Major emphasis or section break

**Example:**
```markdown
<!-- AUDIO -->
Sound familiar?

[PAUSE:500]

Here's what the data shows...
<!-- /AUDIO -->
```

---

## Tag Distribution

Typical distribution for a 15-minute, 6-slide presentation:

| Tag | Frequency |
|-----|-----------|
| `[HOOK]` | 1 (slide 1) |
| `[KEY_POINT]` | 4-6 (most slides) |
| `[EVIDENCE]` | 2-3 (supporting slides) |
| `[STORY]` | 1-2 (memorable moments) |
| `[TRANSITION]` | 2-3 (section changes) |
| `[CALLBACK]` | 1-2 (reinforcement) |
| `[LANDING]` | 1 (final slide) |
| `[CTA]` | 1 (end) |
| `[PAUSE:ms]` | 5-10 (strategic moments) |

---

## Anti-Patterns

**Over-tagging:**
```markdown
<!-- BAD -->
[HOOK] [KEY_POINT] This is really important [EVIDENCE] because [PAUSE:300] data shows...
```

**Under-tagging:**
```markdown
<!-- BAD - no structure visible -->
Welcome everyone. Today I'll talk about AI. It's important. Here's why...
```

**Wrong tag for content:**
```markdown
<!-- BAD - not actually evidence -->
[EVIDENCE] I think AI is going to change everything.
```

---

## Quality Checklist

Before finalizing a Talk Track, verify:

- [ ] Opening slide has exactly one `[HOOK]`
- [ ] Most slides have one `[KEY_POINT]`
- [ ] `[EVIDENCE]` tags point to real, citable data
- [ ] `[STORY]` tags use real examples, not hypotheticals
- [ ] Section changes have `[TRANSITION]`
- [ ] Final slide has `[LANDING]`
- [ ] Clear `[CTA]` near the end
- [ ] `[PAUSE]` values are reasonable (300-1000ms typical)

---

**See also:**
- `talk-track-v5-spec.md` - Format specification
- `presentation-blocklist.md` - Patterns to avoid
