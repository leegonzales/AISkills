---
status: drafting
title: "Prose Polish: Making the Invisible Visible"
series: 12 Days of Original AI Skills
day: 1
skill: prose-polish
version: 2.0.0
angle: "AI writing has tells. I built a system to see them—and fix them."
---

# Day 1: Prose Polish

*Making the Invisible Visible in AI-Generated Text*

---

I write with AI constantly. Not *using* AI to write—writing *with* AI. Conversations that become essays. Ideas that emerge from back-and-forth. The chat is the raw material.

But here's what I kept noticing: the output didn't sound like me. Grammatically perfect. Topically relevant. Completely soulless.

I needed a way to see what was going wrong.

---

## The Problem I Was Solving

I wanted AI as an intellectual prosthesis—something that extends my thinking, not replaces it. I provide the spark, the taste, the vision. AI provides the words, the elevation, the structure. That's the collaboration I want.

But the collaboration kept breaking down in a specific way. The writing would lose its animating spirit somewhere between my ideas and the final prose. Sentences that were technically correct but lacked... something. I couldn't articulate what was missing until I started cataloging examples.

Fifty AI-generated openings. A hundred. Patterns emerged.

"In today's rapidly evolving landscape..."

"This comprehensive guide will delve into..."

"It's important to note that..."

The same phrases. The same rhythms. The same hedging. Over and over.

I'd found the tells. But seeing them wasn't enough. I needed a system that could detect them, explain why they're problems, and help fix them.

---

## What Prose Polish Actually Does

Prose Polish is a Claude skill—a specialized system prompt with heuristic rules and remediation patterns. When you install it, Claude gains new capabilities for analyzing and improving text. The skill operates in four modes:

**Detection:** Analyze any text for AI patterns. Get a scored report (0-100) with specific issues flagged by line number. The scoring isn't about "gotcha" detection—it's about identifying craft weaknesses.

**Elevation:** Take flagged text and fix it. Three-pass remediation: rhythm first (sentence variance), then commitment (remove hedges, add specificity), then voice (personality, embodiment, risk).

**Prevention:** Generate new content with anti-pattern constraints baked in. The skill constructs prompts that avoid common pitfalls before they happen.

**Training:** Learn to spot patterns yourself. Annotated examples, principle explanations, practice exercises.

---

## The Four-Layer Assessment

This is the original innovation I'm most proud of. Existing "AI detectors" look at surface features—word frequency, perplexity scores. They miss what matters.

Prose Polish assesses four distinct layers:

**Lexical:** Banned word density. "Delve," "robust," "comprehensive," "leverage." These words aren't inherently bad—they're *overused* by AI systems. When they cluster, something's off.

**Structural:** Sentence length variance. AI text tends toward uniformity—sentences hovering around 12-15 words with minimal variation. Human writing breathes. Five-word punches followed by thirty-word explorations.

**Rhetorical:** Commitment level. AI hedges constantly. "It's important to note that..." "This can be particularly useful when..." Real writers make claims. They take positions. They risk being wrong.

**Voice:** Embodiment. Does this feel like it came from someone with a body? Someone who's experienced things? Or does it float in abstract space, making vague gestures toward expertise?

---

## The Pattern I Can't Stand

There's one AI pattern that makes me wince every time I see it:

> "You might think [common assumption]... but actually, let me show you why it's really [slightly different thing]."

And all its variations:
- "You might think X is about Y... but actually..."
- "Conventional wisdom says... however, the reality is more nuanced..."
- "Most people assume... but here's what they're missing..."

It's a false contrarian move. It sets up a strawman of what "you" believe, then knocks it down with a revelation that isn't revelatory. The structure promises insight and delivers throat-clearing.

The fix: if you have a contrarian point, make it directly. Don't tell me what I think first. Just say the thing.

---

## The Other Tell: Perfect Sentences, No Soul

The lexical patterns are easy to spot. The deeper problem is harder to name.

AI writes sentences that are grammatically flawless and completely lifeless. Every clause balanced. Every transition smooth. No rough edges, no surprising turns, no sense that a human made choices.

I call it lack of perplexity—not in the technical sense, but in the felt sense. Human writing has texture. It stumbles. It takes risks. It sounds like someone thinking out loud.

AI writing sounds like no one at all.

---

## How the Scoring Works

The 0-100 score maps to interpretation:

- **0-20:** Likely human-written
- **21-40:** Possibly AI-assisted
- **41-60:** Probably AI-generated
- **61-80:** Very likely AI
- **81-100:** Almost certainly unedited AI output

Context matters. Content marketing frequently scores 60-80—not because it's bad, but because AI patterns reflect genre conventions in corporate communication. Technical writing with specific code examples typically scores lower.

The goal isn't undetectability. The goal is excellent writing.

---

## A Real Example

**Input** (synthesized from common AI patterns):

> "In today's rapidly evolving digital landscape, organizations must leverage robust solutions to achieve comprehensive transformation. You might think digital transformation is primarily about technology—but actually, it's really about culture and process alignment."

**Prose Polish Analysis:**

Score: 82/100 (Almost Certainly AI)

Lexical issues: "leverage" (AI overuse), "robust solutions" (generic phrase), "comprehensive" (modifier inflation), "digital landscape" (cliché)

Structural issues: Two sentences, both in the 15-20 word range. No variance.

Rhetorical issues: The "you might think... but actually" pattern. Zero specificity. No names, numbers, or concrete examples.

**What Actually Works:**

> "Digital transformation fails when companies buy software and hope for magic. I've seen it repeatedly: new tools, same processes, no change. What works is smaller. Pick one workflow—say, customer onboarding. Map every step. Find the three biggest delays. Fix those with the simplest tool that addresses the actual problem. Then measure. The technology matters less than the focus."

