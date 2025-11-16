# Scripts Directory

This directory contains utility scripts for {{SKILL_NAME}}.

## Common Scripts

### validator.py
Validates skill functionality and outputs (optional).

**Usage:**
```bash
python3 validator.py [options]
```

### test_*.py
Test suites for skill validation (if applicable).

**Usage:**
```bash
pytest test_*.py -v
```

## Creating New Scripts

When adding scripts:
1. Make them executable: `chmod +x script-name.py`
2. Add shebang: `#!/usr/bin/env python3`
3. Include usage documentation in docstring
4. Follow PEP 8 style guidelines

---

Scripts are optional but recommended for skills with:
- Complex validation logic
- Data processing utilities
- Testing requirements
