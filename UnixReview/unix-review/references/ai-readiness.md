# AI-Readiness Dimension

The novel cross-cutting dimension that evaluates how well a codebase supports AI-assisted development—navigation, understanding, modification, and verification by AI agents.

---

## The AI-Age Thesis

> The Rule of Representation in the AI age: **Fold knowledge into structure so AI agents can be effective and safe.**

Code that is good for humans to read is not automatically good for AI to work with. AI agents have specific constraints:
- **Context windows** limit how much code can be loaded at once
- **Implicit conventions** that humans absorb through team culture are invisible to agents
- **Side effects** that experienced developers "just know about" become landmines
- **Scriptable interfaces** are the difference between an AI that can help and one that can't

AI-Readiness isn't about adding AI-specific accommodations. It's about taking the Unix philosophy seriously in an age where your most prolific collaborator is an AI agent.

---

## The 5 Sub-Scores

### 1. Navigability (0-100)

**Question:** Can an agent find what it needs quickly?

**High Score (75-100):**
- Logical directory structure matching domain concepts
- File names that describe contents accurately
- Entry points are obvious (main, index, app, cli)
- CLAUDE.md, README, or similar providing codebase maps
- Consistent file organization patterns across modules

**Low Score (0-40):**
- Flat directory with 50+ files at one level
- Generic file names (`utils.py`, `helpers.ts`, `common.go`)
- Multiple entry points with no documentation of which is primary
- Inconsistent organization (some features split by type, others by domain)
- No project documentation explaining structure

**Anti-Patterns:**
- `utils/` or `helpers/` directories as dumping grounds
- File names that don't hint at contents (`stuff.py`, `new_file.ts`)
- Deeply nested directories with single files
- Index files that re-export everything (barrel files that obscure location)

---

### 2. Contextual Independence (0-100)

**Question:** Can a file be understood without reading the entire codebase?

**High Score (75-100):**
- Files include their own type definitions or import them explicitly
- Functions document their contracts (parameters, return values, side effects)
- No reliance on global state or ambient context
- Module-level docstrings explain purpose and usage
- Dependencies are explicit, not implicit

**Low Score (0-40):**
- Heavy reliance on global variables or singleton state
- Functions that depend on "setup" having been called elsewhere
- Implicit contracts ("this function assumes X was validated upstream")
- Circular imports revealing tangled dependencies
- Files that only make sense after reading 5+ other files

**Anti-Patterns:**
- Monkey-patching or runtime modification of imports
- Convention-based behavior (`_private` methods called externally)
- Magic middleware that mutates request objects in non-obvious ways
- Import-time side effects (code runs on import)

---

### 3. Modifiability (0-100)

**Question:** Can changes be made safely with predictable effects?

**High Score (75-100):**
- Changes to one module don't cascade to unrelated modules
- Test coverage provides safety net for modifications
- Clear boundaries—public API vs internal implementation
- Type system catches breaking changes at compile time
- Small, focused files (< 300 lines typical)

**Low Score (0-40):**
- Changing one function breaks tests in unrelated modules
- No test coverage on critical paths
- Public and private APIs are indistinguishable
- Large files (1000+ lines) with interleaved concerns
- Shared mutable state creates invisible coupling

**Anti-Patterns:**
- Files over 500 lines (exceed typical AI context window efficiency)
- Functions with 10+ parameters (hard to modify safely)
- Deep inheritance hierarchies (changes ripple unpredictably)
- Implicit ordering dependencies ("must call A before B")

---

### 4. Agent Composability (0-100)

**Question:** Can AI agents interact with this code programmatically?

**High Score (75-100):**
- CLI interface with `--help`, structured output (JSON), exit codes
- Scriptable API (functions callable without UI)
- Makefile, justfile, or task runner with standard targets
- CI/CD pipeline that agents can trigger or inspect
- Configuration via files or environment (not interactive prompts)

**Low Score (0-40):**
- Interactive-only interface (no batch/scriptable mode)
- GUI-only configuration
- No build/test/lint automation
- Manual deployment processes
- No way to invoke functionality from outside the application

**Anti-Patterns:**
- Required interactive prompts with no `--yes` or `--non-interactive` flag
- Configuration only via GUI settings panels
- Build processes that require manual steps ("then open the IDE and click...")
- Outputs only in human-readable format (no `--json` option)

---

### 5. Inspectability (0-100)

**Question:** Can an agent verify its changes are correct?

**High Score (75-100):**
- Comprehensive test suite with clear pass/fail
- Type checking catches errors before runtime
- Linting rules enforce conventions
- Health checks and smoke tests for running services
- Clear error messages that explain what went wrong

**Low Score (0-40):**
- No tests, or tests that pass regardless
- No type checking or linting
- Errors are generic ("something went wrong")
- No way to verify a change without manual testing
- Silent failures that only surface in production

**Anti-Patterns:**
- Tests that mock everything (verify nothing about real behavior)
- `# type: ignore` or `@ts-ignore` scattered throughout
- Error handling that swallows context
- No CI pipeline to validate changes

---

## Scoring the AI-Readiness Dimension

The overall AI-Readiness score is the average of the 5 sub-scores:

```
ai_readiness = (navigability + contextual_independence + modifiability + agent_composability + inspectability) / 5
```

**Interpretation:**
| Score | Level | Meaning |
|-------|-------|---------|
| 85+ | AI-Native | Built with AI collaboration in mind |
| 70-84 | AI-Friendly | Works well with AI agents, minor friction |
| 55-69 | AI-Tolerant | AI can help but hits regular friction |
| 40-54 | AI-Resistant | Significant barriers to AI collaboration |
| <40 | AI-Hostile | AI agents will struggle and make mistakes |

---

## Common Remediation Patterns

### Quick Wins (Low Effort, High Impact)
1. **Add a CLAUDE.md** or project README explaining structure, entry points, and conventions
2. **Split large files** (>500 lines) into focused modules
3. **Add `--json` output** to CLI tools
4. **Add type annotations** to function signatures
5. **Create a Makefile** with `make test`, `make lint`, `make build` targets

### Medium Effort
1. **Eliminate global state** in favor of explicit parameter passing
2. **Add integration tests** for critical paths
3. **Document implicit conventions** that the team "just knows"
4. **Create scriptable interfaces** for interactive-only workflows
5. **Reduce file coupling** by making dependencies explicit

### Structural Changes
1. **Adopt hexagonal/clean architecture** to separate concerns
2. **Introduce dependency injection** to replace hard-wired dependencies
3. **Create a plugin system** for extensible behavior
4. **Implement structured logging** for observability
5. **Add schema validation** for configuration files

---

## The Feedback Loop

AI-Readiness creates a virtuous cycle:
1. Better structure → AI makes better changes
2. Better AI changes → fewer bugs, faster iteration
3. Faster iteration → more time for structural improvements
4. More structure → even better AI collaboration

The inverse is also true: AI-hostile code leads to AI mistakes, which leads to distrust of AI tools, which leads to no investment in AI-readiness. Breaking this cycle starts with the quick wins above.
