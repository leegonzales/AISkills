#!/usr/bin/env python3
"""
Test suite for Dad Joke Validator

Run with: python test_validator.py
"""

import unittest
from validator import DadJokeValidator


class TestDadJokeValidator(unittest.TestCase):
    """Test cases for dad joke validation."""

    def setUp(self):
        """Initialize validator for each test."""
        self.validator = DadJokeValidator()

    def test_peak_dad_joke_facial_hair(self):
        """Test classic high-scoring dad joke."""
        joke = "I used to hate facial hair, but then it grew on me."
        result = self.validator.analyze_joke(joke)

        self.assertGreaterEqual(result['overall_score'], 90)
        self.assertGreaterEqual(result['dimensions']['pun_quality']['score'], 9)
        self.assertEqual(result['dimensions']['wholesomeness']['score'], 10)

    def test_anti_gravity_classic(self):
        """Test anti-gravity book joke."""
        joke = "I'm reading a book about anti-gravity. It's impossible to put down."
        result = self.validator.analyze_joke(joke)

        self.assertGreaterEqual(result['overall_score'], 85)
        self.assertIn("Peak dad joke", result['verdict'])

    def test_atoms_make_up(self):
        """Test atoms joke."""
        joke = "Why don't scientists trust atoms? Because they make up everything!"
        result = self.validator.analyze_joke(joke)

        self.assertGreaterEqual(result['overall_score'], 85)
        self.assertGreaterEqual(result['dimensions']['pun_quality']['score'], 8)

    def test_low_wholesomeness_alcohol(self):
        """Test that alcohol content reduces wholesomeness."""
        joke = "I'm on a whiskey diet. I've lost three days already."
        result = self.validator.analyze_joke(joke)

        self.assertLess(result['dimensions']['wholesomeness']['score'], 7)
        self.assertLess(result['overall_score'], 70)

    def test_over_explained_structure(self):
        """Test that over-explanation hurts structure score."""
        joke = "What's the difference between a guitar and a fish? You can tune a guitar but you can't tuna fish... unless you go to the store and buy one."
        result = self.validator.analyze_joke(joke)

        self.assertLess(result['dimensions']['structure']['score'], 5)
        # Updated: homophone detection now gives credit, but overall still "dad joke adjacent"
        self.assertLess(result['overall_score'], 70)

    def test_improvements_generated(self):
        """Test that low-scoring jokes get improvement suggestions."""
        joke = "This is not a joke at all."
        result = self.validator.analyze_joke(joke)

        self.assertLess(result['overall_score'], 85)
        self.assertGreater(len(result['improvements']), 0)

    def test_verdict_categories(self):
        """Test verdict generation across score ranges."""
        test_cases = [
            ("I grew a beard.", 20, "Not a dad joke"),
            ("Parallel lines have so much in common.", 64, "Dad joke adjacent"),
            ("Why did the bicycle fall over? It was two-tired.", 88, "dad joke")
        ]

        for joke, expected_min_score, expected_verdict_contains in test_cases:
            result = self.validator.analyze_joke(joke)
            self.assertIn(expected_verdict_contains.lower(), result['verdict'].lower())


class TestScoringDimensions(unittest.TestCase):
    """Test individual scoring dimensions."""

    def setUp(self):
        self.validator = DadJokeValidator()

    def test_pun_quality_scoring(self):
        """Test pun quality detection."""
        high_pun = "I used to hate facial hair, but then it grew on me."
        low_pun = "I walked to the store."

        high_score, _ = self.validator._score_pun_quality(high_pun)
        low_score, _ = self.validator._score_pun_quality(low_pun)

        self.assertGreater(high_score, low_score)

    def test_groan_factor_scoring(self):
        """Test groan factor detection."""
        high_groan = "Why did the bicycle fall over? It was two-tired."
        low_groan = "I like bicycles."

        high_score, _ = self.validator._score_groan_factor(high_groan)
        low_score, _ = self.validator._score_groan_factor(low_groan)

        self.assertGreater(high_score, low_score)

    def test_wholesomeness_scoring(self):
        """Test wholesomeness detection."""
        wholesome = "Why did the tomato turn red? It saw the salad dressing!"
        not_wholesome = "I hate everything and alcohol is bad."

        wholesome_score, _ = self.validator._score_wholesomeness(wholesome)
        not_wholesome_score, _ = self.validator._score_wholesomeness(not_wholesome)

        self.assertGreater(wholesome_score, not_wholesome_score)

    def test_structure_scoring(self):
        """Test structure quality detection."""
        good_structure = "I used to hate facial hair. But then it grew on me."
        poor_structure = "I used to hate facial hair but then I stopped hating it and started liking it because it grew on me and now I think it's great and wonderful."

        good_score, _ = self.validator._score_structure(good_structure)
        poor_score, _ = self.validator._score_structure(poor_structure)

        self.assertGreater(good_score, poor_score)


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
