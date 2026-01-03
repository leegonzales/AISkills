# Gemini CLI Command Reference

Complete reference for Gemini CLI commands and flags relevant to peer review workflows.

---

## Overview

Gemini CLI brings Google's Gemini models directly into your terminal for AI-powered peer review. Unlike API-based tools, the CLI provides interactive and non-interactive modes for seamless integration into development workflows.

**Purpose:** Enable automated and interactive peer review through Gemini's powerful models with 1M+ token context windows

**Primary Use Cases:**
- Architecture review and validation
- Security vulnerability analysis
- Design decision evaluation
- Performance bottleneck identification
- Testing strategy assessment
- Code quality review

**Key Differentiators:**
- 1M token context window (swallow entire codebases)
- Multimodal capabilities (images, PDFs, video, audio)
- Google Search grounding for real-time context
- Open source (Apache 2.0)
- Generous free tier (60 req/min, 1,000 req/day)

---

## Installation & Authentication

### Installation

```bash
# Global NPM installation (recommended)
npm install -g @google/gemini-cli

# Homebrew (macOS/Linux)
brew install gemini-cli

# Quick test (no installation)
npx https://github.com/google-gemini/gemini-cli

# Verify installation
gemini --version
```

### Authentication

#### Option 1: Login with Google (Recommended for Individuals)

```bash
# Launch CLI and select "Login with Google"
gemini

# Browser opens for OAuth flow
# No API key management required
```

**Benefits:**
- Free tier: 60 requests/min, 1,000 requests/day
- Access to Gemini 3.0 Pro (1M context)
- No credit card required

---

#### Option 2: Gemini API Key

```bash
# Obtain API key from Google AI Studio
# https://aistudio.google.com/apikey

# Set environment variable
export GEMINI_API_KEY="your-api-key-here"

# Or persist in .gemini/.env
mkdir -p .gemini
cat > .gemini/.env << EOF
GEMINI_API_KEY=your-api-key-here
EOF
```

**Benefits:**
- Free tier: 100 requests/day
- Usage-based billing for higher limits

---

#### Option 3: Vertex AI (Enterprise)

```bash
# Set up Application Default Credentials
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"

# Authenticate
gcloud auth application-default login

# Or use service account
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

**Benefits:**
- Enterprise security
- Higher rate limits
- Pay-as-you-go scaling

---

## Command Basics

### Interactive Mode

**Usage:** `gemini`

**Description:** Launch interactive terminal UI for conversational interaction

```bash
# Start interactive session
gemini

# At gemini> prompt, you can:
gemini> Review the architecture in @./architecture.md
gemini> What security issues exist in @./src/auth/?
gemini> /tools    # List available tools
gemini> /stats    # Show token usage
gemini> /quit     # Exit
```

**Use for peer review:**
- Conversational code exploration
- Iterative refinement
- Follow-up questions
- Deep architectural analysis

---

### Non-Interactive Mode

**Usage:** `gemini -p "prompt"`
**Alias:** `--prompt`

**Description:** One-shot execution with output to stdout

```bash
# Simple query
gemini -p "Review this code for security issues"

# With file reference
gemini -p "Analyze architecture in @./architecture.md"

# Multi-line prompt with heredoc
gemini -p "$(cat <<'EOF'
Review this authentication flow for:
- Security vulnerabilities
- Performance issues
- Best practice violations

Code: @./src/auth/handler.js
EOF
)"
```

**Use for peer review (recommended):**
- Automated workflows
- CI/CD integration
- Scriptable analysis
- Predictable, repeatable reviews

---

### Interactive with Initial Prompt

**Usage:** `gemini -i "prompt"`
**Alias:** `--prompt-interactive`

**Description:** Start interactive session with initial context

```bash
# Start with context
gemini -i "I need help reviewing the microservices architecture"

# Then continue conversation
gemini> Show me service boundaries @./services/
gemini> What are the data consistency risks?
gemini> Recommend improvements
```

---

## Core Commands

### Basic Execution

```bash
# Interactive mode
gemini

# Non-interactive (one-shot)
gemini -p "your prompt here"

