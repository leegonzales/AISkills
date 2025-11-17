# Writing Skills - Meta-Skill for TDD Documentation

**Version:** 1.0.0
**Type:** META-SKILL (improves skill development process)
**Attribution:** Originally developed by obra (Jesse Vincent)
**Source:** https://github.com/obra/superpowers/tree/main/skills/writing-skills

## Overview

**Writing Skills is Test-Driven Development applied to process documentation.**

This meta-skill transforms how you create skills by applying the same rigor to documentation that TDD applies to code. Instead of writing skills based on intuition and hoping they work, you test with subagents first, watch them fail, then write documentation that addresses those specific failures.

**The Iron Law:**
```
NO SKILL WITHOUT A FAILING TEST FIRST
```

This applies to NEW skills AND EDITS to existing skills. No exceptions.

## What is the "Iron Law" Methodology?

The Iron Law is a discipline borrowed directly from Test-Driven Development:

**TDD for Code:**
1. Write test first (it fails - RED)
2. Write minimal code to pass (GREEN)
3. Refactor while keeping tests passing
4. Never write code without a failing test first

**Iron Law for Skills:**
1. Create pressure scenario with subagent (baseline behavior - RED)
2. Write minimal skill that addresses failures (GREEN)
3. Close loopholes by finding new rationalizations (REFACTOR)
4. Never write skills without watching agents fail first

### Why This Matters

**Without the Iron Law:**
- Skills based on assumptions about what agents need
- Unclear if skills actually improve behavior
- Rationalizations and loopholes discovered in production
- Wasted effort on unnecessary documentation

**With the Iron Law:**
- Skills address proven failure modes
- Evidence-based documentation
- Loopholes closed before deployment
- Higher quality, bulletproof skills

## TDD Mapping for Skills

| TDD Concept | Skill Creation |
|-------------|----------------|
| **Test case** | Pressure scenario with subagent |
| **Production code** | Skill document (SKILL.md) |
| **Test fails (RED)** | Agent violates rule without skill (baseline) |
| **Test passes (GREEN)** | Agent complies with skill present |
| **Refactor** | Close loopholes while maintaining compliance |
| **Write test first** | Run baseline scenario BEFORE writing skill |
| **Watch it fail** | Document exact rationalizations agent uses |
| **Minimal code** | Write skill addressing those specific violations |
| **Watch it pass** | Verify agent now complies |
| **Refactor cycle** | Find new rationalizations → plug → re-verify |

## Integration into AISkills Development Workflow

This meta-skill improves how we develop ALL skills in the AISkills collection:

### 1. Before Creating Any New Skill

**Traditional approach (AVOID):**
1. Think "I should create a skill for X"
2. Write SKILL.md based on intuition
3. Hope it works
4. Discover issues later

**Iron Law approach (USE):**
1. Identify technique worth documenting
2. Create pressure scenario (without skill)
3. Watch agent fail - document exact behavior
4. Write skill addressing those failures
5. Verify agent now succeeds
6. Close loopholes systematically

### 2. Quality Gates

Every skill in AISkills should follow the Iron Law methodology:

**For NEW skills (created from scratch):**
- MUST run baseline testing (RED phase)
- MUST document agent failures
- MUST write minimal skill addressing failures (GREEN)
- MUST close loopholes (REFACTOR)
- Peer review with Gemini + Codex (as usual)

**For FORKS (like this one):**
- Original testing already done (trusted source)
- Adaptation testing recommended but not required
- Focus on integration with AISkills structure

### 3. Documentation Standards

All skills should include:
- **Concise SKILL.md** (<500 words, focuses on core pattern)
- **Rich description field** (starts with "Use when...", includes triggers/symptoms)
- **Claude Search Optimization** (keywords, symptoms, error messages)
- **Progressive disclosure** (details in separate reference files)

### 4. Skill Development Checklist

The writing-skills SKILL.md provides a complete TDD-adapted checklist:

**RED Phase:**
- [ ] Create pressure scenarios (3+ combined pressures)
- [ ] Run WITHOUT skill - document baseline
- [ ] Identify rationalization patterns

**GREEN Phase:**
- [ ] Write minimal skill addressing failures
- [ ] Run WITH skill - verify compliance
- [ ] Check YAML frontmatter (name, description only)

**REFACTOR Phase:**
- [ ] Find new rationalizations
- [ ] Add explicit counters
- [ ] Build rationalization table
- [ ] Re-test until bulletproof

## What's Included

### Core Files

1. **SKILL.md** (20,819 bytes)
   - Complete TDD methodology for documentation
   - Skill types and structure
   - Claude Search Optimization (CSO)
   - Iron Law enforcement
   - RED-GREEN-REFACTOR workflow
   - Skill creation checklist

2. **anthropic-best-practices.md** (45,798 bytes)
   - Official Anthropic skill authoring guidelines
   - Conciseness principles
   - Token efficiency
   - Degrees of freedom
   - Discovery optimization

3. **persuasion-principles.md** (5,908 bytes)
   - Research-backed persuasion psychology for LLMs
   - 7 principles (Authority, Commitment, Scarcity, Social Proof, Unity, Reciprocity, Liking)
   - When to use each principle
   - Ethical guidelines
   - Citations (Cialdini 2021, Meincke et al. 2025)

4. **graphviz-conventions.dot** (5,970 bytes)
   - Visual documentation standards
   - Node shapes for different elements
   - Edge labeling conventions
   - When to use flowcharts (only for non-obvious decisions)
   - Good vs bad examples

### Total Size

~78KB of high-value reference material that improves all future skill development.

## Three Before/After Examples

### Example 1: Discipline-Enforcing Skill (TDD)

**BEFORE Iron Law (assumption-based):**
```markdown
# Test-Driven Development

Write tests before code. This helps ensure quality.

## How to Use
1. Think about what you want to build
2. Write a test for it
3. Implement the code
4. Run the test
```

**AFTER Iron Law (evidence-based):**
```markdown
# Test-Driven Development

Write code before test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "It's about spirit not ritual" | Violating letter = violating spirit. |
```

**What improved:**
- Explicit counters to agent rationalizations (discovered via testing)
- No exceptions clause (closes "this is different" loophole)
- Rationalization table (built from baseline failures)
- Imperative language (authority principle from persuasion research)

### Example 2: Technique Skill (Async Testing)

**BEFORE Iron Law:**
```markdown
# Async Testing

Use condition-based waiting for async operations.

```javascript
await waitFor(() => element.isVisible())
```

This is better than timeouts.
```

**AFTER Iron Law:**
```markdown
# Condition-Based Waiting

**Symptoms:** Tests with setTimeout/sleep are flaky, pass/fail inconsistently, hang randomly

**Pattern:**
```javascript
// ❌ BAD: Arbitrary timeout
await sleep(1000)  // Race condition - might fail

// ✅ GOOD: Wait for condition
await waitFor(() => element.isVisible(), { timeout: 5000 })
```

## When NOT to Use
- Fixed delays required by API (explicitly documented)
- Animation timing (use requestAnimationFrame)
```

**What improved:**
- Symptoms section (CSO - helps Claude discover skill)
- Before/after comparison (shows exact problem + solution)
- When NOT to use (prevents misapplication, discovered via testing)
- Specific timeout value with rationale

### Example 3: Reference Skill (API Documentation)

**BEFORE Iron Law:**
```markdown
# PDF Processing

pdfplumber is a library for PDF processing.

## Features
- Extract text
- Extract tables
- Get page info
- Many more features!
```

**AFTER Iron Law:**
```markdown
# PDF Processing

## Extract Text
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Extract Tables
```python
tables = pdf.pages[0].extract_tables()
```

## Common Issues
- **Empty text**: PDF may be scanned image. Use OCR: `pdf.pages[0].to_image().ocr()`
- **Table structure wrong**: Adjust table settings: `extract_tables(table_settings={"vertical_strategy": "lines"})`
```

