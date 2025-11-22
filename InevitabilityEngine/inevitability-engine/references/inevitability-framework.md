# Phase 5: Inevitability Scoring Framework

**Goal**: Quantify which business opportunities are inevitable and at what time horizon.

---

## The Inevitability Thesis

**A business is inevitable if the economic pressure × technical feasibility × market readiness exceeds adoption friction.**

When this happens, the business **will** come into existence. The only question is: who builds it first?

---

## The Inevitability Formula

```
Inevitability Score = (E × T × M) / F

Where:
E = Economic Pressure [0-10]
T = Technical Feasibility [0-10]
M = Market Readiness [0-10]
F = Adoption Friction [1-10]

Interpretation:
- Score > 30: Inevitable within 12 months
- Score > 25: Inevitable within 18 months
- Score > 20: Likely within 24 months
- Score > 15: Possible within 24 months
- Score < 15: Not inevitable in this horizon
```

**Why this formula works:**
- **Multiplicative numerator**: All three factors must be present (if any is zero, score is zero)
- **Divisive friction**: High barriers can delay even high-pressure opportunities
- **Non-linear**: Small improvements in any factor dramatically change inevitability

---

## Component 1: Economic Pressure (E)

**Definition**: The cost reduction or value creation ratio enabled by the synthetic worker solution.

### Calculation

```
E = (current_cost / ai_cost) - 1

Then scale to 0-10:
- 100x+ cost reduction = 10
- 50x cost reduction = 9
- 20x cost reduction = 8
- 10x cost reduction = 7
- 5x cost reduction = 6
- 3x cost reduction = 5
- 2x cost reduction = 4
- 1.5x cost reduction = 3
- 1.2x cost reduction = 2
- <1.2x cost reduction = 0-1
```

### Example: Legal Research

**Current cost:**
- Attorney time: 6 hours @ $250/hr = $1,500
- Database access: $15 per research project
- Total: $1,515 per research task

**AI cost:**
- Inference: $0.50 (500K tokens @ $1/1M)
- Database/API: $5
- Human QA (10% sampling): $25
- Platform overhead: $2
- Total: $32.50 per research task

**Economic pressure:**
```
E_raw = ($1,515 / $32.50) - 1 = 46.6 - 1 = 45.6x cost reduction
E_scaled = 9 (between 20x and 50x)
```

### Adjustment Factors

**Increase E if:**
- Error costs are high (healthcare, legal, finance) → +1
- Task is time-critical (delays cost money) → +0.5
- Current solution has high fixed costs → +0.5

**Decrease E if:**
- Quality degradation significant → -1 to -2
- Only applies to subset of task → -0.5 to -1
- Requires significant manual oversight → -0.5

**Adjusted E for legal research: 9 + 1 (error costs) = 10**

---

## Component 2: Technical Feasibility (T)

**Definition**: The percentage of the workflow that can be automated with AI at the specified time horizon.

### Calculation

```
T = (% of workflow automatable) × 10

Steps:
1. Decompose workflow into steps
2. Assess each step's automation potential (0-100%)
3. Weight by time/importance
4. Calculate weighted average
5. Scale to 0-10
```

### Example: Legal Research (6-month horizon)

| Step | Time | Human Performance | AI Performance (6mo) | Automatable % | Weighted |
|------|------|-------------------|---------------------|---------------|----------|
| Understand question | 15min | 95% | 80% | 84% | 4.2% × 84% |
| Search case law | 30min | 100% | 95% | 95% | 8.3% × 95% |
| Read & analyze cases | 4hr | 100% | 85% | 85% | 66.7% × 85% |
| Synthesize findings | 1hr | 100% | 90% | 90% | 16.7% × 90% |
| Apply to client case | 30min | 100% | 65% | 65% | 4.2% × 65% |

**Weighted automation:**
```
(4.2% × 84%) + (8.3% × 95%) + (66.7% × 85%) + (16.7% × 90%) + (4.2% × 65%)
= 3.53% + 7.89% + 56.70% + 15.03% + 2.73%
= 85.88%
```

**Technical feasibility:**
```
T = 0.8588 × 10 = 8.6 → round to 9
```

### Adjustment Factors

**Increase T if:**
- Current benchmarks exceed assumptions → +0.5 to +1
- Task has structured inputs/outputs → +0.5
- Domain-specific models available → +0.5

**Decrease T if:**
- Requires tacit knowledge → -0.5 to -1
- Safety-critical (low error tolerance) → -1
- Unstructured/creative work → -0.5 to -1

**Adjusted T for legal research: 9 (already conservative)**

---

## Component 3: Market Readiness (M)

**Definition**: The combination of existing budget availability and behavioral readiness to adopt AI solutions.

### Calculation

```
M = (Budget_Availability + Behavior_Readiness) / 2

Each component scored 0-10
```

### Budget Availability (0-10)

**Scoring:**
- 10: Large existing budget for this problem, actively looking for better solutions
- 8: Moderate budget, currently spent on incumbent solutions
- 6: Some budget, but fragmented across multiple point solutions
- 4: Small budget, mostly manual processes
- 2: No budget currently, would need to find new money
- 0: No budget, no priority

