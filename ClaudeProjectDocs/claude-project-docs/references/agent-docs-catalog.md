# Agent Docs Catalog

Complete catalog of `agent_docs/` files for progressive disclosure.

## Core Principle

CLAUDE.md is read every session. `agent_docs/` files are read on-demand.

Put task-specific content in agent_docs/ to:
- Reduce CLAUDE.md bloat
- Keep session context focused
- Allow detailed documentation per topic

## Directory Structure

```
project-root/
├── CLAUDE.md              # ~60 lines, universal
└── agent_docs/
    ├── building.md        # Build and compilation
    ├── testing.md         # Test patterns and execution
    ├── architecture.md    # System design
    ├── database.md        # Data layer
    ├── deployment.md      # Deploy process
    ├── api.md             # API design patterns
    ├── security.md        # Security practices
    └── debugging.md       # Debug workflows
```

## File Specifications

### building.md

**Purpose:** Build process, compilation, bundling

**Include:**
- Build commands with common flags
- Environment-specific builds (dev, staging, prod)
- Build artifacts and their locations
- Common build errors and fixes
- Asset pipeline details

**Template:**
```markdown
# Building

## Quick Commands
- Dev build: `npm run build:dev`
- Prod build: `npm run build:prod`
- Watch mode: `npm run build:watch`

## Build Artifacts
Output goes to `dist/`:
- `dist/server/` - Node.js server bundle
- `dist/client/` - Browser assets

## Environment Variables
Build respects these env vars:
- `NODE_ENV` - development|production
- `API_URL` - Backend API endpoint

## Common Issues
[List 2-3 frequent build problems and solutions]
```

---

### testing.md

**Purpose:** Test execution, patterns, fixtures

**Include:**
- Test commands (unit, integration, e2e)
- Test file locations and naming
- Fixture/mock patterns used
- Coverage requirements
- CI test configuration

**Template:**
```markdown
# Testing

## Quick Commands
- All tests: `npm test`
- Unit only: `npm run test:unit`
- E2E: `npm run test:e2e`
- Coverage: `npm run test:coverage`

## Test Structure
tests/
├── unit/          # Fast, isolated tests
├── integration/   # Service integration tests
└── e2e/           # Full workflow tests

## Fixtures
Fixtures in `tests/fixtures/`. Load with:
```typescript
import { loadFixture } from '@/tests/helpers'
const user = loadFixture('user-active')
```

## Coverage Requirements
- Minimum: 80% line coverage
- New code: Must include tests
- CI fails below threshold
```

---

### architecture.md

**Purpose:** System design, key decisions, patterns

**Include:**
- High-level architecture diagram (ASCII or reference)
- Key design decisions and rationale
- Pattern catalog used in codebase
- Module boundaries and dependencies
- Data flow overview

**Template:**
```markdown
# Architecture

## Overview
[2-3 sentences describing the system]

## Key Decisions
1. **[Decision]**: [Rationale]
2. **[Decision]**: [Rationale]

## Patterns Used
- **Repository Pattern**: Data access in `src/repositories/`
- **Service Layer**: Business logic in `src/services/`
- **DTOs**: API contracts in `src/dtos/`

## Module Dependencies
```
Controllers → Services → Repositories → Database
     ↓
   DTOs
```

## Boundaries
- `src/core/` - No external dependencies
- `src/infra/` - All external integrations
```

---

### database.md

**Purpose:** Data layer, schema, migrations

**Include:**
- Database technology and connection
- Schema overview (key tables/collections)
- Migration commands and workflow
- Seeding and fixtures
- Query patterns and ORM usage

**Template:**
```markdown
# Database

## Technology
PostgreSQL 15 via Prisma ORM

## Connection
- Dev: `DATABASE_URL` in `.env`
- Prod: Managed via infrastructure

## Schema Overview
Key tables:
- `users` - User accounts
- `orders` - Order records
- `products` - Product catalog

Full schema: `prisma/schema.prisma`

## Migrations
- Generate: `npx prisma migrate dev --name [name]`
- Apply: `npx prisma migrate deploy`
- Reset: `npx prisma migrate reset`

## Seeding
`npm run db:seed` - Loads fixtures from `prisma/seed.ts`
```

---

### deployment.md

**Purpose:** Deploy process, environments, infrastructure

**Include:**
- Deployment commands/process
- Environment list and URLs
- Infrastructure overview
- Rollback procedures
- Secrets management

**Template:**
```markdown
# Deployment

## Environments
| Env | URL | Branch |
|-----|-----|--------|
| Dev | dev.example.com | develop |
| Staging | staging.example.com | main |
| Prod | example.com | release/* |

## Deploy Commands
- Staging: `npm run deploy:staging`
- Prod: `npm run deploy:prod` (requires approval)

## Process
1. PR merged to main
2. CI runs tests
3. Auto-deploy to staging
4. Manual promotion to prod

## Rollback
`npm run rollback:prod -- --version=[tag]`

## Secrets
Managed in AWS Secrets Manager. Never commit `.env.prod`.
```

---

### api.md

**Purpose:** API design patterns, conventions

**Include:**
- API style (REST, GraphQL, etc.)
- Endpoint naming conventions
- Request/response patterns
- Authentication approach
- Error handling format

---

### security.md

**Purpose:** Security practices, auth, sensitive data

**Include:**
- Authentication mechanism
- Authorization patterns
- Sensitive data handling
- Security review process
- Known security boundaries

---

### debugging.md

**Purpose:** Debug workflows, logging, troubleshooting

**Include:**
- Logging configuration
- Debug commands and tools
- Common issues and solutions
- Performance profiling
- Error tracking integration

## When to Create Agent Docs

Create a new `agent_docs/` file when:

1. **Content is task-specific** - Only relevant for certain work
2. **Content exceeds 20 lines** - Too much for CLAUDE.md
3. **Content changes frequently** - Isolate changes
4. **Multiple related topics** - Group for discoverability

## Referencing from CLAUDE.md

Add a Reference Documentation section:

```markdown
## Reference Documentation
When working on specific tasks, read relevant files:
- `agent_docs/building.md` - Build process and compilation
- `agent_docs/testing.md` - Test patterns and fixtures
- `agent_docs/architecture.md` - System design decisions
- `agent_docs/database.md` - Prisma schema and migrations
- `agent_docs/deployment.md` - Deploy to staging/production
```

Claude will read these files when the task context matches.
