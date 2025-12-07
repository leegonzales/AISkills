# Example: Web Application CLAUDE.md

A complete example for a Next.js + PostgreSQL web application.

## The CLAUDE.md (52 lines)

```markdown
# ShopStream

Modern e-commerce platform for indie brands.

## Tech Stack

- Next.js 14 (App Router)
- TypeScript
- PostgreSQL + Prisma
- Tailwind CSS + shadcn/ui
- Stripe for payments

## Project Structure

```
src/
├── app/           # Next.js pages and API routes
├── components/    # React components (ui/ for shadcn)
├── lib/           # Utilities, hooks, helpers
├── server/        # Server-only code (actions, db)
└── prisma/        # Database schema
```

## Development

Build: `npm run build`
Test: `npm test`
Dev: `npm run dev` (port 3000)
Lint: `npm run lint`

Database:
- Migrate: `npx prisma migrate dev`
- Studio: `npx prisma studio`

## Critical Rules

- All payments through Stripe API only - never store card data
- Use server actions for mutations, not API routes
- Run `npm test` before pushing

## Reference Documentation

When working on specific tasks, read:
- `agent_docs/testing.md` - Playwright E2E and Jest unit tests
- `agent_docs/database.md` - Prisma schema and migrations
- `agent_docs/deployment.md` - Vercel deployment process
- `agent_docs/stripe.md` - Payment integration patterns
```

## Companion agent_docs/

### agent_docs/testing.md

```markdown
# Testing

## Commands
- All: `npm test`
- Unit: `npm run test:unit`
- E2E: `npm run test:e2e`
- Watch: `npm run test:watch`

## Structure
tests/
├── unit/        # Jest unit tests
├── e2e/         # Playwright E2E
└── fixtures/    # Test data

## E2E Patterns
Playwright tests in `tests/e2e/`. Run against dev server:
```bash
npm run dev &
npm run test:e2e
```

## Fixtures
User fixtures in `tests/fixtures/users.ts`.
Product fixtures auto-generated from seed data.

## Coverage
Minimum 80%. CI fails below threshold.
```

### agent_docs/database.md

```markdown
# Database

## Tech
PostgreSQL 15 via Prisma ORM

## Schema
Main tables:
- `User` - Accounts and profiles
- `Product` - Product catalog
- `Order` - Purchase orders
- `OrderItem` - Line items

Schema: `prisma/schema.prisma`

## Commands
- Generate client: `npx prisma generate`
- Create migration: `npx prisma migrate dev --name [name]`
- Apply migrations: `npx prisma migrate deploy`
- Reset (dev only): `npx prisma migrate reset`
- Browse data: `npx prisma studio`

## Seeding
`npm run db:seed` loads test data for development.

## Conventions
- Use `@db.Uuid` for IDs
- All tables have `createdAt` and `updatedAt`
- Soft delete via `deletedAt` where needed
```

### agent_docs/stripe.md

```markdown
# Stripe Integration

## Overview
Stripe handles all payment processing. We never store card details.

## Test Mode
Dev and staging use test mode. Test cards:
- Success: 4242 4242 4242 4242
- Decline: 4000 0000 0000 0002

## Webhooks
Webhook handler: `src/app/api/webhooks/stripe/route.ts`

Events handled:
- `checkout.session.completed`
- `payment_intent.succeeded`
- `payment_intent.failed`

## Local Testing
```bash
stripe listen --forward-to localhost:3000/api/webhooks/stripe
```

## Keys
- Dev: In `.env.local`
- Prod: In Vercel environment variables

Never commit Stripe keys. Never log them.
```

## Why This Works

| Aspect | Implementation |
|--------|----------------|
| Line count | 52 lines in CLAUDE.md |
| Universal | Tech stack and rules apply every session |
| Progressive | Payment, testing, database details in agent_docs/ |
| Non-obvious | Stripe-only rule, server actions preference |
| Current | Commands match actual package.json |

## Adaptation Guide

To adapt for your web project:

1. Replace project name and description
2. Update tech stack to match yours
3. Adjust directory structure
4. Update commands from your package.json
5. Write 2-3 critical rules specific to your project
6. Create agent_docs/ for your major subsystems
