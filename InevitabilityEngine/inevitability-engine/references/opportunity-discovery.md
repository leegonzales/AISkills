# Phase 2: Opportunity Discovery (Segment-Problem Analysis)

**Goal**: Build exhaustive segment × problem matrix to identify high-value automation targets.

---

## Target Segments

**Company size segments:**
1. **SMBs** (1-50 employees) - Budget-conscious, need generalists
2. **Mid-market** (51-500 employees) - Growing fast, scaling pains
3. **Enterprise** (500-5000 employees) - Process-heavy, compliance burdens
4. **Megacorps** (5000+ employees) - Coordination overhead, legacy systems

**Knowledge worker segments:**
1. **Writers** - Journalists, authors, content creators, copywriters
2. **Designers** - Product, graphic, UX/UI, brand
3. **Programmers** - Frontend, backend, full-stack, infrastructure
4. **Engineers** - Civil, mechanical, electrical, systems
5. **Managers** - Project, product, engineering, operations
6. **Finance professionals** - Analysts, accountants, controllers, CFOs
7. **Legal professionals** - Attorneys, paralegals, compliance officers
8. **Healthcare providers** - Doctors, nurses, administrators, researchers
9. **Educators** - Teachers, professors, instructional designers
10. **Researchers** - Academic, corporate, market, UX

---

## Step 2.1: Build Segment-Problem Matrix

**For EACH segment, execute this research loop:**

### Research Loop Protocol

**Search pattern 1: Time wasters**
```
"[segment] biggest time wasters 2024"
"[segment] time consuming tasks survey"
"[segment] productivity challenges"
```

**Search pattern 2: Workflow automation**
```
"[segment] workflow automation pain points"
"[segment] manual processes bottlenecks"
"[segment] repetitive tasks"
```

**Search pattern 3: AI adoption barriers**
```
"[segment] AI adoption challenges"
"[segment] AI tools not working"
"why [segment] don't use AI"
```

**Search pattern 4: Community discussions**
```
"site:reddit.com [segment] productivity pain points"
"site:news.ycombinator.com [segment] workflow tools"
"site:twitter.com [segment] wish I could automate"
```

**Search pattern 5: Market research**
```
"[segment] software needs survey 2024"
"[segment] workflow tools market research"
"[segment] biggest frustrations with current tools"
```

### What to Extract

For each segment, document:

1. **Top 10 time-consuming tasks**
   - Daily activities that eat hours
   - Manual data entry, gathering, processing
   - Repetitive decision-making
   - Coordination and communication overhead

2. **Top 10 frustrations with current tools**
   - Complaints about existing software
   - Workarounds people have built
   - "If only this tool could..." statements
   - Integration pain points

3. **Information work bottlenecks**
   - Reading/comprehension loads
   - Research and synthesis needs
   - Report generation
   - Document processing

4. **Current manual workarounds**
   - Copy-paste between systems
   - Spreadsheet gymnastics
   - Email-based processes
   - "Just ask Sarah" knowledge dependencies

5. **Budget allocated to solutions**
   - Current software spend
   - Headcount for these tasks
   - Willingness to pay for better solution

---

## Step 2.2: Segment-Problem Matrix Template

| Segment | Task | Time/Week | Current Cost | Pain Score (1-10) | Automation Potential | Notes |
|---------|------|-----------|--------------|-------------------|---------------------|-------|
| Legal | Case law research | 15hr | $3,750 | 9 | High (6mo) | "Spend half my week reading cases" |
| Finance | Data gathering | 10hr | $1,000 | 8 | High (3mo) | "Copy-paste from 12 systems" |
| Writers | Source research | 8hr | $800 | 7 | High (6mo) | "Research takes longer than writing" |
| Designers | Feedback synthesis | 6hr | $600 | 6 | Medium (12mo) | "Track comments across tools" |
| Managers | Meeting notes | 5hr | $500 | 7 | High (3mo) | "Summarize 20 meetings/week" |

**Pain score factors:**
- Frequency (daily = high, monthly = low)
- Time consumed (>10hr/week = high)
- Cognitive load (tedious = high, engaging = low)
- Error-prone (high risk = high)
- Blocks other work (critical path = high)

---

## Step 2.3: Deep Dive Example - Legal Professionals

**Research execution:**

Search 1: "lawyers biggest time wasters 2024"
- Result: Document review (30%), legal research (25%), admin (20%)

Search 2: "legal workflow automation challenges"
- Result: Citation accuracy, jurisdiction-specific rules, precedent tracking

Search 3: "lawyers AI adoption barriers"
- Result: Trust issues (hallucinations), ethical rules, client confidentiality

