# FFmpeg Advanced Operations

Command patterns for GIF creation, frame extraction, HLS streaming, quality metrics, hardware acceleration, multi-pass encoding, and batch processing. See `reference-tables.md` for lookup tables (codecs, platform limits, quality interpretation, flags).

## GIF Creation

```bash
# High-quality GIF (two-pass with palette)
ffmpeg -i input.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png \
  -filter_complex "[0:v]fps=15,scale=480:-1:flags=lanczos[v];[v][1:v]paletteuse" output.gif

# Quick GIF (lower quality, single pass)
ffmpeg -i input.mp4 -vf "fps=10,scale=320:-1" -t 5 output.gif

# GIF from time range
ffmpeg -ss 5 -t 3 -i input.mp4 -vf "fps=15,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -ss 5 -t 3 -i input.mp4 -i palette.png \
  -filter_complex "[0:v]fps=15,scale=480:-1:flags=lanczos[v];[v][1:v]paletteuse" output.gif
```

## Thumbnails & Frame Extraction

```bash
# Single thumbnail at timestamp
ffmpeg -ss 00:00:10 -i input.mp4 -vframes 1 -q:v 2 thumb.jpg

# Thumbnail every N seconds
ffmpeg -i input.mp4 -vf "fps=1/10" thumb_%04d.jpg

# Keyframe extraction (scene changes)
ffmpeg -i input.mp4 -vf "select=eq(pict_type\,I)" -vsync vfr keyframe_%04d.jpg

# Scene detection (configurable threshold 0.0-1.0)
ffmpeg -i input.mp4 -vf "select='gt(scene,0.3)'" -vsync vfr scene_%04d.jpg

# Contact sheet / sprite sheet
ffmpeg -i input.mp4 -vf "fps=1/10,scale=160:-1,tile=5x4" contact_sheet.jpg

# Extract frame at specific resolution
ffmpeg -ss 5 -i input.mp4 -vframes 1 -vf "scale=1280:-1" frame.jpg
```

## HLS Streaming

```bash
# Create HLS stream from video
ffmpeg -i input.mp4 -c:v libx264 -c:a aac -f hls \
  -hls_time 10 -hls_list_size 0 -hls_segment_filename "segment_%03d.ts" \
  playlist.m3u8

# Multi-bitrate HLS (adaptive)
ffmpeg -i input.mp4 \
  -map 0:v -map 0:a -map 0:v -map 0:a \
  -c:v libx264 -c:a aac \
  -b:v:0 5M -s:v:0 1920x1080 \
  -b:v:1 2M -s:v:1 1280x720 \
  -f hls -hls_time 10 -hls_list_size 0 \
  -master_pl_name master.m3u8 \
  -var_stream_map "v:0,a:0 v:1,a:1" \
  stream_%v/playlist.m3u8

# Download HLS stream
ffmpeg -i "https://example.com/playlist.m3u8" -c copy output.mp4

# Download with auth headers
ffmpeg -headers "Authorization: Bearer TOKEN\r\n" \
  -i "https://example.com/playlist.m3u8" \
  -c copy -protocol_whitelist http,https,tcp,tls,crypto output.mp4
```

## Quality Metrics

See `reference-tables.md` for the interpretation table (PSNR/SSIM/VMAF thresholds).

```bash
# PSNR (Peak Signal-to-Noise Ratio) — higher is better
ffmpeg -i compressed.mp4 -i original.mp4 -lavfi psnr -f null -

# SSIM (Structural Similarity) — closer to 1.0 is better
ffmpeg -i compressed.mp4 -i original.mp4 -lavfi ssim -f null -

# VMAF (Netflix perceptual quality) — 0-100 scale
# Default model (FFmpeg 5.0+, uses built-in vmaf_v0.6.1)
ffmpeg -i compressed.mp4 -i original.mp4 -lavfi libvmaf -f null -
```

## Hardware Acceleration

```bash
# macOS (VideoToolbox)
ffmpeg -hwaccel videotoolbox -i input.mp4 -c:v h264_videotoolbox -q:v 50 output.mp4

# Linux NVIDIA (NVENC)
ffmpeg -hwaccel cuda -i input.mp4 -c:v h264_nvenc -preset p4 -cq 23 output.mp4

# Intel Quick Sync (QSV)
ffmpeg -hwaccel qsv -i input.mp4 -c:v h264_qsv -global_quality 23 output.mp4

# Check available hardware acceleration
ffmpeg -hwaccels

# Check available encoders
ffmpeg -encoders | grep -E "videotoolbox|nvenc|qsv"
```

## Multi-Pass Encoding

```bash
# Two-pass for target bitrate (best quality at file size)
ffmpeg -i input.mp4 -c:v libx264 -b:v 5M -pass 1 -f null /dev/null
ffmpeg -i input.mp4 -c:v libx264 -b:v 5M -pass 2 -c:a aac -b:a 192k output.mp4

# Target file size calculation
# target_bitrate = (target_size_MB * 8192) / duration_seconds - audio_bitrate
# Example: 50MB file, 120s video, 128k audio:
# video_bitrate = (50 * 8192) / 120 - 128 ≈ 3285 kbps
```

## Batch Processing

```bash
# Convert all files in directory
for f in *.avi; do
  ffmpeg -i "$f" -c:v libx264 -crf 23 -c:a aac "${f%.avi}.mp4"
done

# Batch with GNU parallel (faster)
ls *.avi | parallel -j4 'ffmpeg -i {} -c:v libx264 -crf 23 -c:a aac {.}.mp4'

# Multi-platform export from single source
export_all() {
  local input="$1"
  local base="${input%.*}"
  ffmpeg -i "$input" -c:v libx264 -crf 18 -preset slow -c:a aac -b:a 192k -movflags +faststart "${base}_youtube.mp4" &
  ffmpeg -i "$input" -c:v libx264 -crf 23 -vf "scale='min(1920,iw)':'min(1200,ih)':force_original_aspect_ratio=decrease" -c:a aac -b:a 128k -t 140 -movflags +faststart "${base}_twitter.mp4" &
  ffmpeg -i "$input" -c:v libx264 -crf 20 -vf "scale=-2:1080" -c:a aac -b:a 192k -movflags +faststart "${base}_linkedin.mp4" &
  wait
  echo "All exports complete"
}
# Usage: export_all input.mp4
```

## Validation Helper

```bash
validate_video() {
  local file="$1"
  if ffprobe -v error -select_streams v:0 -show_entries stream=codec_type -of csv=p=0 "$file" 2>/dev/null | grep -q "video"; then
    echo "✓ Valid: $(ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 "$file" 2>/dev/null)"
    return 0
  else
    echo "✗ Invalid or missing video stream"
    return 1
  fi
}
```
