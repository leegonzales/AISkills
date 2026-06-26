---
name: git-secure
description: Encrypt folders and files in a git repo so they're plaintext locally but encrypted on GitHub. Uses git-crypt for transparent encryption and age for versioned snapshots.
---

# /git-secure

Encrypt folders and files in a git repo so they're plaintext locally but encrypted on GitHub. Uses git-crypt for transparent encryption and age for versioned snapshots.

## When to Use

Run `/git-secure` when you want to protect sensitive content (performance reviews, credentials configs, private docs, client data) in a git repo while keeping it version-controlled and seamlessly readable locally.

## Prerequisites

- `git-crypt` (installed via `brew install git-crypt`)
- `age` (installed via `brew install age`)
- An initialized git repo

## Verification Gate (never tell the user they're protected without proving it)

**You MUST NOT tell the user their data is encrypted, "safe to push," or "protected" until you have run the verification below and shown them its output. Writing `.gitattributes` is not proof — a malformed or mis-scoped attributes file silently no-ops encryption, leaving plaintext committed while the user believes they are covered. Claiming protection on the basis of setup steps alone is a confirm-without-verify failure. Prove it, then claim it.**

Before saying anything reassuring, run and show BOTH checks:

1. **git-crypt status** — confirm the intended files are listed as `encrypted`, not `not encrypted`:
   ```bash
   git-crypt status <target>/
   ```
   Every file you meant to protect must appear under `encrypted`. If any appears as `not encrypted`, encryption is NOT working — stop and fix `.gitattributes` (wrong path, wrong glob, or `.gitattributes` not committed) before continuing.

2. **Prove the committed blob is ciphertext** — inspect what git actually stored, not the working tree (the working tree is always plaintext and tells you nothing):
   ```bash
   git show HEAD:<target>/<file> | head -c 200 | xxd | head
   ```
   You must see the git-crypt header (the file begins with the bytes `\0GITCRYPT\0`) followed by binary ciphertext — NOT readable plaintext. If you can read the secret in this output, it is committed in the clear. Do not tell the user they are protected.

Only after BOTH checks pass — files listed as `encrypted` AND committed blob shows ciphertext — may you state that encryption is working. Quote the actual command output to the user; do not paraphrase "looks good."

### History-leak gate (encryption does not retroactively protect old commits)

If any file you are about to encrypt was **already committed in plaintext** (check with `git log --all --full-history -- <path>` — any prior commits mean it has been stored in the clear), you MUST surface this prominently BEFORE any reassurance:

> ⚠️ **History leak:** `<path>` already exists as plaintext in earlier commits (and on any remote you've already pushed to). Turning on encryption now only protects *future* commits — it does NOT scrub the plaintext sitting in past commits. Anyone with repo or remote access can `git show <old-sha>:<path>` and read it. Pushing now does not fix this.

Then offer the remediation path explicitly — do not let the user believe new encryption covers old history:

- **Scrub history** with `git filter-repo` (rewrites every commit to remove/re-encrypt the file; destructive, rewrites SHAs, requires force-push and coordination with anyone who has clones). Confirm explicitly before running.
- **Rotate the exposed secrets** — if the leaked plaintext contained credentials/keys/tokens, treat them as compromised and rotate them regardless of scrubbing, since the plaintext may already have been cloned or cached.

Never answer "is my data safe to push now?" with an unqualified "yes" when prior plaintext commits exist. The correct answer is: future commits are encrypted (proven above), but the existing history still leaks until scrubbed and the exposed secrets are rotated.

## Interactive Flow

When invoked, walk through these steps with the user:

### Step 1: What to Encrypt

Ask: "What do you want to encrypt?"
Accept:
- A folder path (e.g., `touchpoint/`, `secrets/config/`)
- A glob pattern (e.g., `*.secret.yml`, `private/**`)
- Multiple targets

### Step 2: Snapshot Strategy

Ask: "Do you want versioned snapshots for recovery?"
Options:
- **Yes (recommended)**: Create age-encrypted tar snapshots before modifications
- **No**: Rely on git history alone

If yes, ask:
- Snapshot location (default: `<target>/.snapshots/`)
- Auto-snapshot before modify? (default: yes)

### Step 3: Key Management

Ask: "Where should backup keys be stored?"
- git-crypt key default: `~/.git-crypt-backups/<repo-name>.key`
- age key default: `~/.age/<repo-name>-snapshots.key`
- Remind user to back up to a secure external location

### Step 4: Execute Setup

1. **Check dependencies**: Verify git-crypt and age are installed. Offer to `brew install` if missing.
2. **Initialize git-crypt** if not already done (`git-crypt init`)
3. **Write `.gitattributes`** in the target directory:
   ```
   * filter=git-crypt diff=git-crypt
   .gitattributes !filter !diff
   ```
4. **Generate age key** for snapshots (if enabled)
5. **Export and backup git-crypt key**
6. **Handle already-committed files**: For every target, run `git log --all --full-history -- <path>`. If it returns prior commits, the file is already plaintext in history — trigger the **History-leak gate** (see Verification Gate section above): warn prominently, re-stage (`git rm --cached` + `git add`) so the next commit stores ciphertext, offer `git filter-repo` scrubbing (destructive — confirm explicitly), and recommend rotating any exposed secrets.
7. **Create initial snapshot** (if snapshots enabled)
8. **Create git tag** at the encryption baseline: `git-secure/<target>-baseline`
9. **RUN THE VERIFICATION GATE**: Commit the `.gitattributes` (and re-staged files), then run both checks from the Verification Gate section — `git-crypt status <target>/` and `git show HEAD:<target>/<file> | xxd | head`. Show the output. Do NOT proceed to tell the user they are protected until both pass.
10. **Update CLAUDE.md** with encryption instructions specific to this repo

### Step 5: Update CLAUDE.md

Append an "Encrypted Directories" section (or update existing) with:
- Which paths are encrypted
- "Always read from working tree, not git objects"
- "If files appear as binary, run `git-crypt unlock`"
- Snapshot creation command with the correct age public key
- Key backup locations
- "Never force-push branches with encrypted content"
- Auto-snapshot rule: "Before modifying encrypted files, create a snapshot first"

## CLAUDE.md Template Block

```markdown
## Encrypted Directories

`<target>/` is encrypted via **git-crypt**. Contains <description>.

- **Locally:** Files are plaintext when repo is unlocked. Read/edit normally from the working tree.
- **On GitHub:** Files appear as encrypted binary blobs.
- **Fresh clone:** Run `git-crypt unlock` once after cloning.
- **Never read encrypted files from git objects** (e.g., `git show HEAD:path/...`) — use the working tree.
- **Before modifying encrypted files:** Create a snapshot:
  ```
  tar cf - --exclude='<target>/.snapshots' <target>/ | age -r <PUBLIC_KEY> -o <target>/.snapshots/YYYY-MM-DD-description.tar.age
  ```
- **Key backups:**
  - git-crypt: `~/.git-crypt-backups/<repo>.key`
  - age: `~/.age/<repo>-snapshots.key`
- **Never force-push branches with encrypted content.**
```

## Recovery Procedures

### Decrypt a snapshot
```bash
age -d -i ~/.age/<repo>-snapshots.key <target>/.snapshots/<snapshot>.tar.age | tar xf -
```

### Unlock repo on fresh clone
```bash
git-crypt unlock  # uses key from ~/.git-crypt/keys/default
# OR
git-crypt unlock ~/.git-crypt-backups/<repo>.key
```

### Verify encryption status
Run the full **Verification Gate** (both checks), not just `git-crypt status` alone:
```bash
git-crypt status <target>/                          # files must show as "encrypted"
git show HEAD:<target>/<file> | head -c 200 | xxd   # committed blob must be ciphertext, not plaintext
```
Status alone can be misleading on an uncommitted or partially-staged tree — always confirm the committed blob is ciphertext before declaring success.

## Edge Cases

- **Monorepo with multiple encrypted dirs**: Each gets its own `.gitattributes`. All share the same git-crypt key.
- **Adding encryption to an existing repo with CI**: CI won't be able to read encrypted files without the key. Document this.
- **Nested `.gitattributes`**: git-crypt respects the closest `.gitattributes`, so encryption scopes naturally to subdirectories.
- **Large binary files in encrypted dirs**: git-crypt encrypts deterministically, so identical plaintext = identical ciphertext. But encrypted diffs are useless — rely on snapshots for large binary rollback.

## What This Skill Does NOT Do

- Manage secrets in environment variables or CI (use a secrets manager)
- Encrypt individual values inside files (use `sops` for that)
- Provide access control (anyone with the git-crypt key can decrypt everything)
- Replace proper credential management for API keys/tokens
