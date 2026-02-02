# Eric Raymond's 17 Unix Rules

From *The Art of Unix Programming* (2003). Each rule includes its definition, code smells that violate it, exemplar patterns, and language-specific notes.

---

## 1. Rule of Modularity

**Definition:** Write simple parts connected by clean interfaces.

**Code Smells:**
- Functions longer than ~50 lines
- Classes with 10+ methods spanning multiple concerns
- Files importing from many unrelated modules
- "God objects" that know about everything

**Exemplar Patterns:**
- Single-purpose modules with clear public APIs
- Narrow interfaces (few parameters, few methods)
- Internal implementation details hidden behind boundaries

**Language Notes:**
- Python: One class per concern, `__all__` exports
- Go: Small interfaces (1-3 methods), package-level separation
- JS/TS: Named exports over default, barrel files for public API
- Rust: Trait-based interfaces, module visibility

---

## 2. Rule of Clarity

**Definition:** Clarity is better than cleverness.

**Code Smells:**
- Ternary nesting deeper than 1 level
- Bitwise operations without comments explaining purpose
- Variable names like `x`, `tmp`, `data` in non-trivial contexts
- Regex without explanation of what it matches
- "Clever" one-liners that save lines but cost comprehension

**Exemplar Patterns:**
- Self-documenting function names (`validate_email_format` not `check`)
- Explaining "why" in comments, not "what"
- Breaking complex expressions into named intermediates
- Consistent naming conventions throughout

**Language Notes:**
- Python: Follow PEP 8 naming, use type hints for clarity
- Go: Short variable names OK in small scopes (idiomatic)
- JS/TS: Avoid `any` type—it trades clarity for convenience

---

## 3. Rule of Composition

**Definition:** Design programs to be connected to other programs.

**Code Smells:**
- No CLI interface or scriptable API
- Functions that print directly instead of returning data
- Hard-coded output formats (no JSON/structured option)
- Interactive-only workflows with no batch mode

**Exemplar Patterns:**
- stdin/stdout as primary I/O channels
- Structured output (JSON, CSV) alongside human-readable
- Library core separate from CLI wrapper
- Exit codes that convey status

**Language Notes:**
- Python: `if __name__ == "__main__"` pattern, `click`/`typer` for CLI
- Go: Separate `cmd/` from `pkg/` or `internal/`
- Node: Export functions, don't just execute on import

---

## 4. Rule of Separation

**Definition:** Separate policy from mechanism; separate interfaces from engines.

**Code Smells:**
- Business logic mixed with I/O (database queries inside domain functions)
- Configuration hard-coded in logic files
- UI rendering interleaved with data processing
- HTTP handler functions containing business rules

**Exemplar Patterns:**
- MVC/hexagonal/clean architecture separation
- Configuration loaded at startup, passed as parameters
- Pure functions for business logic, impure shells for I/O
- Repository pattern for data access

**Language Notes:**
- Python: Dependency injection via constructor parameters
- Go: Interface-based dependency inversion
- React: Container/presentation component split

---

## 5. Rule of Simplicity

**Definition:** Design for simplicity; add complexity only where you must.

**Code Smells:**
- Frameworks used where a simple function suffices
- Abstract factory patterns for a single implementation
- Configuration systems more complex than the feature
- "Just in case" code paths never exercised

**Exemplar Patterns:**
- Flat is better than nested
- Functions over classes when no state needed
- Direct dependency over indirection layers
- Features removed, not just disabled

---

## 6. Rule of Parsimony

**Definition:** Write a big program only when it is clear by demonstration that nothing else will do.

**Code Smells:**
- Monolithic applications that could be smaller tools
- Libraries that do too many things
- "Swiss army knife" modules
- Features no one uses but everyone maintains

**Exemplar Patterns:**
- Small, focused tools that do one thing
- Libraries with narrow scope and clear boundaries
- Lean dependency trees

---

## 7. Rule of Transparency

**Definition:** Design for visibility to make inspection and debugging easier.

**Code Smells:**
- Silent failures (catch-and-ignore)
- State changes without logging
- Hidden side effects
- No way to observe internal state during debugging

**Exemplar Patterns:**
- Structured logging at key decision points
- Observable state (metrics, health checks)
- Dry-run / verbose modes
- Intermediate results accessible for inspection

---

## 8. Rule of Robustness

**Definition:** Robustness is the child of transparency and simplicity.