**Indicators:**
- Current software spend on problem
- Headcount allocated to task
- Budget growth trajectory
- Executive priority level

**Example: Legal Research**
```
- Attorneys spend $400-500/month on research databases ✅
- Research is core function, always budgeted ✅
- Market growing (more complex regulations) ✅
- High priority for cost reduction ✅

Budget Availability = 9
```

### Behavior Readiness (0-10)

**Scoring:**
- 10: Already using AI tools, actively experimenting, early adopters
- 8: Aware of AI, some pilots, open to adoption
- 6: Interested but cautious, need proof points
- 4: Skeptical but willing to listen
- 2: Resistant, prefer traditional approaches
- 0: Hostile to automation

**Indicators:**
- Existing AI tool adoption in segment
- Discussion volume about AI in segment
- Influencer endorsements
- Competitive pressure (peers adopting)

**Example: Legal Research**
```
- Some AI legal tools emerging (Casetext, Harvey) ✅
- Attorneys discussing AI on social media ✅
- But: Conservative profession, trust concerns ⚠️
- But: Ethics rules create hesitation ⚠️

Behavior Readiness = 6
```

### Combined Market Readiness

```
M = (Budget_Availability + Behavior_Readiness) / 2
M = (9 + 6) / 2 = 7.5 → round to 8
```

---

## Component 4: Adoption Friction (F)

**Definition**: The barriers that slow or prevent adoption, even when value is clear.

### Calculation

```
F = Integration_Cost + Trust_Gap + Regulatory_Barrier

Each component scored 0-3.33 (total: 1-10)
Higher score = more friction = lower inevitability
```

### Integration Cost (0-3.33)

**Scoring:**
- 0: Zero integration (standalone web app)
- 1: Simple integration (API, SSO)
- 2: Moderate integration (multiple systems, data migration)
- 3.33: Complex integration (deep workflow changes, infrastructure)

**Example: Legal Research**
```
- Standalone research tool ✅
- Optional integrations with practice management
- Some training required
- Not mission-critical infrastructure

Integration Cost = 1.5
```

### Trust Gap (0-3.33)

**Scoring:**
- 0: Low-stakes, errors are tolerable
- 1: Medium stakes, errors caught easily
- 2: High stakes, errors are costly
- 3.33: Critical stakes, errors are catastrophic

**Factors:**
- Professional liability
- Client risk
- Reputation damage
- Regulatory exposure

**Example: Legal Research**
```
- High stakes (legal advice) ⚠️
- But: Research is just input to attorney judgment ✅
- Errors caught in review process ✅
- Attorneys maintain responsibility ✅

Trust Gap = 2.0
```

### Regulatory Barrier (0-3.33)

**Scoring:**
- 0: No regulations
- 1: Light compliance requirements (SOC2, privacy)
- 2: Industry-specific rules (HIPAA, financial)
- 3.33: Licensing, approval processes, strict restrictions

**Example: Legal Research**
```
- Unauthorized practice of law concerns ⚠️
- Attorney-client privilege requirements ⚠️
- But: Tool positioning (not legal advice) ✅
- But: Attorney oversight maintained ✅

Regulatory Barrier = 1.5
```

### Combined Adoption Friction

```
F = Integration_Cost + Trust_Gap + Regulatory_Barrier
F = 1.5 + 2.0 + 1.5 = 5.0
```

---

## Final Inevitability Score

### Legal Research AI Assistant (6-month horizon)

```
E = 10 (45x cost reduction)
T = 9 (85% automatable)
M = 8 (strong budget, moderate behavior readiness)
F = 5 (moderate friction)

Inevitability = (E × T × M) / F
Inevitability = (10 × 9 × 8) / 5
Inevitability = 720 / 5
Inevitability = 144

Wait, that's too high. The formula needs recalibration...
```

### REVISED FORMULA

The issue is that raw multiplication creates scores that are too high. Let's use a normalized version:

```
Inevitability = (E/10 × T/10 × M/10) / (F/10) × 100

This gives scores from 0-100
```

**Recalculated:**
```
Inevitability = (1.0 × 0.9 × 0.8) / 0.5 × 100
Inevitability = 0.72 / 0.5 × 100
Inevitability = 1.44 × 100
Inevitability = 144

Still too high...
```

### FINAL CORRECTED FORMULA

```
Inevitability = ((E + T + M) / 3) - (F / 2)

This creates a 0-10 scale where:
- Perfect opportunity: (10 + 10 + 10) / 3 - (1 / 2) = 9.5
- Threshold for inevitable: > 7
- Likely: 5-7
- Possible: 3-5
- Unlikely: < 3
```

**Legal Research Final Score:**
```
Inevitability = ((10 + 9 + 8) / 3) - (5 / 2)
Inevitability = (27 / 3) - 2.5
Inevitability = 9.0 - 2.5
Inevitability = 6.5

Interpretation: LIKELY inevitable within 6-12 months
```

