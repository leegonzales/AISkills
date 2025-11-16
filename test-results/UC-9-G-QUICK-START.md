# UC-9-G Quick Start Guide
## Gemini Multimodal Technical Review - 5 Minute Setup

**Status:** READY TO EXECUTE

---

## What is UC-9-G?

This test validates **Gemini's unique multimodal capability** to analyze:
- Architecture diagrams
- Design specifications
- Actual code implementation

...and identify gaps/deviations by reasoning across all three modalities.

**This is Gemini-exclusive:** Codex cannot do this level of cross-modal analysis.

---

## Quick Execute (Copy-Paste Ready)

### Prerequisites Check
```bash
# 1. Verify Gemini CLI works
gemini --version

# 2. Verify test materials exist
ls -lh /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/prompt-evolve-design-spec.md
ls -lh /Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/*.mmd
ls -lh /Users/leegonzales/Projects/leegonzales/prompt-evolve/pkg/

# 3. Create results directory if needed
mkdir -p /Users/leegonzales/Projects/leegonzales/AISkills/test-results
```

### Execute Test (Option A: Recommended)

**Trigger through Claude Code with this prompt:**

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

**Watch for:**
- Does Claude invoke GeminiPeerReview skill?
- Is context prepared with all three modalities?
- Does Gemini cross-reference spec ↔ diagram ↔ code?
- Are gaps specific with exact package/file references?

### Save Results
```bash
# Save Gemini's raw output to:
/Users/leegonzales/Projects/leegonzales/AISkills/test-results/UC-9-G-gemini-raw-output.txt

# Complete test report template at:
/Users/leegonzales/Projects/leegonzales/AISkills/test-results/UC-9-G-report.md
```

---

## Success Criteria (Quick Check)

**Test PASSES if ALL 5 are met:**

✓ **Diagram Analyzed**
- [ ] Gemini references architecture diagram
- [ ] Maps diagram components to code

✓ **Code Analyzed**
- [ ] Reviews actual package structure
- [ ] References specific files/locations

✓ **Cross-Modal Consistency Checked**
- [ ] Compares spec ↔ diagram ↔ code
- [ ] Identifies mismatches across modalities

✓ **Gaps Identified with Specifics**
- [ ] Names specific missing components
- [ ] References exact spec sections + diagram nodes + code packages
- [ ] At least 3 specific, verifiable gaps

✓ **Recommendations Actionable**
- [ ] Clear implementation tasks
- [ ] Specific files/packages to modify
- [ ] Concrete next steps

**Quality Minimum:** Average score ≥3.5/5 across 5 metrics

---

## Quality Metrics (Rate 1-5)

1. **Multimodal Integration:** ___/5 - Did it integrate all three modalities?
2. **Gap Analysis Quality:** ___/5 - Were gaps thorough and specific?
3. **Deviation Detection:** ___/5 - Caught real deviations vs. false positives?
4. **Cross-Modal Reasoning:** ___/5 - Synthesized across spec/diagram/code?
5. **Actionability:** ___/5 - Can developer act on recommendations?

**Total:** ___/25 (Need ≥17.5 to pass)

---

## What Good Looks Like

**Strong multimodal analysis includes:**

```
Gap: pkg/core/Mutator interface deviation
- Design spec (Section 2.2): Apply(prompt) → (mutated, error)
- Architecture diagram: Shows Mutator in "Unix interfaces" box
- Implementation (pkg/core/interfaces.go:42): Apply(ctx, prompt, strategy)
- Status: DEVIATION - Added context parameter not in spec
- Recommendation: Update design spec Section 2.2 or remove ctx param
```

**Why this is excellent:**
- Names exact component (pkg/core/Mutator)
- References exact spec section (2.2)
- References diagram component ("Unix interfaces")
- References exact file and line (interfaces.go:42)
- Cross-references all three modalities
- Actionable recommendation with specifics

---

## What Poor Looks Like

**Weak analysis:**

```
The code looks mostly correct. Some differences from the spec but
overall it matches the architecture. A few things could be improved.
```

**Why this fails:**
- No specific gaps identified
- No cross-modal references
- Generic, non-actionable feedback
- Could apply to any codebase

---

## Files You Need

**Read First:**
- `/Users/leegonzales/Projects/leegonzales/AISkills/test-data/UC-9-G-TEST-EXECUTION.md` (Detailed instructions)

**Test Materials (automatically used):**
- `/Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/prompt-evolve-design-spec.md`
- `/Users/leegonzales/Projects/leegonzales/AISkills/test-data/diagrams/architecture-diagram.mmd`
- `/Users/leegonzales/Projects/leegonzales/prompt-evolve/` (code)

**Complete After Test:**
- `/Users/leegonzales/Projects/leegonzales/AISkills/test-results/UC-9-G-report.md` (Template)

**Summary:**
- `/Users/leegonzales/Projects/leegonzales/AISkills/test-results/UC-9-G-SETUP-SUMMARY.md` (Overview)

---

## Troubleshooting

**"Gemini CLI not found"**
```bash
which gemini  # Check if installed
# If not, install Gemini CLI per GeminiPeerReview documentation
```

**"Cannot process diagram as image"**
- Provide Mermaid diagram as text (Gemini can parse Mermaid syntax)
- Include diagram content in context instead of as separate image

**"Context too large"**
- Provide strategic code samples instead of full codebase
- Focus on key packages: evolution, mutations, fitness, core

**"Vague gap analysis"**
- Follow up: "Please provide specific details for each gap with exact file references"

---

## Time Estimate

- **Setup verification:** 2 minutes
- **Test execution:** 10 minutes
- **Evaluation:** 5 minutes
- **Report completion:** 8 minutes
- **Total:** ~25 minutes

---

## Expected Outcome

**If Gemini's multimodal capability works well, you'll see:**
- Gap analysis that connects spec → diagram → code
- Identification of architectural deviations
- Insights that pure code analysis wouldn't provide
- Recommendations that help maintain design-code alignment

**This validates Gemini's unique value for:**
- Technical architecture reviews
- Design-implementation consistency checks
- Onboarding (understanding system from multiple perspectives)
- Documentation accuracy validation

---

## Next Steps After Test

1. **Save all outputs** (raw + completed report)
2. **Calculate metrics** (5 dimensions × 5 points = 25 total)
3. **Determine verdict** (PASS if ≥4/5 criteria met + avg ≥3.5/5)
4. **Document findings** in final report
5. **Compare with Codex** (hypothetically - could Codex do this?)

---

**Ready? Let's test Gemini's multimodal capability!**

Start here: Copy the trigger prompt above and paste into Claude Code.
