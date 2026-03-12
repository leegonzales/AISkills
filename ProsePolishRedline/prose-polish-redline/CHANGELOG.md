# Changelog

## 1.0.0 (2026-03-11)

Initial release.

- 9 kata agents: genre-scorer, coherence, authority, claims, stakes, rhythm, hedge, personality, perspective
- 5 editing tiers: STRUCTURAL, COHERENCE, AUTHORITY, CRAFT, VOICE
- Two-phase pipeline with merge engine (dedup, conflict resolution, Phase 2 rebasing)
- Tracked-changes .docx output via python-docx
- Animated HTML replay with tier-by-tier visualization
- Per-agent match rate diagnostics
- Three depth levels: conservative (3 agents), moderate (7), aggressive (9)
- Dry-run mode for prompt tuning
- Genre-calibrated thresholds for academic, technical, business, creative, personal, journalistic
- Comment-first mode for hallucination-prone agents (authority, claims, stakes, hedge)
- No-chaining rule for rhythm-agent
