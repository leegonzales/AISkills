#!/usr/bin/env python3
"""
Dad Joke Validator - Batch Analysis Tool

Analyzes jokes from file or stdin and outputs scored results.
"""

import json
import sys
import argparse
from typing import Dict, List, Tuple
from pathlib import Path


class DadJokeValidator:
    """Validates jokes against dad joke criteria."""

    def __init__(self):
        """Initialize validator with pun patterns and themes."""
        self.pun_patterns = self._load_pun_patterns()
        self.wholesome_themes = self._load_wholesome_themes()

    def _load_pun_patterns(self) -> Dict:
        """Load pun patterns from assets."""
        pattern_file = Path(__file__).parent.parent / "assets" / "pun-patterns.json"
        if pattern_file.exists():
            with open(pattern_file) as f:
                return json.load(f)
        return {}

    def _load_wholesome_themes(self) -> Dict:
        """Load wholesome themes from assets."""
        theme_file = Path(__file__).parent.parent / "assets" / "wholesome-themes.json"
        if theme_file.exists():
            with open(theme_file) as f:
                return json.load(f)
        return {}

    def analyze_joke(self, joke: str) -> Dict:
        """
        Analyze a joke and return scores.

        Args:
            joke: The joke text to analyze

        Returns:
            Dict with scores and analysis
        """
        # Score each dimension
        pun_score, pun_reason = self._score_pun_quality(joke)
        groan_score, groan_reason = self._score_groan_factor(joke)
        wholesome_score, wholesome_reason = self._score_wholesomeness(joke)
        structure_score, structure_reason = self._score_structure(joke)

        # Calculate overall score
        overall_score = (
            (pun_score * 2.5) +
            (groan_score * 3.0) +
            (wholesome_score * 3.0) +
            (structure_score * 1.5)
        )

        # Generate verdict
        verdict = self._generate_verdict(overall_score)

        # Generate improvements if needed
        improvements = []
        if overall_score < 85:
            improvements = self._generate_improvements(
                pun_score, groan_score, wholesome_score, structure_score
            )

        return {
            "joke": joke,
            "overall_score": round(overall_score, 1),
            "dimensions": {
                "pun_quality": {"score": pun_score, "reason": pun_reason},
                "groan_factor": {"score": groan_score, "reason": groan_reason},
                "wholesomeness": {"score": wholesome_score, "reason": wholesome_reason},
                "structure": {"score": structure_score, "reason": structure_reason}
            },
            "verdict": verdict,
            "improvements": improvements
        }

    def _score_pun_quality(self, joke: str) -> Tuple[int, str]:
        """Score pun quality (0-10)."""
        score = 5  # Default
        reason = "Moderate wordplay detected"

        # Simple heuristic: look for common pun indicators
        joke_lower = joke.lower()

        # Check pun patterns database first (highest quality)
        for pattern in self.pun_patterns.get("common_structures", []):
            if pattern.lower() in joke_lower:
                score = 10
                reason = f"Matches known pun pattern: {pattern}"
                return score, reason

        # Check for homophones (sound-alike words)
        for pair in self.pun_patterns.get("homophone_pairs", []):
            if any(word.lower() in joke_lower for word in pair):
                score = max(score, 8)
                reason = f"Homophone detected: {'/'.join(pair)}"

        # Check for double meaning words
        for word in self.pun_patterns.get("double_meaning_words", []):
            if word.lower() in joke_lower:
                score = max(score, 7)
                reason = f"Double meaning word: '{word}'"

        # Very simple statements with no pun structure
        sentences = joke.split(".")
        if len(sentences) <= 2 and len(joke) < 30 and "?" not in joke and "but" not in joke_lower:
            score = 1
            reason = "No clear wordplay or pun detected"
            return score, reason

        # Multiple meanings indicators
        if any(phrase in joke_lower for phrase in ["but then", "because", "however"]):
            score += 3
            reason = "Contrast structure suggests double meaning"

        # Question-answer format (often reveals pun)
        if "?" in joke and len(joke.split("?")) == 2:
            score += 1
            reason += "; setup/reveal format"

        # Over-explained jokes lose pun clarity
        if "..." in joke:
            score -= 3
            reason = "Pun clarity reduced by over-explanation"

        return min(10, max(0, score)), reason

    def _score_groan_factor(self, joke: str) -> Tuple[int, str]:
        """Score groan factor (0-10, higher is better for dad jokes)."""
        score = 5
        reason = "Moderate groan potential"

        # Common dad joke phrases (give these max groan) - now from JSON
        dad_phrases = self.pun_patterns.get("dad_phrases", [])
        if any(phrase in joke.lower() for phrase in dad_phrases):
            score = 10
            reason = "Classic dad joke phrasing guarantees groan"
            return score, reason

        # Dad jokes tend to be predictable
        if "why" in joke.lower() and "?" in joke:
            score += 2
            reason = "Question format increases predictability"

        # Short punchlines = more groan (only if there's structure)
        sentences = [s.strip() for s in joke.split(".") if s.strip()]
        if len(sentences) > 1 and sentences and len(sentences[-1]) < 50:
            score += 2
            reason += "; economical punchline"

        # Over-explained jokes lose groan factor
        if "..." in joke or "unless" in joke.lower():
            score -= 4
            reason = "Over-explanation reduces groan"

        # Very simple statements aren't groan-worthy
        if len(sentences) == 1 and len(joke) < 30 and "?" not in joke:
            score = 3
            reason = "Too simple, no groan-inducing punchline"

        return min(10, max(0, score)), reason

    def _score_wholesomeness(self, joke: str) -> Tuple[int, str]:
        """Score wholesomeness (0-10)."""
        score = 10  # Start optimistic
        reason = "Family-friendly content"

        # Check for red flags - now from JSON
        red_flags = self.wholesome_themes.get("red_flags", [])
        joke_lower = joke.lower()

        for flag in red_flags:
            if flag in joke_lower:
                score -= 5
                reason = f"Contains '{flag}' - reduces family-friendliness"
                break

        # Mild red flags - now from JSON
        mild_flags = self.wholesome_themes.get("mild_flags", [])
        for flag in mild_flags:
            if flag in joke_lower:
                score -= 2
                reason = f"Contains '{flag}' - slightly edges wholesomeness"
                break

        # "hate" is OK if it's "used to hate" (setup for reversal)
        if " hate " in joke_lower and "used to hate" not in joke_lower:
            score -= 2
            reason = "Contains 'hate' - slightly edges wholesomeness"

        # Bonus for family-friendly adjectives
        adjectives = self.wholesome_themes.get("family_friendly_adjectives", [])
        for adj in adjectives:
            if adj.lower() in joke_lower and score >= 8:
                score = 10
                reason = f"Family-friendly tone: '{adj}'"
                break

        # Check wholesome themes (only if no red flags)
        if score == 10:
            for theme in self.wholesome_themes.get("positive_topics", []):
                if theme.lower() in joke_lower:
                    score = 10
                    reason = f"Wholesome theme: {theme}"
                    break

        return max(0, score), reason

    def _score_structure(self, joke: str) -> Tuple[int, str]:
        """Score setup/punchline structure (0-10)."""
        score = 5
        reason = "Basic structure present"

        # Count sentences (split by . or ? or ,)
        # Handle "but then" as sentence divider for structure
        temp_joke = joke.replace(", but then", ". But then")
        sentences = [s.strip() for s in temp_joke.replace("?", ".").split(".") if s.strip()]

        if len(sentences) == 2:
            score = 9
            reason = "Classic two-sentence setup/punchline"
        elif len(sentences) == 1:
            if "?" in joke:
                score = 7
                reason = "Question/answer format"
            else:
                score = 3
                reason = "Single sentence, no clear setup"
        elif len(sentences) > 3:
            score = 3
            reason = "Too many sentences, loses focus"

        # Check for over-explanation (ellipsis or "unless" indicates continuation)
        if "..." in joke or "unless" in joke.lower():
            score = max(2, score - 6)
            reason = "Over-explained punchline"

        # Very long jokes are problematic
        if len(joke) > 150:
            score -= 2
            reason += "; too verbose"

        return max(0, score), reason

    def _generate_verdict(self, score: float) -> str:
        """Generate overall verdict based on score."""
        if score >= 85:
            return "Peak dad joke territory"
        elif score >= 70:
            return "Solid dad joke"
        elif score >= 50:
            return "Dad joke adjacent - has potential"
        else:
            return "Not a dad joke"

    def _generate_improvements(
        self, pun: int, groan: int, wholesome: int, structure: int
    ) -> List[str]:
        """Generate improvement suggestions."""
        improvements = []

        if pun < 7:
            improvements.append("Strengthen wordplay - find clearer double meaning")
        if groan < 7:
            improvements.append("Make punchline more obvious for better groan factor")
        if wholesome < 7:
            improvements.append("Remove edgy content - keep it family-friendly")
        if structure < 7:
            improvements.append("Tighten structure - shorter punchline, clearer setup")

        return improvements


