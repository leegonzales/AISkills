# CLAUDE.md Template

Minimal template following the 60-line rule. Copy and customize.

## The Template (~55 lines)

```markdown
# [Project Name]

[One sentence describing what this project is and does.]

## Tech Stack

- [Primary language/framework]
- [Database if applicable]
- [Key dependencies (3-5 max)]

## Project Structure

```
[root]/
├── [main-source]/    # [Brief description]
├── [secondary]/      # [Brief description]
├── [config]/         # [Brief description]
└── [tests]/          # [Brief description]
```

## Development

**Build:** `[build command]`
**Test:** `[test command]`
**Run:** `[run/dev command]`
**Lint:** `[lint command]` (configured in [config file])

## Critical Rules

- [Rule 1: Non-negotiable constraint]
- [Rule 2: Security or architectural boundary]
- [Rule 3: Process requirement]

## Reference Documentation

When working on specific tasks, read relevant files:
- `agent_docs/building.md` - Build process and compilation
- `agent_docs/testing.md` - Test patterns and fixtures
- `agent_docs/architecture.md` - System design decisions
```

## Filling the Template

### Project Name Section

One sentence only. Answer: "What is this?"

**Good:**
```markdown
# Acme API

REST API for Acme's customer management system.
```

**Bad:**
```markdown
# Acme API

This is the main API server for Acme Corporation's customer
management platform. It was started in 2019 and has grown to
support over 50 endpoints across 12 domains...
```

### Tech Stack Section

3-5 items maximum. Only what Claude needs to know for code style.

**Good:**
```markdown
## Tech Stack
- Python 3.11 + FastAPI
- PostgreSQL + SQLAlchemy
- Redis for caching
- pytest for testing
```

**Bad:**
```markdown
## Tech Stack
- Python 3.11.4
- FastAPI 0.104.1
- PostgreSQL 15.2
- SQLAlchemy 2.0.23
- Redis 7.2.3
- pytest 7.4.3
- black 23.11.0
- mypy 1.7.1
- ruff 0.1.6
- pre-commit 3.6.0
- Docker 24.0.7
- docker-compose 2.23.0
...
```

### Project Structure Section

Only directories that matter for navigation. 3-5 lines.

### Development Section

Only the commands Claude will actually run. No explanations.

### Critical Rules Section

2-3 rules maximum. These must be:
- **Universal** - Apply to every task
- **Non-obvious** - Claude wouldn't guess them
- **Consequential** - Breaking them causes real problems

**Good rules:**
- Never modify files in `legacy/` - deprecated, will be removed
- All API changes require OpenAPI spec update first
- Database migrations must be reversible

**Bad rules:**
- Use 4-space indentation (that's a linter's job)
- Write tests for new code (Claude does this anyway)
- Follow REST conventions (too vague)

### Reference Documentation Section

List your `agent_docs/` files. Claude will read them when relevant.

## Line Count Check

Count your lines:
```bash
wc -l CLAUDE.md
```

| Lines | Status |
|-------|--------|
| < 40 | Minimal, may need more context |
| 40-60 | Ideal range |
| 60-100 | Acceptable, consider trimming |
| > 100 | Too long, audit needed |
| > 300 | Critical, refactor immediately |

## What NOT to Include

See `anti-patterns.md` for detailed guidance on what to exclude.

Quick list:
- Code style rules (use linters)
- Full command documentation (use agent_docs/)
- API documentation (use OpenAPI/docs/)
- Onboarding instructions for humans
- Project history or roadmap
- Team information
