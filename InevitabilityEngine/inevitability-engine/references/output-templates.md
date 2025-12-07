# Output Templates & Deliverable Formats

**Structured templates for Phase 6 synthesis and final deliverables.**

---

## Executive Summary Template (2 pages)

### Page 1: Context & Key Findings

```markdown
# [Project Name]: AI Business Opportunity Analysis
## Executive Summary

### Research Context
- **Time period**: [Date range]
- **Scope**: [Segments analyzed, time horizons]
- **Methodology**: Inevitability Engine research protocol

### Capability Trajectory
The AI capability landscape is evolving across three key dimensions:

1. **Context windows**: [Current] → [6mo] → [12mo] → [24mo]
2. **Inference cost**: [Current] → [Projected decline]
3. **Tool reliability**: [Current %] → [Projected %]

**Key unlock**: [Most significant capability improvement and timing]

### Market Landscape
- **Segments analyzed**: [Number]
- **Pain points identified**: [Number]
- **Business opportunities generated**: [Number]
- **High-scoring opportunities** (inevitability > 7): [Number]

### Strategic Insight
[2-3 sentence insight about the opportunity space]
```

---

### Page 2: Top Opportunities & Recommendations

```markdown
### Top 10 Opportunities by Inevitability Score

| Rank | Opportunity | Score | Horizon | TAM | Quick Summary |
|------|-------------|-------|---------|-----|---------------|
| 1 | [Name] | [X.X] | [Xmo] | $[X]B | [One sentence] |
| 2 | [Name] | [X.X] | [Xmo] | $[X]M | [One sentence] |
| ... | ... | ... | ... | ... | ... |

### Recommendations for [Organization]

**Immediate action (0-90 days):**
1. [Opportunity name]: [Specific action]
2. [Opportunity name]: [Specific action]

**Strategic investment (3-12 months):**
1. [Opportunity name]: [Rationale]
2. [Opportunity name]: [Rationale]

**Monitor & prepare (12+ months):**
1. [Opportunity name]: [Why wait and what to watch]

### Resource Allocation
- **Internal tools**: [Opportunities that fit BetterUp strategy]
- **Catalyst offerings**: [Opportunities that are packageable/repeatable]
- **Potential spin-outs**: [Venture-scale opportunities]
```

---

## Opportunity Matrix Template (Spreadsheet)

### Columns to Include

```
1. Opportunity Name
2. Synthetic Worker Role
3. Target Segment
4. Problem Solved
5. Time Horizon (3mo, 6mo, 12mo, 18mo, 24mo)
6. Economic Pressure (E, 0-10)
7. Technical Feasibility (T, 0-10)
8. Market Readiness (M, 0-10)
9. Adoption Friction (F, 1-10)
10. Inevitability Score
11. TAM ($)
12. SAM ($)
13. SOM Year 5 ($)
14. Current Cost (manual)
15. AI Cost (automated)
16. Cost Reduction Multiple
17. Competitor Count
18. Top Competitor
19. Differentiation
20. GTM Strategy
21. Priority (P1/P2/P3)
22. Recommended Action
23. Notes/Risks
```

### Sorting & Filtering

**Primary sort**: Inevitability Score (descending)
**Secondary sort**: Time Horizon (ascending)
**Filters**: Segment, Horizon, Priority

---

## Deep Dive Template (5-10 pages per opportunity)

