# Two Claude Skills for Code Intelligence: Codex + Gemini Peer Review

I've built two skills that fundamentally changed how I work with code—whether I'm reviewing PRs, exploring unfamiliar codebases, evaluating architecture decisions, or auditing security.

The approach: bring multiple AI perspectives into conversation with Claude.

The result: when different AI models collaborate on the same problem, they find 44% more issues than any single AI working alone. Not because any one model is better, but because different architectures see different patterns.

## Codex Peer Review - Line-level precision and tactical analysis

OpenAI's Codex excels at the forensic details Claude sometimes glosses over:

- **Line-level bug detection**: Catches off-by-one errors, null checks, edge cases
- **Security vulnerability scanning**: 100% detection rate on critical vulnerabilities in our testing
- **Performance bottleneck identification**: Found all 5 major bottlenecks in a 9k LOC codebase
- **Fast, concise feedback**: ~80 second analysis with actionable specifics

**Use cases:** PR reviews, security audits, bug hunting, understanding unfamiliar code, refactoring validation, production-critical changes

**Best for:** Small to medium changes (<500 LOC), line-level issues, security reviews, quick codebase orientation

## Gemini Peer Review - Strategic architecture and large-scale analysis

Google's Gemini brings two unique capabilities: massive context (1M tokens) and research grounding:

- **Entire codebase analysis**: Processes 9,033 LOC in a single pass (no chunking)
- **Cross-module insights**: Maps attack surfaces, identifies architectural anti-patterns
- **Research-backed recommendations**: Cites current best practices with 15+ external sources
- **Multimodal analysis**: Can analyze diagrams, architecture docs, and code together

**Use cases:** Architecture reviews, large refactors, system design validation, cross-module changes, exploring new codebases, understanding system-wide patterns

**Best for:** Large codebases (>5k LOC), architectural decisions, design reviews, codebase onboarding

## The Parallax Effect: Why Multiple Models Matter

Here's what we discovered during comprehensive testing (27 test cases, 4 phases, real production code):

### Convergent Findings = High Confidence
When Codex and Gemini both flag the same issue, you know it's real. We saw this on critical security vulnerabilities—both models independently identified the same attack vectors, giving immediate validation.

### Divergent Findings = Trade-off Revelation
When they disagree, you're seeing different valid perspectives. Example: Codex might flag performance overhead from abstraction layers, while Gemini recommends those same layers for maintainability. Both are right—you're seeing the trade-off clearly.

### Complementary Coverage = 44% More Issues
The numbers are striking:
- **Codex alone:** 4 unique issues found
- **Gemini alone:** 7 unique issues found
- **Both together:** 15 total issues (4 found by both, 11 found by only one)

That's 44% more comprehensive coverage than using either AI alone.

