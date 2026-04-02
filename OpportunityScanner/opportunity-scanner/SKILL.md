---
name: opportunity-scanner
description: Deep-scan Slack, email, calendar, Jira, Confluence, and other connected tools to discover high-ROI Claude skills, projects, and artifacts to build — for both personal productivity and department leadership. Use when someone says "scan for opportunities", "what should I build", "find automation opportunities", or "what's worth automating".
---

# Opportunity Scanner

Deep-dive your connected work tools to find the highest-value Claude skills, projects, and artifacts you should build — for yourself and for your team.

**This isn't a survey. It scans your actual work patterns, finds the waste, and tells you exactly what to build and why.**

---

## When to Use

Invoke when user:
- Wants to know what Claude skills or projects would save them the most time
- Says "what should I build?" or "scan for opportunities"
- Is a leader looking for AI wins across their department
- Wants ROI-backed recommendations, not guesses
- Has MCPs connected and wants to put them to work strategically

---

## Pre-Flight Check

Before scanning, detect what tools are connected. Probe each MCP silently — don't ask the user to list them.

**Check for availability of:**
- Google Calendar (list events)
- Gmail (search messages)
- Slack (search/read channels)
- Jira (search issues)
- Confluence (search pages)
- Google Docs/Sheets (search/list)

Report what's connected:

> **Connected tools detected:**
> - ✅ Google Calendar
> - ✅ Gmail
> - ✅ Slack
> - ❌ Jira (not connected)
> - ❌ Confluence (not connected)
>
> **I'll scan everything that's connected. The more tools available, the better the recommendations. Ready to start?**

If fewer than 2 tools are connected, warn that recommendations will be limited but proceed anyway.

---

## Core Workflow

### Phase 1: Deep Scan (3-5 minutes)

Scan all connected sources in parallel. Pull data from the last 30 days unless the user specifies otherwise.

#### Calendar Scan
**Pull**: All events from the last 30 days
**Analyze for**:
- **Meeting load**: Total hours/week in meetings. Trend over 4 weeks.
- **Recurring meetings**: Which ones repeat? How many attendees? Duration?
- **1:1 density**: How many 1:1s per week? With whom?
- **Meeting types**: Classify as status update, decision-making, brainstorm, 1:1, all-hands, external
- **Prep patterns**: Are there prep blocks before meetings? Gaps that suggest context-switching?
- **Meeting-free time**: How many focused hours per week?

**Opportunity signals**:
- Status meetings > 3/week → could be async briefings
- Recurring meetings with 5+ people → could have AI-generated pre-reads
- 1:1s with direct reports → prep could be automated
- Back-to-back blocks with no prep time → meeting prep skill needed

#### Email Scan
**Pull**: Last 200 emails (sent + received), search for high-frequency patterns
**Analyze for**:
- **Volume**: Emails sent/received per day
- **Response patterns**: Average response time. Who do they respond to fastest/slowest?
- **Repetitive content**: Similar emails sent to different people (templates hiding in plain sight)
- **Request patterns**: What do people ask them for repeatedly?
- **FYI vs action**: Ratio of informational emails to ones requiring action
- **Thread length**: Long threads suggest decisions that could be structured differently

**Opportunity signals**:
- Same type of email sent 3+ times/month → template or auto-draft skill
- Long response times to certain senders → triage/prioritization needed
- High FYI volume → digest/summary skill
- Repeated requests for the same info → knowledge base or self-serve artifact

#### Slack Scan
**Pull**: Channels they're active in, messages from last 30 days, DMs (last 14 days)
**Analyze for**:
- **Channel load**: How many channels? Active in how many?
- **Message volume**: Messages sent/received per day
- **Question patterns**: What do people ask them in DMs? In channels?
- **Repeated questions**: Same question from different people → documentation gap
- **Status update patterns**: Are they manually posting updates that could be automated?
- **Information routing**: Are they the bridge between teams? Forwarding/translating between groups?
- **@mention response time**: How fast do they respond to direct mentions?
- **Thread patterns**: Do they start threads or respond? Long threads suggest complex decisions.

**Opportunity signals**:
- Same question asked 3+ times → FAQ artifact, knowledge skill, or Confluence page
- Manual status updates → automated status report project
- High DM volume with repeated patterns → team communication skill
- Bridge between 2+ teams → cross-functional digest or routing automation
- Slow @mention response → triage/notification skill needed

#### Jira Scan (if connected)
**Pull**: Issues assigned to them, issues they've created, recent activity
**Analyze for**:
- **Ticket patterns**: What types of tickets do they create/handle most?
- **Status transitions**: How long do tickets sit in each state?
- **Comment patterns**: Repetitive comments or status updates?
- **Sprint patterns**: Consistent velocity? Spillover?
- **Blocker frequency**: What blocks work most often?

