# Multiagent Review — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a `/multiagent-review` skill that fans out to 5-8 parallel reviewers (Codex CLI, Gemini CLI, specialist Claude agents) on PRs, code, designs, or writing.

**Architecture:** Single SKILL.md orchestrates content detection → language detection → prompt template selection → parallel dispatch via Task tool → delivery (line-level PR comments or inline synthesis). Specialist agents are standalone .md files, 3 symlinked to ECC, 3 owned.

**Tech Stack:** Claude Code skills, Task tool for parallel dispatch, `gh` CLI, `codex` CLI, `gemini` CLI, Devon's `post-line-comment.sh`

**Design doc:** `docs/plans/2026-03-08-multiagent-review-design.md`

---

## Task 1: Create skill directory structure and symlinks

**Parallelizable:** Yes (independent of all other tasks)

**Files:**
- Create: `~/.claude/skills/multiagent-review/`
- Create: `~/.claude/skills/multiagent-review/agents/`
- Create: `~/.claude/skills/multiagent-review/references/`
- Symlink: `agents/python-reviewer.md` → `~/Projects/leegonzales/everything-claude-code/agents/python-reviewer.md`
- Symlink: `agents/go-reviewer.md` → `~/Projects/leegonzales/everything-claude-code/agents/go-reviewer.md`
- Symlink: `agents/architecture-reviewer.md` → `~/Projects/leegonzales/everything-claude-code/agents/architect.md`

**Steps:**

```bash
mkdir -p ~/.claude/skills/multiagent-review/agents
mkdir -p ~/.claude/skills/multiagent-review/references

ln -s ~/Projects/leegonzales/everything-claude-code/agents/python-reviewer.md \
      ~/.claude/skills/multiagent-review/agents/python-reviewer.md

ln -s ~/Projects/leegonzales/everything-claude-code/agents/go-reviewer.md \
      ~/.claude/skills/multiagent-review/agents/go-reviewer.md

ln -s ~/Projects/leegonzales/everything-claude-code/agents/architect.md \
      ~/.claude/skills/multiagent-review/agents/architecture-reviewer.md
```

**Verify:** `ls -la ~/.claude/skills/multiagent-review/agents/` — should show 3 symlinks pointing to ECC.

---

## Task 2: Write the TypeScript/JS reviewer agent

**Parallelizable:** Yes (independent)

**Files:**
- Create: `~/.claude/skills/multiagent-review/agents/typescript-reviewer.md`
- Reference: `~/Projects/leegonzales/everything-claude-code/agents/code-reviewer.md` (adapt from this)

**Instructions:**

Adapt ECC's `code-reviewer.md` into a TypeScript/JavaScript specialist. The ECC code-reviewer already has strong TS/React/Next.js/Node.js coverage — extract and sharpen those sections. Add:

YAML frontmatter:
```yaml
name: typescript-reviewer
description: Expert TypeScript/JavaScript code reviewer specializing in strict typing, React/Next.js patterns, Node.js best practices, and frontend security
tools: ["Read", "Grep", "Glob", "Bash"]
model: sonnet
```

Review priorities (adapt from ECC code-reviewer):
- CRITICAL: Security (XSS, injection, CSRF, auth bypass, exposed secrets), strict null violations, `any` type escape hatches
- HIGH: React patterns (missing dependency arrays, stale closures, prop drilling, missing error boundaries, server/client boundary violations), type narrowing gaps, missing discriminated unions, Node.js (unvalidated input, unbounded queries, N+1, missing timeouts)
- MEDIUM: Performance (unnecessary re-renders, large bundles, missing code splitting, synchronous I/O), missing generics where appropriate, inconsistent error handling patterns
- LOW: Naming, formatting, TODO without tickets

Diagnostic commands: `tsc --noEmit`, `eslint .`, `prettier --check .`

Approval criteria: Same pattern as ECC (Approve/Warning/Block based on severity)

Output format: `[SEVERITY] Issue title` + `File:line` + description + fix suggestion

---

## Task 3: Write the Rust reviewer agent

**Parallelizable:** Yes (independent)

**Files:**
- Create: `~/.claude/skills/multiagent-review/agents/rust-reviewer.md`
- Reference: `~/Projects/leegonzales/everything-claude-code/agents/go-reviewer.md` (model structure on this)

**Instructions:**

Create a Rust specialist modeled on ECC's `go-reviewer.md` structure.

YAML frontmatter:
```yaml
name: rust-reviewer
description: Expert Rust code reviewer specializing in ownership/borrowing, unsafe code auditing, error handling patterns, and performance
tools: ["Read", "Grep", "Glob", "Bash"]
model: sonnet
```

