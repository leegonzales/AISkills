# Scoring Rubric — Feasibility × Impact

Used internally during Stage 2 (Map What Exists) to rank the 5–7 candidate opportunities. Surface the ranked scoring to the user only if they ask to see it, or if they're torn between two moves in Stage 3.

Score each candidate on two dimensions. 1 = low, 5 = high.

---

## Feasibility (1–5)

**How easy is it for this user, in their current context, to stand this up in the next 4 weeks?**

Consider:

- **Tooling access.** Do they already have the tools (Claude, Glean, etc.) they'd need? (No = –1, yes = neutral)
- **Data access.** Is the input data already in a place they can hand to AI? Or does it need to be extracted, cleaned, or licensed?
- **Decision authority.** Can they deploy this without buy-in from others? Or does it require a sign-off chain?
- **Technical complexity.** Is this a prompt-and-iterate effort, or does it require integrations, code, or infrastructure?
- **Behavioral change required.** Is this a solo tool or does it require others to change workflow?

**Scoring guide:**
- **5 — Trivial.** Can be built this week with just Claude, no integration, no buy-in.
- **4 — Easy.** Builds in 1–2 weeks with tools the user already has.
- **3 — Moderate.** Requires some integration, light data prep, or one external dependency.
- **2 — Hard.** Requires multiple dependencies, buy-in from others, or novel tooling.
- **1 — Very hard.** Real engineering, procurement, or organizational change required.

---

## Impact (1–5)

**If this works, how much does it matter?**

Consider:

- **Magnitude.** Hours saved per week, decisions improved, outcomes unlocked.
- **Frequency.** Does this fire daily, weekly, quarterly, or once?
- **Compounding.** Does every use make the next use better (feedback loops, accumulating context), or is each instance isolated?
- **Strategic weight.** Does this matter to the user's role, their team, their org? Or is it convenience?
- **Leverage type.** Which transformation pattern?
  - Impossible-to-Possible → typically higher impact when it works
  - Days-to-Hours → high impact if frequency ≥ quarterly
  - Hours-to-Minutes → high cumulative impact if frequency ≥ weekly
  - Invisible-to-Visible → high impact if the surfaced insight changes decisions

**Scoring guide:**
- **5 — Transformative.** Changes what the user or team is capable of. Others will notice.
- **4 — Significant.** Meaningful reclaimed time or materially better output on important work.
- **3 — Real.** Useful improvement the user will feel.
- **2 — Modest.** Quality-of-life win. Nice but not load-bearing.
- **1 — Marginal.** Worth noting but won't move the needle.

---

## Composite score

Two useful ways to use the scores:

### 1. Ranked shortlist (pick 2–3 top movers)

Sum feasibility + impact. Rank. Surface the top 2–3 with their scores and brief rationale. Example:

| Move | Pattern | Feasibility | Impact | Total | Why |
|------|---------|-------------|--------|-------|-----|
| Draft monthly board update from historical data | Days-to-Hours | 4 | 5 | 9 | High frequency, known output shape, user controls the process |
| Extract patterns from 50 post-project surveys | Invisible-to-Visible | 3 | 5 | 8 | Data is accessible; output format needs design |
| Build decision matrix for vendor evaluation | Hours-to-Minutes | 5 | 3 | 8 | Easy to ship; modest per-use savings but frequent |

### 2. Quadrant view (when visualizing for the user)

```
          HIGH IMPACT
               |
   STRATEGIC   |   QUICK WIN
   (worth the  |   (ship this
    investment)|    first)
               |
---------------+---------------
               |
   AVOID       |   EFFICIENCY
   (low ROI)   |   (nice to have)
               |
          LOW IMPACT
```

- **Quick Win (high feasibility, high impact):** Ship this first. These are what Week 1 should attack.
- **Strategic (low feasibility, high impact):** Worth investing in, but not this cycle. Flag for future.
- **Efficiency (high feasibility, low impact):** Fine if easy, but don't overweight them. A pile of small wins can substitute for real leverage.
- **Avoid (low feasibility, low impact):** Not this session.

---

## When to share the scoring with the user

- **Share** if they ask "which of these should I prioritize?" — scoring makes the tradeoff legible.
- **Share** if they're torn between two candidates in Stage 3 — show the scores and the tiebreaker.
- **Don't share** by default. Leading with a scoring table can feel like you're math-washing intuition. The human pick in Stage 3 ("which one makes you lean forward?") is often the right answer; scoring is a backup tool.

## Honesty about scoring

The scores are directional, not precise. Don't pretend 4.2 beats 4.0. Use them to separate clear winners from also-rans, not to resolve close calls. Close calls should go to the user's gut.
