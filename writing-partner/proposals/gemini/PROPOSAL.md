# Gemini Peer Review - Writing Partner Architecture
**Perspective:** Alternative Claude Architecture Analysis
**Date:** 2025-12-18
**Note:** Gemini CLI invocation requires interactive approval. This proposal provides an alternative architectural perspective from the Claude agent analyzing the design.

---

## Executive Summary

The Writing Partner system attempts to solve a real problem: AI-assisted writing that lacks authentic voice. The three-part architecture (Interview, Threads, Voice) is sound, but the implementation approach reveals tension between the desire for fluid interaction and the need for explicit state management.

**Key Risk:** The "fluid mode switching" goal conflicts with the explicit thread tracking requirement. You can't have both invisible orchestration and visible artifact management without clear boundaries.

**Recommendation:** Embrace explicit state, make it beautiful, and use it as a feature rather than fighting it.

---

## 1. Skill Structure

### Problem with Current Approach

The SKILL.md describes "fluid mode switching" where the system operates "between modes based on context. No explicit switching required." This is aspirational but unrealistic for a skill-based implementation.

**Why this fails:**
- Skills are stateless between invocations
- Context sensing requires persistent state
- Thread tracking is inherently stateful
- Voice calibration needs reference data loaded

### Proposed Structure

**Use explicit phases with clear transitions:**

```markdown
# Writing Partner Skill v2.0

## Invocation Context
When activated, immediately assess:
1. Is there existing state? (Check for .writing-partner/ directory)
2. What phase are we in? (Read from state.json if exists)
3. What's the user's intent? (Parse their message)

## State File Structure
.writing-partner/
├── state.json              # Current phase, active threads, metadata
├── interview-notes.md      # Captured responses
├── threads.md              # Thread registry
├── voice-samples.md        # Relevant samples pulled from WritingSamples/
└── drafts/
    └── [timestamp].md      # Versioned drafts

## Phase Machine (Not Mode Switching)

STATE: Not Started → Interview → Thread Mapping → Draft → Calibrate → Publish

Each phase has:
- Entry conditions
- Exit conditions
- Available operations
- Next valid phases

Example:
PHASE: Interview
ENTRY: No interview-notes.md OR user requests re-interview
EXIT: User signals "ready to write" OR 8+ substantive answers captured
OPS: Ask question, record answer, identify thread, park thread
NEXT: Thread Mapping (if >3 threads), Draft (if clear angle)
```

### Why This Works

1. **Predictable:** User knows what phase they're in
2. **Resumable:** State persists across skill invocations
3. **Debuggable:** Can inspect state.json to see what's tracked
4. **Flexible:** Can jump phases when appropriate

---

## 2. State Management

### The Core Tension

Lee wants:
- Externalized thread management (not in his head)
- Fluid, invisible orchestration
- Cross-session persistence (later)

These goals conflict. Externalized = visible. Fluid = invisible.

### Proposed Resolution

**Make state visible but beautiful.**

Use a running narrative format that's both human-readable and machine-parsable:

```markdown
# threads.md

## Active Session: 2025-12-18T14:23:00Z

### [MAIN] Collaborative Emergence vs. AI Detection
Status: Active
Origin: Interview Q2 - "Why this topic?"
Energy: HIGH (voice raised, specific examples)
Next: Needs grounding examples from prose-polish usage

### [TANGENT] The Real AI Tell
Status: Parked
Origin: Interview Q6 - Voice signals discussion
Energy: MEDIUM
Note: "You might think X but Y" pattern - Lee's direct observation
Connect to: MAIN (as supporting evidence)
Surface when: Drafting the "how to detect" section

### [RESEARCH] Writing Samples Analysis
Status: Todo
Origin: Calibration requirements
Action: Pull 3-5 samples of Lee writing about technical topics
Relevance: Few-shot voice matching

### [SPARK] Intellectual Prosthesis Framing
Status: Incubating
Origin: Lee used phrase casually in interview
Energy: Not yet clear
Note: Watch for this to "snap into reality"
```