This version makes claims. It could be wrong. Someone could disagree. That's the point.

---

## When the Score Misleads

The scoring system has limits. I built it; I should tell you where it breaks.

**False positives:** Legal writing often scores 50-60. It *should* hedge. "This may constitute a violation" isn't weak writing—it's appropriate caution. Same with scientific papers. "Results suggest" isn't AI hedging; it's methodological honesty.

**False negatives:** I've seen human-written marketing copy score 15-20—clean, varied sentences, no banned words—that was still vapid filler. The score measures *how* you write, not *what* you're saying. Empty calories can be well-prepared.

The score is a diagnostic, not a judgment. High scores don't mean "bad." Low scores don't mean "good." They mean "these patterns are present" or "these patterns are absent." You decide what to do with that information.

---

## Why This Matters Beyond Detection

I don't care about AI detection for its own sake. I care about writing that works.

The patterns Prose Polish flags are craft problems, not ethics problems. Hedging weakens arguments. Uniformity bores readers. Vagueness fails to communicate.

Whether a human or AI wrote something matters less than whether it accomplishes its purpose. Understanding AI patterns helps you see craft weaknesses you might otherwise miss—in your own writing, regardless of how you produced it.

And here's the thing: I use Prose Polish on my own writing too. Not because I'm worried about sounding like AI, but because the same patterns that make AI writing weak can creep into human writing. The skill makes invisible weaknesses visible. That's useful for everyone.

---

## The Quality Tests

Every output should pass five tests:

**Read-Aloud Test:** Does it sound like human breath and thinking when spoken?

**Surprise Test:** Does it contain at least one unexpected sentence?

**Specificity Test:** Does it include concrete details—names, numbers, dates?

**Risk Test:** Does it make at least one contestable claim?

**Embodiment Test:** Does it feel like it came from someone with a body and real experiences?

---

## Quick Start

**For Claude Code CLI users:**

```bash
# Clone the AISkills repository
git clone https://github.com/leegonzales/AISkills.git
cd AISkills

# Install to personal skills (available in all projects)
cp -r ProsePolish/prose-polish ~/.claude/skills/

# Or install to current project only
mkdir -p .claude/skills && cp -r ProsePolish/prose-polish .claude/skills/
```

This works in Claude Code terminal or Claude-powered editors (Cursor, Windsurf, etc.).

**For Web Claude (claude.ai):** Download the skill prompt from the [dist folder](https://github.com/leegonzales/AISkills/tree/main/dist) and add it to your Project's custom instructions.

Then invoke with:
- "Analyze this text for AI patterns" (Detection)
- "Improve this text" (Elevation)
- "Write [X] with quality focus" (Prevention)

---

## What I Learned Building This

I built Prose Polish because I wanted AI as an intellectual prosthesis, not a replacement for my voice. The collaboration should work like this: I provide the spark—the ideas, the taste, the judgment about what matters. AI helps with the words, the structure, the elevation.

But that collaboration requires being able to see when the AI voice is drowning out the human voice. Prose Polish makes that visible.

The patterns it flags aren't just "AI tells." They're craft weaknesses that existed long before AI—hedging, vagueness, uniformity. AI just produces them at scale and with perfect consistency.

If the skill helps you write better, I don't care whether you're editing AI output or polishing your own first draft. The goal is writing where your mind shines through.

---

## Appendix: Prose Polish in Action

I ran Prose Polish against four different writing samples to show what it actually does. Here's the summary:

| Sample | Score | Verdict | Key Patterns |
|--------|-------|---------|--------------|
| **AI-Generated** | 89/100 | Almost Certainly AI | "delve," "landscape," false contrarian, no specifics |
| **CNN News** | 44/100 | Probably AI / Genre-Formulaic | Good specificity, but formulaic structure |
| **Wikipedia** | 32/100 | Possibly AI-Assisted | Dense academic style, appropriate for genre |
| **Economist** | ~18/100 | Likely Human | Wit, concrete analogy, commitment |

**What separates them:**

The AI sample opens with "In today's fast-paced business environment..." and ends with "Are you ready to embark on this transformative journey?" It uses "delve," "landscape," "leverage," and the "you might think... but actually" pattern. Zero specificity. Every claim hedged.

The Economist sample opens with "Groucho Marx memorably said..." and immediately makes a claim about eurozone economies. Unexpected reference, specific analogy, committed position.

**Before and After:**

Here's the AI sample after elevation (89 → ~25):

**Before:**
> "In today's fast-paced business environment, artificial intelligence is fundamentally transforming how organizations operate. You might think that AI is just another technology trend. However, the reality is far more nuanced..."

**After:**
> "Most AI adoption fails. Not because the technology doesn't work—it does. It fails because companies treat AI like magic software: install it, hope for transformation, wonder why nothing changed.
>
> I've watched this pattern repeat. A Fortune 500 retail company spent $40 million on an AI platform in 2023. Eighteen months later, exactly three teams use it. The rest went back to spreadsheets."

The full reports with detailed analysis:
- [AI-Generated Sample Report](https://gist.github.com/leegonzales/da2ad19a612b664b3295589521f53a1e) (Score: 89/100)
- [Four Samples Compared](https://gist.github.com/leegonzales/c968df445a9ed95f2b93bb3b67817341)

---

Tomorrow: Nano Banana—AI image generation that actually works.

---

*This is Day 1 of 12 Days of Original AI Skills—a series showcasing Claude Code skills I built from scratch to solve real problems.*
