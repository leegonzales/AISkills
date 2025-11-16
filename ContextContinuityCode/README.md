# Context Continuity - Claude Code Edition

**🖥️ Claude Code Only** - Optimized context transfer for development workflows

High-fidelity development context transfer between Claude Code sessions. Preserves code state, git context, running services, and technical decisions when moving work between sessions.

---

## What It Does

When you need to continue development work in a fresh Claude Code session, this skill creates structured artifacts that capture:

- **Code Context** - Files modified, functions changed, pending work
- **Git State** - Branch, commits, staged/unstaged changes
- **Environment** - Running services, dependencies, environment variables
- **Technical Decisions** - Choices made, alternatives rejected, peer review input
- **Open Loops** - Next actions, blockers, pending tests

---

## Key Features

### Development-Optimized Structure

Single mode (~400-600 words) focused on dev contexts:
- § Code Context - Active files and changes
- § Git State - Branch, commits, staging area
- § Environment State - Services, deps, env vars
- § Technical Decisions - With peer review integration
- § Open Loops - Next actions and blockers
- § Testing & Validation - Test status and coverage

### Peer Review Integration

First-class support for Codex and Gemini peer review skills:
```markdown
§ TECHNICAL DECISIONS

**Peer Review Integration**:
- Codex consulted: Yes - Recommended Redis, flagged memory limits
- Gemini consulted: Yes - Suggested Redis Cluster for scaling
- Agreements: Both validated Redis for performance
- Disagreements: Memory limits (1GB vs 2GB) - chose 1.5GB
```

### Git-Aware

Captures complete git state:
- Current branch and base branch
- Recent commits
- Staged/unstaged/untracked files
- Merge status and conflicts

### Environment Tracking

Documents running development environment:
- Running services and ports
- Database connections and state
- Environment variables
- Background processes

---

## Installation

### Claude Code

```bash
# Navigate to your skills directory
cd ~/.claude/skills/

# Clone the entire repo
git clone https://github.com/leegonzales/AISkills.git

# Copy the skill
cp -r AISkills/ContextContinuityCode/context-continuity-code ./

# Or install project-specific
cd your-project/.claude/skills/
cp -r /path/to/AISkills/ContextContinuityCode/context-continuity-code ./
```

**⚠️ Not available for Claude web chat** - This skill requires Claude Code's terminal access for git commands and environment inspection.

---

## Usage

### Basic Transfer

Simply say:
```
"Transfer this development context to another session"
"Create a dev handoff artifact"
"I need to continue this work in a fresh Claude Code session"
```

Claude will:
1. Run `git status` and `git diff` to capture changes
2. Check running services and environment
3. Generate structured dev context artifact
4. Ask if any sections need refinement

### With Peer Review

When you've used Codex or Gemini for peer review:
```
"Create a dev transfer including the Codex review we just did"
"Transfer context - include Gemini's architecture feedback"
```

The artifact will capture:
- What peer review was done
- Key recommendations from each AI
- Where they agreed/disagreed
- Which advice you followed

### Resuming in New Session

1. Copy the artifact
2. Start new Claude Code session
3. Paste artifact
4. Claude will confirm understanding:

```
I've reviewed the dev context. Quick confirmation:
- Mission: Building OAuth2 refresh token mechanism
- Code State: auth.js:145-180 modified, tests pending
- Git: feature/refresh-tokens, 3 commits ahead of main
- Next: Implement token rotation logic
- Environment: Redis running on :6379, test DB populated

Ready to implement token rotation. What's your priority?
```

---

## Examples

### Example 1: Full-Stack Feature Mid-Development

```markdown
**MISSION**: Add real-time notification system using WebSockets

**STATUS**: ⧗ in-progress

§ CODE CONTEXT
**Active Files**:
- server/websocket.js:1-150 - WebSocket server implemented
- client/useNotifications.js:20-45 - React hook in-progress
- server/notifications.test.js:10-50 - Tests passing for server

**Key Changes**:
- WebSocketServer class: Connection pooling, auth verification
- useNotifications hook: Partial implementation (connect/disconnect done)

**Code State**:
- Modified: server/websocket.js, client/useNotifications.js
- Created: server/notifications.test.js
- Deleted: None

§ GIT STATE
**Branch**: feature/websocket-notifications
**Base**: main
**Commits**: 2 commits ahead

**Recent Commits**:
- a1b2c3d Add WebSocket server with connection pooling
- d4e5f6g Start React useNotifications hook

**Staged**: server/websocket.js
**Unstaged**: client/useNotifications.js (still editing)
**Untracked**: None

§ ENVIRONMENT STATE
**Running Services**:
- Node server: localhost:3000 - healthy
- Redis: localhost:6379 - connected, storing connection pool
- WebSocket: ws://localhost:8080 - accepting connections

**Dependencies**:
- Recently installed: ws@8.13.0, ioredis@5.3.2
- Pending: None

§ TECHNICAL DECISIONS
| Decision | Rationale | Alternatives Rejected | Tradeoff |
|----------|-----------|----------------------|----------|
| Use Redis for connection pool | Need shared state across instances | In-memory (doesn't scale) | Added Redis dependency |
| WebSocket over Server-Sent Events | Need bidirectional for acks | SSE (unidirectional only) | More complex protocol |

**Peer Review Integration**:
- Codex consulted: Yes - Validated Redis for scaling, suggested connection limits
- Gemini consulted: No
- Implementation notes: Added max 10K connections per instance per Codex

§ OPEN LOOPS
**Next Actions**:
- [ ] Finish useNotifications hook (subscribe/unsubscribe methods)
- [ ] Add error handling and reconnection logic
- [ ] Write integration tests for client hook

**Blockers**: None

**Pending**:
- Testing: Need to test reconnection scenarios
- Documentation: Add WebSocket API docs to README

§ TESTING & VALIDATION
**Test Status**:
- Passing: 5/5 server tests pass
- Failing: None
- Coverage: 85% server coverage, 0% client (not written yet)

**Still Need to Test**:
- [ ] Client reconnection after disconnect
- [ ] Connection pooling under load
```

