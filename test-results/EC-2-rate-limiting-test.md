# EC-2: Rate Limiting Handling Test

## Test Objective
Test behavior when approaching API rate limits and verify graceful handling.

## Test Date
2025-01-12

## Known Rate Limits

### Gemini Free Tier
- **Per Minute:** 60 requests
- **Per Day:** 1,500 requests
- **Context Window:** 1M tokens (Gemini 2.5 Pro)
- **No credit card required**

### Codex Rate Limits
- Depends on ChatGPT subscription tier
- Plus/Pro/Team/Enterprise have higher limits
- Specific limits not publicly documented

## Test Approach

Since we cannot realistically hit rate limits in this test environment (would require 60+ rapid requests), we will:

1. Document expected behavior based on CLI error messages
2. Test a small burst of requests to verify no immediate issues
3. Assess how Claude should handle rate limit errors

## Small Burst Test

Let me send 5 rapid requests to verify normal operation:
