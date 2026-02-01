# Fabric Piping Idioms & CLI Reference

Complete reference for constructing fabric CLI commands.

---

## Input Methods

### Pipe from stdin
```bash
# Short text — echo directly
echo "Your content here" | fabric -p <pattern>

# Multi-line text — heredoc
cat <<'EOF' | fabric -p <pattern>
Your multi-line
content here
EOF

# From file
cat /path/to/file.md | fabric -p <pattern>

# From clipboard (macOS)
pbpaste | fabric -p <pattern>

# From another command
git diff | fabric -p summarize_git_diff
git log --oneline -20 | fabric -p summarize_git_changes
curl -s https://api.example.com/data | fabric -p extract_insights
```

### Built-in Fetchers (no pipe needed)
```bash
# URL scraping via Jina AI
fabric -u "https://example.com/article" -p extract_wisdom

# URL with search question
fabric -q "What is quantum computing?" -p summarize

# YouTube transcript (default)
fabric -y "https://youtube.com/watch?v=VIDEO_ID" -p extract_wisdom

# YouTube with timestamps
fabric -y "URL" --transcript-with-timestamps -p create_video_chapters

# YouTube comments
fabric -y "URL" --comments -p analyze_comments

# YouTube metadata only
fabric -y "URL" --metadata

# YouTube playlist
fabric -y "URL" --playlist -p summarize

# Spotify podcast
fabric --spotify="https://open.spotify.com/episode/..." -p summarize

# Audio/video transcription
fabric --transcribe-file=/path/to/audio.mp3 -p summarize
```

### HTML Processing
```bash
# Convert HTML to readable text, then process
cat page.html | fabric --readability -p summarize

# Pipe raw HTML with readability filter
curl -s https://example.com | fabric --readability -p extract_wisdom
```

---

## Output Methods

### Terminal Output
```bash
# Standard (buffered)
cat file.md | fabric -p <pattern>

# Streaming (real-time, preferred for long output)
cat file.md | fabric -s -p <pattern>
```

### File Output
```bash
# Save to specific file
cat file.md | fabric -p extract_wisdom -o wisdom.md

# Save full session to file
cat file.md | fabric -p <pattern> --session=my_session --output-session -o session_log.md
```

### Clipboard
```bash
# Copy result to clipboard (macOS)
cat file.md | fabric -p summarize -c
```

### Chaining Patterns
```bash
# Extract then summarize
cat article.md | fabric -p extract_wisdom | fabric -p summarize

# Analyze then improve
cat essay.md | fabric -p analyze_prose | fabric -p improve_writing

# Extract insights then create flashcards
cat textbook.md | fabric -p extract_insights | fabric -p to_flashcards

# YouTube → extract → summarize
fabric -y "URL" -p extract_wisdom | fabric -p create_micro_summary
```

---

## Model Selection

```bash
# Use specific model
fabric -p <pattern> -m claude-opus-4-5-20251101
fabric -p <pattern> -m gpt-4o
fabric -p <pattern> -m gemini-2.0-flash

# Use specific vendor (for ambiguous model names)
fabric -p <pattern> -V "LM Studio" -m openai/gpt-oss-20b

# List available models
fabric -L

# Change default model
fabric -d
```

---

## Advanced Options

### Temperature & Sampling
```bash
fabric -p <pattern> -t 0.3          # Low temp (factual/analytical)
fabric -p <pattern> -t 0.9          # High temp (creative)
fabric -p <pattern> -T 0.5          # Top-P sampling
fabric -p <pattern> -r              # Raw mode (model defaults, no overrides)
```

### Thinking / Reasoning
```bash
fabric -p <pattern> --thinking=high    # Enable deep reasoning
fabric -p <pattern> --thinking=off     # Disable thinking
fabric -p <pattern> --suppress-think   # Run thinking but hide it from output
```

### Reasoning Strategies
```bash
# Layer a reasoning strategy on top of any pattern
fabric -p <pattern> --strategy=cot            # Chain-of-Thought
fabric -p <pattern> --strategy=tot            # Tree-of-Thought
fabric -p <pattern> --strategy=cod            # Chain-of-Density
fabric -p <pattern> --strategy=reflexion      # Reflect and improve
fabric -p <pattern> --strategy=self-refine    # Iterative self-improvement
fabric -p <pattern> --strategy=self-consistent # Multiple paths, pick best
fabric -p <pattern> --strategy=aot            # Agent-over-Tree
fabric -p <pattern> --strategy=ltm            # Long-Term Memory
fabric -p <pattern> --strategy=standard       # No special prompting (default)

# Combine with thinking for maximum reasoning depth
fabric -p analyze_paper --strategy=tot --thinking=high
```

### Web Search
```bash
fabric -p <pattern> --search                              # Enable web search
fabric -p <pattern> --search --search-location="America/Denver"  # With location
```

### Sessions & Context
```bash
# Named session (persists conversation)
fabric -p <pattern> --session=project_review

# Pre-defined context
fabric -p <pattern> -C my_project_context

# Print session contents
fabric --printsession=project_review

# Wipe session
fabric -W project_review
```

### Variables
```bash
# Pass variables to patterns that use them
fabric -p <pattern> -v="#role:security engineer" -v="#points:30"

# Apply variables to user input too
echo "content" | fabric -p <pattern> --input-has-vars
```

### Image Generation
```bash
# Generate image from pattern output
fabric -p create_art_prompt --image-file=output.png
fabric -p <pattern> --image-size=1024x1024 --image-quality=high
```

### Audio / TTS
```bash
# Text-to-speech output
fabric -p <pattern> --voice=Kore
fabric --list-gemini-voices    # List available voices
```

### Attachments
```bash
# Send image for analysis
fabric -p <pattern> -a /path/to/image.png

# Send URL as attachment
fabric -p <pattern> -a "https://example.com/image.jpg"
```

### Debugging
```bash
# Dry run (show what would be sent)
cat file.md | fabric -p <pattern> --dry-run

# Debug output
fabric -p <pattern> --debug=1    # Basic
fabric -p <pattern> --debug=2    # Detailed
fabric -p <pattern> --debug=3    # Trace

# Show metadata
fabric -p <pattern> --show-metadata
```

---

## Common Power Combos

```bash
# Deep article analysis
fabric -u "URL" -p extract_wisdom -s

# YouTube study notes
fabric -y "URL" -p extract_wisdom | fabric -p to_flashcards -o flashcards.md

# Security threat modeling
cat system_description.md | fabric -p create_stride_threat_model -o threat_model.md

# Code change summary
git diff main..HEAD | fabric -p summarize_git_diff -s

# Meeting notes processing
cat meeting_transcript.txt | fabric -p summarize_meeting -o meeting_notes.md

# Research paper analysis
pdftotext paper.pdf - | fabric -p analyze_paper -s

# Content quality rating
cat blog_post.md | fabric -p rate_content

# Prompt improvement
echo "Summarize this article for me" | fabric -p improve_prompt
```

---

## Pattern Management

```bash
# List all installed patterns
fabric -l

# Update patterns to latest
fabric -U

# Get help on which pattern to use
echo "I want to analyze a security incident report" | fabric -p suggest_pattern

# Show a pattern's system prompt (for understanding what it does)
cat ~/.config/fabric/patterns/<pattern_name>/system.md
```
