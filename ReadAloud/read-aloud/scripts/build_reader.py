#!/usr/bin/env python3
"""Build a standalone HTML reader with per-paragraph word alignment.

Aligns HTML words to Whisper timestamps WITHIN each paragraph independently,
so word-count mismatches in one paragraph never cascade to the next.
Audio is compressed to MP3 and embedded as base64.

Run with: python3 build_reader.py <body.md> <audio.wav> <timestamps.json>
"""

import argparse
import base64
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


# ── Markdown → HTML ──

def inline_format(text):
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)_([^_]+)_(?!\w)', r'<em>\1</em>', text)
    return text


def md_paragraph_to_html(para_lines):
    """Convert a single paragraph's lines to HTML."""
    lines = para_lines if isinstance(para_lines, list) else [para_lines]
    first = lines[0].strip()

    # Header
    header_match = re.match(r'^(#{1,6})\s+(.+)$', first)
    if header_match and len(lines) == 1:
        level = len(header_match.group(1))
        text = inline_format(header_match.group(2))
        return f'<h{level}>{text}</h{level}>'

    # Blockquote (all lines start with >)
    if all(l.strip().startswith('>') for l in lines):
        text = ' '.join(l.strip().lstrip('>').strip() for l in lines)
        text = inline_format(text)
        return f'<blockquote>{text}</blockquote>'

    # List (all lines start with - or *)
    if all(re.match(r'^[-*]\s+', l.strip()) for l in lines):
        items = []
        for l in lines:
            item_text = re.sub(r'^[-*]\s+', '', l.strip())
            items.append(f'<li>{inline_format(item_text)}</li>')
        return '<ul>' + ''.join(items) + '</ul>'

    # Aside
    joined = ' '.join(l.strip() for l in lines)
    aside_match = re.match(r'^\[Aside:\s*(.+)\]$', joined)
    if aside_match:
        text = inline_format(aside_match.group(1))
        return f'<div class="aside">Aside: {text}</div>'

    # Regular paragraph
    text = ' '.join(l.strip() for l in lines)
    text = inline_format(text)
    return f'<p>{text}</p>'


def split_md_paragraphs(md_text, n_chunks):
    """Split markdown into paragraph blocks aligned to audio chunk count.

    Splits on \\n\\n, skips HRs, then expands blocks where a header is
    followed by content (since md_to_plain creates separate paragraphs
    for headers). Validated against n_chunks from the audio pipeline.
    """
    raw_blocks = md_text.split('\n\n')
    md_blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if not stripped:
            continue
        # Keep HR lines (---) — generate_audio.py's md_to_plain keeps them
        # as paragraphs, so we must too for chunk alignment
        lines = stripped.split('\n')
        first = lines[0].strip()

        # Header followed by content = 2 audio paragraphs
        if len(lines) > 1 and re.match(r'^#{1,6}\s+', first):
            md_blocks.append([lines[0]])
            rest_lines = [l for l in lines[1:] if l.strip()]
            if rest_lines:
                md_blocks.append(rest_lines)
        else:
            md_blocks.append(lines)

    if len(md_blocks) != n_chunks:
        print(f"WARNING: {len(md_blocks)} MD paragraphs vs {n_chunks} audio chunks")

    return md_blocks


def extract_words_from_html(html):
    """Count words in an HTML fragment (text content only)."""
    text = re.sub(r'<[^>]+>', '', html)
    return len(text.split())


def wrap_words_in_html(html, start_idx):
    """Wrap each visible word with <span class="word" data-idx="N">.
    Returns (wrapped_html, next_idx)."""
    word_idx = start_idx
    output = []
    tokens = re.split(r'(<[^>]+>)', html)
    for token in tokens:
        if token.startswith('<') or not token.strip():
            output.append(token)
            continue

        parts = re.split(r'(\s+)', token)
        for part in parts:
            if part.strip():
                output.append(
                    f'<span class="word" data-idx="{word_idx}">{part}</span>'
                )
                word_idx += 1
            else:
                output.append(part)

    return ''.join(output), word_idx


# ── Per-paragraph alignment ──

