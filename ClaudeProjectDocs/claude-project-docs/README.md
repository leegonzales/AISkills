# Claude Project Docs

**Generate concise CLAUDE.md files and agent documentation following best practices**

Create well-crafted, minimal CLAUDE.md files (~60 lines) with progressive disclosure through an `agent_docs/` directory structure.

## Why This Skill?

Most CLAUDE.md files are too long. Research indicates:

- LLMs reliably follow ~150-200 instructions
- Smaller/non-thinking models follow even fewer
- Instructions at peripheries (beginning/end) get priority
- Every unnecessary line degrades overall compliance

**The solution:** Minimal CLAUDE.md + progressive disclosure via `agent_docs/`.

## Features

### 1. Generate CLAUDE.md

Create a focused, ~60-line CLAUDE.md covering:
- Project identity (what this is)
- Tech stack (essential technologies)
- Project structure (directory overview)
- Development commands (build, test, run)
- Critical rules (non-negotiable constraints)
- Reference pointers (to agent_docs/)

### 2. Audit Existing CLAUDE.md

Analyze existing files for:
- Line count (flag if > 100 lines)
- Anti-patterns (code style, implementation examples)
- Task-specific content (should be in agent_docs/)
- Missing essentials (no tech stack, no commands)

### 3. Create Agent Docs Structure

Generate `agent_docs/` with task-specific documentation:

```
agent_docs/
├── building.md      # Build commands, compilation
├── testing.md       # Test commands, coverage
├── architecture.md  # System design decisions
├── database.md      # Schema, migrations
└── deployment.md    # Deploy process, environments
```

## Usage

### Set Up a New Project

```
"Set up Claude for this project"
"Create a CLAUDE.md for this codebase"
"Help Claude understand this project"
```

### Audit Existing Documentation

```
"Audit my CLAUDE.md"
"Is my CLAUDE.md too long?"
"Review my Claude documentation"
```

### Create Specific Agent Docs

```
"Create agent docs for testing"
"Set up agent_docs for this project"
"Create a building.md for agent_docs"
```

## Best Practices Enforced

### The 60-Line Rule

| Lines | Assessment |
|-------|------------|
| < 60 | Ideal |
| 60-100 | Acceptable |
| 100-300 | Too long, audit needed |
| > 300 | Critical, immediate refactor |

### WHAT/WHY/HOW Structure

Every CLAUDE.md should answer:
- **WHAT**: Tech stack, project structure
- **WHY**: Project purpose, key decisions
- **HOW**: Development workflow, essential commands

### Anti-Patterns Prevented

| Anti-Pattern | Why Bad | Alternative |
|--------------|---------|-------------|
| Code style rules | Use linters | ESLint, Prettier, Black |
| Full command docs | Bloats context | `agent_docs/` |
| Implementation examples | Gets stale | Point to actual code |
| Generated via /init | Generic | Hand-crafted |
| > 300 lines | Instruction decay | Refactor + agent_docs/ |

## Example Output

### Generated CLAUDE.md (~55 lines)

```markdown
# MyApp

Modern e-commerce platform built with Next.js and PostgreSQL.

## Tech Stack
- Next.js 14 (App Router)
- TypeScript
- PostgreSQL + Prisma
- Tailwind CSS
- Stripe payments

## Project Structure
src/
├── app/           # Next.js app router pages
├── components/    # React components
├── lib/           # Utilities and helpers
├── server/        # API routes and server logic
└── prisma/        # Database schema and migrations

## Development

Build: `npm run build`
Test: `npm test`
Dev: `npm run dev`
Lint: `npm run lint` (auto-fixes on save)

## Critical Rules
- All payments through Stripe API only
- Never commit .env files
- Run `npm test` before pushing

## Reference Documentation
When working on specific tasks, read:
- `agent_docs/testing.md` - Test patterns and fixtures
- `agent_docs/database.md` - Prisma schema and migrations
- `agent_docs/deployment.md` - Vercel deployment process
```

## Research Foundation

Based on recommendations from:
- [HumanLayer: Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- Community patterns from claude-md-examples

Key insight: "You're writing for Claude, not onboarding a junior dev." Use short, declarative bullet points.

## Installation

### Claude Code

```bash
# Global installation
cp -r claude-project-docs ~/.claude/skills/

# Project-specific
cp -r claude-project-docs .claude/skills/
```

### Claude Web Chat

Upload the `.skill` file from `dist/` via Settings > Capabilities > Skills.

## Version

v1.0.0 - Initial release

## License

MIT License
