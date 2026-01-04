---
status: draft-from-interview
title: "Claimify: Epistemic Self-Defense for the Information Age"
series: 12 Days of Original AI Skills
day: 3
skill: claimify
version: 2.0.0-draft
angle: "Guard your mind from manipulation—both intentional and accidental."
interview-date: 2025-12-19
---

# Day 3: Claimify

*Epistemic Self-Defense for the Information Age*

---

The internet is full of well-written hot garbage.

I don't mean spam or obvious misinformation. I mean polished prose that sounds authoritative, follows proper grammar, uses sophisticated vocabulary—and makes claims that don't hold up. Essays with unsupported assertions. Articles that manipulate through framing rather than facts. Arguments that work on you without you noticing.

I needed a tool to see through it. Not occasionally. Constantly.

---

## The Problem: Invisible Manipulation

There's a spectrum here that matters. On one end: deliberate propaganda, carefully crafted to shift your beliefs. On the other: sloppy thinking, writers who don't examine their own assumptions. Both do damage.

The techniques are the same whether intentional or not:

**Russell conjugation.** I have firm convictions. You are stubborn. He is a pig-headed fool. Same underlying fact, three different emotional loads. Writers choose their conjugations. You absorb them.

**Assumption hiding.** The premises that would make the conclusion controversial are buried—sometimes in footnotes, sometimes not stated at all. The argument looks airtight because the contested parts are invisible.

**Framing effects.** "Low-risk incremental improvement" vs. "steady march toward dangerous capabilities." Same trajectory. Different response in your nervous system.

I kept reading essays and thinking: *what is this actually claiming?* What's the argument structure? What assumptions make it work? Where are the weak points?

That question—asked rigorously—is Claimify.

---

## What It Actually Does

Claimify is a Claude skill for claim extraction and argument analysis. It does three things:

**1. Extraction.** Take any text—essay, article, transcript, report—and pull out every distinct claim. Not summaries. Individual propositions that can be true or false.

**2. Classification.** Each claim gets typed:
- **Factual:** Verifiable against evidence
- **Normative:** Value judgments about what should be
- **Definitional:** What terms mean
- **Causal:** What causes what
- **Predictive:** What will happen
- **Assumption:** Unstated premises the argument requires

**3. Mapping.** How do claims relate? Which support which? Which contradict? Which assume others without acknowledgment? The structure of the argument, made visible.

The approach isn't novel. Microsoft Research published [a paper on LLM-based claim extraction](https://arxiv.org/abs/2502.10855) (also called Claimify) showing that language models can reliably extract and evaluate factual claims—outperforming existing methods when handling ambiguous source text. I had Claude research argumentation theory and synthesize it into something practical for my workflow. The taxonomy isn't original; the integration is.

---

## A Real Example: METR's GPT-5.1 Evaluation

Theory is easy. Let me show you what it looks like on real content.

METR recently published an evaluation of GPT-5.1-Codex-Max, assessing whether it poses risk for AI R&D automation and rogue replication. The headline: "low-risk incremental improvement."

I ran Claimify on it. Here's what emerged:

### The Claim Structure

The core argument chain:

```text
[Empirical Anchor]
C2: Measured performance: 2h42m on benchmark
    ↓
[Interpretation]
C4: On-trend vs GPT-5 (2h17m → 2h42m)
    ↓
C1: Low-risk incremental improvement
    ↓
[Extrapolation]
C7: 13h25m by April 2026 if trends hold
    ↓
[Conclusion]
C24: Overall takeover risk very low
```

One empirical measurement. One trend comparison. Everything else is interpretation and prediction.

### Hidden Assumptions

The argument requires premises never stated as claims:

- **Time-horizon metric is valid.** The core metric—time to complete benchmark tasks—assumes this predicts dangerous capabilities. A model might be slow at benchmarks but fast at finding novel exploits.

- **Linear extrapolation works.** The predictions assume capability improvements follow smooth curves. AI history shows multiple discontinuities.

- **Reasoning traces are transparent.** The analysis of 81 reasoning traces assumes models externalize their reasoning faithfully. The report notes "no direct training pressure" to hide reasoning—not that hiding is impossible.

- **Developer assurances are accurate.** Multiple conclusions depend on OpenAI claims that were "not independently verified."

### Framing Effects

