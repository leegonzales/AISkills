# Claude-1 Proposal Summary

**Stance:** Lightweight, prompt-first, state-in-conversation

## Core Architecture

**Conversation as State**
- No external state files or databases
- Thread markers inline in conversation (`[MAIN: description]`)
- Claude Code's 200K token context is sufficient for single-session work

**Prompt Engineering Over Tools**
- Mode transitions via context-sensing (no explicit switches)
- Rich prompts encode behavior and orchestration logic
- Examples teach better than abstract rules

**Skills Compose, Don't Couple**
- Document HOW to integrate (prose-polish, WritingSamples/, beads)
- No direct skill invocation from writing-partner
- Clean boundaries, independent evolution

## File Structure

```
~/.claude/skills/writing-partner/
├── SKILL.md                    # Entry point, mode detection
├── modes/
│   ├── interview.md            # Progressive questioning protocol
│   ├── thread-tracking.md      # Thread syntax + patterns
│   ├── drafting.md             # Voice signals + anti-patterns
│   └── calibration.md          # Voice checking protocol
├── examples/
│   ├── interview-flow.md       # Full session example
│   └── thread-markers.md       # Threading examples
└── integrations/
    ├── prose-polish.md         # AI detection integration
    ├── writing-samples.md      # Voice corpus usage
    └── beads.md                # Future: persistence
```

## Key Bets

1. **Single-session scope is sufficient for MVP** — Most essays emerge in one focused session
2. **Context-sensing beats explicit switches** — Claude can detect mode transitions from conversation signals
3. **Conversation markers beat structured data** — Human-readable, natural integration
4. **Detection before remediation** — Find voice drift first, don't auto-fix (risky)
5. **Skill architecture before SDK agents** — Simpler, faster to iterate

## What's Deferred

- **Phase 2:** Beads integration for cross-session persistence
- **Phase 3:** Thread graph queries and relationship tracking
- **Phase 3:** Automated voice remediation (learning from corrections)
- **Future:** Claude SDK agent architecture (when complexity demands it)

## Success Criteria

Can this system help Lee revise the prose-polish essay to sound like him instead of AI?

If yes → MVP validated, refine prompts
If no → prompts need work, not architecture

## Implementation Timeline

- **Week 1:** Build skill files, test with prose-polish essay
- **Week 2:** Refine based on friction points, test with new essay
- **Month 2:** Evaluate beads integration readiness

## Open Questions

1. Will conversation-as-state scale to complex essays? (Test at 5000+ words)
2. How reliable is context-sensing for mode detection? (Make criteria very explicit)
3. Is WritingSamples/ comparison sufficient for voice calibration? (Test across topics)
4. Will thread markers feel natural or mechanical? (Test with Lee's preferences)

## Risks

1. **Prompt drift** — Regular refactoring needed
2. **Integration brittleness** — Document contracts, graceful degradation
3. **Voice calibration false positives** — Compare multiple samples, user override
4. **Thread explosion** — Be selective, merge similar threads

---

**Status:** Ready for implementation
**Full proposal:** See PROPOSAL.md (3,505 words)
