# Unix Review

Evaluate codebases against Eric Raymond's 17 Unix rules and SOLID principles, with a novel AI-Readiness dimension.

## What It Does

Scores codebases across 8 dimensions that collapse 22 raw principles (17 Unix + 5 SOLID) into actionable categories:

| Dimension | Sources |
|-----------|---------|
| Modularity | Unix: Modularity, Parsimony; SOLID: SRP |
| Composability | Unix: Composition, Separation; SOLID: ISP, DIP |
| Clarity | Unix: Clarity, Transparency, Least Surprise |
| Simplicity | Unix: Simplicity, Economy, Optimization |
| Robustness | Unix: Robustness, Repair, Silence |
| Data-Drivenness | Unix: Representation, Generation |
| Extensibility | Unix: Extensibility, Diversity; SOLID: OCP, LSP |
| AI-Readiness | Novel cross-cutting dimension |

## Usage

### In Claude Code (Skill)

```
/unix-review                    # Quick scan of current project
/unix-review deep               # Full deep review
/unix-review ai-readiness       # Focus on AI-readiness dimension
```

### In Claude Projects

Add `UnixReview/unix-review/SKILL.md` to your project knowledge, then ask:

- "Review this codebase against Unix principles"
- "How AI-ready is this project?"
- "Do a deep architecture review"

## Operating Modes

| Mode | Depth | Best For |
|------|-------|----------|
| **Quick Scan** | 5-8 sampled files | Fast health check, PR reviews |
| **Deep Review** | All key files | Architecture decisions, refactoring planning |
| **AI-Readiness Audit** | AI-focused analysis | Preparing codebase for AI collaboration |

## Output Example

```
UNIX REVIEW — ARCHITECTURE PROFILE

Project: my-api
Architecture: Microservice | Calibration: Applied

DIMENSIONAL SCORES:
       Modularity: ████████░░ 82 - Clean service boundaries
    Composability: ██████░░░░ 63 - APIs compose but internal coupling
         Clarity: █████████░ 91 - Excellent naming and types
      Simplicity: ███████░░░ 74 - Some over-engineering in auth
      Robustness: ██████░░░░ 58 - Inconsistent error handling
  Data-Drivenness: █████░░░░░ 48 - Business rules in code, not config
   Extensibility: ████████░░ 79 - Good middleware pattern
    AI-Readiness: ███████░░░ 71 - Good structure, needs docs

OVERALL: ████████░░ 73 (Architecture-weighted)

TOP 5 RECOMMENDATIONS:
1. Extract validation rules from handlers into schema files
2. Add structured error types to replace string errors
3. Create CLAUDE.md with architecture overview
4. Split auth.ts (800 lines) into auth-strategies/ directory
5. Add --json flag to CLI management commands
```

## Architecture-Type Calibration

Scores are weighted by architecture type. A CLI tool values Simplicity more; a library values Composability more. The skill auto-detects architecture type and applies appropriate weights.

## AI-Readiness Sub-Scores

The AI-Readiness dimension breaks into 5 sub-criteria:
- **Navigability** — Can an agent find what it needs?
- **Contextual Independence** — Can a file be understood alone?
- **Modifiability** — Can changes be made safely?
- **Agent Composability** — Are there scriptable interfaces?
- **Inspectability** — Can an agent verify its changes?

## References

- `references/unix-rules.md` — All 17 ESR rules with code smells
- `references/solid-principles.md` — SOLID mapped to dimensions
- `references/scoring-rubric.md` — Score bands and calibration
- `references/ai-readiness.md` — AI-readiness deep dive
