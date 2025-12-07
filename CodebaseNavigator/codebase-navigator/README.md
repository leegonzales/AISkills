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
- **Live indexing** - Background server for frequently changing codebases

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
```

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

1.0.0

## License

MIT