# Interactive with initial prompt
gemini -i "initial context prompt"
```

---

### Slash Commands (/)

Available within interactive sessions for session management:

```bash
/help           # Display help
/tools          # List available tools
/settings       # Open settings editor
/stats          # Show token usage
/mcp            # Show MCP server status
/memory show    # Show current memory
/memory add     # Add context to memory
/compress       # Compress conversation to save tokens
/chat save      # Save current conversation
/chat resume    # Resume saved conversation
/quit           # Exit CLI
```

---

### At Commands (@)

File and resource references:

```bash
@path/to/file.txt           # Include file content
@path/to/directory/         # Include directory contents
@image.png                  # Include image
@document.pdf               # Include PDF
@https://url.com            # Fetch URL content
```

---

### Shell Commands (!)

Execute shell commands directly:

```bash
!ls -la                     # Run shell command
!git status                 # Git commands
!npm test                   # Run tests
!                           # Toggle shell mode
```

---

## Key Flags & Options

### Model Selection

```bash
# ALWAYS use --model to ensure latest version
# Use Pro model (best reasoning, complex tasks)
gemini --model gemini-3.0-pro -p "prompt"

# Use Flash model (fast, efficient, recommended)
gemini --model gemini-3.0-flash -p "prompt"

# Use Deep Think (multi-step reasoning, research-grade)
gemini --model gemini-3.0-deep-think -p "prompt"
```

**Model Selection Guide:**
- **Pro (gemini-3.0-pro):** Deep architectural analysis, complex security reviews
- **Flash (gemini-3.0-flash):** Standard code reviews, performance analysis (recommended)
- **Deep Think (gemini-3.0-deep-think):** Multi-step reasoning, research-grade analysis

**IMPORTANT:** Always explicitly specify `--model gemini-3.0-*` to avoid falling back to older 2.5 models.

---

### Output Formats

```bash
# Default text output (human-readable)
gemini -p "analyze architecture"

# JSON output (programmatic parsing)
gemini --output-format json -p "analyze and return structured data"

# Stream JSON (newline-delimited events)
gemini --output-format stream-json -p "process large files"
```

**Recommended for peer review:**
- `text`: Human consumption, manual review
- `json`: Automated processing, CI/CD integration

---

### Execution Modes

```bash
# YOLO mode (auto-approve all tool calls)
gemini --yolo -p "fix bugs and run tests"

# Sandbox mode (safe execution)
gemini --sandbox -p "execute untrusted code"
gemini -s -p "prompt"

# Debug mode
gemini --debug -p "troubleshoot issue"
gemini -d -p "prompt"

# Clean JSON output (for scripting)
gemini -p "prompt" --output-format json
gemini -p "prompt" --output-format stream-json
```

**Recommended for peer review:**
- Avoid `--yolo` for review (use for implementation)
- Use `--sandbox` for untrusted code execution
- Default mode (ask for approval) for transparency

---

### Display Options

```bash
# Markdown style
gemini --style dark -p "prompt"
gemini -t light -p "prompt"
# Options: ascii, dark, light, pink

# Line wrapping
gemini --wrap 100 -p "prompt"
gemini -w 80 -p "prompt"

# Multi-line input
gemini --multiline
```

---

### Session Management

```bash
# Persist session summary
gemini --session-summary -p "prompt"

# Enable checkpointing
gemini --checkpointing -p "prompt"
```

---

### Configuration

```bash
# Custom config file
gemini -c /path/to/config.json -p "prompt"
gemini --config config.json -p "prompt"
```

---

## Available Models

### Gemini 3.0 Pro (`gemini-3.0-pro`)

**Context:** 1,048,576 input tokens / 65,536 output tokens
**Inputs:** Audio, images, video, text, PDF

**Capabilities:**
- Advanced reasoning and thinking
- Code execution
- Function calling
- Structured outputs
- Search grounding
- Context caching
- SWE-bench Verified: 78%+

**Best For:**
- Complex architectural analysis
- Deep security reviews
- Multi-step problem solving
- Large codebase comprehension

**Usage:**
```bash
gemini --model gemini-3.0-pro -p "$(cat <<'EOF'
Perform deep architectural analysis of this microservices system.
Consider:
- Service boundaries and coupling
- Data consistency patterns
- Scalability bottlenecks
- Security boundaries
- Operational complexity

