# prompt-evolve Architecture Overview

## Purpose

**prompt-evolve** is an evolutionary prompt optimization framework inspired by Google DeepMind's AlphaEvolve. It uses genetic algorithms combined with Large Language Models to automatically evolve and optimize prompts for various tasks. The system applies biological evolution principles (mutation, crossover, selection) with LLM-powered intelligence to improve prompt effectiveness.

## Core Philosophy

The project follows Unix philosophy principles:
- Small, composable tools that do one thing well
- Pipe-able components for flexible workflows
- Separation of concerns (mechanism vs. policy)
- Transparency and observability

## Main Components

### 1. Command-Line Tools (cmd/)

Four specialized CLI tools that form an evolutionary pipeline:

- **prompt-bootstrap**: Phase 1 - Uses Claude Opus to generate initial high-quality prompt variants from a seed prompt
- **prompt-evolve**: Phase 2 - Applies genetic algorithms with LLM-powered mutations to evolve prompts across generations
- **prompt-evaluate**: Phase 3 - Uses LLM judges to score prompt effectiveness
- **prompt-evolve-tui**: Terminal UI for real-time visualization of the evolution process

### 2. Core Library (pkg/)

The library is organized into specialized packages following single-responsibility principle:

#### Core Abstractions (pkg/core, pkg/api)
- `pkg/api/`: Fundamental types and interfaces (Individual, EvolutionConfig, EvolutionResult, etc.)
- `pkg/core/`: Unix-philosophy interfaces (Mutator, Evaluator, Selector, Observable, etc.)

#### Evolution Engine (pkg/evolution)
- `LLMEngine`: Main evolution orchestrator that coordinates the genetic algorithm
- Adaptive parameter tuning (mutation/crossover rates adjust based on diversity)
- Elitism-based survival selection
- Thread-safe concurrent operations

#### Genetic Operations (pkg/mutations)
- **5 Semantic Mutation Strategies**:
  - Semantic Improvement: Enhance clarity while preserving meaning
  - Style Variation: Change tone/format
  - Specificity Adjustment: Add/remove detail
  - Structural Reorganization: Improve flow and organization
  - Creative Exploration: Explore alternative approaches

- **4 Crossover Strategies**:
  - Intelligent combination of parent prompts
  - Strategy selection based on parent fitness
  - LLM-powered semantic blending

#### Fitness Evaluation (pkg/fitness)
- Multi-criteria evaluation framework
- Metrics: clarity, specificity, conciseness, relevance
- Weighted scoring system
- Extensible for custom fitness functions

#### Population Management (pkg/population)
- Thread-safe population tracking
- Parent selection using rank-based probabilities
- Diversity calculation using Levenshtein distance
- Generation statistics tracking

#### LLM Providers (pkg/providers)
- Pluggable provider architecture (Registry pattern)
- Implementations for Claude and OpenAI
- Middleware support for retry, rate limiting, logging
- Provider-agnostic interface

#### Cost Tracking (pkg/cost)
- Token usage monitoring
- Budget management
- Provider-specific pricing
- Comprehensive cost reporting

#### Other Components
- `pkg/evaluation/`: LLM-powered prompt evaluation
- `pkg/history/`: Evolution history tracking
- `pkg/tui/`: Terminal UI components

### 3. Testing Infrastructure (test/)

- `test/e2e/`: End-to-end integration tests with real LLM APIs
- `test/mocks/`: Mock providers for unit testing
- `test/fixtures/`: Test data and helper functions
- `test/helpers/`: Testing utilities

## Key Abstractions

### 1. Individual
Represents a single prompt in the population with its fitness score.

### 2. Evolution Engine
Orchestrates the genetic algorithm:
- Initialize population
- Evaluate fitness
- Select parents
- Apply genetic operators (mutation, crossover)
- Replace population (elitism)
- Track statistics

### 3. Mutator
Applies intelligent LLM-powered mutations using context-aware strategies.

### 4. Fitness Evaluator
Scores prompts based on configurable criteria, can use heuristics or LLM judges.

### 5. Population Manager
Manages the collection of individuals, handles selection, replacement, and diversity tracking.

### 6. Provider
Abstracts LLM API calls, supporting multiple providers through a unified interface.

## Data Flow Overview

### Bootstrap Phase
```
User Seed Prompt
  -> Claude Opus (high-quality model)
  -> Generate N variants
  -> Output: Initial population JSON
```

### Evolution Phase
```
Initial Population
  -> FOR each generation:
       - Evaluate fitness (parallel)
       - Calculate diversity
       - Adapt mutation/crossover rates
       - Select parents (rank-based selection)
       - Generate offspring:
         * Apply crossover (probabilistic)
         * Apply mutation (probabilistic)
       - Evaluate offspring
       - Select survivors (elitism)
       - Update statistics
  -> Output: Best prompt + evolution history
```

### Evaluation Phase
```
Evolved Prompts
  -> LLM Judge evaluation
  -> Detailed metrics per prompt
  -> Ranking and comparison
  -> Output: Evaluation report
```

## Patterns and Design Principles

### 1. Genetic Algorithm Pattern
- Population-based search
- Fitness-guided selection
- Genetic operators (mutation, crossover)
- Elitism for preserving best solutions

### 2. Strategy Pattern
- Pluggable mutation strategies
- Pluggable crossover strategies
- Provider abstraction

### 3. Middleware Pattern
- Composable provider enhancements (retry, rate limiting)
- Separation of concerns

### 4. Observer Pattern
- Event-driven architecture for monitoring
- Decoupled components

### 5. Registry Pattern
- Provider discovery and management
- Extensible architecture

### 6. Adaptive Algorithms
- Mutation rate adapts based on generation number and diversity
- Crossover rate adapts based on population diversity
- Selection pressure adjusts when diversity is low

## Thread Safety

- `sync.RWMutex` protection in critical components
- Secure random number generation using `crypto/rand`
- Thread-safe population operations
- Concurrent fitness evaluations

## Configuration

Multiple configuration approaches:
- Environment variables for API keys and defaults
- TOML configuration files
- Command-line flags
- Programmatic configuration

## External Dependencies

### LLM Providers
- Claude (Anthropic API)
- OpenAI API
- Extensible to other providers

### Go Libraries
- Standard library (crypto/rand, sync, context, etc.)
- tiktoken-go for token counting
- Provider-specific SDKs

## Performance Characteristics

- Parallel fitness evaluation
- Adaptive parameter tuning reduces unnecessary exploration
- Elitism ensures monotonic fitness improvement
- Diversity tracking prevents premature convergence
- Cost tracking prevents budget overruns

## Proven Results

- 16.3% fitness improvement demonstrated in real OpenAI testing
- Semantic understanding: transforms simple prompts into sophisticated variants
- Production-tested with real LLM APIs
