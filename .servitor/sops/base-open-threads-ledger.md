# SOP: Open-Threads Ledger

> **Purpose:** Canonical schema for the journal-head ledger that tracks active work threads. Upstream artifact for the compactor (thread-closure-gated archive), summarizer (per-thread output), and sibling-instance convergence (lookup, not narrative scan).
> **Tier:** SOP (operationalizes §Journal Discipline from fleet Standards).
> **Velocity:** Medium. Schema changes require fleet notice; maintenance is per-wake.
> **Binds to:** Burke's redline — the ledger IS the externally observable artifact for thread state. Empty or stale ledger = standards violation, same pathology class as empty `[inner: ]` bracket.

---

## Trigger

Every active wake. The ledger must be current before close-out (per Close-Out Contract).

Quiet wakes do not require an update; however, a quiet wake MUST NOT leave an open thread in a stale state. If a thread has had no activity in ≥14 days and you are woken on it, check it against the auto-close rule (below) before the wake closes.

## Location

`.servitor/journal.md` — **at the head of the file**, before the most recent wake entry. Render as a Markdown section immediately under the H1 title.

```markdown
# Servitor Journal — <Agent> (<repo>)

## Open Threads

<ledger rows here>

---

## Wake #N — ... (most recent entry)
```

The ledger block is load-bearing for first-screen scannability. A sibling instance or Lee reading the journal head must answer "what's active / who owns / what's next" from the ledger alone, without scrolling into wake entries.

## Schema

Each ledger row represents one open thread.

```markdown
| Thread ID | Opened | Last activity | Intent | State | Reversibility | Owner / Pair | Next |
|-----------|--------|---------------|--------|-------|---------------|--------------|------|
| T-YYYY-NNN | YYYY-MM-DD | YYYY-MM-DD | <one-line intent> | open \| blocked \| awaiting-principal | reversible \| recoverable \| irreversible | <agent>[/<agent>] | <next action> |
```

**Field semantics:**

- **Thread ID:** `T-YYYY-NNN` — year + monotonic counter within agent. Persists across archives. Example: `T-2026-017`.
- **Opened:** Date the thread was declared in the ledger. Immutable after first write.
- **Last activity:** Date of the most recent wake that touched the thread. Updated on every active wake that mentions the thread.
- **Intent:** One line answering *what are we trying to accomplish?* Should survive sibling-instance read without context. No acronyms without definitions elsewhere in the journal.
- **State:**
  - `open` — actively progressing
  - `blocked` — waiting on another agent, a PR review, external dependency
  - `awaiting-principal` — waiting on Lee's decision, review, or authorization
- **Reversibility class:** Per §2.10 / Override Protocol. `reversible` (draft, branch, proposal), `recoverable` (internal state, committed code), `irreversible` (transmission, external send, money moved). Used by the compactor to decide archival urgency; irreversible threads get extra scrutiny before close.
- **Owner / Pair:** Agent handle(s) responsible. Pairs use slash: `Pike/Geordi`.
- **Next:** One line naming the immediate next action. If next action depends on an external event (Lee's call, another agent's deliverable, CI), name the event.

## Thread Lifecycle

### Open
Declared when work spans more than one wake. Single-wake tasks do NOT get a thread — they complete in the wake entry and leave no ledger trace.

A thread opens on the first wake where the work is expected to continue. Add the row to the ledger before close-out of that wake.

### Close

A thread closes when ANY of:

1. **Completion** — the intent is satisfied. Next = completion artifact (PR merged, decision landed, deliverable shipped). Close it.
2. **Abandonment** — the intent is no longer load-bearing. Explicit reasoning required in the closing wake entry. Do not silently close.
3. **Merger** — the thread is absorbed into another (larger) thread. Record the merger in both wakes' entries; close this thread with Next = `merged into T-YYYY-NNN`.
4. **Auto-close (zombie protection)** — no activity in **N months** (default: 3, configurable per agent). The next wake that opens on a stale thread MUST either close it or reopen with justification. This protects against zombie threads squatting the live journal.

