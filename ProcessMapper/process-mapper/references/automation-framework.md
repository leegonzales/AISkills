# Automation Opportunity Framework

Systematic analysis for determining where and how to apply AI/automation to mapped processes.

## The Tractability Grid (Applied to Process Steps)

**Two dimensions determine automation potential:**

### Dimension 1: Context Dependence (Low ↔ High)

**Low Context:**
- Explicit rules
- Minimal domain knowledge
- Algorithmic logic
- Can be done by following instructions
- Success = following procedure correctly

**High Context:**
- Deep domain expertise required
- Relationship/cultural knowledge
- Tacit judgment
- Novel situations
- Success = appropriate judgment given circumstances

**Assessment questions:**
- Could a smart intern do this with written instructions?
- Is decision logic explicit or tacit?
- Does this require knowing "how things work here"?
- Would two experts do this differently?

---

### Dimension 2: Task Complexity (Simple ↔ Complex)

**Simple:**
- Few steps (≤5)
- Single system
- No or minimal branching
- Linear flow
- Predictable duration

**Complex:**
- Many steps (15+)
- Multiple systems
- Extensive branching
- Parallel activities
- Variable duration

**Assessment questions:**
- How many steps end-to-end?
- How many systems touched?
- How many decision points?
- How predictable is the path?

---

## The Nine Zones

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

---

### Zone 1: Simple/Low Context (Green - 85% Success)

**Characteristics:**
- Repetitive data entry
- Simple calculations
- Single-system operations
- Algorithmic decisions

**Examples:**
- Copying data between fields
- Sending standard emails
- Updating spreadsheets
- Filing documents

**Automation approach:**
- RPA (robotic process automation)
- Simple workflow automation
- Basic AI (OCR, extraction)

**Effort:** Low  
**ROI:** Very High  
**Priority:** Quick win - Do first

---

### Zone 2: Moderate/Low Context (Green - 75% Success)

**Characteristics:**
- Multi-step but rule-based
- Some decision points with clear logic
- May span 2-3 systems
- Predictable patterns

**Examples:**
- Invoice processing
- Order fulfillment
- Scheduled reporting
- Standard approvals

**Automation approach:**
- Workflow automation with rules
- API integrations
- Decision trees (if-then)

**Effort:** Medium  
**ROI:** High  
**Priority:** Strategic investment - Do second

---

### Zone 3: Complex/Low Context (Yellow - 60% Success)

**Characteristics:**
- Many steps but algorithmic
- Cross-system but deterministic
- Complex but not requiring judgment
- Tedious manual orchestration

**Examples:**
- Month-end close procedures
- Compliance reporting
- System migrations
- Data reconciliation

**Automation approach:**
- Process orchestration
- Multi-step workflows
- API-heavy integrations

**Effort:** High  
**ROI:** Medium-High  
**Priority:** Strategic project - Requires investment

---

### Zone 4: Simple/Medium Context (Yellow - 50% Success)

**Characteristics:**
- Simple actions but needs interpretation
- Pattern recognition with guidelines
- Some judgment within bounds
- Domain knowledge helpful

**Examples:**
- Categorizing customer requests
- Triaging support tickets
- Basic quality checks
- Routing decisions

**Automation approach:**
- AI-assisted classification
- Suggestion systems
- Copilot with human approval

**Effort:** Medium  
**ROI:** Medium  
**Priority:** Augmentation - Human in loop

---

### Zone 5: Moderate/Moderate Context (Yellow - 40% Success)

**Characteristics:**
- Multiple steps requiring some judgment
- Mixed explicit and tacit knowledge
- Contextual variations
- Experience improves performance

**Examples:**
- Customer service workflows
- Project planning
- Content moderation
- Risk assessment

**Automation approach:**
- AI copilot for steps
- Partial automation of sub-tasks
- Decision support tools
- Knowledge base enhancement

**Effort:** High  
**ROI:** Medium  
**Priority:** Selective automation - Focus on sub-tasks

---

### Zone 6: Complex/Moderate Context (Red - 25% Success)

**Characteristics:**
- Many steps with judgment throughout
- Requires coordination across teams
- Situational adaptation
- Learning from feedback

**Examples:**
- Program management
- Incident response
- Strategic planning
- Complex negotiations

**Automation approach:**
- Automate information gathering
- Provide better tools/dashboards
- Support tasks only, not core process

**Effort:** Very High  
**ROI:** Low  
**Priority:** Avoid automation - Enable instead

