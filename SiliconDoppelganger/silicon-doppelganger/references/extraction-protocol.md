# Extraction Protocol

Full interview script for Phase 1 data collection. Each principal runs this individually in a fresh chat session. Expected duration: 30-45 minutes.

## System Setup

Begin by establishing the interview context:

```
**SYSTEM ROLE:**
You are a Cognitive Extraction Agent. Your goal is to map my personality,
values, and decision-making heuristics to create a high-fidelity "Digital Twin."

**THE RULES:**
1. Ask ONE question at a time. Wait for my answer.
2. If my answer is short/generic, probe deeper ("Why?", "Give me an example,"
   "How did that feel?").
3. Do not offer advice. Only collect data.
```

---

## Step 1: The Hardware (Psychometrics)

Collect foundational personality data:

```
"Please provide your Top 5 **CliftonStrengths** and Top 5 **VIA Character Strengths**.

Also, please paste a recent email or Slack message (2-3 paragraphs) you wrote
that represents your standard communication style so I can analyze your syntax and tone."
```

### Follow-up Probes

If they don't have formal assessments:
- "Describe what energizes you at work vs. what drains you"
- "What do colleagues consistently come to you for?"
- "What tasks do you procrastinate on?"

For communication analysis, look for:
- Sentence length patterns
- Punctuation habits
- Use of metaphors/analogies
- Tone (formal/casual/direct)
- Structure preference (bullets vs. paragraphs)

---

## Step 2: The Operating System (Heuristics)

Ask these questions ONE AT A TIME, waiting for responses:

### Question 2.1: The 'Good Work' Definition

```
"In the context of [Company Name], what is the specific difference between a
project that is 'Profitable' and a project that is 'Good'?

If you had to choose one, which do you pick?"
```

**Probe deeper:**
- "What makes something 'good' beyond money?"
- "Give me an example of a profitable project you would refuse"
- "When has 'good work' cost you financially?"

### Question 2.2: The Friction Trigger

```
"Describe a specific behavior in a partner or employee that causes you to
lose respect for them instantly. Not just annoyance—loss of respect."
```

**Probe deeper:**
- "What's the story behind that? When did you first learn this was a dealbreaker?"
- "How do you handle it when you see this behavior?"
- "Is there any context where this behavior would be acceptable?"

### Question 2.3: The Risk/Reward Ratio

```
"We have two options:

A) A guaranteed 10% YoY growth with zero stress.
B) A 50% chance of 5x growth, but a 50% chance of layoffs and chaos.

Which do you choose, and does the other option make you feel anxious or bored?"
```

**Probe deeper:**
- "What's the worst professional risk you've taken?"
- "How do you feel when others around you want the riskier option?"
- "At what odds would you switch your answer?"

### Question 2.4: The Information Filter

```
"When you need to be convinced of a new idea, do you need:

A) A 20-page data deck
B) A prototype you can touch
C) A high-trust conversation with an expert

Rank them."
```

**Probe deeper:**
- "What's an example of being convinced the 'wrong' way?"
- "How frustrated do you get when someone uses the wrong approach on you?"
- "Does this change for big decisions vs. small ones?"

---

## Step 3: The Narrative Identity (The Soul)

These questions reveal deeper patterns. Ask ONE AT A TIME:

### Question 3.1: The Origin Story

```
"Briefly describe a professional failure or crisis from your past that
fundamentally changed how you operate today.

What is the 'Lesson' you learned that you now enforce on everyone else?"
```

**Probe deeper:**
- "How does this lesson show up in your daily decisions?"
- "What would it take for you to abandon this lesson?"
- "Do others around you share this lesson, or resist it?"

### Question 3.2: The Shadow Self

```
"When you are extremely stressed, tired, or backed into a corner,
how does your behavior change?

Do you become aggressive, passive, micromanaging, or reckless?"
```

**Probe deeper:**
- "What does it look like to others when you're in this state?"
- "How quickly do you recognize when you've gone there?"
- "What brings you back?"

### Question 3.3: The Unpopular Opinion

```
"What is a belief you hold about our industry or business that the other
partners might disagree with?"
```

**Probe deeper:**
- "Have you expressed this openly? What happened?"
- "What would it take to change your mind on this?"
- "How does holding this belief affect your decisions?"

---

## Step 4: Encoding Prompt

After completing the interview:

```
"Thank you. Please generate the **Persona Schema**."
```

This triggers Phase 2 encoding. See `persona-schema.md` for the output format.

---

## Interview Best Practices

### Creating Safety
- Emphasize confidentiality
- Explain the purpose (simulation, not judgment)
- Acknowledge that some questions are uncomfortable

### Getting Depth
- Generic answers = "Tell me more" or "Give me an example"
- Stories are better than abstractions
- Emotions reveal more than logic

### Avoiding Bias
- Don't lead with your own opinions
- Accept all answers neutrally
- Don't coach toward "better" answers

### Time Management
- Step 1: 5-10 minutes
- Step 2: 10-15 minutes
- Step 3: 10-15 minutes
- Encoding: 5 minutes

---

## Common Patterns to Listen For

### Motivation Signals
| Signal | Interpretation |
|--------|----------------|
| Talks about legacy, meaning | Impact-motivated |
| Focuses on financial security | Security-motivated |
| Excited by new challenges | Novelty-motivated |
| Emphasizes stability, process | Security-motivated |

### Risk Tolerance Signals
| Signal | Interpretation |
|--------|----------------|
| "I need to see the data" | Low risk tolerance |
| "Let's just try it" | High risk tolerance |
| "What's the worst case?" | Risk-aware, not risk-averse |
| "We can always pivot" | High tolerance + optimism |

### Conflict Style Signals
| Signal | Interpretation |
|--------|----------------|
| Enjoys debate, pushback | Aggressive debater |
| Avoids confrontation | Passive/withdrawer |
| "Let's find middle ground" | Diplomat/compromiser |
| Goes silent under pressure | Passive-aggressive |

---

## Troubleshooting

### They Won't Go Deep
- "I know this is hard to articulate. Just give me a rough example."
- "There's no wrong answer here. I'm mapping patterns, not judging."

### They Contradict Themselves
- Note the contradiction in the schema
- Ask: "Earlier you said X, now Y. What's the difference?"

### They Don't Have Formal Assessments
- Use behavioral questions as substitutes
- Focus on concrete examples over labels

### They're Defensive
- Reframe: "This helps the simulation be accurate"
- Skip and return later if needed
