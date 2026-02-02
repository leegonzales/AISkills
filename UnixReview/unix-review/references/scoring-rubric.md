# Scoring Rubric

Calibration guide for the 8 dimensions. Includes score bands, architecture-type weights, diagnostic combinations, and calibration examples.

---

## Score Bands

| Range | Label | Meaning |
|-------|-------|---------|
| 90-100 | Exceptional | Best-in-class; actively demonstrates the principle as a teaching example |
| 75-89 | Strong | Consistently follows the principle with minor lapses |
| 60-74 | Adequate | Generally follows the principle but with notable gaps |
| 40-59 | Weak | Significant violations; the principle is not consistently applied |
| 20-39 | Poor | Widespread violations; the principle is largely ignored |
| 0-19 | Absent | No evidence of the principle; actively hostile to it |

**Calibration notes:**
- Most production codebases land in 55-75 range
- Open-source projects with strong maintainers: 70-85
- Legacy codebases under active refactoring: 40-60
- Greenfield with experienced team: 65-80
- Avoid score inflation. A score of 70 means "genuinely good, room to improve."

---

## Architecture-Type Weight Tables

### CLI Tool
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Modularity | 15% | Moderate—CLIs can be simpler |
| Composability | 15% | Stdin/stdout/exit codes matter |
| Clarity | 15% | Users read help text and source |
| Simplicity | 15% | Core Unix value for tools |
| Robustness | 10% | Important but scope is narrow |
| Data-Drivenness | 10% | Config files, flags over hardcoded |
| Extensibility | 10% | Plugins nice but not essential |
| AI-Readiness | 10% | Scriptability = AI-friendliness |

### Library/SDK
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Modularity | 20% | Critical—consumers pick what they need |
| Composability | 20% | Libraries MUST compose |
| Clarity | 15% | API surface must be obvious |
| Simplicity | 10% | Some complexity justified for power |
| Robustness | 10% | Must not crash consumer apps |
| Data-Drivenness | 5% | Less critical for libs |
| Extensibility | 15% | Consumers need extension points |
| AI-Readiness | 5% | Less critical—humans design APIs |

### Web Application
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Modularity | 15% | Standard importance |
| Composability | 10% | Internal composition matters less |
| Clarity | 10% | Team reads this daily |
| Simplicity | 10% | Complexity creep is real |
| Robustness | 15% | User-facing = must handle errors |
| Data-Drivenness | 10% | Config-driven behavior |
| Extensibility | 15% | Features evolve constantly |
| AI-Readiness | 15% | AI will modify this code most |

### Microservice/API
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Modularity | 15% | Service boundaries matter |
| Composability | 20% | Services MUST compose via APIs |
| Clarity | 10% | Internal clarity standard |
| Simplicity | 10% | Each service should be simple |
| Robustness | 15% | Network failures are constant |
| Data-Drivenness | 10% | Schema-driven contracts |
| Extensibility | 10% | Versioned APIs |
| AI-Readiness | 10% | Standard importance |

### AI/ML Pipeline
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Modularity | 10% | Notebooks blur boundaries |
| Composability | 10% | Pipeline stages compose |
| Clarity | 15% | Reproducibility requires clarity |
| Simplicity | 10% | Complexity often justified |
| Robustness | 15% | Data quality failures are common |
| Data-Drivenness | 20% | The whole point |
| Extensibility | 10% | Model swapping, new features |
| AI-Readiness | 10% | Standard importance |

### Monorepo/Multi-Package
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Modularity | 20% | Package boundaries are the architecture |
| Composability | 15% | Packages must interop cleanly |
| Clarity | 10% | Cross-package conventions matter |
| Simplicity | 10% | Build complexity is a real cost |
| Robustness | 10% | Standard importance |
| Data-Drivenness | 10% | Shared schemas and configs |
| Extensibility | 15% | Adding packages should be easy |
| AI-Readiness | 10% | Navigating multi-package is hard for agents |

**Note:** For monorepos, consider also scoring individual sub-packages against their own architecture type for a more granular view.

---

## Dimension Gap Diagnostics

Patterns in score differentials that reveal specific architectural problems:

### High Modularity + Low Composability (>20pt gap)
**Diagnosis:** "Walled Garden" — modules have clean boundaries but poor interfaces between them. Each module works in isolation but the system doesn't compose.
**Root Cause:** Often results from teams working in silos, or from over-zealous encapsulation.
**Remediation:** Define explicit interface contracts. Add integration tests. Consider facade patterns.

