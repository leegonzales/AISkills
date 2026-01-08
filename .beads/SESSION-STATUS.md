# Session Status - Peer Review Skill Testing & Fixes

**Last Updated:** 2026-01-08
**Resume Command:** `bd ready` then read this file

---

## COMPLETED

### 1. Test Infrastructure Setup
- [x] Created test epics: SKILL-80t (Gemini), SKILL-8aw (Codex)
- [x] Created 23 granular test beads across both skills
- [x] Ran FMEA analysis (see `.beads/FMEA-peer-review-tests.md`)
- [x] Smoke tests passed for both CLIs

### 2. Critical Tests Executed
- [x] Gemini CLI Flags (SKILL-16w) - PASSED, found model name bug
- [x] Gemini Templates (SKILL-ajf) - PASSED
- [x] Gemini Synthesis (SKILL-bj2) - PASSED
- [x] Codex CLI Flags (SKILL-zmi) - PASSED, found --reasoning flag bug
- [x] Codex Templates (SKILL-edr) - PASSED

### 3. Documentation Bugs Found
| Bug ID | Skill | Issue | Status |
|--------|-------|-------|--------|
| SKILL-aon | Codex | `--reasoning` flag doesn't exist | **FIXING** |
| SKILL-3lh | Codex | Wrong sandbox mode names | **FIXED** |
| SKILL-oef | Gemini | Outdated model names | **FIXING** |
| SKILL-f5o | Gemini | gemini-2.0-flash returns error | **FIXING** |
| SKILL-qyq | Codex | Reasoning flag syntax | Duplicate of aon |

### 4. Fixes Applied (Partial)
- [x] Codex SKILL.md: Fixed sandbox modes (`workspace-read` → `read-only`)
- [x] Codex SKILL.md: Removed hardcoded model names, use CLI default
- [ ] Codex SKILL.md: Still need to check for `--reasoning` flag references
- [ ] Gemini SKILL.md: Remove hardcoded model names (use CLI default)
- [ ] Sync GitHub versions to local skill installations

### 5. Permissions Updated
- [x] Added auto-approve for skill directories in `~/.claude/settings.json`
- Paths allowed: `~/.claude/skills/**`, `~/Projects/leegonzales/AISkills/**`
- **Requires Claude Code restart to take effect**

---

## IN PROGRESS

### Fix Codex SKILL.md
**File:** `/Users/leegonzales/Projects/leegonzales/AISkills/CodexPeerReview/codex-peer-review/SKILL.md`

Already done:
- Fixed sandbox mode names
- Removed hardcoded model table

Still needed:
- Search for any `--reasoning` flag references and fix them
- Verify no other wrong flags

### Fix Gemini SKILL.md
**File:** `/Users/leegonzales/Projects/leegonzales/AISkills/GeminiPeerReview/gemini-peer-review/SKILL.md`

Needed:
- Remove all `--model gemini-X.X-*` from examples
- Update guidance to "let CLI default to latest"
- Remove/simplify "Current Latest Models" table

---

## PENDING

1. **Sync local skills with GitHub versions**
   - Copy fixed GitHub files to `~/.claude/skills/codex-peer-review/`
   - Copy fixed GitHub files to `~/.claude/skills/gemini-peer-review/`

2. **Close documentation bug beads**
   - Close SKILL-aon, SKILL-3lh, SKILL-oef, SKILL-f5o after fixes verified

3. **Continue remaining tests**
   - Gemini: Use Cases (SKILL-d8t), Multimodal (SKILL-5zs), Error Handling
   - Codex: Use Cases (SKILL-jx5), Synthesis (SKILL-aas), Selection Matrix

4. **Create PRs for skill fixes**
   - AISkills repo needs commits for documentation fixes

---

## KEY LEARNINGS

### Model Names - DO NOT HARDCODE
- **Gemini:** Don't specify `--model`. CLI defaults to latest.
- **Codex:** Don't specify model. CLI defaults to latest.
- Hardcoded model names go stale and cause errors.

### Codex CLI Actual Flags
```
--sandbox read-only|workspace-write|danger-full-access  (NOT workspace-read, NOT none)
-c 'model_reasoning_effort="low|medium|high"'           (NOT --reasoning)
--json                                                   (NOT --output json)
```

### Gemini CLI Actual Syntax
```bash
# Correct (positional/stdin)
gemini "prompt"
cat <<'EOF' | gemini

# Deprecated (still works but warns)
gemini -p "prompt"
```

---

## RESUME INSTRUCTIONS

1. Restart Claude Code (to pick up new permissions)
2. Run: `cd ~/Projects/leegonzales/AISkills && bd ready`
3. Read this file: `cat .beads/SESSION-STATUS.md`
4. Continue with "IN PROGRESS" items using subagents
