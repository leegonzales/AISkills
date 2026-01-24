# Distribution Packages

This directory contains packaged skill files for distribution.

## Available Packages

| Package | Version | Description |
|---------|---------|-------------|
| `profile-builder-v1.0.0.skill` | 1.0.0 | Initial release |

## How to Use

### Claude Code

Copy the skill directory (not the .skill file) to your skills folder:

```bash
cp -r ProfileBuilder/profile-builder ~/.claude/skills/
```

### Claude Web Chat

Upload the `.skill` file directly to any Claude conversation.

## Generating Packages

Use the SkillPackager tools:

```bash
cd /path/to/AISkills
./SkillPackager/scripts/package-skill.sh ProfileBuilder/profile-builder
```

This generates:
- `profile-builder-vX.Y.Z.skill` - ZIP package
- `profile-builder-vX.Y.Z.skill.sha256` - Checksum
- `profile-builder-vX.Y.Z.metadata.json` - Package metadata

## Verification

Verify package integrity:

```bash
shasum -a 256 -c profile-builder-v1.0.0.skill.sha256
```
