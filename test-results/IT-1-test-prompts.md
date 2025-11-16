# IT-1: Automatic Skill Triggering Test Prompts

## Test Objective
Verify that both Codex and Gemini peer review skills are automatically invoked by appropriate natural language prompts without requiring explicit skill commands.

## Test Prompts to Try

### Codex Triggering Attempts

1. **Direct mention:** "Get Codex's opinion on this code"
2. **Second opinion:** "I need a second opinion on this architecture"
3. **Review request:** "Can you review this code design?"
4. **Validation:** "Validate this implementation approach"
5. **Alternative:** "What would Codex think about this?"

### Gemini Triggering Attempts

1. **Direct mention:** "What would Gemini think about this architecture?"
2. **Large codebase:** "Analyze this entire codebase for me"
3. **Second opinion:** "Get Gemini's take on this design"
4. **Holistic:** "Review this whole project structure"

## Test Code Sample

Using mutation strategies code from prompt-evolve:
- File: `/Users/leegonzales/Projects/leegonzales/prompt-evolve/pkg/mutations/strategies.go`
- Focus: Intelligent mutation implementation with LLM provider pattern
- Size: ~200 lines (good for focused review)

## Expected Behaviors

### Success Indicators
- Skill is invoked automatically (no explicit /skill or skill: command needed)
- CLI command is executed in the background
- Synthesis is provided comparing perspectives
- User sees both Claude and Codex/Gemini perspectives

### Failure Indicators
- Skill is not triggered at all
- Only Claude's perspective provided
- User must explicitly invoke skill command
- Error messages about missing configuration

## Test Execution Notes

Testing with realistic scenario to evaluate automatic triggering behavior.
