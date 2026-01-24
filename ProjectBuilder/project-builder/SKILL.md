---
name: project-builder
description: Create Claude Projects with custom instructions and manifests. Use when asked to "set up a Claude project," "create project instructions," or "help me build a Claude workflow."
---

# Project Builder

Guide users through creating effective Claude Projects with custom instructions and dynamic context manifests.

## What You Create

1. **Project Instructions** — Custom instructions teaching Claude about the workflow
2. **Context Manifest** — Document pointing to dynamic information sources
3. **Reference List** — Recommendations for files to upload
4. **Connection Guide** — Which MCP connectors to enable

## Interview Framework

### 1. Workflow Discovery

- What task will this project support?
- How often do you do this task?
- What makes it challenging or time-consuming?

### 2. Context Needs

- What information do you reference while doing this?
- Where does it live? (Google Drive, local, APIs)
- How often does it change?

### 3. Output Requirements

- What should Claude produce?
- What format?
- Who's the audience?

### 4. Quality Criteria

- What makes good output vs. bad?
- Examples of excellent work?
- Mistakes to avoid?

### 5. Personal Context

- Your role and expertise level?
- Domain-specific terminology?
- Preferred tone or style?

## Output: Project Instructions

Generate using template in `references/project-instructions-template.md`.

Key sections to include:
- Context (role, task, domain)
- Primary Workflow (trigger phrase, steps)
- Key Information Sources (dynamic and static)
- Output Requirements (format, tone, length)
- Quality Criteria (good outputs, mistakes to avoid)

## Output: Context Manifest

Generate using template in `references/manifest-template.md`.

Manifests point Claude to living documents rather than static uploads:
- Google Drive docs that change frequently
- Dashboards and metrics
- Team rosters and org charts
- Templates and standards

## Connection Recommendations

| Need | Enable |
|------|--------|
| Access Google Docs/Sheets | Google Workspace |
| Read local files | File System |
| Search current info | Web Search |
| Company knowledge base | Relevant MCP server |

## Workflow

1. **Interview** — Ask discovery questions
2. **Summarize** — Reflect back understanding
3. **Generate** — Create instructions + manifest
4. **Iterate** — Refine based on feedback
5. **Setup Guide** — Walk through project creation

## Setup Instructions

After generating components, guide user through:

1. Create project at claude.ai → Projects
2. Paste Project Instructions
3. Upload static reference files
4. Create manifest in Google Drive
5. Enable connections (Settings → Connected Apps)
6. Test with sample task

## Quality Principles

- **Be Specific** — Vague instructions → vague outputs
- **Include Examples** — Concrete beats abstract
- **Anticipate Edge Cases** — What if info is missing?
- **Keep It Maintainable** — Simple manifests get updated

## References

- `references/manifest-template.md` — Full manifest template with instructions
- `references/project-instructions-template.md` — Full project instructions template
