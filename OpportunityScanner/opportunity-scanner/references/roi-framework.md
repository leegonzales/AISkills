# ROI Framework

How to calculate and present return on investment for recommended builds.

---

## Core Formula

```
Weekly Time Saved = frequency × time_per_instance × automation_rate
Annual ROI (hours) = Weekly Time Saved × 48 weeks
Annual ROI ($) = Annual ROI (hours) × blended_hourly_rate
Impact Score = (Annual ROI hours × people_affected) / effort_hours
```

---

## Input Variables

### Frequency (from scan data)
| Cadence | Weekly Frequency |
|---------|-----------------|
| Multiple times daily | 15-25 |
| Daily | 5 |
| Every other day | 2.5 |
| Weekly | 1 |
| Biweekly | 0.5 |
| Monthly | 0.25 |

### Time per Instance (estimated by task type)
| Task | Minutes |
|------|---------|
| Writing a status update | 15-30 |
| Answering a repeated question | 5-15 |
| Prepping for a meeting | 15-45 |
| Writing a follow-up email | 10-20 |
| Searching for information across tools | 10-30 |
| Creating a report from data | 30-60 |
| Routing information between teams | 5-15 |
| Updating a Jira ticket with status | 5-10 |
| Creating a document from template | 20-45 |
| Reading and triaging email | 15-30 |

### Automation Rate (be conservative)
| Complexity | Rate | Examples |
|------------|------|----------|
| Highly structured, data-available | 80% | Status reports from Jira, calendar digests |
| Semi-structured, needs judgment | 60% | Email drafts, meeting prep, triage |
| Creative/strategic | 40% | Planning docs, strategy decks, complex responses |
| Requires human decision | 20% | Approvals, hiring decisions, conflict resolution |

### Effort to Build
| Level | Hours | Examples |
|-------|-------|---------|
| Low | 0.5-1 | Simple artifact, template, FAQ doc |
| Medium | 2-4 | Project with custom instructions, skill with references |
| High | 4-8 | Complex skill with multiple workflows, multi-source integration |

---

## Presentation Rules

1. **Always show weekly hours**, not annual. People think in weeks.
2. **Round to nearest 0.5 hour**. Don't say "2.7 hours/week" — say "~2.5 hours/week."
3. **Don't convert to dollars** unless the user asks. Hours are more tangible for most people.
4. **Show the math briefly**: "You post status updates 3x/week, ~20 min each = ~1 hour/week"
5. **Team multipliers**: "If 8 people on your team each save 1 hour/week, that's 8 hours/week recovered for the department."
6. **Be honest about effort**: "This takes about 2 hours to set up" is more useful than "Low effort."

---

## ROI Tiers

Use these to categorize recommendations in the report:

| Tier | Weekly Savings | Label |
|------|---------------|-------|
| **High ROI** | 5+ hours/week (or 2+ hours × 5+ people) | "High-impact opportunity" |
| **Medium ROI** | 2-5 hours/week (or 1-2 hours × 3+ people) | "Solid win" |
| **Low ROI** | 0.5-2 hours/week | "Quick win" (only if effort is also low) |
| **Not worth it** | < 0.5 hours/week | Don't recommend |

---

## Impact Score

For ranking recommendations against each other:

```
Impact Score = (annual_hours_saved × people_affected) / effort_hours
```

| Score | Meaning |
|-------|---------|
| > 100 | No-brainer. Build this immediately. |
| 50-100 | Strong recommendation. Build this week. |
| 20-50 | Good opportunity. Schedule it. |
| 10-20 | Worthwhile if time permits. |
| < 10 | Probably not worth the setup cost. Skip. |

---

## Example Calculations

### Status Update Automation
- Frequency: 3x/week
- Time: 20 minutes each
- Automation rate: 80% (structured, data from Jira)
- Weekly savings: 3 × 20 × 0.8 = 48 min ≈ **1 hour/week**
- People affected: 1 (author) + 8 (readers get it faster) = marginal multiplier
- Effort: 2 hours (Medium)
- Impact Score: (48 × 1) / 2 = 24 → **Good opportunity**

### Team FAQ from Repeated Questions
- Frequency: 5 questions/week directed at one person
- Time: 10 minutes per answer
- Automation rate: 70% (most questions have standard answers)
- Weekly savings: 5 × 10 × 0.7 = 35 min ≈ **0.5 hours/week** (for the answerer)
- People affected: 15 (anyone who asks questions) — they get instant answers instead of waiting
- Effort: 1 hour (Low)
- Impact Score: (24 × 15) / 1 = 360 → **No-brainer**

### Meeting Prep Automation
- Frequency: 5 meetings/week needing prep
- Time: 30 minutes each
- Automation rate: 60% (context-gathering automated, judgment still needed)
- Weekly savings: 5 × 30 × 0.6 = 90 min ≈ **1.5 hours/week**
- People affected: 1
- Effort: 3 hours (Medium)
- Impact Score: (72 × 1) / 3 = 24 → **Good opportunity**
