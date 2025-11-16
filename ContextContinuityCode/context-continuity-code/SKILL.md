---
name: context-continuity-code
description: Claude Code-optimized context transfer for development workflows. Preserves code context, git state, running services, and development environment when moving work between sessions. Works seamlessly with peer review skills (Codex/Gemini). Use when transferring development work to a new Claude Code session.
---

# Context Continuity - Claude Code Edition

Transfer development context between Claude Code sessions with high fidelity, preserving code state, git context, and running services.

## Core Concept

When development work needs to transfer between Claude Code sessions, this skill creates structured artifacts that capture:

- **Code Context** - Files being worked on, functions/classes modified, pending changes
- **Git State** - Branch, commits, staged/unstaged changes, merge status
- **Environment State** - Running services, ports, environment variables, dependencies
- **Development Decisions** - Technical choices made, alternatives rejected, tradeoffs
- **Open Loops** - What's next, blockers, pending reviews

## When to Use This Skill

Use when you need to:
- Continue development work in a fresh Claude Code session
- Hand off work to another developer (with AI context preserved)
- Resume after context window fills (180K+ tokens)
- Switch between different Claude Code instances
- Document current state before major refactoring
- Prepare for peer review (Codex/Gemini integration)

**DO NOT use for:**
- General conversation summaries (use base context-continuity skill)
- Non-development contexts (writing, research, analysis)
- Simple task handoffs without code changes

## Workflow: Single Mode (Development-Optimized)

This skill uses a **single optimized mode** for development contexts (~400-600 words):

```markdown
═══════════════════════════════════════════════════════════════════
DEV CONTEXT TRANSFER
═══════════════════════════════════════════════════════════════════
Generated: [ISO timestamp] | Session: [ID if available]

**MISSION**: [What we're building/fixing + why it matters]

**STATUS**: [✓ complete | ⧗ in-progress | ⚠ blocked | ↻ iterating]

**PROGRESS**: [High-level summary of work completed this session]

───────────────────────────────────────────────────────────────────
§ CODE CONTEXT
───────────────────────────────────────────────────────────────────

**Active Files**:
- [file:line] - [What changed or what you're working on]
- [file:line] - [Status: implemented | in-progress | pending]

**Key Changes**:
- [Function/class]: [What changed + why]
- [Module/component]: [Refactoring/addition/fix]

**Code State**:
- Modified: [List files with uncommitted changes]
- Created: [New files added]
- Deleted: [Files removed]

───────────────────────────────────────────────────────────────────
§ GIT STATE
───────────────────────────────────────────────────────────────────

**Branch**: [current-branch-name]
**Base**: [main/master/develop]
**Commits**: [X commits ahead of base]

**Recent Commits**:
- [hash] [message]
- [hash] [message]

**Staged**: [Files in staging area | None]
**Unstaged**: [Modified files not staged | None]
**Untracked**: [New files not in git | None]

**Merge Status**: [Clean | Conflicts in X files | Pending PR #XXX]

───────────────────────────────────────────────────────────────────
§ ENVIRONMENT STATE
───────────────────────────────────────────────────────────────────

**Running Services**:
- [Service]: [localhost:PORT] - [Status: healthy | issue]
- [Database]: [postgres:5432] - [State: connected, X records]

**Dependencies**:
- Recently installed: [package@version, ...]
- Pending: [Packages needed but not installed]

**Environment Variables**:
- Critical vars set: [APP_ENV=dev, DATABASE_URL=localhost, ...]
- Missing/needed: [API_KEY (required for testing), ...]

**Terminal State**:
- Active shells: [X terminals open in /path/to/project]
- Background processes: [npm run dev, docker compose up, ...]

───────────────────────────────────────────────────────────────────
§ TECHNICAL DECISIONS
───────────────────────────────────────────────────────────────────

**Decisions Made**:
| Decision | Rationale | Alternatives Rejected | Tradeoff |
|----------|-----------|----------------------|----------|
| [Choice] | [Why] | [What we didn't do] | [Cost we're paying] |

**Architecture Notes**:
- [Pattern/approach chosen]: [Why it fits this context]
- [Constraint observed]: [Technical/business reason]

**Peer Review Integration**:
- Codex consulted: [Yes/No] - [If yes: key recommendations]
- Gemini consulted: [Yes/No] - [If yes: key recommendations]
- Agreements: [Where both AIs aligned]
- Disagreements: [Where perspectives differed + our choice]

───────────────────────────────────────────────────────────────────
§ OPEN LOOPS
───────────────────────────────────────────────────────────────────

**Next Actions**:
- [ ] [Immediate next step - be specific]
- [ ] [Following step]

**Blockers**:
- [What's blocking + why]: [Waiting for X | Need to solve Y]

**Pending**:
- Code review: [PR #XXX awaiting review]
- Testing: [Need to test X scenario]
- Documentation: [Need to update README/docs]

**Questions to Resolve**:
- [ ] [Technical question needing answer]
- [ ] [Design decision pending]

───────────────────────────────────────────────────────────────────
§ TESTING & VALIDATION
───────────────────────────────────────────────────────────────────

**Test Status**:
- Passing: [X/Y tests pass]
- Failing: [Test names that fail + why]
- Coverage: [X% coverage | Not measured]

**Manual Testing Done**:
- [Scenario tested]: [Result]
- [Edge case checked]: [Outcome]

**Still Need to Test**:
- [ ] [Test case pending]
- [ ] [Integration scenario]

───────────────────────────────────────────────────────────────────
§ CONTEXT NOTES
───────────────────────────────────────────────────────────────────

**Key Insights**:
- [Important discovery from this session]
- [Gotcha/caveat to remember]

**Developer Notes**:
- Communication style: [Preferences for next session]
- Assumed knowledge: [What doesn't need re-explaining]
- Sensitive areas: [Code that's fragile, requires care]

**Links/References**:
- Documentation: [URLs to relevant docs]
- Related PRs/Issues: [GitHub links]
- Design docs: [Figma, diagrams, etc.]

═══════════════════════════════════════════════════════════════════
§ TRANSFER READY
═══════════════════════════════════════════════════════════════════
Review for accuracy before sharing. Check git state and file paths.
```

