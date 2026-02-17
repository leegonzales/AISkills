#!/usr/bin/env python3
"""Generate audio from a markdown file using Kokoro TTS via mlx-audio.

Generates per-paragraph audio chunks for drift-free Whisper alignment,
then concatenates into a single audio file.

Run with: ~/.read-aloud/venv/bin/python generate_audio.py <input.md>
"""

import argparse
import json
import re
from pathlib import Path


def strip_frontmatter(md_text):
    """Strip YAML frontmatter (between --- delimiters) if present."""
    if md_text.startswith('---'):
        end = md_text.find('---', 3)
        if end > 0:
            md_text = md_text[end + 3:].strip()
    return md_text


def strip_sections(md_text, section_names):
    """Strip named heading sections from markdown.

    Removes everything from the heading to the next heading of the same
    or higher level, or end of document.
    """
    if not section_names:
        return md_text

    for name in section_names:
        name = name.strip()
        # Match ## Section Name (any heading level)
        escaped_name = re.escape(name)
        heading_re = r'#{1,6}'
        pattern = re.compile(
            r'^(' + heading_re + r')\s+' + escaped_name + r'\s*\n'
            r'(.*?)'
            r'(?=^' + heading_re + r'\s|\Z)',
            re.MULTILINE | re.DOTALL,
        )
        match = pattern.search(md_text)
        if match:
            md_text = md_text[:match.start()] + md_text[match.end():]

    return md_text.strip()


def extract_body(md_text, sections_to_strip=None):
    """Extract body text, stripping frontmatter and optional sections."""
    md_text = strip_frontmatter(md_text)

    if sections_to_strip:
        md_text = strip_sections(md_text, sections_to_strip)

    return md_text.strip()


def md_to_plain(md_text):
    """Convert markdown to plain text suitable for TTS."""
    text = md_text
    # Links: [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Bold: **text** -> text
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    # Italic: *text* -> text
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    # Italic: _text_ -> text
    text = re.sub(r'(?<!\w)_([^_]+)_(?!\w)', r'\1', text)
    # Headers: ## Title -> Title.
    text = re.sub(r'^#{1,6}\s+(.+)$', r'\n\1.\n', text, flags=re.MULTILINE)
    # Blockquotes: > text -> text
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # List markers: - item -> item
    text = re.sub(r'^[-*]\s+', '', text, flags=re.MULTILINE)
    # Aside markers: [Aside: -> Aside.
    text = re.sub(r'\[Aside:\s*', 'Aside. ', text)
    # Stray brackets
    text = re.sub(r'(?<!\w)\[|\](?!\w)', '', text)
    # Collapse whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def split_paragraphs(text):
    """Split plain text into paragraphs (non-empty blocks)."""
    blocks = text.split('\n\n')
    return [b.strip() for b in blocks if b.strip()]


def main():
    parser = argparse.ArgumentParser(description='Generate TTS audio from markdown')
    parser.add_argument('input', help='Markdown or text file path')
    parser.add_argument('--output-dir', '-d', required=True)
    parser.add_argument('--voice', '-v', default='af_heart')
    parser.add_argument('--speed', '-s', type=float, default=1.0)
    parser.add_argument(
        '--strip-sections',
        default='',
        help='Comma-separated heading names to strip (e.g., "Brief,Links & Resources")',
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    chunks_dir = output_dir / 'chunks'
    chunks_dir.mkdir(parents=True, exist_ok=True)

    audio_path = output_dir / 'audio.wav'
    text_path = output_dir / 'text.txt'
    md_body_path = output_dir / 'body.md'
    manifest_path = output_dir / 'manifest.json'

    # Parse strip-sections
    sections_to_strip = None
    if args.strip_sections:
        sections_to_strip = [s.strip() for s in args.strip_sections.split(',') if s.strip()]

    # Read and process
    md_text = Path(args.input).read_text()
    body = extract_body(md_text, sections_to_strip)
    plain = md_to_plain(body)

    md_body_path.write_text(body)
    text_path.write_text(plain)

    paragraphs = split_paragraphs(plain)
    word_count = len(plain.split())
    print(f"Extracted {word_count} words, {len(paragraphs)} paragraphs")

    # Generate audio per paragraph
    from mlx_audio.tts.utils import load_model
    import soundfile as sf
    import mlx.core as mx

    print("Loading Kokoro model...")
    model = load_model("mlx-community/Kokoro-82M-bf16")

    print(f"Generating audio (voice={args.voice}, speed={args.speed})...")
    manifest = []
    all_audio = []

    for p_idx, para in enumerate(paragraphs):
        para_segments = []
        for result in model.generate(para, voice=args.voice, speed=args.speed):
            para_segments.append(result.audio)

        if not para_segments:
            # Kokoro returned no audio — generate a short silence (0.3s)
            print(f"  Warning: Paragraph {p_idx + 1}: no audio from Kokoro, inserting silence")
            chunk_audio = mx.zeros((int(24000 * 0.3),))
        else:
            chunk_audio = mx.concatenate(para_segments, axis=0)
        chunk_file = f'chunk_{p_idx:03d}.wav'
        chunk_path = chunks_dir / chunk_file
        sf.write(str(chunk_path), chunk_audio, 24000)
        all_audio.append(chunk_audio)

        duration = len(chunk_audio) / 24000
        para_words = len(para.split())
        manifest.append({
            'index': p_idx,
            'file': chunk_file,
            'text': para,
            'word_count': para_words,
            'samples': int(len(chunk_audio)),
            'duration': round(duration, 3),
        })

        total_dur = sum(c['duration'] for c in manifest)
        print(f"  Paragraph {p_idx + 1}/{len(paragraphs)}: "
              f"{para_words} words, {duration:.1f}s "
              f"(total: {int(total_dur // 60)}m {int(total_dur % 60)}s)")

    # Concatenate all chunks
    full_audio = mx.concatenate(all_audio, axis=0)
    sf.write(str(audio_path), full_audio, 24000)

    # Save manifest
    manifest_path.write_text(json.dumps(manifest, indent=2))

    duration_secs = len(full_audio) / 24000
    minutes = int(duration_secs // 60)
    seconds = int(duration_secs % 60)
    print(f"\nAudio saved: {audio_path} ({minutes}m {seconds}s)")
    print(f"Manifest:    {manifest_path} ({len(manifest)} chunks)")


if __name__ == '__main__':
    main()