```markdown
# [Opportunity Name]
## Deep Dive Analysis

### Executive Summary
[2-3 paragraphs covering problem, solution, market, score]

---

### 1. Market Analysis

#### Problem Statement
**Current state**: [How task is done today]
**Pain points**:
- [Pain 1]: [Description and evidence]
- [Pain 2]: [Description and evidence]
- [Pain 3]: [Description and evidence]

**Economic impact**: [Quantified cost of current approach]

#### Target Segment
**Primary**: [Segment description]
- Size: [Number of potential users]
- Characteristics: [Key attributes]
- Current behavior: [How they work today]

**Secondary segments**: [Future expansion targets]

#### Market Size
- **TAM**: $[X]B ([Methodology])
- **SAM**: $[X]M ([Subset and rationale])
- **SOM projections**:
  - Year 1: [Customer count] × $[ARPU] = $[Revenue]
  - Year 3: [Customer count] × $[ARPU] = $[Revenue]
  - Year 5: [Customer count] × $[ARPU] = $[Revenue]

---

### 2. Technical Feasibility

#### Capability Requirements
| Capability | Required Level | Current Status | Horizon |
|------------|----------------|----------------|---------|
| Context window | [X]K tokens | [Y]K available | [Z]mo |
| Tool reliability | [X]% accuracy | [Y]% current | [Z]mo |
| Domain knowledge | [Specific area] | [Via fine-tuning] | [Z]mo |

#### Synthetic Worker Definition
**Role title**: [e.g., "Research Synthesizer"]
**Job description**: [What it does]

**SLA**:
- Accuracy: [X]%
- Speed: [Time per task]
- Throughput: [Volume per day]
- Availability: [Uptime %]
- Escalation: [When to involve human]

**Eval framework**:
- Automated metrics: [What's measured automatically]
- Human evaluation: [Sampling rate and criteria]
- Continuous improvement: [Feedback loop design]

#### Workflow Automation
| Step | Human Time | AI Time | Automatable % | Human-in-Loop |
|------|------------|---------|----------------|---------------|
| [Step 1] | [X]min | [Y]min | [Z]% | [Yes/No + why] |
| [Step 2] | [X]min | [Y]min | [Z]% | [Yes/No + why] |
| **Total** | [X]hr | [Y]hr | [Z]% | [Summary] |

**Technical feasibility score**: [X]/10
**Rationale**: [Why this score]

---

### 3. Business Model

#### Value Proposition
**For [target segment]**: [One sentence value prop]

**Key benefits**:
1. [Benefit]: [Quantified impact]
2. [Benefit]: [Quantified impact]
3. [Benefit]: [Quantified impact]

#### Unit Economics
**Customer acquisition**:
- CAC: $[X] ([Channel and assumptions])
- Payback period: [X] months
- LTV: $[X] ([Retention and expansion assumptions])
- LTV:CAC ratio: [X:1]

**Delivery costs (per customer/month)**:
- Inference: $[X] ([Volume × cost/token])
- Infrastructure: $[X] ([Hosting, databases, etc.])
- Human oversight: $[X] ([% of tasks requiring review])
- Customer success: $[X] ([Support and onboarding])
- **Total COGS**: $[X]

**Pricing**:
- Model: [Per-seat / usage-based / outcome-based]
- Price point: $[X]/month
- **Gross margin**: [X]%

**Break-even**:
- Customers needed: [X] ([COGS × overhead ÷ gross profit per customer])
- Timeline: [X] months ([Assumption about growth rate])

#### Go-to-Market Strategy

**Initial target** (wedge):
- Segment: [Specific niche]
- Size: [Addressable customers]
- Why them: [Strategic reasoning]

**Channels**:
1. [Channel 1]: [Approach and economics]
2. [Channel 2]: [Approach and economics]

**Land and expand**:
- Land: [Initial use case]
- Expand: [Path to broader adoption]

---

### 4. Competitive Analysis

#### Landscape
| Competitor | Type | Positioning | Stage | Strengths | Weaknesses |
|------------|------|-------------|-------|-----------|------------|
| [Name] | AI-native/Bolt-on | [Value prop] | [Stage] | [Top 2-3] | [Top 2-3] |

#### Competitive Positioning

**vs. Incumbents**: [How we're different/better]
**vs. AI-native startups**: [Our unique advantage]
**vs. DIY/Manual**: [Why not just hire someone or build internally]

**Moat & Defensibility**:
1. [Moat type]: [How it works]
2. [Moat type]: [How it works]

**Barriers to entry**:
- Technical: [What's hard to replicate]
- Data: [Proprietary datasets or flywheels]
- Distribution: [Partnerships, integrations, network]
- Regulatory: [Compliance, certifications]

---

### 5. Inevitability Analysis

#### Component Scores

**Economic Pressure (E): [X]/10**
- Current cost: $[X]
- AI cost: $[X]
- Cost reduction: [Y]x
- Rationale: [Why this score]

**Technical Feasibility (T): [X]/10**
- % automatable: [Y]%
- Current vs horizon: [Today X%, [Z]mo Y%]
- Rationale: [Why this score]

**Market Readiness (M): [X]/10**
- Budget availability: [Y]/10 ([Evidence])
- Behavior readiness: [Z]/10 ([Evidence])
- Rationale: [Why this score]

**Adoption Friction (F): [X]/10**
- Integration cost: [Y]/3.33
- Trust gap: [Z]/3.33
- Regulatory barrier: [W]/3.33
- Rationale: [Why this score]

#### Final Score
**Inevitability = ([E + T + M] / 3) - (F / 2) = [X.X]**

**Interpretation**: [Inevitable NOW / Highly inevitable / Likely / Possible / Unlikely]
**Timeline**: [When this becomes inevitable]

#### Sensitivity Analysis
| Scenario | E | T | M | F | Score | Impact |
|----------|---|---|---|---|-------|--------|
| Base case | [X] | [X] | [X] | [X] | [X.X] | [Timeline] |
| Pessimistic | [X] | [X] | [X] | [X] | [X.X] | [Impact on timeline] |
| Optimistic | [X] | [X] | [X] | [X] | [X.X] | [Impact on timeline] |

---

### 6. Risk Assessment

#### Technical Risks
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Strategy] |

#### Market Risks
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Strategy] |

#### Regulatory Risks
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Strategy] |

---

### 7. Strategic Recommendation

#### For [Organization]

**Recommended action**: [Internal tool / Catalyst offering / Spin-out / Pass]

**Rationale**:
- [Reason 1]
- [Reason 2]
- [Reason 3]

**If pursuing**:
- **Next steps** (0-30 days): [Specific actions]
- **Resource requirements**: [Team, budget, timeline]
- **Success metrics**: [How to measure progress]
- **Decision gates**: [When to re-evaluate]

**If monitoring**:
- **Triggers to re-evaluate**: [What would change decision]
- **Information to gather**: [What to track]
- **Timeline**: [When to revisit]
```

