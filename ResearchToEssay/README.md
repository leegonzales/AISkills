# Research-to-Essay

**Version 1.0.0**

Research-driven essay and post creation with thematic synthesis, citation management, and voice calibration. Systematic workflow for producing publication-grade essays from research.

## What Is Research-to-Essay?

This skill transforms research into polished essays through a systematic 6-phase methodology:
- **Multi-source synthesis** with thematic clustering
- **Citation management** with source credibility hierarchy
- **Voice calibration** across multiple registers
- **Platform-specific formatting** (Substack, LinkedIn, Academic)
- **Quality assurance** with structural and evidence checks

## Use Cases

- **Substack/LinkedIn posts** requiring research and synthesis
- **Long-form essays** combining multiple sources with narrative arc
- **Academic writing** with proper citation and methodology
- **Executive briefs** distilling complex research into actionable insights
- **"Research and write about [topic]"** requests
- **Publication-grade content** with proper attribution

## Core Features

### 6-Phase Methodology

**Phase 1: Intake & Planning**
- Format target selection (Substack, LinkedIn, Academic, Executive Brief)
- Essay structure selection (Persuasive, Exploratory, Diagnostic, Narrative-Conceptual, Synthesis)
- Voice profile calibration (Poetic Rigor, Professional Signal, Scholarly Precision, Surgical Clarity)

**Phase 2: Research Execution**
- Source credibility hierarchy (Tiers 1-4: Primary → Expert Analysis → Informed Commentary → Weak Sources)
- Systematic search strategy prioritizing primary sources
- Citation extraction with claim tagging
- Quality requirements by essay type (5-12 sources minimum)

**Phase 3: Synthesis**
- Manual thematic clustering for simple essays
- Python script-assisted synthesis for complex multi-source work
- Convergent/divergent claim identification
- Gap analysis

**Phase 4: Drafting**
- Template-based structure (essay-template.md, linkedin-template.md)
- Source integration (not listing)
- Progressive depth building
- Voice profile application

**Phase 5: Refinement**
- Structural review (hook, stakes, section logic, conclusion)
- Voice & style check (anti-cliché patterns)
- Evidence & citation verification
- Platform-specific polish

**Phase 6: Delivery**
- Complete essay with metadata
- Source list with credibility tiers
- Optional: Alternative versions, further reading, visual suggestions

### Essay Structures

- **Persuasive**: Claim → Evidence → Counter-argument → Resolution
- **Exploratory**: Question → Multiple perspectives → Synthesis
- **Diagnostic**: Problem → Root cause → Solution space
- **Narrative-Conceptual**: Story → Pattern → Framework
- **Synthesis**: Theme → Sources → Integration → Implications

### Voice Profiles

- **Poetic Rigor**: Lyrical + precise, embodied language, sensory detail
- **Professional Signal**: Clear + authoritative, no fluff, data-driven
- **Scholarly Precision**: Formal + rigorous, evidence-based, nuanced
- **Surgical Clarity**: Minimal + direct, active voice, concrete examples

### Source Credibility Hierarchy

**Tier 1 (Primary)**: Research papers, official data, technical docs
**Tier 2 (Expert Analysis)**: Domain specialists, academic reviews, investigative journalism
**Tier 3 (Informed Commentary)**: Practitioner Substacks, conference talks
**Tier 4 (Weak)**: Social media speculation, content marketing, AI-generated farms

## Installation

### For Claude Code

```bash
# Personal skills (globally available)
cp -r ResearchToEssay/research-to-essay ~/.claude/skills/

# Project skills (project-specific)
mkdir -p .claude/skills
cp -r ResearchToEssay/research-to-essay .claude/skills/
```

### For Claude Web Chat

Download [`research-to-essay-v1.0.0.skill`](dist/research-to-essay-v1.0.0.skill) from the `dist/` folder and upload directly to any Claude conversation.

## Quick Start

### Research and Write

```
"Research and write a 2000-word Substack post about AI safety governance using the Exploratory structure"
```

