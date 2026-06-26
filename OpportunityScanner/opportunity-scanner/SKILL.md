---
name: opportunity-scanner
description: Deep-scan Slack, email, calendar, Jira, Confluence, and other connected tools to discover high-ROI Claude skills, projects, and artifacts to build — for both personal productivity and department leadership. Use when someone says "scan for opportunities", "what should I build", "find automation opportunities", or "what's worth automating".
---

# Opportunity Scanner

Deep-dive your connected work tools to find the highest-value Claude skills, projects, and artifacts you should build — for yourself and for your team.

**This isn't a survey. It scans your actual work patterns, finds the waste, and tells you exactly what to build and why.**

---

## Fidelity Firewall (hard gate — never violate)

**This skill's authority comes from one thing: every number in the report is a real count from a real scan.** The moment you invent a frequency, a time-per-instance, an hours-saved figure, or an ROI to fill a template field, the report becomes fiction wearing the costume of rigor — and a confident fabricated number is *worse* than an honest "I don't have the data," because the user will act on it.

**The hard rule — every quantified claim in the report MUST trace to scanned evidence:**

| Claim type | Allowed ONLY when | Never |
|------------|-------------------|-------|
| Frequency ("12 status emails/week") | You counted them in the scanned data | Inferred from "this kind of role probably…" or from a cadence table |
| Time-per-instance | The user told you, OR a real artifact shows it (e.g. calendar event duration) | Pulled from an "estimated minutes by task type" table to fill a field |
| Hours-saved / ROI | Derived **only** from a real frequency × a real/user-supplied time × a stated automation rate | Reverse-engineered to land in a "High ROI" tier |
| Pattern claim ("you're a decision bottleneck") | A real, countable signal supports it (N threads stalled on you, measured) | Two long threads, a vibe, or one anecdote |

**The scan evidence tables are inputs you MAY use as labels for the math AFTER you have a real count — they are NOT permission to estimate the count itself.** A cadence table tells you that "daily ≈ 5/week"; it does not tell you the user does the thing daily. Only the scan tells you that.

**When data is insufficient to quantify, you have exactly three honest moves, in order:**

1. **Scope down to what you can prove.** Report the pattern you actually observed and stop there. "I see 8 calendar events over 30 days; that's too thin to quantify meeting load — here's the one signal I can stand behind."
2. **Mark the recommendation LOW-confidence and name the gap.** Every recommendation must state the specific scan evidence behind it. If the evidence is thin or absent, say so explicitly: `LOW confidence — based on 8 calendar events only; no email/Slack connected, so frequency is unmeasured.`
3. **Ask for the missing input instead of inventing it.** "How often do you actually send this kind of update?" beats a fabricated "~3x/week."

**Never manufacture a number to look rigorous.** An honest "insufficient data to estimate ROI — connect Gmail/Slack for a real figure" is a *correct* answer, not a failure. Under-claiming on thin data is the safe direction; over-claiming is the failure mode this firewall exists to stop.

**Every recommendation must carry: (a) the specific scan evidence it rests on, and (b) a confidence level (HIGH / MEDIUM / LOW) justified by how much real data backs it.** A recommendation with no citable evidence does not go in the report.

**Final pass — evidence re-check:** before delivering the report, re-read every number and pattern claim and confirm each traces to actual scanned data. Roll back or downgrade any figure you cannot source. This check outranks completeness — a shorter, fully-sourced report beats a complete-looking fabricated one.

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

If fewer than 2 tools are connected, warn explicitly that the scan will be **evidence-thin**: with one source there is not enough cross-signal to quantify most patterns, so the report will scope down to what that single tool can prove and most recommendations will be marked LOW confidence. Do **not** compensate for missing tools by estimating the numbers they would have provided (see Fidelity Firewall). Offer to proceed in scoped-down mode or to connect more tools first.

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

**Frequency**: How often does this pattern occur? — **a real count from the scan**, not an estimate. If you cannot count it, you cannot score it (see Fidelity Firewall); scope the recommendation down to LOW confidence and name the gap instead.
**Time per instance**: Minutes per occurrence — only if the user supplied it or a real artifact shows it (e.g. calendar event duration). If neither, leave ROI unquantified and ask the user, rather than pulling a number from a table.
**Automation percentage**: How much can Claude realistically handle? (be honest — 40-80%, not 100%)
**People affected**: Just them, or their whole team? — based on observed recipients/participants, not assumed team size.
**Implementation effort**: Low (1 hour), Medium (half day), High (full day)

