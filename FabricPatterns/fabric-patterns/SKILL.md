---
name: fabric-patterns
description: Run danielmiessler/fabric CLI patterns for content analysis, extraction, summarization, writing, security analysis, and more. Use when user asks to "use fabric," "run a pattern," "extract wisdom," "summarize with fabric," or when piping content through AI patterns would be more effective than inline processing. Triggers include "fabric," "pattern," "extract wisdom," "summarize this article," "analyze this threat report," or any reference to a specific fabric pattern name.
environment: claude-code
---

# Fabric Patterns Skill

Run [danielmiessler/fabric](https://github.com/danielmiessler/fabric) patterns from Claude Code to process content through specialized AI prompts.

## Overview

Fabric is a CLI tool with 240+ curated AI patterns for analysis, extraction, summarization, writing, and security tasks. This skill enables Claude to select and execute the right pattern, pipe content correctly, and integrate results back into the conversation.

**Fabric binary:** `$HOME/go/bin/fabric` (aliased as `fabric`)

---

## When to Use Fabric

### DO use when:
- Processing long-form content (articles, transcripts, papers) through structured extraction
- User explicitly requests a fabric pattern
- YouTube video summarization or transcript analysis
- Spotify podcast summarization
- URL scraping + pattern processing
- Security analysis (threat models, incident reports, malware analysis)
- Content needs structured output that a specific pattern produces better than freeform
- Chaining multiple extraction/analysis passes on the same content

### DON'T use when:
- Simple questions Claude can answer directly
- Short content that doesn't benefit from pattern structure
- User needs conversational back-and-forth (fabric is one-shot)
- Real-time code editing or debugging (use Claude's native tools)

---

## Pattern Selection Protocol

**Always use the dual-judgment approach for pattern selection:**

### Step 1: Claude's Pick
Based on the user's intent and the pattern catalog (load `references/pattern-catalog.md`), select the most appropriate pattern.

### Step 2: Fabric's Pick
Run fabric's own meta-pattern to get a second opinion:

```bash
echo "<describe the user's task here>" | fabric -p suggest_pattern
```

### Step 3: Compare and Decide
- **Both agree** → High confidence. Run the pattern.
- **They disagree** → Evaluate both suggestions. Consider:
  - Which pattern's output format better matches what the user needs?
  - Is one pattern more specific to the domain?
  - When in doubt, briefly tell the user both options and which you recommend.

### Skip dual-judgment when:
- User explicitly names a pattern (e.g., "run extract_wisdom on this")
- Task is unambiguous (e.g., YouTube URL + "summarize" → `summarize`)
- Re-running or chaining a pattern the user already approved

---

## Core Commands Reference

Load `references/piping-idioms.md` for the complete reference. Key patterns:

### Input Methods

```bash
# Pipe text content
echo "content here" | fabric -p <pattern>

# Pipe from file
cat /path/to/file.md | fabric -p <pattern>

# Pipe from clipboard (macOS)
pbpaste | fabric -p <pattern>

# Scrape URL and process
fabric -u "https://example.com" -p <pattern>

# YouTube transcript
fabric -y "https://youtube.com/watch?v=..." -p <pattern>

# YouTube with timestamps
fabric -y "URL" --transcript-with-timestamps -p <pattern>

# YouTube comments instead of transcript
fabric -y "URL" --comments -p <pattern>

# Spotify podcast
fabric --spotify="https://open.spotify.com/episode/..." -p <pattern>
```

### Output Methods

```bash
# Stream to terminal (preferred for long output)
cat file.md | fabric -s -p <pattern>

# Save to file
cat file.md | fabric -p <pattern> -o output.md

# Copy to clipboard
cat file.md | fabric -p <pattern> -c

# Chain patterns (pipe output of one into another)
cat file.md | fabric -p extract_wisdom | fabric -p summarize
```

### Model and Options

```bash
# Use specific model
fabric -p <pattern> -m claude-opus-4-5-20251101

# Set temperature
fabric -p <pattern> -t 0.3

# Use a context
fabric -p <pattern> -C <context_name>

# Use a session (persistent conversation)
fabric -p <pattern> --session=my_session

# Enable web search (Anthropic, OpenAI, Gemini)
fabric -p <pattern> --search

# Enable thinking/reasoning
fabric -p <pattern> --thinking=high

# Use a reasoning strategy (layered on top of pattern)
fabric -p <pattern> --strategy=cot        # Chain-of-Thought
fabric -p <pattern> --strategy=tot        # Tree-of-Thought
fabric -p <pattern> --strategy=reflexion  # Reflect and improve

# Dry run (show what would be sent)
fabric -p <pattern> --dry-run
```

### Management

```bash
# List all patterns
fabric -l

# List available models
fabric -L

# Update patterns to latest
fabric -U

# Change default model
fabric -d
```

---

## Pattern Categories Quick Reference

Full catalog in `references/pattern-catalog.md`. High-value patterns by use case:

### Content Processing
| Pattern | Best For |
|---------|----------|
| `extract_wisdom` | Deep extraction of ideas, insights, quotes from any content |
| `extract_insights` | Focused insight extraction (16-word format) |
| `extract_article_wisdom` | Article-specific structured extraction |
| `summarize` | 20-word summary + key points + takeaways |
| `summarize_micro` | Ultra-short 20-word summary with 3 bullets |
| `create_5_sentence_summary` | Multi-depth summary (5 sentences → 1 word) |

### Analysis
| Pattern | Best For |
|---------|----------|
| `analyze_claims` | Fact-checking and evidence evaluation |
| `analyze_paper` | Academic paper rigor assessment |
| `analyze_prose` | Writing quality evaluation |
| `analyze_debate` | Argument analysis and scoring |
| `find_logical_fallacies` | Formal/informal fallacy detection |
| `label_and_rate` | Content tagging + quality rating (S-D tier) |

### Writing & Creation
| Pattern | Best For |
|---------|----------|
| `improve_writing` | Grammar, style, clarity refinement |
| `improve_prompt` | LLM prompt optimization |
| `write_essay` | Essay composition in specified style |
| `write_micro_essay` | Brief illuminating essays |
| `create_keynote` | TED-style presentation generation |
| `humanize` | Making AI text sound natural |

### Security
| Pattern | Best For |
|---------|----------|
| `create_threat_model` | Threat modeling from descriptions |
| `create_stride_threat_model` | STRIDE-specific threat models |
| `analyze_incident` | Cybersecurity breach analysis |
| `analyze_malware` | Malware indicator extraction |
| `analyze_threat_report` | Threat intel extraction |
| `create_sigma_rules` | Detection rule generation |

### Development
| Pattern | Best For |
|---------|----------|
| `explain_code` | Code explanation and documentation |
| `review_design` | Architecture review |
| `create_git_diff_commit` | Commit message generation |
| `write_pull-request` | PR description drafting |
| `summarize_git_diff` | Git change summarization |

### YouTube & Media
| Pattern | Best For |
|---------|----------|
| `extract_wisdom` | General video insight extraction |
| `create_video_chapters` | Timestamp + topic extraction |
| `youtube_summary` | Timestamped video summary |
| `summarize_lecture` | Academic lecture extraction |

### Research & Thinking
| Pattern | Best For |
|---------|----------|
| `dialog_with_socrates` | Deep Socratic questioning |
| `analyze_mistakes` | Cognitive error mapping |
| `create_better_frame` | Reframing perspectives |
| `solve_with_cot` | Chain-of-thought problem solving |

### Reasoning Strategies — Escalation Framework

Strategies are meta-prompts layered on top of any pattern via `--strategy=<name>`. Use this decision guide:

**Default: No strategy (standard)**
Use for straightforward tasks where the pattern alone is sufficient.

**Escalate to `--strategy=cot` when:**
- Task requires step-by-step reasoning or logical deduction
- Analyzing complex arguments or multi-part problems
- Debugging or tracing through code logic

**Escalate to `--strategy=tot` when:**
- Task is generative or creative (brainstorming, novel solutions)
- Multiple valid approaches exist and you need to explore them
- Problem has no obvious single path

**Escalate to `--strategy=reflexion` when:**
- First result was shallow, superficial, or missed the point
- User says "go deeper" or "that's not quite right"
- Self-improvement pass is likely to catch errors

**Other strategies (use when specifically appropriate):**

| Strategy | Effect |
|----------|--------|
| `cod` | Chain-of-Density — iterative compression (good for summarization refinement) |
| `self-refine` | Iterative self-improvement |
| `self-consistent` | Multiple resolution paths, pick best (good for math/logic) |
| `aot` | Agent-over-Tree — multi-agent collaboration |
| `ltm` | Long-Term Memory — build and reference memory |

**Heuristic:** Start without a strategy. If the output disappoints, re-run with `cot`. If still lacking, try `reflexion`. Reserve `tot` for genuinely open-ended problems.

---

## Autonomous Context Management

Fabric contexts let you inject persistent project-specific context into any pattern call. Manage them proactively.

### Check Existing Contexts

```bash
fabric -x  # List all contexts (--listcontexts)
```

### Create a Context for a Project

When working on a project, create a context file so fabric understands the codebase:

```bash
# Summarize the project and save as a context
cat ~/Projects/myproject/README.md | fabric -p summarize > ~/.config/fabric/contexts/myproject.md

# Or manually create a concise project description
cat > ~/.config/fabric/contexts/myproject.md << 'EOF'
Project: myproject
Language: Python 3.12
Framework: FastAPI
Description: REST API for invoice processing
Key patterns: Domain-driven design, event sourcing
EOF
```

### Apply Contexts Automatically

When running fabric commands related to a known project, always attach the context:

```bash
cat code.py | fabric -p explain_code -C myproject
cat design.md | fabric -p review_design -C myproject
```

**Workflow:** At the start of a session involving a project, check if a context exists (`fabric -x | grep <project>`). If not, create one from the README or key files. Then attach `-C <project>` to all relevant fabric calls.

### Other Context/Session Commands

```bash
fabric -X                    # List all sessions (--listsessions)
fabric --printcontext=<name> # Print a context
fabric --printsession=<name> # Print a session
fabric -w <name>             # Wipe a context
fabric -W <name>             # Wipe a session
```

---

## Creating Temporary Patterns

When no existing pattern fits the user's need, create a custom one on the fly.

**Note:** Fabric's `-p` flag takes a pattern *name*, not a file path. Custom patterns must be placed in the patterns directory.

### Workflow

1. **Create a temporary pattern directory:**

```bash
PATTERN_NAME="tmp_$(date +%s)"
mkdir -p ~/.config/fabric/patterns/$PATTERN_NAME
cat > ~/.config/fabric/patterns/$PATTERN_NAME/system.md << 'PATTERN'
# IDENTITY and PURPOSE
You are an expert at [specific task]. Your job is to [specific goal].

# STEPS
- [Step 1]
- [Step 2]

# OUTPUT INSTRUCTIONS
- Output in [format]
- [Constraints]
PATTERN
```

2. **Run it:**

```bash
echo "input" | fabric -p $PATTERN_NAME
```

3. **If the user finds it useful**, offer to rename it permanently:

```bash
mv ~/.config/fabric/patterns/$PATTERN_NAME ~/.config/fabric/patterns/meaningful_name
```

4. **Clean up unused temp patterns** when done:

```bash
rm -rf ~/.config/fabric/patterns/tmp_*
```

---

## Execution Guidelines

### Content Size
- **Short text** (< 500 words): Pipe directly via `echo`
- **Medium text** (500-5000 words): Write to temp file, pipe via `cat`
- **Long text** (> 5000 words): Write to temp file, pipe via `cat`, consider streaming (`-s`)
- **URLs/YouTube**: Use built-in `-u` or `-y` flags (no manual scraping needed)

### Self-Healing Pattern Knowledge

Fabric's pattern catalog evolves. Prefer live queries over static assumptions:

- **First use in a session:** Consider running `fabric -U` to ensure patterns are current
- **Pattern not found?** Self-diagnose: `fabric -l | grep <pattern>` — the name may have changed
- **Inspect a pattern directly:** `cat ~/.config/fabric/patterns/<pattern>/system.md` to understand what it actually does
- **Prefer `fabric --help`** and live inspection over relying solely on the static reference files in this skill
- **Management commands:** `fabric -x` (list contexts), `fabric -X` (list sessions), `fabric --liststrategies` (list strategies)

### Robust Error Recovery Protocol

When a fabric command fails, follow this numbered sequence:

1. **Syntax check** — Is the command well-formed? Check flags and quoting.
2. **Pattern existence check** — `fabric -l | grep <pattern>` — does the pattern exist?
3. **Dry run** — `fabric -p <pattern> --dry-run` with the actual input to see what would be sent.
4. **Model check** — `fabric -L` — is the model available? Try a different model with `-m`.
5. **Update patterns** — `fabric -U` — maybe the pattern was added/renamed recently.
6. **Strategy escalation** — If output is empty/poor, re-run with `--strategy=cot` or `--strategy=reflexion`.
7. **API failure notification** — If the provider API is down or rate-limited, inform the user and suggest trying a different vendor/model (`-V` flag).

**Never silently swallow errors.** Always tell the user what went wrong and what you tried.

### Session Management
- Use `--session=<name>` when the user wants multi-turn fabric conversations
- Sessions persist context between calls
- Use `-C <context>` for pre-defined context (like project descriptions)

### Output Integration
- After running fabric, present the output to the user clearly
- If the output is long, summarize the key findings and offer to show the full output
- When chaining patterns, show intermediate results if useful

---

## Best Practices

1. **Show the command** — Before running fabric, briefly state which pattern you're using and why
2. **Stream long output** — Use `-s` for patterns that produce substantial output
3. **Respect the pattern's format** — Don't reformat fabric output unless the user asks
4. **Chain thoughtfully** — `extract_wisdom | summarize` is a common power combo
5. **Temp files for large content** — Write content to a temporary file using `mktemp` rather than huge echo statements
6. **Update periodically** — If a pattern seems missing, run `fabric -U`