Claude will:
1. Conduct systematic research across credibility tiers
2. Synthesize sources thematically
3. Draft with chosen structure and voice
4. Apply refinement checks
5. Deliver with source list and metadata

### Create LinkedIn Post

```
"Research distributed systems patterns and create a LinkedIn post (250 words, Professional Signal voice)"
```

Claude will optimize for platform conventions (paragraph breaks, bolding, CTA).

### Academic Essay

```
"Write an academic essay analyzing the impacts of remote work on organizational culture. Use Scholarly Precision voice with full citations."
```

Claude will apply formal citation style, methodology transparency, and limitations notes.

## Usage Examples

### Specifying Essay Structure

```
"Use the Diagnostic structure: identify why companies struggle with AI adoption, analyze root causes, map solution space"
```

### Voice Calibration

```
"Write this in Poetic Rigor voice - I want it lyrical but precise, with sensory details"
```

### Source Constraints

```
"Only use Tier 1 and Tier 2 sources - primary research and expert analysis only"
```

### Platform Formatting

```
"Create both a Substack long-form version (2500 words) and a LinkedIn teaser (200 words)"
```

## Advanced Features

### Python Synthesis Script

For complex essays with 8+ sources:

```python
# Create sources.json with required format
python scripts/synthesize_sources.py sources.json output.md
```

Generates thematic map showing:
- Core themes with supporting sources
- Convergent evidence (agreement)
- Divergent claims (tensions)
- Gaps or under-supported areas

### Quality Checks

**Structural Review Checklist:**
- Hook is genuinely compelling
- Stakes established early
- Each section advances argument necessarily
- Conclusion reframes rather than summarizes
- Length appropriate to format

**Evidence & Citation Check:**
- Every major claim has warrant
- Primary sources for factual claims
- Counter-arguments acknowledged
- No citation decay
- Links functional

## Structure

```
ResearchToEssay/
├── README.md                           # This file
├── Chat Patterns to Essay.skill        # Packaged skill file
└── research-to-essay/                  # Main skill directory
    ├── SKILL.md                        # Skill definition
    ├── references/
    │   ├── essay-structures.md         # 5 essay arc patterns
    │   ├── research-patterns.md        # Source quality & search strategy
    │   └── voice-profiles.md           # 4 voice characteristics
    ├── assets/
    │   ├── essay-template.md           # Substack/long-form template
    │   └── linkedin-template.md        # LinkedIn post template
    └── scripts/
        └── synthesize_sources.py       # Multi-source thematic clustering
```

## Quality Signals

**High-quality output:**
- Opens with genuine insight, not preamble
- Every paragraph necessary, no filler
- Sources integrated into argument, not appended
- Counter-arguments acknowledged, not buried
- Conclusion offers new lens, not recap
- Voice consistent and appropriate
- Citations complete and properly tiered
- Length justified by complexity

**Red flags:**
- Generic opening ("In today's world...")
- List structure when narrative needed
- No complexity acknowledgment
- All sources from same perspective
- Summary conclusion
- Inconsistent tone
- Weak/missing citations
- Excessive length without depth

## Anti-Patterns to Avoid

- Don't search once and write - iterate research based on draft gaps
- Don't list sources separately - integrate naturally
- Don't write intro first - write it last
- Don't ignore voice profile constraints - they prevent AI slop
- Don't cite weak sources when primary available - tier matters
- Don't pad length artificially - every paragraph must earn its keep
- Don't summarize in conclusion - reframe or extrapolate

## Reference Files

**When Claude loads these files:**

- `essay-structures.md` - When uncertain about narrative arc or need structure template
- `research-patterns.md` - When evaluating source quality or planning research strategy
- `voice-profiles.md` - When clarifying voice characteristics or checking forbidden patterns
- `synthesize_sources.py` - When dealing with 8+ sources requiring systematic clustering

## Contributing

Contributions welcome! Consider adding:
- Additional essay structures
- New voice profiles for different domains
- Platform-specific templates (Medium, Dev.to, etc.)
- Enhanced synthesis algorithms
- Citation style templates

---

Built with Claude Code Skills | Research-Driven Writing