**Opportunity signals**:
- Repetitive ticket creation → ticket template or auto-creation skill
- Long time in "waiting" states → escalation or follow-up automation
- Manual status comments → automated status updates
- Recurring blocker patterns → proactive blocker detection

#### Confluence Scan (if connected)
**Pull**: Pages they've authored/edited recently, search for team documentation
**Analyze for**:
- **Documentation freshness**: When were key docs last updated?
- **Page creation patterns**: What kind of docs do they create?
- **Gap analysis**: Topics discussed in Slack/email that have no Confluence page

**Opportunity signals**:
- Stale documentation → doc refresh project
- Topics discussed repeatedly without docs → documentation generation skill
- Frequently referenced pages → could become interactive artifacts

#### Google Docs/Sheets Scan (if connected)
**Pull**: Recently accessed/created documents
**Analyze for**:
- **Document types**: Reports, plans, templates, meeting notes?
- **Creation frequency**: How often do they create similar docs?
- **Collaboration patterns**: Shared with whom? Commented on by whom?

**Opportunity signals**:
- Similar documents created repeatedly → template or generation skill
- Manual data compilation in sheets → automated dashboard artifact
- Meeting notes for every recurring meeting → auto-notes skill

---

### Phase 2: Pattern Analysis (1-2 minutes)

After scanning, synthesize findings across all sources. Look for cross-source patterns:

#### Cross-Source Pattern Detection

| Pattern | Sources | Signal |
|---------|---------|--------|
| **Information broker** | Slack DMs + Email forwards | Person is manually routing information between people/teams |
| **Repetitive reporter** | Calendar meetings + Slack updates + Email summaries | Same information reformatted for different audiences |
| **Question magnet** | Slack DMs + Email requests | People come to them for answers that should be self-serve |
| **Meeting machine** | Calendar + Slack follow-ups + Email recaps | Life revolves around meetings and their aftermath |
| **Context switcher** | Calendar gaps + Slack response times + Email delays | Fragmented attention across too many streams |
| **Template seeker** | Similar emails + similar docs + similar Slack messages | Doing the same thing repeatedly with slight variations |
| **Status updater** | Slack posts + Email updates + Jira comments | Manually broadcasting status across channels |
| **Decision bottleneck** | Long Slack threads + email chains + Jira blockers | Things stall waiting on them |

#### ROI Scoring

For each identified opportunity, calculate:

```
Weekly Time Saved = frequency_per_week × time_per_instance × automation_percentage
Annual ROI Hours = Weekly Time Saved × 48 weeks
Impact Score = (Annual ROI Hours × people_affected) / implementation_effort
```

**Frequency**: How often does this pattern occur? (from scan data)
**Time per instance**: Estimated minutes per occurrence
**Automation percentage**: How much can Claude realistically handle? (be honest — 40-80%, not 100%)
**People affected**: Just them, or their whole team?
**Implementation effort**: Low (1 hour), Medium (half day), High (full day)

---

### Phase 3: Recommendation Generation

Generate recommendations in two categories. Each recommendation must include:
- **What to build** (skill, project, or artifact — be specific)
- **Why** (the pattern that triggered this recommendation, with data)
- **ROI estimate** (hours saved per week, who benefits, implementation effort)
- **How** (2-3 sentence description of what the build looks like)

#### Category 1: For You (Personal Productivity)

Recommendations that help THIS person work faster, stay on top of things, reduce cognitive load.

**Prioritize by**:
1. Highest weekly time savings
2. Lowest implementation effort
3. Daily pain points over weekly ones

**Types to recommend**:

| Type | When to Recommend | Example |
|------|-------------------|---------|
| **Claude Project** | Ongoing workflow needs a persistent context | "Meeting Prep Center" — a project that knows your recurring meetings and auto-generates prep docs |
| **Skill** | Repeatable task with consistent structure | "Status Digest" — scans Slack + Jira and generates a formatted team update |
| **Artifact** | One-time or periodic output | Dashboard showing team velocity trends compiled from Jira data |

#### Category 2: For Your Team (Department Leadership)

Recommendations that help their TEAM or DEPARTMENT. These are force-multiplier plays.

**Prioritize by**:
1. Number of people who benefit
2. Eliminates repeated friction (same question, same manual process)
3. Reduces dependency on any single person (especially them)

**Types to recommend**:

| Type | When to Recommend | Example |
|------|-------------------|---------|
| **Team Project** | Shared workflow the whole team needs | "Engineering Standup Bot" — project that generates async standup reports from Jira + Slack |
| **Department Skill** | Repeatable process many people do | "RFP Drafter" — skill that generates proposal drafts from templates + past RFPs |
| **Team Artifact** | Shared resource or dashboard | "New Hire Onboarding Guide" — generated from Confluence + Slack FAQ patterns |
| **Knowledge Base** | Information scattered across sources | "Team FAQ" — auto-generated from repeated Slack questions with source links |