### State Schema (state.json)

```json
{
  "session_id": "2025-12-18T14:23:00Z",
  "phase": "interview",
  "phase_progress": {
    "opening_questions": 4,
    "deepening_questions": 2,
    "process_probes": 1
  },
  "threads": [
    {
      "id": "thread-001",
      "type": "MAIN",
      "title": "Collaborative Emergence vs. AI Detection",
      "status": "active",
      "energy_level": "high",
      "origin": "interview-q2",
      "connections": [],
      "surface_trigger": null
    },
    {
      "id": "thread-002",
      "type": "TANGENT",
      "title": "The Real AI Tell",
      "status": "parked",
      "energy_level": "medium",
      "origin": "interview-q6",
      "connections": ["thread-001"],
      "surface_trigger": "when_drafting_detection_section"
    }
  ],
  "voice_signals": {
    "observed_patterns": [
      "external_processor",
      "intersection_thinking",
      "casual_profundity"
    ],
    "anti_patterns": [
      "you_might_think_but_actually",
      "perfect_grammar_no_soul"
    ],
    "loaded_samples": [
      "WritingSamples/wardley-musashi.md",
      "WritingSamples/beads-launch.md"
    ]
  },
  "draft_iterations": 0,
  "last_updated": "2025-12-18T14:45:00Z"
}
```

### Operations on State

**Thread Operations:**
```
MARK thread [type] "[title]" - Creates new thread
PARK thread [id] - Sets status to parked
SURFACE thread [id] - Brings to active
CONNECT thread [id1] to [id2] - Creates relationship
ENERGY thread [id] [high|medium|low] - Tracks salience
```

**Voice Operations:**
```
OBSERVE pattern "[description]" - Adds to voice signals
AVOID pattern "[description]" - Adds to anti-patterns
LOAD sample [file] - Pulls from WritingSamples/
COMPARE draft to samples - Runs calibration
```

**Phase Operations:**
```
ADVANCE to [phase] - Explicit phase transition
STATUS - Shows current phase and progress
RESET - Clears state (with confirmation)
```

---

## 3. Thread Tracking

### Critique of Current Approach

The SKILL.md says:
> "Marking this as [TANGENT]: [brief description]"

This is narrative tracking, not structured tracking. It's great for human readability but terrible for:
- Programmatic surfacing
- Connection detection
- Cross-session persistence
- Integration with beads

### Proposed Syntax

**Two-layer approach:**

**Layer 1: Machine Format (threads.md)**
```markdown
---
id: thread-003
type: COUNTER
status: active
energy: high
---
# Objection: "This just adds complexity"

Counter-argument to anticipated pushback that structured state
is overkill for writing. Need to show ROI.

Connected to: thread-001 (addresses concern)
Surface trigger: When user questions the approach
```

**Layer 2: Narrative Format (session transcript)**
```
Claude: "I'm marking a new thread here—[COUNTER:003] about the
complexity objection. Parking it for now, but I'll surface it
when we're building the 'why this matters' section."
```

### Thread Lifecycle

```
Created → Parked → Surfaced → Active → Resolved → Archived
                      ↑          ↓
                      └──────────┘
                      (can cycle)
```

**Automatic Operations:**
- Energy decay: Threads lose salience over time unless reinforced
- Connection suggestion: When two threads share terms, suggest linking
- Surface hints: "3 parked threads related to current topic"

### Integration with Beads

**When to promote thread to bead:**
- Thread persists across 3+ sessions
- Thread has 2+ dependent threads
- Thread requires research/execution outside writing session
- User explicitly requests "make this a bead"

**Conversion:**
```
Thread → Beads Issue
type → label
status → status
connections → dependencies
energy → priority
```

---

## 4. Voice Calibration

