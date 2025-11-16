# prompt-evolve Design Specification

**Version:** 1.0
**Date:** 2025-05-26
**Project:** Evolutionary Prompt Optimization Framework
**Location:** `/Users/leegonzales/Projects/leegonzales/prompt-evolve/`

---

## Design Overview

prompt-evolve is designed as a genetic algorithm framework that uses Large Language Models to intelligently evolve and optimize prompts. The system applies biological evolution principles (mutation, crossover, selection) with LLM-powered semantic understanding.

---

## Architectural Principles

### 1. Unix Philosophy
- **Small, composable tools:** Each CLI command does one thing well
- **Pipe-able components:** Tools can be chained together
- **Separation of concerns:** Mechanism (evolution) separated from policy (fitness criteria)
- **Transparency:** Observable evolution process with detailed logging

### 2. Three-Phase Pipeline Design

```
Phase 1: Bootstrap → Phase 2: Evolution → Phase 3: Evaluation
```

- **Phase 1 (prompt-bootstrap):** Generate initial high-quality prompt variants using Claude Opus
- **Phase 2 (prompt-evolve):** Apply genetic algorithms to evolve prompts across generations
- **Phase 3 (prompt-evaluate):** Use LLM judges to score and rank final prompts

### 3. Pluggable Provider Architecture

The system must support multiple LLM providers through a unified interface:
- Provider registry pattern for extensibility
- Provider-agnostic core evolution logic
- Middleware support (retry, rate limiting, logging)

---

## Core Components

### 1. Evolution Engine (`pkg/evolution`)

**Responsibilities:**
- Orchestrate the genetic algorithm
- Initialize population
- Coordinate evaluation, selection, mutation, crossover
- Implement elitism-based survival
- Track evolution statistics
- Adapt parameters based on diversity

**Key Algorithm:**
```
FOR each generation:
  1. Evaluate fitness (parallel)
  2. Calculate diversity
  3. Adapt mutation/crossover rates
  4. Select parents (rank-based)
  5. Generate offspring (crossover + mutation)
  6. Evaluate offspring
  7. Select survivors (elitism)
  8. Update statistics
```

**Adaptive Parameters:**
- Mutation rate: Decreases over generations, increases when diversity is low
- Crossover rate: Adapts based on population diversity
- Selection pressure: Increases when diversity is too low

### 2. Mutation System (`pkg/mutations`)

**Design Intent:** Semantic mutations powered by LLMs, not random character changes

**Five Mutation Strategies:**
1. **Semantic Improvement** - Enhance clarity while preserving meaning
2. **Style Variation** - Change tone/format/presentation
3. **Specificity Adjustment** - Add or remove detail levels
4. **Structural Reorganization** - Improve flow and organization
5. **Creative Exploration** - Explore alternative approaches

**Four Crossover Strategies:**
- Intelligent combination of parent prompts
- LLM-powered semantic blending
- Strategy selection based on parent fitness

**Expected Implementation:**
- Each strategy implemented as a separate function
- Context-aware mutations that understand prompt semantics
- Provider-agnostic (works with any LLM)

### 3. Fitness Evaluation (`pkg/fitness`)

**Multi-Criteria Framework:**

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Clarity | 30% | How clear and well-structured |
| Specificity | 30% | How specific and detailed |
| Conciseness | 20% | How concise and to-the-point |
| Relevance | 20% | How relevant to the task |

**Design Requirements:**
- Extensible fitness functions
- Weighted scoring system
- Support for custom criteria
- Option for LLM-based evaluation or heuristics

### 4. Population Management (`pkg/population`)

**Responsibilities:**
- Thread-safe population tracking
- Parent selection using rank-based probabilities
- Diversity calculation (Levenshtein distance)
- Generation statistics
- Elitism enforcement

**Expected Data Structures:**
- Population as slice of Individuals
- Each Individual contains: Prompt, Fitness, Metadata
- Thread-safe with `sync.RWMutex`

### 5. Provider System (`pkg/providers`)

**Architecture Pattern:** Registry + Middleware

**Components:**
- `Provider` interface with methods: `Complete()`, `Chat()`, `CountTokens()`
- `Registry` for provider discovery and registration
- Middleware wrappers for cross-cutting concerns
- Provider-specific implementations (Claude, OpenAI)

**Design Goals:**
- Easy to add new providers
- Provider-agnostic core logic
- Consistent error handling
- Token counting abstraction

### 6. Cost Tracking (`pkg/cost`)

**Purpose:** Monitor and limit LLM API costs

**Features:**
- Token usage tracking per generation
- Budget limits with early stopping
- Provider-specific pricing
- Comprehensive cost reporting

### 7. Core Abstractions (`pkg/api`, `pkg/core`)

**pkg/api - Data Types:**
- `Individual` - A single prompt with fitness
- `EvolutionConfig` - Configuration for evolution run
- `EvolutionResult` - Results of evolution including history
- `GenerationStats` - Statistics per generation

**pkg/core - Interfaces:**
- `Mutator` - Apply mutation to prompt
- `Evaluator` - Score prompt fitness
- `Selector` - Select parents from population
- `Observable` - Emit evolution events

---

## Data Flow

### Bootstrap Phase
```
User Seed Prompt
  → Claude Opus API
  → Generate N diverse variants
  → Output: population.json
```

