# Changelog

All notable changes to the Playwright Skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-16

### Added
- Initial integration into AISkills collection from lackeyjb/playwright-skill
- CI/CD integration examples (GitHub Actions, GitLab CI)
- Performance testing documentation and patterns
- Integration guide with Codex/Gemini peer review skills
- Enhanced troubleshooting section with common CI/CD issues
- Examples for parallel test execution in CI environments
- Docker integration for containerized testing

### Enhanced
- README.md with comprehensive CI/CD patterns
- API_REFERENCE.md with CI/CD best practices section
- Contributing guidelines for AISkills collection

### Attribution
Originally developed by lackeyjb (https://github.com/lackeyjb/playwright-skill)
Integrated into AISkills collection with minimal changes - already excellent structure.

## [4.0.2] - 2025-11-15 (Original Release)

### Features from Original Repository
- General-purpose browser automation with Playwright
- Auto-detection of development servers
- Smart test management with /tmp file cleanup
- Universal executor (run.js) for module resolution
- Comprehensive helper library
- Progressive disclosure documentation (SKILL.md + API_REFERENCE.md)
- Visible browser by default for debugging
- Parameterized URLs for flexible testing
- Claude Code plugin system integration

### Original Documentation
- SKILL.md (407 lines) - Concise, model-invoked documentation
- API_REFERENCE.md (630 lines) - Comprehensive Playwright reference
- README.md - User-facing documentation
- CONTRIBUTING.md - Contribution guidelines

## Future Enhancements (Roadmap)

### Planned
- Visual regression testing examples with Percy/Applitools
- Lighthouse performance integration
- Accessibility testing with axe-core
- Cross-browser testing matrices
- Advanced network mocking patterns
- WebSocket testing examples

### Under Consideration
- Integration with popular testing frameworks (Jest, Vitest)
- Playwright trace viewer integration
- Video recording in CI/CD
- Test parallelization strategies
- Database seeding/teardown patterns

---

## Integration Notes

This skill was selected for the AISkills collection as SKILL-12 with a score of 104/100 due to:
- Professional browser automation capabilities
- Model-invoked code generation (not just pre-built scripts)
- Excellent documentation structure
- Clean separation of concerns (SKILL.md vs API_REFERENCE.md)
- Robust helper library
- Proper module resolution via run.js executor

The integration preserves the original excellent work while adding value through:
- CI/CD integration examples
- Peer review workflow integration
- Enhanced performance testing documentation
- Alignment with AISkills collection standards