**After generating, ask:**
"Before you transfer—are there any sections that need further detail or refinement?"

---

## Generating the Artifact

### Step 1: Gather Context

**File Context**:
```bash
# Get modified files
git status --short

# Get recent commits
git log --oneline -5

# Check current branch and tracking
git branch -vv

# Show uncommitted changes summary
git diff --stat
git diff --cached --stat
```

**Environment Context**:
```bash
# Check running processes
lsof -i -P -n | grep LISTEN

# Check environment
env | grep -E '(PATH|NODE_ENV|DATABASE|API|APP_)'

# Recent package changes (if applicable)
git log --oneline -10 package.json
```

**Code Context**:
- Note which files have been actively edited
- Identify key functions/classes modified
- Track new files created vs existing files changed

### Step 2: Generate Artifact

Fill out sections systematically:
1. **Mission/Status/Progress** - What and why
2. **Code Context** - What files/functions changed
3. **Git State** - Branch, commits, staging area
4. **Environment State** - Services, dependencies, env vars
5. **Technical Decisions** - Choices made (include peer review input)
6. **Open Loops** - Next actions, blockers
7. **Testing** - What's validated, what's pending
8. **Context Notes** - Insights, gotchas, references

### Step 3: Present & Refine

1. Present artifact in full
2. Add: "§ TRANSFER READY—Review for accuracy before sharing."
3. Ask: "Before you transfer, are there any sections that need further detail or refinement?"
4. Human reviews, requests expansions if needed

### Step 4: Transfer to New Session

