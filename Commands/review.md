# Review - Structured Code Review

Review this branch objectively and thoroughly. Analyze each parameter one by one:

$ARGUMENTS

## Review Parameters

### 1. Code Quality
- **Code smells**: Violations of language conventions, inefficient patterns
- **Architecture**: Inconsistency with existing codebase patterns
- **Complexity**: Overly complicated solutions, deep nesting, long functions

### 2. Change Analysis
- **Git diff review**: All modified, added, and deleted files
- **Unintended changes**: Modifications outside the scope of this branch's purpose
- **Breaking changes**: Code that could break existing functionality

### 3. Cleanup Check
- **Leftover artifacts**: Debug code, commented blocks, TODO items
- **Simplification opportunities**: Overly complex code that could be simplified
- **Documentation**: Missing or outdated comments/docs for changed code

### 4. Additional Checks (if specified)
[User-specified focus areas from $ARGUMENTS]

## Output Format

```
BRANCH REVIEW: [branch-name]
============================

## Summary
[1-2 sentence overview of what this branch does]

## Findings

### Critical (Must Fix)
- [ ] [Issue with file:line] - [Description]

### Major (Should Fix)
- [ ] [Issue with file:line] - [Description]

### Minor (Consider Fixing)
- [ ] [Issue with file:line] - [Description]

### Suggestions (Optional Improvements)
- [ ] [Suggestion] - [Reasoning]

## Files Reviewed
- [file1.ext] - [status: clean / issues found]
- [file2.ext] - [status: clean / issues found]

## Verdict
[APPROVE / APPROVE WITH CHANGES / REQUEST CHANGES]
[Brief justification]
```

## Instructions

- Be objective - no bias toward approving or rejecting
- Think deeply about edge cases and potential issues
- Surface problems with severity ratings
- Provide actionable feedback with specific file:line references
- Consider both the code AND its impact on the broader codebase
