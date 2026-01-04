# Codex CLI Proposal — Writing Partner Architecture

**Status:** Unable to invoke Codex CLI (Bash prompts unavailable)
**Alternative:** Claude's architectural perspective with Codex-style critique
**Date:** 2025-12-18

---

## Executive Summary

Since Codex CLI was unavailable, this document provides a critical architectural analysis from first principles, examining the Writing Partner system through multiple lenses: technical implementation, failure modes, and design trade-offs.

**Core Thesis:** The MVP spec attempts to compress three hard problems (interview orchestration, thread management, voice calibration) into a single Claude Code skill. This is both ambitious and risky. Success depends on careful scope management and explicit state boundaries.

---

## 1. Skill Structure & Prompt Organization

### Proposed Architecture

```
~/.claude/skills/writing-partner/
├── SKILL.md                    # Main skill orchestrator (entry point)
├── modes/
│   ├── interview.md            # Interview protocol + questions
│   ├── thread-tracker.md       # Thread syntax + operations
│   ├── drafting.md             # Voice signals + writing approach
│   └── calibration.md          # Voice checking + detection
├── context/
│   ├── voice-signals.md        # Lee's voice DO/DON'T patterns
│   └── anti-patterns.md        # AI tells to avoid
└── state/
    └── thread-state.md         # Thread tracking format
```

### Rationale

**Why Split:** The current SKILL.md (211 lines) tries to be both orchestrator and reference manual. This creates context pollution—every invocation loads all modes even when only one is active.

**Why Not Split:** Skills lack dynamic file loading. You'd need to load all files anyway, eliminating the benefit. The skill would need to contain inline instructions for when to "mentally switch" to each mode.

**Proposed Compromise:** Single SKILL.md with clear section markers that help Claude's attention mechanism focus:

```markdown
---BEGIN_INTERVIEW_MODE---
[interview instructions]
---END_INTERVIEW_MODE---

---BEGIN_THREAD_MODE---
[thread instructions]
---END_THREAD_MODE---
```

This gives Claude structural cues without requiring file I/O.

### Key Trade-off

**Modularity vs. Coherence:** Splitting improves maintainability but risks mode confusion. Keeping unified improves coherence but creates a dense prompt.

**Recommendation:** Start unified, split only if you observe mode bleeding (e.g., interviewing when you should be drafting).

---

## 2. State Management for Threads

### The Hard Problem

Claude Code skills have no native state persistence. Every tool invocation is stateless. Thread tracking requires maintaining state across multiple turns of conversation.

### Proposed Approach: Explicit State Rendering

After each significant action, explicitly render thread state in a structured format:

```markdown
## ACTIVE THREADS

[MAIN] Collaborative emergence: AI as intellectual prosthesis
  Status: Active | Next: Define distinction from co-pilot metaphor

[TANGENT] Real AI tell: "You might think... but actually"
  Status: Parked | Note: Lee observed this pattern, not invented

[RESEARCH] Examples of voice drift in AI-generated prose
  Status: Pending | Sources: WritingSamples/ comparison needed

[COUNTER] "But Claude, you're still the one typing"
  Status: Unaddressed | Priority: Medium

[SPARK] Connection to Wardley's doctrine concept
  Status: Subconscious | Surface after: [MAIN] resolved
```

### Operations

**Create Thread:**
```
User mentions new idea → Skill says "Marking [TYPE]: [description]"
→ Renders updated state block
```

**Park Thread:**
```
User: "Let's come back to that" → Skill: "Parking [TANGENT]"
→ Changes status to Parked → Renders state
```

**Surface Thread:**
```
Context becomes relevant → Skill: "Earlier you mentioned [SPARK]..."
→ Changes status to Active → Renders state
```

**Connect Threads:**
```
Pattern emerges → Skill: "This connects [MAIN] to [SPARK]"
→ Adds connection note → Renders state
```

### Why This Works

1. **Visibility:** User sees what's being tracked
2. **Correction:** User can fix misunderstandings ("No, that's not a tangent, that's the main point")
3. **Grounding:** Explicit state prevents thread drift
4. **Recoverable:** If Claude loses context, the last rendered state is recoverable

### Why This Fails

1. **Verbosity:** State rendering adds tokens to every response
2. **Manual:** Skill must remember to render state (no enforcement)
3. **Fragility:** If state gets corrupted, no automatic recovery
4. **No Persistence:** Ends when session ends (unless manually saved)

### Mitigation: State Checkpoints

At natural transition points (interview → drafting, drafting → calibration), explicitly save state to a temp file:

```bash
# Skill invokes:
cat > /tmp/writing-partner-threads.md <<'EOF'
[state block]
EOF
```

