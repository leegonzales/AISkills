#!/usr/bin/env python3
"""
Test skill loading and YAML parsing
Usage: python3 test-skill-loading.py <skill-directory>
"""

import sys
import yaml
from pathlib import Path


def test_skill(skill_dir: Path):
    """Test skill YAML frontmatter loading."""
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        print(f"❌ SKILL.md not found in {skill_dir}")
        return False

    # Read file
    content = skill_md.read_text(encoding='utf-8')

    # Extract frontmatter
    if not content.startswith('---\n'):
        print("❌ SKILL.md must start with ---")
        return False

    # Find end of frontmatter
    parts = content[4:].split('\n---\n', 1)
    if len(parts) != 2:
        print("❌ Could not parse YAML frontmatter")
        return False

    frontmatter_text, markdown_body = parts

    # Parse YAML
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing failed: {e}")
        return False

    # Validate required fields
    if 'name' not in frontmatter:
        print("❌ Missing required field: name")
        return False

    if 'description' not in frontmatter:
        print("❌ Missing required field: description")
        return False

    # Validate name format
    name = frontmatter['name']
    if not isinstance(name, str) or not name:
        print(f"❌ Invalid name: {name}")
        return False

    if not all(c.islower() or c.isdigit() or c == '-' for c in name):
        print(f"❌ Name must use lowercase, numbers, hyphens only: {name}")
        return False

    if len(name) > 64:
        print(f"❌ Name exceeds 64 characters: {len(name)}")
        return False

    # Validate description
    desc = frontmatter['description']
    if not isinstance(desc, str) or not desc:
        print(f"❌ Invalid description")
        return False

    if len(desc) > 1024:
        print(f"⚠️  Description exceeds 1024 characters: {len(desc)}")

    # Check for unsupported fields
    supported_fields = {'name', 'description', 'allowed-tools', 'license', 'environment'}
    unsupported = set(frontmatter.keys()) - supported_fields
    if unsupported:
        print(f"⚠️  Unsupported frontmatter fields: {unsupported}")

    # Success
    print(f"✅ SKILL.md loads successfully")
    print(f"   Name: {name}")
    print(f"   Description: {desc[:80]}...")
    print(f"   Markdown body: {len(markdown_body)} chars")

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 test-skill-loading.py <skill-directory>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    success = test_skill(skill_dir)
    sys.exit(0 if success else 1)