**Receiving agent prompt** (optional prepend):
```
[DEV CONTEXT TRANSFER]

The following is a development context transfer from a previous Claude Code session.

After reading, provide a handshake confirmation:

"I've reviewed the dev context. Quick confirmation:
- Mission: [Echo back what we're building]
- Code State: [Active files and key changes]
- Git: [Branch + commit status]
- Next: [Immediate next action]
- Environment: [Critical services/dependencies]

Ready to [next action]. What's your priority?"
```

---

## Integration with Peer Review Skills

When using Codex or Gemini for peer review **during** the development session:

### Before Peer Review

1. Generate a lightweight context artifact (just Code + Git + Technical Decisions sections)
2. Use as input to peer review request
3. Get Codex/Gemini perspective

### After Peer Review

1. Update § Technical Decisions with peer review findings:
   - What Codex/Gemini recommended
   - Where they agreed
   - Where they disagreed
   - Which advice you followed (and why)

2. Include in transfer artifact so receiving agent knows:
   - What external validation was done
   - What technical debates were resolved
   - What alternatives were already considered

### Example Integration

```markdown
§ TECHNICAL DECISIONS

**Decisions Made**:
| Decision | Rationale | Alternatives Rejected | Tradeoff |
|----------|-----------|----------------------|----------|
| Use Redis for session storage | Sub-ms latency required, peer reviews validated | PostgreSQL (too slow), In-memory (no persistence) | Added infrastructure complexity |

**Peer Review Integration**:
- **Codex consulted**: Yes - Recommended Redis over Postgres for session store, flagged potential memory limits
- **Gemini consulted**: Yes - Agreed with Redis choice, suggested Redis Cluster for scaling
- **Agreements**: Both AIs validated Redis for performance needs
- **Disagreements**: Codex suggested 1GB limit, Gemini suggested 2GB - we chose 1.5GB as middle ground
- **Implementation notes**: Added eviction policy (allkeys-lru) based on Codex warning about memory pressure
```

---

## Best Practices

**Do:**
- Run `git status` and `git diff --stat` before generating
- Include specific file paths with line numbers (file.py:123)
- Note running services and their ports
- Capture peer review insights in § Technical Decisions
- Include error messages or test failures verbatim
- Mark files as "in-progress" vs "completed"

**Don't:**
- Include secrets, API keys, credentials (redact them)
- Paste entire file contents (link to files with line ranges)
- Assume receiving agent has access to same environment
- Skip git state (critical for resuming work)
- Forget to note running services (easy to miss)

---

## Examples

See `references/examples.md` for:
- Full-stack feature development handoff
- Bug fix mid-investigation transfer
- Refactoring session continuation
- Code review preparation
- Post-peer-review implementation
- Emergency context capture

---

## Validation

Use the Python validator to check artifact quality:

```bash
python context-continuity-code/scripts/validate_dev_transfer.py artifact.md
```

Checks for:
- Required sections present
- Git state completeness
- File paths formatted correctly
- No secrets leaked
- Peer review integration (if applicable)

---

## Design Principles

**Development-First**: Optimized for code handoffs, not general conversation
**Git-Aware**: Git state is mandatory, not optional
**Tool State Required**: Environment and services are core context
**Peer Review Integration**: First-class support for Codex/Gemini consultation
**Single Mode**: One format optimized for dev workflows (no Minimal/Full choice)
**Antifragile**: Critical info first (Mission → Code → Git → Environment)

---

## Differences from Base Context Continuity

| Feature | Base Skill | Claude Code Edition |
|---------|-----------|---------------------|
| Target | General conversations | Development work only |
| Modes | Minimal + Full | Single optimized mode |
| Tool State | Optional [T] tags | Mandatory §§ sections |
| Git Context | Not included | Required |
| Code Context | Not included | Core feature |
| Peer Review | Not mentioned | Integrated workflow |
| Length | 200-1000 words | 400-600 words |
| Environment | Any Claude instance | Claude Code only |

---

Use this skill when resuming development work. Use base `context-continuity` for general conversations.
