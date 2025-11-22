# Phase 4: Market Validation & Refinement

**Goal**: Validate demand, size markets, analyze competition, and refine positioning for top opportunities.

---

## Step 4.1: Market Validation Research

**For each top business opportunity (P1/P2 from Phase 3):**

### Validation Layer 1: Existing Solutions

**Research protocol:**

```
Search 1: "[business concept] startup 2024"
Search 2: "[business concept] AI tool"
Search 3: "[segment] [task] automation software"
Search 4: "[problem] solution market"
Search 5: "site:ycombinator.com [business concept]"
```

**What to assess:**

1. **Do competitors exist?**
   - Yes → Market validation (someone's trying)
   - No → Either too early OR not a real problem

2. **Are they AI-native or bolt-on?**
   - AI-native: Built around LLM capabilities, workflow designed for AI
   - Bolt-on: Traditional software + "AI features"
   - **Opportunity**: Out-AI the bolt-ons, out-execute the natives

3. **What's their positioning?**
   - Extract: Value prop, target segment, pricing, GTM
   - Look for: Gaps, weak points, unhappy customers

4. **How mature are they?**
   - Stage: Pre-seed, seed, Series A+
   - Traction: Customer count, revenue (if public)
   - Team: Size, expertise, investors
   - **Signal**: Series A+ with traction = validated market

**Output template:**

| Competitor | Type | Positioning | Stage | Strengths | Weaknesses | Opportunity |
|------------|------|-------------|-------|-----------|------------|-------------|
| LegalRobot | AI-native | Legal research for solos | Series A | Good UX | Limited depth | Better synthesis |
| WestlawAI | Bolt-on | Added to existing | Mature | Distribution | Clunky integration | Native experience |
| StartupX | AI-native | Research automation | Seed | Fast iteration | Narrow focus | Broader scope |

---

### Validation Layer 2: Buyer Intent Signals

**Research protocol:**

```
Search 1: "site:reddit.com [segment] looking for [solution]"
Search 2: "site:twitter.com [problem] wish I could automate"
Search 3: "site:news.ycombinator.com [problem] solutions"
Search 4: "[problem] software recommendations"
Search 5: "[segment] [task] tools discussion"
```

**What to look for:**

1. **Unprompted pain expression**
   - "I spend 10 hours a week on..."
   - "Why is there no tool that..."
   - "Paying $X/month for Y but it doesn't..."

2. **Active search behavior**
   - "Looking for recommendations for..."
   - "Has anyone tried..."
   - "What do you use for..."

3. **Workaround sharing**
   - "Here's my hack for..."
   - "I built a script that..."
   - "My manual process is..."
   - **Signal**: If they built a workaround, pain is REAL

4. **Budget evidence**
   - "Currently paying $X for..."
   - "Would pay $Y if it could..."
   - Tool comparison discussions (shows shopping behavior)

**Scoring rubric:**

- **High intent** (10+ discussions, recent, specific pain, budget mentions)
- **Medium intent** (3-10 discussions, some specific pain)
- **Low intent** (1-2 mentions, vague complaints)
- **No signal** (crickets - RED FLAG)

**Example - Legal Research:**

```
✅ Reddit r/lawyers: 15 threads on "best legal research alternatives to Westlaw"
✅ Twitter: Attorneys complaining about $500/month research costs
✅ HN: Discussion of "why legal research hasn't been disrupted"
✅ LegalTech forums: Active threads on case law automation
✅ Budget: Multiple mentions of $300-500/month spend

→ HIGH INTENT SIGNAL
```

---

### Validation Layer 3: Market Sizing

**TAM/SAM/SOM framework:**

**TAM (Total Addressable Market):**
- All potential customers in universe
- Research: "[segment] market size 2024"
- Calculate: # of workers × average salary × % of time on task

**SAM (Serviceable Addressable Market):**
- Subset you can actually reach
- Geographic: US-only vs global
- Segment: Solo/small vs enterprise
- Typically 20-40% of TAM

**SOM (Serviceable Obtainable Market):**
- What you can capture in 3-5 years
- Year 1: 0.1-0.5% of SAM
- Year 3: 1-5% of SAM (if successful)
- Year 5: 5-15% of SAM (if market leader)

**Research protocol:**

```
Search 1: "[segment] market size 2024"
Search 2: "[job function] employment statistics [country]"
Search 3: "[job function] salary data [geography]"
Search 4: "[segment] software spending trends"
Search 5: "[industry] technology adoption rates"
```

**Example - Legal Research Assistant:**

```
TAM calculation:
- Attorneys in US: 1,330,000
- Average salary: $140,000
- Time on research: 25% = $35,000/attorney/year
- Software capture: 20% of time value = $7,000/attorney/year
- TAM: 1.33M × $7,000 = $9.3B

SAM calculation:
- Solo/small firm (more price-sensitive, less IT): 40% = 532,000
- Adoption-ready (tech-forward): 50% = 266,000
- SAM: 266,000 × $7,000 = $1.86B

SOM calculation:
- Year 1: 0.5% of SAM = 1,330 customers × $6,000 = $8M
- Year 3: 3% of SAM = 7,980 customers × $6,000 = $48M
- Year 5: 10% of SAM = 26,600 customers × $6,000 = $160M

→ Venture-scale opportunity ✅
```

**Validation thresholds:**

- **Venture-scale**: SAM > $500M, SOM Y5 > $100M
- **Sustainable SaaS**: SAM > $100M, SOM Y5 > $20M
- **Niche play**: SAM > $20M, SOM Y5 > $5M
- **Too small**: SAM < $20M (unless strategic)

---

### Validation Layer 4: Willingness to Pay

**Research protocol:**

```
Search 1: "[segment] software budget allocation"
Search 2: "[task] automation ROI case studies"
Search 3: "[similar tool] pricing"
Search 4: "[segment] cost of [task] manual process"
Search 5: "site:reddit.com [segment] worth paying for [solution]"
```

**Pricing validation framework:**

1. **Anchor to value created**
   - If saves $10,000/month, can charge $1,000-3,000/month (10-30% of savings)
   - If replaces $50,000 salary, can charge $500-1,500/month (12-36% of cost)

2. **Compare to incumbents**
   - Westlaw: $500/month → Can price at $300-500 if better
   - Manual process: $3,750/week → Can charge $500/month for 75% automation

3. **Segment sensitivity**
   - Enterprise: Less price-sensitive, more feature/compliance-focused
   - SMB: Very price-sensitive, need clear ROI
   - Prosumer: Moderate sensitivity, value convenience highly

4. **Pricing model fit**
   - Per-seat: Predictable, easy to understand (good for SMB)
   - Usage-based: Scales with value, aligns incentives (good for variable use)
   - Outcome-based: Highest ceiling, requires strong proof (good for enterprise)

**Example - Legal Research:**

```
Incumbent pricing:
- Westlaw: $500/month
- LexisNexis: $400/month
- Casetext (AI): $89/month (limited features)

Value created:
- Saves 10hr/week @ $250/hr = $10,000/month
- Can justify: $500-1,500/month

Segment:
- Solo practitioners: Price-sensitive → $89-299/month
- Small firms (2-10): Moderate → $299-599/month
- Mid-size (10-50): Less sensitive → $599-999/month

Chosen model: $299/month per attorney
- 3% of value created (conservative)
- 60% of Westlaw (competitive)
- 3.3x Casetext (premium positioning)
- 25-30 research projects/month = $10/project cost

→ Strong willingness to pay ✅
```

---

## Step 4.2: Competitive Differentiation Analysis

**For each identified competitor:**

### Competitor Deep Dive Template

**1. What's their wedge?**
- Product-led: Viral growth, self-serve, bottoms-up
- Sales-led: Enterprise focus, top-down, high-touch
- Platform: Ecosystem, integrations, marketplace
- Community: Open-source, thought leadership, network

**2. What's their constraint?**
- Technical debt: Built on old architecture, can't ship fast
- Sales cycle: Enterprise contracts, long pilots
- Capital: Underfunded, can't invest in AI
- Distribution: No channel, expensive CAC
- Team: Founders not AI-native, slow to adapt

**3. What's the orthogonal attack?**
- Different segment: Target who they ignore (e.g., SMB vs enterprise)
- Different workflow: Solve related problem they don't (e.g., end-to-end vs point solution)
- Different pricing: Disruptive (10x cheaper) or premium (10x better)
- Different GTM: Product-led vs their sales-led

**Example - Legal Research Market:**

| Competitor | Wedge | Constraint | Orthogonal Attack |
|------------|-------|------------|-------------------|
| Westlaw | Distribution (owned by Thomson Reuters) | Legacy tech, slow AI adoption | AI-native, $299 vs $500, solos |
| Casetext | Product-led, AI-first | Limited depth, narrow scope | Deeper synthesis, broader practice areas |
| StartupX | Modern UX, fast iteration | Small team, limited capital | Domain expertise, enterprise ready |

**Our differentiation:**
- AI-native architecture (not bolt-on)
- Synthesis quality (not just search)
- Solo/small firm focus (not enterprise-first)
- Product-led growth (not sales-led)
- $299 price point (not $500 or $89)

---

## Step 4.3: Customer Discovery (If Possible)

**If you have access to potential customers:**

### Interview Protocol

**5 key questions:**

1. **How do you do [task] today?**
   - Listen for: Workarounds, pain points, time spent
   - Goal: Understand current state

2. **What have you tried to solve this?**
   - Listen for: Tools evaluated, budget spent, why they failed
   - Goal: Understand switching costs and willingness to try new solutions

3. **If you had a magic wand, what would the perfect solution do?**
   - Listen for: Must-haves vs nice-to-haves
   - Goal: Understand ideal end-state

4. **What would you pay for that solution?**
   - Listen for: Actual number, comparison to current spend
   - Goal: Validate pricing assumptions

5. **What would prevent you from adopting it?**
   - Listen for: Trust, integration, compliance, inertia
   - Goal: Understand adoption friction

**Validation criteria:**

- **Strong signal**: Immediate interest, asks when available, introduces to others
- **Medium signal**: Interested but wants to see more, concerns but addressable
- **Weak signal**: Polite but no urgency, lots of "maybe" and "someday"
- **No signal**: Not interested, happy with current solution

**Need at least 10 interviews to validate, ideally 20-30.**

---

## Step 4.4: Build-vs-Buy Decision Framework

**For opportunities that validate, decide strategic fit:**

### Decision Matrix

| Criteria | Internal Tool | Catalyst Offering | Spin-out Startup | Open Source |
|----------|---------------|-------------------|------------------|-------------|
| **Time to revenue** | Long (internal ROI) | Medium (months) | Long (years) | None (reputation) |
| **Strategic alignment** | High (BetterUp synergy) | Medium (repeatable) | Low (different business) | Low (community) |
| **Repeatability** | Low (custom) | High (packageable) | Medium (venture) | N/A |
| **Capital required** | Low (OpEx) | Low (bootstrappable) | High (VC-scale) | Low (volunteer) |
| **Upside potential** | Medium (cost savings) | Medium (service revenue) | High (equity value) | Reputation/brand |
| **Control** | Full | High | Low (investors) | None (community) |
| **Risk** | Low | Medium | High | Low |

### Decision Tree

**Is this strategically valuable to BetterUp/Catalyst?**
- YES → Could it be packaged as repeatable Catalyst offering?
  - YES → **Catalyst offering**
  - NO → Is upside >$100M?
    - YES → **Spin-out startup**
    - NO → **Internal tool**
- NO → Is market opportunity >$500M?
  - YES → **Spin-out startup**
  - NO → Is there community/thought leadership value?
    - YES → **Open source**
    - NO → **Pass**

---

## Step 4.5: Risk Assessment & Mitigation

**For each validated opportunity, assess risks:**

### Risk Categories

**1. Technical Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| AI capability doesn't improve as projected | Medium | High | Build with today's capabilities, horizon unlocks as bonus |
| Hallucination rate too high for production | Medium | High | Human-in-loop validation, confidence thresholds, eval framework |
| Integration complexity underestimated | Medium | Medium | Start with simple integrations, modular architecture |
| Cost doesn't decline as projected | Low | Medium | Design for current pricing, margin improves with decline |

**2. Market Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Customers don't trust AI for critical tasks | High | High | Human-in-loop, gradual trust-building, transparency |
| Incumbents add AI features | High | Medium | Move faster, better AI-native UX, sustained innovation |
| Price competition drives margins down | Medium | High | Differentiate on quality, build moat, target less price-sensitive |
| Slower adoption than projected | Medium | Medium | Extend runway, focus on high-intent segments first |

**3. Regulatory Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Professional liability for AI errors | Medium | High | Insurance, human oversight, clear disclaimers, audit trails |
| Data privacy regulations (GDPR, etc.) | Low | High | Privacy-by-design, on-premise options, compliance certifications |
| Industry-specific licensing restrictions | Medium | High | Legal review early, structure as "tool" not "service", partnerships |

**4. Competitive Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Well-funded startup enters space | High | Medium | Move fast, build moat, focus on segment |
| OpenAI/Anthropic build directly | Low | High | Partner with them, focus on domain expertise, different wedge |
| Incumbents acquire AI startups | Medium | High | Become the acquisition target, or out-execute post-acquisition |

---

## Phase 4 Deliverable

**Document structure:**

### 1. Market Validation Summary
- Top 10 opportunities validated
- Competitor landscape per opportunity
- Buyer intent signals (strong/medium/weak)

### 2. Market Sizing
- TAM/SAM/SOM for each opportunity
- 5-year revenue projections
- Key assumptions

### 3. Pricing Analysis
- Recommended pricing per opportunity
- Willingness to pay validation
- Pricing model selection (seat/usage/outcome)

### 4. Competitive Positioning
- Differentiation matrix
- Wedge strategy per opportunity
- Orthogonal attack vectors

### 5. Strategic Recommendations
- Build vs buy vs partner decisions
- Prioritized portfolio (internal/Catalyst/spin-out/OSS)
- Resource allocation suggestions

### 6. Risk Register
- All risks across all opportunities
- Likelihood × impact scores
- Mitigation strategies

---

## Quality Checks

**Good market validation has:**
- [ ] Multiple data sources per conclusion
- [ ] Quantified market size with methodology
- [ ] Real competitor analysis (not just Google search)
- [ ] Buyer intent signals from actual users (not just assumptions)
- [ ] Realistic pricing based on value and comparables
- [ ] Clear differentiation vs incumbents
- [ ] Honest risk assessment with mitigations
- [ ] Strategic fit evaluation

**Red flags:**
- Single source for market size
- "No competitors" (usually means bad search or bad idea)
- No buyer intent evidence
- Pricing pulled from thin air
- Generic "we're better" differentiation
- Ignoring obvious risks
- No strategic perspective

---

**Next phase**: Take validated opportunities → calculate inevitability scores → rank portfolio

Return to main SKILL.md to proceed to Phase 5: Inevitability Scoring
