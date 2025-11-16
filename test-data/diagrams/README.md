# prompt-evolve Architecture Diagrams

This directory contains comprehensive architecture documentation and diagrams for the **prompt-evolve** codebase located at `/Users/leegonzales/Projects/leegonzales/prompt-evolve/`.

## Files Overview

### 1. architecture-overview.md
**Purpose:** High-level narrative description of the system architecture.

**Contains:**
- System purpose and philosophy
- Main components overview (cmd/, pkg/, test/)
- Key abstractions and patterns
- Data flow overview for all three phases (Bootstrap, Evolution, Evaluation)
- Design patterns employed
- Thread safety and performance characteristics
- Proven results and metrics

**Use this when:** You need to understand the overall system design and architectural decisions.

---

### 2. architecture-diagram.mmd
**Purpose:** High-level component relationships and system boundaries.

**Contains:**
- Mermaid diagram showing all major packages
- Component groupings (CLI Tools, Core Library, External Services, Testing)
- Package relationships and dependencies
- Data flow through the main pipeline
- Color-coded component categories

**Use this when:** You need a quick visual overview of how packages relate to each other.

**To render:** Use a Mermaid viewer (VS Code extension, Mermaid Live Editor, or GitHub)

---

### 3. component-diagram.mmd
**Purpose:** Detailed breakdown of internal package structure.

**Contains:**
- Mermaid diagram showing individual modules and their contents
- Key types and interfaces per package
- Method signatures for major components
- Implementation details for each package
- Testing infrastructure breakdown

**Use this when:** You need to understand the internal structure of specific packages or find where specific functionality lives.

**To render:** Use a Mermaid viewer (Note: This is a complex diagram, may require scrolling)

---

### 4. data-flow-diagram.mmd
**Purpose:** Sequence diagram showing the evolution process flow.

**Contains:**
- Mermaid sequence diagram of the complete evolution pipeline
- Step-by-step flow through Bootstrap, Evolution, and Evaluation phases
- Interactions between components during evolution
- Data structures at each stage
- Decision points (crossover, mutation)
- Adaptive parameter adjustments
- Cost tracking integration

**Use this when:** You need to understand how prompts flow through the system and how the genetic algorithm executes.

**To render:** Use a Mermaid viewer with sequence diagram support

---

## Quick Reference

### Key Packages

| Package | Purpose |
|---------|---------|
| `pkg/api` | Core types and interfaces (Individual, EvolutionConfig, etc.) |
| `pkg/core` | Unix-philosophy interfaces (Mutator, Evaluator, Selector) |
| `pkg/evolution` | LLMEngine - main genetic algorithm orchestrator |
| `pkg/mutations` | 5 mutation strategies + 4 crossover methods |
| `pkg/fitness` | Multi-criteria fitness evaluation |
| `pkg/population` | Thread-safe population management |
| `pkg/providers` | Pluggable LLM provider architecture (Claude, OpenAI) |
| `pkg/cost` | Token usage and budget tracking |

### CLI Commands

| Command | Purpose |
|---------|---------|
| `prompt-bootstrap` | Generate initial high-quality variants (Phase 1) |
| `prompt-evolve` | Run genetic evolution (Phase 2) |
| `prompt-evaluate` | Evaluate and rank prompts (Phase 3) |
| `prompt-evolve-tui` | Terminal UI for real-time visualization |

### Mutation Strategies

1. **SemanticImprovement** - Enhance clarity while preserving meaning
2. **StyleVariation** - Change tone/format
3. **SpecificityAdjustment** - Add/remove detail
4. **StructuralReorganization** - Improve flow and organization
5. **CreativeExploration** - Explore alternative approaches

### Fitness Metrics

- **Clarity** (30%) - How clear and well-structured
- **Specificity** (30%) - How specific and detailed
- **Conciseness** (20%) - How concise and to-the-point
- **Relevance** (20%) - How relevant to the task

## Viewing the Diagrams

### Online Viewers
- [Mermaid Live Editor](https://mermaid.live/) - Paste diagram code directly
- GitHub - View .mmd files directly in repositories
- GitLab - Native Mermaid rendering

### VS Code Extensions
- "Markdown Preview Mermaid Support" by Matt Bierner
- "Mermaid Editor" by tomoyukim

### Command Line
```bash
# Install mermaid-cli
npm install -g @mermaid-js/mermaid-cli

# Generate PNG from Mermaid files
mmdc -i architecture-diagram.mmd -o architecture-diagram.png
mmdc -i component-diagram.mmd -o component-diagram.png
mmdc -i data-flow-diagram.mmd -o data-flow-diagram.png
```

## Purpose of These Diagrams

These diagrams were created to support peer review testing of the **prompt-evolve** codebase. They provide:

1. **Orientation** - Help reviewers quickly understand system architecture
2. **Navigation** - Guide reviewers to relevant code sections
3. **Context** - Explain design decisions and patterns
4. **Documentation** - Serve as living documentation of the system

## Related Resources

- Source repository: `/Users/leegonzales/Projects/leegonzales/prompt-evolve/`
- README: `prompt-evolve/README.md`
- Contributing guide: `prompt-evolve/CONTRIBUTING.md`
- Status document: `prompt-evolve/STATUS.md`

## Updates

These diagrams are based on the codebase as of **November 12, 2025**. For the most current architecture, always refer to the source code as the single source of truth.