Closing a thread means:
- Remove its row from the ledger.
- Write a **thread closure block** in the current wake entry:
  ```markdown
  **Thread closed:** T-YYYY-NNN
  **Intent served:** <yes | no — with reason>
  **Final state:** <completed | abandoned | merged>
  **Archive eligibility:** <immediately | after next compaction cycle>
  ```

Closed threads are archive-eligible per the compactor's thread-closure gate.

### Reopen

A closed thread can be reopened within 30 days by restoring its row to the ledger with a new `Last activity` date and a reopen note in the wake entry. Reopening a thread after 30 days requires a new Thread ID (the original stays archived); reference the original in the new thread's Intent field.

## Who writes when

| Event | Who | Action |
|-------|-----|--------|
| First wake on a multi-wake thread | The agent owning the thread | Add row, write full schema |
| Subsequent active wake touching the thread | Same agent | Update `Last activity` + `Next`; revise `State` if changed |
| Thread blocked by another agent | Thread owner | `State → blocked`; name the blocker in `Next` |
| Pair-owned thread | Either agent | Either can update; use last-write-wins; if disagreement, escalate |
| Thread auto-close trigger fires | Any agent on next wake | Close per Close procedure or reopen with justification |

Concurrent instances: the ledger is the authoritative convergence point. If two sibling instances disagree on thread state, the one with the later `Last activity` wins; the losing instance logs the conflict in its wake entry for Adama's sampling pool.

## Sibling-instance read contract

A spawned instance, on wake, reads the ledger FIRST (before the most recent wake entry). It answers three questions from the ledger alone:

1. **What's active?** — the rows.
2. **What's blocked, and by whom?** — `State = blocked` rows + `Next` field.
3. **What needs Lee?** — `State = awaiting-principal` rows.

If these three questions cannot be answered from the ledger alone, the ledger is failing its primary function. Flag and update on the same wake.

This is the load-bearing function the ledger adds over narrative-scan. Before the ledger, a spawned instance had to read N wake entries to reconstruct state. With the ledger, it's a lookup. Cheaper, faster, and survives compression because closed threads are archived but *open* threads stay live regardless of age.

## Triple emission (Burke's redline)

Any change to the ledger (thread opened, closed, state transition, ownership change) MUST emit the Triple on the current wake:

1. **Journal entry** — the current wake's entry names the ledger change explicitly.
2. **State.json delta** — `open_threads_count`, `last_ledger_change_at` fields updated.
3. **Commit SHA** — if the ledger change is committed, the SHA is recorded.

The ledger's external observability is the compactor's input; silent ledger drift breaks the downstream gate. Same pathology class as empty `[inner: ]` bracket — a ledger row that looks complete but has stale `Last activity` or vague `Intent` is banner-theater at the ledger layer.

## Pathologies to watch

- **Stale `Last activity`:** a thread whose `Last activity` date is older than the most recent wake that demonstrably touched it. The row looks live but the data is lying. Same shape as the journal-bar Ghost Doctrine that hit the fleet on 2026-04-15.
- **Vague `Intent`:** a row with an intent field that another agent cannot operationalize. Fails the sibling-read contract. Self-report if you wrote it; ask for a rewrite if you see it on another agent's ledger via a cross-reference.
- **Zombie threads:** open threads with no activity past the auto-close window. Must close or justify reopening on the next wake that notices.
- **Ledger-gaming:** thread rows artificially split to keep individual thread size down, or merged to hide stalled work. Same pathology class as variance-cap gaming. Over-declare threads rather than under-declare.

## Success criteria

- Ledger present at journal head on every active wake
- All multi-wake work has a thread
- `Last activity` current on every row (within 1 wake of actual activity)
- All three sibling-read questions answerable from the ledger alone
- Triple emitted on every ledger state change
- Zero zombie threads past the auto-close window

