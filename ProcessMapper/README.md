# Process Mapper

**Version 1.0.0**

Map workflows, extract SOPs, and identify automation opportunities. Systematic process discovery, tacit knowledge documentation, and AI tractability assessment implementing the **SOP-first doctrine**: "You can't automate what you can't see."

## What Is Process Mapper?

This skill grounds systematic process capture in reality:
- **Shadow processes are real processes** - Document what actually happens, not org charts
- **Tacit knowledge is documentable** - Capture decision *points*, not decision *logic*
- **Structure enables automation** - Visibility reveals AI opportunities

**Core workflow:** Discovery → Documentation → Analysis → Automation mapping

## Use Cases

- **Process documentation** - "Map our workflow for X"
- **SOP creation** - "Document our process for Y"
- **Automation opportunity analysis** - "Where can we apply AI to this process?"
- **Process discovery interviews** - Systematic capture of tribal knowledge
- **Workflow optimization** - Identify bottlenecks and failure modes
- **Knowledge transfer** - Document before key people leave

## Core Features

### 3-State Diagnostic

**State 1: Fiction**
- SOPs exist but nobody follows them
- Beautiful docs, zero usage
- Aspirational not actual
- **Action:** Archive and start fresh

**State 2: Nonexistent** (most common)
- No documentation
- Tribal knowledge
- "Just ask Sarah"
- **Action:** Begin discovery

**State 3: Accurate**
- Docs match reality
- Referenced regularly
- Updated when process changes
- **Action:** Use for automation analysis

### 5-Round Interview Methodology

**Round 1: High-Level Flow** (15 minutes)
- Get end-to-end sequence
- Identify trigger, endpoint, duration
- Capture 5-10 major steps

**Round 2: Step Decomposition** (20 minutes)
- Break each step into substeps
- Document inputs, tools, transformations
- Look for: copy-paste, manual entry, system switching

**Round 3: Decision Points** (15 minutes)
- Identify where judgment is required
- Capture explicit criteria
- Document tacit knowledge as **labeled black boxes**
- Map escalation paths

**Round 4: Edge Cases & Exceptions** (10 minutes)
- Understand failure modes
- Document workarounds
- Estimate exception frequency
- Identify shadow processes

**Round 5: Context Dependencies** (10 minutes)
- Surface tacit knowledge
- Identify domain knowledge requirements
- Reveal institutional knowledge
- Assess training needs

### Documentation Formats

**Linear SOP** (≤10 steps, minimal branching)
- Sequential steps with actions/tools/inputs
- Best for straightforward workflows

**Decision Tree** (multiple branches, clear criteria)
- Visual flowchart with if-then logic
- Best for rules-based processes

**State Machine** (complex loops, multiple end states)
- States, transitions, triggers
- Best for stateful processes

**Narrative SOP** (high tacit knowledge, judgment-heavy)
- Principles + examples + decision guidance
- Best for expertise-dependent work

### Automation Tractability Assessment

**High Tractability** (AI-ready now):
- Repetitive tasks
- Clear inputs/outputs
- Explicit rules
- Low context dependency
- High volume

**Medium Tractability** (AI-ready with structure):
- Pattern recognition tasks
- Moderate judgment
- Documentable criteria
- Some context needed
- Medium volume

**Low Tractability** (Not yet automatable):
- Novel situations
- High tacit knowledge
- Complex judgment
- Deep context required
- Relationship-dependent

### Automation Opportunity Types

**Type 1: Full Automation**
- Replace entire step with AI/script
- Example: Data extraction from PDFs

**Type 2: Augmentation**
- AI assists human decision
- Example: Flagging anomalies for review

**Type 3: Acceleration**
- Speed up existing step
- Example: Auto-drafting responses

**Type 4: Quality Enhancement**
- Improve accuracy/consistency
- Example: Validation checks

**Type 5: Insight Generation**
- New capabilities from data
- Example: Pattern detection across cases

## Installation

### For Claude Code

```bash
# Personal skills (globally available)
cp -r ProcessMapper/process-mapper ~/.claude/skills/

# Project skills (project-specific)
mkdir -p .claude/skills
cp -r ProcessMapper/process-mapper .claude/skills/
```

### For Claude Web Chat

Download [`process-mapper-v1.0.0.skill`](dist/process-mapper-v1.0.0.skill) from the `dist/` folder and upload directly to any Claude conversation.

## Quick Start

### Document a Process

```
"Help me document our customer onboarding process. I'll walk you through it."
```

Claude will:
1. Assess SOP state (likely Nonexistent)
2. Conduct 5-round discovery interview
3. Choose appropriate documentation format
4. Generate SOP with decision points and edge cases
5. Assess automation tractability

### Identify Automation Opportunities

```
"Analyze this SOP and tell me where we can apply AI"
```

