# Changelog

All notable changes to Dad Joke Validator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-11-16

### Added
- **Template-Based Joke Generation** - Full implementation of `generator.py`
  - 8 joke templates (homophone, reversal, classic, difference, etc.)
  - Automatic validation of generated jokes
  - Quality filtering with configurable minimum score
  - Batch generation with best-first sorting
  - CLI with `--count`, `--min-score`, and `--best-only` options
- Template system uses asset data:
  - Homophones from pun-patterns.json
  - Common structures for pun phrases
  - Double meaning words for wordplay
  - Wholesome themes for subjects

### Features
- Generate 1-N jokes with single command
- Automatic scoring and filtering
- Template type tracking for debugging
- Best-of-N selection (generates 20 attempts, returns best)

### Known Limitations
- Template-based jokes can be grammatically awkward
- Limited creativity compared to LLM-based generation (v2.0 planned)
- Semantic coherence not guaranteed
- ~70-90% score range typical (peak dad jokes rare)

## [1.0.1] - 2025-11-16

### Changed
- **Externalized hardcoded data to JSON files** (Gemini peer review recommendation)
  - Moved `dad_phrases` to `pun-patterns.json`
  - Moved `red_flags` and `mild_flags` to `wholesome-themes.json`
- **Enhanced pun detection** with previously unused asset data:
  - Now uses `homophone_pairs` from pun-patterns.json (e.g., "two/too", "tuna/tune a")
  - Now uses `double_meaning_words` from pun-patterns.json (e.g., "light", "cool", "sharp")
  - Now uses `family_friendly_adjectives` from wholesome-themes.json (bonus scoring)

### Fixed
- All asset data now actively used in scoring (was partially unused in v1.0.0)
- Test suite updated to match improved scoring algorithm (all 11 tests pass)

### Improved
- Smarter pun quality detection with multi-layered analysis
- Better recognition of sound-alike wordplay (homophones)
- More maintainable code with externalized configuration

## [1.0.0] - 2025-11-16

### Added
- Initial release of Dad Joke Validator skill
- Four-dimensional scoring system (Pun Quality, Groan Factor, Wholesomeness, Structure)
- Overall dad joke score (0-100 scale)
- Joke analysis with detailed feedback
- Dad joke generation capability
- 10 reference examples with full analysis
- Batch validation script (`validator.py`)
- Joke generator script (`generator.py`)
- Comprehensive test suite
- Pun patterns database (JSON)
- Wholesome themes database (JSON)
- Complete documentation (README, examples, theory)
- Packaged .skill file for Claude web chat

### Design Decisions
- Weighted formula emphasizes Groan Factor and Wholesomeness (3x multiplier) as core dad joke characteristics
- Pun Quality weighted 2.5x as essential but not sole factor
- Structure weighted 1.5x as supporting element
- Threshold of 85/100 for "peak dad joke" based on example analysis
- Anti-pattern detection for inappropriate content

### Documentation
- Complete README with installation and usage
- 10 scored examples from 35/100 to 98/100
- Dad joke theory document explaining characteristics
- Detailed scoring guide for each dimension

## [Unreleased]

### Planned for v1.1
- Cultural dad joke variations (international puns)
- Difficulty levels for generation (easy/medium/hard groaners)
- Dad joke database expansion (100+ examples)
- Interactive practice mode
- Rhyme-based pun detection
- Dad joke "hall of fame" (community submissions)

### Under Consideration
- Integration with meme generator (visual dad jokes)
- "De-dad" mode (fix dad jokes that went too far)
- Dad joke tournaments (bracket-style scoring)
- Voice/timing analysis for verbal delivery

---

[1.0.0]: https://github.com/leegonzales/AISkills/releases/tag/dad-joke-validator-v1.0.0
