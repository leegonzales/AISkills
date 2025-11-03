# Process Discovery Methodology

Systematic approach to mapping workflows, extracting SOPs, and identifying automation opportunities.

## Core Philosophy

**From user's SOP doctrine:**
> "You can't automate what you can't see. You can't document what you haven't mapped. Start with the terrain before choosing tools."

**Three fundamental truths:**
1. **Shadow processes are real processes** - What people actually do ≠ what the org chart says
2. **Tacit knowledge is documentable** - You can capture decision *points* even when decision *logic* is tacit
3. **Structure enables automation** - Making work visible is prerequisite to applying AI

---

## The Three SOP States

**Diagnostic framework for existing documentation:**

### State 1: Fiction
**Characteristics:**
- SOPs exist but nobody follows them
- Documentation is aspirational not actual
- Beautiful Confluence pages gathering dust
- Process described ≠ process executed

**Indicators:**
- "We have documentation but..."
- When asked "show me," people say "it's somewhere"
- Documentation hasn't been updated in 18+ months
- New hires don't reference it

**What to do:**
- Throw away or archive old docs
- Start fresh with current-state mapping
- Don't try to "fix" fiction—replace it

---

### State 2: Nonexistent
**Characteristics:**
- No documentation at all
- Process lives in people's heads
- "Just ask Sarah"
- Tribal knowledge

**Indicators:**
- "We don't really have a process for that"
- Different people do it differently
- No onboarding materials
- Reliant on specific individuals

**What to do:**
- This is your starting point
- Begin with process discovery
- Map what actually happens

---

### State 3: Accurate
**Characteristics:**
- Documentation matches reality
- People reference it regularly
- Updated when process changes
- New hires can follow it

**Indicators:**
- "Let me show you the doc"
- Documentation opened during work
- Recent modification dates
- Successful onboarding with docs

**What to do:**
- Maintain and improve
- Use as basis for automation analysis
- Extract for AI opportunity mapping

---

## Process Discovery Interview Framework

### Setup Phase

**Preparation:**
1. **Identify target process:** Specific value stream or task
2. **Find process owner:** Person who does this regularly
3. **Secure time:** 45-90 minutes uninterrupted
4. **Set context:** "Walk me through how you actually do this"
5. **Get artifacts:** Access to tools, screens, documents they use

**Critical framing:**
> "I'm not auditing. I'm trying to understand what actually happens so we can make your work easier. Show me the shadow process, not the org chart version."

---

### Discovery Questions (Sequential)

#### Round 1: High-Level Flow

**Objective:** Get end-to-end sequence

**Questions:**
- "Walk me through this from start to finish"
- "What triggers this process?"
- "What's the endpoint—when are you done?"
- "What are the major steps?"
- "How long does this typically take?"

**Capture:**
- 5-10 major steps
- Trigger event
- End state
- Typical duration

**Don't yet:** Dive into details, ask about decisions, discuss tools

---

#### Round 2: Step Decomposition

**Objective:** Break each major step into substeps

**For each major step, ask:**
- "What specifically happens here?"
- "Show me on your screen"
- "What information do you need at this point?"
- "Where does that information come from?"
- "What tools do you use?"

**Capture:**
- Substeps (actions)
- Information inputs
- Tools/systems
- Data transformations

**Look for:** Copy-paste, manual data entry, switching between systems

---

#### Round 3: Decision Points

**Objective:** Identify where judgment is required

**Questions:**
- "How do you decide X?"
- "What are you looking for when you evaluate Y?"
- "What makes you go down Path A vs Path B?"
- "Who do you ask when Z?"
- "What criteria determine success here?"

**Capture:**
- Decision points (explicit)
- Criteria (if articulatable)
- If-then logic
- Escalation paths

**Critical distinction:**
- **Explicit logic:** "If amount > $5000, escalate" → Documentable as rule
- **Tacit judgment:** "I just know when it looks wrong" → Documentable as **decision point** (labeled black box)

---

#### Round 4: Edge Cases & Exceptions

**Objective:** Understand where process breaks down

**Questions:**
- "What goes wrong most often?"
- "When does this process not work?"
- "Tell me about a time this failed"
- "What are the special cases?"
- "What percentage of cases are 'normal' vs 'exception'?"

**Capture:**
- Common failure modes
- Exception paths
- Workarounds
- Frequency estimates (e.g., 80% standard, 20% exception)

**Look for:** High exception rates (process might be wrong), consistent workarounds (shadow process)

