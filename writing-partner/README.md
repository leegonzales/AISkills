# Writing Partner

An AI writing partner system for collaborative essay creation.

## Vision

Transform AI from a text generator into an intellectual prosthesis—a true writing partner that interviews, tracks threads, calibrates voice, and helps bring order from chaos while preserving the human spark.

## Core Insight

The gap between "I have ideas" and "I have something that sounds like me" is where most AI-assisted writing fails. This system bridges that gap through:

1. **Structured Interview** — Extract ideas through progressive questioning
2. **Thread Tracking** — Manage multiple parallel ideas, surface them at the right time
3. **Voice Calibration** — Ensure output sounds like you, not like AI

## Current Status

**Phase:** Design & MVP
**Approach:** Claude Code skill (may evolve to Claude SDK agent)

## Project Structure

```
writing-partner/
├── README.md           # This file
├── DESIGN.md           # Architecture and interview findings
├── SKILL.md            # Claude skill specification
├── prompts/            # System prompts and templates
│   └── interview.md    # Structured interview protocol
├── examples/           # Reference materials
└── tests/              # Test cases and scenarios
```

## Origin

Emerged from a structured interview session (2025-12-18) exploring how to make AI-assisted writing feel authentic. Key realization: the existing prose-polish essay was written *by* Claude, not *with* Lee—and that's exactly the problem this system solves.

## Related Projects

- `substack/` — Content creation substrate (consumer of this system)
- `AISkills/` — Skill repository (eventual home of the skill)
