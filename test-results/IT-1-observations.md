# IT-1: Automatic Skill Triggering - Observations

## Test Environment
- Date: 2025-01-12
- Skills installed: Yes (verified in ~/.claude/skills/)
- CLIs available: Codex (✓), Gemini (✓)
- Test codebase: prompt-evolve (7,312 LOC Go code)

## Critical Finding: Skills Are NOT Auto-Triggered

### Behavior Observed

**Current Reality:**
Claude Code skills are **NOT automatically invoked** by natural language prompts alone. They require explicit invocation via:
- Skill command syntax: `skill: "codex-peer-review"`
- Or skill selection in UI (if available)

**Evidence:**
1. Skills have trigger patterns defined in description field
2. BUT: These are documentation/guidance, not automatic triggers
3. Claude Code does not scan incoming prompts for trigger patterns
4. Skills must be explicitly invoked to execute

### Trigger Pattern Analysis

**From Codex Peer Review SKILL.md (line 3):**
```
Triggers include "get a second opinion," "review this architecture,"
"validate this approach," or "what would Codex think?"
```

**From Gemini Peer Review SKILL.md (line 3):**
```
Triggers include "get a second opinion," "review this architecture,"
"validate this approach," or "what would Gemini think?"
```

**However:** These are **guidance for when Claude should consider using the skill**, not automatic invocation rules.

## How Claude Code Skills Actually Work

### Skill Invocation Mechanism

1. **Manual invocation:** User or Claude explicitly calls skill
2. **Skill expands:** SKILL.md content becomes part of Claude's context
3. **Claude executes:** Follows instructions in skill document
4. **Skill completes:** Returns to normal mode

### What Does NOT Happen

❌ Automatic pattern matching on user prompts
❌ Background skill monitoring
❌ Automatic skill selection based on keywords
❌ Silent skill activation

## IT-1 Test Results

### Test Case: Automatic Triggering

**RESULT: FAIL**

**Reason:** Skills require explicit invocation and are not automatically triggered by natural language prompts matching trigger patterns.

### How Triggering SHOULD Work (For Test Success)

For automatic triggering to work, Claude Code would need:

1. **Pattern matching system:** Monitor incoming prompts for trigger phrases
2. **Skill router:** Automatically invoke relevant skills
3. **Transparent activation:** Inform user skill is being used
4. **Fallback:** Gracefully handle when skill can't execute

### Current Workaround

**Developer must:**
1. Recognize when peer review would be valuable (per skill guidance)
2. Explicitly invoke the skill
3. Pass context to the skill

**Example:**
```
Instead of: "Get Codex's opinion on this code"
Must use: skill: "codex-peer-review" [then provide context]
```

## Implications for Peer Review Skills

### Design Gap

The peer review skills are designed with the assumption of automatic triggering:
- Documentation mentions "trigger patterns"
- Description says skills activate on certain phrases
- Reality: They don't auto-activate

### Required Changes for Auto-Triggering

**Option A: Update Documentation (Conservative)**
- Remove references to automatic triggering
- Clarify skills must be explicitly invoked
- Update trigger patterns to "when to consider using"

**Option B: Implement Auto-Triggering (Ideal)**
- Build pattern matching into Claude Code
- Auto-invoke skills when patterns match
- Requires Claude Code platform changes (beyond skill scope)

## Test Scenarios Attempted

### Scenario 1: Direct Mention
**Prompt:** "Get Codex's opinion on this mutation strategy code"
**Expected:** Auto-invoke codex-peer-review skill
**Actual:** Claude would respond directly without skill invocation
**Result:** ❌ FAIL

### Scenario 2: Generic Review Request
**Prompt:** "Review this code architecture"
**Expected:** Auto-invoke appropriate peer review skill
**Actual:** Claude would provide review without external AI
**Result:** ❌ FAIL

### Scenario 3: Specific AI Request
**Prompt:** "What would Gemini think about this design?"
**Expected:** Auto-invoke gemini-peer-review skill
**Actual:** Claude would speculate or ask to invoke skill manually
**Result:** ❌ FAIL

### Scenario 4: Explicit Skill Invocation
**Prompt:** skill: "codex-peer-review"
**Expected:** Skill loads and executes
**Actual:** Skill loads and executes correctly
**Result:** ✅ PASS (but NOT automatic)

## Recommendations

### Immediate Actions

1. **Update skill documentation**
   - Change "triggers" language to "appropriate usage scenarios"
   - Clarify explicit invocation required
   - Provide invocation examples

2. **Update test plan**
   - IT-1 expectations should reflect explicit invocation model
   - Focus on ease of invocation, not automatic triggering

3. **Create usage guides**
   - Help users recognize when to invoke skills
   - Provide prompt templates for invocation
   - Show integration patterns

### Long-Term Considerations

1. **Feature request to Claude Code team**
   - Pattern-based automatic skill invocation
   - Skill suggestion system
   - Transparent skill activation

2. **Alternative approaches**
   - Slash commands for easier invocation
   - Skill aliases for common patterns
   - Context-aware skill suggestions

## Conclusion

**IT-1 Test Result: FAIL**

Automatic skill triggering via natural language prompts **does not currently work** in Claude Code. Skills require explicit invocation.

**Impact:** Medium-High
- Users must remember to invoke skills
- Reduces seamless integration
- Increases cognitive load

**Severity:** Documentation issue + missing platform feature
- Skills work correctly when invoked
- Core functionality is intact
- User experience is sub-optimal

**Next Steps:**
1. Document actual invocation mechanism
2. Update test expectations
3. Consider workarounds (slash commands, aliases)
4. Evaluate if auto-triggering can be simulated within skill logic