**What improved:**
- Runnable code (complete imports, not snippets)
- Common issues section (discovered via testing what agents actually need)
- Solution patterns (not just "many features!")
- Token efficiency (removed fluffy intro)

## Installation

### For Claude Code

```bash
# Navigate to AISkills repository
cd /path/to/AISkills

# Copy to Claude skills directory
cp -r WritingSkills/writing-skills ~/.claude/skills/
```

### For Claude Web Chat

1. Download the packaged skill: `writing-skills-v1.0.0.skill`
2. Go to claude.ai
3. Upload the skill file in a new conversation
4. The skill will be available for that conversation

### For AISkills Developers

This meta-skill should be understood by all AISkills contributors:

```bash
# Already integrated in this repository
cd /path/to/AISkills/WritingSkills/writing-skills

# Read the core methodology
cat SKILL.md

# Review persuasion principles
cat persuasion-principles.md

# Check Anthropic best practices
cat anthropic-best-practices.md
```

## Usage

### When Creating a New Skill

1. **Don't write SKILL.md first** - this violates the Iron Law
2. **Create pressure scenario** (task where agent would need this skill)
3. **Run baseline** (test without skill, document failures)
4. **Write minimal skill** addressing those failures
5. **Verify compliance** (test with skill present)
6. **Close loopholes** (find new rationalizations, add counters)

### When Editing an Existing Skill

Same process! Editing without testing = same violation.

1. **Create test scenario** for the addition/change
2. **Run with current skill** (should show gap you want to fill)
3. **Make minimal edit** addressing that gap
4. **Verify improvement** (test shows agents now handle case)
5. **Check for new loopholes**

### Quick Checks

**Am I following the Iron Law?**
- [ ] Did I test without the skill first? (RED)
- [ ] Did I document exact agent failures?
- [ ] Did I write minimal skill for those failures? (GREEN)
- [ ] Did I verify agents now comply?
- [ ] Did I find and close loopholes? (REFACTOR)

**Red flags - STOP:**
- Writing skill before testing
- "I already manually tested it"
- "It's obviously clear"
- "Testing is overkill"
- "This is different because..."

All of these mean: Delete what you wrote. Start with testing.

## Key Principles

### 1. Conciseness is Critical

**Context window is a shared resource:**
- SKILL.md loads into every conversation where skill is used
- Every token competes with conversation history
- Target <500 words for SKILL.md
- Move details to separate reference files

### 2. Claude Search Optimization (CSO)

**Future Claude needs to FIND your skill:**

**Rich description field:**
```yaml
# ❌ BAD: Too abstract
description: For async testing

# ✅ GOOD: Specific triggers + what it does
description: Use when tests have race conditions, timing dependencies, or pass/fail inconsistently - replaces arbitrary timeouts with condition polling for reliable async tests
```

**Keyword coverage:**
- Error messages: "Hook timed out", "ENOTEMPTY", "race condition"
- Symptoms: "flaky", "hanging", "zombie", "pollution"
- Tools: Actual commands, library names
- Synonyms: "timeout/hang/freeze"

### 3. Persuasion Principles

**LLMs respond to same principles as humans:**

**Authority** (for discipline skills):
- "YOU MUST", "Never", "Always"
- "No exceptions"
- Eliminates rationalization

**Commitment** (for process compliance):
- "Announce skill usage"
- "Choose A, B, or C"
- Use TodoWrite for tracking

**Social Proof** (for standards):
- "Every time", "Always"
- "X without Y = failure"

Research: Meincke et al. (2025) showed persuasion techniques increased LLM compliance from 33% → 72%.

### 4. Progressive Disclosure

**Don't front-load everything:**