Review priorities:
- CRITICAL: Security (unsafe blocks without safety comments, raw pointer derefs, FFI boundary issues, unchecked indexing, command injection via std::process, path traversal, hardcoded secrets), ownership (use-after-move, dangling references)
- HIGH: Error handling (unwrap/expect in library code, missing From impls for error types, panic in non-test code, Result ignored), lifetime issues (unnecessary lifetime annotations, 'static abuse, self-referential structs), concurrency (data races via unsafe, deadlock patterns, Send/Sync violations, Arc<Mutex> vs channel choice)
- MEDIUM: Performance (unnecessary clones, Box vs stack allocation, iterator vs loop, string allocation patterns, missing #[inline] on hot paths), idiomatic patterns (builder pattern, newtype pattern, From/Into implementations, proper trait bounds)
- LOW: Naming conventions (snake_case), clippy lints, documentation

Diagnostic commands: `cargo clippy -- -W clippy::all`, `cargo audit`, `cargo test`, `cargo fmt --check`

Approval criteria: Same pattern (Approve/Warning/Block)

Output format: `[SEVERITY] Issue title` + `File:line` + description + fix suggestion

---

## Task 4: Write the security reviewer agent

**Parallelizable:** Yes (independent)

**Files:**
- Create: `~/.claude/skills/multiagent-review/agents/security-reviewer.md`
- Reference: `~/Projects/leegonzales/everything-claude-code/agents/security-reviewer.md` (base)
- Reference: Trail of Bits skills at `https://github.com/trailofbits/skills` (enhance with their methodology)

**Instructions:**

Create a multi-language security reviewer. ECC's version is JS/npm-centric. Broaden to cover Python, Go, Rust, TypeScript.

YAML frontmatter:
```yaml
name: security-reviewer
description: Security vulnerability detection specialist. OWASP Top 10, secrets detection, input validation, auth/authz across Python, TypeScript, Go, and Rust.
tools: ["Read", "Grep", "Glob", "Bash"]
model: sonnet
```

Structure:
1. **Initial scan** — language-aware tooling:
   - Python: `bandit -r .`, `pip audit`, `safety check`
   - TypeScript/JS: `npm audit --audit-level=high`, `eslint-plugin-security`
   - Go: `govulncheck ./...`, `go vet`
   - Rust: `cargo audit`, `cargo clippy -- -W clippy::all`
   - All: grep for hardcoded secrets patterns (API keys, tokens, private keys)

2. **OWASP Top 10 check** — full checklist from ECC's version but with multi-language examples

3. **Trail of Bits methodology** — add:
   - Blast radius estimation (what's the worst case if this vulnerability is exploited?)
   - Trust boundary analysis (where does trusted input become untrusted?)
   - Cross-function call flow tracking (does tainted input flow to a sink?)
   - First principles: "Assume the attacker controls all input"

4. **Threat modeling for designs** — when reviewing design docs instead of code:
   - Attack surface enumeration
   - Data flow diagram analysis
   - Trust boundary identification
   - STRIDE threat categorization

Common false positives, emergency response protocol, and approval criteria from ECC version.

---

## Task 5: Write the dispatch matrix reference

**Parallelizable:** Yes (independent)

**Files:**
- Create: `~/.claude/skills/multiagent-review/references/dispatch-matrix.md`

**Instructions:**

This file contains the actual prompt templates the SKILL.md references when dispatching each reviewer. One section per reviewer, one subsection per content type.

Structure for each reviewer section:
```markdown
## [Reviewer Name]

### PR Mode
[Full prompt template with placeholders for {diff}, {pr_number}, {file_list}]

### Code Mode
[Full prompt template with placeholders for {code}, {file_paths}]

### Design Mode
[Full prompt template with placeholders for {document}]

### Writing Mode
[Full prompt template with placeholders for {document}]
(or "Skip — not applicable for this reviewer")
```

Reviewers to cover:
1. Codex CLI (all 4 modes)
2. Gemini CLI (all 4 modes)
3. Security Agent (PR/Code/Design, skip Writing)
4. Architecture Agent (PR/Code/Design, skip Writing)
5. Python Reviewer (PR/Code only)
6. TypeScript/JS Reviewer (PR/Code only)
7. Go Reviewer (PR/Code only)
8. Rust Reviewer (PR/Code only)
9. Prose-Polish (Writing/Design only)

Each prompt template must:
- State the reviewer's role and expertise area
- Specify the output format (`file:line: [SEVERITY] description` for code, structured sections for design/writing)
- Include the content to review via placeholder
- Be specific enough that the reviewer stays in their lane
- For PR mode: instruct to output findings that can be parsed for `post-line-comment.sh`

---

## Task 6: Write the SKILL.md orchestrator

**Parallelizable:** No — depends on Tasks 1-5 being complete (needs to reference agent files and dispatch matrix)

**Files:**
- Create: `~/.claude/skills/multiagent-review/SKILL.md`

**Instructions:**

This is the main skill file. It must contain:

### Frontmatter
```yaml
name: multiagent-review
description: Fan out to 5-8 parallel reviewers (Codex CLI, Gemini CLI, specialist Claude agents) for multi-perspective review of PRs, code, designs, or writing
```

### Sections

1. **When to Activate** — trigger phrases ("review this PR", "get opinions on", "multiagent review", `/multiagent-review`)

2. **Content Type Detection** — logic for determining PR vs File vs Directory vs Inline mode from the argument

3. **Language Detection** — scan file extensions in diff or target files. Map extensions to language reviewer agents.

4. **Reviewer Selection** — always dispatch: Codex CLI, Gemini CLI, Security, Architecture. Auto-select language reviewers by detected languages. Auto-select prose-polish if non-code content detected.

5. **Dispatch Instructions** — for each reviewer type:
   - **Codex CLI:** Use Bash tool to run `codex exec` with prompt from dispatch-matrix.md. Parse output for `file:line:` format.
   - **Gemini CLI:** Use Bash tool to pipe content to `gemini` with prompt from dispatch-matrix.md. Parse output.
   - **Claude specialist agents:** Use Task tool to dispatch subagents. Each subagent reads its agent file from `agents/` directory and the relevant prompt template from `references/dispatch-matrix.md`. All dispatched in parallel.
   - **Prose-Polish:** Reference existing skill `~/.claude/skills/prose-polish/` — invoke via Skill tool, not as a subagent.

6. **Delivery Instructions:**
   - **PR Mode:** Parse each reviewer's output for `file:line: [SEVERITY] description`. For each finding, call `~/.claude/skills/pr-review-loop/scripts/post-line-comment.sh <PR> <file> <line> <agent-name> "comment"`. After all comments posted, post a summary PR comment via `gh pr comment <PR>` listing: reviewers that ran, finding counts by severity, lines flagged by multiple reviewers.
   - **Non-PR Mode:** Synthesize all reviewer outputs in conversation. Group by severity. Attribute each finding to its source reviewer(s). Highlight findings flagged by 2+ reviewers as high-confidence. End with actionable next steps.

7. **Error Handling:**
   - If `codex` CLI unavailable: warn and continue without it
   - If `gemini` CLI unavailable: warn and continue without it
   - If a subagent fails: report the failure, don't block other reviewers
   - If `post-line-comment.sh` fails: collect the comment and include in summary instead

8. **Dependencies section** listing required CLIs, scripts, and repos.

---

## Task 7: Clone Trail of Bits skills repo

**Parallelizable:** Yes (independent)

**Steps:**
```bash
cd ~/Projects/leegonzales
git clone https://github.com/trailofbits/skills.git trailofbits-skills
```

**Verify:** `ls ~/Projects/leegonzales/trailofbits-skills/` — should contain skill definitions.

**Note:** The security-reviewer agent (Task 4) should reference Trail of Bits methodology. After cloning, review their differential review skill and incorporate key patterns into the security-reviewer.md.

---

## Task 8: Add Codex reviewer to Devon's trigger-review.sh

**Parallelizable:** Yes (independent of Tasks 1-6, but separate from the main skill)

**Files:**
- Modify: `~/Projects/leegonzales/devon-claude-skills/plugins/pr-review-loop/skills/pr-review-loop/scripts/trigger-review.sh`

**Instructions:**

Add a `--codex` flag alongside the existing `--gemini` and `--cursor` flags. When `--codex` is passed:
1. Post a PR comment: `@codex review` (analogous to `/gemini review`)
2. If `--wait` is also passed, poll for Codex review completion (look for comments from `codex` or `codex[bot]` user)

Model the implementation on the existing `--gemini` flag handling in the script. Add `codex` and `codex[bot]` to the bot name detection in `get-review-comments.sh` and `_jq_helpers.sh` priority detection.

---

## Task 9: Integration test

**Parallelizable:** No — depends on all previous tasks

**Steps:**

1. Verify skill loads: invoke `/multiagent-review` in Claude Code and confirm it's recognized
2. Test content type detection:
   - `/multiagent-review #1` on a real PR — should enter PR mode
   - `/multiagent-review src/some_file.py` — should enter file mode
   - `/multiagent-review` with no args — should enter inline mode
3. Test language detection: review a multi-language PR/directory and confirm correct specialists are selected
4. Test PR mode: verify line-level comments appear on a test PR
5. Test non-PR mode: verify inline synthesis with attribution and severity grouping
6. Test graceful degradation: disconnect codex/gemini CLI and verify skill continues with remaining reviewers

---

## Execution Order

**Wave 1 (parallel):** Tasks 1, 2, 3, 4, 5, 7, 8 — all independent
**Wave 2 (sequential):** Task 6 — SKILL.md depends on agents and dispatch matrix existing
**Wave 3 (sequential):** Task 9 — integration test depends on everything

---

## Team Assignment

| Task | Agent | Why |
|------|-------|-----|
| Task 1: Directory + symlinks | agent-1 | Simple bash, fast |
| Task 2: TypeScript reviewer | agent-2 | Writing agent file, needs ECC reference |
| Task 3: Rust reviewer | agent-3 | Writing agent file, needs ECC reference |
| Task 4: Security reviewer | agent-4 | Writing agent file, needs ECC + Trail of Bits reference |
| Task 5: Dispatch matrix | agent-5 | Writing reference doc, needs design doc |
| Task 7: Clone Trail of Bits | agent-1 | Simple clone, fast (after Task 1) |
| Task 8: Codex in trigger-review.sh | agent-2 | Script modification, needs Devon's repo |
| Task 6: SKILL.md | Lead | Core orchestration, depends on all agents/refs |
| Task 9: Integration test | Lead | End-to-end verification |
