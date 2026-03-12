#!/usr/bin/env python3
"""Extract plain text from a .docx file.

Reads all paragraphs, strips tabs, skips empty paragraphs,
and outputs text separated by blank lines.

Usage:
    python extract_text.py input.docx [-o output.txt]
"""
import argparse
import sys
from pathlib import Path

from docx import Document


def extract_text(docx_path: str) -> str:
    """Extract paragraph text from a DOCX, stripping tabs and blanks."""
    doc = Document(docx_path)
    return "\n\n".join(
        p.text.replace("\t", "") for p in doc.paragraphs if p.text.strip()
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract plain text from a .docx file."
    )
    parser.add_argument("input", help="Input DOCX file")
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output text file (default: stdout)",
    )
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)

    text = extract_text(str(path))

    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
