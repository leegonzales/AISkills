# FMEA: Peer Review Skill Test Suite Execution

**Date:** 2026-01-07
**Scope:** Gemini + Codex Peer Review Skill Test Suites
**Estimated Test Count:** ~23 test tasks, 600+ individual test cases

---

## Pre-Flight Check Results

| Component | Status | Version | Notes |
|-----------|--------|---------|-------|
| Gemini CLI | OK | 0.22.5 | Cached OAuth credentials |
| Codex CLI | OK | 0.63.0 | Working with gpt-5.1-codex-max |
| bd CLI | OK | 0.46.0 | Database initialized |
| GEMINI_API_KEY | NOT SET | - | Using OAuth instead |
| OPENAI_API_KEY | NOT SET | - | Using cached auth |

---

## FMEA Analysis

### Severity Scale
- **10 (Critical):** Complete test failure, wasted significant cost
- **7-9 (High):** Major test failures, partial cost waste
- **4-6 (Medium):** Some tests fail, minor cost impact
- **1-3 (Low):** Minor issues, easily recoverable

### Detection Scale
- **10 (None):** Cannot detect until failure
- **7-9 (Low):** Detected only after significant execution
- **4-6 (Medium):** Detected after some execution
- **1-3 (High):** Detected early or pre-flight

### RPN = Severity × Occurrence × Detection (Risk Priority Number)

---

## Failure Mode Analysis

### Category 1: API & Authentication Failures

| ID | Failure Mode | Effect | Severity | Occurrence | Detection | RPN | Mitigation |
|----|--------------|--------|----------|------------|-----------|-----|------------|
| A1 | OAuth token expires mid-test | Tests fail, subagent hangs | 8 | 3 | 6 | 144 | Add auth check before each batch |
| A2 | API rate limit exceeded | Tests throttled/fail | 9 | 5 | 4 | 180 | **HIGH RISK** - Add rate limiting, batch tests |
| A3 | API quota exceeded | All remaining tests fail | 10 | 3 | 2 | 60 | Check quota before starting |
| A4 | Model unavailable | Tests using that model fail | 7 | 2 | 3 | 42 | Fallback model in test config |
| A5 | Network timeout | Individual test fails | 5 | 4 | 5 | 100 | Retry logic in test runner |

### Category 2: Cost & Resource Failures

| ID | Failure Mode | Effect | Severity | Occurrence | Detection | RPN | Mitigation |
|----|--------------|--------|----------|------------|-----------|-----|------------|
| C1 | Runaway API costs | Unexpected high bill | 10 | 3 | 8 | 240 | **CRITICAL** - Set cost limits, estimate upfront |
| C2 | Large context tests expensive | Higher than expected cost | 7 | 6 | 4 | 168 | **HIGH RISK** - Use smaller test contexts |
| C3 | Parallel tests multiply costs | Cost explosion | 8 | 4 | 5 | 160 | **HIGH RISK** - Serialize expensive tests |
| C4 | Multimodal tests costly | Image processing adds cost | 6 | 5 | 3 | 90 | Limit multimodal test count |

### Category 3: Test Design Failures

| ID | Failure Mode | Effect | Severity | Occurrence | Detection | RPN | Mitigation |
|----|--------------|--------|----------|------------|-----------|-----|------------|
| T1 | Non-deterministic AI output | Flaky tests, false failures | 6 | 8 | 7 | 336 | **CRITICAL** - Test for structure, not exact content |
| T2 | Tests require human judgment | Can't automate | 7 | 6 | 3 | 126 | Define objective pass criteria |
| T3 | Tests too granular | Takes forever, high cost | 5 | 5 | 4 | 100 | Group related tests |
| T4 | Missing test dependencies | Tests fail due to missing prereqs | 6 | 4 | 5 | 120 | Add dependency checks |
| T5 | Subagent context overflow | Subagent fails mid-test | 8 | 4 | 6 | 192 | **HIGH RISK** - Limit test batch size |

### Category 4: Infrastructure Failures

| ID | Failure Mode | Effect | Severity | Occurrence | Detection | RPN | Mitigation |
|----|--------------|--------|----------|------------|-----------|-----|------------|
| I1 | Beads database corruption | Can't track results | 5 | 2 | 3 | 30 | Backup before starting |
| I2 | Subagent dies unexpectedly | Lost test progress | 7 | 3 | 4 | 84 | Checkpoint progress frequently |
| I3 | Disk space exhaustion | Tests fail writing output | 6 | 2 | 2 | 24 | Check disk space upfront |
| I4 | CLI version mismatch | Unexpected behavior | 5 | 2 | 2 | 20 | Version check in pre-flight |

### Category 5: Process Failures

