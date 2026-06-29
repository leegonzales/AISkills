---
name: codex-peer-review
description: [CLAUDE CODE ONLY] Leverage Codex CLI for AI peer review, second opinions on architecture and design decisions, cross-validation of implementations, security analysis, and alternative approach generation. Requires terminal access to execute Codex CLI commands. Use when making high-stakes decisions, reviewing complex architecture, or when explicitly requested for a second AI perspective. Must be explicitly invoked using skill syntax.
license: Complete terms in LICENSE.txt
environment: claude-code
---

# Codex Peer Review Skill

🖥️ **Claude Code Only** - Requires terminal access to execute Codex CLI commands.

Enable Claude Code to leverage OpenAI's Codex CLI for collaborative AI reasoning, peer review, and multi-perspective analysis of code architecture, design decisions, and implementations.

**Core philosophy:** Two AI perspectives are better than one for high-stakes decisions. This is a second opinion (Claude + Codex), **not a replacement** for Claude's analysis or the user's judgment.

---

## When to Use Codex Peer Review

**DO use when:**
- Making high-stakes architecture decisions
- Choosing between significant design alternatives
- Reviewing security-critical code
- Validating complex refactoring plans
- Exploring unfamiliar domains or patterns
- User explicitly requests a second opinion
- Significant disagreement about approach
- Performance-critical optimization or testing-strategy decisions

**DON'T use when:**
- Simple, straightforward implementations
- Already confident in a singular approach
- Time-sensitive quick fixes
- No significant trade-offs exist
- Low-impact tactical changes
- Codex CLI is not available/installed

### How to Invoke This Skill

**This skill requires explicit invocation.** It is not automatically triggered by natural language. Claude must explicitly invoke it using:

```
skill: "codex-peer-review"
```

**User phrases that indicate this skill is valuable:** "Get a second opinion on...", "What would Codex think about...", "Review this architecture with Codex", "Use Codex to validate this approach", "Are there better alternatives to...", "Get Codex peer review for this", "Security review with Codex needed", "Ask Codex about this design." When these appear, suggest the skill and invoke it explicitly if appropriate.

### Codex vs Gemini: Which Peer Review Skill?

**Use Codex** when: code < 500 LOC, focused/single-module reviews, precise line-level bug detection, fast concise output, tactical implementation feedback, quick validation.

**Use Gemini** when: code > 5k LOC, need full-codebase context (up to 1M tokens), cross-module architecture/security analysis, multimodal (diagram + code), research-grounded recommendations.

**Mid-range (500–5k LOC):** Codex for focused/single-module/speed/specific-bugs; Gemini for cross-module/holistic/diagram/research grounding. Use **both** for maximum confidence on critical decisions, then apply `references/synthesis-framework.md`.

---

## Core Workflow

### 1. Recognize need for peer review
Assess value: high-stakes decision? multiple valid approaches? complex/unfamiliar architecture? security/performance/scalability concerns? user requested it? If yes to 2+ → proceed.

### 2. Prepare context for Codex
Extract focused, relevant code (not the whole codebase), state project type/constraints/concerns, frame a specific question, and set output expectations. Detailed templates per scenario: load `references/context-preparation.md`.

Quick structure:
```
[CONTEXT]    Project type/purpose, current situation, constraints
[CODE/ARCHITECTURE]    relevant code or architecture description
[QUESTION]    specific question or review request
[EXPECTED OUTPUT]    format: analysis, alternatives, recommendations, etc.
```

### 3. Invoke Codex CLI
Full command/flag/config reference: load `references/codex-commands.md`.

**Non-interactive review (recommended):**
```bash
cat <<'EOF' | codex exec
[prepared context and question here]
EOF
```

Other patterns:
```bash
codex exec "Review this code for security issues"        # simple one-line
codex --image architecture-diagram.png "Analyze this"    # review with diagram
codex --sandbox read-only "..."                          # safe analysis (recommended)
```

