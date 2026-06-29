# FFmpeg Reference Tables

Lookup tables for codec/profile selection, quality interpretation, platform limits, and useful flags.

## ProRes Profiles (Final Cut Pro)

| Profile | Flag | Quality | Use Case |
|---------|------|---------|----------|
| Proxy | `-profile:v 0` | Low | Offline editing |
| LT | `-profile:v 1` | Medium | Light grading |
| Standard | `-profile:v 2` | High | General editing |
| HQ | `-profile:v 3` | Very High | Final delivery |
| 4444 | `-profile:v 4` | Highest | VFX/compositing |

## Codec Selection Guide

| Use Case | Video Codec | Audio Codec | Container |
|----------|-------------|-------------|-----------|
| Web delivery | libx264 | aac | mp4 |
| Smaller web | libx265 | aac | mp4 |
| Open web | libvpx-vp9 | libopus | webm |
| Final Cut Pro | prores_ks | pcm_s16le | mov |
| Archive/lossless | ffv1 | flac | mkv |
| Quick preview | libx264 -preset ultrafast | aac | mp4 |
| Social media | libx264 -crf 20 | aac -b:a 192k | mp4 |

## Speed Reference (setpts / atempo)

atempo max 2.0 per filter — chain for higher multiples.

| Speed | setpts | atempo |
|-------|--------|--------|
| 0.25x (slow) | `4.0*PTS` | `atempo=0.5,atempo=0.5` |
| 0.5x | `2.0*PTS` | `atempo=0.5` |
| 1.5x | `0.667*PTS` | `atempo=1.5` |
| 2x | `0.5*PTS` | `atempo=2.0` |
| 4x | `0.25*PTS` | `atempo=2.0,atempo=2.0` |
| 8x | `0.125*PTS` | `atempo=2.0,atempo=2.0,atempo=2.0` |

## Platform Quick Reference

| Platform | Max Res | Max Size | Max Duration | Aspect |
|----------|---------|----------|-------------|--------|
| YouTube | 8K | 256GB | 12h | 16:9 |
| Twitter/X | 1920x1200 | 512MB | 2:20 | 16:9/1:1 |
| LinkedIn | 4096x2304 | 5GB | 10min | 16:9/1:1 |
| Instagram Reels | 1080x1920 | — | 90s | 9:16 |
| TikTok | 1080x1920 | — | 10min | 9:16 |

## Quality Metric Interpretation

| Metric | Excellent | Good | Fair | Poor |
|--------|-----------|------|------|------|
| PSNR | >40 dB | 35-40 | 30-35 | <30 |
| SSIM | >0.95 | 0.90-0.95 | 0.80-0.90 | <0.80 |
| VMAF | >90 | 75-90 | 60-75 | <60 |

## CRF / Preset Quality Guidelines

| Use Case | CRF | Preset | Notes |
|----------|-----|--------|-------|
| Archival | 15-18 | slow | Large files, maximum quality |
| Production | 18-22 | medium | Good balance |
| Web/sharing | 23-28 | medium | Smaller files |
| Preview/draft | 30-35 | ultrafast | Fast encoding, lower quality |

## Useful Flags

| Flag | Purpose |
|------|---------|
| `-movflags +faststart` | Web playback (moov atom at start) |
| `-pix_fmt yuv420p` | Maximum compatibility |
| `-threads 0` | Auto-detect CPU threads |
| `-max_muxing_queue_size 1024` | Fix muxing queue overflow |
| `-y` | Overwrite output without asking |
| `-n` | Never overwrite |
| `-hide_banner` | Suppress version info |
| `-progress pipe:1` | Machine-readable progress |
