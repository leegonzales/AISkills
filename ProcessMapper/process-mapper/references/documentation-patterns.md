# Process Documentation Patterns

## The Labeled Black Box Pattern

**Critical technique for tacit knowledge:**

When encountering tacit knowledge that resists documentation:

**❌ Don't:** Try to document HOW (impossible)
**✅ Do:** Document THAT (always possible)

### Example

**Bad SOP:**
> "Use your judgment to determine if customer is high-risk"
> (HOW is tacit—can't capture)

**Good SOP:**
> "**Decision point:** Determine if customer is high-risk
> - If yes → Escalate to senior analyst
> - If no → Proceed with standard path
>
> **Decision maker:** Senior analyst (2+ years experience)
> **Typical criteria:** [List if any are explicit]
> **Note:** This requires expert judgment based on pattern recognition"

### What This Enables

- **Process visibility:** Decision point exists and is named
- **Appropriate handoffs:** Who should decide is clear
- **Training focus:** New hires know judgment is required here
- **Future automation planning:** This is identified as the hard part
- **Metrics:** Can track how often this decision point is reached

### When to Use

Use labeled black box pattern when:
- Expert says "I just know" or "It's experience"
- Decision requires pattern recognition over years
- Multiple factors weigh differently based on context
- Explicit rules would have too many exceptions
- Judgment call is fundamental to the role

### Common Tacit Knowledge Areas

**Customer interactions:**
- Risk assessment
- Escalation decisions
- Tone/communication style

**Technical work:**
- Debugging approach
- Architecture decisions
- Code review judgment

**Operations:**
- Priority decisions
- Resource allocation
- Exception handling

### Anti-Pattern

**Don't create false precision:**

❌ Bad:
> "Assess customer risk using the following 47-point checklist..."
> (When in reality expert uses intuition)

This creates:
- Brittle process that breaks on edge cases
- False confidence in automation readiness
- Junior staff following checklist instead of developing judgment

### Template

```markdown
**Decision Point:** [Name the decision]

**Inputs:**
- [What information is available]
- [What context matters]

**Outcomes:**
- Option A → [Next step]
- Option B → [Next step]
- Option C → [Next step]

**Decision Maker:** [Role/seniority level]

**Typical Criteria:** [Any explicit factors, if known]

**Notes:**
- This requires [type of expertise]
- Typical decision time: [estimate]
- Frequency: [how often this decision point is reached]
- Reversibility: [Can this be undone? Cost?]
```

## Movement Strategy for High-Context Processes

**Success in high-context zones often requires building infrastructure that moves the problem to lower zones.**

### Case Study: Air India Customer Support

**Original problem:** Customer support (Zone 8 - Complex/High Context)
- 30,000 daily queries
- High context (policies, exceptions)
- Complex (booking, refunds, special requests)

**Movement strategy:**
1. **Explicit structure:** Document policies, decision trees
2. **Semantic architecture:** Build knowledge base
3. **Scope constraint:** 85% standard, 15% escalate
4. **Result:** Moved to Zone 2 for standard cases

**Success:** 97% accuracy for standard queries (now Zone 2)

### Infrastructure Requirements by Zone

**Zone 8 → Zone 5: Create Frameworks**
- Document policies comprehensively
- Create decision frameworks
- Build knowledge repositories
- Map exception patterns

**Zone 5 → Zone 2: Add Explicit Logic**
- Codify decision rules
- Build system integrations
- Standardize data formats
- Create workflow automation

**Zone 2 → Zone 1: Eliminate Manual Steps**
- Single system interface
- Remove human handoffs
- Automate standard paths
- Exception monitoring only

### Key Insight

You can't automate Zone 8 directly. You must:
1. Document the structure (labeled black boxes)
2. Build supporting infrastructure
3. Narrow scope to automatable subset
4. Move that subset to lower zone
5. Let experts focus on true high-context work

## Common Documentation Mistakes

### Mistake 1: Aspirational Process
**Problem:** Documenting how it "should" work
**Result:** Nobody follows the SOP
**Fix:** Shadow the actual practitioner

### Mistake 2: Over-Documentation
**Problem:** Capturing every tiny detail
**Result:** Unmaintainable, never updated
**Fix:** Focus on decision points and transitions

### Mistake 3: Under-Documentation
**Problem:** "Just ask Bob"
**Result:** Bob becomes bottleneck, tribal knowledge lost when Bob leaves
**Fix:** Labeled black box - name the decision even if logic is tacit

### Mistake 4: Ignoring Exceptions
**Problem:** Only documenting happy path
**Result:** Process breaks constantly in reality
**Fix:** Capture failure modes and workarounds

### Mistake 5: Static Documentation
**Problem:** Created once, never updated
**Result:** Drifts from reality, becomes fiction
**Fix:** Version control, regular validation, update triggers

## SOP Quality Checklist

**Structure:**
- [ ] Clear start and end conditions
- [ ] All decision points identified
- [ ] Exception paths documented
- [ ] Handoff points explicit
- [ ] Tools/systems listed

**Reality:**
- [ ] Validated by actual practitioner
- [ ] Reflects current state, not aspirational
- [ ] Includes common exceptions
- [ ] Captures workarounds as signals

**Usability:**
- [ ] New person could follow (for explicit parts)
- [ ] Decision makers identified
- [ ] Success criteria clear
- [ ] Time estimates realistic

**Maintainability:**
- [ ] Owned by specific person/team
- [ ] Update triggers defined
- [ ] Version controlled
- [ ] Review frequency set
