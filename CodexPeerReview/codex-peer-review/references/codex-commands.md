# Codex CLI Command Reference

Complete reference for Codex CLI commands and flags relevant to peer review use cases.

---

## Command Overview

Codex CLI operates in two primary modes:
1. **Interactive mode:** Terminal UI for conversational interaction
2. **Non-interactive mode:** Exec command for automation and scripting

For peer review, **non-interactive mode** is recommended for predictable, automatable workflows.

---

## Core Commands

### `codex`

**Usage:** `codex [prompt] [flags]`

**Description:** Launch interactive terminal UI

**Common flags:**
- `--image` / `-i`: Attach image files (diagrams, screenshots)
- `--full-auto`: Unattended mode with minimal prompts

**Examples:**
```bash
# Interactive architecture review
codex "Review the architecture in architecture.md"

# With architecture diagram
codex --image architecture-diagram.png "Analyze this system design"

# Full auto mode for suggestions
codex --full-auto "Suggest improvements to the authentication flow"
```

**Use for peer review:**
- Quick interactive consultation
- When you want conversational follow-up
- Exploratory analysis

---

### `codex exec`

**Usage:** `codex exec [prompt] [flags]`
**Alias:** `codex e`

**Description:** Non-interactive execution streaming results to stdout

**Common flags:**
- `--output` / `-o`: Output format (text, json, jsonl)
- `--resume`: Resume previous session
- `--full-auto`: Unattended automation

**Examples:**
```bash
# Non-interactive code review
codex exec "Review this code for security issues: [code]"

# JSON output for programmatic parsing
codex exec --output json "Analyze architecture and return JSON"

# Resume previous analysis
codex exec --resume [session-id] "Continue previous review"
```

**Use for peer review (recommended):**
- Automated peer review workflows
- Scriptable analysis
- CI/CD integration
- Predictable, repeatable reviews

---

## Key Flags

### Image Attachment

**Flag:** `--image [path]` or `-i [path]`

**Description:** Attach image files (architecture diagrams, screenshots, charts)

**Formats:** PNG, JPG, SVG (most common image formats)

**Usage:**
```bash
# Single image
codex --image architecture.png "Review this architecture"

# Multiple images (repeat flag)
codex --image diagram1.png --image diagram2.png "Compare these designs"

# Multiple images (comma-separated)
codex --image diagram1.png,diagram2.png "Compare these designs"
```

**Use cases:**
- Architecture diagram review
- UI/UX design review
- System topology analysis
- Visual documentation review

---

### Automation Flags

**Flag:** `--full-auto`

**Description:** Unattended mode with automatic approvals (use with caution)

**Behavior:**
- Sets `--ask-for-approval on-failure`
- Sets `--sandbox workspace-write`
- Minimal interactive prompts

**Usage:**
```bash
codex --full-auto "Generate test cases for this module"
```

**⚠️ Warning:** Use carefully in peer review—can make changes without explicit approval

**Recommended for peer review:** Generally avoid unless you specifically want Codex to make changes automatically

---

### Approval Mode

**Flag:** `--ask-for-approval [mode]`

**Modes:**
- `suggest` (default): Ask before every action
- `auto`: Automatically approve all actions
- `on-failure`: Only ask when something fails

**Usage:**
```bash
# Ask before every action (safest)
codex --ask-for-approval suggest "Review and improve this code"

# Auto-approve (use with caution)
codex --ask-for-approval auto "Generate documentation"

# Only prompt on failures
codex --ask-for-approval on-failure "Run tests and fix issues"
```

**Recommended for peer review:** `suggest` mode (default) for transparency

---

### Sandbox Mode

**Flag:** `--sandbox [mode]`

**Modes:**
- `none`: No file system access
- `workspace-read`: Read-only access to workspace
- `workspace-write`: Read and write access to workspace

**Usage:**
```bash
# Read-only (safest for review)
codex --sandbox workspace-read "Review codebase structure"

# Write access (for implementing suggestions)
codex --sandbox workspace-write "Implement the suggested refactoring"

# No file access
codex --sandbox none "Analyze this code snippet"
```

