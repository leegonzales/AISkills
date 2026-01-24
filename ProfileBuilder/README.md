# Profile Builder

**Version 1.0.0** | [Changelog](CHANGELOG.md)

Build personalized Claude profile text through structured Q&A interviews. Output is ready to paste into Settings > Profile > Personal Preferences.

## What Is Profile Builder?

This skill helps users create effective Claude personalization profiles through guided conversation:
- **Structured Interview**: Four-section discovery process covering communication, identity, frameworks, and boundaries
- **Voice Calibration**: Output reflects the user's authentic voice, not a template
- **Ready-to-Use Output**: Generated text pastes directly into Claude's Personal Preferences

## Use Cases

- **New Claude Users**: Create an initial profile during onboarding
- **Profile Refresh**: Update outdated or ineffective profiles
- **Team Profiles**: Help colleagues articulate their preferences
- **Voice Discovery**: Users unsure how they want Claude to communicate

## How It Works

### Interview Phases

**Phase 1: Communication Preferences**
- How should Claude talk to you?
- What do you NOT need from Claude?
- What DO you need from Claude?

**Phase 2: Professional Identity**
- What's your role and domain?
- What do you actually do day-to-day?
- What's your relevant background?

**Phase 3: Frameworks & Approaches**
- What methodologies do you use?
- What defaults should Claude apply?

**Phase 4: Boundaries & Defaults**
- What should Claude NEVER do?
- What should Claude ALWAYS do?
- Any tone/style requirements?

### Output

A cohesive 150-400 word profile written in first person, ready to paste into Claude's Personal Preferences.

## Quick Start

### Trigger Phrases

```
"Help me build my Claude profile"
"Create my personal preferences for Claude"
"I want to customize how Claude responds to me"
"Set up Claude for me"
```

Claude will begin the guided interview process.

### Example Output

```
I do not need affirmation—I need reflection, resistance, refinement.
You are not a yes-machine. If you disagree, say so with clarity.

I'm the Director of Customer Success at [Company], leading a team
of 12 CSMs focused on enterprise accounts. My work blends relationship
management, data analysis, and cross-functional coordination.

Core frameworks: Jobs-to-be-Done, OKRs, MEDDIC. Apply when relevant.

Always: Be direct. Challenge weak reasoning. Suggest alternatives.
Never: Pad responses with caveats. Assume I need basics explained.

Match my energy: professional but not stiff, concise but thorough.
```

## Installation

### For Claude Code

```bash
# Personal skills (run from the ProfileBuilder directory)
cp -r profile-builder ~/.claude/skills/

# Project skills (run from your project's root, adjust source path as needed)
mkdir -p .claude/skills
cp -r /path/to/ProfileBuilder/profile-builder .claude/skills/
```

### For Claude Web Chat

Download [`profile-builder-v1.0.0.skill`](dist/profile-builder-v1.0.0.skill) from the `dist/` folder and upload directly to any Claude conversation.

## Structure

```
ProfileBuilder/
├── README.md                      # This file
├── CHANGELOG.md                   # Version history
├── dist/                          # Distribution packages
│   └── profile-builder-v1.0.0.skill
└── profile-builder/               # Main skill directory
    ├── SKILL.md                   # Skill definition
    └── references/
        └── examples.md            # Example profiles
```

## Best Practices

1. **Answer Authentically**: Don't aim for what sounds good—describe how you actually work
2. **Be Specific**: "Be direct" is better than "communicate effectively"
3. **Start Simple**: You can always add complexity later
4. **Iterate**: First draft is never final—refine based on experience

## Examples

See [`profile-builder/references/examples.md`](profile-builder/references/examples.md) for complete examples including:
- Executive Coach profile
- Engineering Leader profile
- Customer Success Leader profile
- Facilitator/Consultant profile
- Minimal profile (valid choice!)
- Power User profile with archetypes

## Limitations

**V1.0 does not include:**
- Multi-session profile building (single conversation)
- Profile comparison or A/B testing
- Team profile templates
- Import from existing profiles

These are reasonable future enhancements.

## Contributing

Contributions welcome! Consider adding:
- Additional example profiles for different roles
- Interview questions for specific domains
- Profile anti-pattern examples
- Integration with other skills

---

Built with Claude Code Skills | Personal AI Customization
