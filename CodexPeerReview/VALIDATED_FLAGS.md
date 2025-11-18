# Codex CLI - Validated Command-Line Flags

**Validation Date:** 2025-11-18
**Source:** Official OpenAI Codex GitHub repository and documentation

## Executive Summary

✅ **Confirmed:** The `--quiet` / `-q` flag **does NOT exist** in the Codex CLI
✅ **Confirmed:** `codex exec` provides non-interactive execution by default
✅ **Fix Applied:** All references to `--quiet` removed from the skill documentation

---

## Primary Commands

| Command | Purpose |
|---------|---------|
| `codex` | Launch interactive TUI |
| `codex "..."` | Start interactive session with initial prompt |
| `codex exec "..."` | Run in non-interactive automation mode |
| `codex resume` | Display session picker UI |
| `codex resume --last` | Reopen most recent session |
| `codex completion [bash\|zsh\|fish]` | Generate shell completions |

---

## Global Flags (All Commands)

### Model & Execution

| Flag | Alias | Values | Default | Description |
|------|-------|--------|---------|-------------|
| `--model` | `-m` | String | Platform-dependent | Specify which model to use (e.g., `gpt-5.1-codex`, `o3`) |
| `--ask-for-approval` | `-a` | See config table | `untrusted` | Request approval before execution |
| `--config` | `-c` | `key=value` | N/A | Override any config option (e.g., `-c model=o3`) |
| `--sandbox` | N/A | `read-only`, `workspace-write`, `danger-full-access` | `read-only` | Set sandbox access level |
| `--full-auto` | N/A | N/A | N/A | Shortcut for `--ask-for-approval on-failure --sandbox workspace-write` |

### Directory & File Access

| Flag | Alias | Values | Default | Description |
|------|-------|--------|---------|-------------|
| `--cd` | `-C` | Path | Current dir | Set working root directory without changing current directory |
| `--add-dir` | N/A | Path | N/A | Add additional writable directory (repeatable) |

### Input Options

| Flag | Alias | Values | Default | Description |
|------|-------|--------|---------|-------------|
| `--image` | `-i` | File path(s) | N/A | Attach images to prompt (comma-separated or repeat flag) |

---

## `codex exec` Specific Flags

### Automation & Access

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--full-auto` | N/A | N/A | Permits file modifications during execution |
| `--sandbox` | See global table | `read-only` | Authorization level for file edits and network commands |
| `--skip-git-repo-check` | N/A | N/A | Bypasses Git repository requirement validation |

### Output Configuration

| Flag | Alias | Values | Default | Description |
|------|-------|--------|---------|-------------|
| `--output-last-message` | `-o` | File path | N/A | Designates a file to capture the agent's final response |
| `--json` | N/A | N/A | N/A | Streams execution events as JSON Lines format to stdout |
| `--output-schema` | N/A | File path | N/A | Applies a JSON Schema to structure the agent's final output |

### Session Control

| Flag | Values | Description |
|------|--------|-------------|
| `resume [SESSION_ID]` | Session ID | Continues a prior non-interactive session |
| `resume --last` | N/A | Restarts the most recent session |

### Default Behavior

**`codex exec` default mode:**
- **Read-only** file access
- **Non-interactive** execution (no TUI)
- Activity streamed to **stderr**
- Final messages to **stdout**

---

## Configuration Options (via `~/.codex/config.toml` or `-c`)

### Approval Policy

| Value | Description |
|-------|-------------|
| `untrusted` | Ask for approval before executing commands (default) |
| `on-failure` | Only ask when something fails |
| `on-request` | Ask only when agent requests approval |
| `never` | Auto-approve all actions |

### Sandbox Mode

| Value | Description |
|-------|-------------|
| `read-only` | No file modifications allowed (default) |
| `workspace-write` | Allow file edits in workspace |
| `danger-full-access` | Full file and network access |

### Model Reasoning

| Option | Values | Default |
|--------|--------|---------|
| `model_reasoning_effort` | `minimal`, `low`, `medium`, `high` | `medium` |
| `model_reasoning_summary` | `auto`, `concise`, `detailed`, `none` | `auto` |
| `model_verbosity` | `low`, `medium`, `high` | `medium` |

---

## Feature Flags

Enable via `[features]` table or `--enable <feature>`:

| Feature | Status | Default | Description |
|---------|--------|---------|-------------|
| `web_search_request` | Stable | false | Enable web search capability |
| `view_image_tool` | Stable | true | Enable image viewing |
| `apply_patch_freeform` | Beta | false | Freeform patch application |
| `streamable_shell` | Experimental | false | Streamable shell execution |
| `unified_exec` | Experimental | false | Unified exec mode |
| `ghost_commit` | Experimental | false | Ghost commit feature |
| `rmcp_client` | Experimental | false | RMCP client support |

---

## Flags That DO NOT Exist

### ❌ Invalid Flags (Removed from Skill)

| Flag | Status | Reason |
|------|--------|--------|
| `--quiet` | **DOES NOT EXIST** | No such flag in Codex CLI |
| `-q` | **DOES NOT EXIST** | No such flag in Codex CLI |

**Note:** The `codex exec` command is **non-interactive by default**, so a `--quiet` flag is unnecessary. Output control is handled via:
- `--output-last-message` / `-o` for final message capture
- `--json` for JSON Lines output format
- `--config model_verbosity=low` to reduce agent verbosity
- Redirecting stderr to suppress activity logs

---

## Command-Line Override Precedence

1. **Specific flags** (highest): `--model o3`
2. **`-c` / `--config` flag**: `--config model=o3`
3. **Environment variables**: `CODEX_API_KEY`, etc.
4. **`config.toml` file** (lowest): `~/.codex/config.toml`

---

## Examples

### Non-Interactive Code Review (Correct)

```bash
# Recommended approach - codex exec is non-interactive by default
codex exec "Review this code for security issues"
```

### With Output Control

```bash
# JSON output for programmatic parsing
codex exec --json "Analyze architecture"