---

### Zone 7: Simple/High Context (Yellow - 35% Success)

**Characteristics:**
- Looks simple but requires deep expertise
- Relationship-dependent
- Cultural knowledge essential
- "Just know" decisions

**Examples:**
- Executive communication
- Stakeholder management
- Sensitive HR decisions
- Trust-based interactions

**Automation approach:**
- Draft generation (human edits)
- Template suggestions
- Research/prep automation

**Effort:** Medium  
**ROI:** Low-Medium  
**Priority:** Light augmentation only

---

### Zone 8: Moderate/High Context (Red - 20% Success)

**Characteristics:**
- Strategic decisions
- Novel situations
- Multiple stakeholder perspectives
- High-stakes judgment

**Examples:**
- Hiring decisions
- Product strategy
- Change management
- Crisis response

**Automation approach:**
- Information aggregation
- Analysis prep
- Documentation assistance
- Do not automate core

**Effort:** High  
**ROI:** Very Low  
**Priority:** Avoid - Focus on enablement

---

### Zone 9: Complex/High Context (Red - <10% Success)

**Characteristics:**
- Highly creative
- Unprecedented situations
- Ethical dimensions
- Long-term implications

**Examples:**
- Organizational transformation
- Innovation strategy
- Major pivots
- Culture design

**Automation approach:**
- Don't automate
- Provide world-class tools
- Remove friction elsewhere

**Effort:** N/A  
**ROI:** N/A  
**Priority:** Never automate

---

## Movement Strategy

**The infrastructure question:**

Success in Zone 5-9 often requires building infrastructure that moves the problem to Zones 1-4.

### Pattern: Context Reduction Through Structure

**Example from user's work: Air India**

**Original problem:** Customer support (Zone 8 - Complex/High Context)
- 30,000 daily queries
- High context (airline operations, policies, exceptions)
- Complex (booking, refunds, special requests)

**Movement strategy:**
1. **Explicit structure:** Document policies, create decision trees
2. **Semantic architecture:** Build knowledge base with relationships
3. **Scope constraint:** Handle 85% of standard queries, escalate 15%
4. **Result:** Moved to Zone 2 (Moderate/Low Context) for standard cases

**Success rate:** 97% for standard queries (now in Zone 2)

---

### Infrastructure Requirements by Zone

**To move Zone 8 → Zone 5:**
- Document policies and precedents
- Create decision frameworks
- Build knowledge bases

**To move Zone 5 → Zone 2:**
- Explicit decision logic
- System integrations
- Standardized inputs/outputs

**To move Zone 2 → Zone 1:**
- Single system consolidation
- Eliminate manual steps
- Pure automation

---

## Prioritization Matrix

**Assess each process step on two axes:**

### Axis 1: Current Pain (Low/Medium/High)
- **High:** Daily complaint, significant time waste, error-prone
- **Medium:** Occasional frustration, some time cost
- **Low:** Annoying but manageable

### Axis 2: Automation Feasibility (Easy/Medium/Hard)
- **Easy:** Zone 1-2, existing tools available
- **Medium:** Zone 3-5, requires custom solution
- **Hard:** Zone 6-9, infrastructure needed

### Priority Quadrants

```
Pain
 ↑
 │  [P2]           [P1]
 │  Build          Quick Win
 │  When Ready     DO NOW
 ├────────────┼────────────→ Feasibility
 │  [P4]           [P3]
 │  Avoid          Efficiency
 │  Not Worth It   Nice to Have
 ↓
```

**P1 - Quick Wins (High Pain/Easy):**
- Do immediately
- High ROI
- Usually Zone 1-2
- Examples: Repetitive data entry, manual copy-paste

**P2 - Strategic Builds (High Pain/Hard):**
- Worth the investment
- Requires planning
- Usually Zone 3-5
- Examples: Cross-system workflows, complex processes

**P3 - Efficiency Gains (Low Pain/Easy):**
- Do when capacity available
- Marginal improvement
- Usually Zone 1-2
- Examples: Nice-to-have automations

**P4 - Avoid (Low Pain/Hard):**
- Not worth effort
- Usually Zone 6-9
- Examples: Complex/rare tasks

---

## ROI Estimation Framework

**For each automation opportunity:**

### Effort Estimation

**Hours to implement:**
- Zone 1: 5-20 hours (RPA setup)
- Zone 2: 20-80 hours (Workflow + integrations)
- Zone 3: 80-200 hours (Complex orchestration)
- Zone 4-5: 40-120 hours (AI development + training)
- Zone 6-9: Often not feasible

