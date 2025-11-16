#!/usr/bin/env python3
"""
Context Transfer Artifact Validator

Validates that transfer artifacts conform to the Context Continuity Protocol v2.
Checks for required sections, completeness, and structural integrity.

Usage:
    python validate_transfer.py <artifact.md>
    python validate_transfer.py <artifact.md> --mode minimal
    python validate_transfer.py <artifact.md> --mode full --strict
"""

import argparse
import re
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional, Tuple


class Mode(Enum):
    MINIMAL = "minimal"
    FULL = "full"
    AUTO = "auto"


class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class ValidationResult:
    severity: Severity
    message: str
    line_number: Optional[int] = None

    def __str__(self):
        location = f"Line {self.line_number}: " if self.line_number else ""
        return f"[{self.severity.value}] {location}{self.message}"


class TransferValidator:
    """Validates context transfer artifacts."""

    # Required sections for Full mode
    FULL_MODE_SECTIONS = [
        "§ IMMEDIATE ORIENTATION",
        "§ DECISION LOG",
        "§ OPEN LOOPS",
        "§ CRITICAL CONTEXT",
        "§ ARTIFACTS & OUTPUTS",
        "§ HUMAN CONTEXT",
        "§ TRANSFER METADATA",
    ]

    # Optional sections
    OPTIONAL_SECTIONS = ["§ CONVERSATION HISTORY"]

    # Required fields in Minimal mode
    MINIMAL_MODE_FIELDS = [
        "**TRANSFER**:",
        "**STATUS**:",
        "**DECIDED**:",
        "**NEXT**:",
        "**CONTEXT**:",
        "**HUMAN PREFS**:",
    ]

    # Evolution tags
    EVOLUTION_TAGS = ["[G]", "[C]", "[P]", "[K]"]

    # Decision types
    DECISION_TYPES = ["explicit", "implicit", "emergent"]

    # Status symbols
    STATUS_SYMBOLS = ["✓", "⧗", "⚠", "↻"]

    def __init__(self, content: str, mode: Mode = Mode.AUTO, strict: bool = False):
        self.content = content
        self.lines = content.split("\n")
        self.mode = mode if mode != Mode.AUTO else self._detect_mode()
        self.strict = strict
        self.results: List[ValidationResult] = []

    def _detect_mode(self) -> Mode:
        """Auto-detect artifact mode based on content."""
        if "MINIMAL MODE" in self.content:
            return Mode.MINIMAL
        elif "CONTEXT TRANSFER ARTIFACT v2.0" in self.content:
            return Mode.FULL
        else:
            # Heuristic: if has section markers, probably full mode
            section_count = sum(1 for line in self.lines if line.strip().startswith("§"))
            return Mode.FULL if section_count >= 5 else Mode.MINIMAL

    def validate(self) -> List[ValidationResult]:
        """Run all validation checks."""
        self.results = []

        # Common validations
        self._check_header()
        self._check_encoding()

        # Mode-specific validations
        if self.mode == Mode.MINIMAL:
            self._validate_minimal_mode()
        else:
            self._validate_full_mode()

        return self.results

    def _add_result(
        self, severity: Severity, message: str, line_number: Optional[int] = None
    ):
        """Add a validation result."""
        self.results.append(ValidationResult(severity, message, line_number))

    def _check_header(self):
        """Validate artifact header."""
        if self.mode == Mode.MINIMAL:
            if "CONTEXT TRANSFER — MINIMAL MODE" not in self.content:
                self._add_result(
                    Severity.ERROR, "Missing 'CONTEXT TRANSFER — MINIMAL MODE' header"
                )
        else:
            if "CONTEXT TRANSFER ARTIFACT v2.0" not in self.content:
                self._add_result(
                    Severity.ERROR, "Missing 'CONTEXT TRANSFER ARTIFACT v2.0' header"
                )

    def _check_encoding(self):
        """Check for proper separator lines."""
        separator = "═══════════════════════════════════════════════════════════════════"
        if separator not in self.content:
            self._add_result(
                Severity.WARNING,
                "Missing decorative separators (═══). Artifact may not be visually scannable.",
            )

    def _validate_minimal_mode(self):
        """Validate Minimal mode artifact."""
        # Check required fields
        for field in self.MINIMAL_MODE_FIELDS:
            if field not in self.content:
                self._add_result(
                    Severity.ERROR, f"Missing required field: {field.strip('**:')}"
                )

        # Check for status symbol
        has_status_symbol = any(symbol in self.content for symbol in self.STATUS_SYMBOLS)
        if not has_status_symbol:
            self._add_result(
                Severity.WARNING,
                "STATUS field should use symbols: ✓ resolved | ⧗ in-progress | ⚠ blocked | ↻ iterating",
            )

        # Check for timestamp
        if not re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", self.content):
            self._add_result(
                Severity.WARNING,
                "Missing ISO timestamp (e.g., 2025-01-15T14:23:00Z)",
            )

        # Check DECIDED includes rationale
        decided_match = re.search(r"\*\*DECIDED\*\*:(.+?)(?=\*\*|\n\n)", self.content, re.DOTALL)
        if decided_match:
            decided_text = decided_match.group(1)
            if "because" not in decided_text.lower():
                self._add_result(
                    Severity.WARNING,
                    "DECIDED field should include rationale (use 'because')",
                )
            if "alternatives rejected" not in decided_text.lower():
                self._add_result(
                    Severity.INFO,
                    "DECIDED field missing 'Alternatives rejected' (recommended)",
                )

        # Check NEXT is actionable
        next_match = re.search(r"\*\*NEXT\*\*:(.+)", self.content)
        if next_match:
            next_text = next_match.group(1).strip()
            if len(next_text) < 10:
                self._add_result(
                    Severity.WARNING,
                    "NEXT action seems too brief. Should be specific and actionable.",
                )

        # Check word count (should be ~200 words)
        word_count = len(self.content.split())
        if word_count > 400:
            self._add_result(
                Severity.WARNING,
                f"Minimal mode should be ~200 words (current: {word_count}). Consider Full mode for complex transfers.",
            )

    def _validate_full_mode(self):
        """Validate Full mode artifact."""
        # Check required sections
        for section in self.FULL_MODE_SECTIONS:
            if section not in self.content:
                self._add_result(Severity.ERROR, f"Missing required section: {section}")

        # Check § IMMEDIATE ORIENTATION fields
        self._validate_section(
            "§ IMMEDIATE ORIENTATION",
            ["**MISSION**", "**STATUS**", "**NEXT ACTION**"],
        )

        # Check § DECISION LOG structure
        if "§ DECISION LOG" in self.content:
            self._validate_decision_log()

        # Check § OPEN LOOPS
        if "§ OPEN LOOPS" in self.content:
            self._validate_open_loops()

        # Check § CRITICAL CONTEXT evolution tags
        if "§ CRITICAL CONTEXT" in self.content:
            self._validate_critical_context()

        # Check § TRANSFER METADATA completeness
        if "§ TRANSFER METADATA" in self.content:
            self._validate_transfer_metadata()

        # Check for TRANSFER READY marker
        if "§ TRANSFER READY" not in self.content:
            self._add_result(
                Severity.WARNING,
                "Missing '§ TRANSFER READY' marker at end of artifact",
            )

    def _validate_section(self, section_name: str, required_fields: List[str]):
        """Validate that a section contains required fields."""
        section_match = re.search(
            rf"{re.escape(section_name)}(.+?)(?=───|§|$)", self.content, re.DOTALL
        )
        if not section_match:
            return

        section_content = section_match.group(1)
        for field in required_fields:
            if field not in section_content:
                self._add_result(
                    Severity.WARNING,
                    f"Section '{section_name}' missing recommended field: {field}",
                )

    def _validate_decision_log(self):
        """Validate Decision Log structure."""
        decision_section = self._extract_section("§ DECISION LOG")
        if not decision_section:
            return

        # Check for table format
        if not re.search(r"\|.+\|", decision_section):
            self._add_result(
                Severity.WARNING,
                "§ DECISION LOG should use table format for decisions",
            )

        # Check for decision types
        has_decision_type = any(
            dtype in decision_section for dtype in self.DECISION_TYPES
        )
        if not has_decision_type:
            self._add_result(
                Severity.WARNING,
                "Decisions should be tagged with type: explicit | implicit | emergent",
            )

        # Check for rationale column
        if "Rationale" not in decision_section:
            self._add_result(
                Severity.ERROR,
                "§ DECISION LOG table missing 'Rationale' column",
            )

    def _validate_open_loops(self):
        """Validate Open Loops section."""
        open_loops = self._extract_section("§ OPEN LOOPS")
        if not open_loops:
            return

        # Check for checkboxes
        checkbox_count = open_loops.count("- [ ]")
        if checkbox_count == 0:
            self._add_result(
                Severity.INFO,
                "§ OPEN LOOPS: No unchecked items found. If nothing pending, consider noting 'None'.",
            )

        # Check for subsections
        expected_subsections = [
            "**Unresolved Questions**",
            "**Blockers**",
            "**Pending Inputs**",
        ]
        for subsection in expected_subsections:
            if subsection not in open_loops:
                self._add_result(
                    Severity.INFO,
                    f"§ OPEN LOOPS missing recommended subsection: {subsection}",
                )

    def _validate_critical_context(self):
        """Validate Critical Context section."""
        critical_context = self._extract_section("§ CRITICAL CONTEXT")
        if not critical_context:
            return

        # Check for evolution tags
        has_evolution_tags = any(
            tag in critical_context for tag in self.EVOLUTION_TAGS
        )
        if not has_evolution_tags:
            self._add_result(
                Severity.WARNING,
                "§ CRITICAL CONTEXT insights should use evolution tags: [G] [C] [P] [K]",
            )

        # Check for constraint types
        if "**Constraints**" in critical_context:
            constraint_types = ["Technical:", "Resource:", "Political/Org:", "Ethical:"]
            found_types = sum(
                1 for ctype in constraint_types if ctype in critical_context
            )
            if found_types == 0:
                self._add_result(
                    Severity.INFO,
                    "Consider categorizing constraints: Technical | Resource | Political/Org | Ethical",
                )

    def _validate_transfer_metadata(self):
        """Validate Transfer Metadata section."""
        metadata = self._extract_section("§ TRANSFER METADATA")
        if not metadata:
            return

        # Check for provenance
        if "**Provenance**:" not in metadata:
            self._add_result(
                Severity.WARNING,
                "§ TRANSFER METADATA missing **Provenance** (source agent identification)",
            )

        # Check for completeness indicator
        if "**Completeness**:" not in metadata:
            self._add_result(
                Severity.WARNING,
                "§ TRANSFER METADATA missing **Completeness** indicator",
            )

        # Check for context window pressure indicator
        pressure_symbols = ["○", "◐", "●"]
        has_pressure = any(symbol in metadata for symbol in pressure_symbols)
        if not has_pressure:
            self._add_result(
                Severity.INFO,
                "Consider adding **Context Window Pressure** indicator: ○ spacious | ◐ moderate | ● constrained",
            )

    def _extract_section(self, section_name: str) -> Optional[str]:
        """Extract content of a specific section."""
        match = re.search(
            rf"{re.escape(section_name)}(.+?)(?=───|§|═|$)", self.content, re.DOTALL
        )
        return match.group(1) if match else None

    def summary(self) -> Tuple[int, int, int]:
        """Return count of errors, warnings, and info messages."""
        errors = sum(1 for r in self.results if r.severity == Severity.ERROR)
        warnings = sum(1 for r in self.results if r.severity == Severity.WARNING)
        infos = sum(1 for r in self.results if r.severity == Severity.INFO)
        return errors, warnings, infos


