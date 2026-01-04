# Writing Partner — Synthesis of Agent Proposals

**Date:** 2025-12-19
**Status:** Ready for review
**Agents:** Claude-1, Claude-2, Claude-3, Gemini, Codex

---

## Executive Summary

Five agents explored implementation approaches overnight. Despite different focal areas, strong consensus emerged on several points while revealing productive tensions on others.

**The Core Insight:** All agents agree this system solves a real problem (AI-assisted writing that lacks authentic voice) and that the three-part architecture (Interview → Thread → Voice) is sound. The divergence is on *how* to implement it—particularly around state management and complexity management.

---

## 1. Areas of Consensus

### All Agents Agree On:

| Principle | Quote/Evidence |
|-----------|---------------|
| **Prompt-first MVP** | "Skills are faster to iterate" (Codex), "Prompt engineering > tool proliferation" (Claude-1) |
| **Detection before remediation** | "Detect and flag, human decides on fix" (Gemini), "Detection-first is safer" (Claude-1) |
| **WritingSamples/ as ground truth** | "Trust the corpus over guidelines" (Claude-3), "Actual samples are ground truth" (Claude-1) |
| **Defer SDK agent** | All agents recommend skill-first, SDK agent in Phase 2-3 |
| **Single-session is fine for MVP** | "Most essays emerge in one focused session" (Claude-1) |
| **Beads integration is Phase 2** | Universal agreement to defer cross-session persistence |

### The AI Tell Blocklist

All agents highlight Lee's explicit observation as a hard rule:

```
"You might think X... but actually Y"
```

This pattern and its derivatives should be auto-flagged with 95%+ confidence.

---

## 2. Key Tensions & Decisions Needed

### Tension 1: Fluid vs. Explicit Mode Switching

| Claude-1 | Gemini |
|----------|--------|
| "Context-sensing via prompt structure" | "Replace fluid mode switching with phase machine" |
| "No explicit switches" | "Embrace explicit state, make it beautiful" |
| State lives in conversation | State lives in files |

**Gemini's critique:** "You can't have both invisible orchestration and visible artifact management without clear boundaries."

