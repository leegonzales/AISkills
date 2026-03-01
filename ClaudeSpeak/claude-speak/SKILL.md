---
name: claude-speak
description: Speak text aloud using high-quality AI voice synthesis (Kokoro TTS on Apple Silicon). Use when user asks to vocalize, narrate, or speak text out loud. Supports concurrent audio generation for multiple callers.
---

# Claude Speak

Vocalize text using high-quality text-to-speech. British male voice (bm_george) by default. Supports concurrent audio generation via a process pool.

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

**TIP:** For longer text, append `&` to run fire-and-forget (see "Long Text" section below).

## Options

```bash
# Different voice
~/Projects/claude-speak/.venv/bin/claude-speak-client -v af_heart "Warm female voice"

# Adjust speed (default 1.0)
~/Projects/claude-speak/.venv/bin/claude-speak-client -s 1.2 "Speaking faster"

# Quiet mode (suppress errors)
~/Projects/claude-speak/.venv/bin/claude-speak-client -q "Silent on success"

# Custom timeout (default: 300s / 5 min)
~/Projects/claude-speak/.venv/bin/claude-speak-client -t 600 "Very long text..."
```

## Concurrency

The daemon supports concurrent audio generation via a `ProcessPoolExecutor`. Multiple callers can generate audio simultaneously.

**Two request paths:**
- `speak` (play aloud) — serialized through a single playback queue to prevent audio overlap
- `generate_file` (return WAV bytes) — parallelized across worker processes, each with its own model copy

**Daemon pool configuration:**
```bash
# Start with custom worker count (default: auto based on CPU count)
~/Projects/claude-speak/.venv/bin/claude-speak-daemon start --workers 3

# Check pool status
python3 -c "from claude_speak_daemon import send_command; print(send_command({'command': 'ping'}))"
# Returns: {"success": true, "status": "ready", "num_workers": 3, "playback_queue_depth": 0}
```

**Programmatic file generation (for concurrent use):**
```python
from claude_speak_daemon import send_command
result = send_command({
    "command": "generate_file",
    "text": "Generate audio without playing",
    "voice": "bm_george",
    "speed": 1.0
}, timeout=120.0)
# result: {"success": true, "audio_base64": "...", "duration": 2.7, "format": "wav"}
```

## Long Text (3+ sentences)

For longer content, use **fire-and-forget mode** with shell backgrounding:

```bash
~/Projects/claude-speak/.venv/bin/claude-speak-client "Your longer text here..." &
```

The trailing `&` runs the command in the background at the shell level, so Claude Code doesn't track it as a task. The audio plays while the conversation continues—no timeout errors or false "failed" notifications.

**Why this works:** Claude Code's `run_in_background` still monitors the task and may report timeout failures even when audio completes successfully. Shell backgrounding (`&`) avoids this entirely.

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

After code updates, restart the daemon to pick up changes:
```bash
~/Projects/claude-speak/.venv/bin/claude-speak-daemon restart
```

## Best Practices

- For short text (1-2 sentences): run normally
- For longer text (paragraphs): use `&` fire-and-forget
- For batch/concurrent generation: use `generate_file` command programmatically
- Check daemon status if issues arise
- Use `--workers N` to tune pool size for your workload
