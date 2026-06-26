---
name: aws-cdk-development
description: AWS Cloud Development Kit (CDK) expert for building cloud infrastructure with TypeScript/Python. Use when creating CDK stacks, defining CDK constructs, implementing infrastructure as code, or when the user mentions CDK, CloudFormation, IaC, cdk synth, cdk deploy, or wants to define AWS infrastructure programmatically. Covers CDK app structure, construct patterns, stack composition, and deployment workflows.
---

# AWS CDK Development

This skill provides comprehensive guidance for developing AWS infrastructure using the Cloud Development Kit (CDK), with integrated MCP servers for accessing latest AWS knowledge and CDK utilities.

## Fidelity / Degraded Mode (when the AWS MCP servers are absent)

**Read this first. It governs every claim this skill makes about AWS.**

This skill depends on the AWS Documentation MCP and AWS CDK MCP servers for ground truth. Those servers may not be present in a given session. When they are absent, you operate in **degraded mode** — and degraded mode has hard rules, because the failure mode here is high-stakes: fabricated service limits, quotas, regional availability, runtime versions, or pricing flow straight into infrastructure, security posture, and cost.

**The volatile facts.** The following CHANGE over time and MUST be verified against a live source — never recalled from training memory:

- AWS **service limits and quotas** (Lambda timeout/memory ceilings, concurrency, payload sizes, account limits, etc.)
- **Regional availability** (whether a service or feature exists in a given region)
- **Supported runtime versions** (Lambda Python/Node/Java runtimes, deprecation dates, EOL runtimes)
- **Pricing** (per-request, per-GB, per-hour, free-tier boundaries)
- New service features, API parameters, and default behaviors

**The firewall (degraded-mode rules):**

1. **If the AWS Documentation / CDK MCP server IS available** — verify the fact against it before stating it. Cite that you verified.
2. **If the AWS MCP servers are NOT available** — you must **NOT** state a specific limit, version, quota, region, or price as fact. Instead, do one of:
   - **(a) Flag for verification.** Say: *"Verify against current AWS docs — I can't confirm this without the AWS Docs MCP or a web check."* A live web search is an acceptable substitute for the MCP server; recalling from memory is not.
   - **(b) Answer conditionally.** Frame the guidance on the assumption, not as fact: *"If Lambda supports Python 3.13 in your region, then ..."* — and surface the assumption explicitly.
   - **(c) Stay version-agnostic.** Write the CDK code so the volatile value is a parameter, context value, or clearly-flagged `// VERIFY:` placeholder, rather than hardcoding a confidently-asserted version/limit.
3. **Never fabricate a confident "X is supported" / "the limit is N" / "available in region R" without a live source.** A plausible-sounding number recalled from memory is the exact failure this gate exists to stop. When unsure, hedge and flag — do not assert.
4. **Default posture is humility about specifics.** General CDK patterns, construct usage, and IaC architecture in this skill are stable and may be stated directly. The volatile facts above are not — gate them.

## Integrated MCP Servers

This skill includes two MCP servers automatically configured with the plugin:

### AWS Documentation MCP Server
**When to use**: Always verify AWS service information before implementation
- Search AWS documentation for latest features and best practices
- Check regional availability of AWS services
- Verify service limits and quotas
- Confirm API specifications and parameters
- Access up-to-date AWS service information

**Critical**: Use this server whenever AWS service features, configurations, or availability need verification.

### AWS CDK MCP Server
**When to use**: For CDK-specific guidance and utilities
- Get CDK construct recommendations
- Retrieve CDK best practices
- Access CDK pattern suggestions
- Validate CDK configurations
- Get help with CDK-specific APIs

**Important**: Leverage this server for CDK construct guidance and advanced CDK operations.

## When to Use This Skill

Use this skill when:
- Creating new CDK stacks or constructs
- Refactoring existing CDK infrastructure
- Implementing Lambda functions within CDK
- Following AWS CDK best practices
- Validating CDK stack configurations before deployment
- Verifying AWS service capabilities and regional availability

## Core CDK Principles

### Resource Naming

**CRITICAL**: Do NOT explicitly specify resource names when they are optional in CDK constructs.

**Why**: CDK-generated names enable:
- **Reusable patterns**: Deploy the same construct/pattern multiple times without conflicts
- **Parallel deployments**: Multiple stacks can deploy simultaneously in the same region
- **Cleaner shared logic**: Patterns and shared code can be initialized multiple times without name collision
- **Stack isolation**: Each stack gets uniquely identified resources automatically

**Pattern**: Let CDK generate unique names automatically using CloudFormation's naming mechanism.

```typescript
// ❌ BAD - Explicit naming prevents reusability and parallel deployments
new lambda.Function(this, 'MyFunction', {
  functionName: 'my-lambda',  // Avoid this
  // ...
});

// ✅ GOOD - Let CDK generate unique names
new lambda.Function(this, 'MyFunction', {
  // No functionName specified - CDK generates: StackName-MyFunctionXXXXXX
  // ...
});
```

**Security Note**: For different environments (dev, staging, prod), follow AWS Security Pillar best practices by using separate AWS accounts rather than relying on resource naming within a single account. Account-level isolation provides stronger security boundaries.

### Lambda Function Development

Use the appropriate Lambda construct based on runtime:

**TypeScript/JavaScript**: Use `@aws-cdk/aws-lambda-nodejs`
```typescript
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

new NodejsFunction(this, 'MyFunction', {
  entry: 'lambda/handler.ts',
  handler: 'handler',
  // Automatically handles bundling, dependencies, and transpilation
});
```