def main():
    parser = argparse.ArgumentParser(
        description="Validate Context Transfer Artifacts (Protocol v2)"
    )
    parser.add_argument("artifact", type=Path, help="Path to artifact markdown file")
    parser.add_argument(
        "--mode",
        choices=["minimal", "full", "auto"],
        default="auto",
        help="Validation mode (default: auto-detect)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (exit code 1)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only show errors and warnings, not info messages",
    )

    args = parser.parse_args()

    # Read artifact file
    if not args.artifact.exists():
        print(f"ERROR: File not found: {args.artifact}", file=sys.stderr)
        sys.exit(1)

    content = args.artifact.read_text(encoding="utf-8")

    # Validate
    mode = Mode(args.mode)
    validator = TransferValidator(content, mode=mode, strict=args.strict)
    results = validator.validate()

    # Display results
    detected_mode = "Minimal" if validator.mode == Mode.MINIMAL else "Full"
    print(f"Validating artifact: {args.artifact}")
    print(f"Mode: {detected_mode}")
    print("-" * 70)

    for result in results:
        if args.quiet and result.severity == Severity.INFO:
            continue
        print(result)

    # Summary
    errors, warnings, infos = validator.summary()
    print("-" * 70)
    print(
        f"Summary: {errors} error(s), {warnings} warning(s), {infos} info message(s)"
    )

    # Exit code
    if errors > 0:
        print("\n❌ Validation FAILED (errors found)")
        sys.exit(1)
    elif warnings > 0 and args.strict:
        print("\n⚠️  Validation FAILED (warnings in strict mode)")
        sys.exit(1)
    elif warnings > 0:
        print("\n⚠️  Validation PASSED with warnings")
        sys.exit(0)
    else:
        print("\n✅ Validation PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