def align_paragraph_timestamps(n_html_words, chunk_whisper_words):
    """Map HTML words to Whisper timestamps within a single paragraph.

    Uses ratio-based mapping: HTML word i maps to Whisper word floor(i * n_ws / n_html).
    This handles mismatches gracefully — if Whisper found 48 words and HTML has 50,
    some HTML words share a neighbor's timing. Drift never exceeds one word.
    """
    n_ws = len(chunk_whisper_words)

    if n_html_words == 0:
        return []

    if n_ws == 0:
        return [{"word": "", "start": 0, "end": 0}] * n_html_words

    result = []
    for i in range(n_html_words):
        ws_idx = min(int(i * n_ws / n_html_words), n_ws - 1)
        ws_word = chunk_whisper_words[ws_idx]

        frac = (i * n_ws / n_html_words) - ws_idx
        if ws_idx + 1 < n_ws and frac > 0:
            next_word = chunk_whisper_words[ws_idx + 1]
            start = ws_word['start'] + frac * (next_word['start'] - ws_word['start'])
            end = ws_word['end'] + frac * (next_word['end'] - ws_word['end'])
        else:
            start = ws_word['start']
            end = ws_word['end']

        result.append({
            "word": ws_word['word'],
            "start": round(start, 3),
            "end": round(end, 3),
        })

    return result


# ── Audio embedding ──

def embed_audio(audio_path):
    """Compress audio to MP3 and return base64 data URI."""
    has_ffmpeg = shutil.which('ffmpeg') is not None

    if has_ffmpeg:
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
            mp3_path = tmp.name

        try:
            subprocess.run(
                ['ffmpeg', '-y', '-i', str(audio_path),
                 '-codec:a', 'libmp3lame', '-b:a', '128k',
                 '-loglevel', 'error', mp3_path],
                check=True,
            )
            mp3_data = Path(mp3_path).read_bytes()
        finally:
            Path(mp3_path).unlink(missing_ok=True)

        b64 = base64.b64encode(mp3_data).decode('ascii')
        size_mb = len(mp3_data) / (1024 * 1024)
        print(f"Audio compressed: WAV -> MP3 ({size_mb:.1f} MB)")
        return f'data:audio/mpeg;base64,{b64}'
    else:
        wav_data = Path(audio_path).read_bytes()
        b64 = base64.b64encode(wav_data).decode('ascii')
        size_mb = len(wav_data) / (1024 * 1024)
        print(f"Audio embedded as WAV ({size_mb:.1f} MB)")
        return f'data:audio/wav;base64,{b64}'


# ── HTML template ──