Architecture: @./architecture.md
Services: @./services/
EOF
)"
```

---

### Gemini 3.0 Flash (`gemini-3.0-flash`)

**Context:** 1,048,576 input tokens / 65,536 output tokens
**Inputs:** Text, images, video, audio

**Capabilities:**
- Thinking mode
- Function calling
- Code execution
- File search
- Structured outputs
- Optimized for high-frequency terminal workflows

**Best For:**
- Standard code reviews
- Performance analysis
- Testing strategy review
- Quick architectural assessments

**Usage:**
```bash
gemini --model gemini-3.0-flash -p "$(cat <<'EOF'
Review this code for:
- Security vulnerabilities
- Performance issues
- Best practice violations
- Missing error handling

Code: @./src/payment-processor.js
EOF
)"
```

---

### Gemini 3.0 Deep Think (`gemini-3.0-deep-think`)

**Context:** 1,048,576 input tokens / 65,536 output tokens
**Inputs:** Text, image, video, audio, PDF

**Capabilities:**
- Multi-step reasoning
- Research-grade analysis
- Function calling
- Code execution
- Structured outputs
- Search grounding

**Best For:**
- Novel or unfamiliar patterns
- Research-grade analysis
- Complex trade-off evaluation
- Deep security analysis

**Usage:**
```bash
gemini --model gemini-3.0-deep-think -p "Analyze architectural trade-offs in @./src/"
```

---

## Command Patterns for Peer Review

### Pattern 1: Architecture Review

```bash
gemini --model gemini-3.0-pro -p "$(cat <<'EOF'
[ARCHITECTURE REVIEW]

System: Multi-tenant SaaS Platform
Scale: 100-500 tenants, 50-5K users per tenant
Constraints: Strict tenant data isolation required

Architecture:
@./architecture.md

Focus Areas:
- Service boundaries and dependencies
- Data consistency approach
- Scalability bottlenecks
- Security boundaries (tenant isolation)
- Operational complexity
- Failure modes and recovery

Question: Provide comprehensive risk assessment with improvement recommendations.

Expected Output:
1. Risk Level (CRITICAL/HIGH/MEDIUM/LOW)
2. Key Concerns (with severity)
3. Recommendations (prioritized by impact)
4. Trade-offs to consider
EOF
)"
```

**Why this pattern:**
- Pro model for complex reasoning
- Structured prompt with context
- Clear focus areas
- Expected output format

---

### Pattern 2: Architecture Review with Diagram

```bash
gemini --model gemini-3.0-pro -p "$(cat <<'EOF'
Analyze the attached architecture diagram.

Context:
- E-commerce platform
- 100K daily active users
- High availability requirements (99.9% uptime)
- Payment processing critical path

Diagram: @./architecture-diagram.png
Code: @./services/

Questions:
1. Single points of failure?
2. Scalability bottlenecks?
3. Data consistency issues?
4. Security vulnerabilities?

Expected Output: Risk assessment with specific recommendations
EOF
)"
```

**Why this pattern:**
- Multimodal analysis (diagram + code)
- Specific questions for focus
- Business context included

---

### Pattern 3: Security Review

```bash
gemini --model gemini-3.0-flash -p "$(cat <<'EOF'
[SECURITY REVIEW]

Threat Model:
- SQL Injection
- Authentication bypass
- Session fixation
- XSS attacks
- Sensitive data exposure
- Timing attacks

Code to Review:
@./src/auth/login-handler.js
@./src/auth/session-manager.js

Question: Identify all security vulnerabilities with OWASP classification.

Expected Output:
1. Vulnerability Summary (count by severity)
2. Detailed Findings (CRITICAL first)
   - OWASP category
   - Severity level
   - Exploit scenario
   - Remediation steps with code examples
3. Security Best Practices Recommendations

Prioritize by severity and exploitability.
EOF
)"
```

**Why this pattern:**
- Flash model (sufficient for security analysis)
- Explicit threat model
- OWASP framework for structure
- Code examples requested

---

### Pattern 4: Performance Analysis

```bash
gemini --model gemini-3.0-flash -p "$(cat <<'EOF'
[PERFORMANCE ANALYSIS]

Current Performance:
- Latency avg: 500ms
- Latency p99: 2s
- Throughput: 100 req/s

Target Performance:
- Latency avg: 100ms
- Latency p99: 300ms
- Throughput: 500 req/s

Context: 1000 concurrent users, average 5 orders per user