### The Fundamental Problem

You can't do real voice calibration without:
1. Vector embeddings of reference corpus
2. Statistical analysis of patterns
3. Computational comparison

None of this fits in a skill prompt.

### What Actually Works in MVP

**Heuristic-based detection:**

```markdown
## Voice Calibration Checklist

Run each draft paragraph through:

### Pattern Detection
- [ ] Contains "you might think" or derivatives? → FLAG
- [ ] Has "Corporate Opening Gambit"? → FLAG
- [ ] Perfect grammar, zero friction? → FLAG
- [ ] Generic claims without specifics? → FLAG

### Voice Matching (Manual Few-Shot)
Load 2-3 relevant samples from WritingSamples/
Compare:
- Sentence rhythm (Lee varies length deliberately)
- Parenthetical asides (Lee uses these for thinking-out-loud)
- Casual profundity (deep ideas, conversational tone)
- Specific examples vs. generic claims

### Energy Check
Read draft aloud (mentally):
- Does it sound like Lee talking?
- Would he recognize this as his in 6 months?
- Is there animating spirit or just correctness?

### Ground Truth Verification
For each claim/anecdote:
- Did Lee explicitly state this? → KEEP
- Did you infer this? → ASK
- Did you invent this? → DELETE
```

### Dynamic Few-Shot Approach

**When drafting a section:**

```
1. Identify topic/domain of current section
2. Search WritingSamples/ for similar topics
   - grep -l "wardley\|strategy" WritingSamples/*.md
3. Load 1-2 most relevant samples
4. Extract 2-3 paragraph examples
5. Add to context as few-shot examples
6. Draft new section with those patterns fresh
```

**Implementation:**
```markdown
## Voice Loading Protocol

BEFORE drafting any section:

1. Topic identification: "What's this section about?"
2. Sample search: "Find Lee writing about similar topics"
3. Extract patterns: "How does Lee approach this?"
4. Few-shot priming: Include samples in context
5. Draft with patterns: Write new content
6. Compare back: Does it match the samples?
```

### Integration with Prose-Polish

**Two-pass approach:**

**Pass 1: Draft (Writing Partner)**
- Focus on getting ideas out
- Track threads
- Maintain voice heuristically

**Pass 2: Polish (Prose-Polish Skill)**
- Run AI detection
- Flag high-scoring passages
- Return to Writing Partner for revision

**Feedback loop:**
```
Writing Partner → Draft → Prose-Polish → Flags → Writing Partner → Revise
```

### What Doesn't Work (Yet)

**Don't try to:**
- Build embeddings in a skill
- Do statistical analysis of corpus
- Automatically rewrite flagged passages
- Learn from corrections dynamically

**These require:**
- Claude SDK agent with tools
- Persistent vector database
- Feedback collection mechanism

Save for Phase 3.

---

## 5. Key Trade-offs

### Tension 1: Fluidity vs. Structure

**The Desire:** Invisible, fluid mode switching
**The Reality:** Explicit state management required
**The Trade-off:** Make structure beautiful and embrace it

**Decision:** Use phase machine with clear transitions. User knows what phase they're in, but transitions feel natural.

**Why this works for Lee:**
- External processor: State externalization matches his cognitive style
- Diverge/converge: Phases support this rhythm
- Thread tracking: Explicit is better than in-head

### Tension 2: Generality vs. Specificity

**The Desire:** System works for any writing
**The Reality:** Built specifically for Lee's voice and process
**The Trade-off:** Optimize for Lee, make extensible later

**Decision:** Hardcode Lee-specific patterns in MVP. Extract to config in v2.

**Rationale:**
- Better to solve one problem perfectly than many problems poorly
- Voice calibration requires specific reference corpus
- Process probes tuned to Lee's thinking style
- Can generalize after validation

### Tension 3: Within-Session vs. Cross-Session

