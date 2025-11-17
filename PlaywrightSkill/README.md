# Playwright Skill for Claude Code

**General-purpose browser automation as a Claude Skill**

A [Claude Skill](https://www.anthropic.com/news/skills) that enables Claude to write and execute any Playwright automation on-the-fly - from simple page tests to complex multi-step flows. Packaged as a [Claude Code Plugin](https://docs.claude.com/en/docs/claude-code/plugins) for easy installation and distribution.

Claude autonomously decides when to use this skill based on your browser automation needs, loading only the minimal information required for your specific task.

Made using Claude Code.

## Features

- **Any Automation Task** - Claude writes custom code for your specific request, not limited to pre-built scripts
- **Visible Browser by Default** - See automation in real-time with `headless: false`
- **Zero Module Resolution Errors** - Universal executor ensures proper module access
- **Progressive Disclosure** - Concise SKILL.md with full API reference loaded only when needed
- **Safe Cleanup** - Smart temp file management without race conditions
- **Comprehensive Helpers** - Optional utility functions for common tasks

## Installation

This repository is structured as a [Claude Code Plugin](https://docs.claude.com/en/docs/claude-code/plugins) containing a skill. You can install it as either a **plugin** (recommended) or extract it as a **standalone skill**.

### Understanding the Structure

This repository uses the plugin format with a nested structure:
```
playwright-skill/              # Plugin root
├── .claude-plugin/           # Plugin metadata
└── skills/
    └── playwright-skill/     # The actual skill
        └── SKILL.md
```

Claude Code expects skills to be directly in folders under `.claude/skills/`, so manual installation requires extracting the nested skill folder.

---

### Option 1: Plugin Installation (Recommended)

Install via Claude Code's plugin system for automatic updates and team distribution:

```bash
# Add this repository as a marketplace
/plugin marketplace add lackeyjb/playwright-skill

# Install the plugin
/plugin install playwright-skill@playwright-skill

# Navigate to the skill directory and run setup
cd ~/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill
npm run setup
```

Verify installation by running `/help` to confirm the skill is available.

---

### Option 2: Standalone Skill Installation

To install as a standalone skill (without the plugin system), extract only the skill folder:

**Global Installation (Available Everywhere):**
```bash
# Clone to a temporary location
git clone https://github.com/lackeyjb/playwright-skill.git /tmp/playwright-skill-temp

# Copy only the skill folder to your global skills directory
mkdir -p ~/.claude/skills
cp -r /tmp/playwright-skill-temp/skills/playwright-skill ~/.claude/skills/

# Navigate to the skill and run setup
cd ~/.claude/skills/playwright-skill
npm run setup

# Clean up temporary files
rm -rf /tmp/playwright-skill-temp
```

**Project-Specific Installation:**
```bash
# Clone to a temporary location
git clone https://github.com/lackeyjb/playwright-skill.git /tmp/playwright-skill-temp

# Copy only the skill folder to your project
mkdir -p .claude/skills
cp -r /tmp/playwright-skill-temp/skills/playwright-skill .claude/skills/

# Navigate to the skill and run setup
cd .claude/skills/playwright-skill
npm run setup

# Clean up temporary files
rm -rf /tmp/playwright-skill-temp
```

**Why this structure?** The plugin format requires the `skills/` directory for organizing multiple skills within a plugin. When installing as a standalone skill, you only need the inner `skills/playwright-skill/` folder contents.

---

### Option 3: Download Release

1. Download and extract the latest release from [GitHub Releases](https://github.com/lackeyjb/playwright-skill/releases)
2. Copy only the `skills/playwright-skill/` folder to:
   - Global: `~/.claude/skills/playwright-skill`
   - Project: `/path/to/your/project/.claude/skills/playwright-skill`
3. Navigate to the skill directory and run setup:
   ```bash
   cd ~/.claude/skills/playwright-skill  # or your project path
   npm run setup
   ```

---

### Verify Installation

Run `/help` to confirm the skill is loaded, then ask Claude to perform a simple browser task like "Test if google.com loads".

## Quick Start

After installation, simply ask Claude to test or automate any browser task. Claude will write custom Playwright code, execute it, and return results with screenshots and console output.

## Usage Examples

### Test Any Page
```
"Test the homepage"
"Check if the contact form works"
"Verify the signup flow"
```

### Visual Testing
```
"Take screenshots of the dashboard in mobile and desktop"
"Test responsive design across different viewports"
```

### Interaction Testing
```
"Fill out the registration form and submit it"
"Click through the main navigation"
"Test the search functionality"
```

### Validation
```
"Check for broken links"
"Verify all images load"
"Test form validation"
```

## How It Works

1. Describe what you want to test or automate
2. Claude writes custom Playwright code for the task
3. The universal executor (run.js) runs it with proper module resolution
4. Browser opens (visible by default) and automation executes
5. Results are displayed with console output and screenshots

## Configuration

Default settings:
- **Headless:** `false` (browser visible unless explicitly requested otherwise)
- **Slow Motion:** `100ms` for visibility
- **Timeout:** `30s`
- **Screenshots:** Saved to `/tmp/`

## Project Structure

```
playwright-skill/
├── .claude-plugin/
│   ├── plugin.json          # Plugin metadata for distribution
│   └── marketplace.json     # Marketplace configuration
├── skills/
│   └── playwright-skill/    # The actual skill (Claude discovers this)
│       ├── SKILL.md         # What Claude reads (314 lines)
│       ├── run.js           # Universal executor (proper module resolution)
│       ├── package.json     # Dependencies & setup scripts
│       └── lib/
│           └── helpers.js   # Optional utility functions
├── API_REFERENCE.md         # Full Playwright API reference (630 lines)
├── README.md                # This file - user documentation
├── CONTRIBUTING.md          # Contribution guidelines
└── LICENSE                  # MIT License
```

## Advanced Usage

Claude will automatically load `API_REFERENCE.md` when needed for comprehensive documentation on selectors, network interception, authentication, visual regression testing, mobile emulation, performance testing, and debugging.

## CI/CD Integration

### GitHub Actions

Complete workflow for running Playwright tests in CI:

```yaml
name: Playwright Tests
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - uses: actions/setup-node@v4
      with:
        node-version: '18'

    - name: Install dependencies
      run: npm ci

    - name: Install Playwright Browsers
      run: npx playwright install --with-deps chromium

    - name: Run Playwright tests
      run: npx playwright test

    - uses: actions/upload-artifact@v4
      if: always()
      with:
        name: playwright-report
        path: playwright-report/
        retention-days: 30
```

### GitLab CI

```yaml
playwright-tests:
  image: mcr.microsoft.com/playwright:v1.48.0-jammy
  stage: test
  script:
    - npm ci
    - npx playwright install --with-deps chromium
    - npx playwright test
  artifacts:
    when: always
    paths:
      - playwright-report/
    expire_in: 1 week
```

### Docker Integration

```dockerfile
FROM mcr.microsoft.com/playwright:v1.48.0-jammy

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .

# Install only Chromium for faster builds
RUN npx playwright install chromium

CMD ["npx", "playwright", "test"]
```

## Performance Testing

### Measuring Core Web Vitals

```javascript
// /tmp/playwright-test-performance.js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  await page.goto('http://localhost:3001', { waitUntil: 'networkidle' });

  // Measure performance metrics
  const metrics = await page.evaluate(() => {
    const navigation = performance.getEntriesByType('navigation')[0];
    const paint = performance.getEntriesByType('paint');

    return {
      // Core Web Vitals
      fcp: paint.find(p => p.name === 'first-contentful-paint')?.startTime,
      lcp: performance.getEntriesByType('largest-contentful-paint')[0]?.renderTime,
      cls: performance.getEntriesByType('layout-shift').reduce((sum, entry) =>
        sum + (entry.hadRecentInput ? 0 : entry.value), 0),

      // Load timing
      domContentLoaded: navigation.domContentLoadedEventEnd - navigation.fetchStart,
      loadComplete: navigation.loadEventEnd - navigation.fetchStart,

      // Resource timing
      transferSize: navigation.transferSize,
      encodedBodySize: navigation.encodedBodySize
    };
  });

  console.log('Performance Metrics:', JSON.stringify(metrics, null, 2));

  // Assert performance thresholds
  if (metrics.loadComplete > 3000) {
    console.warn('Page load time exceeds 3s threshold');
  }

  await browser.close();
})();
```

### Network Performance Testing

```javascript
// /tmp/playwright-test-network.js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const requests = [];
  const responses = [];

  page.on('request', request => {
    requests.push({
      url: request.url(),
      method: request.method(),
      resourceType: request.resourceType()
    });
  });

  page.on('response', response => {
    responses.push({
      url: response.url(),
      status: response.status(),
      contentType: response.headers()['content-type'],
      timing: response.timing()
    });
  });

  await page.goto('http://localhost:3001');
  await page.waitForLoadState('networkidle');

  console.log(`Total requests: ${requests.length}`);
  console.log(`Failed requests: ${responses.filter(r => r.status >= 400).length}`);

  // Analyze slow requests
  const slowRequests = responses
    .filter(r => r.timing && r.timing.responseEnd > 1000)
    .map(r => ({ url: r.url, duration: r.timing.responseEnd }));

  if (slowRequests.length > 0) {
    console.log('Slow requests (>1s):', slowRequests);
  }

  await browser.close();
})();
```

## Integration with Peer Review Skills

The Playwright Skill integrates seamlessly with AI peer review for test validation:

### Using with Codex Peer Review

```bash
# Run tests and get peer review
npx playwright test --reporter=json > test-results.json
codex review test-results.json --focus "test coverage and edge cases"
```

### Using with Gemini Peer Review

```bash
# Get architectural review of test structure
gemini analyze tests/ --context "E2E test architecture and patterns"

# Review test performance and optimization
gemini review playwright-report/ --focus "performance bottlenecks"
```

### Integration Pattern

Ask Claude to:
1. Write Playwright tests for your feature
2. Execute tests and capture results
3. Invoke peer review skill to analyze test quality
4. Iterate based on peer review feedback

Example:
```
"Write Playwright tests for the login flow, then use Gemini to review the test coverage"
```

## Dependencies

- Node.js >= 14.0.0
- Playwright ^1.48.0 (installed via `npm run setup`)
- Chromium (installed via `npm run setup`)

## Troubleshooting

**Playwright not installed?**
Navigate to the skill directory and run `npm run setup`.

**Module not found errors?**
Ensure automation runs via `run.js`, which handles module resolution.

**Browser doesn't open?**
Verify `headless: false` is set. The skill defaults to visible browser unless headless mode is requested.

**Install all browsers?**
Run `npm run install-all-browsers` from the skill directory.

## What is a Claude Skill?

[Skills](https://www.anthropic.com/news/skills) are modular capabilities that extend Claude's functionality. Unlike slash commands that you invoke manually, skills are model-invoked—Claude autonomously decides when to use them based on your request.

When you ask Claude to test a webpage or automate browser interactions, Claude discovers this skill, loads the necessary instructions, executes custom Playwright code, and returns results with screenshots and console output.

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, make your changes, and submit a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Learn More

- [Claude Skills](https://www.anthropic.com/news/skills) - Official announcement from Anthropic
- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Code Plugins Documentation](https://docs.claude.com/en/docs/claude-code/plugins)
- [Plugin Marketplaces](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)
- [API_REFERENCE.md](API_REFERENCE.md) - Full Playwright documentation
- [GitHub Issues](https://github.com/lackeyjb/playwright-skill/issues)

## License

MIT License - see [LICENSE](LICENSE) file for details.
