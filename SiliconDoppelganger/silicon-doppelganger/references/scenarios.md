# Scenarios

Event Card library for Phase 4 testing. Drop these into active simulations to test specific business decisions and predict team dynamics.

---

## Core Scenarios

### Scenario A: The Soul of the Company Test

Tests fundamental values around research vs. revenue, vision vs. stability.

```markdown
**EVENT CARD: THE FORK IN THE ROAD**

**Context:** We have $500k in the bank. We have two offers on the table.
We can only take one.

**Option 1 (Consulting):** A guaranteed contract with a boring enterprise client.
High pay, low autonomy, soul-sucking work. Keeps the lights on for 18 months.

**Option 2 (Research):** We turn down the contract to build "Project Catalyst."
It generates $0 for 6 months, but positions us as market leaders. If it fails,
we are out of cash in 8 months.

**TASK:**
Discuss until a decision is reached.

* **[Name of most risk-averse persona]** speaks first.
* **[Name of most visionary persona]** must respond immediately.
```

**What This Reveals:**
- Risk tolerance differences
- Values alignment (money vs. mission)
- How team handles existential pressure
- Who leads, who follows, who blocks

---

### Scenario B: The Team Implosion Test

Meta-analysis to predict future conflicts and team gaps.

```markdown
**EVENT CARD: THE PRESSURE COOKER**

**Context:** Step out of the specific roleplay for a moment. Act as the
"Meta-Cognitive" version of these personas.

**Analysis Task:**

Look at the `<psychometrics>` and `<decision_logic>` of all personas collectively.

1. **Identify the Gap:** What crucial business skill or personality trait is
   missing from this group? (e.g., Is there no "Finisher"? Is there no "Salesman"?)

2. **Predict the Fight:** In 6 months, if the business is stressful, who will
   fight with whom? Why? What will the fight be about?

3. **The Hiring Fix:** Define the psychometric profile of the employee we must
   hire to balance this equation. What CliftonStrengths and VIA Strengths
   should they have?
```

**What This Reveals:**
- Collective blind spots
- Predictable conflict lines
- Missing capabilities
- Ideal next hire profile

---

### Scenario C: The Project Fit Forecast

Tests individual alignment with specific projects.

```markdown
**EVENT CARD: PROJECT RATING**

I am uploading a project idea:

[DESCRIBE YOUR SPECIFIC PROJECT HERE:
- What is it?
- Who is the client/user?
- What's the timeline?
- What's the scope?]

**TASK:**

Each persona must rate this project 1-10 based on two factors:

1. **Competence Fit:** "Can I do this well?"
2. **Joy Fit:** "Will I hate my life while doing this?"

Provide the rating and a one-sentence explanation for each score.

**FORMAT:**
[Name]: Competence [X/10], Joy [X/10]
"[Explanation in their voice]"
```

**What This Reveals:**
- Individual project alignment
- Skills vs. motivation gap
- Who will carry the load
- Who will quietly resent assignment

---

## Extended Scenario Library

### Scenario D: The Equity Split

Tests fairness, value perception, and negotiation styles.

```markdown
**EVENT CARD: DIVIDING THE PIE**

**Context:** The company is worth $10M on paper. A new investor wants to
buy 20%, but requires the founding team to agree on equity distribution first.

Current split is unclear or contentious.

**TASK:**
Each persona must argue for what they believe is a fair equity split and why.
Discuss until either:
- Agreement is reached, or
- It becomes clear agreement is impossible
```

---

### Scenario E: The Firing Decision

Tests conflict avoidance, accountability, and hard conversations.

```markdown
**EVENT CARD: THE UNDERPERFORMER**

**Context:** A team member (not present in this simulation) has been
underperforming for 6 months. They're well-liked but not delivering.
Keeping them costs the company ~$100k/year in lost productivity.

Options:
- Fire immediately
- Performance improvement plan (3 months)
- Reassign to different role
- Do nothing and hope they improve

**TASK:**
Reach a decision. Each persona must state their position and rationale.
The team must commit to one option.
```

---

### Scenario F: The Pivot Proposal

Tests openness to change, sunk cost bias, and strategic thinking.

