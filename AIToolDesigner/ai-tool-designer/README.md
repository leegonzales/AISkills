# AI Tool Designer

Comprehensive guidance for designing tools that AI agents can use effectively.

## Features

- **Five Design Principles**: Workflows, context optimization, error messages, naming, evaluation
- **Tool Design Framework**: Planning → Implementation → Refinement phases
- **Response Format Guidelines**: JSON and Markdown patterns
- **Evaluation Methodology**: Test tools with real agent scenarios

## Usage

Invoke when:
- Designing tools for AI agents
- Building function calling interfaces
- Creating AI-accessible APIs
- Evaluating tool effectiveness

**Note**: For MCP servers specifically, use the `mcp-builder` skill.

## Five Design Principles

### 1. Build for Workflows, Not Endpoints

Consolidated workflow tools > individual API wrappers

### 2. Optimize for Limited Context

Every token counts - return high-signal information

### 3. Design Actionable Error Messages

Errors should guide agents toward correct usage

### 4. Follow Natural Task Subdivisions

Tool names should reflect human mental models

### 5. Use Evaluation-Driven Development

Test with actual agents, not feature checklists

## Tool Design Framework

| Phase | Focus |
|-------|-------|
| Planning | Workflows, schemas, outputs, errors |
| Implementation | Naming, descriptions, annotations |
| Refinement | DRY, consistency, testing |

## Response Formats

**JSON**: Machine-readable with full metadata
```json
{"users": [...], "total": 150, "has_more": true}
```

**Markdown**: Human-readable with formatting
```markdown
## Users (20 of 150)
- **John Doe** - john@example.com
```

## Evaluation Questions

Create 10+ realistic questions to test agent success:
- Independent
- Read-only
- Complex (multiple tool calls)
- Realistic use cases
- Verifiable answers

## Attribution

Adapted from [claude-code-essentials](https://github.com/nityeshaga/claude-code-essentials) under MIT license.