**Key flags:** `exec` (non-interactive, streams to stdout) · `--image`/`-i` (attach diagrams/screenshots) · `--sandbox read-only|workspace-write|danger-full-access` · `--full-auto` (unattended, use with caution).

**Error handling:** If Codex CLI not installed → inform user, give install instructions (below), continue Claude-only. If rate-limited → note limitation, proceed Claude-only. If response unclear → reformulate with more context and retry once.

### 4. Synthesize perspectives
Detailed framework, templates, and worked examples: load `references/synthesis-framework.md`.

Compare and integrate both perspectives along: **Agreement** (where they align → confidence), **Disagreement** (where/why they diverge), **Complementary insights** (what each saw the other missed), **Trade-offs** (revealed by each lens), **Actionable insights** (key alternatives and risks). Produce an integrated recommendation with rationale, confidence level, and remaining considerations — not a side-by-side concatenation.

### 5. Present balanced analysis
Be transparent about which AI said what; acknowledge disagreements honestly; don't force false consensus; indicate confidence appropriately; give the user enough context to decide. (Transparency phrasing patterns are in `references/synthesis-framework.md`.)

---

## Use Case Patterns

Each pattern below has a full worked process + example in `references/use-case-patterns.md`. The shape is the same: document the situation → prepare context → ask Codex a specific question → synthesize → present.

1. **Architecture Review** — "Review this architecture for scalability, maintainability, and potential issues."
2. **Design Decision Validation** — "Compare approaches A/B/C for [criteria]; which is recommended and what are the trade-offs?"
3. **Security Review** — "Identify vulnerabilities, attack vectors, and hardening opportunities."
4. **Performance Analysis** — "Identify bottlenecks and prioritized optimization opportunities."
5. **Testing Strategy** — "Review testing strategy; find coverage gaps and missing edge cases."
6. **Code Review & Learning** — "Explain this code: patterns, design decisions, potential concerns."
7. **Alternative Approach Generation** — "Generate alternative approaches to [problem]."

---

## Installation Requirements

**Codex CLI must be installed.** (Full command/config/error reference: `references/codex-commands.md`.)

```bash
npm i -g @openai/codex            # or: brew install openai/codex/codex
codex auth login                   # or: codex auth api-key [your-api-key]
codex --version && codex login status   # verify
```

If unavailable: inform the user peer review requires Codex CLI, provide install instructions, and continue with Claude-only analysis (note the second opinion isn't available).

**Config** (optional, `~/.codex/config.toml`): recommend `sandbox = "read-only"` and `ask_for_approval = "suggest"`. Don't hardcode model names — let Codex CLI use its default (latest) model.

---

## Integration Points

- **`concept-forge`:** forge architectural concepts → validate with Codex peer review.
- **`prose-polish`:** polish ADRs / technical docs produced from a review.
- **`claimify`:** map architectural arguments and decision rationale.
- **Claude Code workflows:** use pre-implementation (validate before building), post-implementation (cross-check results), and during implementation (when stuck/uncertain).

---

## Reference Files

- **`references/codex-commands.md`** — Complete Codex CLI command/flag reference, config files (`config.toml`, `codex.md`, `AGENTS.md`, global instructions), per-scenario command patterns, error handling, advanced patterns (chaining, parallel, CI/CD), and quick-reference table.
- **`references/context-preparation.md`** — Principles of effective context, per-scenario context templates, question-framing patterns, code-extraction strategies, output-expectation setting, and context-size management.
- **`references/synthesis-framework.md`** — Full synthesis process and templates, synthesis patterns (convergent/complementary/divergent), quality signals, transparency practices, and common synthesis mistakes/anti-patterns.
- **`references/use-case-patterns.md`** — Detailed worked processes and Claude+Codex synthesis examples for all 7 use-case patterns (architecture, design decision, security, performance, testing, learning, alternatives).
