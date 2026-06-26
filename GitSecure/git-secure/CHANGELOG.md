# Changelog — git-secure

## [1.1.0] — 2026-06-25

### Added

- **Verification Gate** — mandatory before claiming encryption works: run `git-crypt status` AND prove the committed blob is ciphertext (`git show HEAD:<path> | xxd`). Closes a confirm-without-verify gap where a malformed `.gitattributes` could silently no-op encryption while the user was told they were protected.
- **History-leak gate** — when a target file was already committed in plaintext, the skill now surfaces the leak prominently (old commits/remote still hold plaintext), recommends `git filter-repo` scrubbing, and recommends rotating exposed secrets — instead of falsely reassuring that new encryption protects old history.
- Verification step wired into Step 4 (Execute Setup) and strengthened the Recovery "Verify encryption status" procedure.
- LICENSE file (MIT).

## [1.0.0] — 2026-03-19

### Added

- Initial skill definition
- Interactive flow: target selection, snapshot strategy, key management, setup execution
- git-crypt transparent encryption with `.gitattributes` scoping
- age-based versioned snapshot support
- CLAUDE.md template block for documenting encryption in repos
- Recovery procedures (unlock, snapshot decrypt, status check)
- Edge case documentation (monorepo, CI, nested attributes, large binaries)