# Save final response to file
codex exec -o review.txt "Review architecture"

# Reduce verbosity
codex exec -c model_verbosity=low "Quick review"
```

### With File Access

```bash
# Read-only (default) - safe for analysis
codex exec --sandbox read-only "Analyze codebase"

# Allow file edits
codex exec --sandbox workspace-write "Implement feature"

# Full automation (use with caution)
codex exec --full-auto "Generate tests"
```

### With Images

```bash
# Attach architecture diagram
codex --image diagram.png "Analyze this architecture"

# Multiple images
codex --image diagram1.png,diagram2.png "Compare these designs"
```

---

## Interactive Shortcuts

When in interactive TUI mode:

| Shortcut | Action |
|----------|--------|
| `@` | Trigger fuzzy filename search |
| `Esc-Esc` | Enter backtrack mode to edit previous messages |
| Enter (in backtrack) | Fork conversation from selection |

---

## Validation Sources

1. ✅ **GitHub Repository**: https://github.com/openai/codex
2. ✅ **Getting Started**: `docs/getting-started.md`
3. ✅ **Exec Documentation**: `docs/exec.md`
4. ✅ **Config Reference**: `docs/config.md`
5. ✅ **Code Search**: No instances of `--quiet` flag found

---

## Skill Documentation Status

### ✅ Fixed Files

All references to invalid `--quiet` / `-q` flags removed from:
- `SKILL.md`
- `references/codex-commands.md`
- `assets/prompt-templates.md`
- `references/use-case-patterns.md`

### ✅ Current Documentation Accuracy

The skill documentation now correctly reflects:
- `codex exec` is non-interactive by default
- No `--quiet` flag exists or is needed
- Proper flag usage for sandbox, output, and model control
- Correct examples using valid flags only

---

## Recommendations for Peer Review Skill

### Recommended Patterns

**For non-interactive peer review:**
```bash
codex exec "[prompt]"
```

**For read-only analysis (safest):**
```bash
codex exec --sandbox read-only "[prompt]"
```

**For structured output:**
```bash
codex exec --json "[prompt]"
codex exec -o output.txt "[prompt]"
```

**For visual analysis:**
```bash
codex --image diagram.png "[prompt]"
```

### Configuration Recommendations

**~/.codex/config.toml for peer review:**
```toml
model = "gpt-5.1-codex"
approval_policy = "untrusted"  # Ask before actions
sandbox_mode = "read-only"      # Safe analysis mode
model_verbosity = "medium"      # Balanced output
```

---

## Summary

The Codex CLI provides comprehensive flag support for:
- ✅ Model selection and reasoning control
- ✅ Sandbox and approval policies
- ✅ Output formatting and capture
- ✅ Image attachment
- ✅ Session management

**What does NOT exist:**
- ❌ `--quiet` / `-q` flags (removed from skill)

The skill documentation is now accurate and complete based on official Codex CLI documentation.