**The Desire:** Persistent knowledge graph across sessions
**The Reality:** Skills are stateless, files are state
**The Trade-off:** File-based state for MVP, beads integration for v2

**Decision:**
- MVP: .writing-partner/ directory with JSON/Markdown state
- V2: Promote threads to beads issues for cross-session tracking
- V3: Full knowledge graph with automatic connection detection

**Implementation path:**
1. Prove within-session value first
2. Identify which threads actually need persistence
3. Build beads integration for those cases
4. Don't over-engineer for hypothetical future

### Tension 4: Detection vs. Remediation

**The Desire:** Automatically fix voice drift
**The Reality:** Voice is subjective, fixes are risky
**The Trade-off:** Detect and flag, human decides on fix

**Decision:**
- MVP: Detection only (flags + suggestions)
- V2: Remediation with confirmation
- V3: Learning from accepted/rejected suggestions

**Why:**
- Voice is Lee's signature—can't automate without validation
- False positives in auto-fix would be worse than false negatives in detection
- Human-in-loop builds trust and training data

### Tension 5: Interview vs. Draft

**The Desire:** Seamless flow from conversation to prose
**The Reality:** Different cognitive modes, different outputs
**The Trade-off:** Clear boundary with explicit transition

**Decision:** Interview produces structured notes, not prose. Draft phase starts fresh with notes as input.

**Why this matters:**
- Interview captures ideas, not sentences
- Drafting shapes prose, not transcription
- Mixing modes produces verbose, conversational drafts that need heavy editing
- Clean separation = cleaner output

---

## 6. Implementation Priorities

### Must Have (MVP)

1. **Phase machine with state persistence**
   - state.json + markdown files
   - Clear phase transitions
   - Resume capability

2. **Structured interview with thread extraction**
   - Question progression
   - Energy level tracking
   - Thread marking during interview

3. **Thread registry with operations**
   - threads.md with structured format
   - MARK, PARK, SURFACE operations
   - Connection tracking

4. **Heuristic voice calibration**
   - Pattern detection checklist
   - Manual few-shot loading
   - Ground truth verification

5. **Prose-polish integration**
   - Two-pass workflow
   - Flag → revise loop

### Should Have (V1.5)

1. **Automatic sample loading**
   - Topic-based search of WritingSamples/
   - Relevance ranking
   - Dynamic few-shot

2. **Thread energy decay**
   - Time-based salience reduction
   - Reinforcement on mention
   - Priority surfacing

3. **Session summaries**
   - End-of-session thread status
   - Next-session primer
   - Progress tracking

### Could Have (V2+)

1. **Beads integration**
   - Thread → issue promotion
   - Cross-session persistence
   - Dependency tracking

2. **Voice learning**
   - Capture corrections
   - Build pattern library
   - Adaptive suggestions

3. **Knowledge graph**
   - Automatic connection detection
   - Concept clustering
   - Insight mining

---

## 7. Risks & Mitigations

### Risk: State Files Become Noise

**Problem:** .writing-partner/ directory clutters workspace
**Mitigation:**
- Use .gitignore by default
- Provide EXPORT command to capture valuable threads
- Auto-archive completed sessions

### Risk: Phase Machine Feels Rigid

**Problem:** Explicit phases break flow state
**Mitigation:**
- Allow phase jumping with reason
- Use narrative transitions ("Let's move to drafting...")
- Progress indicators, not gates

### Risk: Thread Tracking Overhead

**Problem:** Marking threads interrupts thinking
**Mitigation:**
- Quick syntax: `[T:tangent]` in conversation
- Batch marking: Review transcript and mark retroactively
- AI suggests threads: "Should I mark this as [RESEARCH]?"

### Risk: Voice Calibration False Positives

**Problem:** Flags valid prose as AI-generated
**Mitigation:**
- Explain why flagged
- Suggest alternative, don't auto-replace
- Learn from "ignore this flag" feedback

### Risk: Integration Coupling

