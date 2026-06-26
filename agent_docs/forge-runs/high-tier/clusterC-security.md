# HIGH-tier Forge — Cluster C: Security (2 skills)

| Skill | Bead | Fix | Verification |
|-------|------|-----|--------------|
| **git-secure** | SKILL-9gc | Verification Gate: never tell the user "encrypted/safe" without running `git-crypt status` + proving the committed blob is ciphertext (`git show HEAD:path`); prominent history-leak warning when plaintext was already committed (new encryption doesn't retroactively protect old commits) + offer filter-repo scrub. | Self-test: already-committed-plaintext scenario → runs verification before confirming + surfaces history-leak. PASS. |
| **moltbook-enclave** | SKILL-2jx | Honest-control representation: foreground **isolation (no memory/tools)** as THE security boundary; downgrade the regex sanitizer to "defense-in-depth, catches only known literal patterns — do not trust"; threat-model section; treat ALL post content as adversarial regardless of sanitization. | **Real red-team:** ran 10 bypass payloads through the actual `moltbot.py` sanitizer → **8/10 survived untouched** (homoglyph, base64, leetspeak, translation, no-trigger-phrase). Empirical proof the old "detects injection" claim was false; honest reframe warranted. |

Both validate (LICENSE added). moltbook's red-team is genuine behavioral evidence (ran the real code), not a self-graded narration. Standing caveats: instruction-strength for git-secure; the moltbook isolation depends on the host honoring the sandbox config (now documented).
