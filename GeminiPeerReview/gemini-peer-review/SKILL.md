---
name: gemini-peer-review
description: [CLAUDE CODE ONLY] Leverage Gemini CLI for AI peer review, second opinions on architecture and design decisions, cross-validation of implementations, security analysis, alternative approaches, and holistic codebase analysis. Requires terminal access to execute Gemini CLI commands. Use when making high-stakes decisions, reviewing complex architecture, analyzing large codebases (1M token context window), or when explicitly requested for a second AI perspective. Must be explicitly invoked using skill syntax.
license: Complete terms in LICENSE.txt
environment: claude-code
---

# Gemini Peer Review - AI Collaboration Skill

🖥️ **Claude Code Only** - Requires terminal access to execute Gemini CLI commands.

Enable Claude Code to leverage Google's Gemini CLI for collaborative AI reasoning, peer review, and multi-perspective analysis of code architecture, design decisions, and implementations.

---

## 🛡️ Fidelity Firewall (Degraded Mode) — READ FIRST, NON-NEGOTIABLE

**You may report ONLY what the `gemini` CLI actually returned in THIS session.**

The entire value of this skill is that a *second, independent AI* really weighed in. A fabricated Gemini opinion is worse than no second opinion — it manufactures false confidence and corrupts every downstream decision. Treat inventing a Gemini view as a critical integrity failure, not a stylistic shortcut.

**Hard rules:**

1. **No run, no quote.** Before you write *any* of "Gemini said / Gemini agrees / Gemini found / Gemini's 1M-context analysis revealed / Gemini suggests" — you MUST have actually executed a `gemini ...` command in this session and seen real output in the tool result. If you did not run it, you may not attribute anything to Gemini. Period.

2. **Quote or faithfully summarize real output only.** Attribution must be traceable to actual returned text. Never paraphrase-from-imagination, embellish, "fill in what Gemini would probably say," or upgrade a thin response into a confident one. If Gemini was terse, represent it as terse.

3. **Degraded mode is the safe default.** If the `gemini` CLI is **absent, not installed, errors, times out, returns empty / whitespace / an error blob, or returns nothing usable** — you MUST:
   - State plainly: **"Second opinion unavailable — gemini CLI not available / errored."** (Name the actual reason: not installed, auth failure, timeout, empty response, rate-limited, etc.)
   - Proceed **Claude-only**, and label that analysis as single-perspective.
   - Do **NOT** fabricate a Gemini opinion, a quote, a "Gemini agrees," or a false consensus to fill the gap.

4. **No synthetic consensus.** "Both Claude and Gemini agree…" is permitted **only** when Gemini genuinely ran and genuinely returned an aligned view. One AI is not two. If only Claude ran, there is no agreement to report.

5. **Verification gate before any synthesis section.** Before producing the "Perspective Comparison / Synthesis" output, self-check: *Did I run `gemini` this session? Do I have its real output in front of me?* If either answer is no, skip the two-perspective framing entirely and deliver an honest Claude-only result with the unavailability note.

**Honest degraded-mode template (use verbatim when Gemini is unavailable):**

```
⚠️ Second opinion unavailable — gemini CLI not available / errored.
Reason: [not installed | auth failed | timeout | empty/unusable response | rate-limited | other: ...]

Proceeding with Claude-only analysis (single perspective — not independently cross-validated):
[Claude's analysis...]
```

If you catch yourself about to write a Gemini perspective you cannot trace to a real command output in this session, **stop and switch to the degraded-mode template instead.**

---

## Core Philosophy

**Two AI perspectives are better than one for high-stakes decisions.**

This skill enables strategic collaboration between Claude Code (Anthropic) and Gemini (Google) for architecture validation, design cross-validation, alternative approach generation, security/performance/testing analysis, and learning from different AI reasoning patterns.

**Not a replacement—a second opinion.** Gemini's massive 1M token context window allows it to process entire codebases without chunking, providing holistic analysis that complements Claude's detailed reasoning.

---

## When to Use

**DO use when:** high-stakes architecture decisions; choosing between significant design alternatives; security-critical code; complex refactoring plans; unfamiliar domains/patterns; user explicitly requests a second opinion; significant disagreement about approach; performance-critical optimization; testing strategy validation; large codebases requiring massive context; multimodal analysis needed (diagrams, PDFs, designs).

**DON'T use when:** simple/straightforward implementations; already confident in a singular approach; time-sensitive quick fixes; no significant trade-offs; low-impact tactical changes; Gemini CLI is unavailable.

### How to Invoke This Skill

**This skill requires explicit invocation.** It is not automatically triggered by natural language.

```
skill: "gemini-peer-review"
```

