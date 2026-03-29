# flywheel-scan

Cross-project roadmap discovery scan. Dispatches 4 domain scouts and 1 strategic doppelganger to review all repos, score work items, propose thread resolutions, and produce a replay HTML report.

## Installation

This is a Claude Code skill. Add it to your Claude Code configuration to invoke via `Skill(skill: "flywheel-scan")`.

## Usage

```
Skill(skill: "flywheel-scan")                          # Full scan (default)
Skill(skill: "flywheel-scan", args: "--mode quick")    # Active-invest repos only
Skill(skill: "flywheel-scan", args: "--domain biz")    # Single domain
Skill(skill: "flywheel-scan", args: "--mode diff")     # Only repos with git activity since last scan
Skill(skill: "flywheel-scan", args: "--dry-run")       # Scouts only, no doppelganger scoring
```

## How It Works

1. **Domain scouts** scan repos across 4 domains, surfacing work items and roadmap signals
2. **Strategic doppelganger** scores and prioritizes discovered items against Lee's goals
3. **Thread resolution** proposes how to resolve competing priorities
4. **Replay HTML** produces a browsable report of findings

## Output

Generates a standalone HTML replay document with scored work items, domain summaries, and recommended next actions.
