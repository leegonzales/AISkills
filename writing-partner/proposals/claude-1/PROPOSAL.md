# Writing Partner Implementation Proposal
**Proposal ID:** claude-1
**Date:** 2025-12-18
**Stance:** Lightweight, prompt-first, state-in-conversation

---

## Executive Summary

This proposal advocates for a **minimal skill architecture** that leverages Claude Code's native conversation threading instead of external state management. The core insight: the conversation itself is the state. By designing prompts that maintain thread awareness and using conversation history as memory, we can build a fluid writing partner without the overhead of persistent storage or complex orchestration.

**Key Bets:**
1. Conversation history is sufficient state for single-session work
2. Prompt engineering > tool proliferation
3. Mode transitions via context-sensing, not explicit switches
4. Integration through skill composition, not direct coupling

---

## 1. Skill File Structure

### Directory Layout

```
~/.claude/skills/writing-partner/
├── SKILL.md                    # Main skill prompt (entry point)
├── modes/
│   ├── interview.md            # Interview protocol + questions
│   ├── thread-tracking.md      # Thread syntax + examples
│   ├── drafting.md             # Drafting guidelines + voice signals
│   └── calibration.md          # Voice checking + prose-polish integration
├── examples/
│   ├── interview-flow.md       # Full example session
│   └── thread-markers.md       # Thread tracking patterns
└── integrations/
    ├── prose-polish.md         # How to invoke prose-polish
    ├── writing-samples.md      # How to reference WritingSamples/
    └── beads.md                # Future: thread → bead conversion
```

### Rationale

**Single entry point (SKILL.md):** All mode documentation lives in separate files but is conceptually unified. Claude reads SKILL.md which references other files contextually.

**Mode files are prompts, not code:** Each mode is a rich prompt template that Claude internalizes. No state machines, no switch statements—just well-structured instructions.

**Examples drive behavior:** Concrete examples of interview flows and thread tracking teach better than abstract rules.

**Integration files document interfaces:** Each integration is a clear protocol for how to call other skills or reference resources.

---

## 2. Mode Switching: Context-Sensing via Prompt Structure

### Core Principle

**No explicit mode switches.** Instead, the main skill prompt includes:

1. Mode detection patterns (user intent signals)
2. Transition criteria (when to shift modes)
3. Blending instructions (modes can overlap)

### Implementation in SKILL.md

```markdown
## Mode Detection

You operate fluidly between four modes based on user intent:

**Interview Mode** — Activate when:
- User mentions new topic/essay
- Angle is unclear
- Need ground truth vs. hypothetical
- User asks "interview me" or "let's explore"

**Thread Tracking Mode** — Always active, but emphasize when:
- Multiple ideas surface in conversation
- User digresses (welcome this)
- Complexity is rising
- "Let me think about X" (mark as [SPARK])

**Drafting Mode** — Activate when:
- Angle is clear (test: can state thesis in one surprising sentence)
- Threads are mapped
- User says "let's write" or similar
- Energy shifts from exploration to execution

**Calibration Mode** — Activate when:
- Draft exists
- User asks "does this sound like me?"
- Before finalizing any section
- AI detection flags raised

**Mode Transitions:**
- Interview → Thread Tracking: Natural during conversation
- Interview → Drafting: Only when angle + material are sufficient
- Drafting → Calibration: After each major section
- Calibration → Drafting: After voice adjustments

**Multi-mode operation:**
Thread tracking runs alongside all other modes. Mark threads even during drafting.
```

### Why This Works

Claude Code maintains conversation context. By teaching Claude to recognize signals in the conversation flow, we get fluid transitions without state machines. The skill prompt itself encodes the "when to switch" logic.

---

## 3. State Management: Conversation as Database

### Strong Stance: Reject External State for MVP

**Do NOT build:**
- JSON state files
- Thread databases
- Session persistence to disk
- Custom memory layers