**User phrases that indicate this skill would be valuable:** "Get a second opinion on...", "What would Gemini think about...", "Review this architecture with Gemini", "Use Gemini to validate this approach", "Are there better alternatives to...", "Security review with Gemini needed", "Analyze the entire codebase with Gemini", "Review this architecture diagram with Gemini." When these appear, suggest the skill and invoke it explicitly if appropriate.

---

### Codex vs Gemini: Which Peer Review Skill?

Both provide valuable second opinions but excel in different scenarios.

**Use Gemini Peer Review when:**
- Code size > 5k LOC (large codebase analysis)
- Need full codebase context (up to 1M tokens)
- Reviewing architecture across multiple modules
- Analyzing diagrams + code together (multimodal)
- Want research-grounded recommendations (current best practices)
- Cross-module security analysis (attack surface mapping)
- Systemic performance patterns / design consistency checking

**Use Codex Peer Review when:**
- Code size < 500 LOC (focused reviews)
- Need precise, line-level bug detection
- Want fast analysis with concise output
- Reviewing single modules or functions
- Need tactical implementation feedback
- Performance bottleneck identification (specific issues)
- Quick validation of design decisions

**For mid-range codebases (500-5k LOC):**
- Use **Gemini** if: cross-module patterns, holistic view, diagram analysis, research grounding
- Use **Codex** if: focused review, single module, speed priority, specific bugs
- Consider **Both** for: critical decisions requiring maximum confidence

**For maximum value on high-stakes decisions:** use both skills sequentially and apply the synthesis framework (see `references/synthesis-framework.md`).

---

## Core Workflow

### 1. Recognize Need for Peer Review

Assess if peer review adds value. Consider: Is this high-stakes with significant impact? Are there multiple valid approaches? Is the architecture complex/unfamiliar? Does it involve security, performance, or scalability? Did the user request a second opinion? Would Gemini's 1M context or multimodal capability help? **If yes to 2+:** proceed.

### 2. Prepare Context for Gemini

Identify the core question, extract relevant code (with 1M tokens you can include entire modules/services), provide project context and constraints, frame specific questions, set output expectations, and include multimodal assets (diagrams, PDFs) when relevant.

See `references/context-preparation.md` for detailed guidance, domain-specific templates, code-extraction strategies, and a context-prep checklist.

**Context structure template:**
```
[CONTEXT]      Project type/purpose/stack; current situation; constraints; scale
[CODE/ARCH]    Relevant code or architecture (can be extensive — 1M context)
[ASSETS]       If applicable: diagrams, mockups, specs
[QUESTION]     Specific question or review request
[OUTPUT]       Desired format: analysis, alternatives, recommendations, etc.
```

### 3. Invoke Gemini CLI

See `references/gemini-commands.md` for the complete command reference, flags, and patterns.

**Non-interactive review (recommended) — stdin pipe for multi-line:**
```bash
cat <<'EOF' | gemini
[prepared context and question here]
EOF
```

**Positional prompt / with multimodal:**
```bash
gemini "Review this code for issues" @./src/auth/
gemini "Analyze this architecture diagram: [question]" @architecture.png
```

**Key flags:**
- Positional prompt: `gemini "your prompt"` (non-interactive)
- Stdin pipe: `cat prompt.txt | gemini` (multi-line prompts)
- `--output-format`: text/json/stream-json
- `--yolo`/`-y`: auto-approve (avoid for review); `--sandbox`/`-s`: safe execution
- File references: `@file_path` or `@directory/` to include context

**Note:** The `-p`/`--prompt` flag is deprecated. Use positional prompts or stdin pipe. Don't hardcode `--model` — let the CLI use its default (latest) model.

**Error handling (governed by the Fidelity Firewall above):**
- CLI not installed → inform user, point to installation in `references/gemini-commands.md`, proceed Claude-only via the degraded-mode template. Do NOT invent a Gemini opinion.
- Rate limit / timeout / error → state the actual reason, note "second opinion unavailable," proceed Claude-only. No fabricated consensus.
- Unclear or empty response → reformulate and retry **once**. If still unusable, treat as unavailable and represent it honestly.

### 4. Synthesize Perspectives

Compare and integrate both perspectives across: agreement (shared concerns → confidence), divergence (differing assumptions → trade-offs), complementary insights (what each saw the other missed), trade-off identification, and actionable insight extraction.

See `references/synthesis-framework.md` for the full methodology, output-structure template, presentation-language patterns, and worked examples. Note Gemini-unique value: cross-module patterns from larger context, multimodal insights, Search-grounded best practices.

### 5. Present Balanced Analysis

Be transparent about which AI said what, acknowledge disagreements honestly, don't force false consensus, explain each perspective's reasoning, indicate confidence levels, and highlight insights unique to Gemini (large context, multimodal).

