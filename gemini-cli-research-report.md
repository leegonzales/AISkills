# Google Gemini CLI: Comprehensive Research Report
**Generated:** 2025-11-12
**Purpose:** Foundation for Claude Code skill development for Gemini peer review

---

## Table of Contents
1. [Official Documentation](#1-official-documentation)
2. [Installation & Authentication](#2-installation--authentication)
3. [Command Structure](#3-command-structure)
4. [Key Flags & Options](#4-key-flags--options)
5. [Available Models](#5-available-models)
6. [Use Cases](#6-use-cases)
7. [Differences from Other AI CLI Tools](#7-differences-from-other-ai-cli-tools)
8. [Rate Limits & Pricing](#8-rate-limits--pricing)
9. [Example Commands](#9-example-commands)
10. [Strengths & Weaknesses](#10-strengths--weaknesses)
11. [MCP Integration](#11-mcp-integration)

---

## 1. Official Documentation

### Primary Sources
- **Official GitHub Repository:** https://github.com/google-gemini/gemini-cli
  - Apache 2.0 license
  - 82,287+ stars (as of Nov 2025)
  - Active development with weekly releases

- **Official Documentation Sites:**
  - Google Developers: https://developers.google.com/gemini-code-assist/docs/gemini-cli
  - Google Cloud: https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli
  - CLI Documentation Hub: https://google-gemini.github.io/gemini-cli/docs/

- **Learning Resources:**
  - Google Codelabs: https://codelabs.developers.google.com/gemini-cli-hands-on
  - DataCamp Tutorial: https://www.datacamp.com/tutorial/gemini-cli
  - Official Tutorial Series: https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718

### Description
"An open-source AI agent that brings the power of Gemini directly into your terminal."

---

## 2. Installation & Authentication

### System Requirements
- **Node.js:** Version 20 or higher (required)
- **Operating Systems:** macOS, Linux, or Windows
- **Internet:** Constant connectivity required (cloud-based processing)

### Installation Methods

#### Quick Install (No Installation Required)
```bash
npx https://github.com/google-gemini/gemini-cli
```

#### Global NPM Installation
```bash
npm install -g @google/gemini-cli
```

#### Homebrew (macOS/Linux)
```bash
brew install gemini-cli
```

#### Verification
```bash
gemini --version
```

### Release Channels
1. **Latest (Stable):** Weekly releases published Tuesdays at UTC 2000
2. **Preview:** Weekly releases Tuesdays at UTC 2359 (pre-vetted but may contain issues)
3. **Nightly:** Daily releases at UTC 0000 (all main branch changes, pending validation)

### Authentication Options

#### Option 1: Login with Google (Recommended for Individuals)
```bash
gemini
# Select "Login with Google" from the authentication dialog
# CLI opens browser for OAuth flow
```

**Benefits:**
- No API key management required
- Free tier: 60 requests/min, 1,000 requests/day
- Access to Gemini 2.5 Pro with 1M token context window

#### Option 2: Gemini API Key
1. Obtain API key from Google AI Studio: https://aistudio.google.com/apikey
2. Set environment variable:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Benefits:**
- Free tier: 100 requests/day
- Usage-based billing for higher limits
- Model selection flexibility

**Limitations:**
- Requires manual key management
- Security responsibility on user

#### Option 3: Vertex AI (Enterprise)
**Option A - Application Default Credentials (ADC):**
```bash
# Ensure Google Cloud project is configured
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"  # or your preferred region

# Authenticate with gcloud
gcloud auth application-default login
```

**Option B - Service Account:**
```bash
# Create service account and download JSON key
# Assign "Vertex AI User" role

# Set credentials path
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

**Benefits:**
- Enterprise security and compliance
- Higher rate limits with billing account
- Integration with Google Cloud infrastructure

### Persisting Credentials

Create `.gemini/.env` file in project directory or home directory:

```bash
# In project directory
mkdir -p .gemini
cat > .gemini/.env << EOF
GEMINI_API_KEY=your-api-key-here
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
EOF
```

**Note:** Gemini CLI automatically loads variables from the first `.env` file it finds. `.gemini/.env` is recommended and respects `.gitignore`.

---

## 3. Command Structure

### Basic Usage

#### Interactive Mode
```bash
gemini
# Launches interactive prompt: gemini>
```

#### Non-Interactive Mode (One-Shot)
```bash
gemini -p "Your prompt here"
gemini --prompt "Summarize this file @./report.txt"
```

#### Interactive Mode with Initial Prompt
```bash
gemini -i "Initial prompt to start session"
gemini --prompt-interactive "Analyze this codebase"
```

### Command Categories

#### 1. Slash Commands (/)
Session and tool management commands starting with `/`

```bash
/help           # Display help
/tools          # List available tools
/settings       # Open settings editor
/stats          # Show token usage
/quit           # Exit CLI
```

#### 2. At Commands (@)
File and resource references using `@`

```bash
@path/to/file.txt           # Include file content
@path/to/directory/         # Include directory contents
@image.png                  # Include image
@document.pdf               # Include PDF
```

#### 3. Shell Commands (!)
Execute shell commands directly

```bash
!ls -la                     # Run shell command
!git status                 # Git commands
!                           # Toggle shell mode
```

### Input Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Z` | Undo last input action |
| `Ctrl+Shift+Z` | Redo last undone action |
| `Ctrl+L` | Clear terminal screen |
| `Ctrl+T` | Toggle tool descriptions visibility |
| `Ctrl+Y` | Enable YOLO mode (auto-approve tools) |

---

## 4. Key Flags & Options

### Core Flags

```bash
# Model Selection
--model gemini-2.5-pro              # Use Pro model
--model gemini-2.5-flash            # Use Flash model
--model gemini-2.5-flash-lite       # Use Flash-Lite model

# Output Formats
--output-format json                # Structured JSON output
--output-format stream-json         # Newline-delimited JSON events

# Execution Modes
-p, --prompt "text"                 # Non-interactive mode
-i, --prompt-interactive "text"     # Interactive with initial prompt
--yolo                              # Auto-approve all tool calls
-s, --sandbox                       # Enable sandbox mode
-d, --debug                         # Enable debug mode

# Session Management
--session-summary                   # Persist session summary
--checkpointing                     # Enable checkpointing

# Configuration
-c, --config string                 # Path to config file (JSON)

# Display Options
-t, --style string                  # Markdown style (ascii, dark, light, pink)
-w, --wrap int                      # Line length for word wrapping
--multiline                         # Read input as multi-line string
-v, --version                       # Show version
-h, --help                          # Show help
```

### Environment Variables

```bash
# Authentication
GEMINI_API_KEY                      # Google AI Studio API key
GOOGLE_APPLICATION_CREDENTIALS      # Service account JSON path
GOOGLE_CLOUD_PROJECT                # GCP project ID
GOOGLE_CLOUD_LOCATION               # GCP region

# Configuration
GEMINI_SANDBOX                      # Enable sandbox mode
```

---

## 5. Available Models

### Current Generation (Gemini 2.5 Series)

#### Gemini 2.5 Pro (`gemini-2.5-pro`)
- **Focus:** State-of-the-art reasoning over complex problems
- **Context Window:** 1,048,576 input tokens / 65,536 output tokens
- **Inputs:** Audio, images, video, text, PDF
- **Key Capabilities:**
  - Advanced reasoning and thinking
  - Code execution
  - Function calling
  - Structured outputs
  - Search grounding
  - Context caching
- **Best For:**
  - Complex reasoning tasks
  - Large codebase analysis
  - Multi-step problem solving
  - Data analysis requiring deep thought

#### Gemini 2.5 Flash (`gemini-2.5-flash`)
- **Focus:** Best price-performance ratio
- **Context Window:** 1,048,576 input tokens / 65,536 output tokens
- **Inputs:** Text, images, video, audio
- **Key Capabilities:**
  - Thinking mode
  - Function calling
  - Code execution
  - File search
  - Structured outputs
- **Best For:**
  - Large-scale processing
  - Agentic tasks
  - Low-latency applications
  - Everyday development tasks

#### Gemini 2.5 Flash-Lite (`gemini-2.5-flash-lite`)
- **Focus:** Fastest, most cost-efficient
- **Context Window:** 1,048,576 input tokens / 65,536 output tokens
- **Inputs:** Text, image, video, audio, PDF
- **Key Capabilities:**
  - Function calling
  - Code execution
  - Structured outputs
  - Search grounding
- **Limitations:** No file search support
- **Best For:**
  - High-throughput scenarios
  - Simple, fast tasks
  - Cost-sensitive applications

#### Gemini 2.5 Flash Image (`gemini-2.5-flash-image`)
- **Specialty:** Image generation and understanding
- **Context Window:** 65,536 input tokens / 32,768 output tokens
- **Inputs:** Images and text
- **Outputs:** Images and text
- **Best For:**
  - Image analysis
  - Visual content generation
  - Multimodal tasks

### Previous Generation
- **Gemini 2.0 Flash** (1M context window)
- **Gemini 2.0 Flash-Lite**
- Specialized variants (TTS, Live)

**Note:** Previous generation models remain available with deprecation timelines announced.

### Intelligent Model Routing

The CLI uses intelligent routing to optimize model selection:

1. **Pro for Complex Tasks:** Multi-step reasoning, integration tests, complex code generation
2. **Flash for Simple Tasks:** Starting servers, basic queries, file operations
3. **Auto-Fallback:** Pro → Flash after 2+ slow responses (stays with Flash for session)

### Model Selection

```bash
# Command-line flag
gemini --model gemini-2.5-flash

# In interactive session
gemini> /settings
# Navigate to model settings and select preferred model
```

---

## 6. Use Cases

### Developer-Focused Tasks

#### Code Understanding & Analysis
- **Architecture Analysis:** "Explore and describe the architecture of this project"
- **Code Explanation:** "Explain how the authentication module works @./src/auth/"
- **Flow Mapping:** "Map the data flow from API request to database"
- **Dependency Analysis:** "What are the dependencies between these microservices?"

```bash
gemini -p "Analyze the architecture of this codebase and create a summary"
```

#### Bug Detection & Fixing
- **Bug Identification:** Automatically identifies bugs and proposes fixes
- **Error Diagnosis:** "Debug this error: @./logs/error.log"
- **Regression Analysis:** "Why did this test start failing?"

```bash
gemini -i "Find and fix bugs in @./src/payment-processor.js"
```

#### Test Generation
- **Unit Tests:** "Generate pytest test cases for @./src/calculator.py"
- **Integration Tests:** "Write integration tests for x and y microservices"
- **Test-Driven Development:** "Create tests first for this new feature"
- **Coverage Improvement:** "Improve test coverage for the auth module"

```bash
gemini -p "Generate comprehensive unit tests for @./src/user-service/"
```

#### Documentation Support
- **Code Documentation:** "Add JSDoc comments to all functions in @./src/utils/"
- **README Generation:** "Create a README for this project"
- **Changelog Creation:** "Generate changelog from git history"
- **API Documentation:** "Document all API endpoints in @./routes/"

```bash
gemini -p "Create comprehensive documentation for @./src/api/"
```

#### Refactoring & Optimization
- **Code Refactoring:** "Refactor this code to use modern JavaScript patterns"
- **Performance Optimization:** "Optimize this SQL query for better performance"
- **Code Review:** "Review this PR and suggest improvements"

### Database Operations
- **Natural Language Queries:** "Show me all users who signed up last month"
- **Schema Design:** "Design a database schema for an e-commerce platform"
- **Test Data Generation:** "Generate 100 realistic test users for my database"
- **Data Export:** "Export all orders to CSV format"

### Web Search & Information Retrieval
- **Real-time Data:** "Get the latest news about AI developments"
- **Research:** "Find best practices for React state management in 2025"
- **Documentation Lookup:** "How do I use the latest Next.js App Router?"

```bash
gemini -p "Get latest financial news and save to @./news-summary.md"
```

### Advanced Workflows

#### GitHub Integration
- **PR Review:** "Review all open PRs and identify which lack descriptions"
- **Issue Triage:** "Categorize and prioritize all open issues"
- **Automated Responses:** "Close stale PRs with helpful feedback"
- **Release Management:** "Generate release notes from commits since last release"

```bash
gemini -p "Review PR #123 on github.com/user/repo and provide feedback"
```

#### Video Tutorial Parsing
- **Tutorial Analysis:** "Analyze this YouTube tutorial and extract setup commands"
- **Command Extraction:** Paste YouTube link, get shell commands and notes
- **Environment Setup:** "Set up development environment from this video tutorial"

#### Slide Deck & Media Creation
- **Presentation Generation:** "Create slide deck from git history grouped by features"
- **Visual Content:** Integration with Imagen and Veo for media generation
- **Demo Applications:** "Build full-screen web app displaying GitHub issues"

#### Team Collaboration
- **Code Review Automation:** Automated code review workflow
- **Deployment Documentation:** Generate deployment guides
- **Onboarding Materials:** Create onboarding docs for new developers
- **Release Coordination:** Coordinate multi-repo release processes

### Prototyping & Rapid Development
- **Quick Prototypes:** "Create a React component for user profile"
- **Boilerplate Generation:** "Generate Express.js API boilerplate with authentication"
- **Feature Development:** "Add dark mode toggle to settings page"

### Automation & Scripting
- **Workflow Automation:** Non-interactive mode for CI/CD pipelines
- **Batch Processing:** Process multiple files or tasks
- **Scheduled Tasks:** Integration with cron or scheduled jobs

---

## 7. Differences from Other AI CLI Tools

### vs OpenAI Codex CLI

#### Cost & Licensing
- **Gemini CLI:** Open source (Apache 2.0), generous free tier (60 req/min, 1,000 req/day)
- **Codex CLI:** Not free, proprietary

#### Context Window
- **Gemini CLI:** 1M tokens (Pro 2.5) - swallows entire monorepos without chunking
- **Codex CLI:** Smaller context windows, requires chunking for large codebases

#### Platform Support
- **Gemini CLI:** Native support for macOS, Linux, Windows
- **Codex CLI:** Doesn't run natively on Windows, requires WSL2

#### Performance Focus
- **Gemini CLI:** Best for complex reasoning, large codebases, multi-step workflows
- **Codex CLI:** Better for fast iterative prototyping, tight feedback loops, CLI scripting

#### Output Style
- **Gemini CLI:** Broader explanations, shows how files interact, walks through folders
- **Codex CLI:** Structured explanations, organized output with immediate actionable results

#### Unique Features
- **Gemini CLI:**
  - Google Search grounding for real-time context
  - Multimodal capabilities (images, PDFs, video, audio)
  - MCP (Model Context Protocol) integration
  - GitHub Actions integration
  - ReAct (Reason and Act) loop for complex tasks

- **Codex CLI:**
  - Flexible model variations
  - Better for pair programming scenarios
  - Tighter CLI-native integration

### vs Claude Code CLI

#### Context & Architecture
- **Gemini CLI:** Cloud-based, requires internet, 1M token context
- **Claude Code:** Similar capabilities with different model architecture

#### Integration Ecosystem
- **Gemini CLI:** Deep Google ecosystem integration (Workspace, Cloud, Firebase)
- **Claude Code:** Anthropic ecosystem, different tool integrations

#### Development Approach
- **Gemini CLI:** Open source, community-driven with Google backing
- **Claude Code:** Anthropic-managed, different development philosophy

### vs GitHub Copilot

#### Interface & Interaction
- **Gemini CLI:** Terminal-based, conversational AI agent
- **Copilot:** IDE-integrated, inline code suggestions

#### Scope
- **Gemini CLI:** Full agentic capabilities, multi-file operations, shell access
- **Copilot:** Focused on code completion and generation within editor

#### Autonomy
- **Gemini CLI:** Can execute commands, modify files, perform complex workflows
- **Copilot:** Suggests code, requires developer to execute

### Key Differentiators

1. **Massive Context Window:** 1M tokens enables entire codebase comprehension
2. **Multimodal Processing:** Images, PDFs, videos, audio alongside text
3. **ReAct Loop:** Iterative reasoning and action for complex problem-solving
4. **Open Source:** Apache 2.0 license, community contributions
5. **Google Ecosystem:** Integration with Search, Workspace, Cloud, Firebase
6. **MCP Protocol:** Extensible via Model Context Protocol servers
7. **GitHub Actions:** Native workflow integration for team collaboration
8. **Free Tier:** Industry's most generous free allowance

---

## 8. Rate Limits & Pricing

### Free Tiers

#### Google Account (Gemini Code Assist for Individuals)
```
Rate Limits:
- 60 model requests per minute per user
- 1,000 model requests per day per user

Features:
- Access to Gemini 2.5 Pro (1M context window)
- Access to Gemini 2.5 Flash
- No credit card required
- Combined quotas with Gemini Code Assist agent mode

Authentication:
- OAuth login via browser
```

**Best For:** Individual developers, personal projects, learning

#### Gemini API Key (Unpaid)
```
Rate Limits:
- 10 model requests per minute per user
- 250 model requests per day per user

Features:
- Flash model only
- No billing setup required

Authentication:
- API key from Google AI Studio
```

**Best For:** Testing, small projects, development

#### Vertex AI Express Mode
```
Rate Limits:
- Variable quotas based on account

Features:
- 90-day trial before billing required
- Enterprise features

Authentication:
- Google Cloud credentials
```

**Best For:** Enterprise evaluation

### Paid Tiers

#### Gemini Code Assist (Fixed Price)

**Standard Edition:**
```
Rate Limits:
- 1,500 requests per day
- 120 requests per minute

Pricing:
- Fixed monthly subscription
- Available through Google Cloud or direct subscription

Features:
- Access to full Gemini model family
- Higher quotas than free tier
```

**Enterprise Edition:**
```
Rate Limits:
- 2,000 requests per day
- 120 requests per minute

Pricing:
- Contact Google for pricing

Features:
- Highest fixed-tier quotas
- Enterprise support
- Advanced security features
```

#### Pay-As-You-Go (Vertex AI Regular Mode)
```
Billing Model:
- Per token/model usage
- Dynamic shared quota or pre-purchased throughput

Pricing (Gemini 1.5 Pro as of August 2025):
- Input tokens: $1.25 per million tokens
- Output tokens: $5.00 per million tokens
- Cached tokens: 64% reduction from standard pricing

Example Costs:
- 1,000-word prompt: ~$0.00031
- 1,000-word response: ~$0.00125

Features:
- Most flexible option
- No daily/monthly limits
- Scale to any usage level
```

**Best For:** Production workloads, variable usage, full control

#### Gemini API Key (Paid Tier)
```
Rate Limits:
- Variable by tier

Billing Model:
- Per token/call usage

Features:
- Access to all models
- Usage-based pricing
```

### Subscription Upgrades

#### Individual Developers
- **Google Developer Program Premium**
- **Google AI Pro**
- **Google AI Ultra** (highest limits for individuals)

#### Businesses
- **Standard Edition** (Gemini Code Assist)
- **Enterprise Edition** (Gemini Code Assist)

### Recent Price Reductions (October 2024)
- Input tokens: 64% price reduction
- Output tokens: 52% price reduction
- Cached tokens: 64% price reduction

### Important Notes

1. **Combined Quotas:** Requests from Gemini Code Assist agent mode and Gemini CLI share quotas
2. **Multiple Requests:** One prompt may result in multiple model requests (ReAct loop)
3. **Model Routing:** Intelligent routing between Pro/Flash can affect usage
4. **Token Optimization:** Use `/compress` to reduce token usage with summaries
5. **Cost Awareness:** Pay-As-You-Go requires intentional prompt design to avoid excessive costs

### Cost Optimization Tips

```bash
# Monitor usage
gemini> /stats

# Compress conversation to save tokens
gemini> /compress

# Use Flash for simple tasks
gemini --model gemini-2.5-flash

# Be specific in prompts
gemini -p "Refactor only the auth function in @./src/auth.js"
# vs vague:
gemini -p "Make the code better"
```

---

## 9. Example Commands

### Basic Usage

#### Quick Question (Non-Interactive)
```bash
# Simple query
gemini -p "What is the gcloud command to deploy to Cloud Run?"

# With file reference
gemini -p "Summarize the main points of @./report.txt"

# Multiple files
gemini -p "Compare @./old-version.js and @./new-version.js"

# With image
gemini -p "What's in this screenshot? @./screenshot.png"
```

#### Interactive Session
```bash
# Start interactive mode
gemini

# Then at gemini> prompt:
gemini> Explain how this authentication works @./src/auth/

# Reference multiple files
gemini> Compare these implementations @./v1/handler.go @./v2/handler.go

# Use slash commands
gemini> /tools
gemini> /stats
gemini> /settings
```

#### Interactive with Initial Prompt
```bash
# Start session with context
gemini -i "I need help debugging the payment processing flow"

# Then continue conversation
gemini> Show me the payment handler @./src/payments/
gemini> What could cause a race condition here?
```

### Code Analysis & Understanding

```bash
# Analyze entire project
gemini -p "Analyze the architecture of this codebase"

# Explain specific component
gemini -p "Explain how the authentication module works @./src/auth/"

# Find dependencies
gemini -p "What dependencies does @./src/api/users.js have?"

# Map data flow
gemini -p "Map the data flow from API request to database for user creation"

# Identify patterns
gemini -p "What design patterns are used in @./src/services/?"
```

### Bug Fixing & Debugging

```bash
# Debug error
gemini -p "Debug this error: @./logs/error.log"

# Find bugs in code
gemini -i "Find and fix bugs in @./src/payment-processor.js"

# Analyze test failure
gemini -p "Why is this test failing? @./tests/integration/checkout.test.js"

# Fix specific issue
gemini -p "Fix the race condition in @./src/cache-manager.js"
```

### Test Generation

```bash
# Generate unit tests
gemini -p "Generate pytest test cases for @./src/calculator.py"

# Integration tests
gemini -p "Write integration tests for the user registration flow"

# Test coverage
gemini -p "Generate tests to improve coverage for @./src/api/"

# Test-driven development
gemini -i "I want to add a feature to export users to CSV. Create tests first."
```

### Documentation

```bash
# Generate README
gemini -p "Create a comprehensive README for this project"

# API documentation
gemini -p "Document all API endpoints in @./routes/ using OpenAPI format"

# Code comments
gemini -p "Add JSDoc comments to all functions in @./src/utils/"

# Changelog
gemini -p "Generate changelog from git history since v1.0.0"

# Architecture documentation
gemini -p "Create architecture documentation for @./src/"
```

### Refactoring

```bash
# Modernize code
gemini -p "Refactor @./legacy/auth.js to use modern async/await patterns"

# Optimize performance
gemini -p "Optimize this database query for better performance @./queries/users.sql"

# Extract functionality
gemini -p "Extract the validation logic from @./handlers/ into separate validators"

# Type safety
gemini -p "Add TypeScript types to @./src/api.js"
```

### Database Operations

```bash
# Natural language query
gemini -p "Show me all users who signed up in the last 7 days"

# Schema design
gemini -p "Design a database schema for an e-commerce platform with products, orders, and users"

# Generate test data
gemini -p "Generate 100 realistic test users as SQL INSERT statements"

# Data migration
gemini -p "Create a migration to add email verification to users table"
```

### Web Search & Information

```bash
# Latest information
gemini -p "What are the latest features in React 19?"

# Best practices
gemini -p "What are best practices for securing JWT tokens in 2025?"

# Technology comparison
gemini -p "Compare PostgreSQL vs MySQL for a high-traffic web application"

# Get news and save
gemini -p "Get latest AI developments and save summary to @./ai-news.md"
```

### GitHub Integration

```bash
# Review PR
gemini -p "Review this pull request and provide feedback @https://github.com/user/repo/pull/123"

# Analyze issues
gemini -p "Categorize and prioritize all open issues in github.com/user/repo"

# Generate release notes
gemini -p "Generate release notes from commits between v1.0.0 and v2.0.0"

# Close stale PRs
gemini -p "Find all PRs older than 30 days with no activity and close them with feedback"
```

### Shell Integration

```bash
# Execute and analyze
gemini -p "Run the test suite and analyze failures"
gemini> !npm test
gemini> Analyze these test failures

# System information
gemini -p "Check disk space and recommend cleanup"
gemini> !df -h
gemini> What can I safely clean up?

# Git operations
gemini> !git status
gemini> Create a commit message for these changes

# Toggle shell mode
gemini> !
shell> ls -la
shell> git log --oneline
shell> !  # Toggle back to gemini mode
```

### Multimodal Examples

```bash
# Image analysis
gemini -p "What's wrong with this UI? @./screenshot.png"

# PDF processing
gemini -p "Summarize this research paper @./paper.pdf"

# Video analysis
gemini -p "What setup commands are in this tutorial? @./setup-video.mp4"

# Audio transcription
gemini -p "Transcribe this meeting recording @./meeting.mp3"

# Design to code
gemini -p "Generate React component from this design @./mockup.png"
```

### Session Management

```bash
# Save conversation
gemini> /chat save project-refactor
gemini> /chat save bug-fix-session

# Resume conversation
gemini> /chat resume project-refactor

# List saved chats
gemini> /chat list

# Delete saved chat
gemini> /chat delete old-session

# Share conversation
gemini> /chat share @./conversation-log.md
gemini> /chat share @./session-export.json
```

### Memory & Context

```bash
# Add context to memory
gemini> /memory add "This project uses Tailwind CSS for styling"
gemini> /memory add "Database: PostgreSQL, ORM: Prisma"

# Show current memory
gemini> /memory show

# Refresh memory from GEMINI.md files
gemini> /memory refresh

# List memory sources
gemini> /memory list

# Compress to save tokens
gemini> /compress
```

### MCP Integration Examples

```bash
# List MCP servers
gemini> /mcp

# Use Firebase MCP server
gemini -p "Create a new Firestore collection for user profiles"

# GitHub MCP tools
gemini -p "Create a pull request for this feature"
gemini> Search repositories for authentication examples

# Custom MCP server
gemini -p "Use the flight search tool to find flights from SFO to NYC"
```

### Advanced Workflows

#### Feature Development
```bash
# Start feature development session
gemini -i "I need to add user profile image upload feature"

# Throughout session:
gemini> Show me the current user model @./models/user.js
gemini> Design database schema changes for profile images
gemini> Generate migration for user_profile_images table
gemini> Create API endpoint for image upload
gemini> Write tests for the upload endpoint
gemini> Update documentation @./docs/api.md
```

#### Bug Investigation
```bash
# Debug workflow
gemini -i "Users report checkout isn't working"

gemini> !grep -r "checkout" logs/
gemini> Analyze these error patterns
gemini> Show me checkout flow @./src/checkout/
gemini> What could cause payment processing to fail?
gemini> Check for race conditions in @./src/payment-handler.js
gemini> Generate fix and tests
```

#### Code Review Workflow
```bash
# Review changes
gemini -p "Review all changes in current branch"
gemini> !git diff main...HEAD
gemini> Analyze these changes for:
- Security issues
- Performance problems
- Best practice violations
- Missing tests
gemini> Generate PR description and checklist
```

### Configuration & Settings

```bash
# Open settings
gemini> /settings

# Change model
gemini --model gemini-2.5-flash

# Enable sandbox
gemini --sandbox
# or
gemini -s

# YOLO mode (auto-approve)
gemini --yolo
# or during session: Ctrl+Y

# Debug mode
gemini --debug
# or
gemini -d

# JSON output
gemini --output-format json -p "List all functions in @./src/utils.js"

# Stream JSON
gemini --output-format stream-json -p "Process all files in @./data/"
```

### Project Initialization

```bash
# Generate GEMINI.md for project
cd /path/to/project
gemini
gemini> /init

# This creates customized GEMINI.md with:
# - Project context
# - Code style guidelines
# - Preferred tools
# - Team conventions
```

---

## 10. Strengths & Weaknesses

### Strengths

#### 1. Massive Context Window (1M Tokens)
**Impact:** Game-changing for large codebases
- Analyze entire monorepos without chunking
- Understand complex inter-module dependencies
- Maintain context across long conversations
- Process entire project documentation

**Example Use Case:**
```bash
gemini -p "Analyze the entire microservices architecture and identify bottlenecks"
# Can process 50+ service files simultaneously
```

#### 2. Multimodal Capabilities
**Impact:** Bridge visual and code representations
- Generate code from UI mockups and designs
- Analyze screenshots for bug reports
- Process architecture diagrams
- Extract information from PDFs
- Transcribe meeting recordings

**Example Use Case:**
```bash
gemini -p "Create React component from this Figma export @./design.png"
gemini -p "Summarize technical requirements from @./spec.pdf"
```

#### 3. ReAct Loop (Reason and Act)
**Impact:** Autonomous multi-step problem solving
- Iteratively refines solutions
- Breaks down complex tasks
- Self-corrects and adapts
- Uses tools intelligently

**Example:**
```
Task: "Fix bugs and add tests"
→ Step 1: Analyze code for bugs
→ Step 2: Propose fixes
→ Step 3: Apply fixes
→ Step 4: Generate tests
→ Step 5: Run tests
→ Step 6: Fix failing tests
```

#### 4. Open Source & Generous Free Tier
**Impact:** Accessible to all developers
- Apache 2.0 license
- 60 requests/minute (free)
- 1,000 requests/day (free)
- Community contributions
- No vendor lock-in

#### 5. Google Ecosystem Integration
**Impact:** Seamless workflow for Google users
- **Search Grounding:** Real-time information from Google Search
- **Workspace Integration:** Gmail, Drive, Calendar via MCP
- **Cloud Integration:** GCP, Firebase, Vertex AI
- **Apps Script:** Custom automation

**Example Use Case:**
```bash
# Search grounding
gemini -p "What's the latest stable Node.js version and install it"
# Uses Google Search for current info

# Workspace integration
gemini -p "Send summary of this PR to team@company.com via Gmail"
```

#### 6. MCP (Model Context Protocol) Extensibility
**Impact:** Unlimited customization
- Connect to any external system
- Build custom tools
- Enterprise integrations
- Community-contributed servers

**Available MCP Servers:**
- GitHub (26+ tools)
- Firebase
- Google Workspace
- Flight search (SerpAPI)
- Custom database connectors
- Custom API integrations

#### 7. GitHub Actions Integration
**Impact:** Automate team workflows
- PR reviews
- Issue triage
- Release management
- Documentation generation
- Code quality checks

**Example Workflow:**
```yaml
- name: Gemini CLI Code Review
  uses: google-github-actions/run-gemini-cli@v1
  with:
    prompt: "Review this PR for security issues"
```

#### 8. Intelligent Model Routing
**Impact:** Optimal performance and cost
- Auto-select between Pro and Flash
- Pro for complex reasoning
- Flash for simple operations
- Fallback on slow responses
- Cost optimization

#### 9. Rich Built-in Tools
**Impact:** No additional setup needed
- File system operations (read, write, search, glob)
- Shell command execution
- Web fetching
- Google Search
- Directory management
- Content search

#### 10. Cross-Platform Native Support
**Impact:** Works everywhere
- macOS (native)
- Linux (native)
- Windows (native, no WSL required)
- Cloud Shell (Google Cloud)
- Containerized environments

### Weaknesses

#### 1. Security Vulnerabilities
**Issue:** Several flaws discovered and patched

**Historical Issues:**
- Silent data exfiltration risk
- Command injection via prompt injection
- Allowlist bypass vulnerabilities
- No sandbox mode by default

**Impact:**
- Requires trust in code execution
- Risk in untrusted environments
- Need for careful permission management

**Mitigation:**
```bash
# Always use sandbox mode for untrusted code
gemini --sandbox

# Review tool calls before approval
# Don't use --yolo with unknown code
```

#### 2. Rate Limiting Issues
**Issue:** Confusing and restrictive limits

**Problems:**
- Unclear limits even for paid subscribers
- Free tier exhausted quickly (10-20 requests)
- Infinite rate limit loops (CLI lockup)
- Auto-switching between Pro/Flash models
- Combined quotas with Code Assist

**Impact:**
- Workflow interruptions
- Unpredictable availability
- Difficult to plan usage

**Workaround:**
```bash
# Monitor usage frequently
gemini> /stats

# Use Flash for simple tasks
gemini --model gemini-2.5-flash

# Upgrade to paid tier for consistent access
```

#### 3. Git Integration Problems
**Issue:** Persistent Git workflow challenges

**Problems:**
- Non-interactive shell tool (Git prompts hang)
- Always wants to `git add .` (all files)
- Can't handle interactive Git operations
- Repository synchronization issues
- Inefficient Git workflows

**Impact:**
- Manual Git intervention required
- Risk of committing unintended files
- Broken automation workflows

**Example Problem:**
```bash
gemini> Commit these changes
# Tries: git add .
# Adds files that should be ignored
# Can't handle GPG signing prompts
```

#### 4. Connectivity Dependency
**Issue:** Requires constant internet connection

**Impact:**
- No offline mode
- Cloud-based processing only
- Latency sensitivity
- Dependency on Google infrastructure
- Privacy considerations (code sent to cloud)

**Limitations:**
- Can't work on airplanes/remote locations
- Corporate networks with restrictions
- Regulated industries with data locality requirements

#### 5. Token Waste & Optimization Issues
**Issue:** Excessive token consumption

**Problems:**
- Includes documentation folders despite .gitignore
- Doesn't respect ignore patterns properly
- Millions of tokens for small files
- No automatic optimization
- Expensive on pay-as-you-go

**Impact:**
- Quota exhaustion
- Unexpected costs
- Slow responses

**Workaround:**
```bash
# Use .geminiignore
echo "docs/" >> .geminiignore
echo "node_modules/" >> .geminiignore
echo "*.min.js" >> .geminiignore

# Compress conversations
gemini> /compress

# Be specific in file references
gemini -p "Refactor only @./src/utils/parser.js"
```

#### 6. GitHub MCP Server Reliability
**Issue:** Regular timeouts and unavailability

**Problems:**
- MCP server timeouts
- Requires CLI restart
- MCP refresh doesn't always work
- Unpredictable availability

**Impact:**
- Broken GitHub workflows
- Manual intervention needed
- Unreliable automation

#### 7. Limited Programmatic Interface
**Issue:** Weak enterprise integration

**Problems:**
- Basic non-interactive mode only (`-p` flag)
- No sophisticated API
- Limited CI/CD integration options
- JSON output not always reliable
- Stream-JSON format quirks

**Impact:**
- Difficult to integrate with complex toolchains
- Manual workflows required
- Limited automation potential

#### 8. Terminal-Only Interface
**Issue:** No GUI option

**Limitations:**
- Not intuitive for GUI-accustomed developers
- Limited visualization capabilities
- No rich formatting in terminal
- Markdown rendering varies by terminal

**Partial Mitigation:**
- VS Code companion extension available
- But still primarily terminal-focused

#### 9. Geographic & Organizational Restrictions
**Issue:** Feature availability varies

**Problems:**
- Some features not available in all regions
- Corporate firewall issues
- Enterprise deployment complexity
- Vertex AI regional limitations

#### 10. Early Development Stage
**Issue:** Still maturing with rough edges

**Problems:**
- Occasional bugs
- Unclear error messages
- "Doesn't know what to do next" moments
- Documentation gaps
- Breaking changes between versions

**Impact:**
- Requires patience and workarounds
- Active monitoring of issues/releases
- Community solutions needed

### Summary Comparison

| Aspect | Strength Rating | Weakness Impact |
|--------|----------------|-----------------|
| Context Window | ⭐⭐⭐⭐⭐ | None |
| Multimodal | ⭐⭐⭐⭐⭐ | None |
| Free Tier | ⭐⭐⭐⭐⭐ | Rate limits |
| Security | ⭐⭐⭐ | Historical vulnerabilities |
| Git Integration | ⭐⭐ | Persistent issues |
| Reliability | ⭐⭐⭐ | MCP timeouts |
| Enterprise Ready | ⭐⭐⭐ | Limited APIs |
| Offline Support | ⭐ | Cloud-only |
| Maturity | ⭐⭐⭐ | Rough edges |
| Documentation | ⭐⭐⭐⭐ | Some gaps |

---

## 11. MCP Integration

### What is MCP?

**Model Context Protocol (MCP)** is a standard for connecting AI models to external systems and data sources. It enables Gemini CLI to:
- Access external APIs
- Connect to databases
- Integrate with enterprise systems
- Use custom tools
- Extend capabilities beyond built-in features

### Architecture

```
┌─────────────┐
│ Gemini CLI  │
└──────┬──────┘
       │
       │ MCP Protocol
       │
       ├─────────┬──────────┬──────────┬─────────┐
       │         │          │          │         │
   ┌───▼───┐ ┌──▼──┐  ┌────▼────┐ ┌──▼──┐  ┌───▼───┐
   │GitHub │ │Fire │  │Workspace│ │ DB  │  │Custom │
   │Server │ │base │  │  APIs   │ │     │  │Server │
   └───────┘ └─────┘  └─────────┘ └─────┘  └───────┘
```

### Built-in MCP Servers

#### GitHub MCP Server
**26+ Tools Available:**
- `create_pull_request`
- `get_issue`
- `search_repositories`
- `create_issue`
- `update_pull_request`
- `list_commits`
- `get_repository`
- And more...

**Usage:**
```bash
gemini> /mcp
# Shows GitHub server status

gemini -p "Create a PR for the current branch"
gemini -p "List all issues labeled 'bug'"
gemini -p "Search repositories for React authentication examples"
```

#### Firebase MCP Server
**Tools:**
- Firestore operations
- Realtime Database access
- Authentication management
- Cloud Functions deployment
- Storage operations

**Usage:**
```bash
gemini -p "Create Firestore collection for user profiles"
gemini -p "Deploy Cloud Function for image processing"
```

#### Google Workspace MCP Server
**Integrations:**
- Gmail (send, read, search emails)
- Google Drive (read, write, share files)
- Calendar (create events, check availability)
- Sheets (read, write data)

**Usage:**
```bash
gemini -p "Send PR summary to team@company.com via Gmail"
gemini -p "Create Google Doc with API documentation"
gemini -p "Schedule team meeting for next Tuesday"
```

### Community MCP Servers

#### Flight Search (SerpAPI)
```bash
gemini -p "Find flights from SFO to NYC next week"
```

#### Database Connectors
```bash
# PostgreSQL MCP server
gemini -p "Query users table for accounts created last month"

# MongoDB MCP server
gemini -p "Aggregate sales data by region"
```

#### Custom Enterprise Systems
- CRM integrations
- Ticketing systems
- Internal APIs
- Legacy system connectors

### Setting Up MCP Servers

#### Installation with FastMCP

**FastMCP** is Python's leading library for building MCP servers.

**Prerequisites:**
```bash
# Install latest Gemini CLI
npm install -g @google/gemini-cli@latest

# Install FastMCP
pip install fastmcp>=2.12.3
```

#### Creating Custom MCP Server

**Example: Simple Calculator MCP Server**

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Calculator Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run()
```

**Installation:**
```bash
fastmcp install gemini-cli server.py
```

**Usage:**
```bash
gemini> /mcp
# Shows Calculator Server: CONNECTED

gemini -p "What's 15 multiplied by 23?"
# Uses multiply tool: 345
```

#### Advanced MCP Server Example

**GoDoctor - Go Development Assistant**

Features:
- Go-specific linting
- Best practices checking
- Module management
- Test generation

```bash
# Install GoDoctor MCP server
npm install -g @gotools/godoc-mcp

# Configure in .gemini/config.json
{
  "mcpServers": {
    "godoc": {
      "command": "godoc-mcp",
      "args": ["--workspace", "."]
    }
  }
}

# Use in Gemini CLI
gemini -p "Check Go code for best practices @./main.go"
```

### MCP Configuration

**Location:** `.gemini/config.json`

```json
{
  "mcpServers": {
    "github": {
      "command": "github-mcp",
      "args": ["--token", "${GITHUB_TOKEN}"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxx"
      }
    },
    "custom-db": {
      "command": "python",
      "args": ["-m", "my_db_mcp"],
      "workingDirectory": "./mcp-servers",
      "timeout": 15000
    },
    "firebase": {
      "command": "firebase-mcp",
      "args": ["--project", "my-project-id"]
    }
  }
}
```

### Managing MCP Servers

```bash
# List all MCP servers
gemini> /mcp

# Shows:
# MCP Servers Status:
# 📡 github (CONNECTED)
#    Command: github-mcp
#    Tools: 26 available
#
# 📡 firebase (CONNECTED)
#    Command: firebase-mcp
#    Tools: 12 available
#
# ⚠️  custom-db (TIMEOUT)
#    Requires restart

# List available tools
gemini> /tools

# Shows all tools from all connected MCP servers
# with descriptions

# Refresh MCP connections
# (After config changes)
gemini> /mcp refresh
```

### Multi-Part Content Returns

MCP servers can return rich, multi-part content:
- Text
- Images
- Audio
- Binary data
- Structured data

**Example:**
```python
@mcp.tool()
def generate_chart(data: list) -> dict:
    """Generate chart from data"""
    # Create chart image
    chart_image = create_chart(data)

    return {
        "text": "Chart generated successfully",
        "image": chart_image,
        "metadata": {
            "type": "bar_chart",
            "data_points": len(data)
        }
    }
```

### Real-World MCP Integration Examples

#### Example 1: Automated PR Review Workflow
```bash
# Using GitHub MCP server
gemini -i "Review all open PRs in google-gemini/gemini-cli"

gemini> List all open PRs
# Uses: search_pull_requests

gemini> For each PR:
- Check code quality
- Verify tests exist
- Check for security issues
- Add review comments

# Uses: get_pull_request, create_review_comment
```

#### Example 2: Firebase Deployment
```bash
# Using Firebase MCP server
gemini -p "Deploy the latest Cloud Function for image processing"

# MCP server:
# 1. Builds function
# 2. Runs tests
# 3. Deploys to Firebase
# 4. Verifies deployment
# 5. Returns deployment URL
```

#### Example 3: Google Workspace Automation
```bash
# Using Workspace MCP server
gemini -i "Create weekly report workflow"

gemini> Every Monday:
1. Query analytics database for last week's metrics
2. Generate summary report
3. Create Google Doc with charts
4. Share with team@company.com
5. Schedule presentation meeting

# Uses multiple MCP servers:
# - Database MCP (query data)
# - Workspace MCP (create doc, send email, schedule meeting)
```

#### Example 4: Custom Database Operations
```bash
# Using custom PostgreSQL MCP server
gemini -p "Find all users who haven't logged in for 90+ days and send re-engagement email"

# MCP server executes:
# 1. SQL query for inactive users
# 2. Generate personalized email content
# 3. Use email service MCP to send
# 4. Log results to database
```

### Building Your Own MCP Server

**Step-by-Step Guide:**

1. **Define Purpose**
   - What external system to connect?
   - What tools are needed?
   - What data to expose?

2. **Choose Framework**
   - **FastMCP** (Python) - Recommended, easiest
   - **MCP SDK** (TypeScript/JavaScript)
   - **Custom Implementation** (Any language with STDIO)

3. **Implement Tools**
   ```python
   from fastmcp import FastMCP

   mcp = FastMCP("My Custom Server")

   @mcp.tool()
   def my_tool(param: str) -> str:
       """Tool description for Gemini"""
       # Tool implementation
       return result
   ```

4. **Test Locally**
   ```bash
   python server.py
   # Test in separate terminal
   ```

5. **Install for Gemini CLI**
   ```bash
   fastmcp install gemini-cli server.py
   ```

6. **Verify**
   ```bash
   gemini> /mcp
   # Should show your server as CONNECTED
   ```

7. **Use in Prompts**
   ```bash
   gemini -p "Use my_tool to process this data"
   ```

### MCP Best Practices

1. **Tool Descriptions:** Write clear, detailed tool descriptions
2. **Error Handling:** Implement robust error handling in tools
3. **Timeouts:** Set appropriate timeouts for long-running operations
4. **Security:** Validate inputs, use environment variables for secrets
5. **Documentation:** Document tool parameters and return types
6. **Testing:** Test tools independently before MCP integration
7. **Logging:** Implement logging for debugging
8. **Versioning:** Version your MCP servers for stability

### MCP Resources

- **FastMCP Documentation:** https://fastmcp.dev
- **MCP Specification:** https://modelcontextprotocol.io
- **Gemini CLI MCP Guide:** https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html
- **Community MCP Servers:** https://github.com/topics/mcp-server
- **Tutorial Series:** https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718

---

## Conclusion

### When to Use Gemini CLI

**Ideal For:**
- Large codebases requiring full context comprehension
- Multimodal tasks (code from designs, PDF analysis, etc.)
- Complex, multi-step development workflows
- Google ecosystem integration needs
- Budget-conscious development (generous free tier)
- Open-source projects requiring transparency
- Teams wanting GitHub Actions automation

**Consider Alternatives For:**
- Offline/air-gapped environments (not supported)
- Simple, fast prototyping (Codex may be faster)
- Enterprise with strict data locality requirements
- Highly regulated industries (due to cloud processing)
- Projects requiring guaranteed uptime SLAs

### Key Takeaways

1. **Context is King:** 1M token window is genuinely transformative for real-world codebases
2. **Multimodal Power:** Ability to process designs, PDFs, videos sets it apart
3. **Free Tier Excellence:** 60 req/min free tier beats competitors
4. **MCP Extensibility:** Unlimited integration potential via MCP
5. **Google Integration:** Unmatched for Google Cloud/Workspace users
6. **Rough Edges:** Still maturing, expect occasional issues
7. **Security Awareness:** Use sandbox mode, review tool calls
8. **Rate Limit Management:** Monitor usage, optimize prompts
9. **Git Challenges:** Manual intervention needed for complex Git workflows
10. **Community Growing:** Active development, weekly releases, strong community

### Quick Reference Commands

```bash
# Installation
npm install -g @google/gemini-cli

# Authentication
gemini  # Select login method

# Basic usage
gemini -p "your prompt"
gemini -i "start interactive with prompt"

# Essential slash commands
/help, /tools, /stats, /settings, /mcp

# File references
@./path/to/file
@./directory/

# Model selection
--model gemini-2.5-pro
--model gemini-2.5-flash

# Output formats
--output-format json
--output-format stream-json

# Safety
--sandbox  # Enable sandbox mode
```

### Resources

- **GitHub:** https://github.com/google-gemini/gemini-cli
- **Docs:** https://google-gemini.github.io/gemini-cli/docs/
- **Codelabs:** https://codelabs.developers.google.com/gemini-cli-hands-on
- **Tutorial Series:** https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718
- **Issues:** https://github.com/google-gemini/gemini-cli/issues
- **Discussions:** https://github.com/google-gemini/gemini-cli/discussions

---

**End of Report**
