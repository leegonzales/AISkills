# UC-9-G Test Execution Instructions
## Gemini Multimodal Technical Review (Gemini-Only Feature)

**Test Case ID:** UC-9-G
**Test Type:** Gemini Exclusive Feature Test
**Focus Area:** Multimodal Analysis (Code + Diagrams + Specifications)
**Estimated Time:** 20-25 minutes

---

## Test Objective

Validate Gemini's unique multimodal capability to analyze technical implementations by cross-referencing:
1. Architecture diagrams (visual/text representation)
2. Design specifications (written documentation)
3. Actual code implementation
4. Identify gaps, deviations, and inconsistencies across modalities

This tests Gemini's ability to perform **cross-modal consistency checking** - a capability unique to Gemini that Codex does not possess.

---

## Test Materials

### 1. Design Specification
**Location:** `/Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/prompt-evolve-design-spec.md`

**Contents:**
- Intended architecture and design principles
- Component responsibilities and interfaces
- Expected data flows
- Package structure and dependencies
- Non-functional requirements

### 2. Architecture Diagrams
**Location:** `/Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/`

**Files:**
- `architecture-diagram.mmd` - High-level component relationships (Mermaid)
- `component-diagram.mmd` - Detailed package breakdown
- `data-flow-diagram.mmd` - Evolution process sequence
- `architecture-overview.md` - Narrative description

**Note:** Mermaid diagrams can be rendered visually or analyzed as text-based diagrams.

### 3. Implementation Code
**Location:** `/Users/leegonzales/Projects/leegonzales/prompt-evolve/`

**Key Areas to Analyze:**
- `pkg/evolution/` - Evolution engine implementation
- `pkg/mutations/` - Mutation strategies
- `pkg/fitness/` - Fitness evaluation
- `pkg/population/` - Population management
- `pkg/providers/` - Provider abstraction
- `pkg/cost/` - Cost tracking
- `cmd/` - CLI tools
- `test/` - Testing infrastructure

**Total Size:** ~9,033 LOC (Go code)

---

## Test Setup

### Prerequisites

1. **Gemini CLI Installed and Authenticated**
   ```bash
   gemini --version
   # Should return version info
   ```

2. **Test Materials Available**
   ```bash
   # Verify design spec exists
   ls -lh /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/prompt-evolve-design-spec.md

   # Verify diagrams exist
   ls -lh /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/*.mmd

   # Verify code repository accessible
   ls -lh /Users/leegonzales/Projects/leegonzales/prompt-evolve/pkg/
   ```

3. **Test Results Directory**
   ```bash
   mkdir -p /Users/leegonzales/Projects/leegonzales/AISkills/test-results
   ```

---

## Test Execution Steps

### Step 1: Prepare Context (5 minutes)

Gather all materials that will be provided to Gemini:

```bash
# Read design spec
cat /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/prompt-evolve-design-spec.md

# Read architecture diagrams
cat /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/architecture-diagram.mmd
cat /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/architecture-overview.md

# Scan implementation structure
tree /Users/leegonzales/Projects/leegonzales/prompt-evolve/pkg/ -L 2
tree /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/ -L 1
```

**Context to Include:**
1. Full design specification (text)
2. Architecture diagram (Mermaid as text or rendered image)
3. Relevant code samples from key packages
4. Package structure overview

### Step 2: Trigger Multimodal Analysis (10 minutes)

#### Option A: Using GeminiPeerReview Skill (Preferred)

Trigger through Claude Code with natural language:

```
Gemini, check if our prompt-evolve implementation matches the architecture
diagram and design spec. Use multimodal analysis to identify gaps or deviations.

Materials to analyze:
1. Design spec: /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/prompt-evolve-design-spec.md
2. Architecture diagram: /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/architecture-diagram.mmd
3. Implementation: /Users/leegonzales/Projects/leegonzales/prompt-evolve/

Focus on:
- Does the package structure match the design?
- Are the component responsibilities implemented as specified?
- Do the data flows match the sequence diagrams?
- Are there missing or extra components?
- Are interfaces implemented as designed?
```

**Expected Behavior:**
- Claude Code recognizes this as a Gemini-specific request
- Invokes GeminiPeerReview skill
- Prepares comprehensive context including:
  - Design spec content
  - Diagram content (or reference to diagram file)
  - Code structure and key implementations
- Calls Gemini CLI with appropriate flags
- Synthesizes Gemini's multimodal analysis