Code:
@./src/api/order-handler.ts

Known Issues:
- N+1 query pattern in order items fetch
- No database indexing on foreign keys
- Synchronous external API calls

Question: Identify performance bottlenecks and provide optimization recommendations.

Expected Output:
For each optimization:
- Bottleneck identified
- Expected performance improvement
- Implementation effort (LOW/MEDIUM/HIGH)
- Code example
- Potential trade-offs

Prioritize by impact/effort ratio.
EOF
)"
```

**Why this pattern:**
- Current vs target metrics
- Known issues for context
- Impact/effort prioritization
- Code examples requested

---

### Pattern 5: Design Decision Evaluation

```bash
gemini --model gemini-3.0-pro -p "$(cat <<'EOF'
[DESIGN DECISION EVALUATION]

Decision: Caching strategy for product catalog

Option A: Redis with TTL-based invalidation
Pros: Fast, simple, horizontally scalable
Cons: Stale data risk, invalidation complexity

Option B: Event-driven cache invalidation
Pros: Always fresh data, precise control
Cons: Complex implementation, event overhead

Option C: Hybrid (Redis + event invalidation)
Pros: Fast + fresh, best of both worlds
Cons: Most complex, higher operational overhead

Evaluation Criteria (in priority order):
1. Data freshness
2. Query performance
3. Implementation complexity
4. Operational overhead
5. Team familiarity

Context:
- 10K product SKUs
- Updates 100x/day
- Read-heavy (1M reads/day)
- Team familiar with Redis, less with event streaming
- Must support real-time inventory updates

Question: Which option is recommended? What are the critical trade-offs?

Expected Output:
1. Option Comparison Matrix
2. Criterion-by-Criterion Analysis
3. Recommendation with Rationale
4. Implementation Considerations
5. Decision Risks (what could go wrong)
EOF
)"
```

**Why this pattern:**
- Pro model for comparative reasoning
- Structured options with pros/cons
- Prioritized criteria
- Business context and constraints

---

### Pattern 6: Testing Strategy Review

```bash
gemini --model gemini-3.0-flash -p "$(cat <<'EOF'
[TESTING STRATEGY REVIEW]

Module: User authentication service
Current Coverage: 60%
Test Types: Unit tests only, no integration tests

Sample Tests:
@./tests/auth/login.test.js

Known Concerns:
- Missing edge cases (password reset, token expiration)
- No integration tests for full auth flow
- Brittle mocks for JWT validation
- No security testing (brute force, timing attacks)
- Missing error path testing

Question: What testing improvements are most valuable?

Expected Output:
1. Coverage Assessment
2. Missing Test Scenarios (prioritized by risk)
3. Test Quality Issues
4. Recommended Improvements with examples
5. Testing Best Practices

Provide specific test examples for top 3 improvements.
EOF
)"
```

**Why this pattern:**
- Flash model (sufficient for testing review)
- Current state assessment
- Specific concerns identified
- Prioritization by risk

---

### Pattern 7: Code Review

```bash
gemini --model gemini-3.0-flash -p "$(cat <<'EOF'
[CODE REVIEW - JavaScript]

Focus Areas:
- Security vulnerabilities
- Performance issues
- Error handling
- Code style and maintainability
- Best practices (async/await, null checks)

Style Guide:
- Use async/await (no callbacks)
- Explicit error handling
- Input validation required
- No SQL string concatenation

Code:
@./src/api/user-handler.js
@./src/api/order-handler.js

Question: Provide comprehensive code review.

Expected Output:
1. Summary (overall quality assessment)
2. Issues (categorized: CRITICAL, MAJOR, MINOR)
   - Severity
   - Description
   - Line number if applicable
   - Suggested fix with code example
3. Positive Observations
4. Refactoring Opportunities

Highlight what the code does well.
EOF
)"
```

**Why this pattern:**
- Flash model (efficient for code review)
- Clear focus areas
- Style guide for consistency
- Balanced feedback (positive + negative)

---

## Error Handling

### Common Errors

#### Authentication Required

```bash
# Error: "Authentication required"
# Solution: Sign in
gemini  # Select login method from menu
```

---

#### Rate Limit Exceeded

```bash
# Check usage
gemini
gemini> /stats

