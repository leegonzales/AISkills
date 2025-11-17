---
name: notebooklm
description: Query Google NotebookLM for source-grounded, citation-backed answers from uploaded documents. Reduces hallucinations through Gemini's document-only responses. Browser automation with library management and persistent authentication.
---

# NotebookLM Skill

Query Google NotebookLM notebooks for source-grounded answers exclusively from your uploaded documentation, drastically reducing hallucinations.

## When to Use

Trigger when user:
- Mentions NotebookLM or shares URL (`https://notebooklm.google.com/notebook/...`)
- Asks to query notebooks/documentation ("ask my NotebookLM", "check my docs")
- Wants citations from specific sources
- Needs to add notebooks to library

## Critical: Always Use run.py Wrapper

**NEVER call scripts directly. ALWAYS use `python scripts/run.py [script]`:**

```bash
# ✅ CORRECT
python scripts/run.py auth_manager.py status
python scripts/run.py ask_question.py --question "..."

# ❌ WRONG - Fails without venv!
python scripts/auth_manager.py status
```

The run.py wrapper auto-creates `.venv`, installs dependencies, and executes properly.

## Core Workflow

### 1. Check Authentication
```bash
python scripts/run.py auth_manager.py status
```

### 2. Authenticate (One-Time, Browser Visible)
```bash
python scripts/run.py auth_manager.py setup
```

Tell user: "A browser window will open for Google login"

### 3. Add Notebooks (Smart Discovery Recommended)

**Smart Add:** Query first to discover content:
```bash
# Step 1: Discover content
python scripts/run.py ask_question.py --question "What topics does this notebook cover?" --notebook-url "[URL]"

# Step 2: Add with discovered metadata
python scripts/run.py notebook_manager.py add --url "[URL]" --name "[Based on content]" --description "[From discovery]" --topics "[From discovery]"
```

**Manual Add:** Only if user provides all details:
```bash
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Descriptive Name" \
  --description "What this contains" \  # REQUIRED
  --topics "topic1,topic2,topic3"      # REQUIRED
```

NEVER guess metadata! Use Smart Add if details unknown.

### 4. Ask Questions
```bash
# Uses active notebook
python scripts/run.py ask_question.py --question "Your question"

# Specific notebook
python scripts/run.py ask_question.py --question "..." --notebook-id ID

# Direct URL
python scripts/run.py ask_question.py --question "..." --notebook-url URL
```

## Follow-Up Mechanism (CRITICAL)

Every answer ends with: **"Is that ALL you need to know?"**

**Required behavior:**
1. **STOP** - Don't immediately respond
2. **ANALYZE** - Compare answer to user's request
3. **IDENTIFY GAPS** - Determine missing information
4. **ASK FOLLOW-UP** - If gaps exist, ask immediately:
   ```bash
   python scripts/run.py ask_question.py --question "Follow-up with context..."
   ```
5. **REPEAT** - Continue until information complete
6. **SYNTHESIZE** - Combine all answers before responding

## Quick Commands

```bash
# Authentication
python scripts/run.py auth_manager.py status|setup|reauth|clear

# Library management
python scripts/run.py notebook_manager.py list|search --query QUERY|activate --id ID|stats

# Cleanup (preserves library)
python scripts/run.py cleanup_manager.py --preserve-library --confirm
```

## Troubleshooting

| Error | Solution |
|-------|----------|
| ModuleNotFoundError | Use run.py wrapper |
| Authentication failed | Browser must be visible for setup |
| Rate limit (50/day) | Wait or switch Google account |
| Browser crashes | `cleanup_manager.py --preserve-library` |

## Important Notes

- **Local Claude Code only** - Web UI sandbox blocks network access
- **Stateless sessions** - Each question = fresh browser (3-5 sec overhead)
- **Browser automation** - UI changes will break selectors (see README maintenance section)
- **Expect maintenance** - NotebookLM updates require selector updates
- See README.md and references/ for comprehensive documentation

## Data Storage

```
~/.claude/skills/notebooklm/data/
├── library.json         # Notebook metadata
├── auth_info.json       # Auth status
└── browser_state/       # Browser cookies (NEVER commit)
```

All sensitive data protected by `.gitignore`.
