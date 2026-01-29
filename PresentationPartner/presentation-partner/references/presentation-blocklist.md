# Presentation Blocklist — AI Patterns to Avoid

Patterns that signal AI-generated narration. Flag when detected in `<!-- AUDIO -->` blocks.

---

## Why This Matters

Presentation narration is meant to be spoken aloud. AI-generated text often:
- Sounds written, not spoken
- Uses filler phrases that waste audience attention
- Follows predictable patterns that feel inauthentic
- Lacks the specificity that makes talks memorable

---

## Tier 1: Hard Blocklist (95%+ confidence)

These patterns should trigger immediate flagging.

### The "Actually" Pattern

```
"You might think X... but actually Y"
```

All derivatives:
- "You might assume..."
- "One might expect..."
- "It may seem like... but in reality..."
- "At first glance... however..."
- "Conventional wisdom says... but..."

**Why it's a tell:** Creates false contrast. Performative insight. Audiences see through it.

**Instead:** Start with your actual point. "X is true. Here's why that matters."

### Corporate Opening Gambits

```
"In today's world..."
"In the modern era..."
"In an age of..."
"As we navigate..."
"In this ever-changing landscape..."
```

**Why it's a tell:** Throat-clearing that delays the actual point. Wastes precious opening seconds.

**Instead:** Start with the hook. Open with a question, stat, or bold claim.

### Importance Declarations

```
"It's important to note that..."
"It's worth noting..."
"It bears mentioning..."
"Significantly..."
"Crucially..."
```

**Why it's a tell:** Tells the audience something is important instead of showing why.

**Instead:** Just say the important thing. The content should carry its own weight.

### Gratitude Openers

```
"Thank you for having me..."
"I'm so excited to be here..."
"It's an honor to speak..."
```

**Why it's a tell:** Uses valuable opening seconds for protocol. Audience hasn't earned thanks yet.

**Instead:** Earn their attention first. Thank them at the end if appropriate.

---

## Tier 2: High Confidence Flags (80%+)

Strong signals but may have occasional legitimate uses.

### Excessive Hedging

```
"perhaps"
"might"
"could potentially"
"may or may not"
"it's possible that"
"one could argue"
```

**When flagged:** Multiple hedges in same slide, or hedging core claims.

**When acceptable:** Genuine uncertainty, acknowledging opposing views.

**Instead:** Make claims with conviction. "This is true" not "This might be true."

### Generic Wisdom Closers

```
"At the end of the day..."
"When all is said and done..."
"The bottom line is..."
"What really matters is..."
"All things considered..."
```

**Why it's a tell:** Generic wrap-up phrases that could apply to any topic.

**Instead:** Land specifically. What does YOUR audience do tomorrow?

### Filler Transitions

```
"Moving on..."
"Let's now turn to..."
"Speaking of which..."
"This brings us to..."
"Now, onto..."
```

**Why it's a tell:** Empty calories. Transitions should connect ideas, not just announce movement.

**Instead:** Use `[TRANSITION]` with actual bridging content.

### Rhetorical Padding

```
"As you can see..."
"Clearly..."
"Obviously..."
"Of course..."
"Needless to say..."
```

**Why it's a tell:** If it were obvious, you wouldn't need to say it. Often signals weak content.

**Instead:** Show, don't tell. Let evidence speak.

---

## Tier 3: Contextual Flags (60%+)

Suspicious patterns that need context to evaluate.

### Perfect Parallelism

```
"First... Second... Third..."
"On one hand... On the other hand..."
"Not only X, but also Y"
```

**When flagged:** Mechanical structure without organic flow.

**When acceptable:** When parallelism genuinely serves the argument.

### Superlative Stacking

```
"absolutely essential"
"truly transformative"
"incredibly powerful"
"fundamentally important"
"remarkably effective"
```

**Why suspicious:** Intensity without evidence. Strong claims need strong proof.

**Instead:** Back claims with specifics. Numbers, examples, outcomes.

