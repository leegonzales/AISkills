# Troubleshooting osgrep

Common issues and solutions.

## No Results Returned

### Check if index exists
```bash
osgrep list
```

If your repo isn't listed, create an index:
```bash
osgrep index
```

### Index might be stale
If files were added/changed since indexing:
```bash
osgrep search "query" --sync
```

Or re-index:
```bash
osgrep index
```

### Query too specific
Try broader queries:
- ❌ `"calculateTaxForUSCustomersInCalifornia"`
- ✅ `"tax calculation for customers"`

## Poor Quality Results

### Query too vague
Add descriptive context:
- ❌ `"auth"`
- ✅ `"user authentication and login session management"`

### Wrong domain
osgrep uses semantic embeddings. Technical queries work better than:
- Acronyms without context
- Internal project jargon
- Abbreviated variable names

### Check scores
```bash
osgrep search "query" --scores
```
Low scores (<0.1) indicate poor matches.

## osgrep Not Found

### Check installation
```bash
which osgrep
osgrep --version
```

### Check health
```bash
osgrep doctor
```

Should show all ✅. If models missing:
```bash
osgrep setup
```

## Slow Searches

### Large codebase
First search loads models (~2-3s). Subsequent searches are faster.

### Use background server
For frequent searches:
```bash
osgrep serve
```

### Limit results
```bash
osgrep search "query" --max-count 5
```

## Index Errors

### Permission issues
Ensure write access to `~/.osgrep/data/`

### Disk space
Vector stores can be large for big repos. Check:
```bash
du -sh ~/.osgrep/data/*
```

### Corrupt store
Remove and re-index:
```bash
rm -rf ~/.osgrep/data/projectname.lance
osgrep index
```

## Output Issues

### Too much output
```bash
osgrep search "query" --compact      # File paths only
osgrep search "query" --max-count 5  # Fewer results
```

### Need more context
```bash
osgrep search "query" --content      # Full chunk content
osgrep search "query" --per-file 3   # Multiple matches per file
```

### Need machine-readable
```bash
osgrep search "query" --json
```
