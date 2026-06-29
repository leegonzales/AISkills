---
name: second-brain
description: Personal intelligence system for capturing thoughts, managing knowledge, and surfacing insights. Use when user wants to capture an idea, task, or note during conversation; query their knowledge base; check their inbox; review digests; or update task status. Triggers include "remember this," "add a task," "what did I say about," "show my inbox," or "mark complete."
license: MIT
---

# Second Brain Skill

Conversational interface to the Second Brain personal knowledge management system.
Capture thoughts naturally during Claude Code sessions, query your knowledge graph,
and manage your inbox.

**Core philosophy:** Capture at the point of thinking, not after. The system
remembers so you don't have to.

## When to Use

Recognize and route these intents:

| Intent | Trigger phrases | Command |
|--------|-----------------|---------|
| **Capture** | "remember this", "add a task", "note:", "capture this idea" — also implicit: "I should...", "don't forget..." | `sb capture` |
| **Query** | "what did I say about...", "what supports goal X", "show tasks related to..." | `sb list` / query |
| **Inbox** | "show my inbox", "what's waiting for review", "how many pending" | `sb inbox` |
| **Digest** | "what should I focus on today", "today's digest", "what's overdue" | `sb digest` |
| **Action** | "mark done", "complete task X", "archive...", "set priority to..." | `sb show` / update |
| **Transcript** | user pastes a meeting transcript to extract structured content | see ref |

## CLI Commands (load-bearing)

This skill wraps the `sb` CLI:

```bash
sb capture "content"      # Capture a thought (--source cli|slack|email|calendar|file)
sb inbox                  # List pending captures (--status, --limit)
sb process                # Classify pending captures (--id, --dry-run)
sb digest                 # Generate daily digest
sb list [type]            # List nodes (--status, --domain, --limit)
sb show <id>              # Show node details (by ID or unique title)
sb status                 # System health check
sb init                   # Initialize DB and directories (--force)
```

Full flag tables, output examples, env vars, and exit codes: see
`references/cli-reference.md`.

### Quick Action Shortcuts

```
/sb capture "thought or idea"     # Capture immediately
/sb inbox                         # Show pending items
/sb digest                        # Today's actionable summary
/sb query "search term"           # Search knowledge base
/sb done <id>                     # Mark task complete
```

## Classification

Captures are AI-classified into node types: **task, idea, reference, meeting,
goal, project, value, person**. Confidence threshold gates the inbox:

- High confidence (>=0.6): auto-classified
- Low confidence (<0.6): sent to `needs_review`

Node-type definitions, the classification decision tree, priority levels (0-4),
and domain heuristics: see `references/node-types.md`.

## Capture Workflow

When something capture-worthy comes up in conversation:

1. **Recognize intent** — direct ("Remember this...") or implicit ("I should...").
2. **Capture with context** — include relevant conversation context, tag
   `--source cli`, add any mentioned relationships.
3. **Confirm** — brief confirmation with ID; flag if `needs_review`.

Be selective — capture on expressed intent or importance, not every utterance.
Detailed workflow, context-awareness rules, anti-patterns, transcript-processing
extraction patterns, and worked examples: see `references/workflows-and-examples.md`.

## Graph Model (summary)

Nodes are typed (8 node types above) and connected by typed edges:

| Edge | Meaning |
|------|---------|
| supports | provides evidence for (project -> goal) |
| blocks | prevents progress (task -> task) |
| contains | hierarchical parent (project -> task) |
| derived_from | extracted from (goal -> value) |
| assigned_to | assigned to person (task -> person) |
| mentioned_in | referenced in context (person -> meeting) |
| related_to | general relationship (idea -> reference) |
| child_of | subtask/child (task -> task) |

## Implementation

- **Database:** local SQLite at `~/.local/share/secondbrain/secondbrain.db`
- **Vault:** Obsidian markdown output (wikilinks, daily notes include digest)
- **Config:** `~/.config/secondbrain/config.yml`

```yaml
# ~/.config/secondbrain/config.yml
node_id: "home"
vault_path: "/path/to/vault"
classification:
  model: "claude-sonnet-latest"  # use the current Sonnet ID; don't pin a dated value
  confidence_threshold: 0.6
```

## Reference Files

- `references/cli-reference.md` — full `sb` command/flag tables, output examples, environment variables, file locations, exit codes.
- `references/node-types.md` — node-type definitions, classification decision tree, priority levels, domain classification heuristics.
- `references/workflows-and-examples.md` — workflow integration, context awareness, meeting-transcript extraction patterns + config, worked example interactions, anti-patterns, integration points, success metrics.