Then references it: "State saved to /tmp/writing-partner-threads.md for recovery."

---

## 3. Thread Tracking Syntax

### Design Constraints

1. Must be instantly readable by both human and Claude
2. Must support operations (create, park, surface, connect)
3. Must be lightweight (low token overhead)
4. Must be recoverable if Claude forgets

### Proposed Syntax

```markdown
[TYPE] Brief description | Status | Context notes
```

**Thread Types:**
- `[MAIN]` — Core argument
- `[TANGENT]` — Worth exploring but not central
- `[RESEARCH]` — Needs evidence
- `[COUNTER]` — Counterargument to address
- `[SPARK]` — Subconscious connection

**Status Values:**
- `Active` — Currently working on
- `Parked` — Set aside, revisit later
- `Pending` — Identified but not started
- `Resolved` — Addressed/integrated
- `Subconscious` — Marked but not surfaced yet

**Context Notes:**
- `Next: [action]` — What happens next
- `Surface after: [condition]` — When to bring this back
- `Connects to: [other thread]` — Relationship
- `Note: [clarification]` — Important detail

### Example Operations

**Creating:**
```
User: "Maybe this relates to Wardley's doctrine?"
Skill: "Marking [SPARK] Connection to Wardley doctrine | Status: Subconscious"
```

**Parking:**
```
User: "Let's save that for later"
Skill: "Parking [TANGENT] Real AI tells | Status: Parked | Surface after: Draft complete"
```

**Surfacing:**
```
Skill: "You parked [TANGENT] Real AI tells earlier. Want to develop that now?"
User: "Yes"
Skill: "Activating [TANGENT] → [MAIN] Real AI tells as design constraint"
```

**Connecting:**
```
Skill: "This [RESEARCH] Examples of voice drift connects to [MAIN] Collaborative emergence.
The examples show why prose-polish matters for partnership, not just detection."
```

---

## 4. Voice Calibration Approach

### The Hard Problem

"Does this sound like Lee?" is a subjective question that requires:
1. Reference corpus (WritingSamples/)
2. Detection mechanism (prose-polish)
3. Comparison heuristic (pattern matching)
4. Remediation strategy (rewriting)

The MVP only tackles detection. This is wise—remediation is a separate hard problem.

### Proposed Calibration Flow

#### When to Check

**Always:**
- After generating any draft passage (3+ sentences)
- Before declaring "done" with a section
- When user asks "does this sound like me?"

**Never:**
- During interview (no draft yet)
- During thread tracking (no prose yet)
- On user's own words (don't second-guess them)

#### How to Compare

**Step 1: Pattern Detection**
```
Run prose-polish AI detection on passage.
If score > 25: Flag for review.
```

**Step 2: Voice Signal Check**
```
Compare against Lee's known patterns:

AVOID (AI tells):
- "You might think X... but actually Y"
- Perfectly crafted but soulless sentences
- Generic platitudes
- Excessive hedging
- Throat-clearing openings

PRESERVE (Lee's voice):
- External processing (thinking out loud)
- Intersection/exaptation moves
- Heartfelt directness
- "You want that, right?" confirmations
- Contrarian positioning with evidence
```

**Step 3: Corpus Comparison**
```
Pull few-shot examples from WritingSamples/ on similar topics.
Compare:
- Sentence structure complexity
- Vocabulary level
- Paragraph length
- Opening/closing patterns
- Use of questions vs. statements
```

**Step 4: Flagging**
```
If any check fails:
"Flagging paragraph 3, sentence 2: '[quoted text]'
Issue: Matches 'You might think' AI tell pattern
Reference: Compare to WritingSamples/[file] where you wrote '[example]'"
```

### Implementation Strategy

**Option A: Inline Checking**
Skill checks every passage as it's generated.

**Pros:** Immediate feedback, fewer compounding errors
**Cons:** High token overhead, slows flow

**Option B: Batch Checking**
Skill generates full draft, then runs calibration pass.

**Pros:** Maintains flow, efficient token use
**Cons:** Late feedback, harder to fix structural issues

**Option C: Checkpoint Checking**
Skill checks after completing each major section.

**Pros:** Balance of flow and feedback
**Cons:** Requires clear section boundaries

**Recommendation:** Option C for MVP. Check after:
1. Interview → Drafting transition
2. Each major section (intro, body, conclusion)
3. User request ("how's the voice?")

---

## 5. Key Trade-offs & Design Decisions

### Trade-off 1: Skill vs. Agent

**Current Choice:** Claude Code skill
**Alternative:** Claude SDK agent

