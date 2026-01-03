# Gemini CLI - Validated Command-Line Flags

**Validation Date:** 2025-11-19
**Source:** Official Google Gemini CLI GitHub repository and documentation

## Executive Summary

✅ **Confirmed:** The `--quiet` flag **does NOT exist** in the official Google Gemini CLI
✅ **Confirmed:** Use `-p` flag for headless/non-interactive mode instead
❌ **Issue Found:** Skill documentation incorrectly references `--quiet` in 9 locations
✅ **Fix Required:** Remove all `--quiet` references and update with correct flags

---

## Primary Commands

| Command | Purpose |
|---------|---------|
| `gemini` | Launch interactive TUI |
| `gemini -p "prompt"` | Run in headless mode (non-interactive) |

---

## Validated Command-Line Flags

### Headless/Non-Interactive Mode

| Flag | Alias | Values | Default | Description |
|------|-------|--------|---------|-------------|
| `--prompt` | `-p` | String | N/A | Run in headless mode with direct query input |
| `--output-format` | N/A | `text`, `json`, `stream-json` | `text` | Specify output format |
| `--model` | `-m` | Model name | `gemini-3.0-pro` | Specify which Gemini model to use |
| `--debug` | `-d` | N/A | N/A | Enable debug mode for troubleshooting |
| `--include-directories` | N/A | Comma-separated paths | N/A | Include additional directories for context |
| `--yolo` | `-y` | N/A | N/A | Auto-approve all actions without prompts |
| `--approval-mode` | N/A | e.g., `auto_edit` | N/A | Set approval behavior |

---

## Flags That DO NOT Exist

### ❌ Invalid Flags (Found in Skill Documentation)

| Flag | Status | Reason |
|------|--------|--------|
| `--quiet` | **DOES NOT EXIST** | No such flag in official Google Gemini CLI |

**Note:** The Gemini CLI uses `-p` (headless mode) + `--output-format` for clean, non-interactive output. There is no separate `--quiet` flag.

---

## Correct Usage for Non-Interactive Peer Review

### ❌ INCORRECT (Current Skill Documentation)

```bash
gemini --quiet -p "prompt"
```

### ✅ CORRECT

```bash
# Basic headless mode (non-interactive)
gemini -p "prompt"

# With clean JSON output
gemini -p "prompt" --output-format json

# With streaming JSON events
gemini -p "prompt" --output-format stream-json

# With specific model
gemini -m gemini-3.0-flash -p "prompt"

# Full automation (auto-approve)
gemini -y -p "prompt"
```

---

## Complete Flag Reference

### Model Selection

| Flag | Alias | Values | Description |
|------|-------|--------|-------------|
| `--model` | `-m` | `gemini-3.0-pro`, `gemini-3.0-flash`, `gemini-3.0-flash-thinking`, `gemini-3.0-deep-think` | Specify which Gemini model to use |

**Model Characteristics:**
- **gemini-3.0-pro**: 1M token context, best reasoning, slower
- **gemini-3.0-flash**: 1M token context, fast, balanced
- **gemini-3.0-flash-thinking**: Extended reasoning mode
- **gemini-3.0-deep-think**: Latest ultra-fast model

### Output Formats

| Value | Description | Use Case |
|-------|-------------|----------|
| `text` | Plain text output (default) | Human consumption |
| `json` | Structured JSON response | Programmatic parsing |
| `stream-json` | Newline-delimited JSON events | Real-time streaming |

### Execution Modes

| Flag | Description | Use Case |
|------|-------------|----------|
| `-p` / `--prompt` | Headless mode with prompt | Non-interactive scripts |
| `--yolo` / `-y` | Auto-approve all actions | Full automation (use with caution) |
| `--approval-mode` | Custom approval behavior | Fine-grained control |

### Debug & Development

| Flag | Alias | Description |
|------|-------|-------------|
| `--debug` | `-d` | Enable debug output |
| `--include-directories` | N/A | Add directories to context |

---

## Interactive Mode Features

When running `gemini` without `-p` (interactive mode):

### Slash Commands

| Command | Purpose |
|---------|---------|
| `/tools` | List available tools |
| `/stats` | Show token usage |
| `/chat` | Start new chat |
| `/bug` | Report issues |
| `/settings` | Configure CLI |
| `/quit` | Exit |

### At Commands

