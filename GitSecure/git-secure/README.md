# git-secure

Encrypt folders and files in a git repo so they're plaintext locally but encrypted on GitHub. Uses git-crypt for transparent encryption and age for versioned snapshots.

## Installation

This is a Claude Code skill. Add it to your Claude Code configuration to invoke via `/git-secure`.

### Prerequisites

- `git-crypt` — `brew install git-crypt`
- `age` — `brew install age`
- An initialized git repository

## Usage

Invoke `/git-secure` when you want to protect sensitive content (performance reviews, credentials configs, private docs, client data) in a git repo while keeping it version-controlled and readable locally.

The skill walks through an interactive flow:

1. **What to encrypt** — specify folder paths or glob patterns
2. **Snapshot strategy** — optional age-encrypted tar snapshots for recovery
3. **Key management** — backup key locations
4. **Execute setup** — installs git-crypt, writes `.gitattributes`, generates keys
5. **Update CLAUDE.md** — documents encryption for future sessions

## How It Works

- **git-crypt** handles transparent encryption/decryption via git filters. Files are plaintext in your working tree, encrypted binary blobs on GitHub.
- **age** (optional) creates versioned encrypted snapshots for point-in-time recovery independent of git history.

## Recovery

```bash
# Unlock repo on fresh clone
git-crypt unlock ~/.git-crypt-backups/<repo>.key

# Decrypt a snapshot
age -d -i ~/.age/<repo>-snapshots.key snapshot.tar.age | tar xf -

# Verify encryption status
git-crypt status <path>/
```

## Limitations

- Does not manage environment variable secrets or CI secrets (use a secrets manager)
- Does not encrypt individual values inside files (use `sops` for that)
- No access control — anyone with the git-crypt key decrypts everything
- Not a replacement for proper credential management for API keys/tokens