def build_html(body_html, word_count, timestamps_json, audio_data_uri):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Read Aloud</title>
<style>
  :root {{
    --bg: #fafaf8;
    --text: #1a1a1a;
    --highlight: #ffe066;
    --highlight-text: #1a1a1a;
    --muted: #999;
    --border: #ddd;
    --control-bg: #f0f0ee;
    --accent: #2a5a8a;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Georgia', 'Times New Roman', serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.8;
  }}
  .controls {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--control-bg);
    border-bottom: 1px solid var(--border);
    padding: 12px 24px;
    display: flex;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 14px;
  }}
  .controls button {{
    font-family: inherit;
    font-size: 14px;
    padding: 6px 16px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: white;
    cursor: pointer;
    transition: all 0.15s;
  }}
  .controls button:hover {{
    background: var(--accent);
    color: white;
    border-color: var(--accent);
  }}
  .controls button.active {{
    background: var(--accent);
    color: white;
    border-color: var(--accent);
  }}
  .controls label {{
    display: flex;
    align-items: center;
    gap: 6px;
    color: #666;
  }}
  .controls input[type="range"] {{ width: 100px; }}
  .speed-display {{
    min-width: 36px;
    text-align: center;
    font-variant-numeric: tabular-nums;
  }}
  .progress-bar {{
    flex: 1;
    min-width: 120px;
    height: 6px;
    background: var(--border);
    border-radius: 3px;
    overflow: hidden;
    cursor: pointer;
  }}
  .progress-fill {{
    height: 100%;
    background: var(--accent);
    width: 0%;
    transition: width 0.1s linear;
  }}
  .time-display {{
    color: #666;
    font-size: 12px;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }}
  .content {{
    max-width: 680px;
    margin: 0 auto;
    padding: 48px 24px 120px;
  }}
  .content h1 {{ font-size: 2em; line-height: 1.2; margin-bottom: 24px; }}
  .content h2 {{ font-size: 1.4em; margin-top: 40px; margin-bottom: 16px; line-height: 1.3; }}
  .content p {{ margin-bottom: 20px; }}
  .content blockquote {{
    border-left: 3px solid var(--accent);
    padding-left: 20px;
    margin: 24px 0;
    color: #333;
    font-style: italic;
  }}
  .content ul, .content ol {{ margin: 16px 0; padding-left: 28px; }}
  .content li {{ margin-bottom: 8px; }}
  .content a {{
    color: var(--accent);
    text-decoration: underline;
    text-underline-offset: 2px;
  }}
  .content .aside {{
    background: #f5f5f0;
    border-radius: 6px;
    padding: 16px 20px;
    margin: 24px 0;
    font-size: 0.95em;
    color: #444;
  }}
  .word {{
    border-radius: 2px;
    padding: 0 1px;
    cursor: pointer;
    transition: background-color 0.08s;
  }}
  .word.current {{
    background-color: var(--highlight);
    color: var(--highlight-text);
  }}
  .word.spoken {{ color: var(--muted); }}
  .word:hover {{ background-color: #e8e8e0; }}
  /* No scroll-behavior: smooth on html — we control scroll manually */
</style>
</head>
<body>

<div class="controls">
  <button id="playBtn">&#9654; Play</button>
  <button id="stopBtn">&#9632; Stop</button>
  <label>
    Speed
    <input type="range" id="speedRange" min="0.5" max="2.0" step="0.1" value="1.0">
    <span class="speed-display" id="speedDisplay">1.0x</span>
  </label>
  <div class="progress-bar" id="progressBar">
    <div class="progress-fill" id="progressFill"></div>
  </div>
  <span class="time-display" id="timeDisplay">0:00 / 0:00</span>
</div>

<div class="content" id="content">
{body_html}
</div>

<audio id="audio" preload="auto">
  <source src="{audio_data_uri}">
</audio>

<script>
const TIMESTAMPS = {timestamps_json};
const WORD_COUNT = {word_count};

const audio = document.getElementById('audio');
const playBtn = document.getElementById('playBtn');
const stopBtn = document.getElementById('stopBtn');
const speedRange = document.getElementById('speedRange');
const speedDisplay = document.getElementById('speedDisplay');
const progressBar = document.getElementById('progressBar');
const progressFill = document.getElementById('progressFill');
const timeDisplay = document.getElementById('timeDisplay');

const words = document.querySelectorAll('.word');
let currentWordIdx = -1;
let animFrame = null;

function formatTime(secs) {{
  const m = Math.floor(secs / 60);
  const s = Math.floor(secs % 60);
  return m + ':' + String(s).padStart(2, '0');
}}

function findWordAtTime(t) {{
  let lo = 0, hi = TIMESTAMPS.length - 1;
  while (lo <= hi) {{
    const mid = (lo + hi) >> 1;
    if (TIMESTAMPS[mid].start <= t && t < TIMESTAMPS[mid].end) return mid;
    if (TIMESTAMPS[mid].start > t) hi = mid - 1;
    else lo = mid + 1;
  }}
  for (let i = TIMESTAMPS.length - 1; i >= 0; i--) {{
    if (TIMESTAMPS[i].start <= t) return i;
  }}
  return -1;
}}

function highlightWord(idx) {{
  if (idx === currentWordIdx) return;
  // Un-highlight previous current word
  if (currentWordIdx >= 0 && currentWordIdx < words.length) {{
    words[currentWordIdx].classList.remove('current');
    words[currentWordIdx].classList.add('spoken');
  }}
  // Mark skipped words as spoken (batch update, no scrolling)
  const start = Math.max(0, currentWordIdx + 1);
  for (let i = start; i < idx && i < words.length; i++) {{
    words[i].classList.add('spoken');
    words[i].classList.remove('current');
  }}
  currentWordIdx = idx;
  if (idx >= 0 && idx < words.length) {{
    words[idx].classList.add('current');
    words[idx].classList.remove('spoken');
    // Only auto-scroll forward (down) during playback — never bounce
    if (!audio.paused) {{
      const rect = words[idx].getBoundingClientRect();
      const viewH = window.innerHeight;
      // Scroll when word nears bottom 25% of viewport
      if (rect.bottom > viewH * 0.75) {{
        // Place word at ~30% from top
        const targetY = window.scrollY + rect.top - viewH * 0.3;
        window.scrollTo({{ top: targetY, behavior: 'smooth' }});
      }}
    }}
  }}
}}

function tick() {{
  if (audio.paused) return;
  const t = audio.currentTime;
  const dur = audio.duration || 1;
  progressFill.style.width = (t / dur * 100) + '%';
  timeDisplay.textContent = formatTime(t) + ' / ' + formatTime(dur);
  const tsIdx = findWordAtTime(t);
  if (tsIdx >= 0 && tsIdx < words.length) highlightWord(tsIdx);
  animFrame = requestAnimationFrame(tick);
}}

function resetHighlights() {{
  words.forEach(w => w.classList.remove('current', 'spoken'));
  currentWordIdx = -1;
  progressFill.style.width = '0%';
}}

playBtn.addEventListener('click', () => {{
  if (audio.paused) {{
    audio.play();
    playBtn.innerHTML = '&#10074;&#10074; Pause';
    playBtn.classList.add('active');
    tick();
  }} else {{
    audio.pause();
    playBtn.innerHTML = '&#9654; Play';
    playBtn.classList.remove('active');
    cancelAnimationFrame(animFrame);
  }}
}});

stopBtn.addEventListener('click', () => {{
  audio.pause();
  audio.currentTime = 0;
  playBtn.innerHTML = '&#9654; Play';
  playBtn.classList.remove('active');
  cancelAnimationFrame(animFrame);
  resetHighlights();
  timeDisplay.textContent = '0:00 / ' + formatTime(audio.duration || 0);
}});

speedRange.addEventListener('input', () => {{
  const rate = parseFloat(speedRange.value);
  speedDisplay.textContent = rate.toFixed(1) + 'x';
  audio.playbackRate = rate;
}});

progressBar.addEventListener('click', (e) => {{
  const rect = progressBar.getBoundingClientRect();
  const pct = (e.clientX - rect.left) / rect.width;
  audio.currentTime = pct * (audio.duration || 0);
  resetHighlights();
  if (!audio.paused) tick();
}});

document.getElementById('content').addEventListener('click', (e) => {{
  const wordSpan = e.target.closest('.word');
  if (!wordSpan) return;
  const idx = parseInt(wordSpan.dataset.idx);
  if (idx >= 0 && idx < TIMESTAMPS.length) {{
    audio.currentTime = TIMESTAMPS[idx].start;
    resetHighlights();
    highlightWord(idx);
    if (audio.paused) {{
      audio.play();
      playBtn.innerHTML = '&#10074;&#10074; Pause';
      playBtn.classList.add('active');
      tick();
    }}
  }}
}});

document.addEventListener('keydown', (e) => {{
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  if (e.code === 'Space') {{ e.preventDefault(); playBtn.click(); }}
  else if (e.code === 'Escape') stopBtn.click();
  else if (e.code === 'ArrowRight') audio.currentTime = Math.min(audio.currentTime + 5, audio.duration);
  else if (e.code === 'ArrowLeft') audio.currentTime = Math.max(audio.currentTime - 5, 0);
}});

audio.addEventListener('loadedmetadata', () => {{
  timeDisplay.textContent = '0:00 / ' + formatTime(audio.duration);
}});
audio.addEventListener('ended', () => {{
  playBtn.innerHTML = '&#9654; Play';
  playBtn.classList.remove('active');
  cancelAnimationFrame(animFrame);
}});
</script>
</body>
</html>'''


# ── Main ──

def main():
    parser = argparse.ArgumentParser(
        description='Build standalone HTML reader with per-paragraph alignment'
    )
    parser.add_argument('markdown', help='Body markdown file')
    parser.add_argument('audio', help='Audio WAV file')
    parser.add_argument('timestamps', help='Per-chunk timestamps JSON')
    parser.add_argument('--output', '-o', required=True)
    args = parser.parse_args()

    md_text = Path(args.markdown).read_text()
    ts_data = json.loads(Path(args.timestamps).read_text())
    audio_path = Path(args.audio)

    chunks = ts_data['chunks']

    # Split markdown into paragraphs, using chunk count as alignment target
    md_paragraphs = split_md_paragraphs(md_text, len(chunks))

    # Truncate to shorter of the two if still mismatched
    if len(md_paragraphs) != len(chunks):
        n = min(len(md_paragraphs), len(chunks))
        md_paragraphs = md_paragraphs[:n]
        chunks = chunks[:n]

    # Process each paragraph: convert to HTML, wrap words, align timestamps
    all_html_parts = []
    all_timestamps = []
    global_word_idx = 0

    for p_idx, (para_lines, chunk) in enumerate(zip(md_paragraphs, chunks)):
        para_html = md_paragraph_to_html(para_lines)
        wrapped_html, next_idx = wrap_words_in_html(para_html, global_word_idx)
        n_html_words = next_idx - global_word_idx

        para_timestamps = align_paragraph_timestamps(
            n_html_words, chunk['words']
        )

        all_html_parts.append(wrapped_html)
        all_timestamps.extend(para_timestamps)
        global_word_idx = next_idx

    body_html = '\n'.join(all_html_parts)
    word_count = global_word_idx

    print(f"Paragraphs: {len(md_paragraphs)}")
    print(f"HTML words: {word_count}")
    print(f"Timestamps: {len(all_timestamps)}")

    # Embed audio
    audio_data_uri = embed_audio(audio_path)

    # Build HTML
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    html = build_html(
        body_html, word_count, json.dumps(all_timestamps), audio_data_uri
    )
    output_path.write_text(html)

    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"Reader: {output_path} ({size_mb:.1f} MB, standalone)")


if __name__ == '__main__':
    main()