---

#### Round 5: Context Dependencies

**Objective:** Identify what tacit knowledge enables this

**Questions:**
- "What do you need to know to do this well?"
- "What would trip up someone new?"
- "What context am I missing as an outsider?"
- "How did you learn this?"
- "What's not written down anywhere?"

**Capture:**
- Domain knowledge required
- Institutional knowledge
- Relationship dependencies
- Cultural context

**This reveals:** What can't easily be automated (high context) vs. what can (low context)

---

### Validation Phase

**Walk-through validation:**
1. Show them your mapped process
2. Ask: "Did I get this right?"
3. Let them correct/refine
4. Watch for: "Well, actually..." → reveals shadow process

**Parallel validation (if possible):**
1. Interview second person who does same process
2. Compare maps
3. Identify variations
4. Determine if variation is:
   - Personal style (acceptable)
   - Process drift (problematic)
   - Role-based (expected)

---

## Mapping Notation Standards

### Basic Flow Elements

**Sequential steps:**
```
[Step 1] → [Step 2] → [Step 3]
```

**Decision points:**
```
        ┌─→ [Path A]
[Check] ┤
        └─→ [Path B]
```

**Parallel activities:**
```
[Start] ──┬─→ [Activity A] ──┐
          └─→ [Activity B] ──┴─→ [Continue]
```

**Iteration/loops:**
```
[Start] → [Do Thing] → [Check] ──→ [End]
              ↑            |
              └────NO──────┘
```

---

### Information Flow Elements

**Data inputs:**
```
[System A]
    ↓ (data)
[Process Step]
```

**Transformations:**
```
[Raw Data] → [Process: Clean/Transform] → [Structured Data]
```

**Human judgment:**
```
[Data] → [👤 Review] → [Decision]
         (tacit)
```

**System handoffs:**
```
[System A] → [Manual Export] → [System B]
              (copy-paste)
```

---

### Complexity Indicators

**Tacit knowledge point:**
```
[Step] → [⚡ Expert Judgment] → [Continue]
          (undocumentable)
```

**High-frequency pain point:**
```
[Step] → [⚠️ Often Fails] → [Workaround]
```

**Dependency blocker:**
```
[Wait for Sarah] → [Can Continue]
   (bottleneck)
```

**Context requirement:**
```
[Step requiring domain knowledge]
🧠 Must know: X, Y, Z
```

---

## The Labeled Black Box Pattern

**From user's SOP doctrine:**

When you encounter tacit knowledge that resists capture:

**Don't try to document the HOW (impossible)**
**Document the THAT (always possible)**

**Example:**
```
❌ Bad SOP: "Use your judgment to determine if customer is high-risk"
              (HOW is tacit)

✅ Good SOP: "Decision point: Determine if customer is high-risk
              → If yes: [Escalation path]
              → If no: [Standard path]
              Decision maker: Senior analyst with 2+ years experience"
              (THAT there's a decision is captured)
```

