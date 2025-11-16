# MCP Builder Skill

A comprehensive guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.

## Overview

The Model Context Protocol (MCP) is an open standard that enables AI assistants like Claude to securely connect to external data sources and tools. MCP servers act as bridges between LLMs and external services, providing structured tool interfaces that LLMs can use to accomplish real-world tasks.

This skill provides a complete, production-ready methodology for building MCP servers in both Python (using FastMCP) and TypeScript (using the MCP SDK).

## Features

- **4-Phase Development Methodology**: Research, Implementation, Review, and Evaluation
- **Agent-Centric Design Principles**: Build tools optimized for LLM workflows, not just API wrappers
- **Dual Language Support**: Complete guides for both Python (FastMCP) and TypeScript (MCP SDK)
- **Best Practices Library**: Comprehensive guidelines for naming, design, pagination, error handling
- **Evaluation Framework**: Create rigorous test suites to validate MCP server effectiveness
- **Production-Ready Patterns**: Security, rate limiting, character limits, and error handling
- **Example Servers**: Reference implementations and evaluation scripts

## When to Use This Skill

Use MCP Builder when you need to:

- Build a custom MCP server to integrate an external API or service with Claude
- Create tools that allow Claude to interact with databases, SaaS platforms, or internal systems
- Design LLM-optimized interfaces for existing services
- Implement standardized protocols for AI-to-service communication
- Enable Claude to perform multi-step workflows across external systems

## When NOT to Use MCP

Before building a new MCP server, consider:

1. **Existing MCP Servers**: Check if a server already exists for your service at [modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers)
2. **Direct Tool Use**: For simple operations, Claude's existing tools (WebFetch, Bash, etc.) may suffice
3. **One-Time Tasks**: Building an MCP server requires investment - ensure recurring value
4. **Read-Only Web Content**: Use WebFetch or WebSearch instead of building an MCP server

## Prerequisites

### For Python (FastMCP)
- Python 3.10 or higher
- pip package manager
- Basic understanding of async/await patterns
- Familiarity with Pydantic for data validation

### For TypeScript (MCP SDK)
- Node.js 16 or higher
- npm or yarn package manager
- TypeScript knowledge
- Understanding of Zod schema validation

### General Knowledge
- REST API fundamentals
- Authentication patterns (API keys, OAuth)
- HTTP request/response cycles
- JSON data structures

## Installation

### Claude Code
```bash
# Install to global skills directory
cp -r mcp-builder ~/.claude/skills/

# Or install to project-specific skills
cp -r mcp-builder .claude/skills/
```

### Claude Web Chat
1. Download the packaged skill file: `mcp-builder-v1.0.0.skill`
2. Upload to claude.ai in Settings > Skills
3. Verify the skill is enabled for your conversation

## The 4-Phase Methodology

### Phase 1: Deep Research and Planning

**Understand Agent-Centric Design**
- Build for workflows, not just API endpoints
- Optimize for limited context (make every token count)
- Design actionable error messages
- Follow natural task subdivisions

**Study Documentation**
- Load MCP protocol spec from modelcontextprotocol.io
- Review language-specific SDK documentation
- Exhaustively study the target API documentation

**Create Implementation Plan**
- Select high-value tools to implement
- Design shared utilities and helpers
- Plan input/output schemas
- Define error handling strategies

### Phase 2: Implementation

**Set Up Project Structure**
- Python: Single `.py` file or modular structure with FastMCP
- TypeScript: Proper package.json, tsconfig.json, and SDK setup

**Implement Core Infrastructure**
- API request helper functions
- Error handling utilities
- Response formatting (JSON and Markdown)
- Pagination helpers
- Authentication/token management

**Implement Tools Systematically**
- Define input schemas with Pydantic (Python) or Zod (TypeScript)
- Write comprehensive docstrings/descriptions
- Implement tool logic with proper error handling
- Add tool annotations (readOnlyHint, destructiveHint, etc.)

### Phase 3: Review and Refine

**Code Quality Review**
- Ensure DRY principle (no duplication)
- Verify composability and shared logic
- Check consistency across similar operations
- Validate comprehensive error handling
- Confirm full type coverage

