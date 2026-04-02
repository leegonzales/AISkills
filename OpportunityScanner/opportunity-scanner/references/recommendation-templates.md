# Recommendation Templates

Example recommendations by role type. Use these as starting points — always customize with actual scan data.

---

## Engineering Leader

### Personal
1. **Sprint Pulse Project** — Scans Jira + Slack daily, surfaces blockers, velocity trends, and team sentiment. Morning check-in replaces 30 min of manual Jira browsing.
   - ROI: ~2.5 hours/week | Effort: Medium

2. **1:1 Prep Skill** — Before each 1:1, pulls the report's recent PRs, Jira activity, Slack contributions, and any pending items. Generates talking points and follow-ups from last time.
   - ROI: ~2 hours/week | Effort: Medium

3. **Incident Post-Mortem Drafter** — After incidents, scans Slack incident channel, Jira tickets, and calendar (who was in the war room) to generate a structured post-mortem draft.
   - ROI: ~1 hour/incident | Effort: Low

### Department
1. **Engineering Weekly Digest** — Auto-generated from Jira (PRs merged, tickets closed, sprint progress) + Slack (announcements, decisions made). Replaces or supplements the weekly all-hands.
   - ROI: 1 hour/week × team size | Effort: Medium

2. **On-Call Handoff Artifact** — Generates a handoff doc from the last week's incidents, open alerts, and known issues. Pulls from Jira + Slack incident channels.
   - ROI: 30 min/handoff × 2/week | Effort: Low

3. **New Engineer Onboarding Project** — Claude project pre-loaded with team FAQs, architecture docs, and common setup issues extracted from Slack history.
   - ROI: 5+ hours per new hire | Effort: High

---

## Sales Leader

### Personal
1. **Deal Prep Project** — Before customer calls, pulls all prior email threads, Slack mentions of the account, and CRM notes. Generates a brief with key context and suggested talking points.
   - ROI: ~3 hours/week | Effort: Medium

2. **Pipeline Review Skill** — Scans email + calendar to identify deals that haven't had contact in 7+ days, upcoming renewals, and meetings with no follow-up action.
   - ROI: ~2 hours/week | Effort: Medium

3. **Win/Loss Analyzer** — After a deal closes (won or lost), compiles the full communication history and generates insights on what worked or didn't.
   - ROI: ~1 hour/deal | Effort: Low

### Department
1. **Sales Playbook Artifact** — Generated from top performers' email patterns, Slack coaching threads, and successful deal histories. Living document that updates quarterly.
   - ROI: Variable but high for new reps | Effort: High

2. **Competitive Intel Digest** — Scans Slack for mentions of competitors, email threads about competitive deals, and generates a weekly brief.
   - ROI: 1 hour/week × sales team | Effort: Medium

---

## Operations / Chief of Staff

### Personal
1. **Executive Briefing Project** — Daily scan of email, Slack, and calendar. Generates a prioritized briefing with items requiring attention, decisions needed, and FYI items.
   - ROI: ~3-5 hours/week | Effort: Medium

2. **Board Prep Skill** — Compiles data from across tools into board deck structure. Flags missing data, stale metrics, and items needing exec input.
   - ROI: ~5 hours/quarter | Effort: High

3. **Cross-Functional Tracker** — Monitors Slack channels across departments, flags items that cross team boundaries, identifies misalignment early.
   - ROI: ~2 hours/week | Effort: Medium

### Department
1. **Company Pulse Artifact** — Weekly snapshot pulling metrics, sentiment (from Slack), key decisions made, and blockers. Auto-generated, posted to leadership channel.
   - ROI: 2 hours/week (creation) + faster alignment | Effort: Medium

2. **OKR Progress Tracker** — Scans Jira, project channels, and docs to auto-update OKR progress. Flags items at risk.
   - ROI: 1 hour/week × leadership team | Effort: High

---

## People / HR Leader

### Personal
1. **Employee Pulse Project** — Scans team channels for sentiment signals, tracks engagement patterns, flags unusual drops in activity or tone shifts.
   - ROI: ~2 hours/week | Effort: Medium

2. **Offer Letter / Comms Drafter** — Skill that generates standard HR communications from templates + context. Offer letters, policy updates, benefit explanations.
   - ROI: ~2 hours/week | Effort: Low

### Department
1. **Policy FAQ Project** — Claude project pre-loaded with HR policies, benefits info, and common questions extracted from Slack #hr-questions history.
   - ROI: 3+ hours/week (answering repeated questions) | Effort: Medium

2. **Onboarding Checklist Generator** — Creates personalized onboarding plans based on role, team, and location. Pulls from Confluence templates + Slack welcome channel patterns.
   - ROI: 2 hours per new hire | Effort: Low

---

## Product Leader

### Personal
1. **Feature Request Tracker** — Scans Slack, email, and Jira for feature requests, clusters them by theme, and generates a prioritized backlog suggestion.
   - ROI: ~3 hours/week | Effort: Medium

2. **Competitive Landscape Skill** — Monitors Slack for competitor mentions, customer feedback channels, and generates a weekly competitive brief.
   - ROI: ~2 hours/week | Effort: Medium

### Department
1. **Product Update Digest** — Auto-generated from Jira releases, Slack announcements, and docs. Distributed to stakeholders weekly.
   - ROI: 1 hour/week × team + stakeholder alignment | Effort: Medium

2. **User Feedback Synthesizer** — Scans all channels where customer feedback lands, clusters by theme, quantifies frequency, and generates insights.
   - ROI: 3+ hours/week | Effort: High

---

## Formatting Each Recommendation

Always follow this structure:

```markdown
### [N]. [Build Name] — [Skill/Project/Artifact]
**ROI**: ~[X] hours saved/week [for who] | Effort: [Low/Med/High]
**Pattern**: [1-2 sentences describing what the scan found — with numbers]
**Build**: [2-3 sentences describing what gets built and how it works]
**Quick test**: [One thing they can try right now to validate the need]
```

The "Quick test" line is important — it gives them an immediate action that proves the pattern exists, before committing to a build.
