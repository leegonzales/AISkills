# Codex Peer Review

**Version:** 1.0.0
**License:** MIT
**Author:** Claude Code AI Skills Collection

🖥️ **Claude Code Only** - This skill requires terminal access to execute Codex CLI commands.

Enable Claude Code to leverage OpenAI's Codex CLI for AI peer review, second opinions on architecture and design decisions, cross-validation of implementations, and multi-perspective analysis.

---

## Overview

**Two AI perspectives are better than one for high-stakes decisions.**

The Codex Peer Review skill enables strategic collaboration between Claude Code (Anthropic) and Codex CLI (OpenAI) for:

- **Architecture validation** - Get independent validation of system designs
- **Design decision cross-validation** - Compare approaches from two AI perspectives
- **Security review** - Identify vulnerabilities with complementary analysis
- **Performance optimization** - Find bottlenecks from different analytical angles
- **Alternative approach generation** - Discover creative solutions through multi-perspective reasoning
- **Code review & learning** - Understand complex code with explanations from two AIs

This isn't about replacing Claude Code's capabilities—it's about adding a second opinion when it matters most.

---

## Why Use Peer Review?

### When Two Perspectives Add Value

**Architecture decisions** are complex with subtle trade-offs. Different AI training and reasoning approaches can reveal:
- Concerns you might not initially see
- Trade-offs that become clearer through different lenses
- Alternative approaches worth considering
- Validation when both perspectives align

**High-stakes decisions** benefit from independent validation:
- Security-critical code
- Performance-critical optimization
- Scalability architecture
- Technology selection

### Real-World Example

**Scenario:** Designing multi-tenant SaaS database strategy

**Claude's Analysis:** Recommends shared database with row-level security, prioritizing operational simplicity and team expertise.

**Codex's Analysis:** Recommends separate databases per tenant, prioritizing data isolation guarantees and tenant independence.

**Value:** The divergence reveals a fundamental trade-off between operational complexity and isolation strength. Neither is "wrong"—the right choice depends on your context (compliance requirements, operational capacity, tenant characteristics).

**Result:** Make an informed decision understanding the trade-offs from both perspectives.

---

## Features

### Core Capabilities

**Architecture Review**
- System design validation
- Scalability assessment
- Failure mode analysis
- Alternative architecture suggestions

**Design Decision Validation**
- Compare multiple approaches
- Explicit trade-off analysis
- Context-dependent recommendations
- Risk assessment from two perspectives

**Security Review**
- Vulnerability identification
- Attack vector analysis
- Security best practices validation
- Complementary security insights

**Performance Analysis**
- Bottleneck identification
- Optimization recommendations
- Performance vs complexity trade-offs
- Algorithmic improvements

**Testing Strategy**
- Coverage gap identification
- Edge case discovery
- Test quality improvements
- Testing approach validation

**Code Review & Learning**
- Pattern identification
- Design rationale explanation
- Potential improvements
- Learning from existing code

---

## Installation

### Prerequisites

**1. Codex CLI** must be installed to use this skill.

#### Install Codex CLI

```bash
# Via npm
npm i -g @openai/codex

# Via Homebrew
brew install openai/codex/codex
```

#### Authenticate

```bash
# Sign in with ChatGPT Plus/Pro/Business/Edu/Enterprise account
codex auth login

# Or provide API key
codex auth api-key [your-api-key]
```

#### Verify Installation

```bash
# Check installation
codex --version

# Verify authentication
codex /status
```