> **Gate:** ROI is computed only when both frequency AND time-per-instance are real (scanned or user-supplied). If either is missing, do not emit an hours-saved number — emit `ROI: unquantified (LOW confidence) — [missing input]` and either ask the user or scope the recommendation to the bare pattern you can prove.

---

### Phase 3: Recommendation Generation

Generate recommendations in two categories. Each recommendation must include:
- **What to build** (skill, project, or artifact — be specific)
- **Why** (the pattern that triggered this recommendation, **with the specific scan evidence and real counts** — "47 status messages across 3 channels in 30 days", not "frequent status updates")
- **ROI estimate** (hours saved per week, who benefits, implementation effort) — **only if frequency and time-per-instance are real** (see Gate above); otherwise `ROI: unquantified (LOW confidence)`
- **Confidence** (HIGH / MEDIUM / LOW) — justified by how much real data backs it. HIGH = counted frequency + known time. LOW = thin/single-source/uncounted; name the gap.
- **How** (2-3 sentence description of what the build looks like)

A recommendation with no citable scan evidence does not go in the report (Fidelity Firewall).

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
**Sources scanned**: [List connected tools] — [N events / N emails / N messages actually pulled]
**Time window**: Last 30 days
**Evidence depth**: [Strong (3+ tools, rich history) / Moderate / Thin — quantification limited, see confidence flags]

> Only report metrics for sources actually scanned. Omit lines for tools that aren't connected — do NOT show a placeholder number for them. Every figure below is a real count from the scan.

---

## Key Findings

**Your work profile** (counted from scanned data):
- [X] hours/week in meetings ([trend] from last month) — [from N calendar events]
- [X] emails/day ([X] requiring action, [X] FYI) — [from N emails]
- [X] Slack channels active, [X] DMs/day — [from N messages]
- [X] Jira tickets touched/week — [from N issues]

**Top patterns detected**:
1. [Pattern name] — [one-line description with data]
2. [Pattern name] — [one-line description with data]
3. [Pattern name] — [one-line description with data]

---

## For You: Top [N] Recommendations

### 1. [Build Name] — [Skill/Project/Artifact]
**ROI**: ~[X] hours saved/week (or `unquantified — LOW confidence, [gap]`) | Effort: [Low/Med/High] | Confidence: [HIGH/MED/LOW]
**Evidence**: [Specific scanned counts this rests on — e.g. "31 near-duplicate update emails in 30 days"]
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

**Thin-data variant.** When evidence is too sparse to fill the template honestly (e.g. one tool, little history), do NOT pad it with estimated numbers. Deliver the scoped-down version instead:

```markdown
# Opportunity Scan Report — [Name] (Scoped — Thin Data)
**Sources scanned**: Google Calendar only — 8 events, 30 days
**Evidence depth**: Thin. No email/Slack/Jira connected, so frequency and time-saved are unmeasured.

## What I Can Actually Say
- [The one or two patterns the single source genuinely shows, with real counts]

## What I Can't Say Yet (and why)
- Hours-saved / ROI: unquantified — I have no frequency data for email, messaging, or ticket work.
- "[Bottleneck / broker / etc.]" patterns: insufficient signal to claim.

## Best Next Step
- Connect [Gmail / Slack / Jira] and rerun for a quantified report, OR tell me how often you do [X] and I'll compute ROI from a real number.

## Candidate (LOW confidence — verify before building)
### [Build Name] — [Type]
**ROI**: unquantified (LOW confidence) | Effort: [est] | Confidence: LOW
**Evidence**: [the single thin signal] — not enough to quantify savings.
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

- **Lead with data, not opinions.** Every recommendation cites scan evidence — this is a hard gate (Fidelity Firewall), not a stylistic preference. No evidence, no recommendation.
- **Be honest about ROI.** Don't inflate numbers, and don't *invent* them. 2 hours/week saved is meaningful — don't round up to 5, and never fabricate a figure to fill the field. "Unquantified — LOW confidence, [gap]" is a valid and correct answer when the scan can't support a number.
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
