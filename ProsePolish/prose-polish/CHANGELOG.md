# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0] - 2026-06-23

### Added
- **Fidelity Firewall** (SKILL.md): a hard constraint for Elevation/Analysis — never add facts, statistics, citations, names, scenes, sensory detail, anecdotes, or lived experience the author didn't supply. Non-fabricating fallbacks: sharpen-from-source → `[specify: …]`/`[cite: …]` flag → reduce-the-claim. Explicit polish-vs-generate boundary (the firewall binds when editing a real author, not in Prevention/Generation). New "FIDELITY CHECK" step in the elevation output + a final meaning re-check.

### Changed
- **Authority Pass + Commitment Pass** (SKILL.md + references/remediation-strategies.md): gated behind the Fidelity Firewall. Reworked the worked examples that previously *modeled fabrication* (inventing companies/engineers, an unsourced "mortality drops 40%", a "97% … funded by fossil fuel interests", a 2008-desk scene) — each now shows the grounded-only result plus the faithful fallback (flag or soften) for when the draft lacks the specific.

### Why
A clean-room A/B forge (skill-forge, 2026-06-21) found the prior version produced the most vivid prose but **fabricated content** on low-source opinion + narrative drafts — both blind panels ranked those last. Root cause: the remediation examples taught the model to *add* invented specifics. This release closes that hole while keeping the craft/diagnostic engine intact. See `agent_docs/forge-runs/prose-polish-cleanroom/`.

## [1.1.0] - 2025-11-01

### Added
- Enhanced detection patterns
- 100% accuracy validation on real-world samples
- Corporate Opening Gambit Pattern detection (85%+ accuracy)

### Changed
- Improved 4-layer craft assessment

## [1.0.0] - 2025-10-15

### Added
- Initial release
- 4-layer assessment (Lexical, Structural, Rhetorical, Voice)
- Three-pass remediation framework
- Register-specific guidelines