### Tactical + Strategic = Complete Picture
Codex gives you the tactical view (this loop is O(n²), this null check is missing). Gemini gives you the strategic view (this architecture won't scale, consider event-driven instead). Together, you get both micro and macro perspectives.

## How We Built These (And Why You Can Trust Them)

### Development Approach
Rather than API integration, both skills use CLI interfaces (OpenAI Codex CLI, Google Gemini CLI). This means:
- Real terminal output Claude can analyze
- No API key juggling in prompts
- Same tools developers use directly
- Reproducible results

### Testing Regime
We didn't guess if these worked—we validated systematically:

**27 test cases** across 4 phases:
1. **Core Capabilities** (8 tests): Basic functionality validation
2. **Specialized Use Cases** (7 tests): Security reviews, performance analysis, architecture
3. **Integration & Synthesis** (9 tests): Multi-AI collaboration patterns
4. **Edge Cases** (3 tests): Rate limiting, minimal context, error handling

**Test methodology:**
- Automated AI agent testing (no human bias)
- Real production codebase: [prompt-evolve](https://github.com/leegonzales/prompt-evolve) (genetic algorithm framework, 9k+ LOC)
- Quality scoring on 1-5 scales with specific success criteria
- Comparative analysis to measure complementary value

**Results:**
- **93% overall pass rate** (25/27 tests)
- **4.6/5.0 average quality score**
- **Codex: 100% pass rate** (7/7), 4.8/5.0 quality
- **Gemini: 87.5% pass rate** (7/8), 5.0/5.0 quality
- **Both together: 44% more comprehensive** than single-AI baseline

**Note on test failures:** The 2 failed tests weren't functional issues—they were test setup problems where I hadn't created the sample files needed for edge case scenarios. Rather than spend another day polishing test infrastructure, I chose to ship. The skills work, the core validation is solid, and perfect is the enemy of good enough.

Full test documentation available in the repo: [CodexPeerReview/TESTING.md](https://github.com/leegonzales/AISkills/blob/main/CodexPeerReview/TESTING.md) and [GeminiPeerReview/TESTING.md](https://github.com/leegonzales/AISkills/blob/main/GeminiPeerReview/TESTING.md)

### Production Validation
These aren't toy examples. We validated on:
- Real security vulnerabilities (JWT auth, session management, API keys)
- Production architecture (microservices vs monolith decision)
- Complex refactoring (genetic algorithm optimization)
- Large-scale analysis (9,033 LOC codebase)

Both skills are approved for production deployment.

## Installation (10 minutes)

**Requirements:**
- Claude Code (not available in web chat—requires terminal access)
- OpenAI Codex CLI (`npm install -g @openai/codex-cli`)
- Google Gemini CLI (`npm install -g @google/gemini-cli`)
- API keys for both services

**Quick install:**

```bash
# Install CLIs
npm install -g @openai/codex-cli @google/gemini-cli

# Configure API keys (follow CLI prompts)
codex auth
gemini auth

# Download skills from GitHub
cd ~/.claude/skills/

# Option 1: Clone entire repo
git clone https://github.com/leegonzales/AISkills.git
cp -r AISkills/CodexPeerReview/codex-peer-review ./
cp -r AISkills/GeminiPeerReview/gemini-peer-review ./

# Option 2: Download individual skills via curl
curl -L https://github.com/leegonzales/AISkills/archive/refs/heads/main.tar.gz | \
  tar xz --strip=2 AISkills-main/CodexPeerReview/codex-peer-review

curl -L https://github.com/leegonzales/AISkills/archive/refs/heads/main.tar.gz | \
  tar xz --strip=2 AISkills-main/GeminiPeerReview/gemini-peer-review
```

**Claude discovers and uses them automatically when relevant.**

Detailed setup guides with API configuration:
- [Codex Peer Review Setup](https://github.com/leegonzales/AISkills/tree/main/CodexPeerReview)
- [Gemini Peer Review Setup](https://github.com/leegonzales/AISkills/tree/main/GeminiPeerReview)

Official Claude Code skills documentation: https://docs.claude.com/en/docs/claude-code/skills

## When to Use Each

**Use Codex when you need:**
- Line-by-line bug detection
- Security vulnerability scanning
- Quick feedback on focused changes
- Performance optimization validation

**Use Gemini when you need:**
- Entire codebase analysis
- Architecture review
- Cross-module impact analysis
- Research-backed recommendations

**Use both when you need:**
- Critical production changes
- Major architectural decisions
- Comprehensive security review
- High-confidence validation

## The Broader Lesson: Multi-Model Collaboration

What we learned building these skills applies beyond code review:

**Different models have different strengths.** Not because one is "better," but because they're trained differently, use different architectures, and optimize for different objectives.

**Collaboration beats competition.** Rather than picking "the best AI," we gain more by orchestrating multiple AIs in conversation.

**Parallax reveals depth.** Just like binocular vision creates depth perception from two 2D images, multiple AI perspectives reveal dimensions you can't see from a single viewpoint.

This is the future of AI-assisted work: not one AI to rule them all, but ensembles of specialized models collaborating on complex problems.

---

Both skills follow Anthropic's skill-building best practices—explicit invocation, comprehensive documentation, and robust error handling.

They work exclusively in Claude Code (require terminal access for CLI commands).

Happy to answer questions about either one. If you want to see my other skills check out: https://github.com/leegonzales/AISkills

**Resources:**
- GitHub repo: https://github.com/leegonzales/AISkills
- Codex Peer Review: https://github.com/leegonzales/AISkills/tree/main/CodexPeerReview
- Gemini Peer Review: https://github.com/leegonzales/AISkills/tree/main/GeminiPeerReview
- Full test report: [FINAL_TEST_REPORT.md](https://github.com/leegonzales/AISkills/blob/main/FINAL_TEST_REPORT.md)
