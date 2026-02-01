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

# Pipe from clipboard
pbpaste | fabric -p <pattern>

# Scrape URL and process
fabric -u "https://example.com" -p <pattern>

# YouTube transcript
fabric -y "https://youtube.com/watch?v=..." -p <pattern>

# YouTube with timestamps
fabric -y "URL" --transcript-with-timestamps -p <pattern>

# YouTube comments instead of transcript
fabric -y "URL" --comments -p <pattern>
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

---

## Execution Guidelines

### Content Size
- **Short text** (< 500 words): Pipe directly via `echo`
- **Medium text** (500-5000 words): Write to temp file, pipe via `cat`
- **Long text** (> 5000 words): Write to temp file, pipe via `cat`, consider streaming (`-s`)
- **URLs/YouTube**: Use built-in `-u` or `-y` flags (no manual scraping needed)

### Error Handling
- If fabric returns empty output, check: is the pattern installed? Run `fabric -l | grep <pattern>`
- If patterns are outdated, run `fabric -U` to update
- If a model isn't available, try `fabric -L` to list available models

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
5. **Temp files for large content** — Write content to `/tmp/fabric_input.md` rather than huge echo statements
6. **Update periodically** — If a pattern seems missing, run `fabric -U`
