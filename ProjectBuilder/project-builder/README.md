# Project Builder

Create effective Claude Projects with custom instructions and dynamic context manifests.

## What It Does

Guides you through building Claude Projects that:
- Understand your specific workflow
- Access dynamic information sources via Google Drive
- Produce consistent, high-quality outputs

## Usage

**Start the interview:**
```
I want to create a Claude project for [task]. Can you help me set it up?
```

**Or be specific:**
```
Help me build a Claude project for weekly reporting. I need to pull data from
multiple Google Sheets and generate executive summaries.
```

## Trigger Phrases

- "Set up a Claude project"
- "Create project instructions"
- "Help me build a Claude workflow"
- "I need a project for [task]"

## What You Get

1. **Project Instructions** — Custom instructions for Claude
2. **Context Manifest** — Points to your dynamic documents
3. **Setup Guide** — Step-by-step project creation
4. **Connection Recommendations** — Which integrations to enable

## Key Concept: Context Manifests

Unlike static file uploads, manifests point Claude to living documents:

```markdown
## Quick Reference

When you need... | Check this source
-----------------|------------------
Current metrics  | [Q1 Dashboard](link)
Team roster      | [People Doc](link)
Style guide      | [Brand Standards](link)
```

This lets Claude access up-to-date information through Google Drive connection.

## Best For

- Recurring workflows (weekly reports, reviews, analyses)
- Tasks requiring current data from multiple sources
- Workflows with consistent output formats
- Team processes that need documentation

## File Structure

```
ProjectBuilder/
└── project-builder/
    ├── SKILL.md                     # Core skill definition
    ├── README.md                    # This file
    └── references/
        └── manifest-template.md     # Full manifest template
```

## Related Skills

- **Skill Extractor** — Extract skills from conversations
- **Claude Project Docs** — Generate CLAUDE.md files
- **Process Mapper** — Document workflows before building projects