**Instead:**
The conversation history IS the state. Claude Code's context window (200K tokens) is more than sufficient for:
- Interview Q&A history
- Thread markers in conversation
- Draft iterations
- Voice calibration notes

### Thread Tracking in Conversation

Threads are marked inline during conversation using a simple syntax:

```
[MAIN: Core argument about collaborative emergence]
[TANGENT: Real AI tell observation ("you might think...")]
[RESEARCH: Need examples from WritingSamples/]
[COUNTER: What if fabrications are unavoidable?]
[SPARK: Connection to intellectual prosthesis concept]
```

These markers appear naturally in Claude's responses. When a thread is surfaced later:

```
"Earlier we marked [TANGENT: Real AI tell]. Want to develop that now?"
```

The conversation history maintains thread continuity. No database required.

### When Conversation State Breaks Down

**Problem:** Session ends, threads lost.

**Solution for MVP:** Don't solve this yet. Accept single-session scope.

**Future (Phase 2):** Integrate with beads. At session end:
1. Skill prompts: "Create bead issue for this essay?"
2. Threads become issue notes/subtasks
3. Next session: `beads:show ESSAY-1` loads context back

But for MVP, one-session constraint is fine. Most essays emerge in a single focused session anyway.

---

## 4. Integration Hooks

### Design Principle: Skills Compose, Don't Couple

Writing-partner should not directly invoke other skills. Instead, it provides clear prompts for WHEN and HOW to integrate.

### Integration 1: prose-polish

**File: integrations/prose-polish.md**

```markdown
## Prose-Polish Integration

### When to Invoke
- After drafting any substantial section (>300 words)
- Before finalizing the piece
- When user asks "does this sound like me?"

### How to Invoke
1. Invoke prose-polish skill with the draft text
2. Look for AI detection scores >25 (Lee's threshold)
3. Flag specific phrases/patterns identified
4. Suggest alternatives using WritingSamples/ voice

### Example Conversation Flow

**Writing Partner:** "I've drafted the opening section. Let me run it through prose-polish for AI detection..."

*[Invokes prose-polish skill]*

**Writing Partner:** "Prose-polish flagged paragraph 2, sentence 3: 'You might think AI writing is inevitable...' This matches the AI tell pattern you identified. Here's an alternative in your voice: 'Most people assume AI writing is inevitable. I'm not convinced.'"
```

**Key:** The integration is documented as a conversation pattern, not as a function call.

### Integration 2: WritingSamples/

**File: integrations/writing-samples.md**

```markdown
## WritingSamples/ Integration

### Purpose
Reference corpus for voice calibration. Use to:
- Check if phrasing matches Lee's style
- Pull few-shot examples for similar topics
- Ground voice guidelines in actual writing

### How to Reference

**During Calibration:**
1. Identify topic similarity (e.g., user writing about AI → look for AI-related samples)
2. Read relevant WritingSamples/ file
3. Compare:
   - Sentence rhythm (short vs. long)
   - Opening moves (does Lee start with questions? assertions?)
   - Transition patterns
   - Use of examples (concrete vs. abstract)

**During Drafting:**
Pull few-shot examples:
"Looking at how you wrote about [similar topic] in WritingSamples/[file].md, I'll match that energy here."

### Voice Signals to Extract
- Sentence-level patterns
- Paragraph structures
- Transitions between ideas
- Use of questions vs. statements
- Concrete:abstract ratio
```

**Implementation:** The skill uses Read tool to fetch samples dynamically. No caching, no indexes—just direct file reads when needed.

### Integration 3: Beads (Future)

**File: integrations/beads.md**

```markdown
## Beads Integration (Phase 2)

### Thread → Issue Conversion

At session end, offer:
"Create bead issue to persist these threads?"

**If yes:**
1. `beads:create` with:
   - Title: Essay title/topic
   - Description: Current angle + thesis
   - Notes: All marked threads
2. Thread markers become subtasks or dependencies

### Session Resume

Next session:
1. `beads:show ESSAY-{id}`
2. Load threads back into conversation
3. "We were working on [topic]. Here's where we left off: [threads]"

### Thread Graph (Phase 3)
- Use `beads:dep` to link related threads
- Knowledge graph emerges from thread connections
- Query: "Show me all threads related to 'collaborative emergence'"
```

