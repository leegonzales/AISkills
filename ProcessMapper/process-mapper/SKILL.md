---
name: process-mapper
description: Map workflows, extract SOPs, and identify automation opportunities. Use when user requests (1) "map this process", (2) "document our workflow for X", (3) "where can we apply AI to this", (4) "create SOP for Y", (5) process discovery interviews, (6) automation opportunity analysis. Grounds user's SOP-first doctrine in systematic process capture, tacit knowledge documentation, and AI tractability assessment.
license: Complete terms in LICENSE.txt
---

# Process Mapper Skill

Systematic workflow for discovering, documenting, and analyzing processes. Implements user's SOP-first doctrine: **"You can't automate what you can't see."**

## Core Philosophy

**From user's work:**
> "When I sit with a person or team to start working through how they can work out where and how to apply AI into their job, I often like to start with a common task or value stream, and talk through—or more often than not, document—the SOP for that value stream."

**Three truths:**
1. **Shadow processes are real processes** (what actually happens ≠ org chart)
2. **Tacit knowledge is documentable** (capture decision *points*, not decision *logic*)
3. **Structure enables automation** (visibility → AI opportunities)

---

## Core Workflow

### 1. Diagnostic: Assess Current State

**Determine SOP state:**

Load `references/discovery-methodology.md` for framework

**State 1: Fiction**
- SOPs exist but nobody follows them
- Beautiful docs, zero usage
- Aspirational not actual

**State 2: Nonexistent**
- No documentation
- Tribal knowledge
- "Just ask Sarah"

**State 3: Accurate**
- Docs match reality
- Referenced regularly
- Updated when process changes

**Action by state:**
- Fiction → Archive and start fresh
- Nonexistent → Begin discovery (most common)
- Accurate → Use for automation analysis

---

### 2. Process Discovery Interview

**If starting from State 2 (Nonexistent), conduct discovery:**

**Setup:**
- Identify process owner (person who actually does this)
- Secure 45-90 minutes uninterrupted
- Frame: "Show me what actually happens, not what should happen"
- Get screen access to tools they use

**Five-round interview sequence:**

#### Round 1: High-Level Flow
**Objective:** Get end-to-end sequence

**Questions:**
- "Walk me through this from start to finish"
- "What triggers this?"
- "When are you done?"
- "What are the major steps?"

**Capture:** 5-10 major steps, trigger, endpoint, duration

---

#### Round 2: Step Decomposition
**Objective:** Break each step into substeps

**For each major step:**
- "What specifically happens here?"
- "Show me on your screen"
- "What information do you need?"
- "Where does that come from?"
- "What tools do you use?"

**Capture:** Substeps, inputs, tools, transformations

**Look for:** Copy-paste, manual entry, system switching

---

#### Round 3: Decision Points
**Objective:** Identify where judgment is required

**Questions:**
- "How do you decide X?"
- "What are you looking for?"
- "What makes you go Path A vs Path B?"
- "Who do you ask when...?"

**Capture:**
- Decision points (explicit)
- Criteria (if articulatable)
- If-then logic
- Escalation paths

**Critical distinction:**
- **Explicit:** "If >$5K, escalate" → Documentable as rule
- **Tacit:** "I just know" → Document as **labeled black box** (decision point exists, logic is tacit)

---

#### Round 4: Edge Cases & Exceptions
**Objective:** Understand failure modes

**Questions:**
- "What goes wrong most often?"
- "When doesn't this work?"
- "Tell me about a time this failed"
- "What % is normal vs exception?"

**Capture:** Failure modes, workarounds, frequency estimates

**Look for:** High exception rates (process might be wrong), consistent workarounds (shadow process)

---

#### Round 5: Context Dependencies
**Objective:** Identify tacit knowledge

**Questions:**
- "What do you need to know to do this well?"
- "What would trip up someone new?"
- "What context am I missing?"
- "How did you learn this?"

**Capture:** Domain knowledge, institutional knowledge, relationships, culture

**Reveals:** What can't easily be automated (high context) vs. what can (low context)

---

### 3. Process Documentation

**Choose format based on process characteristics:**

**Format 1: Linear SOP** (≤10 steps, minimal branching)
- Sequential steps with actions/tools/inputs
- Quality checks
- Common issues

**Format 2: Decision Tree** (multiple paths, branching logic)
- Entry conditions
- Path A/B/C with criteria
- Decision matrix

**Format 3: Swimlane** (multi-role, handoffs important)
- Who does what when
- Handoff points
- Role responsibilities

**Format 4: Visual Diagram** (complex flows)
- Mermaid flowchart
- System integrations
- Exception paths

