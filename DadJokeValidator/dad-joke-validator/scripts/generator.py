#!/usr/bin/env python3
"""
Dad Joke Generator - Template-Based Generation

Generates dad jokes using templates and word lists, then validates
them with the Dad Joke Validator to ensure quality.
"""

import json
import random
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
from validator import DadJokeValidator


class DadJokeGenerator:
    """Generates dad jokes using templates and validation."""

    def __init__(self):
        """Initialize generator with templates and word lists."""
        self.validator = DadJokeValidator()
        self.templates = self._load_templates()
        self.pun_patterns = self.validator.pun_patterns
        self.wholesome_themes = self.validator.wholesome_themes

    def _load_templates(self) -> List[Dict]:
        """
        Load joke templates.

        Returns:
            List of template dictionaries with 'pattern', 'type', and 'fillable_slots'
        """
        return [
            # Homophone-based templates
            {
                "pattern": "Why don't {subjects} ever {action}? Because they're too {homophone1}!",
                "type": "homophone",
                "fillable_slots": ["subjects", "action", "homophone1"]
            },
            {
                "pattern": "What do you call {article} {subject} that {action}? {homophone1}!",
                "type": "homophone",
                "fillable_slots": ["article", "subject", "action", "homophone1"]
            },
            # Common structure templates
            {
                "pattern": "I used to {dislike} {topic}, but then it {pun_verb}.",
                "type": "reversal",
                "fillable_slots": ["dislike", "topic", "pun_verb"]
            },
            {
                "pattern": "Why did the {subject} {action}? Because it was {pun_phrase}!",
                "type": "classic",
                "fillable_slots": ["subject", "action", "pun_phrase"]
            },
            {
                "pattern": "What's the difference between {thing1} and {thing2}? You can {action1} {thing1}, but you can't {pun_phrase}!",
                "type": "difference",
                "fillable_slots": ["thing1", "thing2", "action1", "pun_phrase"]
            },
            # Double meaning templates
            {
                "pattern": "Why are {subjects} so {adjective}? Because they're always {double_meaning}!",
                "type": "double_meaning",
                "fillable_slots": ["subjects", "adjective", "double_meaning"]
            },
            {
                "pattern": "I'm reading a book about {topic}. It's {double_meaning}!",
                "type": "simple_pun",
                "fillable_slots": ["topic", "double_meaning"]
            },
            # Setup-punchline format
            {
                "pattern": "Why did the {subject} go to {place}? To {pun_action}!",
                "type": "motivation",
                "fillable_slots": ["subject", "place", "pun_action"]
            }
        ]

    def _get_word_lists(self) -> Dict[str, List[str]]:
        """Generate word lists for template filling."""
        return {
            "subjects": ["calendars", "scarecrows", "atoms", "bicycles", "trees", "clocks",
                        "computers", "books", "pencils", "elevators", "cats", "dogs"],
            "subject": ["calendar", "scarecrow", "atom", "bicycle", "tree", "clock",
                       "computer", "book", "pencil", "elevator", "cat", "dog"],
            "action": ["win arguments", "tell jokes", "make friends", "play sports",
                      "go to parties", "work late", "tell secrets", "take breaks"],
            "dislike": ["hate", "avoid"],
            "topic": ["math", "gardening", "books", "music", "science", "cooking"],
            "pun_verb": ["grew on me", "made sense", "came together"],
            "pun_phrase": ["outstanding in its field", "two tired", "make up everything",
                          "put down", "take for granted"],
            "article": ["a", "an"],
            "thing1": ["a guitar", "a book", "a pencil", "math"],
            "thing2": ["a fish", "a movie", "a pen", "cooking"],
            "action1": ["tune", "read", "write", "count on"],
            "adjectives": self.wholesome_themes.get("family_friendly_adjectives", []),
            "place": ["school", "the store", "the park", "work", "the doctor"],
            "pun_action": ["get better grades", "buy fresh ideas", "have fun", "work things out", "get checked out"],
            "double_meaning": ["heavy", "light", "cool", "sharp", "bright"]
        }

    def _fill_template(self, template: Dict) -> str:
        """
        Fill a template with random words from word lists.

        Args:
            template: Template dictionary

        Returns:
            Filled joke string
        """
        word_lists = self._get_word_lists()
        pattern = template["pattern"]

        # Fill each slot
        for slot in template["fillable_slots"]:
            placeholder = f"{{{slot}}}"

            # Skip if already filled
            if placeholder not in pattern:
                continue

            # Handle homophone slots specially
            if "homophone" in slot:
                pairs = self.pun_patterns.get("homophone_pairs", [])
                if pairs:
                    pair = random.choice(pairs)
                    # Use the "punchline" version (usually second word)
                    word = pair[1] if len(pair) > 1 else pair[0]
                    pattern = pattern.replace(placeholder, word)
            # Handle pun_phrase from common structures
            elif slot == "pun_phrase":
                phrases = self.pun_patterns.get("common_structures", [])
                if phrases:
                    pattern = pattern.replace(placeholder, random.choice(phrases))
            # Handle adjective slot (use wholesome adjectives)
            elif slot == "adjective":
                adjectives = self.wholesome_themes.get("family_friendly_adjectives", ["nice"])
                pattern = pattern.replace(placeholder, random.choice(adjectives))
            # Handle double_meaning from pun patterns
            elif slot == "double_meaning":
                words = self.pun_patterns.get("double_meaning_words", ["cool", "light"])
                pattern = pattern.replace(placeholder, random.choice(words))
            # Handle regular word lists
            elif slot in word_lists:
                word = random.choice(word_lists[slot])
                pattern = pattern.replace(placeholder, word)

        return pattern

    def generate(self, theme: str = None, min_score: int = 70, max_attempts: int = 20) -> Dict:
        """
        Generate a dad joke that meets the minimum score threshold.

        Args:
            theme: Optional theme (not fully implemented)
            min_score: Minimum acceptable score (default: 70)
            max_attempts: Maximum generation attempts (default: 20)

        Returns:
            Dict with 'joke', 'score', and 'analysis'
        """
        best_joke = None
        best_score = 0

        for attempt in range(max_attempts):
            # Pick random template
            template = random.choice(self.templates)

            # Fill template
            joke = self._fill_template(template)

            # Validate
            analysis = self.validator.analyze_joke(joke)
            score = analysis["overall_score"]

            # Track best
            if score > best_score:
                best_score = score
                best_joke = {
                    "joke": joke,
                    "score": score,
                    "analysis": analysis,
                    "template_type": template["type"]
                }

            # Return if meets threshold
            if score >= min_score:
                return best_joke

        # Return best attempt even if below threshold
        return best_joke

    def generate_batch(self, count: int = 10, min_score: int = 70) -> List[Dict]:
        """
        Generate multiple dad jokes.

        Args:
            count: Number of jokes to generate
            min_score: Minimum acceptable score

        Returns:
            List of joke dictionaries
        """
        jokes = []
        for _ in range(count):
            joke = self.generate(min_score=min_score)
            if joke:
                jokes.append(joke)

        # Sort by score (best first)
        jokes.sort(key=lambda x: x["score"], reverse=True)
        return jokes


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Generate dad jokes")
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        default=5,
        help="Number of jokes to generate (default: 5)"
    )
    parser.add_argument(
        "--min-score",
        "-s",
        type=int,
        default=70,
        help="Minimum acceptable score (default: 70)"
    )
    parser.add_argument(
        "--best-only",
        "-b",
        action="store_true",
        help="Only show jokes that meet min-score threshold"
    )

    args = parser.parse_args()

    print("Dad Joke Generator v1.1")
    print("=" * 60)
    print()

    generator = DadJokeGenerator()
    jokes = generator.generate_batch(count=args.count, min_score=args.min_score)

    # Filter if best-only
    if args.best_only:
        jokes = [j for j in jokes if j["score"] >= args.min_score]

    if not jokes:
        print(f"No jokes generated meeting the threshold of {args.min_score}/100")
        print("Try lowering --min-score or increasing --count")
        return

    print(f"Generated {len(jokes)} dad joke(s):\n")

    for i, joke_data in enumerate(jokes, 1):
        analysis = joke_data["analysis"]
        print(f"{i}. {joke_data['joke']}")
        print(f"   Score: {joke_data['score']}/100 ({analysis['verdict']})")
        print(f"   Template: {joke_data['template_type']}")
        print(f"   Pun: {analysis['dimensions']['pun_quality']['score']}/10, "
              f"Groan: {analysis['dimensions']['groan_factor']['score']}/10, "
              f"Wholesome: {analysis['dimensions']['wholesomeness']['score']}/10, "
              f"Structure: {analysis['dimensions']['structure']['score']}/10")
        print()


if __name__ == "__main__":
    main()