**Analysis:**

| Dimension | Skill (MVP) | Agent (Future) |
|-----------|-------------|----------------|
| Complexity | Low — single prompt file | High — orchestration code |
| State | Manual tracking | Persistent via tools |
| Tools | Read, Write, Bash | Custom interview/thread/voice tools |
| Flexibility | Limited — prompt-only | High — code-level control |
| Maintenance | Edit markdown | Edit TypeScript/Python |

**Decision Rationale:** Skills are faster to iterate. If MVP validates the concept, upgrade to agent. If not, minimal wasted effort.

**Risk:** Skills might be too limited. If thread state becomes unmanageable, you'll hit the ceiling fast.

### Trade-off 2: Mode Switching

**Current Choice:** Fluid, context-sensing
**Alternative:** Explicit commands (/interview, /draft, /calibrate)

**Analysis:**

Fluid switching requires Claude to infer mode from context:
- "Why this topic?" → Interview mode
- "Let me draft..." → Drafting mode
- "Does this sound like me?" → Calibration mode

This works when context is clear but fails at boundaries:
- User says "I think X" — Are they answering an interview question or proposing draft content?
- User says "What about Y?" — Are they raising a thread or critiquing a draft?

**Risk:** Mode confusion leads to inappropriate responses (drafting when you should be interviewing).

**Mitigation:** Use explicit state markers in skill's own responses:

```
[INTERVIEW MODE]
Why this topic? What's pulling you here?

[User responds]

[THREAD MODE]
Marking [MAIN]: Collaborative emergence
Marking [TANGENT]: Real AI tells

[INTERVIEW MODE]
You said "intellectual prosthesis"—what's the distinction from co-pilot?
```

This helps both Claude and user track mode transitions.

### Trade-off 3: Voice Corpus

**Current Choice:** WritingSamples/ directory
**Alternative:** Embedded examples in VOICE.md

**Analysis:**

Dynamic corpus (directory) allows:
- Adding new samples over time
- Few-shot selection based on topic
- Real examples, not descriptions