| Command | Purpose |
|---------|---------|
| `@file_path` | Reference file in prompt |
| `@./directory/` | Reference entire directory |

### Shell Passthrough

| Command | Purpose |
|---------|---------|
| `!command` | Execute shell command |

---

## Key Differences from Codex CLI

| Feature | Gemini CLI | Codex CLI |
|---------|-----------|-----------|
| **Headless Mode** | `-p` / `--prompt` | `codex exec` |
| **Quiet Output** | `--output-format json` | No equivalent (exec is non-interactive) |
| **Auto-approve** | `--yolo` / `-y` | `--full-auto` |
| **Model Selection** | `-m` / `--model` | `--model` / `-m` |
| **Debug Mode** | `-d` / `--debug` | N/A documented |
| **Context Window** | 1M tokens (3.0 models) | Varies by model |
| **Multimodal** | Via file references | `--image` flag |

---

## Authentication Methods

### 1. Login with Google (Free Tier)

```bash
gemini
# Select "Login with Google" in UI
```

**Limits:** 60 requests/min, 1,000 requests/day

### 2. Gemini API Key

```bash
export GEMINI_API_KEY="your-api-key-here"
gemini -p "prompt"
```

**Limits:** 100 requests/day (free), higher with billing

### 3. Vertex AI (Enterprise)

```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
gcloud auth application-default login
gemini -p "prompt"
```

**Limits:** Pay-as-you-go with enterprise SLA

---

## Recommended Patterns for Peer Review

### Architecture Review

```bash
gemini -p "$(cat <<'EOF'
Review this architecture for scalability and maintainability:

[architecture description or file references with @]
EOF
)"
```

### With File Context

```bash
gemini -p "Review the architecture in @./architecture.md for security issues"
```

### With Multiple Files

```bash
gemini -p "Analyze the codebase: @./src/ and provide refactoring recommendations"
```

### With JSON Output for Parsing

```bash
gemini -p "Identify all security vulnerabilities in @./src/auth.ts" --output-format json > review.json
```

### With Specific Model

```bash
gemini -m gemini-3.0-pro -p "Deep architectural analysis of @./docs/architecture.md"
```

### With Auto-Approval (Use Carefully)

```bash
gemini -y -p "Generate comprehensive test suite for @./src/utils.ts"
```

---

## Configuration File

**Location:** `.gemini/.env`

```bash
# API Authentication
GEMINI_API_KEY=your-api-key-here

# Or Vertex AI
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
```

---

## Validation Sources

1. ✅ **GitHub Repository**: https://github.com/google-gemini/gemini-cli
2. ✅ **Headless Mode Docs**: `docs/cli/headless.md`
3. ✅ **README**: `README.md`
4. ✅ **Code Search**: No instances of `--quiet` flag found

---

## Skill Documentation Issues Found

### ❌ Files with Invalid `--quiet` References

1. `SKILL.md` - 2 instances
2. `references/gemini-commands.md` - 4 instances
3. `references/synthesis-framework.md` - 1 instance
4. `references/context-preparation.md` - 2 instances

**Total:** 9 instances across 4 files

---

## Required Fixes

### 1. Remove `--quiet` Flag

**Before:**
```bash
gemini --quiet -p "prompt"
```

**After:**
```bash
gemini -p "prompt"
```

### 2. Update Flag Documentation

**Before:**
```
--quiet: Suppress interactive prompts
```

**After:**
```
-p / --prompt: Run in headless mode (non-interactive)
--output-format: Control output format (text/json/stream-json)
```

### 3. Update Examples

All examples should use correct flags:
- Replace `--quiet` with nothing (headless mode is implicit with `-p`)
- Add `--output-format json` when clean output is needed
- Use `-y` or `--yolo` for auto-approval instead

---

## Summary

The official Google Gemini CLI provides comprehensive functionality for:
- ✅ Headless/non-interactive execution via `-p`
- ✅ Output format control via `--output-format`
- ✅ Model selection via `-m`
- ✅ Auto-approval via `--yolo` / `-y`
- ✅ Debug mode via `-d`
- ✅ Massive 1M token context window
- ✅ Multimodal support (images, PDFs via @ references)

**What does NOT exist:**
- ❌ `--quiet` flag (must be removed from skill)

The skill documentation requires updates to remove all invalid `--quiet` references and replace with correct headless mode usage patterns.
