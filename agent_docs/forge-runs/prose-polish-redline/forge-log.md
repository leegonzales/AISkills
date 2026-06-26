# Forge Log — prose-polish-redline (SKILL-l30)

**Diagnosis (from audit):** the redline skill predated prose-polish's Fidelity Firewall and shared its fabrication risk — worse, because it auto-applies edits to a .docx with no human in the loop, and the `insert` edit_type has no `original_text` so the verbatim guard can't catch an invented citation. The smoking gun: `edit-schema.md`'s canonical `insert` example literally inserted `" (Schuch et al., 2019)"` ("Ground delegated authority with specific citation"), and `authority-agent.md` listed "Research shows" → "Sweller's (1988)..." as an acceptable surgical swap — both teaching fabrication, contradicting their own "don't invent" rules.

**Fix (port the firewall):**
- SKILL.md: new top-level **Fidelity Firewall** binding all agents — no edit may introduce a citation/stat/number/date/name/quote/fact not in the source; three honest moves (sharpen / comment / soften); `insert` may add connective phrasing ONLY (the bypass path is named explicitly).
- edit-schema.md: replaced the citation-injecting `insert` example with a connective-phrasing example + a ⚠ FIDELITY callout; fixed the `replace` example that invented "40%".
- authority-agent / claims-agent / stakes-agent: elevated the buried "(only if already in the document)" caveats into a foregrounded **FIDELITY FIREWALL** Critical Rule in each (agents run as independent subagents, so each must carry it).
- Added MIT LICENSE (was missing). Validates clean.

**Verification (the proof):** ran the hardened authority + claims agents on a deliberately citation-thin, claim-heavy draft (`thin-draft.md` — "Research shows", "Studies indicate", "experts agree", zero references/numbers). Result: **14 edits, ZERO fabrications.** Every `comment` flagged the gap and refused to invent ("the author must supply the source — I won't invent one"); every `replace` was pure phrasing (no citation/number/date added); no `insert` of a citation. The pre-firewall version (per the prose-polish precedent + the schema's own examples) would have injected "Sweller (1988)" / "(Schuch et al., 2019)". Firewall holds.

**Status:** forged. Limitation: verified on the two highest-risk agents against one thin draft (directional, consistent with the campaign's other runs); a full-pipeline .docx run + cross-model panel would make it conclusive.