---

## Scoring Interpretation Guide

| Score | Interpretation | Timing | Action |
|-------|----------------|--------|--------|
| **8.5-10** | Inevitable NOW | 3-6 months | Drop everything, build immediately |
| **7-8.5** | Highly inevitable | 6-12 months | Prioritize, start planning |
| **5-7** | Likely inevitable | 12-18 months | Monitor closely, prepare |
| **3-5** | Possible | 18-24+ months | Track, wait for catalyst |
| **<3** | Unlikely | 24+ months or never | Revisit assumptions |

---

## Sensitivity Analysis

**For each opportunity, test score sensitivity:**

### What if assumptions change?

**Scenario 1: Pessimistic**
- Technical feasibility 20% lower (T = 7 instead of 9)
- Behavior readiness slower (M = 6 instead of 8)

```
Inevitability = ((10 + 7 + 6) / 3) - 2.5 = 7.67 - 2.5 = 5.17
Still LIKELY but delayed
```

**Scenario 2: Optimistic**
- Cost reduction even better (E = 10, already maxed)
- Integration easier than expected (F = 3 instead of 5)

```
Inevitability = ((10 + 9 + 8) / 3) - 1.5 = 9.0 - 1.5 = 7.5
HIGHLY inevitable, earlier timeline
```

**Scenario 3: Competitive pressure**
- Well-funded competitor launches → Increases behavior readiness (M = 9)
- Market validation → Reduces trust gap (F = 4)

```
Inevitability = ((10 + 9 + 9) / 3) - 2.0 = 9.33 - 2.0 = 7.33
HIGHLY inevitable, market heating up
```

---

## Comparative Scoring Template

**Score multiple opportunities to build portfolio:**

| Opportunity | E | T | M | F | Score | Timing | Priority |
|-------------|---|---|---|---|-------|--------|----------|
| Legal research AI | 10 | 9 | 8 | 5 | 6.5 | 6-12mo | P1 |
| Financial data aggregation | 8 | 9 | 9 | 3 | 7.17 | 3-6mo | P1 |
| Meeting synthesis | 6 | 10 | 9 | 2 | 7.5 | 3mo | P1 |
| Design feedback tracker | 5 | 7 | 6 | 4 | 4.0 | 12-18mo | P2 |
| Code review automation | 7 | 8 | 8 | 3 | 6.17 | 6-12mo | P2 |

**Portfolio insights:**
- Meeting synthesis: Highest score, move now
- Financial data aggregation: High score, low friction
- Legal research: Strong fundamentals, moderate friction
- Design feedback: Possible but wait for catalyst
- Code review: Solid, competitive market

---

## Time-Horizon Adjustment

**Scores change over time as capabilities improve:**

### Legal Research: Horizon Sensitivity

**Today:**
- T = 6 (only 60% automatable with 128K context)
- Score = ((10 + 6 + 8) / 3) - 2.5 = 5.5 (LIKELY but marginal)

**3 months:**
- T = 7 (70% automatable with 200K context)
- Score = ((10 + 7 + 8) / 3) - 2.5 = 5.83 (LIKELY)

**6 months:**
- T = 9 (85% automatable with 500K context)
- M = 8 (more awareness)
- Score = ((10 + 9 + 8) / 3) - 2.5 = 6.5 (LIKELY)

**12 months:**
- T = 10 (95% automatable with 1M context)
- M = 9 (proven solutions in market)
- F = 4 (trust gap narrowing)
- Score = ((10 + 10 + 9) / 3) - 2.0 = 7.67 (HIGHLY INEVITABLE)

**Insight: Opportunity strengthens over time → Early mover advantage**

---

## Phase 5 Deliverable

**Document structure:**

### 1. Scoring Methodology
- Formula explanation
- Component definitions
- Calibration examples

### 2. Scored Opportunities
- All opportunities with component scores
- Final inevitability scores
- Timing estimates

### 3. Ranked Portfolio
- Sorted by inevitability score
- Segmented by time horizon
- Priority assignments

### 4. Sensitivity Analysis
- Pessimistic/optimistic scenarios
- Time-horizon trajectories
- Key assumption risks

### 5. Strategic Recommendations
- Top 5 opportunities to pursue
- Timing and sequencing
- Resource allocation

---

## Quality Checks

**Good inevitability analysis has:**
- [ ] Quantified component scores (not gut feel)
- [ ] Clear methodology (reproducible)
- [ ] Sensitivity analysis (tested assumptions)
- [ ] Time-horizon awareness (how scores evolve)
- [ ] Comparative rankings (portfolio view)
- [ ] Strategic insights (not just scores)

**Red flags:**
- Scores based on feeling, not calculation
- All opportunities score high (not selective enough)
- No sensitivity testing
- Ignoring time-horizon dynamics
- Treating scores as absolute truth (they're estimates)

---

**Next phase**: Take scored opportunities → synthesize into deliverable → create action plan

Return to main SKILL.md to proceed to Phase 6: Synthesis & Output
