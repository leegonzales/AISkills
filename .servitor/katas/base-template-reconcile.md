# Kata: Template Reconciliation

> **Purpose:** Drift scanner for scaffolded files (`CLAUDE_SERVITOR.md`, `CLAUDE_WORKER.md`, `sops/base-*.md`). Diffs local copies against the fleet seed, merges or variance-justifies each change, emits a commit + journal triple.
> **Rhythm:** On every `TEMPLATE_UPDATE` message from Adama + weekly drift check.
> **Gating condition:** Must run before adopting a new wake-protocol or base-SOP update. Refusing to run = the update didn't take.

---

## Trigger

1. `TEMPLATE_UPDATE` message received via fleetmail (or Mattermost during fleetmail transition) from Adama
2. Weekly drift check
3. Manual run before any significant persona or SOP change in `.servitor/`

## Inputs

- `.servitor/CLAUDE_SERVITOR.md` — local wake protocol (may have agent-specific additions below the base block)
- `.servitor/CLAUDE_WORKER.md` — local worker protocol
- `.servitor/sops/base-*.md` — base SOPs (heartbeat, mail-processing, escalation, journal-discipline)
- Fleet seed: the embedded templates in `servitor-cli` (run `servitor-cli refresh-templates --help` to see current behavior)

## Scope — what this kata DOES and DOES NOT touch

| File | Touched? |
|------|----------|
| `CLAUDE_SERVITOR.md` | ✓ |
| `CLAUDE_WORKER.md` | ✓ |
| `sops/base-*.md` | ✓ |
| `CONSTITUTION.md` | handled by `refresh-templates` directly (always overwritten in-place, 0o444) — no kata ceremony needed |
| `soul.md` | NEVER — agent identity, variance justification not accepted |
| `state.json`, `journal.md`, `dream-*.md` | NEVER — runtime state, not templated |
| `doctrine.md`, `standards.md` | Use `base-doctrine-reconcile.md` kata instead |
| `sops/<domain>.md` (non-base) | NEVER — domain SOPs are agent-owned |

## Steps

### 1. Run refresh-templates (sidecar mode, non-destructive)

```bash
servitor-cli refresh-templates
```

Output partitions each in-scope file into: `missing` (created), `identical` (no-op), `modified` (`.new` sidecar written). No files overwritten without `--force`.

### 2. Triage each status

For each `missing` → file was created from embedded content. No review needed; the embed is the source of truth for missing templates.

For each `identical` → no-op. Skip.

For each `modified` (i.e., `.new` sidecar present):

- `diff <file> <file>.new` — read the diff
- Classify:
  - **Trivial drift** (whitespace, link formatting, wording polish) → accept upstream, `mv <file>.new <file>`
  - **Substantive update** (new wake step, new SOP section, tool change) → read for impact, accept if aligned with local operation, otherwise file a variance
  - **Local customization at risk** (you added an agent-specific block and the seed changed around it) → preserve local additions, merge seed changes around them manually, `rm <file>.new` once file is correct

### 3. Record variances

If you chose NOT to adopt a seed change, record it in `.servitor/memory/template-variances.md`:

```markdown
## <file> — <date>
**Seed change:** <brief>
**Local variant:** <why you're keeping the deviation>
**Justification:** <what local condition requires it>
**Review trigger:** <what would make you re-reconcile this later>
```

Variance count ≤5 across all reconciled files. 6+ escalates to Adama: seed may be wrong.

### 4. Commit the reconciliation

Stage only the files you accepted. Commit with message:

```
chore(reconcile): adopt template update <YYYY-MM-DD>

<one-line summary of what changed>
```

If nothing changed (all identical), no commit needed — journal the green run anyway.

### 5. Emit the triple artifact

**Journal entry** (required, in `.servitor/journal.md`):

```
## Wake #N — YYYY-MM-DD HH:MM — [source: ...] — Template reconcile (<status>)

TEMPLATE_UPDATE from Adama (<seed sha or trigger>).

- Created: <count>
- Refreshed: <files merged>
- Variance: <count>, see memory/template-variances.md#<date>
- Commit: <sha>

<any notes>
```

**State.json delta:**

```json
{
  "last_template_reconcile_at": "YYYY-MM-DDTHH:MM-06:00",
  "last_template_reconcile_seed_sha": "<sha>",
  "last_template_reconcile_status": "green | amber | red",
  "template_variance_count": <n>
}
```

**Commit SHA:** the commit from step 4, or the prior commit SHA if no changes. This is the corpse-independent witness that the reconcile actually ran.

### 6. Reply to Adama

Via fleetmail:

```
fleetmail reply <msg-id> --body "TEMPLATE_RECONCILE_REPORT <agent> <status> — variance=<n> commit=<sha7>"
```

If fleetmail isn't yet live at your agent, use Mattermost DM to Adama or mcp-agent-mail (transitional).

Adama only reviews amber + red. Green self-acknowledges.

## Output Artifact (Required)

Per the falsifiability rule: the kata emits an externally observable artifact, not self-assertion. Pass = the triple is present and coherent. Fail = any leg missing.

Adama samples ~10% of green submissions for triple coherence. Green without the triple is treated as amber pending artifact production.

## Success Criteria

- Every in-scope file is either identical, refreshed in local commit, or has a variance entry
- Variance count ≤5 (6+ escalates)
- Triple artifact emitted (journal + state + commit)
- Reply sent to Adama within 1 wake of `TEMPLATE_UPDATE`

## Eval

| Metric | Target | Measurement |
|--------|--------|-------------|
| Coverage | 100% of in-scope files reconciled | Diff `templates/` against `.servitor/` for base-* and top-level files |
| Timeliness | Reply within 1 wake of update | Timestamp on reply |
| Variance discipline | ≤5 variances per agent | Count in memory/template-variances.md |
| Drift detection | No silent divergence between weekly checks | Seed SHA match on scheduled run |

## Escalation

- **Red** (cannot reconcile safely, local state diverged in a way refresh can't surface): pause and hail Adama
- **Amber ≥6:** escalate — seed may be over-reaching for local conditions
- **Repeated weekly drift:** possible tooling or heartbeat gap

---

## Known Limitations (v0)

- **Sidecar ergonomics.** Three-way-merge would be better than `.new` files; v0 uses `.new` because that's what `refresh-templates` ships. If agents routinely struggle with manual merges, revisit.
- **Mail-subject parsing.** `TEMPLATE_RECONCILE_REPORT <agent> <status>` is social-contract-enforced in v0, not validated.
- **Scope creep risk.** If a fleet change needs to propagate to `doctrine.md` or `standards.md` *and* `CLAUDE_SERVITOR.md`, run both katas. Do not inline doctrine changes into this kata.

---

*Paired with `servitor-cli refresh-templates`. Companion to `base-doctrine-reconcile.md`.*