---

### Phase 4: Deliver Report

Present findings in a structured, scannable format.

```markdown
# Opportunity Scan Report — [Name], [Role]
**Scan date**: [Date]
**Sources scanned**: [List connected tools]
**Time window**: Last 30 days

---

## Key Findings

**Your work profile**:
- [X] hours/week in meetings ([trend] from last month)
- [X] emails/day ([X] requiring action, [X] FYI)
- [X] Slack channels active, [X] DMs/day
- [X] Jira tickets touched/week

**Top patterns detected**:
1. [Pattern name] — [one-line description with data]
2. [Pattern name] — [one-line description with data]
3. [Pattern name] — [one-line description with data]

---

## For You: Top [N] Recommendations

### 1. [Build Name] — [Skill/Project/Artifact]
**ROI**: ~[X] hours saved/week | Effort: [Low/Med/High]
**Pattern**: [What we found in the data]
**Build**: [2-3 sentences on what this looks like]

### 2. ...

---

## For Your Team: Top [N] Recommendations

### 1. [Build Name] — [Skill/Project/Artifact]
**ROI**: ~[X] hours saved/week across [N] people | Effort: [Low/Med/High]
**Pattern**: [What we found in the data]
**Build**: [2-3 sentences on what this looks like]

### 2. ...

---

## Quick Wins (< 1 hour to build)
- [ ] [Quick win 1] — [one line]
- [ ] [Quick win 2] — [one line]
- [ ] [Quick win 3] — [one line]

---

## Implementation Roadmap

| Priority | Build | Type | Effort | ROI/week | Start |
|----------|-------|------|--------|----------|-------|
| 1 | [Name] | Skill | Low | 3h | Now |
| 2 | [Name] | Project | Med | 5h | This week |
| 3 | [Name] | Artifact | Low | 2h | Now |
| ... | ... | ... | ... | ... | ... |
```

---

### Phase 5: Interactive Deep-Dive

After delivering the report:

> **That's the scan. Want to:**
> 1. **Deep-dive** a specific recommendation (I'll spec it out in detail)
> 2. **Build one now** (I'll generate the skill, project instructions, or artifact)
> 3. **Rescan** with a different time window or focus area
> 4. **Export** the full report as a document

If they choose to build, generate the complete output:
- **Skill**: Full SKILL.md with references
- **Project**: Complete custom instructions ready to paste
- **Artifact**: The actual artifact (dashboard, template, FAQ, etc.)

---

## Presentation Rules

- **Lead with data, not opinions.** Every recommendation cites scan evidence.
- **Be honest about ROI.** Don't inflate numbers. 2 hours/week saved is meaningful — don't round up to 5.
- **Separate personal from team.** Leaders think in both frames. Don't mix them.
- **Quick wins first.** Low-effort, high-frequency wins build momentum.
- **No jargon about AI.** Don't say "leverage AI to optimize workflows." Say "this scans your Jira every morning and posts a status update so you don't have to."
- **Specific > generic.** "Build a meeting prep skill for your weekly product review" beats "Consider automating meeting preparation."

---

## Anti-Patterns

- **Don't recommend things the user clearly doesn't need.** If they have 3 meetings a week, don't recommend a meeting prep skill.
- **Don't assume all tools are connected.** Only recommend based on what's actually available.
- **Don't recommend building what already exists in the environment.** Check if the skill/project already exists before recommending.
- **Don't overload the report.** Max 5 personal + 5 team recommendations. Quality over quantity.
- **Don't hand-wave implementation.** Every recommendation should be buildable. If it's not, don't recommend it.
- **Don't scan private/sensitive content beyond what's needed.** Summarize patterns, don't quote private messages in the report.

---

## Privacy & Sensitivity

- **Never quote private DMs or emails verbatim in the report.** Summarize patterns only.
- **Don't name individuals in negative contexts.** "Your team asks the same onboarding question frequently" not "Sarah asked the same question 4 times."
- **Aggregate, don't expose.** Team recommendations should reference patterns, not individuals.
- **Skip HR/legal/compensation signals.** If the scan surfaces sensitive topics, ignore them — they're not automation candidates.

---

## References

For detailed protocols:
- `references/scan-protocols.md` — MCP query patterns for each data source
- `references/pattern-catalog.md` — Full catalog of cross-source patterns and their signals
- `references/roi-framework.md` — Detailed ROI calculation methodology
- `references/recommendation-templates.md` — Example recommendations by role and industry
