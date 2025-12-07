# Example: Monorepo CLAUDE.md

A complete example for a TypeScript monorepo with multiple packages.

## The CLAUDE.md (58 lines)

```markdown
# Acme Platform

Monorepo for Acme's web platform, API, and shared packages.

## Tech Stack

- TypeScript (strict mode)
- pnpm workspaces
- Turborepo for builds
- Packages: React (web), Fastify (api), shared libs

## Project Structure

```
packages/
├── web/           # Next.js frontend
├── api/           # Fastify backend
├── ui/            # Shared React components
├── config/        # Shared configs (tsconfig, eslint)
└── types/         # Shared TypeScript types
apps/
└── docs/          # Documentation site
```

## Development

```bash
# Install all packages
pnpm install

# Commands (from root)
pnpm dev           # Start all in dev mode
pnpm build         # Build all packages
pnpm test          # Test all packages
pnpm lint          # Lint all packages

# Single package
pnpm --filter web dev
pnpm --filter api test
```

## Critical Rules

- Changes to `packages/types/` require running `pnpm build` first
- Never import from `../` across package boundaries - use package names
- All packages must pass CI before merge

## Reference Documentation

When working on specific tasks, read:
- `agent_docs/package-deps.md` - Package dependency graph
- `agent_docs/web.md` - Frontend patterns
- `agent_docs/api.md` - Backend patterns
- `agent_docs/adding-packages.md` - Creating new packages
```

## Companion agent_docs/

### agent_docs/package-deps.md

```markdown
# Package Dependencies

## Dependency Graph

```
apps/docs ──────────────────────────────┐
                                        ▼
packages/web ─────┬────────────────► packages/ui
                  │                      │
                  ▼                      ▼
packages/api ─────┴──────────────► packages/types
                                        ▲
packages/config ────────────────────────┘
```

## Package Purposes

| Package | Purpose | Depends On |
|---------|---------|------------|
| web | Next.js frontend | ui, types, config |
| api | Fastify backend | types, config |
| ui | React component library | types, config |
| types | Shared TypeScript types | config |
| config | Shared configs | (none) |
| docs | Documentation site | ui, types |

## Import Rules

Always use package names, never relative paths:

```typescript
// Correct
import { Button } from "@acme/ui"
import { User } from "@acme/types"

// Wrong - never do this
import { Button } from "../../ui/src/Button"
```

## Build Order

Turborepo handles this automatically, but for reference:
1. config (no deps)
2. types (depends on config)
3. ui (depends on types, config)
4. api, web, docs (depend on above)
```

### agent_docs/web.md

```markdown
# Frontend (packages/web)

## Tech
- Next.js 14 with App Router
- React Query for data fetching
- Tailwind CSS for styling
- Uses @acme/ui components

## Structure
src/
├── app/           # Next.js app router
├── features/      # Feature modules
├── hooks/         # Custom hooks
└── lib/           # Utilities

## Patterns

### Data Fetching
Use React Query, not useEffect:

```typescript
const { data, isLoading } = useQuery({
  queryKey: ['users'],
  queryFn: () => api.users.list(),
})
```

### API Client
API client in `src/lib/api.ts`. Type-safe via @acme/types.

### Components
Prefer @acme/ui components. Only create local components
for page-specific UI.

## Running
```bash
pnpm --filter web dev    # Start on port 3000
pnpm --filter web build  # Production build
pnpm --filter web test   # Run tests
```
```

### agent_docs/api.md

```markdown
# Backend (packages/api)

## Tech
- Fastify
- Prisma ORM
- PostgreSQL
- Uses @acme/types for shared types

## Structure
src/
├── routes/        # API route handlers
├── services/      # Business logic
├── repositories/  # Data access
├── plugins/       # Fastify plugins
└── prisma/        # Schema and migrations

## Patterns

### Route Structure
```typescript
// src/routes/users/index.ts
export default async function(fastify: FastifyInstance) {
  fastify.get('/', listUsers)
  fastify.get('/:id', getUser)
  fastify.post('/', createUser)
}
```

### Services
Business logic in services, not routes:

```typescript
// Route calls service
const user = await userService.create(data)

// Service handles logic
class UserService {
  async create(data: CreateUserInput): Promise<User> {
    // validation, business rules, etc.
  }
}
```

## Running
```bash
pnpm --filter api dev    # Start on port 4000
pnpm --filter api test   # Run tests
```
```

### agent_docs/adding-packages.md

```markdown
# Adding New Packages

## Steps

1. Create package directory:
```bash
mkdir packages/new-package
cd packages/new-package
```

2. Initialize package.json:
```json
{
  "name": "@acme/new-package",
  "version": "0.0.0",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "scripts": {
    "build": "tsup src/index.ts --format cjs,esm --dts",
    "dev": "tsup src/index.ts --format cjs,esm --dts --watch"
  }
}
```

3. Add tsconfig.json extending shared config:
```json
{
  "extends": "@acme/config/tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist"
  },
  "include": ["src"]
}
```

4. Install from root:
```bash
pnpm install
```

5. Add to dependent packages:
```bash
pnpm --filter web add @acme/new-package
```

## Checklist
- [ ] Package name starts with @acme/
- [ ] Extends shared tsconfig
- [ ] Has build and dev scripts
- [ ] Added to turbo.json if needed
- [ ] Documented in agent_docs/package-deps.md
```

## Why This Works

| Aspect | Implementation |
|--------|----------------|
| Line count | 58 lines in CLAUDE.md |
| Workspace commands | pnpm filter syntax shown |
| Boundary rules | Cross-package import rule is critical |
| Progressive | Each package gets its own agent_docs/ file |
| Build order | Turborepo handles, but explained in agent_docs/ |

## Adaptation Guide

To adapt for your monorepo:

1. Update project name and package list
2. Match your workspace tool (pnpm/npm/yarn)
3. Document your package structure
4. Add critical rules about package boundaries
5. Create agent_docs/ per package for detailed patterns
