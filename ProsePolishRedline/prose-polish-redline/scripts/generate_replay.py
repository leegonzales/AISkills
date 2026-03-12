#!/usr/bin/env python3
"""Generate animated HTML redline replay from text files + review JSON pairs.

Adapted from Robo Jen's generate_replay.py for the Prose Polish Redline system.

Usage:
  Single document:
    python scripts/generate_replay.py input.md review.json -o output.html

  Multi-document (tabbed view):
    python scripts/generate_replay.py \
      -m "doc1.md:review1.json:Essay Draft:96%" \
      -m "doc2.md:review2.json:Blog Post" \
      -o redline-replay.html

Accepts .md (markdown), .txt, or .docx (Word) input files.
"""
import argparse
import json
import re
import sys
from pathlib import Path

# Tier ordering -- matches edit-schema.md and tier-mapping.md
TIER_ORDER = [
    "STRUCTURAL",
    "COHERENCE",
    "AUTHORITY",
    "CRAFT",
    "VOICE",
]


def extract_text(path: Path) -> str:
    """Extract text from a file, dispatching by extension."""
    suffix = path.suffix.lower()
    if suffix == ".docx":
        from docx import Document

        doc = Document(str(path))
        return "\n\n".join(
            p.text.replace("\t", "") for p in doc.paragraphs if p.text.strip()
        )
    # Default: read as plain text (.md, .txt, .markdown, etc.)
    return path.read_text(encoding="utf-8")


def load_review_json(json_path: Path) -> list[dict]:
    """Load review JSON and return the edits list.

    Accepts either the full agent output format:
        {"agent": "...", "phase": 1, "edits": [...]}
    or a merged format with a top-level edits array,
    or a bare list of edit objects.
    """
    data = json.loads(json_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    return data.get("edits", [])


def slugify(title: str) -> str:
    """Convert a display title to a URL-safe slug."""
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return slug or "document"


def build_document_entry(
    text_path: Path,
    json_path: Path,
    title: str,
    match_rate: str,
) -> dict:
    """Build a single document data dict for the replay engine."""
    text = extract_text(text_path)
    edits = load_review_json(json_path)

    return {
        "label": title,
        "editCount": len(edits),
        "matchRate": match_rate,
        "text": text,
        "edits": edits,
    }


def load_template() -> str:
    """Load the HTML template from replay_template.html in the same directory."""
    template_path = Path(__file__).parent / "replay_template.html"
    if not template_path.exists():
        print(f"Error: Template not found at {template_path}", file=sys.stderr)
        sys.exit(1)
    return template_path.read_text(encoding="utf-8")


def generate_replay(
    manuscripts: dict[str, dict],
    output_path: Path,
) -> None:
    """Generate the replay HTML from document data and the external template."""
    template = load_template()
    data_js = (
        "const MANUSCRIPTS = "
        + json.dumps(manuscripts, ensure_ascii=False, indent=2)
        + ";"
    )
    html = template.replace("{{MANUSCRIPT_DATA}}", data_js)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    size = output_path.stat().st_size
    print(f"Generated replay: {output_path} ({size:,} bytes)")
    for key, ms in manuscripts.items():
        rate = f", {ms['matchRate']} match" if ms["matchRate"] else ""
        print(f"  {key}: {ms['label']} ({ms['editCount']} edits{rate})")


def parse_multi_spec(spec: str) -> tuple[Path, Path, str, str]:
    """Parse a -m spec string: 'text_path:json_path:title[:match_rate]'.

    The match_rate field is optional (defaults to empty string).
    """
    parts = spec.split(":")
    if len(parts) < 3:
        print(
            f"Error: -m spec must have at least 3 colon-separated parts: "
            f"text_path:json_path:title[:match_rate]\n  Got: {spec}",
            file=sys.stderr,
        )
        sys.exit(1)
    text_path = Path(parts[0])
    json_path = Path(parts[1])
    title = parts[2]
    match_rate = parts[3] if len(parts) > 3 else ""
    return text_path, json_path, title, match_rate


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate animated HTML redline replay from text + review JSON pairs."
    )
    parser.add_argument(
        "text_file",
        nargs="?",
        help="Path to input text file (.md, .txt, or .docx) (single mode)",
    )
    parser.add_argument(
        "json_file",
        nargs="?",
        help="Path to review JSON (single mode)",
    )
    parser.add_argument(
        "-m",
        "--manuscript",
        action="append",
        default=[],
        help="Multi-document spec: 'text_path:json_path:title[:match_rate]'",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="redline-replay.html",
        help="Output HTML path (default: redline-replay.html)",
    )
    parser.add_argument(
        "-t",
        "--title",
        default=None,
        help="Display title for single document mode",
    )
    parser.add_argument(
        "-r",
        "--match-rate",
        default="",
        help="Match rate string for single document mode (e.g. '96%%')",
    )

    args = parser.parse_args()

    manuscripts: dict[str, dict] = {}

    if args.manuscript:
        # Multi-document mode
        for spec in args.manuscript:
            text_path, json_path, title, match_rate = parse_multi_spec(spec)
            if not text_path.exists():
                print(f"Error: {text_path} not found", file=sys.stderr)
                sys.exit(1)
            if not json_path.exists():
                print(f"Error: {json_path} not found", file=sys.stderr)
                sys.exit(1)
            slug = slugify(title)
            base_slug = slug
            counter = 2
            while slug in manuscripts:
                slug = f"{base_slug}_{counter}"
                counter += 1
            manuscripts[slug] = build_document_entry(
                text_path, json_path, title, match_rate
            )
    elif args.text_file and args.json_file:
        # Single document mode
        text_path = Path(args.text_file)
        json_path = Path(args.json_file)
        if not text_path.exists():
            print(f"Error: {text_path} not found", file=sys.stderr)
            sys.exit(1)
        if not json_path.exists():
            print(f"Error: {json_path} not found", file=sys.stderr)
            sys.exit(1)
        title = args.title or text_path.stem
        match_rate = args.match_rate or ""
        slug = slugify(title)
        manuscripts[slug] = build_document_entry(
            text_path, json_path, title, match_rate
        )
    else:
        parser.print_help()
        print(
            "\nError: Provide either positional args (text_file json_file) or -m flags.",
            file=sys.stderr,
        )
        sys.exit(1)

    generate_replay(manuscripts, Path(args.output))


if __name__ == "__main__":
    main()
