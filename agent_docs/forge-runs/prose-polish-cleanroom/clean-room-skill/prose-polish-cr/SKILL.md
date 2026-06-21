---
name: prose-polish-cr
description: Make a piece of writing meaningfully better — clearer, tighter, better-structured, more authoritative, with a distinct genre-appropriate voice — without changing the author's meaning or fabricating content. Use when asked to revise, edit, tighten, sharpen, improve, or "make this read better": essays, posts, emails, docs, reports, fiction, marketing copy. Triggers include "polish this," "edit my draft," "make this clearer," "tighten this up," "improve this writing," or "give this more authority."
---

# Prose Polish

Revise writing so it lands harder while still sounding like the author and saying exactly what the author meant.

The two cardinal sins of automated editing are **homogenization** (flattening every genre into the same smooth corporate voice) and **drift** (silently changing claims, adding facts, or inventing detail). This skill is built to avoid both. Every edit must be traceable to a craft problem, and every edit must leave meaning and voice intact.

## When to Use

Invoke when the user wants existing prose improved:
- "Polish / edit / revise / tighten / sharpen this"
- "Make this clearer / punchier / more authoritative / flow better"
- "Why does this read flat?" (diagnose-only mode)
- Any draft handed over for line editing or developmental notes

Do **not** use this to generate net-new content from a brief — that is drafting, not polishing. If there is no draft, ask for one.

## The Two Hard Constraints (never violate)

1. **Preserve meaning.** Do not add facts, examples, statistics, names, or claims the author did not make. Do not strengthen a hedged claim into a certain one, or soften a firm claim, unless asked. If a sentence is ambiguous, surface it as a question rather than guessing.
2. **Preserve voice.** Match the author's existing register, rhythm, and idiom. Improve *within* their voice — do not replace it with a generic "good writing" voice. A salty personal essay and a regulatory filing should not converge after editing. When unsure, edit conservatively.

If improving the prose would require breaking either constraint, stop and flag the tradeoff instead of guessing.

## Workflow: Structure Before Line

Edit top-down. Big-leverage problems live above the sentence; fixing word choice in a misordered argument is rearranging deck chairs. Always work in this order:

1. **Read once for intent.** What is the author trying to do, to whom, in what genre? Identify the through-line / thesis / call. Note the voice (formal? wry? technical? lyrical?). This frame governs every later decision.
2. **Diagnose** across the six dimensions below. Find the 2–4 problems with the highest payoff. Do not list everything — prioritize.
3. **Fix structure & flow.** Reorder for logical progression. Cut or merge redundant sections. Make sure the strongest point is positioned for impact (often the opening hook and the closing line). Ensure each paragraph has one job and transitions earn their place.
4. **Fix sentences.** Recast for clarity and rhythm: vary length, prefer active voice and strong verbs, surface the real subject, break or fuse where the breath demands it.
5. **Fix words.** Cut filler, deflate jargon, replace vague abstractions with concrete terms — *only where it sharpens meaning*, never to hit a word count or impose house style.
6. **Re-read against the constraints.** Did meaning shift? Did voice flatten? Roll back any edit that fails this check.

For the detailed dimension definitions, diagnostic questions, genre calibration, and before/after exemplars, read `references/craft-guide.md`. For the edit-pass mechanics and self-check, read `references/editing-protocol.md`.

## The Six Dimensions

Assess and improve across these. Genre shifts the target for each (see craft-guide):

1. **Clarity** — Can a first-time reader follow it without rereading? Are referents, claims, and logic unambiguous?
2. **Structure** — Does the order of ideas serve the argument? Does it open strong and close with force?
3. **Economy** — Is every sentence load-bearing? Filler, hedging, throat-clearing, and redundancy cut.
4. **Authority** — Do claims feel earned (specific, evidenced, confident) rather than vague or over-hedged? *Without inventing evidence.*
5. **Voice** — Is there a distinct, consistent human presence? Edits should sharpen it, not sand it off.
6. **Genre fit** — Does the register, structure, and diction match the form's conventions and the reader's expectations?

## Genre Awareness (anti-homogenization)

Before editing, name the genre and let it set the targets. A few defaults:

- **Essay / opinion** — voice and argument are paramount; protect the author's idiom and any deliberate informality. A strong hook and a resonant last line matter.
- **Technical / documentation** — precision and scannability win; ruthless economy, parallel structure, no flourish.
- **Business / email / memo** — lead with the ask or the bottom line; respect brevity and the reader's time.
- **Marketing / persuasive** — rhythm, concreteness, and a single clear benefit; cut hype that isn't backed.
- **Fiction / narrative** — preserve cadence, dialect, and intentional rule-breaking; "errors" may be craft. Edit lightly.

When the genre is unclear, infer it from cues and state your assumption.

## Economy Must Not Cost Authority (the vague-passage rule)

Trimming is not the goal; *sharpening* is. **Cutting a vague sentence shorter still leaves it vague** — and a shorter generic passage can read *flatter* than the longer one it replaced. When a passage is generic or hedged, you have exactly three honest moves, in order of preference:

1. **Sharpen it into the concrete** — but only using meaning already present or that the author plainly intends (recast "time is valuable as we all know" → "you reclaim the hour the commute used to eat"). This adds force without adding facts.
2. **Flag it for the author** — when the draft genuinely lacks the specific and you cannot supply one without inventing (the cardinal sin), leave a bracketed prompt: `[specify: a concrete example here]`. Do **not** fabricate the example, and do **not** silently smooth the gap away.
3. **Tighten as a last resort** — only after 1 and 2.

Never trade authority or voice for a lower word count. A faithful, vivid, slightly-longer line beats a faithful, flat, shorter one. Economy is in service of impact, not the reverse — especially in opinion/argument and narrative, where a flattened draft is a worse outcome than a wordy one.

## Output

Default to **two parts**:

1. **The revised text** — clean, ready to use.
2. **What changed and why** — a short, prioritized list (3–6 items) tying each major edit to a dimension and the author's goal. Flag any place you needed to preserve an ambiguous meaning, plus 1–2 judgment calls left to the author.

Offer **diagnose-only** mode (notes, no rewrite) when the user wants feedback rather than a rewrite, and **light/heavy** intensity (default light: smallest set of high-leverage edits). When in doubt, edit less and explain more.

## Anti-Patterns (do not do)

- Rewriting voice into bland "professional" prose.
- Adding examples, data, or claims to make a point land harder.
- Cutting deliberate stylistic choices (fragments, repetition, dialect) as "errors."
- Listing every nit instead of prioritizing the few edits that matter.
- Inflating word count with transitions and qualifiers in the name of "flow."
- Editing structure and sentences simultaneously and losing the thread.
