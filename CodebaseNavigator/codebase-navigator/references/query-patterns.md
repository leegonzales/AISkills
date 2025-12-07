# Query Patterns for osgrep

Effective query formulations for common code search scenarios.

## Architecture Queries

| Goal | Query |
|------|-------|
| Entry point | `"main entry point and application bootstrap"` |
| Routing | `"HTTP routes and URL endpoint definitions"` |
| Middleware | `"middleware chain and request interceptors"` |
| Database layer | `"database connection and query execution"` |
| Config | `"configuration loading and environment setup"` |

## Feature-Specific Queries

| Feature | Query |
|---------|-------|
| Authentication | `"user authentication login and session management"` |
| Authorization | `"permission checks and access control"` |
| Validation | `"input validation and data sanitization"` |
| Error handling | `"error handling exceptions and error responses"` |
| Logging | `"logging and log message formatting"` |
| Caching | `"cache management and cache invalidation"` |
| Background jobs | `"background jobs queues and async tasks"` |

## Code Pattern Queries

| Pattern | Query |
|---------|-------|
| API endpoints | `"REST API endpoints and HTTP handlers"` |
| Data models | `"data models schemas and type definitions"` |
| Database migrations | `"database migrations and schema changes"` |
| Tests | `"test cases and test utilities"` |
| Utilities | `"utility functions and helper methods"` |

## Language-Specific Queries

### JavaScript/TypeScript
- `"React component rendering and props handling"`
- `"Redux actions and state management"`
- `"Express middleware and route handlers"`
- `"async await and promise handling"`

### Python
- `"FastAPI routes and request handlers"`
- `"SQLAlchemy models and ORM queries"`
- `"pytest fixtures and test setup"`
- `"decorator definitions and function wrapping"`

### Go
- `"HTTP handler functions and router setup"`
- `"goroutines and concurrent processing"`
- `"interface implementations and type assertions"`
- `"error wrapping and error handling"`

## Query Improvement Techniques

### Add Context
❌ `"auth"` (too vague)
✅ `"user authentication and login flow"`

### Use Synonyms
❌ `"config"` (single keyword)
✅ `"configuration settings environment variables"`

### Describe Purpose
❌ `"calculate"` (generic)
✅ `"calculate total price including tax and discounts"`

### Be Specific
❌ `"handle errors"` (too broad)
✅ `"handle database connection errors and retry logic"`

## Combining Searches

For complex questions, run multiple focused queries:

**Question:** "How does the checkout process work?"

**Queries:**
1. `"shopping cart and cart management"`
2. `"checkout flow and order creation"`
3. `"payment processing and transaction handling"`
4. `"order confirmation and email notification"`

Then synthesize results into coherent explanation.

## When osgrep Isn't Ideal

Use traditional grep/ripgrep for:
- Exact string matches: `rg "TODO:"`
- Specific function names: `rg "def calculate_tax"`
- Error messages: `rg "Connection refused"`
- Import statements: `rg "from utils import"`

osgrep excels at finding code by **meaning**, not exact text.
