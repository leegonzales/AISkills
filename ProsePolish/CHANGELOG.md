# Changelog

All notable changes to Prose Polish will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-11-01

### Added
- **Corporate Opening Gambit pattern** - New detection pattern for business-speak temporal framing ("In today's rapidly evolving [X] landscape...") with 85%+ AI detection rate validated through real-world testing
- **Data Injection pattern** - Detection pattern for sophisticated AI prompting where real data is embedded in AI-generated prose (handles cases where users provide facts/numbers to AI)
- **Score interpretation context** - Added real-world context note explaining that content marketing frequently scores 60-80+, helping users understand pattern density vs deception

### Changed
- Improved calibration for content marketing and business copy (which naturally contains more AI patterns due to genre conventions)
- Enhanced detection of sophisticated AI use cases where human-provided data is wrapped in AI prose

### Testing
- Validated with 100% detection accuracy on real-world writing samples from the internet
- Tested against 10 diverse samples spanning technical, business, academic, and creative writing

## [1.0.0] - 2025-11-01

### Added
- Initial release of Prose Polish (formerly Anti-Cliché Writing)
- Multi-layer detection system (Lexical, Structural, Rhetorical, Voice)
- Three-pass remediation framework (Rhythm, Commitment, Voice)
- Prevention mode with anti-cliché prompt engineering
- Training mode for teaching writing craft
- Register-specific guidelines (Technical, Business, Academic, Creative)
- Comprehensive reference files:
  - `ai-vocabulary.md` - AI-overused words with frequency multipliers
  - `detection-patterns.md` - Structural, rhetorical, and lexical tells
  - `remediation-strategies.md` - Three Pillars improvement framework
  - `prevention-prompts.md` - Quality-first prompt templates

### Features
- Research-backed detection incorporating Wikipedia AI pattern catalog, GPTZero frequency analysis
- Quality-focused philosophy (craft over evasion)
- Scored reporting (0-100 scale) with severity levels and actionable fixes
- Before/after examples with explanations
- Context-aware analysis respecting different writing registers

[1.1.0]: https://github.com/leegonzales/AISkills/releases/tag/v1.1.0
[1.0.0]: https://github.com/leegonzales/AISkills/releases/tag/v1.0.0
