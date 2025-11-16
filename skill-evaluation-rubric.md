# Skill Evaluation Rubric

**Version:** 1.0
**Purpose:** Systematic evaluation of Claude skills for integration into AISkills collection
**Last Updated:** 2025-11-16

---

## Evaluation Criteria

### Category 1: Core Value Proposition (25 points)

**Clear Unique Purpose (10 pts)**
- 10: Solves specific problem not addressed by existing skills; clear value proposition
- 7: Useful but overlaps with existing capabilities
- 4: Generic or poorly defined purpose
- 0: Duplicate or unclear value

**Real-World Applicability (10 pts)**
- 10: Multiple clear, practical use cases with broad applicability
- 7: Niche but valuable for specific domain
- 4: Limited practical application
- 0: Theoretical or contrived use case

**Execution Quality (5 pts)**
- 5: Works reliably, produces high-quality outputs
- 3: Functional but inconsistent or needs refinement
- 1: Buggy or produces poor quality outputs
- 0: Non-functional

---

### Category 2: Documentation Quality (20 points)

**README Comprehensiveness (8 pts)**
- 8: Complete README with purpose, features, installation, examples, use cases
- 6: Good README but missing key sections
- 4: Basic README, minimal information
- 0: Missing or inadequate README

**Installation Instructions (4 pts)**
- 4: Clear instructions for both Claude Code and web chat (if applicable)
- 3: Instructions for one platform only
- 2: Incomplete or unclear instructions
- 0: Missing installation guidance

**Usage Examples (8 pts)**
- 8: Multiple detailed examples showing diverse usage patterns
- 6: Some examples but limited breadth
- 4: Minimal examples
- 0: No examples

---

### Category 3: Technical Structure (20 points)

**Repository Organization (8 pts)**
- 8: Professional structure (dist/, skill-name/, references/, proper naming)
- 6: Good structure but missing optional components
- 4: Basic structure, lacks organization
- 0: Disorganized or non-standard structure

**SKILL.md Quality (8 pts)**
- 8: Concise, focused, well-structured skill definition with clear instructions
- 6: Functional but verbose or lacks clarity
- 4: Minimal skill definition
- 0: Missing or inadequate SKILL.md

**Supporting Assets (4 pts)**
- 4: Includes references/, examples/, scripts/ or other value-add assets
- 3: Some supporting materials
- 2: Minimal supporting materials
- 0: No supporting assets

---

### Category 4: Production Readiness (15 points)

**Versioning & Releases (5 pts)**
- 5: Semantic versioning, packaged .skill files, changelog
- 3: Version number but no packaging/changelog
- 1: Unversioned or ad-hoc versioning
- 0: No version management

**Testing/Validation (5 pts)**
- 5: Comprehensive testing with documented results
- 3: Some testing or validation
- 1: Minimal testing
- 0: No evidence of testing

**Error Handling & Edge Cases (5 pts)**
- 5: Robust handling, documented limitations
- 3: Basic error handling
- 1: Minimal error consideration
- 0: No error handling

---

### Category 5: Ecosystem Fit (10 points)

**Complementarity (5 pts)**
- 5: Fills gap in our collection or enhances existing skills
- 3: Useful but overlaps with existing skills
- 1: Redundant with minor differentiation
- 0: Duplicate functionality

**Integration Potential (5 pts)**
- 5: Works well with Claude Code tools, could enhance workflows
- 3: Standalone value but limited integration
- 1: Isolated functionality
- 0: Conflicts with ecosystem

---

### Category 6: Innovation & Design (10 points)

**Novel Approach (5 pts)**
- 5: Innovative methodology, unique framework, or creative solution
- 3: Solid approach with some novel elements
- 1: Standard approach, no innovation
- 0: Derivative or outdated approach

**Design Philosophy (5 pts)**
- 5: Demonstrates best practices (concise core, progressive disclosure, research-backed)
- 3: Good design but inconsistent application
- 1: Minimal design consideration
- 0: Poor design choices

---

## Scoring System

**Total: 100 points**

### Quality Tiers

**Tier 1: Exceptional (85-100)**
- **Action:** Fork immediately and integrate
- **Criteria:** High value, excellent documentation, production-ready
- **Examples from our collection:** Prose Polish, Gemini Peer Review

