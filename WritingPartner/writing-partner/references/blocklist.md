# Voice Blocklist — AI Tells to Avoid

Patterns that signal AI-generated text. Auto-flag with high confidence when detected.

---

## Tier 1: Hard Blocklist (95%+ confidence)

These patterns should trigger immediate flagging. Lee has explicitly identified these.

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

**Why it's a tell:** Creates false contrast, sounds like performative insight. Lee's observation, not invented.

### Corporate Opening Gambits

```
"In today's world..."
"In the modern era..."
"In an age of..."
"As we navigate..."
```

**Why it's a tell:** Throat-clearing that delays the actual point. Lee starts with the point.

### Importance Declarations

```
"It's important to note that..."
"It's worth noting..."
"It bears mentioning..."
"Significantly..."
"Crucially..."
```

**Why it's a tell:** Tells the reader something is important instead of showing why.

---

## Tier 2: High Confidence Flags (80%+)

These patterns are strong signals but may have occasional legitimate uses.

### Excessive Hedging

```
"perhaps"
"might"
"could potentially"
"may or may not"
"it's possible that"
"one could argue"
```

**When flagged:** Multiple hedges in same paragraph, or hedging core claims.

**When acceptable:** Genuine uncertainty, speculative sections.

### Generic Wisdom

```
"At the end of the day..."
"When all is said and done..."
"The bottom line is..."
"What really matters is..."
```

**Why it's a tell:** Generic wrap-up phrases that could apply to anything.

### Listicle Formatting

```
🎯 **Key Insight:**
✨ **Pro Tip:**
💡 **Remember:**
```

**Why it's a tell:** Performative structure over substance. Lee doesn't write like a listicle.

---

## Tier 3: Contextual Flags (60%+)

These patterns are suspicious but need context to evaluate.

### Perfect Parallelism

```
"First... Second... Third..."
"On one hand... On the other hand..."
"Not only X, but also Y"
```

**When flagged:** Mechanical structure without organic flow.

**When acceptable:** When parallelism serves the argument.

### Superlative Stacking

```
"absolutely essential"
"truly transformative"
"incredibly powerful"
"fundamentally important"
```

**Why suspicious:** Intensity without evidence. Lee backs claims with specifics.

### Passive Constructions

```
"It has been observed that..."
"It is believed that..."
"It could be argued that..."
```

**Why suspicious:** Hides agency. Lee owns his claims.

---

## Tier 4: Soullessness Indicators

Not specific phrases but patterns that signal AI-generated prose.

### Grammatical Perfection + Zero Friction

Every sentence technically correct but nothing snags attention. No parenthetical asides, no rhythm variation, no thinking-out-loud quality.

**Test:** Read aloud. Does it sound like someone talking or like a textbook?

### Generic Examples

```
"For example, imagine a scenario where..."
"Consider the case of a hypothetical..."
```

**Lee's style:** Concrete, specific examples from real experience.

### Missing "I"

Long passages without first-person ownership. Lee's voice is present—he uses "I" when he means it.

---

## Detection Protocol

When calibrating, run through this checklist:

1. **Tier 1 scan:** Any hard blocklist matches? → Flag immediately
2. **Tier 2 scan:** Multiple hedges? Generic wisdom? → Flag for review
3. **Tier 3 scan:** Mechanical structure? Superlatives without evidence? → Note for context
4. **Tier 4 feel:** Does it sound like Lee or like AI? → Compare to WritingSamples/

---

## Remediation Approach

When flagged:

1. **Quote the specific phrase** that triggered the flag
2. **Explain why** it's on the blocklist
3. **Show alternative** from WritingSamples/ if available
4. **Suggest rewrite** in Lee's voice

**Example:**

```
Flagged: "It's important to note that collaborative emergence matters."

Why: "It's important to note" is on the blocklist—it tells importance instead of showing.

Alternative from WritingSamples/: "Collaborative emergence matters because..."

Suggested rewrite: "Collaborative emergence is the whole point. Without it, you just have AI writing about you instead of with you."
```

---

## Updating the Blocklist

When Lee corrects a new pattern:
1. Add to appropriate tier
2. Note why it's a tell
3. Include example of what Lee prefers instead

The blocklist should grow from actual corrections, not speculation.

---

**Last updated:** 2025-12-18
**Source:** Interview session + Lee's explicit observations
