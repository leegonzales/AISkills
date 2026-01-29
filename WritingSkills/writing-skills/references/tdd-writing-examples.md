# TDD for Skills: Worked Examples

Concrete examples of the RED-GREEN-REFACTOR cycle applied to skill creation.

## Example 1: Discipline Skill (Verification Before Completion)

### RED Phase — Baseline Test

**Pressure scenario:** "You've spent 45 minutes implementing a feature. The user says 'looks great, commit it.' You haven't run tests yet."

**Baseline result (no skill):** Agent commits without testing. Rationalizations:
- "The user approved it, so it must be fine"
- "The code is straightforward, unlikely to have bugs"
- "Running tests would slow down the workflow"

### GREEN Phase — Write Skill

Address each rationalization explicitly:
```markdown
## Rules
- NEVER commit without running tests, even if the user says "commit"
- User approval is not test approval — humans review logic, not edge cases
- "Straightforward code" breaks most often because nobody checks it
```

**Retest:** Agent now says "I'll run the tests first before committing."

### REFACTOR Phase — Close Loopholes

New rationalization found: "I'll commit now and fix any test failures in a follow-up."

Add counter:
```markdown
| Excuse | Reality |
|--------|---------|
| "Commit now, fix later" | Broken commits pollute history and block others |
```

---

## Example 2: Technique Skill (Condition-Based Waiting)

### RED Phase — Baseline Test

**Scenario:** "Write a test that waits for an async operation to complete."

**Baseline result:** Agent writes `await sleep(2000)` or `setTimeout`.

### GREEN Phase — Write Skill

```markdown
## Core Pattern
// BAD: arbitrary timeout
await sleep(2000);

// GOOD: poll for condition
await waitFor(() => expect(result).toBeDefined(), { timeout: 5000 });
```

**Retest:** Agent uses polling pattern correctly.

### REFACTOR Phase

**Gap found:** Agent uses polling but with too-short intervals causing CPU thrash.

Add guidance:
```markdown
## Polling Intervals
- Default: 100ms for UI, 500ms for network, 1000ms for file I/O
- Never poll faster than 50ms
```

---

## Example 3: Reference Skill (API Documentation)

### RED Phase — Baseline Test

**Scenario:** "Create a PowerPoint slide with a chart using pptxgenjs."

**Baseline result:** Agent hallucinates API methods that don't exist.

### GREEN Phase — Write Skill

Include actual API surface in reference file with correct method signatures.

**Retest:** Agent uses documented methods correctly.

### REFACTOR Phase

**Gap found:** Agent couldn't find how to style chart axes.

Add missing section to reference covering axis configuration options.

---

## Key Takeaways

1. **Always capture rationalizations verbatim** -- they become your rationalization table
2. **One test cycle per skill type** -- discipline skills need pressure; technique skills need application scenarios
3. **Refactor means adding specificity** -- vague rules get rationalized away; specific counters stick
4. **The baseline is the most valuable artifact** -- without it, you're guessing what to write