**Recommended for peer review:** `workspace-read` for analysis, `none` for isolated snippets

---

### Output Format

**Flag:** `--output [format]` or `-o [format]`

**Formats:**
- `text` (default): Human-readable text
- `json`: Structured JSON output
- `jsonl`: JSON Lines format (streaming)

**Usage:**
```bash
# Default text output
codex exec --output text "Review architecture"

# JSON for programmatic parsing
codex exec --output json "Analyze code and structure results"

# JSON Lines for streaming
codex exec --output jsonl "Long-running analysis"
```

**Recommended for peer review:** `text` for human consumption, `json` for automated processing

---

## Slash Commands

Available within interactive Codex sessions (not applicable to `codex exec`).

### `/status`

**Description:** Check API limits and usage

**Usage:** Type `/status` in interactive session

**Shows:**
- Remaining API calls
- Rate limit status
- Token usage

**Use case:** Verify rate limits before extensive peer review session

---

### `/model`

**Description:** View current model (don't change it - let CLI use default)

**Usage:** Type `/model` in interactive session to see what's active

**Note:** Don't hardcode model names. Let Codex CLI use its default (latest) model.

---

## Configuration

### Config File: `~/.codex/config.toml`

**Location:** `~/.codex/config.toml`

**Common settings:**

```toml
# Approval mode (suggest|auto|on-failure)
ask_for_approval = "suggest"

# Sandbox mode (none|workspace-read|workspace-write)
sandbox = "workspace-read"

# Output format
output_format = "text"
```

**Recommended peer review config:**
```toml
ask_for_approval = "suggest"
sandbox = "workspace-read"
output_format = "text"
```

**Note:** Don't set model in config. Let Codex CLI use its default (latest) model.

---

### Project Config: `codex.md`

**Location:** `[project-root]/codex.md`

**Purpose:** Project-specific context, architecture notes, style guides

**Format:** Markdown file with project information

**Example:**
```markdown
# Project: Multi-Tenant SaaS Platform

## Architecture
- Microservices architecture
- PostgreSQL with row-level security for multi-tenancy
- Redis for caching
- BullMQ for background jobs

## Code Style
- TypeScript strict mode
- Functional programming preferred
- Jest for testing

## Key Decisions
- Multi-tenancy via RLS (see ADR-001)
- JWT authentication with refresh tokens (see ADR-002)
```

**Use case:** Codex automatically reads `codex.md` for project context

---

### Team Config: `AGENTS.md`

**Location:** `[project-root]/AGENTS.md`

**Purpose:** Define team roles and behaviors for multi-agent workflows

**Format:** Markdown with agent definitions

**Example:**
```markdown
# Agents

## Reviewer
Role: Code review and architecture critique
Focus: Security, performance, maintainability

## Implementer
Role: Implementation and refactoring
Focus: Clean code, test coverage
```

**Use case:** Advanced multi-agent scenarios (less common for peer review)

---

### Global Config: `~/.codex/instructions.md`

**Location:** `~/.codex/instructions.md`

**Purpose:** Global user preferences for all Codex sessions

**Example:**
```markdown
# Global Instructions

- Always consider security implications
- Prefer functional programming patterns
- Provide rationale for recommendations
- Highlight trade-offs explicitly
```

**Use case:** Consistent behavior across all peer review sessions

---

## Command Patterns for Peer Review

### Architecture Review

**Command:**
```bash
cat <<'EOF' | codex exec --sandbox workspace-read
[ARCHITECTURE REVIEW]

System: Multi-tenant SaaS platform
Scale: 100-500 tenants, 50-5K users per tenant

Architecture:
[architecture description or reference to codex.md]

Question: Review for scalability, security, and operational complexity.

Focus:
- Service boundaries
- Data consistency
- Tenant isolation
- Deployment complexity

Expected Output: Risk assessment with improvement recommendations
EOF
```

**Why this pattern:**
- Heredoc pipes cleanly to `codex exec`
- `--sandbox workspace-read`: Safe read-only access

---

### Architecture Review with Diagram

**Command:**
```bash
codex --image architecture-diagram.png --sandbox workspace-read "Analyze this architecture for single points of failure, scalability bottlenecks, and data consistency issues"
```

**Why this pattern:**
- `--image`: Visual architecture analysis
- Simple prompt for diagram-based review

---

### Security Review

**Command:**
```bash
cat <<'EOF' | codex exec --sandbox none
[SECURITY REVIEW]

Code:
[paste security-critical code here]

Threat Model:
- Authentication bypass
- SQL injection
- XSS attacks
- Sensitive data exposure

Question: Identify vulnerabilities and prioritize by severity.

Expected Output: Vulnerability list with remediation steps
EOF
```

**Why this pattern:**
- Heredoc for multi-line prompt
- `--sandbox none`: No file access for isolated code review
- Explicit threat model for focused analysis

---

### Design Decision Comparison

**Command:**
```bash
cat <<'EOF' | codex exec
[DESIGN DECISION]

Decision: Caching strategy for product catalog

Option A: Redis with TTL-based invalidation
- Pros: Fast, simple, horizontally scalable
- Cons: Stale data risk, invalidation complexity

Option B: Event-driven cache invalidation
- Pros: Always fresh data, precise control
- Cons: Complex implementation, event overhead

Option C: Hybrid (Redis + event-based invalidation)
- Pros: Fast + fresh
- Cons: Most complex

Context:
- 10K product SKUs
- Updates 100x/day
- Read-heavy (1M reads/day)
- Team familiar with Redis, less with event streaming

Criteria (in priority order):
1. Data freshness
2. Query performance
3. Implementation complexity
4. Operational overhead

Question: Which option is recommended? What are critical trade-offs?

Expected Output: Comparative analysis with recommendation and rationale
EOF
```

**Why this pattern:**
- Structured comparison format
- Clear criteria for evaluation
- Explicit context and constraints

---

### Performance Analysis

**Command:**
```bash
cat <<'EOF' | codex exec --sandbox workspace-read
[PERFORMANCE ANALYSIS]

File: src/api/order-handler.ts

Current Performance: 500ms average, 2s p99
Target: 100ms average, 300ms p99
Load: 1000 requests/sec

Code: [reference file path or paste code]

Known Issues:
- N+1 query pattern in order items fetch
- No database indexing on foreign keys
- Synchronous external API calls

Question: Identify bottlenecks and prioritized optimization recommendations.

Expected Output: Optimization plan with complexity/impact assessment
EOF
```

**Why this pattern:**
- Performance context with metrics
- Known issues for focused analysis
- Clear optimization criteria

---

### Testing Strategy Review

**Command:**
```bash
cat <<'EOF' | codex exec --sandbox workspace-read
[TESTING STRATEGY REVIEW]

Module: User authentication service
Current Coverage: 60%
Test Types: Unit tests only, no integration tests

Current Tests: [reference or paste sample tests]

Concerns:
- Missing edge cases (password reset, token expiration)
- No integration tests for auth flow
- Brittle mocks for JWT validation

Question: What testing improvements are most valuable?

Expected Output: Prioritized testing improvements with examples
EOF
```

**Why this pattern:**
- Current state context
- Specific concerns identified
- Prioritization requested

---

## Error Handling

### Common Errors

**Error:** `codex: command not found`
**Solution:** Codex CLI not installed. Install via `npm i -g @openai/codex` or `brew install openai/codex/codex`

---

**Error:** `Authentication required`
**Solution:** Sign in with `codex auth login` or provide API key with `codex auth api-key [key]`

---

**Error:** `Rate limit exceeded`
**Solution:** Check status with `/status` in interactive mode, wait for rate limit reset, or upgrade plan

---

**Error:** `Context too large`
**Solution:** Reduce prompt size, use file references instead of pasting code, break into smaller reviews

---

**Error:** `Model not available`
**Solution:** Check available models with `/model`, switch to available model, verify account access

---

### Retry Strategies

**For transient errors (network, timeouts):**
```bash
# Retry with exponential backoff
codex exec "[prompt]" || sleep 2 && codex exec "[prompt]"
```

**For rate limits:**
```bash
# Check status first
codex exec "/status" && codex exec "[prompt]"
```

**For unclear responses:**
```bash
# Reformulate with more specific question
codex exec "[refined prompt with more context]"
```

---

## Best Practices

### 1. Use Non-Interactive Mode for Peer Review

**Recommended:**
```bash
codex exec "[prompt]"
```

**Why:** `exec` subcommand provides non-interactive execution, predictable and scriptable

---

### 2. Use Read-Only Sandbox

**Recommended:**
```bash
codex --sandbox workspace-read "[prompt]"
```

**Why:** Safe for analysis, prevents unintended changes

---

### 3. Structure Prompts with Heredocs

**Recommended:**
```bash
codex exec "$(cat <<'EOF'
[Structured prompt]
...
EOF
)"
```

**Why:** Clean multi-line prompts, easy to maintain

---

### 4. Specify Output Expectations

**Recommended:**
```bash
"... Expected Output: Risk assessment with severity levels and mitigation strategies"
```

**Why:** Codex provides structured, useful responses

---

### 5. Use Images for Visual Architecture

**Recommended:**
```bash
codex --image architecture.png "Analyze this architecture"
```

**Why:** Visual context is often clearer than textual descriptions

---

### 6. Set Appropriate Config Defaults

**Recommended `~/.codex/config.toml`:**
```toml
model = "codex-1"
ask_for_approval = "suggest"
sandbox = "workspace-read"
```

**Why:** Consistent, safe defaults for peer review

---

## Advanced Patterns

### Chaining Reviews

```bash
# First pass: Architecture review
ARCH_REVIEW=$(codex exec --output json "Review architecture: [context]")

# Second pass: Security review of identified concerns
codex exec "Security review focusing on: $ARCH_REVIEW"
```

---

### Parallel Reviews

```bash
# Run multiple reviews in parallel
codex exec "Security review: [code]" > security-review.txt &
codex exec "Performance review: [code]" > performance-review.txt &
wait
cat security-review.txt performance-review.txt
```

---

### Session Resumption

```bash
# Initial review
SESSION_ID=$(codex exec --output json "Review architecture" | jq -r '.session_id')

# Continue review with more details
codex exec --resume $SESSION_ID "Now focus on security concerns"
```

---

## Integration Examples

### CI/CD Pipeline

```bash
#!/bin/bash
# Pre-merge architecture review

echo "Running Codex peer review..."

REVIEW_OUTPUT=$(codex exec --sandbox workspace-read "$(cat <<'EOF'
Review the architecture changes in this PR.

Changes: $(git diff main --name-only)

Focus:
- Breaking changes
- Security implications
- Performance impacts

Expected Output: Risk assessment (HIGH/MEDIUM/LOW) with justification
EOF
)")

echo "$REVIEW_OUTPUT"

# Fail if HIGH risk identified
if echo "$REVIEW_OUTPUT" | grep -q "HIGH"; then
  echo "HIGH risk identified in peer review. Please address before merging."
  exit 1
fi
```

---

### Git Pre-Commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Security review of changed files
CHANGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(ts|js)$')

if [ -n "$CHANGED_FILES" ]; then
  codex exec "Security review these changed files: $CHANGED_FILES" > /tmp/codex-security-review.txt

  if grep -q "CRITICAL\|HIGH" /tmp/codex-security-review.txt; then
    echo "Security concerns identified. Review: /tmp/codex-security-review.txt"
    exit 1
  fi
fi
```

---

### VS Code Integration

```json
{
  "tasks": [
    {
      "label": "Codex Peer Review",
      "type": "shell",
      "command": "codex exec 'Review ${file} for security and performance'",
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
```

---

## Command Quick Reference

| Use Case | Command |
|----------|---------|
| Simple review | `codex exec "Review this code"` |
| Multi-line prompt | `cat <<'EOF' \| codex exec` |
| Review with diagram | `codex --image arch.png "Analyze"` |
| Interactive mode | `codex "question"` |
| JSON output | `codex exec -o json "prompt"` |
| Resume session | `codex exec --resume [id]` |
| Read-only mode | `codex exec --sandbox workspace-read` |

---

This command reference covers the essential Codex CLI commands and patterns for effective peer review workflows.