**Python**: Use `@aws-cdk/aws-lambda-python`
```typescript
import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';

new PythonFunction(this, 'MyFunction', {
  entry: 'lambda',
  index: 'handler.py',
  handler: 'handler',
  // Automatically handles dependencies and packaging
});
```

**Benefits**:
- Automatic bundling and dependency management
- Transpilation handled automatically
- No manual packaging required
- Consistent deployment patterns

### Pre-Deployment Validation

Use a **multi-layer validation strategy** for comprehensive CDK quality checks:

#### Layer 1: Real-Time IDE Feedback (Recommended)

**For TypeScript/JavaScript projects**:

Install [cdk-nag](https://github.com/cdklabs/cdk-nag) for synthesis-time validation:
```bash
npm install --save-dev cdk-nag
```

Add to your CDK app:
```typescript
import { Aspects } from 'aws-cdk-lib';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
Aspects.of(app).add(new AwsSolutionsChecks());
```

**Optional - VS Code users**: Install [CDK NAG Validator extension](https://marketplace.visualstudio.com/items?itemName=alphacrack.cdk-nag-validator) for faster feedback on file save.

**For Python/Java/C#/Go projects**: cdk-nag is available in all CDK languages and provides the same synthesis-time validation.

#### Layer 2: Synthesis-Time Validation (Required)

1. **Synthesis with cdk-nag**: Validate stack with comprehensive rules
   ```bash
   cdk synth  # cdk-nag runs automatically via Aspects
   ```

2. **Suppress legitimate exceptions** with documented reasons:
   ```typescript
   import { NagSuppressions } from 'cdk-nag';

   // Document WHY the exception is needed
   NagSuppressions.addResourceSuppressions(resource, [
     {
       id: 'AwsSolutions-L1',
       reason: 'Lambda@Edge requires specific runtime for CloudFront compatibility'
     }
   ]);
   ```

#### Layer 3: Pre-Commit Safety Net

1. **Build**: Ensure compilation succeeds
   ```bash
   npm run build  # or language-specific build command
   ```

2. **Tests**: Run unit and integration tests
   ```bash
   npm test  # or pytest, mvn test, etc.
   ```

3. **Validation Script**: Meta-level checks
   ```bash
   ./scripts/validate-stack.sh
   ```

The validation script now focuses on:
- Language detection
- Template size and resource count analysis
- Synthesis success verification
- (Note: Detailed anti-pattern checks are handled by cdk-nag)

## Workflow Guidelines

### Development Workflow

1. **Design**: Plan infrastructure resources and relationships
2. **Verify AWS Services**: Use AWS Documentation MCP to confirm service availability and features
   - Check regional availability for all required services
   - Verify service limits and quotas
   - Confirm latest API specifications
3. **Implement**: Write CDK constructs following best practices
   - Use CDK MCP server for construct recommendations
   - Reference CDK best practices via MCP tools
4. **Validate**: Run pre-deployment checks (see above)
5. **Synthesize**: Generate CloudFormation templates
6. **Review**: Examine synthesized templates for correctness
7. **Deploy**: Deploy to target environment
8. **Verify**: Confirm resources are created correctly

### Stack Organization

- Use nested stacks for complex applications
- Separate concerns into logical construct boundaries
- Export values that other stacks may need
- Use CDK context for environment-specific configuration

### Testing Strategy

- Unit test individual constructs
- Integration test stack synthesis
- Snapshot test CloudFormation templates
- Validate resource properties and relationships

## Using MCP Servers Effectively

### When to Use AWS Documentation MCP

**Always verify before implementing**:
- New AWS service features or configurations
- Service availability in target regions
- API parameter specifications
- Service limits and quotas
- Security best practices for AWS services

**Example scenarios**:
- "Check if Lambda supports Python 3.13 runtime"
- "Verify DynamoDB is available in eu-south-2"
- "What are the current Lambda timeout limits?"
- "Get latest S3 encryption options"

### When to Use CDK MCP Server

**Leverage for CDK-specific guidance**:
- CDK construct selection and usage
- CDK API parameter options
- CDK best practice patterns
- Construct property configurations
- CDK-specific optimizations

**Example scenarios**:
- "What's the recommended CDK construct for API Gateway REST API?"
- "How to configure NodejsFunction bundling options?"
- "Best practices for CDK stack organization"
- "CDK construct for DynamoDB with auto-scaling"

### MCP Usage Best Practices

1. **Verify First**: Always check AWS Documentation MCP before implementing new features
2. **Regional Validation**: Check service availability in target deployment regions
3. **CDK Guidance**: Use CDK MCP for construct-specific recommendations
4. **Stay Current**: MCP servers provide latest information beyond knowledge cutoff
5. **Combine Sources**: Use both skill patterns and MCP servers for comprehensive guidance
6. **Degraded Mode**: If the MCP servers are absent, the "Fidelity / Degraded Mode" rules at the top of this skill apply — do not substitute training-memory recall for verification. Flag, answer conditionally, or stay version-agnostic.

## CDK Patterns Reference

For detailed CDK patterns, anti-patterns, and architectural guidance, refer to the comprehensive reference:

**File**: `references/cdk-patterns.md`

This reference includes:
- Common CDK patterns and their use cases
- Anti-patterns to avoid
- Security best practices
- Cost optimization strategies
- Performance considerations

## Additional Resources

- **Validation Script**: `scripts/validate-stack.sh` - Pre-deployment validation
- **CDK Patterns**: `references/cdk-patterns.md` - Detailed pattern library
- **AWS Documentation MCP**: Integrated for latest AWS information
- **CDK MCP Server**: Integrated for CDK-specific guidance

## GitHub Actions Integration

When GitHub Actions workflow files exist in the repository, ensure all checks defined in `.github/workflows/` pass before committing. This prevents CI/CD failures and maintains code quality standards.
