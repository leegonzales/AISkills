# Kata: Doctrine Reconciliation

> **Purpose:** Drift scanner. Diffs local doctrine/standards against fleet seed, reports green/amber, enforces variance cap.
> **Rhythm:** On every fleet-doctrine update + weekly drift check.
> **Gating condition:** This kata must ship with the doctrine templates. Without it, doctrine rollout is incomplete.

---

## Trigger

1. `DOCTRINE_UPDATE` message received via agent-mail from Adama
2. Weekly drift check (scheduled via cron or triggered by heartbeat)
3. Manual run before any significant persona change in `soul.md`

## Inputs

- `.servitor/doctrine.md` — local copy (may have Local Variance section)
- Fleet seed reference: `templates/doctrine/fleet-doctrine.md@<commit sha>` from servitor repo
- Local tuning header (names the seed SHA this local copy was reconciled against)

## Steps

### 1. Fetch fleet seed
```bash
cd ~/Projects/leegonzales/servitor && git fetch && git show origin/main:templates/doctrine/fleet-doctrine.md > /tmp/fleet-doctrine-seed.md
```

### 2. Extract principle list from seed
Level-3 headings matching regex `^### \d+\.\d+ ` — these are the canonical fleet principles. Expect ~28 in v0. Sub-principles (e.g., `### 4.1a`) are part of their parent unless they match the base regex themselves.

```bash
grep -E '^### [0-9]+\.[0-9]+ ' /tmp/fleet-doctrine-seed.md | sed 's/^### //'
```

### 3. Extract principle coverage from local
Walk `.servitor/doctrine.md`. For each fleet principle:
- **Present verbatim** → green for this principle
- **Present with Local Variance entry** → amber, variance must have justification
- **Missing entirely** → **red** — unacceptable; reconcile before closing kata

### 4. Count variances
Total count of Local Variance entries.

| Variance count | Status | Action |
|----------------|--------|--------|
| 0 | Green | Acknowledge and close |
| 1-5 | Amber | Report each variance with justification to Adama |
| 6+ | **Red — fleet-level** | Escalate to Adama *and* Pike: fleet doctrine may be wrong, not this agent |

### 5. Check tuning header
Header must contain:
- `Seeded from: templates/doctrine/fleet-doctrine.md @ <sha>`
- `Last reconciled: <date>`
- `Tuning contract: represent every fleet principle. Tune locally. Justify variance.`

If header missing or stale SHA, update it.

### 6. Write reconciliation report
Drop in `.servitor/memory/doctrine-reconcile-YYYY-MM-DD.md`:

```markdown
# Doctrine Reconciliation — <agent> — <date>

## Status
<Green | Amber | Red>

## Seed SHA
<prev sha> → <new sha>

## Principle coverage
- Present verbatim: <count>
- Present with variance: <count>
- Missing (must reconcile): <count>

## Variances (amber)
### <principle number> — <principle name>
**Local variant:** <how we do it here>
**Justification:** <why local conditions demand it>

## Escalations
<any red items, any 6+ variance trigger>
```

### 7. Respond to Adama
Via agent-mail, reply to the `DOCTRINE_UPDATE` with subject line:

```
DOCTRINE_RECONCILE_REPORT <agent> <status>
```

Example: `DOCTRINE_RECONCILE_REPORT walsh amber`

Body:
- Status (green/amber/red)
- Variance count
- Link to reconciliation report

Adama only reviews amber + red. Green self-acknowledges (Adama never sees it).

### 8. Repeat for standards.md
Same process, against `templates/standards/fleet-standards.md`. Standards variances have stricter rule: **cannot lower a bar without Adama variance approval.**

## Output Artifact (Required)

Per Burke's falsifiability redline: the kata must emit an externally observable artifact, not self-assertion. Pass = the triple is present and coherent. Fail = any leg of the triple is missing or internally inconsistent.

**The Triple:**

1. **Journal entry** — dated, wake-numbered, cites kata name and result (green/amber/red), links the reconciliation report path.
2. **State.json delta** — fields updated: `last_doctrine_reconcile_at`, `last_doctrine_reconcile_sha`, `last_doctrine_reconcile_status`, `doctrine_variance_count`, `standards_variance_count`.
3. **Commit SHA** — if doctrine/standards local copies changed, the commit that locked the change. If no change, the prior commit SHA recorded in state.

Adama samples ~10% of green submissions unannounced for artifact coherence. Green without the triple is treated as amber pending artifact production.

*Attribution: Burke (redline). Dax (triple spec). Walsh (sampling). Ratified CIC.*

## Success Criteria

- Every fleet principle is present in local doctrine (verbatim or with variance)
- Variance count ≤5 (6+ triggers fleet-level escalation)
- Tuning header is current (SHA matches fleet HEAD)
- Reconciliation report exists for this update
- **Triple artifact emitted** (journal entry + state.json delta + commit SHA)
- Reply sent to Adama within 1 wake of `DOCTRINE_UPDATE`

## Eval

| Metric | Target | Measurement |
|--------|--------|-------------|
| Coverage | 100% of fleet principles represented | Report section counts |
| Timeliness | Reply within 1 wake of update | Timestamp diff on mail |
| Variance discipline | ≤5 variances per agent | Count in report |
| Drift detection | No silent divergence between weekly checks | SHA match on scheduled run |

## Escalation

- **Red (missing principle):** Block wake close-out until reconciled
- **Amber ≥6:** Escalate to Adama + Pike same wake — fleet doctrine candidate for re-draft
- **Repeated weekly drift:** Escalate to Adama — possible tooling gap or heartbeat failure
- **Header stale >30 days:** Agent heartbeat may be broken — diagnostic ping from Adama

## Variance Cap Rationale

If 6+ agents each flag the same missing principle or the same forced local deviation, the *fleet doctrine* is under-specified for how the fleet actually operates. Escalating to the fleet level is not failure — it is the feedback loop doing its job. The cap is the signal, not a punishment.

---

## Known Limitations (v0)

- **Present-but-degraded.** This kata inspects textual presence of principles in local doctrine. It cannot detect when an agent claims a principle verbatim but violates it in practice (e.g., keeps §2.7 "Verify before claiming done" in local doctrine but skips verification on quiet wakes). Behavioral audit is out of scope for v0; a separate `katas/base-behavioral-audit.md` is the planned iteration-2 companion. Until then, Adama may surface suspected degradation via direct mail.
- **Sub-principle drift.** Sub-headings like `### 4.1a` are not independently tracked. If fleet doctrine adds sub-principles, the regex and extractor need an update before next reconcile.
- **Mail-subject parsing.** Agents that drift from the `DOCTRINE_RECONCILE_REPORT <agent> <status>` convention fall back to manual triage and may be missed in admiral review. Convention is enforced by social contract in v0; may become a hook later.
- **Cross-agent variance aggregation.** Variance cap (6+ same missing principle) is currently Adama's manual pattern-match across amber reports. Iteration 2 should aggregate automatically.

---

*Paired with `templates/doctrine/fleet-doctrine.md` and `templates/standards/fleet-standards.md`.*