---

## Research Appendix Template

```markdown
# Research Appendix

## Search Queries Executed

### Phase 1: Capability Mapping
- [Query 1]: [Result summary]
- [Query 2]: [Result summary]
[...]

### Phase 2: Opportunity Discovery
- [Query 1]: [Result summary]
- [Query 2]: [Result summary]
[...]

### Phase 3: Business Model Generation
[...]

### Phase 4: Market Validation
[...]

### Phase 5: Inevitability Scoring
[...]

---

## Key Sources

### Capability Data
1. [Source 1]: [Citation and key findings]
2. [Source 2]: [Citation and key findings]
[...]

### Market Data
1. [Source 1]: [Citation and key findings]
2. [Source 2]: [Citation and key findings]
[...]

### Competitive Intelligence
1. [Source 1]: [Citation and key findings]
2. [Source 2]: [Citation and key findings]
[...]

---

## Assumptions Log

| Assumption | Source | Confidence | Impact if Wrong |
|------------|--------|------------|-----------------|
| [Assumption 1] | [Source/Reasoning] | High/Med/Low | [What happens] |
| [Assumption 2] | [Source/Reasoning] | High/Med/Low | [What happens] |
[...]

---

## Uncertainty Flags

### High Uncertainty
- [Area 1]: [What's unclear and why it matters]
- [Area 2]: [What's unclear and why it matters]

### Medium Uncertainty
- [Area 1]: [What's unclear and why it matters]
- [Area 2]: [What's unclear and why it matters]

### Requires Primary Research
- [Topic 1]: [Why secondary research insufficient]
- [Topic 2]: [Why secondary research insufficient]

---

## Gaps in Research

### Information Not Found
- [What was sought]: [Why it matters]
- [What was sought]: [Why it matters]

### Contradictory Information
- [Topic]: [Source A says X, Source B says Y, implications]

### Outdated Information
- [Topic]: [Latest data is from [date], may have changed]
```

---

## Presentation Deck Template (for stakeholders)

### Slide 1: Title
```
[Organization] AI Business Opportunity Analysis
The Inevitability Engine Research Report
[Date]
```

### Slide 2: Executive Summary
```
- X opportunities identified across Y segments
- Top 10 scored for inevitability (range: [min] - [max])
- Z opportunities recommended for immediate action
- Total addressable market: $[X]B across opportunities
```

### Slide 3: Capability Trajectory
```
[Visual timeline showing capability unlocks across 3-24 month horizons]
Key insight: [What becomes possible that wasn't before]
```

### Slides 4-6: Top 3 Opportunities
```
[One slide per opportunity]
- Problem & solution
- Market size & score
- Key differentiator
- Recommended action
```

### Slide 7: Full Portfolio
```
[Bubble chart or matrix]
- X-axis: Time horizon
- Y-axis: Inevitability score
- Size: Market size
- Color: Priority tier
```

### Slide 8: Strategic Recommendations
```
- Immediate action items
- Strategic investments
- Monitor & prepare
- Resource allocation
```

### Slide 9: Next Steps
```
- Decision needed: [What]
- Timeline: [When]
- Resources: [What's required]
- Success metrics: [How to measure]
```

---

## One-Pager Template (per opportunity)

```markdown
# [Opportunity Name]
*[Tagline - one sentence value prop]*

## The Problem
[2-3 sentences on current pain]

## The Solution
[2-3 sentences on synthetic worker approach]

## The Market
- **Segment**: [Who]
- **TAM**: $[X]B
- **Target**: [Specific niche to start]

## Why Now
[Capability unlock that makes this inevitable]

## The Numbers
- **Current cost**: $[X] per [unit]
- **AI cost**: $[X] per [unit]
- **Savings**: [Y]x reduction
- **Pricing**: $[X]/month
- **Margin**: [Z]%

## Competition
[2 sentences on landscape and differentiation]

## Inevitability Score: [X.X]/10
**[Inevitable NOW / Highly inevitable / Likely]** | Timeline: [X] months

## Recommended Action
[Internal tool / Catalyst offering / Spin-out / Pass]

**Next step**: [Specific action]
```

---

## Quality Checklist for Deliverables

**Executive Summary:**
- [ ] Context clearly stated
- [ ] Key findings highlighted
- [ ] Top opportunities ranked
- [ ] Recommendations actionable
- [ ] Fits on 2 pages

**Opportunity Matrix:**
- [ ] All opportunities included
- [ ] Scores calculated consistently
- [ ] Sortable and filterable
- [ ] Key data points present

**Deep Dives:**
- [ ] Complete analysis per template
- [ ] Data sourced and cited
- [ ] Assumptions clearly stated
- [ ] Risks honestly assessed
- [ ] Recommendations clear

**Research Appendix:**
- [ ] All queries documented
- [ ] Sources cited
- [ ] Assumptions logged
- [ ] Uncertainties flagged
- [ ] Gaps noted

---

Return to main SKILL.md for full workflow or to Phase 6 for synthesis guidance.
