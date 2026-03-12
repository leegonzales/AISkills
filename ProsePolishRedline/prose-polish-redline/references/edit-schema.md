# Edit Schema -- Prose Polish Redline

The JSON contract every kata agent must follow. The `apply_redlines` and `merge_redlines` scripts depend on this exact structure.

---

## Agent Output Format

Every kata agent must return a **single JSON object** with this structure:

```json
{
  "agent": "<agent-name>",
  "phase": 1,
  "edits": [ ... ]
}
```

| Field   | Type            | Required | Description |
|---------|-----------------|----------|-------------|
| agent   | string          | yes      | Agent identifier, e.g. `"coherence-agent"`, `"rhythm-agent"` |
| phase   | integer (1 or 2)| yes      | `1` = Structural (Coherence + Authority), `2` = Stylistic (Craft + Voice) |
| edits   | array of edit objects | yes | Zero or more edits. Empty array is valid (no changes needed). |

---

## Edit Object Schema

```json
{
  "tier": "STRUCTURAL",
  "severity": "MUST_FIX",
  "edit_type": "replace",
  "original_text": "verbatim text from the document",
  "new_text": "replacement text",
  "after_text": null,
  "comment": "Why this edit improves the writing",
  "kata": "coherence-logic-flow"
}
```

### Field Definitions

| Field          | Type   | Required         | Values / Constraints |
|----------------|--------|------------------|----------------------|
| `tier`         | string | yes              | One of: `STRUCTURAL`, `COHERENCE`, `AUTHORITY`, `CRAFT`, `VOICE` |
| `severity`     | string | yes              | One of: `MUST_FIX`, `SHOULD_FIX`, `SUGGESTION` |
| `edit_type`    | string | yes              | One of: `replace`, `delete`, `insert`, `comment` |
| `original_text`| string | yes for `replace`, `delete`, `comment`; null for `insert` | Verbatim text from the document (see Verbatim Matching below) |
| `new_text`     | string | yes for `replace`, `insert`; null for `delete`, `comment` | The replacement or inserted text |
| `after_text`   | string | yes for `insert`; null otherwise | Anchor text after which the new text is inserted |
| `comment`      | string | yes              | Human-readable explanation of why this edit matters |
| `kata`         | string | yes              | Which kata triggered this edit (e.g. `"coherence-logic-flow"`, `"rhythm-variance"`) |

---

## CRITICAL: Verbatim Text Matching

Your `original_text` must be a **VERBATIM COPY-PASTE** from the document text you received.

- Do NOT paraphrase or summarize the original
- Do NOT fix typos in the original (the edit fixes them via `new_text`)
- Do NOT normalize whitespace (preserve exact spacing)
- Do NOT add or remove punctuation
- This is code-level exact string matching -- the `apply_redlines` script will `indexOf()` this exact string in the document

**Minimum context rule:** Include enough surrounding text to make the match unique. If your `original_text` appears more than once in the document, extend it until it is unique.

**Maximum context rule:** Do not include entire paragraphs when only a sentence needs changing. Keep `original_text` as short as possible while remaining unique.

---

## Edit Type Specifications

### `replace` -- Swap existing text for new text

The most common edit type. Use when text exists and needs modification.

```json
{
  "tier": "COHERENCE",
  "severity": "MUST_FIX",
  "edit_type": "replace",
  "original_text": "Moreover, the system also improved throughput.",
  "new_text": "The system improved throughput by 40%.",
  "after_text": null,
  "comment": "Remove mechanical transition; add functional specificity",
  "kata": "coherence-transitions"
}
```

### `delete` -- Remove text entirely

Use when text should be removed with no replacement.

```json
{
  "tier": "CRAFT",
  "severity": "SHOULD_FIX",
  "edit_type": "delete",
  "original_text": "It is worth noting that ",
  "new_text": null,
  "after_text": null,
  "comment": "Impersonal opener adds nothing; sentence works without it",
  "kata": "hedge-impersonal-openers"
}
```

### `insert` -- Add new text after an anchor

Use when new text must be added without removing anything. `after_text` is the anchor string; `new_text` is inserted immediately after it.

```json
{
  "tier": "AUTHORITY",
  "severity": "SHOULD_FIX",
  "edit_type": "insert",
  "original_text": null,
  "new_text": " (Schuch et al., 2019)",
  "after_text": "exercise as effective as antidepressants for mild depression",
  "comment": "Ground delegated authority with specific citation",
  "kata": "authority-delegated"
}
```

### `comment` -- Flag an issue without providing a fix

Use when the agent identifies a problem but the fix requires human judgment or is outside the agent's scope.

```json
{
  "tier": "VOICE",
  "severity": "SUGGESTION",
  "edit_type": "comment",
  "original_text": "Different organizations use different approaches. Each has advantages and disadvantages.",
  "new_text": null,
  "after_text": null,
  "comment": "Olympian neutrality -- consider taking a position here. What do YOU think is the better approach?",
  "kata": "personality-perspective"
}
```

---

## Severity Guidelines

### `MUST_FIX`
Errors that damage the document's credibility or coherence. The document should not ship without addressing these.

- Logical fallacies or causal incoherence
- Factual errors or unsupported claims presented as fact
- Broken narrative flow (reader gets lost)
- Missing critical context

### `SHOULD_FIX`
Significant quality improvements that materially strengthen the writing. Skipping these leaves value on the table.

- Mechanical transitions that could be earned
- Delegated authority that could be demonstrated
- Cowardly hedges masking real opinions
- Uniform rhythm flattening emphasis

### `SUGGESTION`
Optional enhancements. Reasonable people could disagree.

- Voice personality additions
- Alternative phrasings for variety
- Density adjustments for pacing
- Style preferences

---

## Conflict Resolution

When multiple agents edit the same text, the merge engine resolves conflicts using:

1. **Tier priority:** STRUCTURAL > COHERENCE > AUTHORITY > CRAFT > VOICE
2. **Severity priority:** MUST_FIX > SHOULD_FIX > SUGGESTION
3. **Phase priority:** Phase 1 edits take precedence over Phase 2 edits on the same text

If two edits have identical tier, severity, and phase, the merge engine flags them for human review.

---

## Validation Rules

The merge engine will **reject** edits that fail these checks:

1. `original_text` not found in the source document (for replace/delete/comment)
2. `after_text` not found in the source document (for insert)
3. `original_text` matches multiple locations and is ambiguous
4. `edit_type` is not one of the four valid types
5. `tier` is not one of the five valid tiers
6. `severity` is not one of the three valid severities
7. Missing required fields for the given `edit_type`
8. `new_text` is identical to `original_text` (no-op replace)
