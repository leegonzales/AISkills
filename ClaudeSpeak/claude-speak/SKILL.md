---
name: claude-speak
description: Speak text aloud using high-quality AI voice synthesis (Kokoro TTS on Apple Silicon). Use when user asks to vocalize, narrate, or speak text out loud.
---

# Claude Speak

Vocalize text using high-quality text-to-speech. British male voice (bm_george) by default.

## When to Use

Invoke when user:
- Asks to "say this out loud" or "speak this"
- Wants narration or audio feedback
- Uses `/speak` command
- Requests vocalization of content

## Core Command

```bash
~/Projects/claude-speak/.venv/bin/claude-speak-client "Text to speak"
```

**That's it.** The daemon runs in background via launchd - instant response.

## Options

```bash
# Different voice
~/Projects/claude-speak/.venv/bin/claude-speak-client -v af_heart "Warm female voice"

# Adjust speed (default 1.0)
~/Projects/claude-speak/.venv/bin/claude-speak-client -s 1.2 "Speaking faster"

# Quiet mode (suppress errors)
~/Projects/claude-speak/.venv/bin/claude-speak-client -q "Silent on success"
```

## Available Voices

| Voice | Description |
|-------|-------------|
| `bm_george` | British male, distinguished (DEFAULT) |
| `af_heart` | American female, warm |
| `am_adam` | American male, deep |
| `bf_emma` | British female, elegant |

## Troubleshooting

If "Daemon not running" error:
```bash
~/Projects/claude-speak/.venv/bin/claude-speak-daemon start
```

## Best Practices

- Keep utterances concise (1-2 sentences)
- Use for key points, not entire responses
- Check daemon status if issues arise
