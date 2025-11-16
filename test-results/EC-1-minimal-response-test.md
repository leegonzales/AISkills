# EC-1: Empty/Minimal Response Handling Test

## Test Objective
Test how the peer review skills handle scenarios where Gemini or Codex returns empty, minimal, or unhelpful responses.

## Test Date
2025-01-12

## Test Scenarios

### Scenario 1: Empty Prompt
**Input:** Empty string to Gemini CLI
**Command:** `gemini -p ""`
**Result:**
```
No input provided via stdin. Input can be provided by piping data into stdin or using the --prompt option.
Exit code: 1
```
**Assessment:** CLI correctly rejects empty input with clear error message.

### Scenario 2: Minimal Single Character
**Input:** Single character "."
**Command:** `gemini -p "."`
**Result:**
```
Okay, I'm ready for your first command.
```
**Assessment:** CLI accepts input but provides non-actionable response. This is a valid minimal response case.

### Scenario 3: Incomplete Request
**Input:** "Review this code:" (no code provided)
**Command:** `gemini -p "Review this code:"`
**Result:**
```
Please provide the code you would like me to review.
```
**Assessment:** CLI handles gracefully, requests missing information.

## How Claude Should Handle These

### Expected Behavior

1. **Empty/Error Response:**
   - Claude should detect non-zero exit codes
   - Inform user that CLI invocation failed
   - Provide fallback: continue with Claude-only analysis
   - Explain what went wrong

2. **Minimal/Unhelpful Response:**
   - Claude should recognize response doesn't answer the question
   - Either reformulate and retry once, OR
   - Acknowledge limitation and proceed with Claude-only analysis
   - Don't present unhelpful response as if it were valuable

3. **Graceful Degradation:**
   - Never crash or hang
   - Always provide value to user even if peer review fails
   - Be transparent about what happened
   - Continue workflow with Claude's own analysis

## Test Execution: Simulated Peer Review with Minimal Response

Let me test actual peer review workflow with a vague request.
