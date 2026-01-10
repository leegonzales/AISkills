# Writing Partner

**Version 1.0.0**

Collaborative essay writing through structured interview, thread tracking, and voice calibration. Transform AI from text generator into intellectual prosthesis.

## What It Does

- **Interview-first:** Extract real experiences before drafting—no fabrication
- **Thread tracking:** Mark and manage ideas as they emerge (MAIN, TANGENT, RESEARCH, COUNTER, SPARK)
- **Voice calibration:** Check output against blocklist patterns and optional voice samples
- **Ground truth preservation:** Only draft from interview material

## Use Cases

- Blog posts and essays that should sound authentically like you
- Thought leadership grounded in real experience
- Personal narratives without AI fabrication
- Any writing where voice matters more than speed

## Quick Start

```bash
# Install globally
cp -r writing-partner ~/.claude/skills/

# Or per-project
cp -r writing-partner your-project/.claude/skills/
```

Then start with:
- "Let's work on an essay about [topic]"
- "Interview me about [topic]"

## How It Works

**Division of Labor:**
- You provide: spark, taste, vision, real experiences
- AI provides: words, elevation, structure
- Shared: iterative refinement toward authentic voice

**Mode Flow:**
```
Interview → Thread Tracking → Drafting → Calibration
```

## Integration

Works with [Prose Polish](../ProsePolish/) for AI detection scoring. After drafting, run prose-polish to check for AI patterns.

## Structure

```
WritingPartner/
├── README.md                           # This file
└── writing-partner/
    ├── SKILL.md                        # Skill definition
    ├── references/
    │   └── blocklist.md                # AI patterns to avoid
    └── integrations/
        └── prose-polish.md             # Prose-polish integration
```

---

Built with Claude Code Skills