# Shows:
# Token usage: 45,234 / 1,000,000
# Requests: 58 / 60 per minute
# Daily quota: 234 / 1,000

# Wait for rate limit reset or upgrade plan
```

---

#### Context Too Large

```bash
# Error: "Context exceeds limit"
# Solution: Compress conversation or reduce files
gemini
gemini> /compress

# Or be more specific
gemini -p "Review only @./src/auth/login.js (not entire directory)"
```

---

#### Model Not Available

```bash
# Error: "Model not available"
# Solution: Check available models
gemini
gemini> /settings

# Switch to available model
gemini --model gemini-3.0-flash -p "prompt"
```

---

### Retry Strategies

```bash
# For transient errors (network, timeouts)
gemini -p "prompt" || sleep 2 && gemini -p "prompt"

# For rate limits
# Check status first
gemini
gemini> /stats
# Then retry after cooldown

# For unclear responses
# Reformulate with more specific question
gemini -p "$(cat <<'EOF'
[More specific prompt with additional context]
EOF
)"
```

---

## Best Practices

### 1. Use Non-Interactive Mode for Automation

**Recommended:**
```bash
gemini -p "prompt"
```

**Why:** Predictable, scriptable, suitable for CI/CD

---

### 2. Structure Prompts with Heredocs

**Recommended:**
```bash
gemini -p "$(cat <<'EOF'
[Structured multi-line prompt]
...
EOF
)"
```

**Why:** Clean multi-line prompts, easy to maintain, proper escaping

---

### 3. Specify Output Expectations

**Recommended:**
```bash
"... Expected Output: Risk assessment with severity levels and mitigation strategies"
```

**Why:** Gemini provides structured, actionable responses

---

### 4. Use Flash for Most Peer Reviews

**Recommended:**
```bash
gemini --model gemini-3.0-flash -p "standard review prompt"
```

**Why:** Same 1M context, faster, more cost-efficient than Pro

**Use Pro for:**
- Complex architectural analysis
- Multi-step reasoning
- Deep security reviews

---

### 5. Leverage Multimodal Capabilities

**Recommended:**
```bash
gemini -p "Analyze architecture: @./diagram.png @./architecture.md"
```

**Why:** Visual context often clearer than text descriptions

---

### 6. Monitor Token Usage

```bash
# Check usage regularly
gemini
gemini> /stats

# Compress to save tokens
gemini> /compress

# Use .geminiignore
cat > .geminiignore << EOF
node_modules/
dist/
build/
*.min.js
docs/
EOF
```

---

### 7. Use Sandbox for Untrusted Code

```bash
# Safe execution
gemini --sandbox -p "execute and test this code"
gemini -s -p "prompt"
```

**Why:** Prevents unintended system modifications

---

### 8. Set Up Project Context

```bash
# Create GEMINI.md in project root
cat > GEMINI.md << 'EOF'
# Project: Multi-Tenant SaaS Platform

## Architecture
- Microservices (Node.js, Go, Python)
- PostgreSQL with RLS for multi-tenancy
- Redis for caching
- BullMQ for background jobs

## Code Style
- TypeScript strict mode
- Functional patterns preferred
- Jest for testing
- ESLint + Prettier

## Key Decisions
- Multi-tenancy via RLS (see ADR-001)
- JWT authentication (see ADR-002)
EOF

# Gemini automatically reads GEMINI.md for context
```

---

## Integration Examples

### CI/CD Pipeline (GitHub Actions)

```yaml
name: Gemini Peer Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Gemini CLI
        run: npm install -g @google/gemini-cli

      - name: Architecture Review
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: |
          REVIEW=$(gemini -p "$(cat <<'EOF'
          Review architecture changes in this PR.

          Changed files: $(git diff origin/main --name-only)

          Focus:
          - Breaking changes
          - Security implications
          - Performance impacts

          Expected Output: Risk level (HIGH/MEDIUM/LOW) with justification
          EOF
          )")

          echo "$REVIEW"

          # Fail if HIGH risk
          if echo "$REVIEW" | grep -q "HIGH"; then
            echo "HIGH risk identified. Review required."
            exit 1
          fi