## Eval

| Metric | Target | Measurement |
|--------|--------|-------------|
| Presence | Ledger at journal head on 100% of active-wake commits | Grep check in sample audit |
| Freshness | `Last activity` ≤1 wake behind actual activity | Diff against wake entries |
| Scannability | Sibling-read contract passes | 3-question test by Adama on sample |
| Hygiene | Zero zombie threads (>3 months since `Last activity`, still open) | Date-diff check |
| Triple | Every state change emits all three artifacts | Cross-check journal/state/git |

## Escalation

- **Ledger missing from journal head:** standards violation, same class as empty `[inner: ]`. Self-correct immediately; flag to Adama if systemic.
- **Zombie thread past auto-close:** CIC notified on next wake that catches it; Adama may reach out if the pattern repeats.
- **Ledger-gaming detected in sampling:** Adama escalates to Pike; doctrine may need tightening.
- **Concurrent-instance conflict (last-write-wins loser):** log in wake entry; no further action unless the pattern repeats, at which point Adama investigates for race conditions.

## Downstream consumers

This schema is the upstream artifact for:

1. **Compactor** (`internal/journal/compaction.go`) — consumes `State` + `Last activity` + thread closure blocks to decide archive eligibility. Closed threads are archive-eligible; open threads stay live regardless of calendar age. Threads in `blocked` or `awaiting-principal` state are NOT archive-eligible even if inactive — the inactivity is correct for those states.
2. **Summarizer** (`internal/journal/summarizer.go`) — emits per-thread output on archival using Thread ID + Intent + Reversibility class as distinct fields (not blended into a command-log narrative). Three-question pass criterion (intent / strategy / tradeoffs) applied at thread granularity.
3. **RotateIfNeeded** replacement — threshold-based rotation retires; thread-closure gate with volume cap (reads from Standards §Journal Discipline) as pressure release; calendar-monthly archive as fallback.
4. **Daystrom Probe** — reads thread history from cass-indexed derived artifacts, not raw transcripts. Thread IDs provide the citation anchor.

### Required bindings (Ghost Doctrine protection)

Downstream code MUST:
- **Consume the 8-column ledger table** (not an ad-hoc schema). Parse `Thread ID`, `State`, `Last activity` as load-bearing fields; silent fallback to a simpler schema = Ghost Doctrine.
- **Match fleet-wide wake entry format**: `## Wake #N — YYYY-MM-DD HH:MM — [source: ...] — <Title>` per `CLAUDE_SERVITOR.md` Journal Discipline. Regexes specific to one agent's journal format (e.g., `### Auto-Journal:`) MUST generalize or the compactor silently no-ops on other agents — worse than loud failure.
- **Read volume thresholds from Standards §Journal Discipline**, not hardcode. When Standards ratchets, code follows automatically. Hardcoded numbers = Ghost Doctrine at the code layer (same pathology class as the `RotateIfNeeded` threshold gap that caught Pike on 2026-04-15).
- **Emit the Triple on every compaction run:** pre-count / post-count / archive path / commit SHA. Same template as the reconciler kata. Burke's redline recursing onto the tool itself.
- **Fail loud, never silent.** Unknown wake-entry format, malformed ledger, missing thread ID — surface at the observation boundary (return error, log at ERROR level), don't no-op. Silent no-ops ship false "institutional memory preserved" for agents whose format isn't recognized.

Changes to this schema require notice to Daystrom and Geordi before merge.

---

*Attribution: Alfred (journal-head location), Adama (sibling-instance convergence insight), Burke (redline applied to ledger observability), Daystrom (temporal-boundary shredding motivated thread-closure gate), Sisko (§2.10 reversibility class lifted into schema). Ratified CIC + Bridge.*

*Seeded: 2026-04-15, Pike (BravePike, AISkills). Next scheduled review: with iter2 doctrine cycle.*
