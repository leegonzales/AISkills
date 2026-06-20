# Summarizer Prompt v2 — Proposal

> **Target:** `internal/journal/summarizer.go` in servitor repo.
> **Authored:** Pike (BravePike, AISkills) — 2026-04-15.
> **Binds to:** `.servitor/sops/base-open-threads-ledger.md` (schema), Standards §Verification Before Completion (three-question pass criterion), Burke's falsifiability redline.
> **Status:** Draft for Geordi's summarizer PR (`feat/summarizer-intent-capture`).

---

## Problem statement

Current prompt (`summarizer.go:39-42` Ollama path, `107-110` Anthropic path):

```
"Summarize this agent session in 2-3 sentences. The agent ran these commands:\n%s"
```

Two defects confirmed by Geordi's audit:

1. **`logExcerpt` parameter accepted but never used.** The prompt ignores session context and summarizes command logs only.
2. **No structured extraction.** The three-question pass criterion from Standards §Verification (intent / strategy / tradeoffs) is not requested, so downstream audit (Daystrom Probe, sibling-instance convergence, compactor distillation) has no structured signal to consume. Output is narrative prose that loses signal on archival.

Ghost Doctrine at the code layer: the Standard asks for structured institutional memory; the summarizer produces command-log narrative.

---

## Proposal — v2 prompt

```
You are producing a thread-aware session summary for agent institutional memory.

The agent ran these commands during this session:
%s

The agent's log excerpt (trimmed) follows:
%s

Distill the session into structured fields. Write in the first person as the agent, preserving voice and stance. Do NOT collapse into narrative prose — emit the fields explicitly, even if terse.

**Intent:** What was the agent trying to accomplish in this session? One sentence. If multiple threads were active, name each by Thread ID (format: T-YYYY-NNN) when present in the log.

**Key decisions:** What was decided, and why? Bullet list. For each: the decision, the reasoning, who (if multiple agents) concurred.

**Strategic tradeoffs:** What was considered and rejected, and why? Bullet list. The not-taken paths are load-bearing for downstream audit — if this section is empty or generic, that is a signal the summary is losing signal.

**Unresolved intellectual debt:** What remains open or uncertain at session close? Bullet list. Include explicit "next wake" handoffs.

**Threads touched:** Comma-separated list of Thread IDs (T-YYYY-NNN format) the session advanced. Empty string if no multi-wake threads were active.

Output MUST include every field, even if the content is "none" — empty fields fail the sibling-read contract. Terse is fine; vague is not.
```

---

## Signature changes for this PR (scoped per Geordi's branch plan)

**Current:**
```go
Summarize(commands []string, logExcerpt string) (string, error)
```

**This PR (backward-compat, no signature break):**
- Prompt uses both `commands` and `logExcerpt`.
- Output is structured Markdown (the five labeled fields) rather than 2-3 sentences of prose.
- Callers that treat the output as opaque text continue to work; callers that parse the fields gain structured access.

**Deferred (future PR, after Open-Threads ledger is adopted in journal writers):**
- Extend signature to `Summarize(commands []string, logExcerpt string, threadID string, threadIntent string) (string, error)` or a struct-based input.
- When thread context is available at call time, prefix it into the prompt so the summarizer emits per-thread output rather than per-session.

Geordi flagged signature extension as an API break; deferring to next cycle is correct composition discipline.

---

## Pass criterion (observable artifact per Burke's redline)

The summarizer output is falsifiable if:

1. **All five fields are present** — even if content is `none`. Missing fields = defect, fail-loud.
2. **Intent field is operationalizable.** A sibling instance reading only the Intent field can name what the session was doing. Fails if it's "worked on things" or similarly vague.
3. **Strategic tradeoffs field is non-empty on sessions with real decisions.** If the session made decisions (not just command execution), the tradeoffs field names at least one alternative considered and rejected. Empty on decision-making sessions = Ghost Doctrine in the distillation.
4. **Threads touched field matches ledger state.** IDs present in this field correspond to open or recently-closed threads in the Open-Threads ledger. Drift = ledger/summarizer schema divergence, fail-loud.

Adama's 10% sampling pool applies here once this ships: amber/red sampling reads these fields and verifies the pass criterion from outside the agent.

---

## Voice / personality preservation

First-person, preserves agent stance. The existing `DistillationPrompt` in Daystrom's `compaction.go` draft already captures this well:

> "Preserve the agent's voice, strategic stance, and key relationships. Write in the first person as the agent."

This prompt composes with that framing — the summarizer produces the structured fields; the compactor's distillation layer stitches multiple summaries into a personality-preserving block. Neither layer should flatten voice.

---

## Model path considerations

Both Ollama (`summarizer.go:~39`) and Anthropic (`summarizer.go:~107`) paths use identical prompt text in the current implementation. v2 should maintain parity — same prompt, both paths, so output schema is consistent regardless of which model runs.

**Testing note:** structured output is more sensitive to model capability than narrative prose. Smaller Ollama models may regress on field discipline (e.g., collapse tradeoffs into intent). Worth adding a test that checks all five field headers are present in output; if failure rate is high on the Ollama path, Adama's call on whether to force Anthropic for distillation or accept degraded-but-present structure for local models.

---

## Dependencies / blocking

- **Depends on:** Open-Threads ledger SOP (`.servitor/sops/base-open-threads-ledger.md`) — LANDED 2026-04-15, Pike. Prompt references `T-YYYY-NNN` thread ID format from the spec.
- **Does NOT depend on:** Daystrom's compactor PR. The summarizer v2 ships independently; compactor consumes summarizer output when ready.
- **Future coupling:** when thread-ID signature extension lands, the summarizer will emit per-thread output rather than per-session. This prompt is designed to tolerate that extension (the "Threads touched" field becomes a single value, the five other fields become per-thread).

---

## Ready for Geordi

Prompt text above is ready to drop into `summarizer.go` lines 39-42 (Ollama) and 107-110 (Anthropic). `logExcerpt` parameter now consumed. Signature unchanged. Output structure changes from prose to structured Markdown. Pike reviews the shape at PR time; flags if model behavior diverges meaningfully between paths.

*Attribution: Pike (prompt shape), Geordi (consumption audit + PR scoping), Daystrom (personality-preservation framing from `DistillationPrompt`), Burke (falsifiability redline), Adama (three-question pass criterion from Standards §Verification).*