**SKILL.md**: Core pattern only (<500 words)
**Separate files**:
- Heavy reference (API docs, comprehensive syntax)
- Reusable tools (scripts, utilities, templates)
- Examples and troubleshooting

### 5. Testing with Subagents

**Different skill types need different tests:**

**Discipline-enforcing:** Pressure scenarios (time + sunk cost + exhaustion)
**Technique:** Application scenarios (can they apply correctly?)
**Pattern:** Recognition scenarios (do they know when to use?)
**Reference:** Retrieval scenarios (can they find the info?)

See SKILL.md for complete testing methodology.

## How This Improves AISkills Development

### Before Writing-Skills Integration

1. Create skills based on intuition
2. Hope they work
3. Discover issues in production
4. Patch reactively
5. Unclear if skills help

### After Writing-Skills Integration

1. Test baseline behavior (RED)
2. Document proven failures
3. Write evidence-based skills (GREEN)
4. Close loopholes systematically (REFACTOR)
5. Deploy bulletproof skills

### Metrics of Success

**Quality improvements:**
- Skills address real failure modes (not hypothetical)
- Loopholes identified and closed before deployment
- Higher compliance rates under pressure
- Fewer "skill didn't work" issues

**Efficiency improvements:**
- Less rework (get it right first time)
- Faster debugging (know what skills should do)
- Better reuse (skills proven to work)
- Systematic methodology (not ad-hoc)

## Development

This is a fork/integration skill, not built from scratch. The original obra/superpowers skill has already undergone extensive testing and refinement.

### Directory Structure

```
writing-skills/
├── SKILL.md                      # Core TDD methodology (20KB)
├── README.md                     # This file
├── CHANGELOG.md                  # Version history
├── anthropic-best-practices.md  # Official Anthropic guidelines (46KB)
├── persuasion-principles.md     # Psychology research (6KB)
└── graphviz-conventions.dot     # Visual documentation standards (6KB)
```

### Customization

This skill is used as-is from obra/superpowers with:
- Added README.md for AISkills integration context
- Added CHANGELOG.md for version tracking
- No modifications to core SKILL.md (trusted source)

### Contributing

Improvements to this meta-skill should be contributed back to obra/superpowers:
https://github.com/obra/superpowers

For AISkills-specific integration issues, open an issue in the AISkills repository.

## References

### Research Citations

**Cialdini, R. B. (2021).** *Influence: The Psychology of Persuasion (New and Expanded).* Harper Business.
- Seven principles of persuasion
- Foundation for skill design principles

**Meincke, L., Shapiro, D., Duckworth, A. L., Mollick, E., Mollick, L., & Cialdini, R. (2025).** Call Me A Jerk: Persuading AI to Comply with Objectionable Requests. University of Pennsylvania.
- N=28,000 LLM conversations testing persuasion
- Compliance increased from 33% → 72%
- Authority, commitment, scarcity most effective

### Related Skills

**Required background:**
- **test-driven-development** (from superpowers) - Fundamental TDD concepts
- **testing-skills-with-subagents** (from superpowers) - Complete testing methodology

**Complementary skills:**
- **systematic-debugging** (from superpowers) - Debugging methodology
- **verification-before-completion** (from superpowers) - Quality gates

### External Resources

- **Original source:** https://github.com/obra/superpowers/tree/main/skills/writing-skills
- **Anthropic Skills documentation:** https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills
- **Superpowers collection:** https://github.com/obra/superpowers

## License

MIT License (same as obra/superpowers)

Copyright (c) 2024 Jesse Vincent (obra)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## Support

For questions about using this meta-skill with AISkills:
- Open an issue in the AISkills repository
- Include "writing-skills" in the issue title

For questions about the core methodology:
- Refer to obra/superpowers repository
- The original author has extensive documentation

---

**Remember the Iron Law:** No skill without a failing test first. No exceptions.

This meta-skill ensures every skill in AISkills is evidence-based, bulletproof, and actually works.
