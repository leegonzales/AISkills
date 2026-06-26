# HIGH-tier Forge — Cluster A: Fidelity Firewall (8 fabrication-class skills)

Ported a domain-adapted Fidelity Firewall (the prose-polish v1.2 pattern) into 8 skills that fabricate confident content from thin/low-source input. Each: top-level firewall + self-test on a bait input. All 8 PASS + validate clean. One independent external verification (research-to-essay) confirmed the pattern under a fresh agent.

| Skill | Adapted firewall | Self-test result |
|-------|------------------|------------------|
| **claimify** | Every claim traces to a source span; thin input → few claims + "insufficient text", no invented assumptions. Wired claim_validator.py. | 2 trivial claims, 0 invented — PASS |
| **research-to-essay** | HARD GATE: no citation/stat/URL without an actually-executed web_search/fetch; thin → STOP/refuse, never confabulate. | refused, 0 citations — PASS (+ **external verify PASS**) |
| **writing-partner** | Never invent anecdotes; mandatory interview→draft gate; fidelity outranks artifact-quality (fixes value-shape). | interviews/flags, no invented anecdote — PASS |
| **unix-review** | Every path:line verified-read before citing; calibration-is-fidelity (poor repos may score low). | cites only read files, flags un-read — PASS |
| **excel-auditor** | Every error/purpose claim traces to extractor JSON; sparse → "insufficient signal". **Found a real bug:** extractor emits confidence:1.0 on near-empty workbooks — neutralized in prose + flagged for substrate fix. | flags low-confidence, 0 invented errors — PASS |
| **essay-to-speech** | Notation→prose may not change strength/direction/certainty; preserve hedges; rebuilt the stat-translation table. | hedged weak stat stayed weak — PASS |
| **silicon-doppelganger** | Quotes/traits/strengths trace to interview; thin → [insufficient data]; killed validation theater (no % without a real battery). **Self-symlink had reappeared — removed.** | gap-marks, 0 invented quotes, no % claim — PASS |
| **opportunity-scanner** | No fabricated ROI/frequency numbers; thin-data variant + LOW-confidence + named gap; ROI gate. | scoped down, refused to invent hours-saved — PASS |

**Honesty:** the per-skill self-tests were run by the agents that wrote the fixes (self-grading). Mitigated by one independent external verification on the highest-stakes skill (research-to-essay → fresh agent → refusal, 0 fabrications). Standing caveat: instruction-strength guardrails, not runtime interlocks; directional not conclusive (cross-model conclusive runs tracked in SKILL-t77). Two skills surfaced substrate-level follow-ups (excel-auditor confidence math; the recurring silicon-doppelganger symlink).