#### Option B: Direct Gemini CLI Invocation (Alternative)

If testing CLI directly:

```bash
# Create a combined context file
cat > /tmp/uc9g-context.md <<EOF
# Multimodal Technical Review Request

## Design Specification
$(cat /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/prompt-evolve-design-spec.md)

## Architecture Diagram
$(cat /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/architecture-diagram.mmd)

## Implementation Structure
$(tree /Users/leegonzales/Projects/leegonzales/prompt-evolve/pkg/ -L 2)

## Request
Analyze this prompt-evolve implementation and compare it against:
1. The design specification above
2. The architecture diagram (Mermaid)
3. The actual code implementation

Identify:
- Gaps between design and implementation
- Deviations from architectural intent
- Missing components
- Extra/unexpected components
- Interface mismatches
- Data flow inconsistencies

Provide actionable recommendations.
EOF

# Invoke Gemini with multimodal context
gemini --file /tmp/uc9g-context.md \
       --image /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/architecture-diagram.mmd \
       "Perform a cross-modal consistency check and identify gaps"
```

**Note:** The `--image` flag may require rendering the Mermaid diagram to PNG first. If unavailable, Gemini can analyze the Mermaid text representation.

### Step 3: Observe and Document (5 minutes)

**Watch for These Behaviors:**

1. **Context Preparation Quality**
   - Does Claude Code include all three modalities (spec, diagram, code)?
   - Is the context well-structured for cross-modal analysis?
   - Are code samples representative of key components?

2. **Gemini CLI Invocation**
   - Does it use appropriate flags for multimodal input?
   - Is the diagram included properly?
   - Is the prompt clear about cross-modal analysis?

3. **Multimodal Integration**
   - Does Gemini reference the diagram visually (if rendered)?
   - Does Gemini cross-reference between spec, diagram, and code?
   - Does it identify inconsistencies across modalities?

4. **Analysis Quality**
   - Are gaps specific and accurate?
   - Are deviations from design intent identified?
   - Are recommendations actionable?
   - Does it show understanding of architectural intent?

### Step 4: Evaluate Results (5 minutes)

**Success Criteria Checklist:**

- [ ] **Diagram Analyzed**
  - Gemini references the architecture diagram
  - Understands component relationships from diagram
  - Can map diagram elements to code

- [ ] **Code Analyzed**
  - Reviews actual implementation structure
  - Examines key package implementations
  - Identifies code patterns and abstractions

- [ ] **Cross-Modal Consistency Checked**
  - Compares design spec ↔ diagram
  - Compares design spec ↔ code
  - Compares diagram ↔ code
  - Identifies mismatches across modalities

- [ ] **Gaps Identified with Specifics**
  - Names specific missing components
  - Points to specific package/interface deviations
  - Quantifies differences (e.g., "Spec calls for 5 strategies, found 4")
  - References specific sections of spec, diagram, and code

- [ ] **Recommendations Actionable**
  - Clear implementation tasks
  - Priority levels indicated
  - Specific files/packages to modify
  - Concrete next steps

**Quality Metrics (Rate 1-5):**

1. **Multimodal Integration:** ___/5
   - How well did Gemini integrate diagram, spec, and code?
   - Did it leverage visual/structural information from diagram?

2. **Gap Analysis Quality:** ___/5
   - How thorough was the gap identification?
   - Were gaps specific and verifiable?

3. **Deviation Detection:** ___/5
   - Did it catch real deviations from design intent?
   - Were false positives minimal?

4. **Cross-Modal Reasoning:** ___/5
   - Did it reason across all three modalities?
   - Did it synthesize insights from multiple sources?

5. **Actionability:** ___/5
   - How actionable are the recommendations?
   - Can a developer immediately act on them?

---

## Expected Outcomes

### What Good Looks Like

**Example of Strong Multimodal Analysis:**

