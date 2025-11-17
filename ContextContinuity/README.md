# Context Continuity

**Version 1.0.0**

High-fidelity context transfer protocol for moving conversations between AI agents. Preserve decision tempo, open loops, and critical context with graceful degradation.

## What Is Context Continuity?

When you need to transfer conversations between AI agents (different chats, systems, or context window resets), naive copy-paste loses critical context. This skill creates structured transfer artifacts that:

- **Preserve decision tempo** - Avoid rehashing resolved questions
- **Maintain forward momentum** - Surface open loops and next actions
- **Gracefully degrade** - Critical information survives truncation
- **Separate fact from interpretation** - What happened vs. why it matters
- **Support dual parsing** - Human-scannable and machine-parseable

## Use Cases

- **Context window resets** - Start fresh chat without losing state
- **Cross-system transfers** - Move from Claude.ai to Claude Code (or vice versa)
- **Long-running projects** - Preserve multi-week context across sessions
- **Team handoffs** - Transfer work between developers/analysts
- **Emergency pivots** - Quickly capture state when conversation derails
- **Iterative transfers** - Chain multiple transfers for complex projects

## Installation

### For Claude Code (Recommended)

1. Clone or download this repository
2. Copy the `context-continuity/` directory to your skills location:
   - **Personal skills**: `~/.claude/skills/context-continuity/`
   - **Project skills**: `.claude/skills/context-continuity/` in your project root
3. The skill will be automatically discovered by Claude

```bash
# Personal skills (globally available)
cp -r context-continuity ~/.claude/skills/

# Project skills (project-specific)
mkdir -p .claude/skills
cp -r context-continuity .claude/skills/
```

### For Claude Web Chat

Download [`context-continuity-v1.0.0.skill`](dist/context-continuity-v1.0.0.skill) from the `dist/` folder and upload directly to any Claude conversation.

### Direct GitHub Download

**Option 1: Download single file**
```bash
curl -O https://raw.githubusercontent.com/leegonzales/AISkills/main/ContextContinuity/dist/context-continuity-v1.0.0.skill
```

**Option 2: Download entire repository**
```bash
git clone https://github.com/leegonzales/AISkills.git
cd AISkills/ContextContinuity
```

## Quick Start

### Triggering the Skill

Claude automatically activates this skill when you say:

```
"Transfer this conversation"
"Create a handoff artifact"
"Continue this in another chat"
"Handoff to new session"
"Summarize for transfer"
```

**Important:** The skill does NOT trigger on simple "summarize our conversation" requests—only when transfer intent is explicit.

### Two Modes Available

**Minimal Mode (~200 words)**
- Fast, captures essentials
- Mission, key decisions, next action
- Perfect for 80% of transfers

**Full Mode (~1000 words)**
- Comprehensive context preservation
- Decision log, open loops, critical context, conversation history
- For complex strategic work

### Example Workflow

```
You: "I need to transfer this conversation to Claude Code"

Claude: "I can create a transfer artifact in two modes:
        1. Minimal (~200 words) - Fast, captures essentials
        2. Full (~1000 words) - Comprehensive
        Which would you prefer?"

You: "Minimal is fine"

Claude: [Generates minimal artifact]
        "§ TRANSFER READY—Before you transfer, does this capture
        the essentials, or should I expand any section?"

You: "Looks good"

[Copy artifact to new Claude Code session]

Claude Code: "I've reviewed the transfer. Quick confirmation:
             - Mission: [echoes mission]
             - Status: [echoes status]
             - Next: [echoes next action]

             Ready to [next action]. What's your priority?"
```

## Features

### Minimal Mode

Perfect for straightforward transfers:

```markdown
**TRANSFER**: [One sentence describing the work]
**STATUS**: [✓ resolved | ⧗ in-progress | ⚠ blocked | ↻ iterating]
**DECIDED**: [Key decision + rationale]
**NEXT**: [Immediate next action]
**CONTEXT**: [1-2 paragraphs of critical background]
**HUMAN PREFS**: [Communication style preferences]
```

Fast, concise, captures what matters.

### Full Mode

For complex transfers requiring detailed context:

- **§ Immediate Orientation** - Mission, status, next action
- **§ Decision Log** - What was decided, why, what was rejected, tradeoffs
- **§ Open Loops** - Unresolved questions, blockers, pending inputs
- **§ Critical Context** - Key insights with evolution tags [G/C/P/K]
- **§ Artifacts & Outputs** - Created files, references, tools used
- **§ Human Context** - Communication preferences, assumed knowledge
- **§ Conversation History** - Chronological narrative (optional)
- **§ Transfer Metadata** - Provenance, completeness, handoff notes

### Evolution Tags

Track information maturity using Wardley-inspired tags:

- **[G] Genesis** - Novel discovery, first-time insight
- **[C] Custom** - Emerging pattern, still validating
- **[P] Product** - Established approach, proven
- **[K] Commodity** - Common knowledge, standard practice

Helps receiving agent understand how much trust to place in each piece of information.

### Decision Taxonomy

Prevents rehashing resolved debates:

- **Explicit** - Deliberate choice with clear rationale
- **Implicit** - Started doing X without formal decision
- **Emergent** - Pattern that evolved over conversation

### Handshake Protocol

Critical safety feature: receiving agent echoes back mission, status, and next action to confirm understanding before continuing. Catches misinterpretation early.

## Validation

Validate artifacts using the included script:

```bash
python context-continuity/scripts/validate_transfer.py artifact.md

# Auto-detect mode
python validate_transfer.py my-handoff.md

# Explicit mode selection
python validate_transfer.py my-handoff.md --mode minimal

# Strict validation (warnings = errors)
python validate_transfer.py my-handoff.md --strict

# Quiet mode (errors and warnings only)
python validate_transfer.py my-handoff.md --quiet
```

The validator checks:
- Required sections/fields present
- Proper structure and formatting
- Decision types specified
- Evolution tags used correctly
- Completeness indicators
- Handshake readiness

## Structure

```
ContextContinuity/
├── README.md                               # This file
├── Context Continuity Guide.md             # Detailed usage examples
├── Context Continuity Analysis.md          # Design rationale
├── dist/
│   └── context-continuity-v1.0.0.skill    # Versioned release
└── context-continuity/                     # Main skill directory
    ├── SKILL.md                            # Skill definition
    ├── references/
    │   ├── artifact-template.md            # Full template structure
    │   ├── generator-prompt.md             # Prompt for generating artifacts
    │   ├── receiver-prompt.md              # Guidance for receiving agents
    │   └── examples.md                     # 6 real-world scenarios
    └── scripts/
        └── validate_transfer.py            # Artifact validator
```

## Best Practices

### For Generating Transfers

1. **Choose the right mode** - Minimal for 80% of cases, Full for complexity
2. **Be specific about decisions** - Include type (explicit/implicit/emergent)
3. **Flag uncertainties** - Use Uncertainty Map in Critical Context
4. **Mark evolution stage** - Tag insights with [G/C/P/K]
5. **Force engagement** - Always ask "which section to expand?"
6. **Don't fabricate** - Mark emergent patterns honestly, don't create post-hoc rationale

### For Receiving Transfers

1. **Scan § Immediate Orientation first** - Get bearings quickly
2. **Read § Decision Log** - Don't rehash resolved debates
3. **Check § Open Loops** - Know what needs attention
4. **Acknowledge with handshake** - Echo mission/status/next before continuing
5. **Integrate naturally** - Don't say "I can see from the artifact..."; just continue the work

### For Humans

**Before pasting to new agent:**
- Answer the "which section to expand" question
- Scan for accuracy and completeness
- Redact sensitive information
- Verify § NEXT ACTION matches intent

**When starting with new agent:**
- Paste artifact first, then state immediate need
- Wait for handshake confirmation
- If agent seems confused, point to specific sections
- Accept some context loss is unavoidable

## Advanced Usage

### Iterative Transfer Chains

For long-running projects:
- Previous artifacts can be referenced in § Conversation History
- Evolution tags track how understanding matured across agents
- Decision log accumulates across transfer boundaries

