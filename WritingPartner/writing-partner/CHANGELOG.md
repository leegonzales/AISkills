# Changelog

All notable changes to Writing Partner will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-18

### Added
- Initial release of Writing Partner skill
- **Interview Mode**: 3-phase progressive questioning protocol
  - Phase 1: Opening (Why This, Why Now)
  - Phase 2: Deepening (Ground Truth)
  - Phase 3: Process Probes
- **Thread Tracking**: Mark and manage emerging ideas
  - Types: MAIN, TANGENT, RESEARCH, COUNTER, SPARK
  - Operations: Mark, Park, Surface, Connect
- **Drafting Mode**: Collaborative writing from interview material
  - Pre-flight checklist for readiness
  - Voice-first approach (no generic-then-polish)
- **Calibration Mode**: Voice verification and AI detection
  - Blocklist pattern matching
  - Optional WritingSamples/ comparison
  - prose-polish integration for scoring
- **Voice blocklist**: Tiered AI pattern detection
  - Tier 1: Hard blocklist (95%+ confidence)
  - Tier 2: High confidence flags (80%+)
  - Tier 3: Contextual flags (60%+)
  - Tier 4: Soullessness indicators
- **prose-polish integration**: AI detection scoring workflow
- **WritingSamples/ support**: Optional voice calibration against real samples

### Design Decisions
- Interview-first approach prevents AI fabrication
- Thread tracking welcomes digressions (insight emerges from tangents)
- WritingSamples/ is optional for portability
- Blocklist-only mode works without personal samples
- Single-session MVP scope (most essays emerge in one session)

## [Unreleased]

### Planned for v1.1
- Beads integration for cross-session persistence
- Voice capture mode to help users build their own samples
- Enhanced thread visualization

---

[1.0.0]: https://github.com/leegonzales/AISkills/releases/tag/writing-partner-v1.0.0