Claude will:
1. Map tractability for each step
2. Identify automation opportunity types
3. Estimate effort vs impact
4. Prioritize recommendations
5. Flag tacit knowledge barriers

### Process Discovery Interview

```
"I need to document how our support team handles escalations. Can you interview me?"
```

Claude will systematically walk through 5 rounds, asking targeted questions.

## Usage Examples

### Round 1: High-Level Flow

```
Claude: "Walk me through this from start to finish. What triggers this process?"

User: "Sales closes a deal. That triggers onboarding."

Claude: "When are you done? What's the endpoint?"

User: "Customer is live in production with training complete."

Claude: "What are the major steps between deal close and production live?"
```

### Round 3: Decision Points

```
Claude: "How do you decide whether to assign a Technical Account Manager?"

User: "If the deal is over $100K annual contract value, they get a TAM."

Claude: "That's explicit criteria - documentable as rule. What if it's $95K but complex technical requirements?"

User: "Then I escalate to my director."

Claude: [Documents: Decision point with explicit rule + escalation path for edge cases]
```

### Labeling Black Boxes

```
Claude: "How do you decide if a bug report is critical vs high priority?"

User: "I just... know. Based on experience."

Claude: [Documents: **Labeled black box** - decision point exists, logic is tacit. Requires domain expertise. High context dependency. Low automation tractability.]
```

## Structure

```
ProcessMapper/
├── README.md                                    # This file
├── Process Mapper Skill - Claude.skill          # Packaged skill file
└── process-mapper/                              # Main skill directory
    ├── SKILL.md                                 # Skill definition
    ├── references/
    │   ├── discovery-methodology.md             # 5-round interview framework
    │   └── automation-framework.md              # Tractability assessment system
    └── assets/
        └── visual-templates.md                  # Flowchart and diagram templates
```

## Automation Tractability Framework

**Assessment dimensions:**

**Input Clarity** (How well-defined are inputs?)
- Structured data: HIGH
- Semi-structured: MEDIUM
- Unstructured/novel: LOW

**Decision Logic** (How explicit are decision rules?)
- Explicit rules: HIGH
- Documentable patterns: MEDIUM
- Tacit expertise: LOW

**Context Requirements** (How much context needed?)
- Self-contained: HIGH
- Some context: MEDIUM
- Deep institutional knowledge: LOW

**Exception Rate** (How often does normal path fail?)
- <5%: HIGH
- 5-20%: MEDIUM
- >20%: LOW (might indicate wrong process)

**Volume/ROI** (How often does this happen?)
- Daily/hourly: HIGH value to automate
- Weekly: MEDIUM value
- Monthly/rare: LOW value

## Quality Signals

**High-quality SOP:**
- Reflects what actually happens (not aspirational)
- Decision points clearly marked
- Tacit knowledge labeled (not hidden)
- Edge cases and failure modes documented
- Exception rates estimated
- Workarounds captured (reveal shadow processes)
- Tools and inputs specified
- Context dependencies explicit

**Poor SOP:**
- Describes ideal not real
- "Contact manager" without criteria
- Decision logic vague or missing
- No edge cases acknowledged
- No failure modes documented
- Unrealistic linear flow
- Tools/inputs assumed

## Anti-Patterns to Avoid

- **Don't document the org chart** - Document the real flow
- **Don't hide tacit knowledge** - Label it explicitly as black box
- **Don't ignore workarounds** - They reveal the real process
- **Don't skip edge cases** - High exception rates signal problems
- **Don't force automation** - Some things shouldn't be automated
- **Don't assume clarity** - "Decide appropriately" isn't a step
- **Don't optimize prematurely** - Document actual before ideal

## Reference Files

**When Claude loads these files:**

- `discovery-methodology.md` - When conducting process discovery interviews or assessing SOP state
- `automation-framework.md` - When analyzing automation opportunities or assessing tractability
- `visual-templates.md` - When creating flowcharts, state machines, or process diagrams

## Advanced Features

### Shadow Process Detection

```
"I notice you mentioned three different workarounds. Those might be the real process. Let's document the shadow process instead of the official one."
```

### Tacit Knowledge Extraction

```
"You said 'I just know' - that's tacit knowledge. Let's try to surface the pattern. Show me three examples of decisions you made, and let's see if there's implicit criteria."
```

### Automation Prioritization Matrix

Effort vs Impact mapping:
- **Quick Wins** (Low effort, High impact) - Do first
- **Major Projects** (High effort, High impact) - Plan carefully
- **Fill-ins** (Low effort, Low impact) - Do if time permits
- **Money Pits** (High effort, Low impact) - Avoid

## Contributing

Contributions welcome! Consider adding:
- Additional documentation formats
- Interview question libraries
- Industry-specific templates (healthcare, finance, etc.)
- Automation pattern library
- Integration with workflow tools

---

Built with Claude Code Skills | SOP-First Process Mapping