See [Example 6 in examples.md](context-continuity/references/examples.md#example-6-iterative-transfer-chain-minimal-mode--full-mode)

### Cross-System Transfers

Works between:
- Claude.ai ↔ Claude Code
- Claude ↔ Other LLMs (with handshake protocol)
- Human ↔ Human (for team handoffs)

No special formatting required—just markdown.

### Custom Adaptations

Extend for domain-specific needs:
- Add § Code Context for dev projects
- Add § Research Notes for analysis work
- Add § Stakeholder Map for strategic planning
- Reorder sections based on priority
- Adjust detail level for different audiences

### Emergency Pivots

Use Minimal mode to quickly capture state when:
- Conversation derails unexpectedly
- Context window approaching limit
- Need to switch tools/systems mid-work
- Unexpected interruption requires handoff

## Documentation

- **[Context Continuity Guide.md](Context%20Continuity%20Guide.md)**: Detailed examples and workflows
- **[Context Continuity Analysis.md](Context%20Continuity%20Analysis.md)**: Design philosophy and meta-analysis
- **[context-continuity/SKILL.md](context-continuity/SKILL.md)**: Core skill definition
- **[context-continuity/references/examples.md](context-continuity/references/examples.md)**: Six worked examples (Minimal and Full modes)
- **[context-continuity/references/artifact-template.md](context-continuity/references/artifact-template.md)**: Complete template structure
- **[context-continuity/references/generator-prompt.md](context-continuity/references/generator-prompt.md)**: Prompt for creating artifacts
- **[context-continuity/references/receiver-prompt.md](context-continuity/references/receiver-prompt.md)**: Optional prepend for receiving agents

## Design Philosophy

Context Continuity follows proven skill-building patterns:

- **Dual-mode operation** - Minimal (80% of cases) vs Full (20% complex transfers)
- **Antifragile structure** - Critical info at top; graceful degradation under truncation
- **Dual interface** - Human-scannable (verification) + machine-parseable (structured)
- **Tempo preservation** - Decision taxonomy prevents circular rehashing
- **Fact-meaning separation** - Artifacts (what exists) vs Critical Context (why it matters)
- **Forced engagement** - "Which section to expand?" prevents blind paste
- **Evolution awareness** - [G/C/P/K] tags track information maturity

See [Context Continuity Analysis.md](Context%20Continuity%20Analysis.md) for complete design rationale.

## Failure Modes and Mitigations

**Problem:** Receiving agent treats artifact as gospel
**Mitigation:** Transfer Metadata includes uncertainty indicators; handshake forces re-orientation

**Problem:** Human doesn't know what's critical
**Mitigation:** Generator asks for evolution tags and uncertainty maps; forced section review

**Problem:** Truncation cuts off critical context
**Mitigation:** Antifragile structure puts mission/status/next at top; each section self-contained

**Problem:** Load-bearing jokes/metaphors lost
**Mitigation:** § Conversation History explicitly calls out notable moments

**Problem:** Over-reliance on artifact instead of re-engagement
**Mitigation:** Artifact is starting hypothesis, not replacement for human context-setting

## FAQ

**Q: When should I use Minimal vs Full mode?**
A: Minimal for 80% of transfers (quick tasks, clear next action). Full for complex strategic work, multiple decision points, or long-running projects.

**Q: Can I edit the artifact before pasting?**
A: Yes! The artifact is for you to review and refine. Redact sensitive info, expand sections, or adjust detail level.

**Q: What if the receiving agent doesn't understand the artifact?**
A: Point them to specific sections (§ Immediate Orientation, § Open Loops). If still confused, paste the receiver-prompt.md prepend for guidance.

**Q: Does this work with non-Claude AI systems?**
A: Yes, with handshake protocol. The artifact is plain markdown with no Claude-specific assumptions.

**Q: How do I handle multiple transfers in a project?**
A: Reference previous artifacts in § Conversation History. Evolution tags track how understanding matured across transfers.

**Q: What if I don't want Full mode's 8 sections?**
A: Use Minimal mode, or adapt Full mode template. The structure is customizable—just maintain antifragile ordering (critical info first).

## Contributing

Contributions welcome! Consider adding:

- Additional real-world examples for different domains
- Domain-specific template variants (dev, research, strategy)
- Validation rules for specialized use cases
- Integration tools (export to project management systems)

## License

MIT License - feel free to use, modify, and distribute.

## Questions?

- Check [Context Continuity Guide.md](Context%20Continuity%20Guide.md) for detailed examples
- See [references/examples.md](context-continuity/references/examples.md) for 6 real-world scenarios
- Use the validator to check artifact structure
- Ask Claude to explain any part of the protocol

---

Built with Claude Code Skills | [Learn more about Claude Code](https://code.claude.com/)