```

---

### Git Pre-Commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Security review of staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|ts|py)$')

if [ -n "$STAGED_FILES" ]; then
  echo "Running security review..."

  REVIEW=$(gemini -p "$(cat <<EOF
Security review of staged files:

$(for file in $STAGED_FILES; do
  echo "- @./$file"
done)

Focus on CRITICAL and HIGH severity issues only.
Expected Output: List of security issues or "No issues found"
EOF
)")

  echo "$REVIEW"

  if echo "$REVIEW" | grep -q "CRITICAL\|HIGH"; then
    echo ""
    echo "Security concerns identified. Review output above."
    echo "To commit anyway, use: git commit --no-verify"
    exit 1
  fi
fi

echo "Security review passed."
```

---

### Bash Script for Batch Review

```bash
#!/bin/bash
# review-all.sh - Batch review all services

SERVICES=(
  "api-gateway"
  "auth-service"
  "user-service"
  "order-service"
)

for service in "${SERVICES[@]}"; do
  echo "Reviewing $service..."

  gemini --model gemini-3.0-flash -p "$(cat <<EOF
Review service: $service

Code: @./services/$service/

Focus:
- Security vulnerabilities
- Performance issues
- Best practice violations

Expected Output: Summary with risk level
EOF
)" > "reviews/$service-review.txt"

  echo "Review saved to reviews/$service-review.txt"
done

echo "All reviews complete."
```

---

### VS Code Task

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Gemini Peer Review",
      "type": "shell",
      "command": "gemini",
      "args": [
        "-p",
        "Review ${file} for security and performance issues. Expected Output: List of issues with severity levels."
      ],
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    },
    {
      "label": "Gemini Architecture Review",
      "type": "shell",
      "command": "gemini",
      "args": [
        "--model",
        "gemini-3.0-pro",
        "-p",
        "Comprehensive architecture review of entire project. Focus on scalability, security, maintainability."
      ],
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

## Quick Reference

### Command Quick Reference

| Use Case | Command | Key Flags |
|----------|---------|-----------|
| Architecture review | `gemini -p "[context]"` | `--model gemini-3.0-pro` |
| Review with diagram | `gemini -p "analyze: @diagram.png"` | None (multimodal) |
| Security review | `gemini -p "[threat model + code]"` | `--model gemini-3.0-flash` |
| Performance analysis | `gemini -p "[metrics + code]"` | `--model gemini-3.0-flash` |
| Design comparison | `gemini -p "[options + criteria]"` | `--model gemini-3.0-pro` |
| Testing strategy | `gemini -p "[coverage + concerns]"` | `--model gemini-3.0-flash` |
| Code review | `gemini -p "[focus areas + code]"` | `--model gemini-3.0-flash` |
| Interactive exploration | `gemini` | None (interactive) |
| JSON output | `gemini --output-format json -p "[prompt]"` | `--output-format json` |
| Sandbox execution | `gemini --sandbox -p "[prompt]"` | `--sandbox` or `-s` |

---

### Flag Quick Reference

| Flag | Short | Description | Recommended Use |
|------|-------|-------------|----------------|
| `--prompt` | `-p` | Non-interactive mode | Automation, CI/CD |
| `--prompt-interactive` | `-i` | Start interactive with context | Conversational review |
| `--model` | None | Select model | Pro for complex, Flash for standard |
| `--output-format` | None | json, stream-json, text | JSON for automation |
| `--sandbox` | `-s` | Safe execution mode | Untrusted code |
| `--yolo` | None | Auto-approve tools | Implementation (not review) |
| `--debug` | `-d` | Debug mode | Troubleshooting |
| `--output-format` | None | Control output (text/json/stream-json) | Scripts, parsing |
| `--style` | `-t` | Markdown style | Visual preference |
| `--wrap` | `-w` | Line wrapping | Readability |

---

### Slash Command Quick Reference

| Command | Description | Use Case |
|---------|-------------|----------|
| `/help` | Show help | Learn commands |
| `/tools` | List available tools | See capabilities |
| `/stats` | Show token usage | Monitor quota |
| `/settings` | Open settings | Configure model, etc. |
| `/mcp` | Show MCP server status | Check integrations |
| `/memory show` | Show current memory | View context |
| `/compress` | Compress conversation | Save tokens |
| `/chat save` | Save conversation | Resume later |
| `/quit` | Exit CLI | End session |

---

This command reference provides comprehensive guidance for using Gemini CLI in peer review workflows through direct CLI invocation rather than API calls.