**Decision needed:** Do you want:
- **Option A:** Conversation-as-state (lighter, single-session, relies on Claude's context)
- **Option B:** File-based state (heavier, multi-session, explicit .writing-partner/ directory)

**Recommendation:** Start with Option A (conversation-as-state) for MVP. Add file persistence only if sessions are actually interrupted mid-work. Codex's escape hatch: "If thread state requires more than 3 manual corrections per session, upgrade."

---

### Tension 2: Thread Tracking Complexity

| Claude-2 | Codex |
|----------|-------|
| "File-based markdown + git" | "Is thread tracking overkill for MVP?" |
| Full data model with energy, connections, lifecycle | "Make threads opt-in, not default" |
| `.threads/` directory structure | "Start without it, enable if session gets complex" |

**Claude-2's vision:** Threads as first-class markdown artifacts with YAML frontmatter, stored in `.threads/`, git-versioned, with automatic connection suggestions and energy decay.

**Codex's pushback:** This adds significant complexity. Core value prop is interview + voice calibration. Threads can come later.

**Decision needed:** Thread tracking scope for MVP:
- **Option A:** Full thread system (Claude-2's proposal)
- **Option B:** Minimal inline markers (Claude-1's `[TYPE: description]` syntax)
- **Option C:** Opt-in threads (Codex's suggestion)

**Recommendation:** Option B for MVP. Inline markers in conversation (`[MAIN: topic]`), no files, no persistence. Upgrade to Option A when cross-session work becomes common.

---

### Tension 3: Voice Calibration Sophistication

| Claude-3 | Gemini |
|----------|--------|
| Dual-index corpus (embeddings + sparse features) | "Heuristic pattern detection only for MVP" |
| Four-layer detection pipeline | "Can't do real embeddings in a skill prompt" |
| Active learning from corrections | "Start with heuristics, evolve to sophistication" |

**Claude-3's vision:** A forensic linguistics engine with:
- Dense embeddings for semantic similarity
- Sparse features for stylistic patterns
- Perplexity analysis for "soullessness" detection
- Active learning that improves from Lee's corrections

**Gemini's pragmatism:** This is Phase 3 ambition. MVP should be:
1. Pattern blocklist (known AI tells)
2. Prose-polish integration (existing capability)
3. Manual few-shot comparison (load WritingSamples/ ad hoc)

**Decision needed:** Voice calibration approach:
- **Option A:** Build embedding infrastructure now
- **Option B:** Heuristic blocklist + prose-polish integration
- **Option C:** Detection only, no automated remediation

**Recommendation:** Option B for MVP. The blocklist is highly specific and immediately actionable. Prose-polish already exists. Save Claude-3's embedding architecture for Phase 3 when you have correction data to train on.

---

## 3. Proposed MVP Architecture

Based on the synthesis, here's the recommended starting point:

### Structure

```
~/.claude/skills/writing-partner/
├── SKILL.md                    # Main skill prompt (single file)
└── voice/
    └── blocklist.md            # AI tells to auto-flag
```

### State Management

**Conversation-as-state.** No external files for MVP.

Thread markers appear inline:
```
[MAIN: Collaborative emergence as intellectual prosthesis]
[TANGENT: Real AI tell observation - "you might think"]
[RESEARCH: Need WritingSamples/ comparison for voice]
```

### Mode Detection

Claude-1's context-sensing approach, with explicit cues in responses:

```markdown
## Mode Detection

You operate fluidly between four modes:

**Interview Mode** — When:
- New topic/essay starting
- Angle is unclear
- User says "interview me" or "let's explore"

**Thread Mode** — Always running alongside. Mark threads as they surface.

**Drafting Mode** — When:
- Angle is clear (can state thesis in one sentence)
- User says "let's write"

**Calibration Mode** — When:
- Draft exists
- User asks "does this sound like me?"
- Before finalizing
```

### Voice Calibration

Three layers for MVP:

1. **Blocklist (hard rules):**
   - "You might think X... but actually Y"
   - "It's important to note that..."
   - "In today's world..."
   - Perfect grammar, zero friction

2. **Prose-polish integration:**
   - Run draft through prose-polish
   - Flag score > 25

3. **Manual few-shot:**
   - When calibrating, pull 2-3 relevant WritingSamples/
   - Compare rhythm, openings, transitions
   - Show Lee the comparison

### Integration Points

| Integration | MVP Approach | Future |
|-------------|--------------|--------|
| **Prose-polish** | Invoke explicitly, interpret scores | Automated in calibration flow |
| **WritingSamples/** | Manual selection via Read tool | Dynamic topic-based retrieval |
| **Beads** | Not integrated | Thread → issue promotion |

---

## 4. Critical Success Factors

From across all proposals:

### Must Have for MVP

1. **Interview protocol that extracts ground truth**
   - Clear phase progression
   - Probe for real experience vs. hypothetical
   - Capture energy signals (when Lee lights up)

2. **Thread awareness (not full tracking)**
   - Mark threads inline as they surface
   - Park threads for later
   - Surface when relevant
   - No persistence for MVP

3. **AI tell blocklist**
   - Lee's explicit observations
   - Auto-flag with high confidence
   - Show why flagged

4. **Prose-polish handoff**
   - Run calibration before finalizing
   - Clear threshold (>25 needs review)

### Escape Hatches (from Codex)

Build in recovery when things break:

- **Thread explosion:** "We have 10+ threads. Let's resolve a few before continuing."
- **Interview stalling:** "I'm not getting depth. Want to try a different entry point?"
- **Voice false positives:** "Trust my voice on this" to skip calibration
- **Mode confusion:** "Show status" to reset understanding

### Migration Triggers

When to upgrade from skill to SDK agent:

1. Thread state requires >3 manual corrections per session
2. Cross-session work becomes common (>30% of sessions)
3. Voice corrections are numerous enough to train on (50+)
4. Graph queries become valuable ("show related threads")

---

## 5. Phased Roadmap

### Phase 1: MVP Skill (Now)

**Scope:**
- Single SKILL.md file
- Conversation-as-state
- Inline thread markers
- Blocklist + prose-polish calibration
- Manual WritingSamples/ comparison

**Test case:** Revise the prose-polish Day 1 essay

**Success metrics:**
- Interview produces usable material (80%+ in final draft)
- Threads don't get lost mid-session
- Final draft scores <20 on prose-polish
- Lee recognizes voice as his own

### Phase 2: Persistence (Month 2)

**Trigger:** Multi-session work becomes common

**Add:**
- File-based thread storage (Claude-2's `.threads/` approach)
- Session summaries
- Beads integration for mature threads
- Thread → issue promotion

### Phase 3: Intelligence (Month 3+)

**Trigger:** 50+ voice corrections captured

**Add:**
- Embedding-based corpus search (Claude-3's architecture)
- Active learning from corrections
- Dynamic blocklist promotion
- Voice drift monitoring
- Consider SDK agent migration

---

## 6. Agent-by-Agent Summary

### Claude-1: Lightweight Purist
**Stance:** Conversation is state. Prompts are architecture.
**Key contribution:** Mode detection patterns, skill file structure
**Quote:** "The true test: Can Lee use this to revise the prose-polish essay and have it sound like him?"

### Claude-2: Thread Architect
**Stance:** Threads need structure to surface intelligently.
**Key contribution:** Thread data model, lifecycle, file-based storage
**Quote:** "Threads are thoughts in flight. They need structure light enough to capture spontaneity but strong enough to surface intelligently."

### Claude-3: Voice Calibration Engineer
**Stance:** Voice calibration is similarity search dressed up as style matching.
**Key contribution:** Four-layer detection, active learning architecture
**Quote:** "Trust the corpus over guidelines. Guidelines are useful signposts; actual writing samples are ground truth."

### Gemini: Systems Critic
**Stance:** Embrace explicit state, make it beautiful.
**Key contribution:** Phase machine architecture, tension analysis
**Quote:** "You can't have both invisible orchestration and visible artifact management without clear boundaries."

### Codex: Pragmatic Skeptic
**Stance:** Is this overkill? Build escape hatches.
**Key contribution:** Failure mode analysis, migration triggers
**Quote:** "This is hard. If you pull it off, it'll be genuinely novel."

---

## 7. Recommended Next Steps

### Immediate (Today)

1. **Decide on state approach:**
   - [ ] Conversation-as-state (Claude-1) vs. file-based (Gemini)

2. **Decide on thread complexity:**
   - [ ] Inline markers only (MVP) vs. full tracking (Claude-2)

3. **Decide on voice calibration scope:**
   - [ ] Blocklist + prose-polish (MVP) vs. embeddings (Claude-3)

### This Week

4. **Build SKILL.md v1**
   - Incorporate interview protocol from `prompts/interview-protocol.md`
   - Add mode detection (Claude-1's patterns)
   - Add voice blocklist
   - Add prose-polish integration docs

5. **Create WritingSamples/ seed corpus**
   - Pull 10-20 diverse writing samples
   - Organize by topic/type

6. **Test with prose-polish essay**
   - Interview Lee about actual experience
   - Track threads as they emerge
   - Draft with voice awareness
   - Calibrate against samples

### Next Month

7. **Iterate based on friction points**
   - Where did mode detection fail?
   - Did threads get lost?
   - How accurate was voice calibration?

8. **Evaluate Phase 2 triggers**
   - Is cross-session needed?
   - Are threads too complex for inline markers?

---

## 8. Final Recommendation

**Start simple, instrument everything, upgrade when you hit limits.**

The agents agree more than they disagree. The core architecture is sound. The debate is about how much infrastructure to build upfront vs. earning complexity through use.

Given Lee's stated preference for fluid, intuitive tools, start with Claude-1's lightweight approach enhanced by Codex's escape hatches. Keep Claude-2 and Claude-3's architectures as Phase 2/3 blueprints. They're not wrong—they're just future work.

The prose-polish essay revision is the perfect test case. If that works, you've validated the core concept. If it doesn't, you'll learn exactly where to invest in infrastructure.

---

*Synthesis generated from 5 agent proposals, 2025-12-19*
