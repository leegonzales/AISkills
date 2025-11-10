# Claimify

A Claude Code skill that transforms messy discourse into structured argument maps. Extract claims, map logical relationships, identify assumptions, and reveal the structure of reasoning.

## What Is Claimify?

Claimify analyzes arguments by:
- Extracting explicit and implicit claims
- Mapping logical relationships (supports/opposes/assumes/contradicts)
- Identifying evidence chains and argument structure
- Finding tension points, gaps, and hidden assumptions

## Use Cases

- Debate analysis
- Strategic document review
- Meeting notes → decision maps
- Research synthesis
- Red-teaming your own arguments
- Identifying logical gaps and contradictions

## Installation

### For Claude Code (Recommended)

1. Clone or download this repository
2. Copy the `claimify/` directory to your skills location:
   - Personal skills: `~/.claude/skills/claimify/`
   - Project skills: `.claude/skills/claimify/` in your project root
3. The skill will be automatically discovered by Claude

### For Claude Web Chat

Download [`claimify-v1.0.0.skill`](dist/claimify-v1.0.0.skill) from the `dist/` folder and upload directly to any Claude conversation.

## Quick Start

Once installed, trigger Claimify by asking Claude:

```
"What are the claims in this argument?"
"Analyze this debate"
"Map the logical structure"
"What assumptions does this make?"
"Extract the reasoning"
"Find contradictions"
"Red-team this argument"
```

### Example

```
You: Analyze this argument:

"Remote work is better because it saves commute time.
Therefore, all companies should go fully remote."

Claude will extract claims, identify the implicit assumption
(that time savings are paramount), and flag the absolutism
of "all companies."
```

## Features

### Analysis Depth Levels

- **Surface**: Quick scan of explicit claims
- **Standard** (default): Explicit claims + obvious implicit assumptions
- **Deep**: Full logical structure with hidden assumptions and strengthening suggestions

Specify your level: `"Do a deep analysis of..."`

### Output Formats

- **Table**: Quick reference and claim tracking
- **Graph** (Mermaid): Visualizing argument structure
- **Narrative**: Understanding flow and identifying tensions
- **JSON**: Programmatic processing

Specify format: `"Extract claims as JSON"` or `"Show me a graph"`

### Claim Types

- **Factual**: Empirical statements
- **Normative**: Value judgments, "should" statements
- **Definitional**: Establishing meaning
- **Causal**: X causes Y
- **Predictive**: Future-oriented claims
- **Assumption**: Unstated premises

### Relationship Types

- **Supports**: Evidence/reasoning for
- **Opposes**: Undermines/contradicts
- **Assumes**: Requires to be true
- **Refines**: Specifies/clarifies
- **Contradicts**: Mutually exclusive

## Documentation

- **[Claimify Guide.md](Claimify%20Guide.md)**: Complete usage guide with examples
- **[Claimify Analysis.md](Claimify%20Analysis.md)**: Meta-analysis of building the skill
- **[claimify/SKILL.md](claimify/SKILL.md)**: Core skill definition
- **[claimify/references/examples.md](claimify/references/examples.md)**: Six detailed worked examples

## Validation

Validate JSON output using the included script:

```bash
python claimify/scripts/claim_validator.py your_claims.json
```

## Structure

```
Claimify/
├── README.md                          # This file
├── Claimify Guide.md                  # Complete usage guide
├── Claimify Analysis.md               # Meta-analysis and design doctrine
├── dist/
│   └── claimify-v1.0.0.skill         # Versioned release
└── claimify/                          # Main skill directory
    ├── SKILL.md                       # Skill definition
    ├── references/
    │   └── examples.md                # Worked examples
    └── scripts/
        └── claim_validator.py         # JSON validation utility
```

## Best Practices

1. **Provide Context**: Give complete arguments, not sentence fragments
2. **Specify What You Need**: Surface level vs. deep analysis
3. **Choose the Right Format**: Narrative for exploring, Table for tracking, Graph for presenting
4. **Iterate**: Start with standard analysis, then request deeper dives

## Advanced Usage

### Synthesizing Multiple Sources

```
"Synthesize claims across these three documents and show me
where they agree, disagree, and what's unstated."
```

### Decision Mapping

```
"Extract the decision structure from this meeting transcript—
what claims support each option?"
```

### Strengthening Arguments

```
"Red-team my argument and suggest how to make it stronger."
```

## Design Philosophy

Claimify follows skill-building best practices:

- **Concise core**: Lean skill definition (< 500 lines)
- **Progressive disclosure**: Examples split into references
- **Appropriate freedom**: Guidelines, not rigid rules
- **Bundled utility**: Validator script for quality checks
- **Examples over explanation**: Six worked examples showing patterns

See [Claimify Analysis.md](Claimify%20Analysis.md) for the complete meta-analysis.

## Contributing

This skill was built using the skill-creator framework's doctrine. Contributions welcome:

- Additional examples for different domains
- Enhanced validation rules
- Domain-specific variants (legal, scientific, strategic)
- Integration tools

## License

MIT License - feel free to use, modify, and distribute.

## Questions?

- Check the [Claimify Guide.md](Claimify%20Guide.md) for detailed examples
- Use the validator to check JSON structure
- Ask Claude to explain any part of the analysis

---

Built with Claude Code Skills | [Learn more about Claude Code](https://docs.claude.com/en/docs/claude-code)