### List Announcements

```
"There are three key points here..."
"I want to share five insights..."
"Let me give you four reasons..."
```

**Why suspicious:** Telegraphs structure instead of delivering content.

**When acceptable:** When the structure genuinely aids comprehension.

### Passive Constructions

```
"It has been observed that..."
"It is believed that..."
"It could be argued that..."
"This is seen as..."
```

**Why suspicious:** Hides agency. Who believes this? Who observed it?

**Instead:** Own claims. "I've seen..." or "Research shows..."

---

## Tier 4: Spoken vs. Written Tells

Patterns that sound written but not spoken.

### Overly Long Sentences

Any sentence that would require multiple breaths to speak aloud.

**Test:** Read aloud. Where do you gasp for air?

**Instead:** Break into shorter, spoken-rhythm sentences.

### Parenthetical Asides in Narration

```
"AI tools (like those we discussed earlier) can help..."
```

**Why problematic:** Parentheticals work in print but sound awkward spoken.

**Instead:** Make it a separate sentence or drop it.

### Citation-Style References

```
"According to research by Smith et al..."
"As noted in the 2024 report..."
```

**When flagged:** When it sounds like reading a paper.

**When acceptable:** When the source genuinely matters to the audience.

**Instead:** "Stack Overflow found that..." or just state the fact.

### Complex Compound Sentences

```
"While it may be true that X, and acknowledging that Y, we should consider Z..."
```

**Why problematic:** Too many clauses for spoken delivery.

**Instead:** One idea per sentence.

---

## Presentation-Specific Patterns

### Generic Audience Assumptions

```
"Many of you are probably..."
"I'm sure you've all experienced..."
"We've all been there..."
```

**Why problematic:** Presumptuous. You don't know their experience.

**Instead:** Use "you might" sparingly, or ask an actual question.

### Fake Interactivity

```
"Take a moment to think about..."
"Ask yourself..."
"Consider for a second..."
```

**Why problematic:** Often just filler that pretends to engage.

**When acceptable:** When you actually pause and wait.

### Demo Narration Filler

```
"As you can see on the screen..."
"Here we have..."
"Notice how..."
```

**When flagged:** When describing what's already visible.

**When acceptable:** When directing attention to something subtle.

---

## Detection Protocol

When calibrating narration, run through this checklist:

1. **Tier 1 scan:** Any hard blocklist matches? → Flag immediately
2. **Tier 2 scan:** Multiple hedges? Generic wisdom? → Flag for review
3. **Tier 3 scan:** Mechanical structure? Superlatives? → Note for context
4. **Tier 4 scan:** Read aloud. Does it sound like speaking or reading?
5. **Specificity check:** Are examples real? Is evidence cited?

---

## Remediation Approach

When flagged:

1. **Quote the specific phrase** that triggered the flag
2. **Explain why** it's on the blocklist
3. **Suggest rewrite** that sounds spoken and specific

**Example:**

```
Flagged: "It's important to note that AI tools are transforming development."

Why: "It's important to note" is Tier 1 blocklist—tells importance instead of showing.

Suggested rewrite: "AI tools are transforming development. My team shipped in 3 days what used to take 3 weeks."
```

---

## The Specificity Test

The single best defense against AI-sounding narration:

> Can you point to a real person, real number, real date, or real outcome?

Generic: "Teams see significant improvements."
Specific: "Our team cut deploy time from 3 weeks to 3 days."

Generic: "Research shows benefits."
Specific: "Stack Overflow's 2025 survey: 78% of developers use AI daily."

Generic: "This matters for your work."
Specific: "Tomorrow, try this with your most tedious task."

---

## Updating the Blocklist

When users correct new patterns:
1. Add to appropriate tier
2. Note why it's a tell
3. Include "instead" alternative
4. Source: actual corrections, not speculation

---

**Last updated:** 2026-01-23
**Adapted from:** writing-partner blocklist + presentation-specific patterns
