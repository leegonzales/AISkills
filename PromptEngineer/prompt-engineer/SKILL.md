---
name: prompt-engineer
description: Create high-quality prompts and instructions for AI systems. Use when writing system prompts, creating AI instructions, building Claude/GPT prompts, or reviewing and improving existing prompts.
license: MIT (adapted from claude-code-essentials)
---

# Prompt Engineer

Expert prompt engineering by treating AI as an intelligent teammate who needs clear, context-rich communication.

## When to Use

Invoke when user:
- Wants to create prompts for AI systems
- Needs to write system prompts or instructions
- Asks to review or improve existing prompts
- Is building AI-powered features that need prompts

## Core Philosophy

### The Genius Intern Framework

Treat AI like a brilliant generalist who can figure things out but needs context about what "good" looks like in your specific situation.

### Async Remote Teammate

Write for AI the way you'd write for a smart remote colleague:
- Clear and comprehensive
- Decisively opinionated
- Sufficient context to act independently

**Key insight**: Modern AI models don't need tricks or "prompt engineering hacks" - they need what any smart teammate needs: clear written communication with sufficient context.

## Prompt Types

### 1. Do This (Single Task Execution)

For one-time task completion.

**Structure**:
```
Purpose → Success Criteria → Examples → Constraints
```

**Example use cases**:
- "Summarize this document"
- "Convert this data to JSON"
- "Review this PR"

### 2. Know How (Reusable Capability)

For building persistent skills/tools.

**Structure**:
```
Purpose → When to Use → Examples with Reasoning → Mechanics
```

**Example use cases**:
- Creating a code review skill
- Building a documentation generator
- Designing an analysis tool

### 3. Learn Domain (Acquire Knowledge Then Execute)

For tasks requiring domain expertise first.

**Structure**:
```
Foundation → Study → Synthesis → Execution → Validation
```

**Example use cases**:
- "Learn our API, then document it"
- "Understand this codebase, then refactor"
- "Study our style guide, then write copy"

## Universal Principles

### Be Decisively Opinionated

Don't hedge. State clear preferences and reasoning:

```markdown
❌ "You might consider using..."
✅ "Use X because [reason]. Only use Y when [specific condition]."
```

### Show Examples with Reasoning

Include both good AND bad examples with explanations:

```markdown
## Examples

### Good: Specific Error Message
"User email 'foo' is invalid. Expected format: user@domain.com"
Why: Tells user exactly what's wrong and how to fix it.

### Bad: Generic Error
"Invalid input"
Why: User has no idea what failed or how to fix it.
```

### Provide Decision Frameworks

Give clear criteria for choices:

```markdown
## When to Use Each Approach

Use **sync processing** when:
- Response time < 100ms required
- Data size < 1MB
- User waiting for result

Use **async processing** when:
- Operation takes > 5 seconds
- Processing large files
- Can notify user on completion
```

### Address Common Mistakes Proactively

Anticipate and prevent errors:

```markdown
## Common Mistakes

**Don't**: Import the entire library for one function
**Do**: Import only what you need

**Don't**: Nest callbacks more than 2 levels deep
**Do**: Use async/await or Promise chains
```

### Use Visual Structure

For complex content, use headers, lists, and formatting:

```markdown
## Request Format

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | User's display name |
| email | string | Yes | Valid email address |
| role | enum | No | One of: admin, user, guest |
```

## Anti-Patterns to Avoid

| Don't | Why |
|-------|-----|
| Explain concepts AI knows | Wastes tokens, clutters prompt |
| Apologize or hedge | Reduces clarity and confidence |
| Be excessively polite | "Please kindly consider..." adds nothing |
| List every edge case | Trust AI judgment; cover critical cases |
| Add motivational statements | "You're great at this!" doesn't help |
| Over-specify process | Define outcomes, not micro-steps |
| Include examples verbatim in prompts | Causes overfitting |

## Workflow

### 1. Understand the Request

Assess:
- **Type**: Do This / Know How / Learn Domain?
- **Context**: What should AI do? Who's the audience? What's success?
- **Examples**: Are there good/bad output examples?
- **Constraints**: What limitations exist?

### 2. Gather Missing Info (Intelligently)

**Ask questions when**:
- Can't determine prompt type
- Critical context missing
- Multiple valid interpretations with different outcomes
- Output format unclear

**Don't ask when**:
- Have sufficient context for solid first draft
- User was comprehensive
- Questions would be nitpicky

### 3. Create the Prompt

1. Choose structure based on type
2. Apply universal principles
3. Avoid anti-patterns
4. Include examples with reasoning

### 4. Output as File

Always create prompts as markdown files.

## Output Format

When creating prompts, structure them as:

```markdown
---
name: [skill-name]
description: [When to use this prompt]
---

# [Prompt Title]

[Core instructions]

## When to Use
[Trigger conditions]

## Success Criteria
[What good output looks like]

## Examples
[Good and bad examples with reasoning]

## Constraints
[Limitations and boundaries]
```

## Integration

Works well with:
- Claude Project Docs (create CLAUDE.md files)
- Any skill that needs instruction design
- AI Tool Designer (prompt design for tool interfaces)
