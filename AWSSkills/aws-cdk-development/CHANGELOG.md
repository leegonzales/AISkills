# Changelog

All notable changes to the AWS CDK Development skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-16

### Added
- Initial release of AWS CDK Development skill
- Comprehensive SKILL.md with core CDK principles
- Detailed README.md with real-world examples
- CDK patterns reference documentation (references/cdk-patterns.md)
- Pre-deployment validation script (scripts/validate-stack.sh)
- Integration with AWS Documentation MCP server
- Integration with AWS CDK MCP server
- Resource naming best practices and patterns
- Lambda function development guidelines (NodejsFunction, PythonFunction)
- Multi-layer validation strategy (cdk-nag, synthesis, pre-commit)
- Development workflow documentation
- Stack organization patterns
- Testing strategy guidelines
- MCP usage best practices
- Real-world code examples (serverless API, S3 processor, multi-region)
- GitHub Actions integration guidance
- Prerequisites and installation instructions
- MIT License

### Documentation
- Core CDK principles: no explicit resource naming
- Benefits of CDK-generated names (reusability, parallel deployments)
- Security best practices (separate accounts per environment)
- Automatic bundling with NodejsFunction and PythonFunction
- Three-layer validation approach (IDE, synthesis, pre-commit)
- When to use each integrated MCP server
- Complete development workflow from design to deployment
- Common patterns and anti-patterns reference

### Features
- Support for TypeScript/JavaScript CDK projects
- Support for Python CDK projects
- Support for Java/C#/Go CDK projects via cdk-nag
- CloudFormation template validation
- Resource naming compliance checks
- GitHub Actions workflow integration
- Language-agnostic validation script

[1.0.0]: https://github.com/leegonzales/AISkills/releases/tag/aws-cdk-development-v1.0.0
