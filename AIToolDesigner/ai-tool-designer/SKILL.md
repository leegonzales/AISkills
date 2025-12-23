---
name: ai-tool-designer
description: Design effective tools for AI agents. Use when creating agent tools, function calling interfaces, or any AI-accessible APIs. Covers tool naming, input/output design, error handling, and evaluation methodologies.
license: MIT (adapted from claude-code-essentials)
---

# AI Tool Designer

Comprehensive guidance for designing tools that AI agents can use effectively.

## When to Use

Invoke when user:
- Is designing tools for AI agents
- Building function calling interfaces
- Creating any AI-accessible APIs
- Wants to evaluate tool effectiveness

**Note**: For MCP servers specifically, use the `mcp-builder` skill instead.

## Core Principle

> The quality of a tool system is measured not by how comprehensively it implements features, but by how well it enables AI agents to accomplish realistic, complex tasks.

## Five Design Principles

### 1. Build for Workflows, Not Endpoints

**Don't** simply wrap API endpoints. **Do** build workflow tools that enable complete tasks.

```
❌ Separate tools: check_availability, create_event, send_notification
✅ Single tool: schedule_event (checks conflicts, creates event, notifies)
```

**Why**: Agents need to accomplish complete tasks, not make individual API calls. Consolidated tools reduce steps and improve success rates.

### 2. Optimize for Limited Context

Agents have constrained context windows. Make every token count.

| Do | Don't |
|----|-------|
| Return high-signal information | Return exhaustive data dumps |
| Offer "concise" vs "detailed" modes | Force verbose responses |
| Use human-readable identifiers | Return only technical IDs |
| Implement character limits (~25k) | Allow unbounded responses |
| Paginate with reasonable defaults (20-50) | Return all results |

### 3. Design Actionable Error Messages

Errors should guide agents toward correct usage:

```
❌ "Error 400: Invalid request"
✅ "The limit parameter must be 1-100. You provided 500.
   Try limit=50 with pagination using offset."
```

**Include**:
- What went wrong
- Why it's wrong
- How to fix it
- Example of correct usage

### 4. Follow Natural Task Subdivisions

Tool names should reflect how humans think about tasks:

```
❌ api_endpoint_users_post, api_endpoint_users_get
✅ create_user, search_users, delete_user
```

**Naming conventions**:
- Use snake_case: `search_users`
- Include service prefix: `github_create_issue`
- Start with verbs: get, list, search, create, update, delete
- Be specific to avoid conflicts

### 5. Use Evaluation-Driven Development

Test with actual agents, not just feature checklists:

1. Create 10+ realistic questions agents should answer
2. Test with actual AI agents
3. Observe where agents struggle
4. Iterate on tool design
5. Measure by task completion, not feature count

## Tool Design Framework

### Phase 1: Planning

**Identify Core Workflows**:
- List most valuable operations
- Prioritize common use cases
- Map tool combinations for complex tasks

**Design Input Schemas**:
- Use strong validation (JSON Schema, Zod, Pydantic)
- Include constraints (min/max, patterns, ranges)
- Provide clear descriptions with examples
- Set sensible defaults

**Design Output Formats**:
- Support JSON (programmatic) and Markdown (readable)
- Define consistent structures
- Plan for scale (pagination, truncation)
- Include metadata: `has_more`, `next_offset`, `total_count`

**Plan Error Handling**:
- Actionable, agent-friendly messages
- Authentication/authorization handling
- Rate limiting and timeout scenarios
- Guidance on recovery

### Phase 2: Implementation

**Tool Descriptions Must Include**:
1. One-line summary
2. Detailed purpose explanation
3. When to use (and when NOT to)
4. Parameter descriptions with examples
5. Return value schema
6. Error handling guidance

**Tool Annotations**:
```
readOnlyHint: true      # Read-only operations
destructiveHint: false  # Non-destructive
idempotentHint: true    # Repeated calls same effect
openWorldHint: true     # External system interaction
```

### Phase 3: Refinement

**Quality Checklist**:
- [ ] No duplicated code (DRY)
- [ ] Shared logic extracted
- [ ] Similar operations return similar formats
- [ ] All external calls have error handling
- [ ] Full type coverage
- [ ] Comprehensive documentation

## Response Formats

### JSON Format

For programmatic processing:

```json
{
  "users": [
    {"id": "U123", "name": "John", "email": "john@example.com"}
  ],
  "total": 150,
  "count": 20,
  "has_more": true,
  "next_offset": 20
}
```

### Markdown Format

For human presentation (often default):

```markdown
## Users (20 of 150)

- **John Doe** (@john.doe)
  - Email: john@example.com
  - Role: Developer

*Showing 20 results. Use offset=20 for more.*
```

## Pagination Best Practices

- Always respect `limit` parameter
- Return metadata: `has_more`, `next_offset`, `total_count`
- Default to 20-50 items
- Never load all results into memory
- Include clear guidance for getting more

## Input Validation

**Security**:
- Validate all parameters against schema
- Sanitize file paths (prevent traversal)
- Validate URLs and identifiers
- Prevent command injection

**Usability**:
- Return clear validation errors
- Include examples of correct format
- Mark required vs optional clearly
- Set sensible defaults

## Evaluation Questions

Create 10+ questions that test real agent use:

**Requirements for each question**:
- Independent (not dependent on others)
- Read-only (non-destructive)
- Complex (multiple tool calls needed)
- Realistic (based on real use cases)
- Verifiable (clear, single answer)
- Stable (answer won't change)

**Format**:
```xml
<evaluation>
  <qa_pair>
    <question>Find all projects with failed builds in the last week</question>
    <answer>project-alpha, project-gamma</answer>
  </qa_pair>
</evaluation>
```

## Output Format

When designing tools, document them as:

```markdown
## Tool: [tool_name]

**Purpose**: One-line description

**When to Use**: [Trigger conditions]
**When NOT to Use**: [Anti-patterns]

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| ... | ... | ... | ... |

### Response

**JSON Format**:
[schema]

**Markdown Format**:
[example]

### Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| ... | ... | ... |
```

## Integration

Works well with:
- MCP Builder (for MCP server implementation)
- Prompt Engineer (tool description writing)
- Any skill that defines agent capabilities