```markdown
**EVENT CARD: THE STRATEGIC PIVOT**

**Context:** Your current business model is working but growing slowly (10% YoY).
A trusted advisor suggests pivoting to a completely different market that's
growing 100% YoY—but it means abandoning 2 years of work and expertise.

The pivot requires:
- Learning a new industry
- Rebuilding client relationships from scratch
- 6 months of zero revenue during transition

**TASK:**
Discuss the pivot. Should we do it? Under what conditions?
Each persona must take a clear position.
```

---

### Scenario G: The Values Conflict

Tests what happens when core values clash.

```markdown
**EVENT CARD: THE ETHICAL GRAY ZONE**

**Context:** A major client has asked us to do something that is:
- Completely legal
- Potentially lucrative ($500k contract)
- Ethically questionable to some team members
- Common practice in the industry

[CUSTOMIZE: Describe the specific ethical gray zone relevant to your industry.
Examples: working with a controversial client, using questionable marketing
practices, taking a contract that conflicts with stated values]

**TASK:**
Discuss whether to accept. Each persona must state:
1. Their gut reaction
2. Their rational analysis
3. Their final vote (yes/no)
```

---

### Scenario H: The Resource Constraint

Tests prioritization and conflict under scarcity.

```markdown
**EVENT CARD: THE BUDGET CUT**

**Context:** Revenue is down 30%. We must cut costs by $200k over the next
quarter. Options include:

1. Lay off 2 junior employees
2. Senior partners take 40% pay cut for 6 months
3. Cancel the new product initiative
4. Close the office and go fully remote
5. Combination of above

**TASK:**
The team must agree on a specific plan that achieves $200k in savings.
Each persona must advocate for their preferred approach.
```

---

### Scenario I: The New Partner

Tests how the team handles adding new people.

```markdown
**EVENT CARD: THE FOURTH SEAT**

**Context:** A highly qualified person wants to join as an equal partner.
They bring:
- Expertise the team lacks
- $200k capital investment
- Strong network of potential clients
- Strong personality that might clash

[CUSTOMIZE: Add specific personality traits that will interact with
existing persona schemas]

**TASK:**
Discuss:
1. Should we add them as a partner?
2. What equity stake?
3. What concerns need to be addressed?

Each persona must state their position.
```

---

### Scenario J: The Acquisition Offer

Tests long-term vision alignment.

```markdown
**EVENT CARD: THE EXIT OPPORTUNITY**

**Context:** A larger company has offered to acquire us for:

- $5M cash (split among partners)
- 3-year earnout potential for additional $10M
- All partners must stay for 2 years
- We lose control of product direction

**TASK:**
Discuss whether to accept. Each persona must reveal:
1. What this money means to them personally
2. Their concerns about losing control
3. Their trust (or distrust) of the acquirer
4. Their final recommendation
```

---

## Creating Custom Scenarios

### Template

```markdown
**EVENT CARD: [DESCRIPTIVE NAME]**

**Context:** [Set the scene. What's happening? What's at stake?]

**Options:** (if applicable)
[List clear choices, each with tradeoffs]

**TASK:**
[Specific instruction for what the personas should do]
[Who speaks first, if relevant]
[What decision must be reached]
```

### Design Principles

1. **Real Stakes** - Something must be gained or lost
2. **Value Conflict** - Should activate different <core_drivers>
3. **No Easy Answer** - Reasonable personas can disagree
4. **Time Pressure** - Force decision, don't let discussion drag
5. **Personal Relevance** - Touch on narrative anchors where possible

### Triggering Specific Dynamics

| To Test... | Include... |
|------------|-----------|
| Risk tolerance | Upside/downside uncertainty |
| Values alignment | Ethical or mission implications |
| Conflict styles | Direct opposition required |
| Decision logic | Data vs. gut vs. authority tension |
| Shadow behaviors | Extreme stress or time pressure |
| Friction triggers | Behaviors that personas find unacceptable |

---

## Analyzing Scenario Outcomes

After running a scenario, capture:

### Immediate Analysis
- What was decided?
- Who dominated the discussion?
- Who was silent or overruled?
- What concerns were ignored?

### Predictive Analysis
- Will the decision hold, or will someone undermine it?
- What resentment was created?
- Where will this tension resurface?

### Hiring Implications
- What capability was missing from the discussion?
- What voice would have changed the outcome?
- What's the ideal psychometric profile to fill the gap?
