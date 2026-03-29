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
6. **Handle already-committed files**: If any target files are already in git history unencrypted:
   - Warn the user: "These files exist unencrypted in git history. They'll be encrypted going forward, but old commits still contain plaintext."
   - Offer to re-stage them (`git rm --cached` + `git add`) so the next commit stores them encrypted
   - Offer history scrubbing via `git filter-repo` (destructive — confirm explicitly)
7. **Create initial snapshot** (if snapshots enabled)
8. **Create git tag** at the encryption baseline: `git-secure/<target>-baseline`
9. **Update CLAUDE.md** with encryption instructions specific to this repo

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
```bash
git-crypt status <target>/
```

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
