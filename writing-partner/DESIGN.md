# Writing Partner — Design Document

## Interview Findings (2025-12-18)

The following was extracted through structured interview with Lee.

### Why This System Exists

**The Problem:**
- Prose-polish essay was written BY Claude, not BY Lee
- It doesn't feel like his voice
- Contains fabrications presented as Lee's experience
- The essay about authentic voice lacks authentic voice (structural irony)

**Lee's Writing Philosophy:**
- Partner writing with AI
- Human provides: spark, taste, vision, wisdom
- AI provides: words, elevation, prosthetic extension
- Goal: collaborative emergence where essays emerge from conversation

### What Makes Writing "Lee's"

| Dimension | Signal |
|-----------|--------|
| Purpose | Explore ideas, tell stories, change minds, demonstrate expertise, sell positions, communicate emotions |
| Style | External processor, thinks out loud, monologue-to-clarity |
| Feel | Heartfelt writing where his mind shines through |
| Entry points | "I wonder about...", intersection exploration, exaptation across domains |

### The Real AI Tell

Lee's observed pattern (not Claude's invention):
> **"You might think Y... but actually X"** and all its derivatives

Also can't stand:
- Lack of writing perplexity
- Perfectly crafted sentences that are grammatically perfect but soulless
- Missing animating spirit

### How Lee Works

**Idea Generation:**
- Starts with "I wonder about..." or "go research this topic"
- Explores intersections of different thinkers (Wardley + Musashi)
- Exaptation of ideas across domains
- Curiosity-driven exploration

**Processing Style:**
- Deeply intuitive
- Loves digressions and side quests
- Subconscious processes in background, then "snaps into reality" later
- Those snaps signal novel/powerful insights
- Diverge then converge

**Voice Selection:**
- Already has reasoner roster (@strategist, @builder, etc.)
- Lets AI figure out which to invoke
- Enjoys surprise of which voice appears
- Rarely overrides, sometimes names specific thinkers

**Mode Switching:**
- Fluid, context-sensing
- No explicit commands
- Prompt guides the AI on approach

**Thread Management:**
- Write threads down
- Mark for later with marker
- Surface them as we go
- System should manage this, not his head

---

## System Architecture

### Three Integrated Capabilities

#### 1. Structured Interview

Extracts ideas through progressive questioning.

**Phases:**
- Opening questions (why this topic, core insight, what feels thin)
- Deepening questions (actual experience, real examples, ground truth)
- Process probes (how did you think about this, what's your entry point)
- Orientation probes (what would success look like)

**Outputs:**
- Raw material for drafting
- Voice calibration data
- Ground truth vs. fabrication distinction

**Key Principles:**
- Probe process, not just content
- Capture what's real vs. what's invented
- Progressive deepening

#### 2. Thread Tracker

Manages multiple parallel ideas across a session.

**Thread Types:**
- Main argument
- Tangent worth exploring
- Research needed
- Counterargument to address
- Subconscious connection (surfaced later)

**Operations:**
- Mark thread when it surfaces
- Park thread for later
- Surface thread at appropriate moment
- Connect threads (maybe automatically via graph)

**Persistence:**
- Within session: definitely
- Across sessions: connect to beads
- Graph structure: threads connect to each other, generating knowledge

**Key Principles:**
- Welcome digressions
- Don't force premature convergence
- Create space for "snap into reality" moments

#### 3. Voice Calibration

Ensures output sounds like Lee, not like AI.

**Components:**
- WritingSamples/ corpus as reference
- Prose-polish as detection layer
- Real-time or on-demand drift detection

**Operations:**
- Compare draft passages to reference corpus
- Flag patterns that don't match voice
- Suggest alternatives that do
- Pull few-shot examples dynamically

**Key Principles:**
- Use actual samples, not just guidelines
- Detection before remediation
- "Does this sound like you?" as core question

### Orchestration

**Mode:** Fluid, context-sensing (no explicit switches)
**Voice:** AI selects, human can override
**Flow:** Interview → Drafting → Polish → Publication

### Integration Points

- **Beads:** Threads can become issues, issues can spawn threads
- **Prose-polish:** Detection layer for voice calibration
- **WritingSamples/:** Reference corpus
- **VOICE.md:** Guidelines (complement to samples)

---

## MVP Specification

### Scope

A Claude Code skill that:
1. Can run structured interviews to extract ideas
2. Tracks threads explicitly with markers
3. Uses WritingSamples/ for voice comparison
4. Integrates with prose-polish for AI detection

### Out of Scope (for MVP)

- Cross-session thread persistence (future: beads integration)
- Automatic thread-to-graph generation
- Claude SDK agent architecture
- Full voice remediation (detection only for MVP)

### Invocation

Natural language triggers:
- "Let's work on an essay about [topic]"
- "Interview me about [topic]"
- "I want to write about [idea]"

Or explicit:
- `skill: writing-partner`

### Files

```
~/.claude/skills/writing-partner/
├── SKILL.md              # Main skill prompt
├── interview-protocol.md # Structured interview questions
└── thread-markers.md     # Thread tracking syntax
```

---

## Future Evolution

### Phase 2: Beads Integration
- Threads persist as beads issues
- Connections between threads tracked as dependencies
- Knowledge graph emerges from thread relationships

### Phase 3: Claude SDK Agent
- Dedicated agent with specialized tools
- Interview tool, thread tool, voice tool
- More sophisticated orchestration
- Multi-session memory

### Phase 4: Voice Learning
- Active learning from corrections
- Pattern extraction from new writing
- Dynamic profile evolution

---

## Test Cases

### Prose-Polish Essay Revision
Use this system to revise the Day 1 essay:
1. Interview Lee about why he built prose-polish
2. Track threads that emerge (real AI tells, collaborative emergence, intellectual prosthesis)
3. Calibrate voice against WritingSamples/
4. Replace fabrications with ground truth
5. Run through prose-polish to verify

### New Essay Creation
Test the full workflow on a new topic:
1. Start with "I wonder about..."
2. Interview to extract the angle
3. Track threads as they diverge
4. Converge into draft
5. Calibrate and polish