> **Firewall reminder:** Every "Gemini" statement is permitted ONLY if Gemini actually ran this session and returned real output. If it did not, drop the two-perspective framing and use the degraded-mode template above.

Presentation-language patterns (align / diverge / one-found-issues / unique-capability) live in `references/synthesis-framework.md`.

---

## Use Case Patterns

Detailed processes, templates, and worked examples for each scenario are in `references/use-case-patterns.md`:

1. **Architecture Review** — system design before major implementation
2. **Design Decision Validation** — choosing between implementation approaches
3. **Security Review** — vulnerabilities, attack vectors, hardening
4. **Performance Analysis** — bottlenecks and optimization
5. **Testing Strategy** — coverage gaps and quality
6. **Code Review & Learning** — understanding unfamiliar code/patterns
7. **Alternative Approach Generation** — when stuck or exploring better options
8. **Large Codebase Analysis** — holistic architecture of big codebases (Gemini's sweet spot, 1M context)
9. **Multimodal Technical Review** — design specs/diagrams vs. implementation (Gemini-unique)

---

## Command & Setup Reference

See `references/gemini-commands.md` for installation, authentication (OAuth / API key / Vertex AI), interactive and non-interactive modes, slash/`@`/`!` commands, output formats, session management, error handling, CI/CD and pre-commit integration, and quick-reference tables.

**Quick lookup:**

| Use Case | Command Pattern |
|----------|----------------|
| Simple review | `gemini "Review this code for issues"` |
| Review with diagram | `gemini "Analyze this architecture" @diagram.png` |
| Multi-line prompt | `cat <<'EOF' \| gemini` ... `EOF` |
| Include file context | `gemini "Review" @./src/auth/` |
| JSON output | `gemini --output-format json "..."` |

**Install (npm, requires Node 20+):** `npm install -g @google/gemini-cli` then `gemini --version`. Authenticate via `gemini` (OAuth) or `export GEMINI_API_KEY=...`. Free tier: 60 req/min, 1,000 req/day, latest 1M-context model.

---

## Quality Signals

**Valuable when:** both perspectives identify the same concerns (high confidence); perspectives are complementary; trade-offs become clearer; non-obvious alternatives emerge; security/performance concerns are independently validated; Gemini's holistic view reveals patterns not apparent in isolation; multimodal analysis adds visual-structural insight.

**Needs refinement when:** responses are vague/generic; the question wasn't specific enough; context was insufficient; both perspectives state the obvious; no new insights emerge; Gemini misunderstands the question. → **Action:** reformulate with better context and specificity (see `references/context-preparation.md`).

**Skip when:** Gemini unavailable and blocking progress; decision is time-sensitive and low-risk; approach is straightforward with no trade-offs; user doesn't value a second opinion here; quota exhausted.

---

## Best Practices

**DO:** frame specific, answerable questions; provide sufficient context; reserve for high-stakes decisions; leverage the 1M context for large codebases; include diagrams/design docs (multimodal); be transparent about attribution; acknowledge and explain disagreements; synthesize rather than concatenate.

**DON'T:** use for every trivial decision; ask vague questions without context; force false consensus; hide which AI said what; present peer review as authoritative truth; waste the large context window on tiny snippets; send sensitive/proprietary code without considering that it goes to Google's cloud.

Detailed question-framing examples and context do's/don'ts are in `references/context-preparation.md`.

---

## Limitations & Considerations

- Requires Gemini CLI installation and authentication; subject to Google API rate limits; cloud-based (code sent to Google servers); no offline mode; response time varies with context size; needs Node.js 20+.
- Neither AI is objectively "correct" — both offer perspectives; user judgment is the ultimate arbiter. Peer review adds time; over-reliance slows decisions. Consider data privacy before sending code externally.

**When to trust which:** *Convergence* increases confidence (shared concerns are likely real). *Divergence* reveals trade-offs and differing priorities (valuable information). *Specialized knowledge* — Gemini excels at holistic large-codebase and multimodal analysis; Claude excels at detailed step-by-step reasoning and native Claude Code integration with no external data exposure.

---

## Reference Files

- `references/context-preparation.md` — what to include, question framing, domain templates, code-extraction strategies, context checklist, common mistakes.
- `references/gemini-commands.md` — complete CLI command/flag reference, installation, authentication, error handling, CI/CD and pre-commit integration.
- `references/synthesis-framework.md` — synthesis methodology, output-structure template, presentation-language patterns, trade-off matrices, worked examples.
- `references/use-case-patterns.md` — detailed processes and worked examples for all 9 use-case patterns.
- `references/example-workflows.md` — four end-to-end peer-review scenarios (architecture decision, security review, large-codebase analysis, multimodal design-to-implementation).

---

**End of Skill Guide.** For setup and API reference, see `references/gemini-commands.md`.
