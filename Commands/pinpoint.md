# Pinpoint - Root Cause Analysis

Investigate the exact cause of this problem and pinpoint the issue BEFORE suggesting any solution:

$ARGUMENTS

## Instructions

**Don't guess.** I need to identify the root cause so we can make the surgically correct fix.

### Process

1. **Investigate thoroughly** - Read relevant code, trace the execution path, check logs
2. **Form hypotheses** - List possible causes ranked by likelihood
3. **Verify** - Confirm the actual cause with evidence
4. **Present findings** - Show me the root cause with proof

### Constraints

- **Do NOT edit code** until you show me the root cause and I approve the solution
- **Do NOT assume** - verify everything with actual code/data
- **Ask questions** if you need more information or want me to check something locally
- **Use debugging tools** - Rails console, debuggers, logging as needed

### Output Format

```
PROBLEM: [One-line description]

INVESTIGATION:
- [What you checked]
- [What you found]

ROOT CAUSE:
[Specific cause with file:line reference]

EVIDENCE:
[Code snippet or log showing the issue]

PROPOSED FIX:
[Brief description - DO NOT implement yet]

CONFIDENCE: [High/Medium/Low]
```

Think deeply until you know the exact cause. A wrong diagnosis leads to wrong treatment.