**Code Smells:**
- Bare `except` / `catch` clauses
- Assuming network calls always succeed
- No input validation at system boundaries
- Race conditions from shared mutable state

**Exemplar Patterns:**
- Explicit error types and handling
- Graceful degradation on partial failure
- Input validation at boundaries, trust internally
- Timeouts on all external calls

---

## 9. Rule of Representation

**Definition:** Fold knowledge into data so program logic can be stupid and robust.

**Code Smells:**
- Long `if/elif/else` chains that could be lookup tables
- Business rules encoded in control flow
- Hard-coded values that should be configuration
- State machines implemented as nested conditionals

**Exemplar Patterns:**
- Configuration files/tables driving behavior
- Data-driven dispatch (maps/dicts of handlers)
- Schema definitions for validation
- State machines as explicit data structures

---

## 10. Rule of Least Surprise

**Definition:** In interface design, always do the least surprising thing.

**Code Smells:**
- `delete()` that archives instead of deleting
- `get_user()` that modifies database state
- Boolean parameters that reverse function meaning
- Inconsistent return types (sometimes list, sometimes None)

**Exemplar Patterns:**
- Method names match behavior exactly
- Consistent return types
- Standard library idioms followed
- Side effects explicit in naming (`update_and_notify`)

---

## 11. Rule of Silence

**Definition:** When a program has nothing surprising to say, it should say nothing.

**Code Smells:**
- "Starting..." / "Done!" messages on every operation
- Logging at INFO level for routine operations
- Progress bars for sub-second operations
- Banner/ASCII art on startup

**Exemplar Patterns:**
- Silent on success, verbose on failure
- Logging at appropriate levels (DEBUG for routine, WARN for concerns)
- Quiet by default, verbose via flag (`-v`)

---

## 12. Rule of Repair

**Definition:** When you must fail, fail noisily and as soon as possible.

**Code Smells:**
- Swallowed exceptions
- Default values that mask errors
- Continuing execution after inconsistent state
- Error messages without context

**Exemplar Patterns:**
- Fail-fast validation
- Error messages include what, why, and how to fix
- Assertions for invariants
- Structured error types with context

---

## 13. Rule of Economy

**Definition:** Programmer time is expensive; conserve it in preference to machine time.

**Code Smells:**
- Hand-rolled parsers for standard formats
- Custom build systems
- NIH syndrome (reimplementing well-solved problems)
- Premature optimization at the cost of readability

**Exemplar Patterns:**
- Standard libraries and well-maintained dependencies
- Code generation for boilerplate
- Higher-level languages where performance isn't critical
- Automation of repetitive tasks

---

## 14. Rule of Generation

**Definition:** Avoid hand-hacking; write programs to write programs when you can.

**Code Smells:**
- Copy-pasted boilerplate across files
- Hand-maintained serialization code
- Manual API client generation
- Repetitive test setup that could be generated

**Exemplar Patterns:**
- Code generators for repetitive patterns
- Schema-driven code (OpenAPI, protobuf, GraphQL codegen)
- Template engines for boilerplate
- Macros/metaprogramming where appropriate

---

## 15. Rule of Optimization

**Definition:** Prototype before polishing. Get it working before you optimize it.

**Code Smells:**
- Micro-optimizations without benchmarks
- Custom data structures for standard operations
- Caching without profiling evidence
- Assembly/unsafe blocks without justification

**Exemplar Patterns:**
- Benchmarks before and after optimization
- Profiler-guided optimization
- Clear comments explaining why optimization was necessary
- Simple baseline with optimized hot paths

---

## 16. Rule of Diversity

**Definition:** Distrust all claims for "one true way."

**Code Smells:**
- Only one way to configure the application
- Hard-coded to single database/queue/storage backend
- No extension points for alternative implementations
- Monolingual systems where polyglot would serve better

**Exemplar Patterns:**
- Strategy/adapter patterns for swappable backends
- Configuration-driven behavior selection
- Plugin architectures
- Multiple interface options (CLI, API, library)

---

## 17. Rule of Extensibility

**Definition:** Design for the future, because it will be here sooner than you think.

**Code Smells:**
- Version-specific behavior with no migration path
- Hard-coded limits or magic numbers
- No plugin or hook system
- Breaking changes without versioning

**Exemplar Patterns:**
- Semantic versioning
- Plugin/middleware architectures
- Configuration over code for tunable behavior
- Forward-compatible data formats (extra fields ignored, not rejected)
