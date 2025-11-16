# Distribution Directory

This directory contains packaged `.skill` files for Claude web chat.

## Contents

Packaged releases in ZIP format:
- `{{skill-name}}-v1.0.0.skill` - Version 1.0.0 release
- `{{skill-name}}-v1.0.0.skill.sha256` - SHA256 checksum

## Creating Packages

To create a new package:
```bash
# From AISkills root
./scripts/package-skill.sh {{skill-name}}
```

This will:
1. Validate skill structure
2. Create versioned ZIP file
3. Generate SHA256 checksum
4. Place files in this directory

## Installation

Users can download and upload these files to Claude web chat:
1. Download the `.skill` file
2. Go to claude.ai > Settings > Capabilities
3. Click "Upload skill"
4. Select the downloaded file

---

For Claude Code, users install from the source directory, not dist/.