**Testing**
- Verify Python syntax or TypeScript build
- Test with evaluation harness (recommended)
- Use tmux for manual testing (server runs indefinitely)

**Quality Checklist**
- Follow language-specific checklist in reference docs
- Validate naming conventions
- Check documentation completeness
- Review security considerations

### Phase 4: Create Evaluations

**Develop 10 Complex Questions**
- Independent and self-contained
- Read-only operations only
- Require multiple tool calls
- Based on realistic use cases
- Verifiable with single, clear answers
- Stable (answers won't change over time)

**Run Evaluation Suite**
- Use provided evaluation scripts
- Measure LLM effectiveness with your tools
- Iterate based on results
- Document evaluation outcomes

## Example Use Cases

### 1. GitHub MCP Server
**Scenario**: Enable Claude to manage issues, pull requests, and repositories

**Tools Implemented**:
- `github_create_issue`: Create issues with labels and assignees
- `github_search_issues`: Search across repositories with filters
- `github_create_pull_request`: Open PRs with automated descriptions
- `github_list_commits`: View commit history with filtering

**Workflow**: Claude can investigate bugs, create issues, search for related work, and propose PRs - all through natural language conversation.

### 2. Slack MCP Server
**Scenario**: Allow Claude to participate in team communication

**Tools Implemented**:
- `slack_send_message`: Send messages to channels or users
- `slack_search_messages`: Find messages by keyword, user, or date
- `slack_list_channels`: Discover available channels
- `slack_get_thread`: Read threaded conversations

**Workflow**: Claude can respond to messages, search conversation history, and coordinate across channels.

### 3. Database MCP Server
**Scenario**: Enable Claude to query and analyze data

**Tools Implemented**:
- `db_execute_query`: Run SELECT queries with safety checks
- `db_get_schema`: Retrieve table structures and relationships
- `db_analyze_table`: Get statistics and distributions
- `db_export_results`: Export query results in multiple formats

**Workflow**: Claude can explore schemas, write optimized queries, analyze data patterns, and generate reports.

### 4. Customer Support MCP Server
**Scenario**: Integrate with Zendesk/Intercom for support automation

**Tools Implemented**:
- `support_search_tickets`: Find tickets by customer, topic, or status
- `support_create_ticket`: Open new tickets with categorization
- `support_add_comment`: Respond to existing tickets
- `support_get_customer_history`: View complete customer interactions

**Workflow**: Claude can triage tickets, research customer history, draft responses, and escalate when needed.

### 5. Analytics MCP Server
**Scenario**: Connect Claude to Google Analytics or custom analytics platforms

**Tools Implemented**:
- `analytics_get_metrics`: Retrieve key metrics over time periods
- `analytics_compare_segments`: Compare user cohorts or campaigns
- `analytics_get_funnel`: Analyze conversion funnels
- `analytics_generate_report`: Create formatted analysis reports

**Workflow**: Claude can answer business questions, identify trends, and generate insights from data.

## Integration with Peer Review Skills

MCP Builder works exceptionally well with AISkills peer review capabilities:

### Codex Peer Review (codex-peer-review)
Use Codex for code-level review of your MCP server implementation:

```bash
# Review Python MCP server implementation
codex "Review this Python MCP server for code quality, design patterns, and best practices. Focus on: FastMCP usage, Pydantic models, async patterns, error handling, and tool design." --files my_service_mcp.py

# Review TypeScript MCP server
codex "Review this TypeScript MCP server for type safety, SDK usage, and implementation quality. Check: Zod schemas, Promise patterns, error handling, and API integration." --files src/
```

### Gemini Peer Review (gemini-peer-review)
Use Gemini for architectural review and design validation:

```bash
# Review overall MCP server design
gemini "Review this MCP server architecture for: tool selection, workflow optimization, agent-centric design, and alignment with MCP best practices. Suggest improvements." --files .

# Review evaluation questions
gemini "Review these MCP evaluation questions for quality, complexity, and coverage. Check: independence, realism, verification, and comprehensive testing." --files evaluation.xml
```

### Combined Workflow
1. **Design Phase**: Use Gemini to review your implementation plan
2. **Implementation**: Build the MCP server following this skill's methodology
3. **Code Review**: Use Codex to review implementation quality
4. **Evaluation Review**: Use Gemini to validate your test questions
5. **Final Validation**: Run evaluations and iterate based on results

## Documentation

### Core Resources
- **SKILL.md**: Complete 4-phase methodology and workflow
- **reference/mcp_best_practices.md**: Universal MCP guidelines
- **reference/python_mcp_server.md**: Python/FastMCP implementation guide
- **reference/node_mcp_server.md**: TypeScript/MCP SDK implementation guide
- **reference/evaluation.md**: Evaluation creation and execution guide

### Scripts
- **scripts/evaluation.py**: Run evaluation suites against your MCP server
- **scripts/connections.py**: Test MCP server connections
- **scripts/example_evaluation.xml**: Sample evaluation format
- **scripts/requirements.txt**: Python dependencies for evaluation scripts

## Quick Start

### Python Example

```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# Initialize server
mcp = FastMCP("myservice_mcp")

# Define input model
class SearchInput(BaseModel):
    query: str = Field(..., description="Search query")
    limit: int = Field(default=10, ge=1, le=100)

# Register tool
@mcp.tool(
    name="myservice_search",
    annotations={"readOnlyHint": True}
)
async def search(params: SearchInput) -> str:
    """Search for items in MyService."""
    # Implementation here
    return f"Results for: {params.query}"
```

### TypeScript Example

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { z } from "zod";

const server = new Server({ name: "myservice-mcp-server" });

// Define input schema
const SearchSchema = z.object({
  query: z.string(),
  limit: z.number().min(1).max(100).default(10)
});

// Register tool
server.registerTool({
  name: "myservice_search",
  description: "Search for items in MyService",
  inputSchema: zodToJsonSchema(SearchSchema),
  annotations: { readOnlyHint: true }
}, async ({ query, limit }) => {
  // Implementation here
  return { content: [{ type: "text", text: `Results for: ${query}` }] };
});
```

## Best Practices Summary

### Design Principles
1. **Workflow-Oriented**: Combine related operations into coherent tools
2. **Context-Efficient**: Return high-signal information, not data dumps
3. **Actionable Errors**: Guide users toward correct usage
4. **Natural Naming**: Follow how humans think about tasks

### Implementation Guidelines
1. **Input Validation**: Use Pydantic (Python) or Zod (TypeScript)
2. **Error Handling**: Comprehensive try/catch with clear messages
3. **Response Formats**: Support both JSON and Markdown
4. **Pagination**: Always respect limits and provide next_offset
5. **Character Limits**: Truncate gracefully at 25,000 characters
6. **Type Safety**: Full type coverage throughout

### Security Considerations
1. Store API credentials securely (environment variables)
2. Validate and sanitize all inputs
3. Implement rate limiting for expensive operations
4. Log errors without exposing sensitive data
5. Use HTTPS for all API communications
6. Follow OAuth best practices for user authentication

## Version History

See [CHANGELOG.md](./CHANGELOG.md) for detailed version history.

## Attribution

Originally developed by Anthropic.

**Source**: https://github.com/anthropics/skills/tree/main/mcp-builder

Licensed under the Apache License 2.0 (see LICENSE.txt for complete terms).

Integrated into AISkills collection with enhancements:
- Comprehensive README with use cases and integration examples
- Integration with codex-peer-review and gemini-peer-review skills
- Packaged for easy distribution via Claude Code and web chat
- Enhanced documentation and quick start guides

## License

Apache License 2.0 - See LICENSE.txt for complete terms.

Copyright notice preserved from original Anthropic implementation.

## Contributing

This skill is maintained as part of the AISkills collection. For issues or improvements:

1. Test thoroughly with real MCP server implementations
2. Document any additions with examples
3. Ensure changes align with MCP protocol standards
4. Update reference documentation as needed

## Additional Resources

### Official MCP Resources
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk
- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk
- **Server Registry**: https://modelcontextprotocol.io/servers

### AISkills Integration
- **Codex Peer Review**: Use for code-level review of MCP implementations
- **Gemini Peer Review**: Use for architectural and design validation
- **Context Continuity**: Maintain MCP server development context across sessions

---

**Version**: 1.0.0
**Last Updated**: 2025-11-16
**Maintained By**: AISkills Collection