**This enables:**
- Clear process visibility
- Appropriate handoffs
- Training focus (new hires know there's judgment here)
- Future automation planning (this is the hard part)

---

## Complexity Classification

**Map each step to Tractability Grid dimensions:**

### Context Dependence (Low → High)

**Low context:**
- Algorithmic (if-then rules)
- No domain knowledge required
- Can be done by following instructions
- Examples: Data entry, standard calculations

**Medium context:**
- Some domain knowledge helpful
- Pattern recognition
- Contextual judgment within bounds
- Examples: Categorization with guidelines

**High context:**
- Deep domain expertise required
- Relationship knowledge essential
- Cultural/institutional awareness needed
- Examples: Strategic decisions, relationship management

---

### Task Complexity (Simple → Complex)

**Simple:**
- Single system
- Few steps (≤5)
- No branching
- Examples: Send email, update field

**Moderate:**
- Multiple systems
- 5-15 steps
- Some decision points
- Examples: Process invoice, schedule meeting

**Complex:**
- Many systems
- 15+ steps
- Multiple decision trees
- Parallel activities
- Examples: Close quarterly books, manage escalation

---

## Automation Opportunity Analysis

**For each process step, assess:**

### Zone 1: Simple/Low Context (Green - High Automation Potential)
**Characteristics:**
- Algorithmic logic
- Single system or API-connected systems
- No judgment required
- High volume/frequency

**Automation approach:**
- RPA (robotic process automation)
- Workflow automation
- Simple AI (classification, extraction)

**ROI:** High - Easy to automate, high impact

---

### Zone 2: Simple/High Context (Yellow - Augmentation Potential)
**Characteristics:**
- Simple steps but needs domain knowledge
- Human judgment on inputs
- AI can't decide but can assist

**Automation approach:**
- AI copilot for suggestions
- Decision support tools
- Knowledge base enhancement

**ROI:** Medium - Can reduce time, but not eliminate human

---

### Zone 3: Complex/Low Context (Yellow - Partial Automation)
**Characteristics:**
- Many steps but algorithmic
- Cross-system but rule-based
- Tedious but deterministic

**Automation approach:**
- Multi-step workflow automation
- API integrations
- Process orchestration

**ROI:** Medium - High setup cost, high ongoing value

---

### Zone 4: Complex/High Context (Red - Human Required)
**Characteristics:**
- Strategic decisions
- Relationship management
- Novel situations
- Creative problem-solving

**Automation approach:**
- Don't try to automate the core
- Automate supporting tasks (information gathering, documentation)
- Provide better tools/interfaces

**ROI:** Low for automation, focus on enablement

---

## Output Formats

### Format 1: Linear SOP Document

**Use for:** Simple sequential processes (≤10 steps, minimal branching)

```markdown
# Process Name

**Trigger:** [What starts this]
**Owner:** [Role]
**Duration:** [Typical time]
**Frequency:** [How often]

## Steps

1. **[Step Name]**
   - Action: [What to do]
   - Tool: [System/tool used]
   - Input: [What you need]
   - Output: [What you produce]
   
2. **[Step Name]**
   [Same structure]

## Quality Checks
- [Validation point 1]
- [Validation point 2]

## Common Issues
- **Issue:** [Problem]
  **Solution:** [Fix]
```

---

### Format 2: Decision Tree SOP

**Use for:** Processes with multiple paths (branching logic)

```markdown
# Process Name

## Entry Point

**Situation:** [Context]
**First Decision:** [Question]

### Path A: [Condition]
→ Steps: [1, 2, 3]
→ Outcome: [End state]

### Path B: [Condition]
→ Steps: [4, 5, 6]
→ Outcome: [End state]

## Decision Matrix

| Criteria | Path A | Path B | Path C |
|----------|--------|--------|--------|
| [Factor] | Yes    | No     | N/A    |
| [Factor] | >$5K   | <$5K   | Custom |
```

---

### Format 3: Swimlane Process Map

**Use for:** Multi-role processes (who does what when)

```markdown
# Process Name

## Roles
- **Requestor:** [Person who initiates]
- **Approver:** [Person who decides]
- **Processor:** [Person who executes]

## Flow

| Step | Requestor | Approver | Processor |
|------|-----------|----------|-----------|
| 1    | Submit request | | |
| 2    | | Review & decide | |
| 3a (if approved) | | | Execute |
| 3b (if denied) | Notified | | |
| 4    | | | Close & document |
```

---

### Format 4: Visual Process Diagram

**Use for:** Complex flows needing visualization

**Export as:**
- Mermaid diagram (embeddable in docs)
- Flowchart image
- Interactive diagram

**Elements to include:**
- Start/end nodes
- Process boxes
- Decision diamonds
- Data flows
- System boundaries
- Swim lanes for roles

---

## Integration with AI Opportunity Mapping

**Once process is mapped:**

1. **Classify each step** (Tractability Grid)
2. **Identify automation zones**
3. **Estimate effort/impact**
4. **Create prioritization matrix**
5. **Design phased implementation**

**Output:** Automation roadmap with:
- Quick wins (high impact, low effort)
- Strategic bets (high impact, high effort)
- Efficiency gains (low impact, low effort)
- Avoid (low impact, high effort)

---

## Quality Signals

**Good process map has:**
- [ ] Actual current state (not aspirational)
- [ ] All decision points identified
- [ ] Tacit knowledge points marked
- [ ] Context dependencies noted
- [ ] Exception paths included
- [ ] Validated by process owner
- [ ] Frequency/volume data
- [ ] Pain points documented
- [ ] Clear start and end
- [ ] Realistic time estimates

**Red flags:**
- Too neat (probably fictional)
- No exceptions (not real)
- No pain points (incomplete discovery)
- No tacit knowledge points (missed shadow process)
- Can't estimate frequency (no real data)
- Process owner says "that's not quite right"