**Tier 2: Strong (70-84)**
- **Action:** Copy and improve with proper repo structure
- **Criteria:** Good value but needs documentation/structure refinement
- **Effort:** Medium refactoring needed

**Tier 3: Moderate (50-69)**
- **Action:** Consider for inspiration or future enhancement
- **Criteria:** Good idea but significant work needed
- **Effort:** Substantial refactoring required

**Tier 4: Low Priority (< 50)**
- **Action:** Pass or use as learning reference only
- **Criteria:** Limited value or too much work to salvage

---

## Additional Evaluation Factors

### Repository Health Signals
- **Stars:** Indicates community interest (weight: medium)
- **Recent commits:** Shows active maintenance (weight: high)
- **Issues/PRs:** Shows community engagement (weight: low)
- **License:** MIT/Apache preferred (weight: medium)

### Red Flags (Automatic disqualification)
- ❌ No license or restrictive license
- ❌ Malicious code or security concerns
- ❌ Abandoned (no updates in 12+ months for new skills)
- ❌ Requires paid services without free tier
- ❌ Violates Claude usage policies

### Bonus Points (+5 each, max +15)
- ✅ Validated with real-world testing
- ✅ Research-backed methodology
- ✅ Includes utility scripts/validators
- ✅ Multimodal capabilities
- ✅ Unique technical capability (e.g., API integration, specialized analysis)
- ✅ Active community (5+ contributors)

---

## Evaluation Workflow

### Step 1: Quick Assessment (2 min)
1. Read README and skill description
2. Check repository structure
3. Review star count and activity
4. **Decision:** Proceed to full evaluation or pass

### Step 2: Detailed Evaluation (10 min)
1. Score all 6 categories
2. Check for red flags
3. Assess bonus point eligibility
4. Calculate total score
5. Determine tier

### Step 3: Decision
- **Tier 1 (85+):** Fork and integrate
- **Tier 2 (70-84):** Copy, improve structure, document
- **Tier 3 (50-69):** Note for future consideration
- **Tier 4 (< 50):** Pass

### Step 4: Documentation
Record in evaluation log:
- Skill name and repo URL
- Total score and tier
- Key strengths and weaknesses
- Integration action (fork/copy/pass)
- Notes for improvement if copying

---

## Usage Notes

**For Subagent Reviews:**
- Each agent receives rubric and skill assignments
- Agents evaluate assigned skills independently
- Agents return structured scoring and recommendations
- Avoid duplicate assignments (track in master catalog)

**Scoring Calibration:**
- Use our existing skills as reference points (all should score 85+)
- Be generous with innovation but strict on documentation
- Value unique capabilities over incremental improvements
- Prioritize production-ready over experimental

**Decision Bias:**
- When uncertain between tiers, bias toward higher tier
- Quality over quantity - better to have fewer excellent skills
- Complementarity > Redundancy - favor gap-filling over duplication

---

## Example Evaluation

**Skill:** `test-driven-development` (obra/superpowers)

**Category Scores:**
- Core Value: 22/25 (clear purpose, broad applicability, proven execution)
- Documentation: 18/20 (excellent README, good examples, minor gaps)
- Technical: 18/20 (professional structure, solid SKILL.md)
- Production: 12/15 (versioned, proven usage, needs formal testing docs)
- Ecosystem: 9/10 (complements our collection, good integration)
- Innovation: 8/10 (battle-tested framework, solid design)

**Bonus:** +10 (validated with real-world usage, battle-tested, active community)

**Total: 87/100 (Tier 1 - Exceptional)**

**Action:** Fork and integrate with minimal modifications

**Notes:**
- Strengths: Proven methodology, clear value, excellent examples
- Minor gaps: Could add formal testing documentation
- Integration: Fits well with CodexPeerReview and GeminiPeerReview

---

## Reference: Our Skill Benchmarks

Use these as calibration points:

**Prose Polish (100 points est.)**
- Perfect documentation, comprehensive testing, research-backed, unique value

**Gemini Peer Review (97 points est.)**
- Exceptional capability, excellent docs, proven testing, production-ready

**Claimify (92 points est.)**
- Strong unique value, great structure, good examples, solid design

**Codex Peer Review (95 points est.)**
- Unique capability, excellent docs, comprehensive testing

**All our skills should score 85+ on this rubric**

---

Built for AISkills repository quality assurance | v1.0