**Status:** Documented but not implemented. Phase 2 work.

---

## 5. Prompt Engineering: Key Patterns

### Pattern 1: Progressive Interview (interview.md)

The interview protocol is structured in phases, each building on the last:

```markdown
## Interview Protocol

You are conducting a structured interview to extract authentic material.

### Phase 1: Opening (Why This, Why Now)
Ask all four questions before moving on:
1. Why this topic? What's pulling you here?
2. What's the core insight?
3. What feels thin or uncertain?
4. What's the entry point?

**Do not move to Phase 2 until you have specific answers to all four.**

### Phase 2: Deepening (Ground Truth)
Now push for real material:
5. What's your actual experience? (Not hypothetical)
6. What pattern have you observed that others miss?
...

**Do not move to Phase 3 until you can distinguish ground truth from fabrication.**

...
```

**Key technique:** Explicit blocking between phases. "Do not move on until X" creates natural pacing.

### Pattern 2: Thread Awareness (thread-tracking.md)

```markdown
## Thread Tracking Syntax

Mark threads as they surface:
- Inline during conversation
- Brief description (1 sentence max)
- Type indicator

**Format:**
[TYPE: Brief description]

**Types:**
- MAIN: Core argument
- TANGENT: Interesting but not central
- RESEARCH: Needs evidence
- COUNTER: Counterargument
- SPARK: Subconscious connection

**Examples in conversation:**

User: "I think the real issue is that AI writing lacks perplexity..."

You: "Marking [MAIN: Writing perplexity as authenticity signal]. This feels central to your argument."

User: "Yeah, and it connects to that thing we talked about earlier with collaborative emergence..."

You: "Marking [SPARK: Perplexity ↔ collaborative emergence connection]. Not sure how yet, but noting it."
```

**Threading during interview:**
- Mark threads as they emerge
- Don't interrupt flow to explain threads
- Surface threads naturally when relevant
- Multiple threads can be active simultaneously

### Pattern 3: Voice Calibration (calibration.md)

```markdown
## Voice Calibration Protocol

When checking draft against Lee's voice:

### Step 1: Read Reference Sample
Pull a WritingSamples/ file on similar topic:
- Read entire file
- Note sentence rhythm, opening moves, transitions
- Extract 2-3 exemplar paragraphs

### Step 2: Compare Patterns
Check draft against these dimensions:
- **Sentence rhythm:** Does Lee use short punchy sentences or longer flowing ones here?
- **Opening moves:** Question? Bold assertion? Story?
- **Transition style:** Explicit ("Now let's...") or implicit (topic shift)?
- **Example use:** Concrete specifics or abstract concepts?
- **Voice of authority:** Confident assertion or exploratory wondering?

### Step 3: Flag Mismatches
Mark any passage where:
- Rhythm feels off (too uniform, too AI-smooth)
- Transitions feel mechanical
- Examples are generic instead of specific
- AI tell patterns appear ("You might think...")

### Step 4: Suggest Alternatives
For each flagged passage:
1. Quote the original
2. Explain the mismatch
3. Offer rewrite in Lee's voice
4. Point to similar passage in WritingSamples/ as evidence

### Step 5: Invoke Prose-Polish (Optional)
For final check:
- Run through prose-polish skill
- Look for scores >25
- Cross-reference with voice analysis
```

**Key insight:** Voice calibration is comparative. Always ground in actual samples, never just abstract guidelines.

### Pattern 4: Drafting with Voice Awareness (drafting.md)