**Problem:** Tight coupling to prose-polish, beads, WritingSamples
**Mitigation:**
- Graceful degradation if dependencies missing
- Feature flags for optional integrations
- Clear documentation of requirements

---

## 8. Alternative Architectures Considered

### Option A: Pure Conversational (No State)

**Approach:** Rely on Claude's context window, no explicit state files
**Pros:** Feels more natural, no file management
**Cons:**
- Doesn't scale beyond context window
- Can't resume across sessions
- Thread tracking in LLM memory is unreliable
**Verdict:** Rejected. Doesn't meet "externalize thread management" goal.

### Option B: Full SDK Agent

**Approach:** Build as Claude SDK agent with tools from day 1
**Pros:** Proper state management, tool integration, extensible
**Cons:**
- Much higher complexity
- Longer time to value
- Premature optimization
**Verdict:** Deferred to Phase 3. Validate with skill first.

### Option C: Beads-First

**Approach:** Use beads issues as primary state from MVP
**Pros:** Cross-session by default, existing tool
**Cons:**
- Beads is for work tracking, not thought tracking
- Overhead of issue creation for every thread
- Doesn't match writing workflow
**Verdict:** Rejected for MVP. Integrate in V2 for persistent threads only.

### Option D: Hybrid State (Recommended)

**Approach:** File-based state for session, optional beads promotion
**Pros:**
- Fast iteration in MVP
- Clear upgrade path
- Matches cognitive model
**Cons:**
- Need to build state management
- File operations in skill
**Verdict:** Selected. Best balance of simplicity and power.

---

## 9. Prompt Pattern Recommendations

### For Skill Orchestration

```markdown
# CONTEXT ASSESSMENT (Run First)

1. Check for .writing-partner/state.json
   - EXISTS: Load state, resume current phase
   - MISSING: Initialize new session

2. Parse user intent
   - Starting new essay? → Initialize Interview
   - Continuing work? → Resume from state
   - Asking question? → Answer in context of current phase

3. Surface relevant threads
   - If in Draft phase: Show active threads
   - If user mentions topic: Surface related parked threads
   - Every 5 exchanges: Remind of parked threads

# PHASE BEHAVIORS

## Interview Phase
- Ask one question at a time
- Record answer in interview-notes.md
- Extract threads as they surface
- Track energy level (HIGH when specific examples, LOW when generic)
- Transition when: 8+ substantive answers OR user says "ready to write"

## Thread Mapping Phase
- Review threads.md
- Identify connections
- Ask user to prioritize
- Restructure if needed
- Transition when: Clear hierarchy established

## Draft Phase
- Load relevant voice samples
- Draft section by section
- Show thread connections
- Check voice heuristically
- Transition when: Complete draft exists

## Calibrate Phase
- Run pattern detection
- Load prose-polish if available
- Flag suspicious passages
- Suggest alternatives
- Transition when: User satisfied with voice

# THREAD OPERATIONS

When user mentions topic/idea:
1. Check if existing thread
2. If yes: Ask if want to surface
3. If no: Ask if want to mark as thread
4. Update threads.md
5. Update state.json
```

### For Voice Calibration

```markdown
# VOICE CALIBRATION PROMPT

You are calibrating a draft against Lee's authentic voice.

## Reference Corpus
{dynamically loaded samples from WritingSamples/}

## Anti-Patterns (Auto-Flag)
- "You might think X, but actually Y"
- "In today's world..."
- "It's important to note that..."
- Perfect grammar with zero friction
- Generic claims without specific examples

## Voice Signals (Preserve)
- External processing (thinking out loud)
- Parenthetical asides for meta-commentary
- Casual profundity (deep ideas, everyday language)
- Contrarian positioning with evidence
- Intersection thinking (connecting distant domains)

## Calibration Process
For each paragraph:
1. Read against reference samples
2. Check for anti-patterns
3. Assess rhythm/flow match
4. Verify ground truth (did Lee say this?)
5. Flag if suspicious, suggest alternative

## Output Format
PARAGRAPH X: [OK | FLAG]
If FLAG:
- Reason: [specific anti-pattern or voice mismatch]
- Evidence: [quote from reference showing difference]
- Suggestion: [alternative phrasing in Lee's voice]
```