**Official Documentation:** [Codex CLI](https://developers.openai.com/codex/cli/)

---

### Install Skill for Claude Code

Skills are automatically discovered from your skills directories.

#### Personal Skills (Available Globally)

```bash
cd ~/.claude/skills/
git clone https://github.com/leegonzales/AISkills.git temp-aiskills
cp -r temp-aiskills/CodexPeerReview/codex-peer-review ./
rm -rf temp-aiskills
```

#### Project Skills (Project-Specific)

```bash
cd your-project/
mkdir -p .claude/skills
git clone https://github.com/leegonzales/AISkills.git temp-aiskills
cp -r temp-aiskills/CodexPeerReview/codex-peer-review .claude/skills/
rm -rf temp-aiskills
```

**Documentation:** [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)

---

### ⚠️ Not Available for Claude Web Chat

**This skill requires Claude Code** with terminal access to execute Codex CLI commands. It cannot function in Claude web chat's sandboxed browser environment.

**Why it doesn't work on web:**
- Cannot execute bash/terminal commands
- Cannot access locally installed CLI tools like Codex
- Requires system-level command execution

**Use Claude Code instead** where terminal access is available.

---

## Quick Start

### Basic Usage

Once installed, Claude Code will automatically use the skill when appropriate. You can also explicitly request peer review:

```
"Get a second opinion on this architecture"
"Review this code with Codex for security issues"
"What would Codex think about this design?"
"Validate this approach with peer review"
```

### Example Workflow

**1. You're designing a caching strategy:**

```
User: "I'm choosing between Redis with TTL-based invalidation and event-driven cache invalidation for our product catalog. What do you recommend?"

Claude Code: Let me analyze both approaches and get Codex's perspective as well.

[Claude analyzes]
[Invokes Codex peer review]
[Synthesizes both perspectives]

Claude Code: Here's the analysis from both perspectives:

**Claude's Analysis:** Recommends Redis + TTL, prioritizing implementation simplicity...
**Codex's Analysis:** Recommends event-driven, prioritizing data freshness...

The divergence reveals a trade-off between implementation complexity and data freshness.

[Provides decision framework based on context]
```

**2. Security review before deployment:**

```
User: "Review this JWT authentication implementation for security issues before we deploy."

Claude Code: I'll review this for security concerns and get Codex's perspective as well.

[Claude performs security analysis]
[Invokes Codex security review]
[Synthesizes findings]

Claude Code: Both perspectives identified critical issues:

**Convergent Findings (High Confidence):**
- Both: Refresh token rotation missing
- Both: Tokens in localStorage (XSS risk)

**Complementary Insights:**
- Codex: Identified race condition in multi-tab refresh
- Claude: Emphasized monitoring and detection gaps

[Provides prioritized remediation plan]
```

---

## Use Cases

### 1. Architecture Review

**When:** Designing new systems or major refactoring

**Example:**
```
"Review my microservices architecture. I'm using separate databases per service with event-driven communication. What are the scalability and consistency concerns?"
```

**Value:** Independent validation of architectural decisions, identification of failure modes, alternative approaches

---

### 2. Design Decision Validation

**When:** Choosing between multiple implementation approaches

**Example:**
```
"Should I use server-side rendering or client-side rendering for this dashboard? Consider performance, SEO, and development complexity."
```

**Value:** Structured trade-off analysis, context-dependent recommendations from two perspectives

---

### 3. Security Review

**When:** Before deploying security-critical code

**Example:**
```
"Security review this authentication flow. Focus on token handling, session management, and potential attack vectors."
```

**Value:** Vulnerability identification from two analytical perspectives, comprehensive attack vector analysis

---

### 4. Performance Optimization

**When:** Optimizing performance-critical code

**Example:**
```
"This API endpoint is averaging 500ms but needs to be under 100ms. What are the bottlenecks and how should I optimize?"
```

**Value:** Bottleneck identification, prioritized optimization recommendations with impact estimates

---

### 5. Testing Strategy

**When:** Improving test coverage and quality

**Example:**
```
"Review our testing strategy for this authentication service. What coverage gaps exist and what edge cases are we missing?"
```

**Value:** Coverage gap identification, edge case discovery from two perspectives

---

### 6. Code Review & Learning

**When:** Understanding unfamiliar code or patterns

**Example:**
```
"Explain this recursive backtracking algorithm. What pattern is being used and are there better alternatives?"
```

**Value:** Multi-perspective explanations, pattern identification, learning from different analytical approaches

---

## How It Works

### The Peer Review Process

**1. Recognition**
- Claude Code identifies scenarios where peer review adds value
- User explicitly requests second opinion
- High-stakes decision with significant trade-offs

**2. Preparation**
- Extract relevant code or architecture
- Structure context clearly
- Frame specific questions
- Set output expectations

**3. Codex Invocation**
- Execute Codex CLI with prepared context
- Use appropriate command flags
- Handle responses and errors

**4. Synthesis**
- Compare Claude's and Codex's analyses
- Identify agreement (increases confidence)
- Identify divergence (reveals trade-offs)
- Extract complementary insights
- Build unified recommendations

**5. Presentation**
- Transparent about which AI said what
- Acknowledge disagreements honestly
- Provide decision framework
- Indicate confidence levels
- Give actionable recommendations

### Example Synthesis

```markdown
## Perspective Comparison

**Claude's Analysis:**
Recommends shared database with row-level security for operational simplicity.

**Codex's Analysis:**
Recommends separate databases for strongest data isolation.

**Points of Agreement:**
- Data isolation is critical concern
- PostgreSQL is appropriate technology
- Decision has long-term operational implications

**Points of Divergence:**
- Claude prioritizes operational simplicity
- Codex prioritizes security guarantees
- Reveals trade-off between complexity and isolation

## Synthesis & Recommendation

Start with shared database + RLS, build capability to migrate tenants to dedicated databases later. This:
- Matches team capability (Claude's concern)
- Provides migration path to stronger isolation (Codex's concern)
- Pragmatic evolution strategy (synthesis)

**Confidence:** High - Both perspectives agree on fundamentals, differ on timing and risk tolerance.
```

---

## Documentation

### Comprehensive Guides

The skill includes detailed reference documentation:

**[SKILL.md](codex-peer-review/SKILL.md)**
- Complete skill definition and workflow
- When to use vs when not to use
- Synthesis and presentation patterns
- Integration with Claude Code

**[Context Preparation Guide](codex-peer-review/references/context-preparation.md)**
- How to structure context effectively
- Templates for different scenarios
- Common preparation mistakes
- Context size management

**[Codex Commands Reference](codex-peer-review/references/codex-commands.md)**
- Complete command reference
- Flags and options
- Command patterns for peer review
- Error handling and retry strategies

**[Synthesis Framework](codex-peer-review/references/synthesis-framework.md)**
- How to synthesize two AI perspectives
- Agreement and divergence analysis
- Trade-off identification patterns
- Synthesis quality signals

**[Use Case Patterns](codex-peer-review/references/use-case-patterns.md)**
- Detailed patterns for each use case
- Process for each scenario
- Example syntheses
- Expected outcomes

**[Prompt Templates](codex-peer-review/assets/prompt-templates.md)**
- Ready-to-use templates
- Architecture, security, performance reviews
- Design decisions, testing strategy
- Customization guidance

---

## Configuration

### Optional Codex CLI Configuration

Create `~/.codex/config.toml` for custom defaults:

```toml
# Recommended peer review settings
model = "codex-1"
ask_for_approval = "suggest"
sandbox = "workspace-read"
quiet = true
output_format = "text"
```

### Project Context

Create `codex.md` in your project root for project-specific context:

```markdown
# Project: Your Project Name

## Architecture
[High-level architecture description]

## Code Style
[Coding conventions]

## Key Decisions
[Important architectural decisions]
```

Codex automatically reads this for context.

---

## Best Practices

### When to Use Peer Review

**DO use for:**
- High-stakes architecture decisions
- Security-critical code review
- Complex design trade-offs
- Performance-critical optimization
- Learning from unfamiliar code
- Validation of significant decisions

**DON'T use for:**
- Every trivial decision
- Simple, straightforward implementations
- Time-sensitive quick fixes
- Low-impact tactical changes
- When Codex CLI unavailable

### Effective Context Preparation

**Good context:**
- Focused on specific decision
- Clear question
- Relevant code/architecture only
- Explicit constraints
- Expected output format stated

**Poor context:**
- Vague question ("Is this good?")
- Entire codebase dump
- Missing constraints
- No focus area

### Synthesis Quality

**High-quality synthesis:**
- Clearly distinguishes what each AI said
- Explains why perspectives differ
- Makes trade-offs explicit
- Provides actionable recommendations
- Indicates confidence appropriately

**Poor synthesis:**
- Concatenates without integration
- Forces false consensus
- Hides which AI said what
- Vague recommendations

---

## Limitations & Considerations

### Technical Limitations

- Requires Codex CLI installation and authentication
- Subject to OpenAI API rate limits
- Different context windows and capabilities than Claude
- Sequential analysis (not real-time collaboration)
- Response quality depends on prompt clarity

### Philosophical Considerations

- Neither AI is objectively "correct"—both offer perspectives
- User judgment is ultimate arbiter
- Peer review adds time to workflow
- Over-reliance can slow decision-making
- Different training data → different perspectives

### When to Trust Which Perspective

**Trust convergence:** When both AIs agree, confidence increases

**Trust divergence:** Reveals important trade-offs, neither necessarily "right"

**Trust specialized knowledge:** Consider which AI's reasoning aligns better with your context

---

## Troubleshooting

### Codex CLI Not Found

**Problem:** `codex: command not found`

**Solution:** Install Codex CLI:
```bash
npm i -g @openai/codex
# or
brew install openai/codex/codex
```

---

### Authentication Errors

**Problem:** `Authentication required`

**Solution:**
```bash
codex auth login
# or
codex auth api-key [your-api-key]
```

---

### Rate Limit Exceeded

**Problem:** `Rate limit exceeded`

**Solution:**
- Check rate limit status: `/status` in interactive mode
- Wait for rate limit reset
- Upgrade plan if needed
- Batch reviews to stay within limits

---

### Unclear or Generic Responses

**Problem:** Codex response is too vague

**Solution:**
- Provide more specific context
- Narrow the question focus
- Add explicit constraints
- Specify expected output format
- See [Context Preparation Guide](codex-peer-review/references/context-preparation.md)

---

## Examples

### Example 1: Architecture Decision

**Prompt:**
```
I'm designing a multi-tenant SaaS architecture. Should I use separate databases per tenant or shared database with row-level security? Consider operational complexity, data isolation, and team expertise (we know PostgreSQL well).
```

**Result:**
- Claude analyzes both approaches
- Invokes Codex for second opinion
- Synthesizes perspectives
- Reveals trade-off between operational simplicity and isolation strength
- Provides decision framework based on context
- Recommends phased approach

---

### Example 2: Security Review

**Prompt:**
```
Security review this JWT authentication implementation before production. Focus on token handling, refresh tokens, and session management.
```

**Result:**
- Claude performs security analysis
- Codex provides independent security review
- Both identify refresh token issues (high confidence)
- Codex finds race condition (complementary insight)
- Claude emphasizes monitoring gaps (complementary insight)
- Prioritized remediation plan combining both perspectives

---

## FAQ

**Q: Does this replace Claude Code's capabilities?**
A: No. This adds a second opinion for high-stakes decisions where different perspectives add value.

**Q: When should I use peer review vs just Claude Code?**
A: Use peer review for complex architecture decisions, security-critical code, significant design trade-offs, and when explicitly wanting a second perspective. Skip for simple, straightforward tasks.

**Q: What if Claude and Codex disagree?**
A: Disagreement is valuable—it reveals trade-offs and different priorities. The synthesis explains why they differ and provides a decision framework based on your context.

**Q: Does this cost extra?**
A: Codex CLI requires OpenAI API access (ChatGPT Plus/Pro or API key). Each peer review uses Codex API calls.

**Q: Can I use this without Codex CLI?**
A: No, the skill requires Codex CLI. Claude will inform you if it's not available and continue with Claude-only analysis.

**Q: How do I know when to trust which AI?**
A: When perspectives converge, confidence increases. When they diverge, consider which reasoning aligns better with your context. The synthesis explains the trade-offs to help you decide.

---

## Version History

### v1.0.0 (2025-11-12)
- Initial release
- Architecture review, design decisions, security, performance, testing, learning use cases
- Comprehensive synthesis framework
- Complete documentation and templates
- Ready-to-use prompt templates

---

## Contributing

Contributions welcome! To improve this skill:

1. Fork the repository
2. Add improvements or new use case patterns
3. Update documentation
4. Test with real scenarios
5. Submit pull request

---

## Resources

### Documentation
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Codex CLI Documentation](https://developers.openai.com/codex/cli/)

### Related Skills
- [Concept Forge](../ConceptForge/) - Dialectical concept development
- [Claimify](../Claimify/) - Argument structure analysis
- [Process Mapper](../ProcessMapper/) - Workflow documentation

---

## License

MIT License - See [LICENSE](LICENSE.txt) for details.

---

## Support

**Issues or Questions:**
- Open an issue in this repository
- Check [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)
- Review [comprehensive guides](codex-peer-review/references/) in this skill

**Codex CLI Issues:**
- Consult [Codex CLI documentation](https://developers.openai.com/codex/cli/)
- Check OpenAI developer forums

---

**Version:** 1.0.0 | **Last Updated:** 2025-11-12 | Built with Claude Code

*Two AI perspectives are better than one for decisions that matter.*