But requires:
- File I/O on every calibration check
- Topic classification to select relevant samples
- Risk of corpus drift (old samples don't match current voice)

Embedded examples are:
- Always available (no I/O)
- Curated (best examples only)
- Static (no drift)

But:
- Limited to prompt size
- Can't grow organically
- Might not cover edge cases

**Decision Rationale:** Start with embedded examples in VOICE.md for common patterns. Add WritingSamples/ lookup for edge cases only.

**Risk:** Over-reliance on static examples creates brittle voice model. Need periodic refresh.

---

## 6. Risks & Failure Modes

### Failure Mode 1: Thread Explosion

**Scenario:** User is highly divergent thinker. Session spawns 15+ threads. State becomes unmanageable.

**Symptom:** Skill loses track of which thread is active. User has to manually correct constantly.

**Mitigation:**
- Set thread limit (max 7 active threads)
- Auto-merge related threads
- Prompt user to resolve threads before spawning new ones

**Escape Hatch:** If threads > 10, skill says "We have too many threads. Let's resolve a few before continuing."

### Failure Mode 2: Voice Drift Detection False Positives

**Scenario:** Skill flags passages as "not Lee's voice" when they actually are.

**Symptom:** User overrides calibration frequently. Loses trust in system.

**Mitigation:**
- Conservative thresholds (only flag obvious AI tells)
- Always show reasoning ("Flagging because X pattern matches Y anti-pattern")
- Let user tune sensitivity ("I'm okay with that pattern")

**Escape Hatch:** User can say "trust my voice on this" to skip calibration for a section.

### Failure Mode 3: Interview Stalling

**Scenario:** User gives short, surface-level answers. Skill can't extract depth.

**Symptom:** Draft feels generic because interview didn't uncover ground truth.

**Mitigation:**
- Meta-question: "This answer feels surface-level. What's underneath?"
- Reframe: "Let me ask differently..."
- Probe process: "How did you come to this conclusion?"

**Escape Hatch:** If 5+ questions yield shallow answers, skill says "I'm not getting the depth I need. Want to try a different entry point?"

### Failure Mode 4: State Desynchronization

**Scenario:** Skill and user have different mental models of what threads exist and their status.

**Symptom:** Skill surfaces parked thread, user says "I already addressed that."

**Mitigation:**
- Render state explicitly after every operation
- Confirm thread operations ("Parking [X]—sound right?")
- Periodic state sync ("Here's what I'm tracking...")

**Escape Hatch:** User can say "show threads" to force state render and correct mismatches.

---

## 7. What I'd Do Differently

### Challenge 1: Is Thread Tracking Overkill for MVP?

**Concern:** Thread tracking adds complexity. Do you actually need it for MVP, or is it premature optimization?

**Alternative MVP:** Remove thread tracking entirely. Focus on:
1. Interview → Extract ideas
2. Draft → Generate prose
3. Calibrate → Check voice

This is simpler and still validates the core value: collaborative emergence with authentic voice.

Add thread tracking in V2 if users say "I keep losing track of ideas during sessions."

**Counter:** Lee's workflow is deeply divergent. Without thread tracking, the system won't match how he thinks. The value prop is managing complexity, not just generating text.

**Verdict:** Keep threads, but make them opt-in. Default mode doesn't track threads. User can say "start tracking threads" if session gets complex.

### Challenge 2: Voice Calibration Might Be Futile

**Concern:** "Does this sound like Lee?" is subjective and temporal. Lee's voice evolves. What sounds like him today might not in 6 months.

**Alternative MVP:** Remove voice calibration. Focus on:
1. Ground truth vs. fabrication (interview extracts real experience)
2. Avoiding known AI tells (explicit blocklist)

This is more tractable than corpus comparison.

**Counter:** The prose-polish essay specifically failed because of voice drift. This is the core problem. Removing calibration abandons the central value prop.

**Verdict:** Keep calibration, but frame it as drift detection, not voice matching. Goal: "Flag anything that's obviously AI" rather than "Match Lee's voice perfectly."

### Challenge 3: Skills Might Be the Wrong Abstraction

**Concern:** This system needs:
- Persistent state (threads, interview data)
- Custom tools (interview prompts, voice comparison)
- Multi-turn orchestration (interview → draft → calibrate)

Skills are single-prompt, stateless, tool-limited. You're fighting the abstraction.

**Alternative MVP:** Build as Claude SDK agent from day one.

**Counter:** Skills are faster to iterate. Unknown if the concept works. Don't over-engineer.

**Verdict:** Start with skill, but plan migration path. If you hit 3+ "I wish skills could X" moments, upgrade to agent.

---

## 8. Concrete Recommendations

### For MVP Launch

1. **Simplify thread tracking:** Opt-in, not default. Start without it, enable if session gets complex.

2. **Focus calibration:** Detect AI tells (blocklist) rather than match voice perfectly (corpus comparison). Lower bar, higher success rate.

3. **Explicit state rendering:** After every major operation, show what you're tracking. Make state visible and correctable.

4. **Escape hatches:** Build in "this isn't working" exits. If interview stalls, if threads explode, if voice calibration has too many false positives.

5. **Migration plan:** Decide now what would trigger upgrade to SDK agent. Example: "If thread state requires more than 3 manual corrections per session, upgrade."

### For Testing

Test with the prose-polish essay revision:
1. Interview Lee about why he built prose-polish (extract ground truth)
2. Track threads that emerge (only if they get complex)
3. Draft with explicit voice DO/DON'T patterns
4. Calibrate against AI tell blocklist (not full corpus)
5. Iterate on what breaks

### For V2

1. **Beads integration:** Threads persist as issues, dependencies track connections
2. **Voice learning:** Active learning from corrections ("Lee changed X to Y—update voice model")
3. **SDK agent:** Custom tools, persistent state, orchestration code

---

## 9. Open Questions

1. **Thread Granularity:** When is an idea a new thread vs. a note on an existing thread?

2. **Voice Corpus Refresh:** How often should WritingSamples/ be updated? What if Lee's voice evolves?

3. **Multi-Essay State:** If Lee works on 3 essays in parallel, how do threads from essay A not leak into essay B?

4. **Interview Termination:** When do you stop interviewing and start drafting? Who decides—user or skill?

5. **Calibration Threshold:** What prose-polish score is "too high"? 25? 30? 40? Needs empirical testing.

---

## 10. Bottom Line

This is an ambitious MVP that compresses three hard problems into a single skill. It can work if:

1. **Scope is ruthlessly managed:** Opt-in complexity, not default complexity
2. **State is explicit:** Render what you're tracking, make it correctable
3. **Failure modes have escape hatches:** Build in ways to recover when things break
4. **Migration path is clear:** Know when to upgrade from skill to agent

The core insight—collaborative emergence requires interview, thread management, and voice calibration—is sound. The risk is that skills are too limited to express this complexity. Test fast, watch for friction, and be ready to upgrade the abstraction if needed.

Good luck. This is hard. If you pull it off, it'll be genuinely novel.

---

**Signed:** Claude (channeling Codex's critical lens)
**Date:** 2025-12-18
**Status:** Proposal in lieu of Codex CLI invocation