Watch the language choices:

**"Low-risk incremental improvement"** — "Incremental" suggests small, manageable. "Low-risk" front-loads the conclusion. Alternative framing: "measurable capability increase" or "continued progress toward greater capability."

**"On-trend" vs. "trend-break"** — The default case is framed as safe. Risk requires exceptional events. This frames continued development as conservative—when historically, AI development has been characterized by frequent surprises.

**"Developer assurances"** — "Assurances" carries positive valence. Compare with "claims" or "assertions."

### The Structural Tension

Here's the contradiction I found most striking:

The report opens with "Note on independence" but immediately discloses that OpenAI's "comms and legal team required review and approval of this post."

It continues: OpenAI "would have had the legal right to block us from sharing conclusions about risk."

That's not independence. That's approved disclosure. The framing obscures what the content reveals.

### The Gap

What METR actually demonstrated:
1. GPT-5.1-Codex-Max completed a specific benchmark 25 minutes faster than GPT-5
2. This is consistent with recent trends
3. Under specific assumptions, extrapolation doesn't cross their thresholds

What the headline implies:
1. "Low-risk" as a general property (only 2 of many threat models)
2. Robust 6-month forecast (depends on "if trends hold")
3. Independent evaluation (OpenAI had approval rights)

The gap between what was shown and what readers conclude is precisely what Claimify exposes.

---

## Why This Matters

I want to wire Claimify into every system that puts tokens into my mind.

That's not hyperbole—it's the logical endpoint.

Every essay you read, every article, every YouTube transcript—they're all making claims. Some supported, some not. Some explicit, some assumed. Some framed neutrally, some designed to move you.

You can't evaluate what you can't see. Claimify makes invisible logic visible.

This isn't about catching liars. Most bad arguments aren't malicious. They're lazy—assumptions unexamined, framings unconsidered, conclusions outrunning evidence. The writer might not know they're doing it.

The fix is the same either way: see the structure, name the assumptions, notice the framing. Then decide what you believe based on the actual argument, not its surface presentation.

---

## How I Use It

I run Claimify regularly on:

- **Essays and articles** where I catch myself nodding along—agreement is when I most need scrutiny
- **Technical reports** with authoritative tone but policy implications
- **My own drafts** before publishing—what am I actually claiming? What am I assuming?

The last one matters. Claimify makes me a better writer because it forces me to know my own argument. If I can't articulate the claim structure, the assumptions, the relationship between my points—I haven't thought it through.

Epistemic self-defense and clear thinking are the same practice.

---

## The Bigger Picture

We're in an information environment where:
- More content is generated than ever before
- Production quality (grammar, structure, polish) tells you nothing about truth
- Sophisticated manipulation is cheap and scalable
- Most people have no tools for structural analysis

This is memetic warfare territory. Not in the paranoid sense—in the practical sense. Ideas compete for your belief. Some are true. Some are useful. Some are designed to benefit someone else at your expense.

You need defenses. Not filters that block content—tools that reveal structure. Not someone telling you what to think—capability to evaluate for yourself.

Claimify is one such tool. Run it on the things you read. Run it on the things you write. Make the invisible visible.

Wire it into every system that puts tokens in your mind. Guard the ecology.

---

## Quick Start

```bash
# Install the skill
git clone https://github.com/leegonzales/AISkills.git
cp -r AISkills/Claimify/claimify ~/.claude/skills/

# Then invoke
```

- "Claimify this essay" — Full extraction, classification, and mapping
- "What are the hidden assumptions here?" — Focus on unstated premises
- "Run a Russell conjugation analysis" — Focus on framing effects
- "What's the gap between claims and evidence?" — Focus on overreach

---

## What I Learned

I built Claimify because I was drowning in well-written garbage. Essays that felt persuasive but didn't hold up. Arguments that worked on me before I could think.

The solution wasn't reading less—it was reading better. Structural analysis. Claim extraction. Assumption surfacing. The practices exist in argumentation theory; I just needed them accessible in my workflow.

Now when I read something that feels important, I can ask: what is it actually claiming? And get an answer I can evaluate.

That's the cornerstone of good thinking. That's protecting your mind from manipulation—intentional and otherwise.

Tomorrow: [Day 4 Skill]

---

*Day 3 of 12 Days of Original AI Skills*
