# IT-3: Synthesis Quality Test Context

## Test Code Sample

**File:** `/Users/leegonzales/Projects/leegonzales/prompt-evolve/pkg/mutations/strategies.go`

**Purpose:** Test both Codex and Gemini peer review on the same code to evaluate synthesis quality

**Code Focus:** Intelligent LLM-powered mutation strategies for prompt evolution

### Key Code Elements (Lines 1-150)

```go
package mutations

// LLMProvider interface for mutation operations
type LLMProvider interface {
    Generate(ctx context.Context, prompt string) (string, error)
    GenerateWithSystem(ctx context.Context, system, prompt string) (string, error)
}

// MutationStrategy defines different types of intelligent mutations
type MutationStrategy int

const (
    SemanticImprovement MutationStrategy = iota
    StyleVariation
    SpecificityAdjustment
    StructuralReorganization
    CreativeExploration
)

// Mutator provides intelligent LLM-powered mutations
type Mutator struct {
    provider LLMProvider
    model    string
    mutex    sync.RWMutex

    // Configuration
    temperature       float64
    maxRetries        int
    contextWindow     int
    preserveLength    bool
    creativityLevel   float64
}

// Mutate applies intelligent mutation to a prompt using LLM reasoning
func (m *Mutator) Mutate(ctx context.Context, prompt string, strategy MutationStrategy) (string, error) {
    // Validation
    if strings.TrimSpace(prompt) == "" {
        return prompt, fmt.Errorf("cannot mutate empty prompt")
    }

    m.mutex.RLock()
    defer m.mutex.RUnlock()

    // Choose mutation approach based on strategy
    systemPrompt := m.getSystemPrompt(strategy)
    userPrompt := m.buildMutationPrompt(prompt, strategy)

    // Attempt mutation with retries
    for attempt := 0; attempt < m.maxRetries; attempt++ {
        result, err := m.provider.GenerateWithSystem(ctx, systemPrompt, userPrompt)
        if err != nil {
            if attempt == m.maxRetries-1 {
                return "", fmt.Errorf("mutation failed after %d attempts: %w", m.maxRetries, err)
            }
            continue
        }

        // Validate and clean the result
        mutated := m.cleanMutationResult(result, prompt)
        if mutated != "" && mutated != prompt {
            return mutated, nil
        }
    }

    return "", fmt.Errorf("mutation produced no valid result after %d attempts", m.maxRetries)
}

// getSystemPrompt returns strategy-specific system prompts (lines 106-150+)
// Each MutationStrategy has detailed prompt engineering guidelines
```

## Review Question

**Prompt for both AIs:**

"Review this Go code implementing intelligent LLM-powered mutation strategies for prompt evolution. Focus on:

1. **Architecture & Design:** Is the interface abstraction appropriate? Are the mutation strategies well-designed?
2. **Error Handling:** Are errors handled properly? Any edge cases missed?
3. **Concurrency:** Is the mutex usage correct? Any race condition concerns?
4. **LLM Integration:** Is the retry logic sound? Are the system prompts effective?
5. **Code Quality:** Any improvements or concerns?"

## Expected Synthesis Elements

### 1. Convergence (Agreement)
Both AIs should identify similar:
- Overall architecture quality
- Obvious issues or strengths
- Standard Go patterns

### 2. Divergence (Different Perspectives)
Different insights such as:
- Codex: May focus on implementation details
- Gemini: May consider broader patterns
- Different prioritization of concerns

### 3. Complementary Insights
Unique observations:
- Issues one AI catches that the other misses
- Different suggestions for improvement
- Alternative approaches from different perspectives

## Test Execution Plan

1. **Invoke Codex peer review** with context
2. **Invoke Gemini peer review** with same context
3. **Analyze synthesis:**
   - Document convergence points
   - Document divergence points
   - Document complementary insights
4. **Score synthesis quality:** 1-5 scale based on:
   - Presence of all 3 elements (convergence, divergence, complementary)
   - Specificity of insights (not generic)
   - Actionable recommendations
   - Value added beyond single perspective