Search 4: "site:reddit.com lawyers productivity pain points"
- Result: Threads on manual citation, reading case law, tracking changes in precedent

Search 5: "legal professionals software spending 2024"
- Result: $300-500/month/attorney on research tools (Westlaw, LexisNexis)

**Extracted pain points:**

1. **Legal research** (15hr/week, $3,750/week)
   - Pain: Manual case law reading and synthesis
   - Current: Expensive research databases, still manual reading
   - Frustration: "Find the 3 relevant cases among 300 results"

2. **Document review** (20hr/week, $5,000/week)
   - Pain: Contract review, discovery, due diligence
   - Current: Junior associates or contract attorneys
   - Frustration: "Repetitive, error-prone, expensive"

3. **Citation management** (3hr/week, $750/week)
   - Pain: Ensuring all cites are accurate and properly formatted
   - Current: Manual checking + software assist
   - Frustration: "One wrong cite can derail a case"

4. **Client communication** (5hr/week, $1,250/week)
   - Pain: Explaining legal concepts, status updates
   - Current: Billable time for routine questions
   - Frustration: "Same questions over and over"

5. **Regulatory tracking** (4hr/week, $1,000/week)
   - Pain: Staying current on law changes
   - Current: Manual reading of updates
   - Frustration: "Can't possibly read everything"

**Budget analysis:**
- Current tools: $300-500/month (Westlaw, LexisNexis, practice management)
- Headcount costs: Associates at $150-250/hr doing research
- Willingness to pay: High if it saves billable hours

**Automation potential:**
- Legal research: HIGH (6mo horizon with 500K context + legal corpus)
- Document review: HIGH (3mo horizon with current capabilities)
- Citation management: HIGH (today, with fine-tuning)
- Client communication: MEDIUM (6mo horizon with firm-specific knowledge)
- Regulatory tracking: HIGH (3mo horizon with continuous monitoring)

---

## Step 2.4: First Principles Decomposition

**For each high-pain task, decompose into cognitive primitives:**

### Example: Legal Research

**Task breakdown:**
1. **Understand question** (15 min)
   - Client issue → legal question
   - Identify jurisdiction, area of law
   - Human: 90%, AI today: 60%, AI 6mo: 85%

2. **Search case law** (30 min)
   - Query construction
   - Database search
   - Result filtering
   - Human: 100%, AI today: 90%, AI 6mo: 95%

3. **Read and analyze cases** (4 hours)
   - Comprehension of lengthy documents
   - Identify relevant holdings
   - Note distinctions
   - Human: 100%, AI today: 70%, AI 6mo: 90%

4. **Synthesize findings** (1 hour)
   - Combine multiple cases
   - Identify patterns and conflicts
   - Draft summary
   - Human: 100%, AI today: 80%, AI 6mo: 90%

5. **Apply to client situation** (30 min)
   - Map general law to specific facts
   - Assess strength of argument
   - Make recommendation
   - Human: 100%, AI today: 50%, AI 6mo: 70%

**Economic analysis:**
- Total time: 6.25 hours
- Human cost: $1,560 (at $250/hr)
- AI cost estimate (6mo): $20 (inference) + $10 (tools) = $30
- **ROI: 52x cost reduction**
- **Automatable %: 75% today, 85% at 6mo**
- **Human-in-loop: Question understanding, final judgment**

---

## Step 2.5: Economic Impact Calculation

**Formula:**

```
Economic Impact = (Task Frequency × Time Saved × Hourly Rate) × Market Size

Where:
- Task Frequency: How often task is performed (daily, weekly, monthly)
- Time Saved: Hours automated × % automation success
- Hourly Rate: Cost of human performing task
- Market Size: Number of workers doing this task
```

**Example: Legal Research**

```
- Frequency: 3x per week per attorney
- Time per task: 6.25 hours
- Automation %: 75% (at 6mo horizon)
- Time saved: 6.25 × 0.75 = 4.7 hours
- Attorney rate: $250/hr
- Savings per task: 4.7 × $250 = $1,175
- Savings per attorney per week: $1,175 × 3 = $3,525
- Annual savings per attorney: $3,525 × 50 = $176,250
- Number of attorneys in US: 1.3M
- Addressable market (solo/small firm, 40%): 520,000
- Adoption rate (conservative, 10%): 52,000
- Annual market value: 52,000 × $176,250 = $9.2B
```

**This becomes a business opportunity.**

---

## Step 2.6: Pattern Recognition Across Segments

**Look for common pain patterns:**

