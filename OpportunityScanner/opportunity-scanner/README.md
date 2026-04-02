# Opportunity Scanner

Deep-scan your connected work tools to discover the highest-value Claude skills, projects, and artifacts to build — for personal productivity and department leadership.

## What It Does

Scans Slack, email, calendar, Jira, Confluence, and other connected tools to find patterns of wasted time, repeated work, and automation opportunities. Delivers a ranked report with ROI estimates and specific build recommendations.

## Two Lenses

1. **For You** — Skills, projects, and artifacts that save YOU time daily
2. **For Your Team** — Builds that multiply across your department

## How It Works

1. **Pre-flight** — Detects which MCPs are connected
2. **Deep Scan** (3-5 min) — Scans 30 days of data across all connected tools
3. **Pattern Analysis** (1-2 min) — Identifies cross-source work patterns
4. **Recommendations** — Ranked by ROI with implementation roadmap
5. **Build** — Pick any recommendation and generate it on the spot

## Patterns It Detects

- Information Broker (manually routing info between teams)
- Repetitive Reporter (same update in 3 formats)
- Question Magnet (institutional knowledge bottleneck)
- Meeting Machine (calendar overload)
- Template Seeker (same doc with slight variations)
- Context Switcher (fragmented attention)
- Decision Bottleneck (team waiting on you)
- And 7 more quick-win patterns

## Installation

### Claude Web (claude.ai)
1. Open Claude → Settings → Skills
2. Upload the `.skill` file
3. Start a conversation and say "Scan for opportunities"

### Claude Code
1. Copy `opportunity-scanner/` to `.claude/skills/`
2. Invoke with `/opportunity-scanner`

## Requirements

- At least 2 MCPs connected (Google Workspace, Slack, Atlassian)
- 30 days of activity for meaningful patterns
- 5-10 minutes for the full scan and report