Load `assets/visual-templates.md` for specific templates

**Documentation principles:**
- Capture **actual** current state (not aspirational)
- Mark tacit knowledge points with ⚡
- Note context dependencies with 🧠
- Flag frequent failures with ⚠️
- Include frequency/volume data
- Validate with process owner

---

### 4. Complexity Classification

**Map each process step to Tractability Grid:**

Load `references/automation-framework.md` for full framework

**Two dimensions:**

#### Dimension 1: Context Dependence (Low → High)

**Low context:**
- Algorithmic (if-then rules)
- No domain knowledge required
- Follow instructions

**High context:**
- Deep expertise required
- Relationship knowledge
- Tacit judgment

**Assessment:** Could a smart intern do this with written instructions?

---

#### Dimension 2: Task Complexity (Simple → Complex)

**Simple:**
- Few steps (≤5)
- Single system
- No branching

**Complex:**
- Many steps (15+)
- Multiple systems
- Extensive branching

**Assessment:** How many steps? How many systems? How many decision points?

---

### 5. Automation Opportunity Analysis

**Plot each step on grid (9 zones):**

```
        High Context
             ↑
    [🟥 Red]  │ [🟨 Yellow] │ [🟨 Yellow]
    Zone 7    │  Zone 8     │  Zone 9
    ──────────┼─────────────┼──────────→ High Complexity
    [🟨 Yellow]│ [🟨 Yellow] │ [🟥 Red]
    Zone 4    │  Zone 5     │  Zone 6
    ──────────┼─────────────┼──────────
    [🟩 Green]│ [🟩 Green]  │ [🟨 Yellow]
    Zone 1    │  Zone 2     │  Zone 3
             ↓
        Low Context
```

**Zone characteristics:**

**Zones 1-2 (Green):** High automation potential (85-75% success)
- RPA, workflow automation
- Quick wins, high ROI

**Zones 3-5 (Yellow):** Medium potential (60-40% success)
- Partial automation, AI copilots
- Strategic investment, human-in-loop

**Zones 6-9 (Red):** Low potential (<25% success)
- Avoid automation of core
- Automate supporting tasks only
- Focus on enablement

---

### 6. Prioritization & ROI

**Assess each opportunity on two axes:**

**Pain Level:**
- High: Daily complaint, error-prone, time waste
- Medium: Occasional frustration
- Low: Annoying but manageable

**Feasibility:**
- Easy: Zone 1-2, existing tools
- Medium: Zone 3-5, custom solution
- Hard: Zone 6-9, infrastructure needed

**Priority quadrants:**

**P1 - Quick Wins (High Pain/Easy):**
- Do immediately
- Usually Zone 1-2
- Example: Repetitive data entry

**P2 - Strategic Builds (High Pain/Hard):**
- Worth investment
- Usually Zone 3-5
- Example: Complex workflows

**P3 - Efficiency Gains (Low Pain/Easy):**
- Do when capacity available
- Nice-to-have improvements

**P4 - Avoid (Low Pain/Hard):**
- Not worth effort
- Usually Zone 6-9

**ROI calculation:**
```
Payback Period = Implementation Cost / Annual Benefit

Annual Benefit = (Hours Saved × Hourly Rate) + Error Reduction Value
```

---

### 7. Output Delivery

**Standard deliverables:**

1. **Process Map** (visual diagram with annotations)
   - Current state flow
   - Context/complexity markers
   - Decision points highlighted
   - Exception paths shown

2. **SOP Document** (written procedure)
   - Step-by-step instructions
   - Tools/systems referenced
   - Decision criteria
   - Quality checks

3. **Automation Opportunity Analysis** (structured assessment)
   - Each step classified by zone
   - Priority quadrant placement
   - ROI estimates
   - Recommended approach

4. **Implementation Roadmap** (phased plan)
   - Phase 1: Quick wins (Months 1-2)
   - Phase 2: Strategic builds (Months 3-6)
   - Phase 3: Augmentation (Months 6-12)
   - Phase 4: Infrastructure (Ongoing)

**Optional deliverables:**
- Interview transcript
- Validation session notes
- Comparative analysis (if multiple people interviewed)
- Metrics dashboard design

---

## The Labeled Black Box Pattern

**Critical technique from user's doctrine:**

When encountering tacit knowledge that resists documentation:

**❌ Don't:** Try to document HOW (impossible)
**✅ Do:** Document THAT (always possible)

**Example:**

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

**This enables:**
- Process visibility (decision point exists)
- Appropriate handoffs (who should decide)
- Training focus (new hires know judgment required here)
- Future automation planning (this is the hard part)

