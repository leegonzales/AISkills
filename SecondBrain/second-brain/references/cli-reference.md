# Second Brain CLI Reference

Quick reference for all `sb` CLI commands.

## Core Commands

### sb init
Initialize Second Brain database and directories.

```bash
sb init              # Initialize with defaults
sb init --force      # Reinitialize (deletes existing)
```

### sb capture
Capture a thought or note.

```bash
sb capture "Remember to call Mom"
sb capture "API rate limit is 1000/min" --source email
sb capture "Meeting notes from standup" --source slack
```

**Options:**
- `--source, -s`: Source of capture (cli, slack, email, calendar, file)

### sb inbox
List pending captures in the inbox.

```bash
sb inbox                      # Show pending captures
sb inbox --status needs_review  # Show items needing review
sb inbox --limit 50           # Show more items
```

**Options:**
- `--status, -s`: Filter by status (pending, processing, classified, failed, needs_review)
- `--limit, -n`: Maximum items to show (default: 20)

### sb process
Process pending captures through classification.

```bash
sb process              # Process all pending
sb process --id abc123  # Process specific capture
sb process --dry-run    # Show what would happen
```

**Options:**
- `--id`: Process specific capture by ID
- `--dry-run`: Preview without making changes

### sb list
List nodes in the graph.

```bash
sb list              # List all nodes
sb list task         # List only tasks
sb list --status active
sb list --domain work
sb list --limit 50
```

**Options:**
- `--status, -s`: Filter by status
- `--domain, -d`: Filter by domain (work, personal, both)
- `--limit, -n`: Maximum items (default: 20)

### sb show
Show details of a node.

```bash
sb show abc123       # Show by ID (full or partial)
sb show "Call Mom"   # Show by title (if unique)
```

### sb digest
Generate daily digest.

```bash
sb digest            # Today's digest
```

### sb status
System health check.

```bash
sb status            # Show system status
```

---

## Output Examples

### Inbox Output
```
                        Inbox (pending)
┏━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ ID       ┃ Source ┃ Content                     ┃ Created          ┃
┡━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ abc12345 │ cli    │ Remember to call Mom...     │ 2026-01-09 14:30 │
│ def67890 │ slack  │ TODO: Review the PR from... │ 2026-01-09 15:00 │
└──────────┴────────┴─────────────────────────────┴──────────────────┘
```

### Status Output
```
Second Brain Status

Configuration:
  Node ID: home
  Database: /Users/lee/.local/share/secondbrain/secondbrain.db
  Vault: /Users/lee/Obsidian/Vault
  API Key: Configured

Database:
  Total nodes: 127
  Total edges: 84
  Total captures: 15
  Total events: 423

Inbox:
  Pending: 3
  Needs review: 2
```

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `NODE_ID` | Unique identifier for this machine | "default" |
| `ANTHROPIC_API_KEY` | Claude API key | (required) |
| `VAULT_PATH` | Path to Obsidian vault | ~/Obsidian |
| `DATABASE_PATH` | Path to SQLite database | ~/.local/share/secondbrain/secondbrain.db |
| `CLASSIFICATION_MODEL` | Claude model for classification | claude-sonnet-4-20250514 |
| `CONFIDENCE_THRESHOLD` | Min confidence for auto-classification | 0.6 |
| `LOG_LEVEL` | Logging verbosity | INFO |

---

## File Locations

| File | Purpose | Path |
|------|---------|------|
| Database | SQLite store | `~/.local/share/secondbrain/secondbrain.db` |
| Config | Settings | `~/.config/secondbrain/config.yml` |
| Vault | Obsidian output | Configured in VAULT_PATH |

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Configuration error |
| 3 | Database error |
| 4 | API error |
