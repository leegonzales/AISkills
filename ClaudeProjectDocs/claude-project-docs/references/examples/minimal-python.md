# Example: Python Library CLAUDE.md

A complete example for a Python library/package.

## The CLAUDE.md (48 lines)

```markdown
# DataForge

Data transformation library with pandas-like API and lazy evaluation.

## Tech Stack

- Python 3.11+
- No runtime dependencies (stdlib only)
- pytest for testing
- mypy for type checking

## Project Structure

```
src/dataforge/
├── core/          # Core transformation engine
├── io/            # Data readers and writers
├── ops/           # Transformation operations
└── types/         # Type definitions
tests/             # Test suite (mirrors src/)
docs/              # Sphinx documentation
```

## Development

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Commands
pytest                    # Run tests
mypy src/                 # Type check
ruff check src/           # Lint
python -m build           # Build package
```

## Critical Rules

- Zero runtime dependencies - stdlib only
- All public functions must have type hints
- Lazy evaluation by default - never materialize early

## Reference Documentation

When working on specific tasks, read:
- `agent_docs/architecture.md` - Lazy evaluation design
- `agent_docs/testing.md` - Property-based testing patterns
- `agent_docs/api-design.md` - Public API conventions
```

## Companion agent_docs/

### agent_docs/architecture.md

```markdown
# Architecture

## Core Principle: Lazy Evaluation

DataForge uses lazy evaluation. Operations build a computation graph,
only executed when `.collect()` is called.

```python
# This builds a graph, doesn't execute
result = df.filter(col("x") > 0).select("x", "y").sort("x")

# This executes the graph
data = result.collect()
```

## Module Responsibilities

### core/
- `engine.py` - Execution engine, graph optimization
- `frame.py` - DataFrame abstraction
- `expr.py` - Expression DSL

### ops/
- `filter.py` - Filter operations
- `select.py` - Column selection
- `aggregate.py` - Groupby and aggregations

### io/
- `csv.py` - CSV reader/writer
- `parquet.py` - Parquet support (optional dependency)

## Graph Optimization

Before execution, the engine optimizes:
1. Predicate pushdown
2. Projection pushdown
3. Operation fusion

See `core/optimizer.py` for implementation.
```

### agent_docs/testing.md

```markdown
# Testing

## Commands
- All tests: `pytest`
- With coverage: `pytest --cov=src/dataforge`
- Single file: `pytest tests/test_filter.py`
- Verbose: `pytest -v`

## Structure
Tests mirror source:
- `src/dataforge/ops/filter.py` → `tests/ops/test_filter.py`

## Property-Based Testing

We use Hypothesis for property-based tests:

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_filter_preserves_order(data):
    df = DataFrame({"x": data})
    result = df.filter(col("x") > 0).collect()
    assert is_sorted_like(result, [x for x in data if x > 0])
```

## Fixtures
Common fixtures in `tests/conftest.py`:
- `sample_df` - Small DataFrame for unit tests
- `large_df` - Large DataFrame for performance tests

## Coverage
Target: 90%+ coverage on core/ and ops/.
```

### agent_docs/api-design.md

```markdown
# API Design

## Naming Conventions

- Classes: PascalCase (`DataFrame`, `Expression`)
- Functions: snake_case (`read_csv`, `filter_by`)
- Constants: UPPER_SNAKE (`DEFAULT_CHUNK_SIZE`)

## Method Chaining

All transformation methods return self for chaining:

```python
def filter(self, predicate: Expression) -> "DataFrame":
    # ... implementation
    return self  # Enable chaining
```

## Error Messages

Include actionable information:

```python
# Bad
raise ValueError("Invalid column")

# Good
raise ValueError(
    f"Column '{name}' not found. "
    f"Available columns: {', '.join(self.columns)}"
)
```

## Type Hints

All public API must have complete type hints:

```python
def read_csv(
    path: str | Path,
    *,
    delimiter: str = ",",
    header: bool = True,
) -> DataFrame:
```

Use `typing.overload` for polymorphic returns.
```

## Why This Works

| Aspect | Implementation |
|--------|----------------|
| Line count | 48 lines in CLAUDE.md |
| No dependencies | Matches project constraint |
| Type checking | mypy command included |
| Critical rules | Zero-dep and lazy eval are non-obvious |
| Progressive | Architecture and API patterns in agent_docs/ |

## Adaptation Guide

To adapt for your Python project:

1. Update project name and description
2. List actual dependencies (or lack thereof)
3. Update directory structure
4. Add your virtualenv setup if different
5. Write 2-3 critical rules (architectural constraints)
6. Create agent_docs/ for complex subsystems
