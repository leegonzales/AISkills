# Quality Standards

Evaluation criteria and quality standards for AISkills collection.

## Quality Tiers

| Tier | Score | Action |
|------|-------|--------|
| Exceptional | 85-100 | Integrate immediately |
| Strong | 70-84 | Copy and improve |
| Moderate | 50-69 | Consider for future |
| Low Priority | <50 | Pass |

**All skills in this collection should score 85+**

## Evaluation Categories (100 points)

### Core Value (25 pts)
- **Unique Purpose (10):** Solves specific problem not addressed elsewhere
- **Applicability (10):** Multiple practical use cases
- **Execution (5):** Works reliably, quality outputs

### Documentation (20 pts)
- **README (8):** Complete with purpose, features, installation, examples
- **Installation (4):** Clear instructions for Claude Code
- **Examples (8):** Multiple detailed usage examples

### Technical Structure (20 pts)
- **Organization (8):** Professional structure (skill-slug/, references/)
- **SKILL.md (8):** Concise, focused, well-structured
- **Assets (4):** Includes references/, examples/, scripts/

### Production Ready (15 pts)
- **Versioning (5):** Semantic versioning, CHANGELOG.md
- **Testing (5):** Documented validation results
- **Error Handling (5):** Robust, documented limitations

### Ecosystem Fit (10 pts)
- **Complementarity (5):** Fills gap or enhances existing skills
- **Integration (5):** Works with Claude Code tools

### Innovation (10 pts)
- **Novel Approach (5):** Unique methodology or framework
- **Design (5):** Best practices, progressive disclosure

## Red Flags (Automatic Disqualification)

- No license or restrictive license
- Security concerns
- Abandoned (12+ months no updates)
- Requires paid services without free tier
- Violates Claude usage policies

## Quick Quality Check

Before submitting a skill, verify:

- [ ] Unique value - not duplicate of existing skill
- [ ] SKILL.md under 400 lines (use references/)
- [ ] README with installation and examples
- [ ] CHANGELOG.md with version history
- [ ] Validates without errors
- [ ] Tested with real usage

## Benchmark Skills

Use these as quality references:

| Skill | Est. Score | Strengths |
|-------|------------|-----------|
| Prose Polish | 100 | Perfect docs, research-backed, unique |
| Gemini Peer Review | 97 | Exceptional capability, proven testing |
| Codex Peer Review | 95 | Unique capability, comprehensive docs |
| Claimify | 92 | Strong unique value, great structure |

## Improvement Checklist

For skills scoring below 85:

**Documentation gaps:**
- [ ] Add installation section to README
- [ ] Add 3+ usage examples
- [ ] Document limitations

**Structure issues:**
- [ ] Move verbose content to references/
- [ ] Add CHANGELOG.md
- [ ] Standardize directory naming

**Production readiness:**
- [ ] Add validation testing
- [ ] Document error cases
- [ ] Package with SkillPackager

## Full Rubric

For detailed scoring criteria, see `docs/skill-evaluation-rubric.md`.