```markdown
## Drafting Protocol

You are drafting collaboratively with Lee.

### Division of Labor
- **Lee provides:** Spark, taste, vision, wisdom, real experience
- **You provide:** Words, elevation, structure, prosthetic extension
- **Shared:** Iterative refinement

### Before Drafting: Checklist
- [ ] Angle is clear (can state thesis in one surprising sentence)
- [ ] Ground truth vs. fabrication is distinguished
- [ ] Threads are mapped (know what's MAIN vs. TANGENT)
- [ ] Have reference WritingSamples/ file loaded (if available)

### During Drafting: Voice Signals

**Preserve these:**
- External processing style (thinking out loud)
- Intersection/exaptation moves (Wardley + Musashi)
- Heartfelt directness
- "You want X, right?" confirmation style
- Contrarian positioning with evidence
- Concrete examples over abstractions

**Avoid these:**
- "You might think X... but actually Y" (Lee's identified AI tell)
- Grammatically perfect but soulless sentences
- Generic platitudes
- Excessive hedging ("perhaps", "might", "could potentially")
- Throat-clearing openings ("In today's world...")
- Corporate buzzwords

### Drafting Flow
1. **Opening paragraph:** Match Lee's typical opening move (question? assertion? story?)
2. **Development:** Follow thread order (MAIN first, TANGENT if relevant, COUNTER to address)
3. **Rhythm check:** Every 2-3 paragraphs, pause and compare to WritingSamples/ rhythm
4. **Calibration pause:** After ~300 words, ask: "Want me to check voice before continuing?"

### When Stuck
- Return to interview material
- Surface a parked thread
- Ask Lee for the next move
- Don't fabricate—ask for real material
```

**Anti-pattern:** Don't draft generically then "add voice." Voice must be present from first sentence.

---

## 6. Trade-offs and Design Decisions

### What We're Prioritizing

#### 1. Single-Session Fluidity Over Multi-Session Persistence

**Rationale:** Most essays emerge in one focused session. By optimizing for single-session work, we get a cleaner architecture without state management overhead. Beads integration can solve cross-session persistence in Phase 2.

**Trade-off:** Users cannot pause mid-essay and resume days later without losing thread context. Acceptable for MVP.

#### 2. Prompt Engineering Over Tool Building

**Rationale:** Claude Code's conversation threading + rich prompts can achieve fluid mode transitions without building custom state machines or orchestration layers. This keeps the skill lightweight and maintainable.

**Trade-off:** Less explicit control over mode transitions. Relies on Claude's ability to interpret context signals. Early testing required to validate this bet.

#### 3. Conversation Markers Over Structured Data

**Rationale:** Thread markers like `[MAIN: description]` are human-readable and naturally integrated into conversation flow. No need for JSON schemas or databases.

**Trade-off:** Thread markers are less queryable. Can't easily ask "show me all TANGENT threads" without parsing conversation history. Acceptable until we need graph queries (Phase 3).

#### 4. Composition Over Coupling

**Rationale:** Writing-partner documents HOW to integrate with prose-polish and WritingSamples/ rather than directly invoking them. This creates clean boundaries and allows each skill to evolve independently.

**Trade-off:** More manual orchestration required. User or Claude must explicitly invoke other skills. But this preserves modularity and prevents tight coupling.

#### 5. Detection Before Remediation (Voice Calibration)

**Rationale:** For MVP, focus on detecting voice drift via WritingSamples/ comparison and prose-polish. Automated remediation (rewriting to match voice) is deferred to Phase 2.

**Trade-off:** More human-in-the-loop required during calibration. But this ensures quality and prevents the skill from confidently rewriting in the wrong direction.

### What We're Deferring

#### Deferred to Phase 2: Beads Integration
**Why:** Requires beads skill to be stable and widely used. Thread → issue conversion is valuable but not critical for single-session MVP.

**Unlock:** Once beads is stable, add integrations/beads.md implementation. Minimal changes to core skill.

#### Deferred to Phase 2: Cross-Session Thread Persistence
**Why:** Adds architectural complexity (state files, session IDs, merge logic) without clear MVP value.

**Unlock:** Beads integration naturally solves this.

