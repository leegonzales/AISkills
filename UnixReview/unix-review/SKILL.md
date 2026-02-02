---
name: unix-review
description: Evaluate codebases against Eric Raymond's 17 Unix rules and SOLID principles, with a novel AI-Readiness dimension. Performs dimensional scoring across Modularity, Composability, Clarity, Simplicity, Robustness, Data-Drivenness, Extensibility, and AI-Readiness. Use for architecture reviews, codebase audits, or assessing how well code follows time-tested engineering principles.
environment: claude-code
---

# Unix Review

Evaluate codebases against the Unix philosophy and SOLID principles, with a novel AI-Readiness dimension for the age of AI-assisted development.

## Philosophy

**Code Quality = f(Codebase, Architecture Type, Team Context, AI Collaboration)**

The Unix philosophy—born from decades of building systems that survive—remains the most battle-tested framework for software design. Eric Raymond distilled it into 17 rules. SOLID principles complement them at the object/module level. Together they form a complete lens for evaluating code.

But we add a new dimension: **AI-Readiness**. Code that AI agents can navigate, understand, and safely modify is not a luxury—it's a competitive advantage. The same properties that make code good for humans (clarity, modularity, separation of concerns) make it good for AI, but AI has specific needs around context windows, file independence, and composable interfaces.

We collapse 17 Unix rules + 5 SOLID principles into **8 scoreable dimensions** to avoid overwhelming output while preserving full analytical coverage.

## Quick Start

**Quick Scan:** Reconnaissance → Score 8 dimensions → Top 5 recommendations
**Deep Review:** Full file analysis → Dimensional scoring with exemplars/violations → Architecture profile → Detailed remediation
**AI-Readiness Audit:** Focus on AI-Readiness sub-scores with specific remediation

## Operating Modes

### Mode 1: Quick Scan (default)

**When:** User says "review," "evaluate," or "how's this codebase?"

**Process:**
1. **Reconnaissance** (2-3 min exploration)
   - Read project structure, entry points, config files
   - Sample 5-8 representative files across the codebase
   - Identify architecture type
2. **Score** all 8 dimensions (0-100)
3. **Output** architecture profile with top 5 recommendations

### Mode 2: Deep Review

**When:** User says "deep review," "full audit," or "thorough analysis"

**Process:**
1. **Reconnaissance** (thorough exploration)
   - Map full project structure
   - Read all key files, not just samples
   - Trace dependency chains
   - Analyze test coverage patterns
2. **Score** all 8 dimensions with exemplar files and violation citations
3. **Diagnose** dimension gaps
4. **Output** full architecture profile with detailed remediation plan

### Mode 3: AI-Readiness Audit

**When:** User says "AI readiness," "agent friendly," or "how AI-ready is this?"

**Process:**
1. Standard reconnaissance
2. Deep-dive on AI-Readiness sub-scores:
   - Navigability, Contextual Independence, Modifiability, Agent Composability, Inspectability
3. Load `references/ai-readiness.md`
4. **Output** AI-readiness focused report with specific file-level recommendations

## Three-Phase Workflow

### Phase 1: Reconnaissance

Before scoring, understand the terrain:

1. **Structure scan:** `tree` or glob patterns to map the project
2. **Entry points:** Find main files, CLI entry, server bootstrap
3. **Architecture type detection:**
   - CLI Tool
   - Library/SDK
   - Web Application
   - Microservice/API
   - AI/ML Pipeline
   - Monorepo/Multi-package
4. **Sample files:** Read representative files across layers (entry, core logic, utilities, tests, config)
5. **Dependency analysis:** Check package manifest, imports, coupling patterns

### Phase 2: Dimensional Scoring

Score each dimension 0-100. Load `references/scoring-rubric.md` for calibration.

**The 8 Dimensions:**

| Dimension | Unix Rules | SOLID | What It Measures |
|-----------|-----------|-------|------------------|
| **Modularity** | Modularity, Parsimony | SRP | Do modules do one thing? Are interfaces narrow? |
| **Composability** | Composition, Separation | ISP, DIP | Can parts be recombined? Are concerns separated? |
| **Clarity** | Clarity, Transparency, Least Surprise | — | Can you understand what code does without tracing? |
| **Simplicity** | Simplicity, Economy, Optimization | — | Is complexity justified? Is premature optimization absent? |
| **Robustness** | Robustness, Repair, Silence | — | Does it handle failure gracefully? Is error reporting clear? |
| **Data-Drivenness** | Representation, Generation | — | Is complexity in data structures, not code? Is code generated where possible? |
| **Extensibility** | Extensibility, Diversity | OCP, LSP | Can behavior be extended without modifying internals? |
| **AI-Readiness** | (cross-cutting) | (cross-cutting) | Can AI agents navigate, understand, and safely modify this code? |

**For each dimension, identify:**
- **Exemplar:** Best file/module demonstrating this principle (with path:line)
- **Violation:** Worst offender against this principle (with path:line)
- **Score rationale:** 1-2 sentence justification

### Phase 3: Synthesis

1. Apply architecture-type calibration weights (load `references/scoring-rubric.md`)
2. Compute weighted overall score
3. Diagnose dimension gaps (high X + low Y = specific problem)
4. Generate top 5 actionable recommendations ranked by impact
5. Format output

## Architecture-Type Calibration

Different architectures emphasize different dimensions:

