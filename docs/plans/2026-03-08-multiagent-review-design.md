# Design: `/multiagent-review` Skill
*Date: 2026-03-08*
*Status: Approved*

## Problem

Lee's current PR review setup is fragmented: `requesting-code-review` dispatches 3 generalist reviewers, `gemini-peer-review` and `codex-peer-review` require separate explicit invocation, and there are no specialist agents going deep on security, architecture, or language-specific idioms. Reviews produce prose dumps instead of line-level GitHub comments.

## Goals

1. Single command (`/multiagent-review`) fans out to 5-8 parallel reviewers
2. Multi-model parallax preserved (Codex CLI + Gemini CLI)
3. Specialist agents go deep on their lane (security, architecture, language)
4. PRs get line-level GitHub comments; everything else gets inline conversation feedback
5. Works on PRs, code files, design docs, writing, architecture docs
6. Duplicates across reviewers are signal, not noise — preserved intentionally
7. Upstream agents stay current via symlinks to source repos

## Non-Goals

- Does NOT replace `pr-review-loop` (that handles the iterative fix cycle with Gemini Code Assist on GitHub)
- Does NOT deduplicate findings — overlap = confidence
- No reviewer picker or presets — always dispatches all relevant reviewers

## Architecture

```
User invokes: /multiagent-review <target>
                    |
                    v
            Content Type Detection
            (PR / File / Dir / Inline)
                    |
                    v
            Language Detection
            (scan extensions in diff or files)
                    |
                    v
            Prompt Template Selection
            (dispatch-matrix.md: reviewer x content type)
                    |
    +-------+-------+-------+-------+-------+
    |       |       |       |       |       |
    v       v       v       v       v       v
  Codex  Gemini  Security  Arch  Lang(s)  Prose
   CLI    CLI    Agent    Agent  Agents   Polish
    |       |       |       |       |       |
    | (all dispatched in parallel via Task tool)
    |       |       |       |       |       |
    +-------+-------+-------+-------+-------+
                    |
                    v
            Delivery Layer
            PR -> post-line-comment.sh + summary PR comment
            Other -> inline synthesized feedback
```

## Content Type Detection

| Input | Mode | How Detected |
|-------|------|-------------|
| `#123` or number | PR | Starts with `#` or is numeric |
| File path | File | Path exists as file |
| Directory path | Directory | Path exists as directory |
| No argument | Inline | Reviews current conversation context |

## Reviewer Lineup

### Always Fire (every invocation)

| Reviewer | Type | Invocation |
|----------|------|-----------|
| Codex CLI | External | `codex exec "<prompt>"` |
| Gemini CLI | External | `cat <<'EOF' \| gemini` |
| Security | Claude subagent | Task tool with agent file |
| Architecture | Claude subagent | Task tool with agent file |

### Auto-Selected by Language (file extensions in target)

| Agent | Triggers On |
|-------|------------|
| Python | `.py` |
| TypeScript/JS | `.ts`, `.tsx`, `.js`, `.jsx` |
| Go | `.go` |
| Rust | `.rs` |

### Auto-Selected by Content Type

| Agent | Triggers On |
|-------|------------|
| prose-polish (existing skill) | `.md`, `.txt`, design docs, non-code content |

Mixed-language targets dispatch multiple language specialists. Mixed code+prose targets dispatch both language specialists and prose-polish.

## Dispatch Matrix (Prompt Templates)

### Codex CLI

| Content Type | Prompt Focus |
|---|---|
| PR | Review diff for bugs, logic errors, edge cases. Output as `file:line: description` |
| Code | Review code for bugs, edge cases, missed error handling. Line references |
| Design | Evaluate technical feasibility, identify implementation risks and gaps |
| Writing | Check factual claims, logical consistency, unsupported assertions |

### Gemini CLI

| Content Type | Prompt Focus |
|---|---|
| PR | Holistic review. Cross-file patterns, architectural coherence, missed interactions. Output as `file:line: description` |
| Code | Cross-module analysis. Coupling, patterns, naming consistency, design smell |
| Design | Evaluate completeness. Missing considerations, alternatives, scaling concerns |
| Writing | Assess structure, argument flow, coherence, audience fit |

### Security Agent

| Content Type | Prompt Focus |
|---|---|
| PR / Code | OWASP top 10, injection, auth bypass, secrets, input validation. Line-level |
| Design | Threat model. Attack surfaces, trust boundaries, data flow risks |
| Writing | Skip |

### Architecture Agent

| Content Type | Prompt Focus |
|---|---|
| PR / Code | SOLID violations, coupling, abstraction leaks, dependency direction. Line-level |
| Design | Component boundaries, extensibility, dependency graph, trade-offs |
| Writing | Skip |

### Language Specialists

| Content Type | Prompt Focus |
|---|---|
| PR / Code | Language idioms, type safety, error handling, performance, linter-level concerns. Line-level |
| Design / Writing | Skip |

### Prose-Polish (existing skill)

| Content Type | Prompt Focus |
|---|---|
| Writing / Design | Full assessment: craft, coherence, authority, purpose, voice |
| PR / Code | Skip |

## Delivery Layer

### PR Mode

1. Fetch diff: `gh pr diff <number>`
2. Detect languages from diff
3. Dispatch all relevant reviewers in parallel
4. Reviewers output findings as `file:line: [SEVERITY] description`
5. Claude subagents post via `post-line-comment.sh <PR> <file> <line> <agent-name> "comment"`
6. Codex/Gemini CLI output parsed and posted via same script
7. Summary PR comment: who reviewed, findings per severity, agreement highlights

### Non-PR Mode

1. Read target content
2. Detect languages / prose
3. Dispatch all relevant reviewers in parallel
4. Synthesize all feedback in conversation:
   - Grouped by severity (Critical -> Low)
   - Each finding attributed to reviewer(s)
   - Duplicates highlighted as high-confidence ("3/5 reviewers flagged this")
   - Actionable next steps

## File Structure

```
~/.claude/skills/multiagent-review/
├── SKILL.md                      # Orchestration, detection, dispatch, delivery
├── agents/
│   ├── python-reviewer.md        -> symlink to ECC
│   ├── go-reviewer.md            -> symlink to ECC
│   ├── architecture-reviewer.md  -> symlink to ECC architect.md
│   ├── typescript-reviewer.md    # Adapted from ECC code-reviewer.md
│   ├── rust-reviewer.md          # New build
│   └── security-reviewer.md      # Trail of Bits-informed
└── references/
    └── dispatch-matrix.md        # Prompt templates per reviewer x content type
```

## Update Strategy

- **Symlinked agents** (python, go, architecture): `git pull` in ECC repo updates them automatically
- **Owned agents** (typescript, rust, security): maintained by Lee
- **Trail of Bits skills**: installed as separate repo, `git pull` for updates
- **Staleness check**: skill can optionally compare local ECC commit hash vs remote and warn if behind

## Dependencies

- `gh` CLI (authenticated)
- `codex` CLI (authenticated)
- `gemini` CLI (authenticated)
- Devon's `post-line-comment.sh` (for PR mode line comments)
- ECC repo cloned at `~/Projects/leegonzales/everything-claude-code/`
- Trail of Bits skills repo (to be cloned)
- Existing `prose-polish` skill at `~/.claude/skills/prose-polish/`

## Addendum: Codex as GitHub Reviewer

Separate from this skill, add Codex as a GitHub-native reviewer in Devon's `pr-review-loop`:
- Add `--codex` flag to `trigger-review.sh`
- Posts `@codex review` as PR comment (analogous to `/gemini review`)
- Allows pr-review-loop to iterate on Codex feedback alongside Gemini Code Assist