#### Deferred to Phase 3: Thread Graph Queries
**Why:** Requires structured thread storage and graph traversal logic. High complexity for uncertain value.

**Unlock:** Once we have data on thread relationships (from beads), evaluate if graph queries actually help.

#### Deferred to Phase 3: Automated Voice Remediation
**Why:** Rewriting passages to match voice is high-risk (could make things worse). Detection + human edit is safer for MVP.

**Unlock:** After collecting calibration data, train on what Lee accepts/rejects, then explore automated suggestions.

#### Deferred to Future: Claude SDK Agent Architecture
**Why:** Skill architecture is simpler and sufficient for MVP. SDK agent adds overhead (tools, state, deployment) without clear benefits yet.

**Unlock:** Migrate to SDK agent when we need:
- Custom tools (e.g., graph query tool)
- More sophisticated orchestration
- Multi-session state management
- Better debugging/introspection

---

## 7. Implementation Roadmap

### Phase 1: MVP (This Proposal)

**Goal:** Single-session writing partner with interview, thread tracking, drafting, and voice calibration.

**Deliverables:**
1. Skill file structure (SKILL.md + modes/ + examples/ + integrations/)
2. Interview protocol with progressive phases
3. Thread tracking syntax and examples
4. Drafting guidelines with voice signals
5. Calibration protocol using WritingSamples/
6. Integration docs for prose-polish

**Success Metrics:**
- Can conduct structured interview from scratch
- Threads marked and surfaced appropriately
- Voice calibration catches AI tells
- Draft feels like "Lee thinking out loud"

**Timeline:** 1-2 focused sessions to build, 3-5 test essays to refine

### Phase 2: Persistence (Beads Integration)

**Goal:** Enable cross-session thread continuity.

**Deliverables:**
1. Thread → bead conversion at session end
2. Session resume from bead issue
3. Thread markers in bead notes/subtasks

**Dependencies:**
- Beads skill stable and used regularly
- Phase 1 validated with multiple essays

### Phase 3: Graph Queries (Thread Intelligence)

**Goal:** Surface thread relationships and patterns.

**Deliverables:**
1. Thread dependency tracking (Thread A → Thread B)
2. Graph queries ("show threads related to X")
3. Pattern detection (recurring themes across essays)

**Dependencies:**
- Phase 2 complete (threads in beads)
- Sufficient data on thread relationships

### Phase 4: Voice Learning (Adaptive Calibration)

**Goal:** Learn from corrections, improve voice matching over time.

**Deliverables:**
1. Track what Lee accepts/rejects during calibration
2. Extract patterns from new writing
3. Dynamically update voice profile
4. Automated remediation suggestions

**Dependencies:**
- Phase 1 calibration data collected
- Pattern extraction methodology validated

---

## 8. Concrete Next Steps

### Immediate: Build MVP Skill

1. **Create directory structure:**
   ```bash
   mkdir -p ~/.claude/skills/writing-partner/{modes,examples,integrations}
   ```

2. **Write SKILL.md** (main entry point):
   - Activation triggers
   - Mode detection logic
   - Core principles
   - Example flow

3. **Write modes/interview.md:**
   - Copy from prompts/interview-protocol.md
   - Add explicit phase blocking
   - Add thread marking during interview

4. **Write modes/thread-tracking.md:**
   - Thread syntax definition
   - Examples in conversation
   - Surfacing patterns

5. **Write modes/drafting.md:**
   - Voice signals (preserve/avoid)
   - Drafting flow
   - Anti-patterns

6. **Write modes/calibration.md:**
   - Comparison protocol
   - WritingSamples/ integration
   - Flag → suggest → validate flow

7. **Write examples/interview-flow.md:**
   - Full example session from "I want to write about X" to first draft
   - Show thread marking in action
   - Demonstrate mode transitions

8. **Write integrations/prose-polish.md:**
   - When to invoke
   - How to interpret results
   - Conversation flow example