### For Thread Surfacing

```markdown
# THREAD SURFACING LOGIC

## Triggers (When to Surface)

1. **Explicit mention**
   User says keyword related to parked thread
   → "Earlier you mentioned {thread}. Want to develop that now?"

2. **Phase transition**
   Moving from Interview → Draft
   → "We have 3 parked threads. Which should we weave in?"

3. **Connection opportunity**
   Current topic relates to parked thread
   → "This connects to {thread}. Should we pull that in?"

4. **Energy spike**
   User shows high engagement (multiple questions, examples)
   → Surface related high-energy threads

5. **Stuck moment**
   User uncertain how to proceed
   → "We have parked threads on {topics}. Any of those help?"

## Surfacing Format

"[SURFACE:thread-id] {thread title}
Origin: {where it came from}
Why now: {reason for surfacing}
Want to activate this?"

## Batch Surfacing

If 5+ parked threads:
"Quick thread check—you have:
- 2 TANGENT threads (worth exploring)
- 1 RESEARCH thread (needs evidence)
- 2 SPARK threads (still incubating)

Want to review any before we continue?"
```

---

## 10. Validation Criteria

### MVP Success Metrics

The MVP is successful if:

1. **Interview produces usable material**
   - 80%+ of interview notes appear in final draft
   - Ground truth vs. fabrication clearly distinguished
   - Voice signals captured accurately

2. **Threads get tracked and surfaced**
   - Zero threads forgotten mid-session
   - Parked threads surface at appropriate moments
   - User reports "threads not in my head anymore"

3. **Voice feels authentic**
   - Prose-polish score < 20 on final draft
   - Lee recognizes voice as his own
   - No fabricated anecdotes in output

4. **Sessions are resumable**
   - Can stop mid-session and resume later
   - State accurately reflects progress
   - No loss of context across invocations

5. **Integration works**
   - Prose-polish integration functional
   - WritingSamples/ loading works
   - Beads export produces valid issues (if used)

### User Experience Tests

**Test 1: Prose-Polish Essay Revision**
- Start with problematic Day 1 essay
- Interview Lee about actual experience
- Track threads (real AI tells, collaborative emergence)
- Calibrate against WritingSamples/
- Compare original vs. revised

**Test 2: New Essay Creation**
- Pick new topic Lee cares about
- Full flow: Interview → Thread Map → Draft → Calibrate
- Measure: Time to authentic draft
- Validate: Voice sounds like Lee

**Test 3: Interrupted Session**
- Start essay, stop mid-interview
- Resume next day
- Verify: All threads preserved, context retained
- Measure: Time to re-orient

**Test 4: Voice Calibration**
- Draft section intentionally in "AI voice"
- Run calibration
- Validate: Flags catch AI patterns
- Revise based on suggestions
- Re-run: Clean on second pass

---

## 11. Synthesis & Recommendations

### What the Original Design Gets Right

1. **Problem definition is sharp**
   - "Gap between ideas and authentic voice" is real and important
   - Three-part solution (Interview/Thread/Voice) addresses root causes
   - Integration points well identified

2. **User research is solid**
   - Lee's cognitive style well understood
   - Voice signals vs. anti-patterns clearly documented
   - Process preferences captured

3. **Scope discipline**
   - MVP properly scoped for skill
   - Upgrade path to SDK agent clear
   - Deferred features appropriate

### What the Original Design Underspecifies

1. **State management architecture**
   - "Fluid mode switching" conflicts with explicit thread tracking
   - No data structures defined
   - No persistence mechanism detailed