**Ongoing maintenance:**
- Simple automation: 1-2 hours/month
- Complex automation: 5-10 hours/month
- AI systems: 10-20 hours/month (retraining, monitoring)

---

### Impact Estimation

**Time saved per execution:**
- Measure current manual time
- Multiply by frequency (daily/weekly/monthly)
- Calculate annual hours saved

**Example:**
- Manual process: 15 minutes
- Frequency: 20 times/day
- Annual time: 15 min × 20 × 250 days = 1,250 hours/year
- At $50/hour fully loaded = $62,500/year saved

**Error reduction value:**
- Estimate error rate before/after
- Cost per error (rework, customer impact)
- Annual error cost reduction

---

### Payback Calculation

**Simple formula:**
```
Payback Period = Implementation Cost / Annual Benefit

Implementation Cost = Hours × Hourly Rate
Annual Benefit = (Time Saved × Hourly Rate) + Error Reduction Value
```

**Rule of thumb:**
- Payback <3 months: Definitely do
- Payback 3-12 months: Probably do
- Payback >12 months: Requires business case

---

## Phased Implementation Roadmap

### Phase 1: Quick Wins (Months 1-2)
**Focus:** Zone 1-2, P1 quadrant
**Approach:**
- Map 3-5 highest-pain simple processes
- Implement with existing tools (Zapier, RPA)
- Demonstrate value quickly
- Build organizational confidence

**Success criteria:** 3+ processes automated, visible time savings

---

### Phase 2: Strategic Builds (Months 3-6)
**Focus:** Zone 2-3, P2 quadrant
**Approach:**
- Tackle complex but high-ROI processes
- Custom integrations if needed
- May require vendor support
- Measure impact rigorously

**Success criteria:** 2+ major processes automated, documented ROI

---

### Phase 3: Augmentation (Months 6-12)
**Focus:** Zone 4-5, AI copilots
**Approach:**
- Build AI-assisted tools
- Human-in-the-loop systems
- Knowledge base development
- Training and adoption

**Success criteria:** 5+ augmented workflows, user adoption >70%

---

### Phase 4: Infrastructure (Ongoing)
**Focus:** Moving processes between zones
**Approach:**
- Document policies → reduce context
- Build integrations → reduce complexity
- Create frameworks → enable automation

**Success criteria:** Zone movement (8→5, 5→2, 2→1)

---

## Documentation Standards

### Automation Opportunity Record

**For each identified opportunity:**

```markdown
# [Process Name] Automation Analysis

**Current State:**
- Zone: [1-9]
- Pain Level: [Low/Medium/High]
- Frequency: [X times per day/week/month]
- Manual Time: [Y minutes per execution]
- Error Rate: [Z%]

**Proposed Automation:**
- Approach: [RPA/Workflow/AI/Copilot]
- Zone Target: [After automation]
- Effort Estimate: [Hours]
- Tools Needed: [List]

**Business Case:**
- Annual Time Saved: [Hours]
- Annual Cost Savings: [$]
- Error Reduction: [%]
- Payback Period: [Months]
- Priority: [P1/P2/P3/P4]

**Implementation Notes:**
- Prerequisites: [What needs to happen first]
- Risks: [What could go wrong]
- Alternatives: [Other approaches considered]

**Status:** [Not Started / In Progress / Complete]
```

---

## Integration Points

**With process mapping:**
- Map process first
- Classify each step by zone
- Identify opportunities
- Prioritize and plan

**With `concept-forge`:**
- Test automation hypotheses
- Challenge assumptions about feasibility
- Refine zone classifications

**With `strategy-to-artifact`:**
- Create automation roadmap deck
- Build business case one-pagers
- Present to stakeholders

---

## Anti-Patterns

**Don't:**
- Automate before mapping (can't automate what you can't see)
- Force Zone 8-9 into automation (will fail)
- Ignore context dependencies (leads to brittle systems)
- Skip validation with process owners (will automate wrong thing)
- Automate fictional processes (garbage in, garbage out)
- Measure only time saved (ignore error reduction, morale)

**Do:**
- Start with current state (not aspirational)
- Acknowledge tacit knowledge (label the black boxes)
- Build infrastructure (create movement paths)
- Validate continuously (with actual users)
- Measure comprehensively (time, errors, satisfaction)
- Iterate and improve (automation isn't one-and-done)