### Evolution Phase
```
Load population.json
  → Initialize Evolution Engine
  → FOR each generation:
      - Parallel fitness evaluation
      - Diversity calculation
      - Parameter adaptation
      - Parent selection (rank-based)
      - Offspring generation (crossover + mutation)
      - Offspring evaluation
      - Survivor selection (elitism)
      - Statistics tracking
  → Output: best_prompt.txt + evolution_history.json
```

### Evaluation Phase
```
Load evolved prompts
  → LLM Judge evaluation
  → Detailed scoring
  → Ranking and comparison
  → Output: evaluation_report.md
```

---

## Thread Safety Requirements

- **Population:** Protected by `sync.RWMutex`
- **Random number generation:** Use `crypto/rand` for security
- **Concurrent evaluations:** Safe parallel fitness evaluation
- **Shared state:** Minimize shared mutable state

---

## Configuration Design

**Multiple Configuration Sources (in priority order):**
1. Command-line flags (highest priority)
2. TOML configuration file
3. Environment variables
4. Programmatic defaults (lowest priority)

**Required Configuration:**
- Provider selection (claude, openai)
- API keys (via environment)
- Population size
- Number of generations
- Mutation/crossover rates (optional, can use adaptive defaults)
- Fitness weights
- Budget limits

---

## Testing Strategy

**Three-Tier Testing:**

1. **Unit Tests:** Core logic (mutations, selection, fitness)
2. **Integration Tests:** Provider interactions with mocks
3. **End-to-End Tests:** Real LLM API calls with small populations

**Test Data:**
- Mock providers in `test/mocks/`
- Test fixtures in `test/fixtures/`
- E2E tests in `test/e2e/`

---

## Performance Expectations

- **Parallelization:** Fitness evaluations run concurrently
- **Adaptive tuning:** Reduce unnecessary exploration as evolution progresses
- **Elitism:** Ensure monotonic fitness improvement (best never degrades)
- **Diversity tracking:** Prevent premature convergence
- **Cost awareness:** Stop if budget exceeded

**Target Performance:**
- Fitness improvement: >10% over generations
- Time per generation: <30 seconds (with parallel evaluation)
- Cost per run: Controllable via budget limits

---

## CLI Design

### prompt-bootstrap
```bash
prompt-bootstrap --seed "prompt" --count 10 --output population.json
```

### prompt-evolve
```bash
prompt-evolve --input population.json --generations 20 --output results/
```

### prompt-evaluate
```bash
prompt-evaluate --input results/best_prompt.txt --criteria custom_fitness.toml
```

### prompt-evolve-tui
```bash
prompt-evolve-tui --config evolution.toml
# Real-time terminal UI visualization
```

---

## Package Dependencies

### Expected Package Structure:
```
cmd/
  prompt-bootstrap/    - Phase 1 CLI
  prompt-evolve/       - Phase 2 CLI
  prompt-evaluate/     - Phase 3 CLI
  prompt-evolve-tui/   - Terminal UI CLI

pkg/
  api/                 - Core types and interfaces
  core/                - Unix-philosophy interfaces
  evolution/           - Evolution engine
  mutations/           - Mutation strategies
  fitness/             - Fitness evaluation
  population/          - Population management
  providers/           - LLM provider abstraction
  cost/                - Cost tracking
  evaluation/          - Prompt evaluation
  history/             - Evolution history
  tui/                 - Terminal UI components

test/
  mocks/               - Mock providers
  fixtures/            - Test data
  e2e/                 - Integration tests
  helpers/             - Test utilities
```

### Key Dependencies Between Packages:
- `cmd/*` → depends on all `pkg/*` packages
- `pkg/evolution` → depends on `api`, `core`, `mutations`, `fitness`, `population`, `cost`
- `pkg/mutations` → depends on `providers`, `api`
- `pkg/fitness` → depends on `api`, `providers`
- `pkg/providers` → standalone (minimal dependencies)
- `test/*` → depends on `pkg/*` for testing

---

## Extension Points

The design explicitly supports future extensions:

1. **New Mutation Strategies:** Implement `Mutator` interface
2. **New Providers:** Implement `Provider` interface and register
3. **Custom Fitness Functions:** Implement `Evaluator` interface
4. **New Selection Methods:** Implement `Selector` interface
5. **Middleware:** Wrap providers with cross-cutting concerns

---

## Non-Functional Requirements

### Security
- API keys stored in environment variables (never in code)
- Secure random number generation using `crypto/rand`
- No logging of sensitive API keys

### Observability
- Detailed logging at configurable levels
- Evolution events via Observer pattern
- Statistics tracking per generation
- Cost tracking and reporting

### Reliability
- Graceful error handling
- Retry logic with exponential backoff
- Rate limiting respect
- Budget limits to prevent runaway costs

### Maintainability
- Clear separation of concerns
- Comprehensive tests (unit, integration, e2e)
- Documentation in code and separate docs
- Examples for common use cases

---

## Success Metrics

The implementation should demonstrate:

- **Effectiveness:** >10% fitness improvement over generations
- **Semantic Understanding:** Mutations that preserve meaning while improving clarity
- **Production Readiness:** Handles real LLM APIs, rate limits, errors
- **Extensibility:** Easy to add new providers and strategies
- **Cost Control:** Stays within budget limits
- **Thread Safety:** No race conditions in concurrent operations

---

**End of Design Specification**
