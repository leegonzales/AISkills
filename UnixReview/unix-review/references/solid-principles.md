# SOLID Principles — Mapped to Unix Review Dimensions

The 5 SOLID principles complement the Unix philosophy at the module/class level. Each maps to one or more of the 8 scoring dimensions.

---

## Single Responsibility Principle (SRP) → Modularity

**Principle:** A class/module should have one, and only one, reason to change.

**Dimension Mapping:** Modularity (primary)

**What to Look For:**
- Classes with multiple `save_`, `render_`, `validate_` method families → multiple responsibilities
- Modules that change when unrelated requirements change
- Files longer than ~300 lines often signal mixed responsibilities
- Constructor with many unrelated dependencies

**Positive Signals:**
- Each module/class has a clear, single-sentence purpose
- Changes to one feature don't ripple across unrelated files
- Test files mirror source files 1:1

**Pragmatic Exceptions:**
- Data transfer objects / value types naturally combine data + validation
- Small utility modules may group related helpers (OK if cohesive)
- Framework conventions sometimes force mixed concerns (e.g., Django models with save logic)

**Scoring Impact:**
- SRP violations directly reduce Modularity score
- Severe violations (God classes) cap Modularity at ~40

---

## Open/Closed Principle (OCP) → Extensibility

**Principle:** Software entities should be open for extension, closed for modification.

**Dimension Mapping:** Extensibility (primary)

**What to Look For:**
- Adding features requires modifying existing switch/case statements
- New behavior types require touching core files
- No plugin, middleware, or hook mechanisms
- Hard-coded behavior that should be configurable

**Positive Signals:**
- Strategy pattern or similar for behavioral variation
- Middleware/plugin pipelines
- Event-driven extension points
- New features added as new files, not modifications to existing ones

**Pragmatic Exceptions:**
- Small projects (< 5 files) don't need formal extension mechanisms
- YAGNI trumps OCP—don't add extension points "just in case"
- Sometimes modifying existing code IS the simplest approach

**Scoring Impact:**
- OCP violations reduce Extensibility score
- Absence of any extension mechanism in a large project caps Extensibility at ~50

---

## Liskov Substitution Principle (LSP) → Extensibility

**Principle:** Objects of a supertype should be replaceable with objects of a subtype without altering program correctness.

**Dimension Mapping:** Extensibility (secondary)

**What to Look For:**
- Subclasses that throw `NotImplementedError` for inherited methods
- `isinstance` checks to handle subtypes differently
- Overridden methods that change return type or error behavior
- Inheritance hierarchies where children violate parent contracts

**Positive Signals:**
- Subtypes honor all contracts of their supertypes
- Composition preferred over inheritance
- Interfaces/protocols define contracts, implementations vary freely
- No `isinstance` checks in consumer code

**Pragmatic Exceptions:**
- Some frameworks encourage inheritance patterns that bend LSP (acceptable if framework-idiomatic)
- Abstract base classes with `NotImplementedError` are OK as interface definitions
- Duck-typed languages naturally relax formal LSP

**Scoring Impact:**
- LSP violations are a secondary factor in Extensibility
- Severe violations (broken substitutability) reduce both Extensibility and Robustness

---

## Interface Segregation Principle (ISP) → Composability

**Principle:** No client should be forced to depend on methods it does not use.

**Dimension Mapping:** Composability (primary)

**What to Look For:**
- Interfaces with 10+ methods where most clients use 2-3
- "Fat" base classes that force empty method implementations
- Modules that import a large dependency for one small function
- APIs where consumers must understand the full surface to use any part

**Positive Signals:**
- Small, focused interfaces (1-3 methods each)
- Role-based interfaces (`Readable`, `Writable`, `Closeable`)
- Consumers depend on narrow slices, not full objects
- Utility functions importable individually

**Pragmatic Exceptions:**
- Standard library interfaces are intentionally broad (acceptable)
- ORMs and framework base classes necessarily combine operations
- Convenience wrappers that aggregate narrow interfaces for common use cases

**Scoring Impact:**
- ISP violations directly reduce Composability score
- Fat interfaces that force unnecessary coupling cap Composability at ~50

---

## Dependency Inversion Principle (DIP) → Composability

**Principle:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Dimension Mapping:** Composability (primary), Extensibility (secondary)

**What to Look For:**
- Direct imports of concrete implementations in business logic
- Database/HTTP client instantiated inside domain functions
- No dependency injection (constructors create their own dependencies)
- Test files needing to mock internals because dependencies are hard-wired

**Positive Signals:**
- Constructor/function parameter injection
- Interfaces/protocols for external dependencies
- Configuration-driven wiring (composition root pattern)
- Easy to test with stubs/mocks

**Pragmatic Exceptions:**
- Pure utility functions don't need DI
- Small scripts and CLIs can wire directly (low cost of change)
- Over-abstracting stable dependencies (e.g., wrapping `os.path`) adds noise

**Scoring Impact:**
- DIP violations reduce Composability and testability
- Hard-wired dependencies in core logic cap Composability at ~55

---

## SOLID ↔ Dimension Summary

| SOLID Principle | Primary Dimension | Secondary Dimension |
|----------------|-------------------|---------------------|
| SRP | Modularity | — |
| OCP | Extensibility | — |
| LSP | Extensibility | Robustness |
| ISP | Composability | — |
| DIP | Composability | Extensibility |

Note: SOLID principles don't directly map to Clarity, Simplicity, Data-Drivenness, Robustness (except LSP), or AI-Readiness. Those dimensions are primarily covered by the Unix rules.
