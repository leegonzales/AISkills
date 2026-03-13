# Build Timeline

Generate interactive HTML timelines of Claude Code development activity from conversation logs and git history.

## What It Does

Build Timeline parses Claude Code's `.jsonl` conversation logs and correlates them with git history to produce a standalone HTML visualization of the entire development process. The output shows:

- Agent spawns with names, prompts, and durations
- Shell commands with outputs and exit codes
- File operations (reads, writes, edits)
- Git commits with changed files
- Errors and retries
- Parallel agent work (swim lanes)
- Auto-detected development phases

## Installation

Symlink the slash command into your Claude Code commands directory:

```bash
mkdir -p ~/.claude/commands
ln -sf /Users/lgonzales/Projects/leegonzales/AISkills/BuildTimeline/dist/build-timeline.md ~/.claude/commands/build-timeline.md
```

## Usage

Inside any Claude Code conversation:

```
/build-timeline
/build-timeline --since "1 day ago" --detailed
/build-timeline /path/to/repo --theme dark --phases
/build-timeline --since "2026-03-12" --output report.html
```

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `[path]` | Target repo path | Current directory |
| `--since <date>` | Start date filter | All history |
| `--until <date>` | End date filter | Now |
| `--output <path>` | Output file path | `./build-timeline.html` |
| `--phases` | Auto-detect phases | Off |
| `--detailed` | Include all tool calls | Off |
| `--theme <name>` | `default`, `dark`, `afs` | `default` |

## Output

A standalone HTML file with:
- Fixed navigation bar with stats
- Vertical timeline with alternating event cards
- Phase headers with color coding
- Expandable detail panels
- Phase filter toggles
- Keyboard navigation (arrow keys)
- Responsive and print-friendly design
