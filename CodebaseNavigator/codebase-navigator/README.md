# Codebase Navigator

Semantic code search using osgrep - find code by meaning, not just keywords.

## Overview

Codebase Navigator enables natural language code search. Ask questions like "where is authentication handled?" and get relevant results based on semantic meaning, not exact string matches.

**Powered by [osgrep](https://github.com/anthropics/osgrep)** - a semantic search tool using vector embeddings.

## Features

- **Semantic search** - Find code by describing what it does
- **Natural language queries** - "where do we handle payments?"
- **Multiple output modes** - snippets, full content, paths only, JSON
- **Relevance scoring** - See how well results match your query
- **Auto-refresh workflow** - Check index freshness, refresh if stale (>4 hours)
- **osgrep vs grep guidance** - Know when to use semantic vs literal search
- **Tool combination patterns** - Combine osgrep with Glob, grep, and Read

## Requirements

- [osgrep](https://github.com/anthropics/osgrep) installed and configured
- Run `osgrep setup` for first-time setup
- Run `osgrep index` in your repository

## Quick Start

```bash
# Check osgrep is working
osgrep doctor

# Index your repository
osgrep index

# Search semantically
osgrep search "user authentication and login"

# Always-safe search (updates index first)
osgrep search "query" --sync
```

## Usage

### Basic Search
```bash
osgrep search "what you're looking for"
```

### With Options
```bash
osgrep search "query" --max-count 10    # Limit results
osgrep search "query" --content         # Show full content
osgrep search "query" --compact         # Paths only
osgrep search "query" --scores          # Show relevance
osgrep search "query" --sync            # Update index first
```

## When to Use osgrep vs grep

| Use osgrep | Use grep |
|------------|----------|
| Searching by concept | Searching for exact strings |
| "Where is auth handled?" | "Find TODO:" |
| Unknown function names | Known identifiers |
| Architecture questions | Error message lookup |

**Rule of thumb:** If you could type the exact string, use grep. If you're describing what code *does*, use osgrep.

## Query Tips

**Good queries describe purpose:**
- ✅ "database connection and query execution"
- ✅ "error handling and exception management"
- ❌ "db" (too vague)
- ❌ "handle" (too generic)

See `references/query-patterns.md` for comprehensive examples.

## Troubleshooting

See `references/troubleshooting.md` for common issues.

## Version

1.0.2

## License

MIT