### Example 2: Bug Fix Investigation

```markdown
**MISSION**: Fix memory leak in image processing pipeline

**STATUS**: ⧗ in-progress - Leak source identified, fix pending

§ CODE CONTEXT
**Active Files**:
- lib/imageProcessor.js:78-95 - Memory leak identified here
- tests/imageProcessor.test.js:120-140 - Added leak detection test

**Key Changes**:
- ImageProcessor.process(): Found buffer not being released
- Added test that fails after 100 iterations (heap grows 500MB)

**Code State**:
- Modified: lib/imageProcessor.js (added debug logging)
- Created: tests/leak-detection.test.js
- Deleted: None

§ GIT STATE
**Branch**: bugfix/image-memory-leak
**Base**: main
**Commits**: 1 commit ahead

**Recent Commits**:
- 7g8h9i Add failing test demonstrating memory leak

**Staged**: tests/leak-detection.test.js
**Unstaged**: lib/imageProcessor.js (debugging in progress)

§ TECHNICAL DECISIONS
| Decision | Rationale | Alternatives Rejected | Tradeoff |
|----------|-----------|----------------------|----------|
| Use node --expose-gc for testing | Need to force GC to confirm leak | Rely on auto GC (unreliable) | Test requires flag |

**Peer Review Integration**:
- Codex consulted: Yes - Identified buffer.slice() creating copy, suggested subarray()
- Gemini consulted: Yes - Confirmed Codex diagnosis, suggested WeakMap for tracking
- Agreements: Both identified buffer.slice() as culprit
- Our choice: Will use subarray() + explicit null after processing (Codex suggestion)

§ OPEN LOOPS
**Next Actions**:
- [ ] Replace buffer.slice() with buffer.subarray() at line 82
- [ ] Add explicit buffer = null after processing
- [ ] Re-run leak detection test to confirm fix
- [ ] Add regression test to CI

**Blockers**: None

§ TESTING & VALIDATION
**Test Status**:
- Passing: 15/16 tests pass
- Failing: leak-detection.test.js (expected - demonstrating bug)
- Coverage: 92%

**Manual Testing Done**:
- Heap profiling: Confirmed 500MB leak after 100 iterations
- Chrome DevTools: Buffer count grows linearly

**Still Need to Test**:
- [ ] Leak fixed (heap stays flat after 1000 iterations)
- [ ] Performance impact of subarray() vs slice()
```

---

## Peer Review Workflow

### Before Consulting Peer Review

1. Generate lightweight context (Code + Git + Decisions)
2. Use as context for peer review request:
   ```
   "Review this authentication implementation [paste context]"
   ```

### After Peer Review

Update the transfer artifact with findings:
```markdown
§ TECHNICAL DECISIONS

**Peer Review Integration**:
- **Codex consulted**: Yes - Validated approach, flagged SQL injection risk in line 45
- **Gemini consulted**: Yes - Suggested parameterized queries, validated overall design
- **Agreements**: Both identified SQL injection vulnerability
- **Disagreements**: None
- **Actions taken**: Switched to parameterized queries (line 45-52 refactored)
```

---

## Validation

Validate your artifact before transfer:

```bash
# Check artifact quality
python context-continuity-code/scripts/validate_dev_transfer.py my-artifact.md

# Checks for:
# - Required sections present
# - Git state completeness
# - File paths formatted correctly
# - No secrets/credentials leaked
```

---

## Best Practices

**Before Generating:**
```bash
# Get fresh git state
git status

# Check environment
lsof -i -P -n | grep LISTEN
env | grep -E '(DATABASE|API|APP_)'

# Review recent changes
git diff --stat
git log --oneline -5
```

**When Generating:**
- Include specific file:line references (auth.js:145)
- Note ALL running services and ports
- Capture peer review insights if consulted
- Mark work status: completed vs in-progress vs pending
- Redact secrets/API keys

**When Receiving:**
- Wait for handshake confirmation before continuing
- Verify git branch matches
- Check environment requirements
- Ask about missing context before starting

---

## Differences from Base Context Continuity

| Feature | Base Skill | Code Edition |
|---------|-----------|--------------|
| **Target** | Any conversations | Development only |
| **Modes** | Minimal + Full | Single dev mode |
| **Tool State** | Optional | Mandatory |
| **Git** | Not included | Required |
| **Code Context** | Not included | Core feature |
| **Peer Review** | Not mentioned | Integrated |
| **Environment** | Any Claude | Claude Code only |

**Use base `context-continuity` for:**
- General conversations
- Writing projects
- Research and analysis
- Non-code discussions

**Use `context-continuity-code` for:**
- Active development work
- Bug fixes in progress
- Feature implementation
- Refactoring sessions
- Post-peer-review work

---

## Requirements

- **Claude Code** environment (requires terminal access)
- **Git** repository (skill runs git commands)
- Development project with code being modified

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0.0 | 2025-11-16 | Initial release - dev-optimized context transfer |

---

## Questions?

- **Usage**: See examples above
- **Base skill**: See [Context Continuity](../ContextContinuity/)
- **Peer Review**: See [Codex Peer Review](../CodexPeerReview/) and [Gemini Peer Review](../GeminiPeerReview/)

Built with Claude Code | Optimized for Development Workflows
