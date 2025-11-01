# AI Skills Collection

A curated collection of skills for Claude Code and general Claude conversations, designed for enhanced AI-assisted development, analysis, and reasoning.

## What Are Claude Skills?

Skills are modular, model-invoked capabilities that extend Claude's functionality. Unlike slash commands that require explicit invocation, skills are automatically discovered and used by Claude based on context, enabling complex workflows with automatic discovery.

This collection includes:
- **Claude Code Skills**: For use within the Claude Code IDE, supporting development workflows
- **General Claude Skills**: For use in any Claude conversation, enhancing analysis and reasoning capabilities

Many skills work in both contexts, providing flexible capabilities wherever you interact with Claude.

## Skills in This Collection

### Claimify

Transform messy discourse into structured argument maps. Extract claims, map logical relationships, identify assumptions, and reveal the structure of reasoning.

**Use for:**
- Debate analysis
- Strategic document review
- Meeting notes → decision maps
- Research synthesis
- Red-teaming arguments
- Identifying logical gaps

**[View Claimify →](Claimifty/)**

### Anti-Cliché Writing

Comprehensive detection, prevention, and remediation of AI writing clichés. Elevate text to human-quality through systematic analysis and targeted interventions.

**Use for:**
- Polish AI-generated content
- Analyze writing quality with scored reports
- Generate better content with anti-cliché prompts
- Teach pattern recognition and writing craft
- Ensure professional client deliverables

**[View Anti-Cliché Writing →](AntiClicheWriting/)**

---

## Installation

### For Claude Code

#### Personal Skills (Available Globally)

```bash
# Install all skills for all projects
cp -r Claimifty/claimify ~/.claude/skills/
cp -r AntiClicheWriting/anti-cliche-writing ~/.claude/skills/

# Or install individual skills
cp -r Claimifty/claimify ~/.claude/skills/claimify/
cp -r AntiClicheWriting/anti-cliche-writing ~/.claude/skills/anti-cliche-writing/
```

#### Project Skills (Project-Specific)

```bash
# Install skills for a specific project
cd your-project/
mkdir -p .claude/skills

# Copy desired skills
cp -r /path/to/AISkills/Claimifty/claimify .claude/skills/
cp -r /path/to/AISkills/AntiClicheWriting/anti-cliche-writing .claude/skills/
```

### For General Claude Conversations

Upload the packaged `.skill` file directly to any Claude conversation:

```
1. Navigate to the skill directory (e.g., Claimifty/)
2. Upload the .skill file (e.g., "Claimify Skill - Claude.skill")
3. The skill will be available for that conversation
```

Alternatively, you can share the SKILL.md content directly in your conversation.

## Using Skills

Once installed, skills are automatically discovered by Claude. Simply use natural language that matches the skill's description:

```
# Triggers Claimify
"Analyze this argument and map the claims"
"What assumptions does this make?"
"Red-team this reasoning"
```

## Repository Structure

```
AISkills/
├── README.md                           # This file
├── Claimifty/                          # Claimify skill
│   ├── README.md                       # Claimify documentation
│   ├── claimify/                       # Main skill directory
│   │   ├── SKILL.md                    # Skill definition
│   │   ├── references/                 # Examples and documentation
│   │   └── scripts/                    # Utilities
│   └── ...                             # Additional documentation
├── AntiClicheWriting/                  # Anti-Cliché Writing skill
│   ├── README.md                       # Skill documentation
│   ├── AI Writing Clichés Review.md    # Design analysis
│   ├── AI Writing Clichés Guide.skill  # Packaged skill file
│   └── anti-cliche-writing/            # Main skill directory
│       ├── SKILL.md                    # Skill definition
│       └── references/                 # Detection patterns, strategies
└── [future skills]                     # More skills coming soon
```

## Skill Design Philosophy

All skills in this collection follow these principles:

1. **Concise core**: Lean skill definitions (< 500 lines)
2. **Progressive disclosure**: Essential content in SKILL.md, examples in references
3. **Appropriate freedom**: Guidelines over rigid rules for flexibility
4. **Bundled utilities**: Scripts and tools that support the skill
5. **Examples over explanation**: Worked examples showing real usage

## Creating Your Own Skills

Each skill directory contains:

```
skill-name/
├── SKILL.md              # Required: Name, description, workflow
├── references/           # Optional: Examples and additional docs
│   └── examples.md
└── scripts/              # Optional: Utilities and validators
    └── helper.py
```

See individual skill documentation for design patterns and best practices.

## Contributing

Contributions welcome! To add a new skill:

1. Create a new directory following the structure above
2. Include comprehensive SKILL.md with clear trigger phrases
3. Add worked examples
4. Include any supporting scripts or utilities
5. Update this README with the new skill

## Skills Roadmap

Planned skills for future development:

- **Strategic Mapping**: Wardley mapping and doctrine analysis
- **Decision Trees**: Multi-criteria decision analysis
- **Research Synthesis**: Academic paper analysis and synthesis
- **Code Architecture**: System design and architecture analysis
- **Project Planning**: OODA loop and agile planning

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Skill Creation Best Practices](https://docs.claude.com/en/docs/claude-code/skills#best-practices)

## License

MIT License - feel free to use, modify, and distribute.

Each skill may have its own license - check individual skill directories for details.

## Questions?

- Check individual skill documentation for usage questions
- Refer to [Claude Code Skills documentation](https://docs.claude.com/en/docs/claude-code/skills)
- Open an issue for bugs or feature requests

---

**Current Skills**: 2 | **Last Updated**: 2025-11-01 | Built with Claude Code