9. **Write integrations/writing-samples.md:**
   - How to select relevant samples
   - What to extract (rhythm, patterns, moves)
   - Comparison methodology

10. **Test with prose-polish essay revision:**
    - Use the skill to re-interview Lee about prose-polish
    - Track threads
    - Draft revision
    - Calibrate against WritingSamples/
    - Document what worked / what broke

### Week 2: Refinement

1. **Test with new essay:**
   - Pick a fresh topic
   - Full workflow (interview → draft → calibrate)
   - Collect friction points

2. **Iterate on prompts:**
   - Where did mode detection fail?
   - Where did thread tracking get messy?
   - Where did voice calibration miss?

3. **Add more examples:**
   - Document successful sessions
   - Build example library in examples/

### Month 2: Phase 2 Planning

1. **Evaluate beads stability:**
   - Is beads used regularly?
   - Is the issue/dependency model stable?

2. **Design thread → bead conversion:**
   - What thread metadata is needed?
   - How to represent thread relationships?

3. **Prototype session resume:**
   - Load bead issue
   - Reconstruct thread markers
   - Continue conversation

---

## 9. Open Questions and Risks

### Open Questions

**Q1: Will conversation-as-state scale to complex essays?**
- Risk: Long interviews + multiple tangents could exceed context window
- Mitigation: Test with longest expected essay (5000+ words)
- Fallback: Implement thread summarization if needed

**Q2: How reliably can Claude detect mode transitions?**
- Risk: Context-sensing might miss signals, wrong mode activated
- Mitigation: Make transition criteria very explicit in prompts
- Fallback: Add optional explicit mode commands (`/interview`, `/draft`) if fluid detection fails

**Q3: Is WritingSamples/ comparison sufficient for voice calibration?**
- Risk: Samples might not cover all essay types or topics
- Mitigation: Test across diverse topics
- Fallback: Add VOICE.md guidelines as secondary reference

**Q4: Will thread markers feel natural in conversation?**
- Risk: Could feel mechanical or interrupt flow
- Mitigation: Test with Lee's actual workflow preferences
- Fallback: Make thread marking optional/toggleable

### Risks

**R1: Prompt drift over time**
- As skill files grow, might lose coherence
- Mitigation: Regular refactoring, keep prompts crisp
- Backup plan: Version skill files, roll back if needed

**R2: Integration brittleness**
- Changes to prose-polish or WritingSamples/ structure could break skill
- Mitigation: Document integration contracts clearly
- Backup plan: Graceful degradation (skill works without integrations)

**R3: Voice calibration false positives**
- Might flag passages that actually match Lee's voice
- Mitigation: Compare to multiple samples, look for patterns not single signals
- Backup plan: User always has override, calibration is suggestive not prescriptive

**R4: Thread explosion**
- Too many threads marked, becomes noise instead of signal
- Mitigation: Be selective about what gets marked, merge similar threads
- Backup plan: Add thread archiving/pruning

---

## 10. Conclusion

This proposal takes a strong stance: **conversation is state, prompts are architecture.**

By rejecting external state management and tool proliferation, we can build a lightweight, fluid writing partner that feels natural in conversation. The skill acts as a richly-prompted guide, not a state machine or orchestrator.

Key bets:
1. Claude Code's context window is sufficient for single-session work
2. Well-structured prompts enable fluid mode transitions
3. Conversation markers (thread syntax) are better than structured data for MVP
4. Skills compose better when loosely coupled
5. Detection-first is safer than automated remediation

This architecture is optimized for speed to MVP and ease of iteration. When we hit its limits (cross-session persistence, graph queries), we have clear Phase 2/3 paths.

The true test: Can Lee use this to revise the prose-polish essay and have it sound like him? If yes, we've built something valuable. If no, the prompts need refinement—not the architecture.

---

**Proposal Status:** Ready for implementation
**Next Action:** Build skill files, test with prose-polish essay revision
**Feedback Loop:** Document what works, what breaks, iterate on prompts