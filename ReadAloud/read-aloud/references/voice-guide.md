# Read Aloud — Voice Guide

## Kokoro Voice Variants

Kokoro is an 82M parameter TTS model optimized for Apple Silicon via MLX. It supports multiple voice variants with distinct characteristics.

### American Voices

| Voice ID | Gender | Style | Character |
|----------|--------|-------|-----------|
| `af_heart` | Female | Warm, expressive | Default. Natural cadence, slight breathiness. Best all-around voice for essays and narratives. |
| `af_bella` | Female | Clear, articulate | Precise enunciation. Good for technical content where clarity matters. |
| `af_nicole` | Female | Conversational | Relaxed, informal tone. Good for blog posts and casual writing. |
| `af_sarah` | Female | Professional | Measured, newscaster-like. Good for reports and formal content. |
| `am_adam` | Male | Deep, resonant | Authoritative bass. Good for persuasive and argumentative pieces. |
| `am_michael` | Male | Neutral, clear | General-purpose male voice. Clean and balanced. |

### British Voices

| Voice ID | Gender | Style | Character |
|----------|--------|-------|-----------|
| `bf_emma` | Female | Elegant, refined | Literary quality. Good for formal essays and philosophical content. |
| `bm_george` | Male | Distinguished | Classic narrator voice. Good for technical and formal writing. |

## Speed Recommendations

| Content Type | Recommended Speed | Why |
|-------------|-------------------|-----|
| Proofreading | `0.9` | Slower pace helps catch awkward phrasing |
| Narrative essays | `1.0` | Natural reading pace |
| Technical content | `0.95` | Slightly slower for complex concepts |
| Blog posts | `1.05` | Slightly brisk, conversational feel |
| News/updates | `1.1` | Efficient information delivery |
| Casual listening | `1.15–1.25` | Background listening pace |

### Speed × Voice Interactions

Some voices sound better at certain speeds:

- **af_heart** — Best at 0.9–1.1. Gets breathy above 1.2.
- **bm_george** — Excellent at 1.0–1.2. Maintains clarity even at higher speeds.
- **am_adam** — Deep voice can sound muddy above 1.15. Best at 0.9–1.1.
- **af_bella** — Clear at any speed. Good choice if you want to listen at 1.2+.

## Choosing a Voice

**For proofreading your own writing:**
Use a voice that contrasts with how you hear yourself. If you write in a conversational male voice, try `bf_emma` or `af_heart` — the contrast makes awkward phrases jump out.

**For sharing with readers:**
Match the voice to the content tone:
- Warm, personal essay → `af_heart`
- Technical explainer → `af_bella` or `bm_george`
- Persuasive argument → `am_adam`
- Literary/philosophical → `bf_emma`

**For accessibility:**
Any voice works. Consider `af_bella` or `am_michael` for maximum clarity, especially if listeners may have hearing difficulties.

## Model Details

- **Model:** `mlx-community/Kokoro-82M-bf16` (BFloat16, optimized for Apple Silicon)
- **Sample rate:** 24,000 Hz
- **First-run download:** ~200 MB (cached at `~/.cache/huggingface/`)
- **Generation speed:** ~10x realtime on M1 Pro (a 10-second clip generates in ~1 second)