### High Clarity + Low Simplicity (>20pt gap)
**Diagnosis:** "Well-Documented Complexity" — code is readable but unnecessarily complex. Comments and naming are excellent, but the underlying design is over-engineered.
**Root Cause:** Experienced developers who write clean code but over-abstract.
**Remediation:** Question every abstraction layer. Remove indirection that doesn't earn its keep.

### High Robustness + Low Clarity (>20pt gap)
**Diagnosis:** "Paranoid Code" — extensive error handling obscures the happy path. Defensive programming makes it hard to see what the code actually does.
**Root Cause:** Trauma from production incidents, or cargo-culting error handling patterns.
**Remediation:** Separate error handling from business logic. Use result types. Move validation to boundaries.

### High Extensibility + Low Modularity (>15pt gap)
**Diagnosis:** "Plugin Monolith" — extension mechanisms bolted onto a monolithic core. You can add plugins but can't refactor the core.
**Root Cause:** Extensibility added retroactively without restructuring.
**Remediation:** Refactor core into modules FIRST, then extension points become natural.

### High Simplicity + Low Robustness (>20pt gap)
**Diagnosis:** "Happy Path Code" — clean and simple but breaks on edge cases. No error handling, no validation, no defensive patterns.
**Root Cause:** Prototype-quality code in production, or "it works on my machine" development.
**Remediation:** Add boundary validation. Handle failure modes. Add error types.

### Low AI-Readiness + High Clarity (>15pt gap)
**Diagnosis:** "Human-Readable, Agent-Hostile" — good naming and comments but implicit conventions, no scriptable interfaces, large files that exceed context windows.
**Root Cause:** Code written for human team members, not considering AI collaboration.
**Remediation:** Split large files. Add CLI/API interfaces. Reduce implicit state. Add CLAUDE.md or similar context files.

### High Data-Drivenness + Low Clarity (>20pt gap)
**Diagnosis:** "Magic Configuration" — behavior driven by data/config but the config format and effects are opaque.
**Root Cause:** Configuration grew organically without documentation or schema.
**Remediation:** Add schema validation for config. Document configuration effects. Add config examples.

---

## Overall Score Calculation

```
overall = Σ (dimension_score × architecture_weight)
```

The overall score uses architecture-specific weights from the tables above.

**Interpretation:**
| Overall | Assessment |
|---------|-----------|
| 85+ | Excellent codebase, minor improvements only |
| 70-84 | Good codebase with clear improvement areas |
| 55-69 | Functional but needs architectural attention |
| 40-54 | Significant quality concerns |
| <40 | Major refactoring needed |

---

## Calibration Examples

### Example 1: Well-Structured Go CLI (Score: ~78)
- Modularity: 82 (clean package separation)
- Composability: 75 (good stdin/stdout, some hard-coded formats)
- Clarity: 85 (idiomatic Go, clear naming)
- Simplicity: 80 (minimal dependencies)
- Robustness: 70 (error handling present but inconsistent)
- Data-Drivenness: 72 (config file support, some hardcoded values)
- Extensibility: 65 (no plugin system, but clean interfaces)
- AI-Readiness: 74 (good structure, reasonable file sizes)

### Example 2: Legacy Django Monolith (Score: ~48)
- Modularity: 35 (fat models, mixed concerns)
- Composability: 40 (tightly coupled apps)
- Clarity: 55 (some good naming, inconsistent patterns)
- Simplicity: 45 (accumulated complexity)
- Robustness: 60 (Django handles much of this)
- Data-Drivenness: 50 (ORM-driven but logic in views)
- Extensibility: 40 (hard to add features without touching core)
- AI-Readiness: 42 (large files, implicit Django conventions)

### Example 3: Modern TypeScript Library (Score: ~82)
- Modularity: 90 (excellent module boundaries)
- Composability: 88 (tree-shakeable, narrow exports)
- Clarity: 85 (TypeScript types as documentation)
- Simplicity: 75 (some over-abstraction in type system)
- Robustness: 78 (good error types, boundary validation)
- Data-Drivenness: 70 (some config-driven, some hard-coded)
- Extensibility: 85 (plugin system, middleware support)
- AI-Readiness: 72 (good types but complex generics)