---

## Movement Strategy

**Success in high-context zones often requires building infrastructure that moves the problem to lower zones.**

**Example from user's work: Air India**

**Original problem:** Customer support (Zone 8 - Complex/High Context)
- 30,000 daily queries
- High context (policies, exceptions)
- Complex (booking, refunds, special requests)

**Movement strategy:**
1. **Explicit structure:** Document policies, decision trees
2. **Semantic architecture:** Build knowledge base
3. **Scope constraint:** 85% standard, 15% escalate
4. **Result:** Moved to Zone 2 for standard cases

**Success:** 97% for standard queries (now Zone 2)

**Infrastructure requirements by zone:**
- Zone 8 → Zone 5: Document policies, create frameworks
- Zone 5 → Zone 2: Explicit logic, integrations, standards
- Zone 2 → Zone 1: Single system, eliminate manual steps

---

## Quality Signals

**Good process map has:**
- [ ] Actual current state (not aspirational)
- [ ] All decision points identified
- [ ] Tacit knowledge points marked (⚡)
- [ ] Context dependencies noted (🧠)
- [ ] Exception paths included
- [ ] Validated by process owner
- [ ] Frequency/volume data
- [ ] Pain points documented
- [ ] Clear start and end
- [ ] Realistic time estimates

**Red flags:**
- Too neat (probably fictional)
- No exceptions (incomplete)
- No pain points (not real discovery)
- No tacit knowledge points (missed shadow process)
- Can't estimate frequency (no data)
- Process owner says "that's not quite right"

---

## Integration Points

**With `concept-forge`:**
- Test automation hypotheses dialectically
- Challenge zone classifications
- Refine through multiple perspectives

**With `strategy-to-artifact`:**
- Process map → Presentation deck
- Automation roadmap → Executive one-pager
- Business case → Slide deck

**With `research-to-essay`:**
- Process patterns → Substack post on SOP doctrine
- Case studies → Long-form analysis

**With user's voice (from `research-to-essay`):**
- Use dialogue structure in documentation
- Employ concrete examples (Air India vs Air Canada)
- Include practitioner stance ("In my experience...")
- Show recursive refinement ("Let me be more precise...")

---

## Common Process Types & Patterns

### Type 1: Approval Workflows
**Characteristics:** Request → Review → Decision → Action
**Common zones:** 1-2 (if rule-based), 4-5 (if judgment-heavy)
**Automation potential:** High for rule-based criteria

### Type 2: Data Processing
**Characteristics:** Input → Transform → Output
**Common zones:** 1-3 (depends on transformation complexity)
**Automation potential:** Very high if algorithmic

### Type 3: Customer Service
**Characteristics:** Inquiry → Triage → Resolution
**Common zones:** 4-8 (depends on query complexity and context)
**Automation potential:** Medium (copilot model works well)

### Type 4: Reporting
**Characteristics:** Gather → Analyze → Present
**Common zones:** 1-3 (if structured), 5-7 (if insights required)
**Automation potential:** High for data gathering, medium for analysis

### Type 5: Coordination
**Characteristics:** Schedule → Communicate → Align
**Common zones:** 4-9 (highly relationship-dependent)
**Automation potential:** Low for core, high for supporting tasks

---

## Anti-Patterns

**Don't:**
- Map aspirational process (document what actually happens)
- Skip validation with process owner (will be wrong)
- Try to capture tacit HOW (use labeled black box)
- Force Zone 8-9 into automation (will fail)
- Ignore shadow processes (they're the real process)
- Over-document (keep it actionable)
- Create one-time map (processes evolve, keep updated)

**Do:**
- Start with actual current state
- Validate iteratively
- Document decision points even when logic is tacit
- Acknowledge complexity honestly
- Focus on high-ROI opportunities
- Build movement infrastructure
- Update as process changes

---

## Success Metrics

**Process mapping succeeds when:**
- Process owner says "Yes, that's exactly what we do"
- New team members can follow documented process
- Automation opportunities clearly identified
- ROI estimates are validated
- Quick wins deliver promised value
- Documentation is referenced regularly (not ignored)

**Automation analysis succeeds when:**
- Zone classifications match reality
- Prioritization aligns with business value
- Implementation follows plan
- Expected savings materialize
- User adoption high (not forced)

---

## Example Triggers

- "Map our customer onboarding process"
- "Document how we handle support tickets"
- "Where can we apply AI to our workflow?"
- "Create SOP for expense approval"
- "Show me where automation makes sense"
- "Why does this process keep breaking?"
- "Help me understand what my team actually does"
- "Walk me through your typical day"