### Pattern 1: Information Overload
- **Segments**: Researchers, analysts, managers, healthcare
- **Pain**: Too much to read, need synthesis
- **Solution**: Research Synthesizer synthetic worker
- **Horizon**: 6 months (500K context)

### Pattern 2: Cross-System Data Wrangling
- **Segments**: Finance, operations, sales ops, analysts
- **Pain**: Manual data gathering from multiple systems
- **Solution**: Data Orchestrator synthetic worker
- **Horizon**: 3 months (reliable tool use)

### Pattern 3: Routine Communication
- **Segments**: Managers, sales, support, HR
- **Pain**: Repetitive emails, updates, questions
- **Solution**: Communication Coordinator synthetic worker
- **Horizon**: 3 months (template-based generation)

### Pattern 4: Compliance & Monitoring
- **Segments**: Legal, finance, healthcare, regulated industries
- **Pain**: Continuous tracking of changing rules
- **Solution**: Compliance Auditor synthetic worker
- **Horizon**: 3 months (monitoring + alerting)

### Pattern 5: Document Processing
- **Segments**: Legal, finance, HR, operations
- **Pain**: Extract, validate, transform documents
- **Solution**: Document Processor synthetic worker
- **Horizon**: Today (current capabilities)

---

## Step 2.7: Prioritization Framework

**Rank opportunities by:**

1. **Pain severity** (1-10)
   - How much does this hurt?
   - How often does it occur?
   - What's the cost of NOT solving it?

2. **Economic leverage** (cost reduction multiple)
   - 10x+ = tier 1
   - 5-10x = tier 2
   - 2-5x = tier 3
   - <2x = ignore

3. **Market size** (TAM/SAM)
   - $1B+ TAM = tier 1
   - $100M-1B = tier 2
   - $10M-100M = tier 3
   - <$10M = niche

4. **Time to market** (capability horizon)
   - Today = tier 1
   - 3-6 months = tier 2
   - 12 months = tier 3
   - 18+ months = tier 4

**Priority matrix:**

| Opportunity | Pain | Leverage | TAM | Horizon | Priority |
|-------------|------|----------|-----|---------|----------|
| Legal research automation | 9 | 52x | $9B | 6mo | **P1** |
| Financial data aggregation | 8 | 30x | $5B | 3mo | **P1** |
| Meeting synthesis | 7 | 15x | $12B | 3mo | **P1** |
| Design feedback tracking | 6 | 8x | $500M | 12mo | **P2** |
| Email template generation | 5 | 10x | $2B | 3mo | **P2** |

---

## Phase 2 Deliverable

**Document structure:**

### 1. Segment Analysis (per segment)
- Top 10 time-consuming tasks
- Top 10 tool frustrations
- Information work bottlenecks
- Current workarounds
- Budget analysis

### 2. Segment-Problem Matrix
- Complete spreadsheet with all segments × tasks
- Pain scores, time costs, economic impact
- Automation potential by horizon

### 3. First Principles Decomposition
- Top 20 tasks broken into cognitive primitives
- % automatable today vs future horizons
- Human-in-loop requirements
- Economic calculations

### 4. Pattern Analysis
- Common pain patterns across segments
- Synthetic worker archetypes
- Cross-segment opportunities

### 5. Prioritized Opportunity List
- Top 25-50 opportunities ranked
- Priority tier assignments (P1, P2, P3)
- Quick summary per opportunity

---

## Quality Checks

**Good opportunity discovery has:**
- [ ] Real pain points (from actual user complaints)
- [ ] Quantified time/cost (not vague "it's annoying")
- [ ] Multiple sources per segment (not single article)
- [ ] Budget validation (people pay for solutions)
- [ ] Pattern recognition (common themes across segments)
- [ ] Economic modeling (ROI calculations)
- [ ] Automation feasibility (tied to capabilities)
- [ ] Market sizing (TAM/SAM estimates)

**Red flags:**
- Only hypothetical pain (no user evidence)
- Vague descriptions ("productivity issues")
- Single source per segment
- No budget information
- Missing economic analysis
- Unclear automation potential
- No market size estimates

---

## Tips for Effective Discovery

1. **Trust user complaints more than surveys**: Reddit threads > market research reports
2. **Look for workarounds**: If they built a hack, the pain is real
3. **Follow the money**: What do they already spend on?
4. **Quantify everything**: "Time-consuming" → "15hr/week"
5. **Cross-reference sources**: Validate pain across multiple channels
6. **Talk to practitioners**: Nothing beats primary research
7. **Watch for frequency**: Daily pain >> monthly annoyance

---

**Next phase**: Take prioritized opportunities → generate business models → define synthetic workers

Return to main SKILL.md to proceed to Phase 3: Business Model Generation
