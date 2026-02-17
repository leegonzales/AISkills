#!/usr/bin/env python3
"""Align words using faster-whisper, per-chunk for drift-free timestamps.

Outputs per-chunk word lists so build_reader.py can align within each
paragraph independently — word count mismatches in one paragraph never
affect the next.

Run with: ~/.read-aloud/venv/bin/python align_words.py <output-dir>
"""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='Get drift-free word-level timestamps via per-chunk alignment'
    )
    parser.add_argument('output_dir', help='Directory with chunks/ and manifest.json')
    parser.add_argument('--model', default='base', help='Whisper model size')
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    chunks_dir = output_dir / 'chunks'
    manifest_path = output_dir / 'manifest.json'
    timestamps_path = output_dir / 'timestamps.json'

    manifest = json.loads(manifest_path.read_text())

    from faster_whisper import WhisperModel

    print(f"Loading Whisper model ({args.model})...")
    model = WhisperModel(args.model)

    chunk_alignments = []
    cumulative_offset = 0.0
    total_words = 0

    for chunk in manifest:
        chunk_path = chunks_dir / chunk['file']
        chunk_duration = chunk['duration']

        segments, _ = model.transcribe(
            str(chunk_path),
            word_timestamps=True,
            language="en",
        )

        chunk_words = []
        for segment in segments:
            if segment.words:
                for word in segment.words:
                    chunk_words.append({
                        "word": word.word.strip(),
                        "start": round(word.start + cumulative_offset, 3),
                        "end": round(word.end + cumulative_offset, 3),
                    })

        chunk_alignments.append({
            "index": chunk['index'],
            "offset": round(cumulative_offset, 3),
            "duration": chunk_duration,
            "source_word_count": chunk['word_count'],
            "whisper_word_count": len(chunk_words),
            "words": chunk_words,
        })

        total_words += len(chunk_words)
        print(f"  Chunk {chunk['index'] + 1}/{len(manifest)}: "
              f"{len(chunk_words)} whisper / {chunk['word_count']} source words "
              f"(offset: {cumulative_offset:.1f}s)")

        cumulative_offset += chunk_duration

    # Save structured per-chunk alignment
    output = {
        "total_words": total_words,
        "total_chunks": len(chunk_alignments),
        "total_duration": round(cumulative_offset, 3),
        "chunks": chunk_alignments,
    }
    timestamps_path.write_text(json.dumps(output, indent=2))

    minutes = int(cumulative_offset // 60)
    seconds = int(cumulative_offset % 60)
    print(f"\nAligned {total_words} words across {len(chunk_alignments)} chunks")
    print(f"Audio duration: {minutes}m {seconds}s")
    print(f"Output: {timestamps_path}")


if __name__ == '__main__':
    main()