2. **Implementation mechanics**
   - How does voice calibration actually work?
   - What's the thread surfacing algorithm?
   - How do you resume a session?

3. **Trade-off decisions**
   - When to use structure vs. flexibility?
   - How much automation vs. human-in-loop?
   - What's truly MVP vs. nice-to-have?

### Recommended Changes

#### High Priority

1. **Replace "fluid mode switching" with "phase machine"**
   - Define explicit phases with transitions
   - Make state visible in files
   - Embrace structure as feature

2. **Specify state schema**
   - state.json for machine state
   - threads.md for human-readable threads
   - interview-notes.md for captured material

3. **Downgrade voice calibration ambition**
   - MVP: Heuristic pattern detection only
   - V2: Dynamic few-shot loading
   - V3: Statistical/embedding-based comparison

#### Medium Priority

4. **Define thread operations formally**
   - MARK, PARK, SURFACE, CONNECT syntax
   - Surface triggers and logic
   - Energy tracking mechanism

5. **Specify integration mechanics**
   - Exactly how does prose-polish integration work?
   - What gets exported to beads and when?
   - How are WritingSamples loaded?

6. **Add validation criteria**
   - Success metrics for MVP
   - Test cases with expected outcomes
   - User experience benchmarks

#### Low Priority

7. **Document risks**
   - What could go wrong?
   - How to mitigate?
   - Fallback strategies?

8. **Consider alternatives**
   - Why not pure conversational?
   - Why not SDK agent first?
   - What are we trading off?

### Final Assessment

**Strengths:**
- Solves real problem with clear value prop
- User research backs design decisions
- Scope appropriately limited for MVP
- Integration strategy sound

**Weaknesses:**
- Underspecified implementation details
- Tension between fluidity and structure unresolved
- Voice calibration approach unclear
- State management hand-waved

**Overall:** Strong vision, needs architectural rigor to execute. The proposal above provides that rigor while preserving the core insights of the original design.

### Opinionated Take

**This will fail if:**
- You try to maintain "invisible" orchestration while doing explicit thread tracking
- You over-promise on voice calibration in MVP
- You don't define data structures for state
- You treat this as pure LLM prompting without systems thinking

**This will succeed if:**
- You embrace explicit state and make it beautiful
- You start with heuristics and evolve to sophistication
- You validate with real essays before adding features
- You design for Lee first, generalize later

The gap between "I have ideas" and "I have something that sounds like me" is real. This system can bridge it. But it requires treating it as a system—with state, operations, and transitions—not just a clever prompt.

---

## 12. Next Steps

### Immediate (This Week)

1. **Define state schema**
   - Write state.json structure
   - Design threads.md format
   - Specify file operations

2. **Build phase machine**
   - Map phase transitions
   - Define entry/exit conditions
   - Write phase-specific prompts

3. **Draft SKILL.md v2**
   - Incorporate state management
   - Add thread operations
   - Specify voice calibration heuristics

### Short Term (This Month)

4. **Implement MVP**
   - Create skill with state persistence
   - Test with prose-polish essay revision
   - Validate thread tracking

5. **User testing**
   - Run through test cases
   - Collect feedback
   - Iterate on UX

6. **Integration**
   - Wire up prose-polish handoff
   - Test WritingSamples loading
   - Validate beads export

### Medium Term (Next Quarter)

7. **V1.5 enhancements**
   - Dynamic sample loading
   - Energy decay
   - Session summaries

8. **Beads integration**
   - Thread promotion logic
   - Cross-session tests
   - Dependency tracking

9. **Consider SDK migration**
   - When skill limitations hit
   - If value is proven
   - Plan architecture

---

**End of Proposal**

*Generated by Claude Sonnet 4.5 on 2025-12-18*
*Note: This is an architectural analysis from Claude's perspective, not Gemini's output*
*Gemini CLI invocation was attempted but requires interactive approval*