def main():
    """Main entry point for CLI tool."""
    parser = argparse.ArgumentParser(description="Validate dad jokes")
    parser.add_argument(
        "command",
        choices=["analyze", "score"],
        help="Command to execute"
    )
    parser.add_argument(
        "--input",
        "-i",
        help="Input file with jokes (one per line)"
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output JSON file"
    )
    parser.add_argument(
        "--joke",
        "-j",
        help="Single joke to analyze"
    )

    args = parser.parse_args()

    validator = DadJokeValidator()
    results = []

    # Get jokes from source
    if args.joke:
        jokes = [args.joke]
    elif args.input:
        with open(args.input) as f:
            jokes = [line.strip() for line in f if line.strip()]
    else:
        # Read from stdin
        jokes = [line.strip() for line in sys.stdin if line.strip()]

    # Analyze each joke
    for joke in jokes:
        result = validator.analyze_joke(joke)
        results.append(result)

        # Print to stdout
        print(f"\nJoke: {joke}")
        print(f"Score: {result['overall_score']}/100 - {result['verdict']}")
        print("\nDimensions:")
        for dim, data in result['dimensions'].items():
            print(f"  {dim}: {data['score']}/10 - {data['reason']}")

        if result['improvements']:
            print("\nImprovements:")
            for imp in result['improvements']:
                print(f"  - {imp}")
        print("-" * 60)

    # Write JSON if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults written to {args.output}")


if __name__ == "__main__":
    main()
