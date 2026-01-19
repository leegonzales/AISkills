# Essay to Speech

Transform written essays into spoken word presentations while preserving the source material for downstream processing.

## Overview

This skill converts written prose into natural spoken delivery. Unlike a simple "make this conversational" prompt, it:

1. **Segments** the essay into atomic chunks by argument/idea
2. **Transforms** each chunk from written to spoken language
3. **Preserves** both versions in a connected output structure

The connected output format is designed for pipeline processing—particularly for a downstream slide-builder skill that needs both the original content and the talk track.

## Usage

```
/essay-to-speech

[paste your essay]
```

Or simply ask Claude to transform an essay into a presentation format.

### Options

- **Standard output**: Clean talk track with original preserved
- **Annotated output**: Add `annotated` to get delivery markup (`[PAUSE]`, `*emphasis*`, etc.)

## Output Format

```markdown
# [Title]: Presentation Version

**Source**: [Original title]
**Chunks**: [N sections]

---

## Section 1: [Title]

### Original
[Verbatim essay text]

### Talk Track
[Spoken version]

---

## Section 2: [Title]
...
```

## What Gets Transformed

| Written | Spoken |
|---------|--------|
| Complex sentences | Shorter, punchier |
| "This essay examines..." | "Let me ask you something..." |
| Passive voice | Active voice |
| Academic hedging | Confident assertions |
| "In conclusion..." | Memorable landing |

## What Stays the Same

- Core arguments and claims
- Factual content
- Author's perspective and stance
- The original text (preserved verbatim in each section)

## Pipeline Context

This skill is the first step in a presentation pipeline:

```
Essay → [essay-to-speech] → Connected chunks
                                  ↓
                    [slide-builder] → Slides + speaker notes
```

The connected output ensures the slide-builder has access to:
- Original text (for accurate slide content)
- Talk track (for speaker notes)
- Logical chunking (for slide boundaries)

## References

- `references/transformation-patterns.md` - Detailed written→spoken patterns
- `references/examples.md` - Full before/after transformations

## Version

1.0.0