| Dimension | CLI | Library | Web App | Microservice | AI/ML |
|-----------|-----|---------|---------|--------------|-------|
| Modularity | 15% | 20% | 15% | 15% | 10% |
| Composability | 15% | 20% | 10% | 20% | 10% |
| Clarity | 15% | 15% | 10% | 10% | 15% |
| Simplicity | 15% | 10% | 10% | 10% | 10% |
| Robustness | 10% | 10% | 15% | 15% | 15% |
| Data-Drivenness | 10% | 5% | 10% | 10% | 20% |
| Extensibility | 10% | 15% | 15% | 10% | 10% |
| AI-Readiness | 10% | 5% | 15% | 10% | 10% |

## AI-Readiness Sub-Scores

AI-Readiness breaks into 5 sub-criteria (each 0-100, averaged for dimension score):

| Sub-Score | What It Measures |
|-----------|-----------------|
| **Navigability** | Can an agent find what it needs? Clear naming, logical structure, discoverable entry points |
| **Contextual Independence** | Can a file be understood without reading the entire codebase? Minimal implicit state |
| **Modifiability** | Can changes be made safely? Clear boundaries, good test coverage, predictable side effects |
| **Agent Composability** | Are there CLI interfaces, scriptable APIs, or tool-friendly boundaries? |
| **Inspectability** | Can an agent verify its changes? Observable state, testable contracts, clear feedback loops |

Load `references/ai-readiness.md` for detailed criteria and anti-patterns.

## Dimension Gap Diagnostics

Certain dimension combinations reveal specific architectural problems:

| Pattern | Diagnosis |
|---------|-----------|
| High Modularity + Low Composability | Good boundaries but poor interfaces—modules can't talk |
| High Clarity + Low Simplicity | Well-documented complexity—the docs explain unnecessary code |
| High Robustness + Low Clarity | Defensive programming obscuring logic—error handling hides the happy path |
| High Extensibility + Low Modularity | Plugin systems bolted onto monoliths—extension points but no seams |
| High Simplicity + Low Robustness | Happy-path code that breaks on edge cases |
| Low AI-Readiness + High Clarity | Human-readable but agent-hostile—implicit conventions, no scriptable interfaces |

## Output Format

```
UNIX REVIEW — ARCHITECTURE PROFILE

Project: [name]
Architecture: [detected type] | Calibration: [applied]
Files analyzed: [N] | Lines of code: [~N]

DIMENSIONAL SCORES:
       Modularity: ████████░░ 82 - [Brief interpretation]
    Composability: ██████░░░░ 63 - [Brief interpretation]
         Clarity: █████████░ 91 - [Brief interpretation]
      Simplicity: ███████░░░ 74 - [Brief interpretation]
      Robustness: ██████░░░░ 58 - [Brief interpretation]
  Data-Drivenness: █████░░░░░ 48 - [Brief interpretation]
   Extensibility: ████████░░ 79 - [Brief interpretation]
    AI-Readiness: ███████░░░ 71 - [Brief interpretation]

OVERALL: ████████░░ 73 (Architecture-weighted)

DIMENSION GAP DIAGNOSIS:
[Diagnostic based on score patterns — e.g., "High clarity but low
data-drivenness suggests logic encoded in control flow rather than
data structures. Consider configuration-driven approaches."]

EXEMPLARS (Best Practices Found):
1. [path:line] — [What it does well and which dimension]
2. [path:line] — [...]
3. [path:line] — [...]

VIOLATIONS (Highest Impact):
1. [path:line] — [What principle it violates and why it matters]
2. [path:line] — [...]
3. [path:line] — [...]

AI-READINESS DETAIL:
      Navigability: ████████░░ 80
  Context Independence: ██████░░░░ 65
     Modifiability: ███████░░░ 72
  Agent Composability: ██████░░░░ 60
    Inspectability: ████████░░ 78

TOP 5 RECOMMENDATIONS:
1. [Most impactful, actionable fix with specific files]
2. [...]
3. [...]
4. [...]
5. [...]
```

## Scoring Philosophy

- **Be calibrated, not generous.** 70 is genuinely good. 90+ is exceptional. 50 means real problems.
- **Architecture type matters.** A CLI tool doesn't need the composability of a library.
- **Dimension gaps are diagnostic.** The pattern of scores reveals more than any single number.
- **Cite specific files.** Every exemplar and violation must reference actual code with path:line.
- **Recommendations must be actionable.** "Improve modularity" is useless. "Extract the validation logic from `src/handlers/auth.ts:45-120` into a separate module" is actionable.

## Reference Files

Load as needed:
- **`references/unix-rules.md`** — All 17 ESR rules with code smells and exemplar patterns
- **`references/solid-principles.md`** — 5 SOLID principles mapped to the 8 dimensions
- **`references/scoring-rubric.md`** — Score bands, architecture weights, diagnostic combos, calibration examples
- **`references/ai-readiness.md`** — AI-age thesis, sub-criteria detail, anti-patterns

## Critical Principles

1. **Reconnaissance Before Judgment.** Never score without reading code. Sample broadly.
2. **Architecture-Type Calibration Is Non-Negotiable.** A microservice and a CLI have different priorities.
3. **Dimension Gaps Are Diagnostic.** The pattern matters more than the average.
4. **Cite or It Didn't Happen.** Every claim must reference specific files and lines.
5. **Actionable Over Exhaustive.** Five concrete recommendations beat twenty vague observations.
6. **The Unix Way Is Pragmatic.** Rules are heuristics, not laws. Flag violations but acknowledge justified exceptions.
7. **AI-Readiness Is About Structure, Not Comments.** Good structure for AI means good structure for humans—but the reverse isn't always true.
8. **Score the Code, Not the Idea.** Evaluate implementation quality, not whether the project concept is good.
