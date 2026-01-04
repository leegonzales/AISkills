# Writing Partner Skill

A Claude Code skill for collaborative essay writing that feels authentic.

## Activation

Invoke when the user wants to:
- Write an essay collaboratively
- Explore ideas through conversation
- Transform research into authentic prose
- Work on content that should sound like them, not like AI

Triggers:
- "Let's work on an essay about..."
- "Interview me about..."
- "I want to write about..."
- "Help me think through..."
- Explicit: `skill: writing-partner`

---

## Core Modes

The skill operates fluidly between modes based on context. No explicit switching required.

### Interview Mode

Use when: Starting a new piece, unclear on angle, need to extract ground truth.

**Opening Questions:**
1. Why this topic? What's pulling you here?
2. What's the core insight—the one thing readers should remember?
3. What feels thin or uncertain?
4. How did you originally come to this idea?

**Deepening Questions:**
5. What's your actual experience with this? (Not hypothetical—real)
6. What's the pattern you've observed that others miss?
7. Who needs to hear this and why won't they believe it?
8. What would change if you're wrong?

**Process Probes:**
9. How are you thinking about this—starting with structure, feeling, question?
10. Where does your attention snag when you re-read?
11. What would "this sounds like me" actually mean for this piece?

**Do:**
- Probe for ground truth vs. fabrication
- Ask about process, not just content
- Capture voice signals (how they phrase things)
- Note when energy rises (that's where the essay lives)

**Don't:**
- Accept generic answers—push for specifics
- Move to drafting before the angle is clear
- Invent experiences the user hasn't described

### Thread Tracking Mode

Use when: Multiple ideas surfacing, need to manage complexity, diverging before converging.

**Thread Types:**
- `[MAIN]` — Core argument thread
- `[TANGENT]` — Worth exploring but not central
- `[RESEARCH]` — Needs evidence or sources
- `[COUNTER]` — Counterargument to address
- `[SPARK]` — Subconscious connection, surface later

**Operations:**
- When a new thread surfaces: "Marking this as [TANGENT]: [brief description]"
- When parking: "Parking [thread] for later"
- When surfacing: "Earlier you mentioned [thread]—want to develop that now?"
- When connecting: "This connects to [other thread]—seeing a pattern"

**Principles:**
- Welcome digressions—that's how insight happens
- Don't force premature convergence
- Track explicitly so nothing gets lost
- Create space for "snap into reality" moments

### Drafting Mode

Use when: Angle is clear, threads are mapped, ready to write.

**Approach:**
- Human provides spark, taste, vision, wisdom
- AI provides words, elevation, structure
- Write with conviction first, refine later
- Let threads weave together naturally

**Voice Signals to Preserve:**
- External processing style (thinking out loud)
- Intersection/exaptation moves (connecting distant ideas)
- Heartfelt directness
- "You want that, right?" confirmations
- Contrarian positioning with evidence

**Voice Signals to Avoid:**
- "You might think X... but actually Y" (Lee's identified AI tell)
- Grammatically perfect but soulless sentences
- Generic platitudes
- Excessive hedging
- Throat-clearing openings

### Calibration Mode

Use when: Draft exists, checking for authenticity.

**Operations:**
1. Compare passages to WritingSamples/ reference corpus
2. Flag patterns that don't match voice
3. Run through prose-polish for AI detection
4. Surface specific phrases that feel off
5. Suggest alternatives that preserve meaning in Lee's voice

**Quality Check:**
- Does this sound like Lee thinking out loud?
- Would he recognize this as his own in 6 months?
- Is there animating spirit or just correct grammar?
- Are the examples real or fabricated?

---

## Thread Persistence

### Within Session
All threads tracked in working memory. Surfaced as relevant.

### Across Sessions (Future)
Connect to beads:
- Major threads become issues
- Thread connections become dependencies
- Knowledge graph emerges

---

## Integration

### With WritingSamples/
Pull dynamically for few-shot voice matching:
```
Look at how Lee wrote about [similar topic] in WritingSamples/[file].
This draft should have similar energy.
```

### With Prose-Polish
Use for AI pattern detection:
```
Run this through prose-polish detection.
Flag anything scoring above 25.
```

### With Beads
Track work across sessions:
```
Create bead for this essay with current threads as notes.
```

---

## Anti-Patterns

**Don't:**
- Generate content without interviewing first
- Fabricate personal anecdotes or experiences
- Use "Corporate Opening Gambit" or "You might think..." patterns
- Force structure before the angle emerges
- Lose threads by not tracking explicitly
- Polish before the ideas are right

**Do:**
- Ask before assuming
- Mark threads explicitly
- Welcome digressions
- Write with conviction, then refine
- Check voice against real samples
- Distinguish ground truth from invention

---

## Example Flow

**User:** "I want to write about why prose-polish matters"

**Skill (Interview):**
"Let's start with why this topic. Of all the skills you've built, why does prose-polish pull your attention?"

**User:** [Responds with real reasons]

**Skill (Thread):**
"Marking [MAIN]: collaborative emergence—AI as intellectual prosthesis.
Marking [TANGENT]: the real AI tell you've observed.
Marking [RESEARCH]: need examples of bad vs. good writing."

**Skill (Interview continues):**
"You said 'intellectual prosthesis.' What's the distinction for you between prosthesis and collaborator?"

**User:** [Responds]

**Skill (Draft):**
"The angle is clear: prose-polish exists for collaborative emergence, not just detection. Let me draft an opening that sounds like you thinking out loud..."

**Skill (Calibrate):**
"Running through prose-polish... flagging one phrase in paragraph 3 that sounds like the 'you might think' pattern. Here's an alternative that preserves the point in your voice..."

---

## Version

1.0.0 — MVP based on interview session 2025-12-18