| ID | Failure Mode | Effect | Severity | Occurrence | Detection | RPN | Mitigation |
|----|--------------|--------|----------|------------|-----------|-----|------------|
| P1 | No clear pass/fail criteria | Can't assess results | 8 | 5 | 6 | 240 | **CRITICAL** - Define criteria before running |
| P2 | Tests run out of order | Dependency failures | 5 | 3 | 4 | 60 | Enforce test ordering |
| P3 | Results not captured | Can't analyze outcomes | 7 | 3 | 5 | 105 | Log all outputs |
| P4 | Bug beads not created | Issues lost | 6 | 4 | 6 | 144 | Template bug creation |

---

## Top Risk Items (RPN > 150)

| Rank | ID | Risk | RPN | Required Action |
|------|----|------|-----|-----------------|
| 1 | T1 | Non-deterministic AI output | 336 | **MUST FIX**: Define structural pass criteria, not content matching |
| 2 | C1 | Runaway API costs | 240 | **MUST FIX**: Calculate cost estimate, set hard limits |
| 3 | P1 | No clear pass/fail criteria | 240 | **MUST FIX**: Define objective criteria for each test |
| 4 | T5 | Subagent context overflow | 192 | **MUST FIX**: Limit tests per subagent batch |
| 5 | A2 | API rate limit exceeded | 180 | **MUST FIX**: Add rate limiting between tests |
| 6 | C2 | Large context tests expensive | 168 | **SHOULD FIX**: Use minimal viable test contexts |
| 7 | C3 | Parallel tests multiply costs | 160 | **SHOULD FIX**: Control parallelism |

---

## Cost Estimation

### Gemini API (estimated)
- Simple prompt: ~$0.001-0.005 per test
- Large context (10k+ tokens): ~$0.05-0.10 per test
- Multimodal: ~$0.10-0.20 per test

### Codex API (estimated)
- Simple exec: ~$0.01-0.02 per test
- Complex reasoning (xhigh): ~$0.10-0.20 per test

### Test Count Estimate
| Category | Gemini Tests | Codex Tests | Est. Cost/Test | Subtotal |
|----------|--------------|-------------|----------------|----------|
| CLI Flags | 30 | 40 | $0.02 | $1.40 |
| Templates | 14 | 12 | $0.05 | $1.30 |
| Use Cases | 20 | 15 | $0.10 | $3.50 |
| Synthesis | 15 | 15 | $0.10 | $3.00 |
| Multimodal/Large | 10 | 0 | $0.15 | $1.50 |
| Error Handling | 15 | 15 | $0.02 | $0.60 |
| Integration | 10 | 10 | $0.05 | $1.00 |

**Estimated Total: $12-15** (assuming no retries or failures)
**With 30% buffer for retries: ~$20**

---

## Required Pre-Execution Actions

### MUST DO (Blockers)

1. [ ] **Define pass/fail criteria** for each test category
   - Structural validation (JSON schema, required fields)
   - Error message presence/absence
   - Response time thresholds

2. [ ] **Create cost limits**
   - Set per-test timeout (30s default, 120s for complex)
   - Set per-batch cost limit
   - Add kill switch for runaway tests

3. [ ] **Fix non-determinism**
   - Tests check for presence of key elements, not exact wording
   - Use regex patterns for validation
   - Allow multiple acceptable outputs

4. [ ] **Limit subagent scope**
   - Max 5-10 tests per subagent
   - Checkpoint after each test
   - Write results immediately

5. [ ] **Add rate limiting**
   - 2-3 second delay between API calls
   - Batch similar tests together
   - Serialize expensive tests

### SHOULD DO (Risk Reduction)

6. [ ] Run smoke test first (1 test from each category)
7. [ ] Create test result schema for consistent logging
8. [ ] Backup beads database before starting
9. [ ] Document rollback procedure

---

## Recommended Execution Strategy

### Phase 1: Smoke Test (~$1-2)
Run 1 representative test from each category to validate:
- CLI authentication works
- Tests execute correctly
- Results captured properly
- Cost within expectations

### Phase 2: Critical Path Tests (~$5-7)
Run tests for documented functionality:
- Core CLI commands
- Primary use cases
- Basic synthesis

### Phase 3: Edge Case Tests (~$5-8)
Run error handling and edge cases:
- Error scenarios
- Large contexts
- Multimodal

### Phase 4: Integration Tests (~$3-5)
Run full workflow integration:
- End-to-end workflows
- Cross-skill integration

---

## Go/No-Go Checklist

Before executing tests, verify:

- [ ] Pass/fail criteria defined for all test categories
- [ ] Cost estimate approved ($15-25 range acceptable?)
- [ ] Rate limiting implemented
- [ ] Smoke test passes
- [ ] Subagent batch sizes limited
- [ ] Results logging confirmed
- [ ] Bug bead creation tested

**Recommendation:** Address the 7 high-priority items before proceeding.
