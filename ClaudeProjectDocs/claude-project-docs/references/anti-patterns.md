# Anti-Patterns Guide

What NOT to include in CLAUDE.md and why.

## The Core Problem

CLAUDE.md content goes into every session. LLMs have limited instruction-following capacity:

- **~150-200 instructions** for frontier thinking models
- **Fewer** for smaller or non-thinking models
- **Peripheral bias** - Beginning/end of prompt get priority

Every unnecessary line in CLAUDE.md:
1. Consumes instruction budget
2. Dilutes important instructions
3. Increases chance of being ignored

## Anti-Pattern Catalog

### 1. Code Style Rules

**Bad:**
```markdown
## Code Style
- Use 2-space indentation
- Use single quotes for strings
- Add trailing commas in arrays
- Use arrow functions over function declarations
- Prefer const over let
- No semicolons
```

**Why it's bad:**
- Linters do this faster and cheaper
- Adds 6+ instructions Claude may ignore
- Gets stale when config changes

**What to do instead:**
```markdown
## Development
Lint: `npm run lint` (auto-fixes on save)
```

Configure ESLint, Prettier, Black, etc. properly. Claude will follow existing code patterns through in-context learning.

---

### 2. Comprehensive Command Documentation

**Bad:**
```markdown
## Commands

### Development
- `npm run dev` - Start development server with hot reload on port 3000
- `npm run dev:debug` - Start with Node inspector on port 9229
- `npm run dev:mock` - Start with mock API responses

### Building
- `npm run build` - Production build to dist/
- `npm run build:dev` - Development build with source maps
- `npm run build:analyze` - Build with bundle analyzer
- `npm run build:docker` - Build Docker image

### Testing
- `npm test` - Run all tests
- `npm run test:unit` - Unit tests only
- `npm run test:e2e` - End-to-end tests
- `npm run test:watch` - Watch mode
- `npm run test:coverage` - With coverage report

[...20 more commands...]
```

**Why it's bad:**
- Bloats CLAUDE.md by 30+ lines
- Most commands won't be used in a session
- Package.json already documents this

**What to do instead:**

In CLAUDE.md (~4 lines):
```markdown
## Development
Build: `npm run build`
Test: `npm test`
Dev: `npm run dev`
```

In `agent_docs/building.md` (full documentation):
```markdown
[Complete command reference here]
```

---

### 3. Implementation Examples

**Bad:**
```markdown
## API Pattern
When creating new endpoints, follow this pattern:

```typescript
// src/routes/example.ts
import { Router } from 'express'
import { validateRequest } from '@/middleware/validation'
import { exampleSchema } from '@/schemas/example'
import { ExampleService } from '@/services/example'

const router = Router()

router.post('/',
  validateRequest(exampleSchema),
  async (req, res) => {
    const service = new ExampleService()
    const result = await service.create(req.body)
    res.status(201).json(result)
  }
)

export default router
```
```

**Why it's bad:**
- 20+ lines of code in system prompt
- Gets stale when patterns change
- Existing code shows the pattern better

**What to do instead:**
```markdown
## Critical Rules
- Follow existing patterns in src/routes/
```

Claude learns from your actual code through in-context learning.

---

### 4. Generated /init Content

**Bad:**
Using the raw output from `claude /init`:
```markdown
# Project

This is a TypeScript project using Node.js.

## Files
- package.json: Contains dependencies
- tsconfig.json: TypeScript configuration
- src/: Source files
- tests/: Test files

## Scripts
See package.json for available scripts.
```

**Why it's bad:**
- Generic, not project-specific
- States obvious facts
- Provides no real guidance

**What to do instead:**
Hand-craft your CLAUDE.md. Every line should be:
- **Non-obvious** - Claude wouldn't know without it
- **Actionable** - Affects how Claude works
- **Universal** - Relevant to every session

---

### 5. Excessive Critical Rules

**Bad:**
```markdown
## Rules
1. Use TypeScript for all new files
2. Follow ESLint configuration
3. Write tests for new functionality
4. Use meaningful variable names
5. Add JSDoc comments to public functions
6. Keep functions under 50 lines
7. Use async/await over promises
8. Handle all errors appropriately
9. Log important operations
10. Validate all user input
11. Never commit secrets
12. Follow REST conventions
13. Use proper HTTP status codes
14. Document API changes in OpenAPI
15. Update changelog for features
```

**Why it's bad:**
- 15 rules compete for attention
- Many are obvious or covered by linters
- Violates the ~150 instruction limit principle

**What to do instead:**
```markdown
## Critical Rules
- Never modify files in `legacy/` - deprecated code
- All API changes require OpenAPI spec update first
- Run `npm test` before pushing
```

2-3 rules that are:
- Non-obvious
- Specific to this project
- Have real consequences if violated

---

### 6. Team/Process Information

**Bad:**
```markdown
## Team
- Frontend: @alice, @bob
- Backend: @charlie, @diana
- DevOps: @eve

## Process
1. Create feature branch from develop
2. Open draft PR when starting
3. Request review from 2 team members
4. Squash merge when approved
5. Delete branch after merge

## Meetings
- Standup: Daily 9am
- Sprint planning: Monday 10am
- Retro: Friday 3pm
```

**Why it's bad:**
- Irrelevant to Claude's work
- Takes up instruction budget
- Human process, not AI context

**What to do instead:**
Don't include this in CLAUDE.md. It's for humans, not agents.

---

### 7. Project History/Roadmap

**Bad:**
```markdown
## History
This project started in 2019 as a hackathon prototype...

## Roadmap
- Q1: Mobile app launch
- Q2: International expansion
- Q3: Enterprise features
```

**Why it's bad:**
- Narrative text wastes tokens
- Future plans don't help current coding
- Gets stale

**What to do instead:**
Focus on present-state, actionable information only.

---

## Quick Audit Checklist

Run this audit on your CLAUDE.md:

| Check | Action |
|-------|--------|
| Line count > 100? | Trim or move to agent_docs/ |
| Code style rules? | Delete, use linters |
| Command list > 5? | Move to agent_docs/building.md |
| Code examples? | Delete, point to actual code |
| Generated by /init? | Rewrite from scratch |
| > 5 rules? | Reduce to 2-3 critical ones |
| Team/process info? | Delete |
| History/roadmap? | Delete |
| Tutorial-style prose? | Convert to bullets |

## The Litmus Test

For every line in CLAUDE.md, ask:

1. **Is this universal?** - Applies to every session, not just some tasks
2. **Is this non-obvious?** - Claude wouldn't know without it
3. **Is this actionable?** - Changes how Claude works
4. **Is this current?** - Won't become stale

If any answer is "no," remove it or move it to `agent_docs/`.