```
Gap Analysis Report:

1. Missing Component: pkg/history/
   - Design spec (Section: Core Components) specifies evolution history tracking
   - Architecture diagram shows "HIST" component in Infrastructure group
   - Implementation: ✓ FOUND at pkg/history/
   - Status: ✓ IMPLEMENTED

2. Interface Deviation: pkg/core/Mutator
   - Design spec defines Mutator interface with Apply(prompt) → (mutated, error)
   - Component diagram shows Mutator in Unix interfaces
   - Implementation: Mutator interface has Apply(ctx, prompt, strategy) signature
   - Status: ⚠ PARTIAL MATCH (added context parameter, not in spec)
   - Recommendation: Update spec to document context parameter rationale

3. Missing Strategy: pkg/mutations/
   - Design spec specifies 5 mutation strategies
   - Implementation: Found 5 strategies ✓
   - However, crossover strategies not shown in design spec
   - Status: ⚠ ENHANCEMENT (implementation exceeds spec)
   - Recommendation: Update design spec to document crossover strategies

4. Data Flow Deviation: Evolution Phase
   - Sequence diagram shows "Adapt mutation/crossover rates" step
   - Implementation (pkg/evolution/engine.go): Adaptive logic found ✓
   - However, adaptation uses different criteria than spec
   - Status: ⚠ DEVIATION (implementation uses diversity metric, spec suggests generation number)
   - Recommendation: Align spec with actual adaptive logic or document rationale

5. Package Structure Match: ✓ EXCELLENT
   - All packages in design spec are present in implementation
   - Directory structure matches architectural intent
   - Dependencies align with component diagram
```

### What Poor Looks Like

**Example of Weak Analysis:**

```
The implementation looks mostly correct. I see the packages and they seem
to match the diagram. There might be some small differences but overall
it's good.
```

**Issues with Poor Analysis:**
- No specific gap identification
- No cross-referencing between modalities
- No verification of spec vs. implementation
- Generic, non-actionable feedback

---

## Troubleshooting

### Issue: Gemini CLI Not Found
```bash
# Check if installed
which gemini

# If not found, install (adjust based on actual installation method)
# See GeminiPeerReview skill documentation
```

### Issue: Cannot Process Diagram as Image
**Solution:** Provide Mermaid diagram as text
- Gemini can analyze Mermaid syntax textually
- Include diagram content in context rather than as image
- Note this in test results (limitation of test setup, not Gemini)

### Issue: Code Context Too Large
**Solution:** Provide strategic code samples
- Focus on key packages: evolution, mutations, fitness
- Include interface definitions from pkg/core/
- Include key types from pkg/api/
- Reference full codebase location for Gemini to explore

### Issue: Vague Gap Analysis
**Follow-up Prompt:**
```
Please provide more specific details for each gap:
1. Quote the exact section from the design spec
2. Reference the specific diagram component
3. Point to the actual code location or absence
4. Quantify the deviation if possible
```

---

## Test Deliverables

### 1. Raw Output
**File:** `/Users/leegonzales/Projects/leegonzales/AISkills/test-results/UC-9-G-gemini-raw-output.txt`

Save the complete raw output from Gemini for reference.

### 2. Test Report
**File:** `/Users/leegonzales/Projects/leegonzales/AISkills/test-results/UC-9-G-report.md`

Complete test report using the template structure:
- Test execution summary
- Success criteria evaluation
- Quality metrics scores
- Observations and findings
- Recommendations

### 3. Context Used
**File:** `/Users/leegonzales/Projects/leegonzales/AISkills/test-results/UC-9-G-context.md`

Document what context was provided to Gemini:
- Design spec sections included
- Diagram content/reference
- Code samples provided
- Total token count estimate

---

## Post-Test Analysis

After completing the test, reflect on:

1. **Did Gemini demonstrate true multimodal capability?**
   - Could it reference visual diagram elements?
   - Did it connect diagram → spec → code?

2. **Was the gap analysis valuable?**
   - Would a developer find it useful?
   - Did it catch real issues vs. false positives?

3. **How does this compare to Codex?**
   - Could Codex perform this cross-modal analysis?
   - What unique value does Gemini's multimodal capability provide?

4. **Skill Integration Quality**
   - Did Claude Code prepare context appropriately?
   - Was the synthesis of Gemini's output helpful?
   - Any improvements needed to skill implementation?

---

## Success Definition

**This test PASSES if:**
- ✓ Gemini processes all three modalities (spec, diagram, code)
- ✓ Cross-modal consistency checking is performed
- ✓ At least 3 specific gaps/deviations identified
- ✓ Recommendations are actionable with specific file/package references
- ✓ Analysis quality scores average ≥3.5/5

**This test demonstrates unique value if:**
- Gemini identifies issues that pure code analysis wouldn't catch
- Cross-modal reasoning provides architectural insights
- Diagram understanding enhances the analysis
- Analysis would help developers maintain design-code alignment

---

**Ready to Execute!**

Follow the steps above and document your findings in the test report.
