# AWS CDK Development Skill

Expert guidance for building AWS cloud infrastructure using the AWS Cloud Development Kit (CDK) with TypeScript, Python, and other languages.

## Overview

This skill provides comprehensive best practices for AWS CDK development, enabling you to define cloud infrastructure using familiar programming languages instead of YAML/JSON templates. It integrates with AWS MCP servers to provide up-to-date service information and CDK-specific guidance.

## When to Use This Skill

Use this skill when you need to:

- Create new CDK stacks or constructs
- Define AWS infrastructure programmatically (IaC)
- Implement Lambda functions within CDK applications
- Refactor existing CDK infrastructure
- Follow AWS CDK best practices and patterns
- Validate CDK configurations before deployment
- Synthesize CloudFormation templates
- Deploy infrastructure with `cdk deploy`
- Verify AWS service capabilities and regional availability

**Keywords**: CDK, CloudFormation, Infrastructure as Code, IaC, cdk synth, cdk deploy, constructs, stacks

## Integrated MCP Servers

This skill works with two powerful MCP servers:

### 1. AWS Documentation MCP Server

**Use whenever you need to verify AWS service information before implementation:**

- Search AWS documentation for latest features and best practices
- Check regional availability of AWS services
- Verify service limits and quotas
- Confirm API specifications and parameters
- Access up-to-date AWS service information beyond knowledge cutoff

**Example queries:**
- "Check if Lambda supports Python 3.13 runtime"
- "Verify DynamoDB is available in eu-south-2"
- "What are the current Lambda timeout limits?"
- "Get latest S3 encryption options"

### 2. AWS CDK MCP Server

**Leverage for CDK-specific guidance and utilities:**

- Get CDK construct recommendations
- Retrieve CDK best practices
- Access CDK pattern suggestions
- Validate CDK configurations
- Get help with CDK-specific APIs and parameters

**Example queries:**
- "What's the recommended CDK construct for API Gateway REST API?"
- "How to configure NodejsFunction bundling options?"
- "Best practices for CDK stack organization"
- "CDK construct for DynamoDB with auto-scaling"

## Core CDK Principles

### 1. Resource Naming - The Golden Rule

**CRITICAL: Do NOT explicitly specify resource names when they are optional in CDK constructs.**

**Why this matters:**
- **Reusable patterns**: Deploy the same construct/pattern multiple times without conflicts
- **Parallel deployments**: Multiple stacks can deploy simultaneously in the same region
- **Cleaner shared logic**: Patterns and shared code can be initialized multiple times without name collision
- **Stack isolation**: Each stack gets uniquely identified resources automatically

```typescript
// ❌ BAD - Explicit naming prevents reusability and parallel deployments
new lambda.Function(this, 'MyFunction', {
  functionName: 'my-lambda',  // Avoid this - creates hard-coded name
  // ...
});

// ✅ GOOD - Let CDK generate unique names
new lambda.Function(this, 'MyFunction', {
  // No functionName specified
  // CDK generates: StackName-MyFunctionXXXXXX
  // ...
});
```

**Security Note**: For different environments (dev, staging, prod), follow AWS Security Pillar best practices by using **separate AWS accounts** rather than relying on resource naming within a single account. Account-level isolation provides stronger security boundaries.

### 2. Lambda Function Development

Use the appropriate Lambda construct based on your runtime for automatic bundling:

**TypeScript/JavaScript:**
```typescript
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

new NodejsFunction(this, 'MyFunction', {
  entry: 'lambda/handler.ts',
  handler: 'handler',
  // Automatically handles bundling, dependencies, and transpilation
});
```

**Python:**
```typescript
import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';

new PythonFunction(this, 'MyFunction', {
  entry: 'lambda',
  index: 'handler.py',
  handler: 'handler',
  // Automatically handles dependencies and packaging
});
```

**Benefits:**
- Automatic bundling and dependency management
- Transpilation handled automatically
- No manual packaging required
- Consistent deployment patterns

### 3. Pre-Deployment Validation

Use a **multi-layer validation strategy** for comprehensive CDK quality checks:

#### Layer 1: Real-Time IDE Feedback (Recommended)

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

**Optional for VS Code users**: Install the [CDK NAG Validator extension](https://marketplace.visualstudio.com/items?itemName=alphacrack.cdk-nag-validator) for faster feedback on file save.

**Note**: cdk-nag is available in all CDK languages (TypeScript, Python, Java, C#, Go).

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

Before committing CDK code:

```bash
# 1. Build - Ensure compilation succeeds
npm run build  # or language-specific build command

# 2. Tests - Run unit and integration tests
npm test  # or pytest, mvn test, etc.

# 3. Validation Script - Meta-level checks
./scripts/validate-stack.sh
```

The validation script focuses on:
- Language detection
- Template size and resource count analysis
- Synthesis success verification
- (Note: Detailed anti-pattern checks are handled by cdk-nag)

## Development Workflow

### Step-by-Step Process

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

**Always verify before implementing:**
- New AWS service features or configurations
- Service availability in target regions
- API parameter specifications
- Service limits and quotas
- Security best practices for AWS services

### When to Use CDK MCP Server

**Leverage for CDK-specific guidance:**
- CDK construct selection and usage
- CDK API parameter options
- CDK best practice patterns
- Construct property configurations
- CDK-specific optimizations

### MCP Usage Best Practices

1. **Verify First**: Always check AWS Documentation MCP before implementing new features
2. **Regional Validation**: Check service availability in target deployment regions
3. **CDK Guidance**: Use CDK MCP for construct-specific recommendations
4. **Stay Current**: MCP servers provide latest information beyond knowledge cutoff
5. **Combine Sources**: Use both skill patterns and MCP servers for comprehensive guidance

## Real-World Examples

### Example 1: Serverless API with Lambda and DynamoDB

```typescript
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

export class ApiStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB table with auto-scaling
    const table = new dynamodb.Table(this, 'ItemsTable', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST, // No name specified
    });

    // Lambda function with automatic bundling
    const handler = new NodejsFunction(this, 'ApiHandler', {
      entry: 'lambda/api.ts',
      handler: 'handler',
      environment: {
        TABLE_NAME: table.tableName,
      },
    });

    // Grant Lambda permissions to access DynamoDB
    table.grantReadWriteData(handler);

    // API Gateway
    const api = new apigateway.RestApi(this, 'ItemsApi', {
      restApiName: undefined, // Let CDK generate name
    });

    const items = api.root.addResource('items');
    items.addMethod('GET', new apigateway.LambdaIntegration(handler));
    items.addMethod('POST', new apigateway.LambdaIntegration(handler));
  }
}
```

### Example 2: S3 Bucket with Lambda Trigger

```typescript
import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

export class S3ProcessorStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket with encryption
    const bucket = new s3.Bucket(this, 'DataBucket', {
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      versioned: true,
    });

    // Lambda processor
    const processor = new NodejsFunction(this, 'Processor', {
      entry: 'lambda/process.ts',
      handler: 'handler',
      environment: {
        BUCKET_NAME: bucket.bucketName,
      },
    });

    // Grant read/write access
    bucket.grantReadWrite(processor);

    // Trigger Lambda on object creation
    bucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(processor),
      { prefix: 'uploads/' }
    );
  }
}
```

### Example 3: Multi-Region Stack

```typescript
import * as cdk from 'aws-cdk-lib';

export class MultiRegionApp extends cdk.App {
  constructor() {
    super();

    // Deploy same stack to multiple regions
    new ApiStack(this, 'ApiStack-US-East', {
      env: { region: 'us-east-1', account: process.env.CDK_DEFAULT_ACCOUNT },
    });

    new ApiStack(this, 'ApiStack-EU-West', {
      env: { region: 'eu-west-1', account: process.env.CDK_DEFAULT_ACCOUNT },
    });

    // Works because we don't specify resource names
    // Each region gets unique CloudFormation-generated names
  }
}
```

## Common Patterns

The `references/cdk-patterns.md` file contains detailed guidance on:

- Common CDK patterns and their use cases
- Anti-patterns to avoid
- Security best practices
- Cost optimization strategies
- Performance considerations
- Construct composition patterns
- Cross-stack references
- Custom constructs

## Validation Script

The `scripts/validate-stack.sh` script provides pre-deployment validation:

- Language detection (TypeScript, Python, Java, C#, Go)
- Template size analysis
- Resource count analysis
- Synthesis success verification
- Integration with GitHub Actions workflows

Run it before committing:

```bash
cd /path/to/cdk/project
/path/to/skill/scripts/validate-stack.sh
```

## GitHub Actions Integration

When GitHub Actions workflow files exist in the repository, ensure all checks defined in `.github/workflows/` pass before committing. This prevents CI/CD failures and maintains code quality standards.

## Prerequisites

### Required Tools

- AWS CDK CLI: `npm install -g aws-cdk`
- AWS CLI with configured credentials
- Node.js 18+ (for TypeScript/JavaScript)
- Python 3.9+ (for Python CDK)
- Appropriate runtime for your chosen language

### AWS Credentials

Configure AWS credentials using one of:

```bash
# Option 1: AWS CLI configure
aws configure

# Option 2: Environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1

# Option 3: AWS SSO
aws sso login --profile my-profile
export AWS_PROFILE=my-profile
```

### IAM Permissions

Your AWS user/role needs permissions for:
- CloudFormation (create/update/delete stacks)
- Services being deployed (Lambda, S3, DynamoDB, etc.)
- IAM (for creating roles and policies)
- S3 (for CDK asset storage)

## Installation

### As a Claude Code Skill

Add this skill to your Claude Code skills directory:

```bash
# Copy to Claude Code skills directory
cp -r aws-cdk-development ~/.claude/skills/

# Or create a symlink
ln -s /path/to/aws-cdk-development ~/.claude/skills/aws-cdk-development
```

### MCP Server Configuration

The AWS Documentation and CDK MCP servers should be configured in your Claude Code MCP settings. Refer to the [AWS MCP Servers documentation](https://awslabs.github.io/mcp/) for setup instructions.

## Resources

### Included Files

- `SKILL.md` - Concise skill definition and core principles
- `README.md` - This comprehensive guide
- `references/cdk-patterns.md` - Detailed CDK patterns and anti-patterns
- `scripts/validate-stack.sh` - Pre-deployment validation script
- `CHANGELOG.md` - Version history
- `LICENSE` - MIT License

### External Resources

- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/)
- [CDK Patterns](https://cdkpatterns.com/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [cdk-nag on GitHub](https://github.com/cdklabs/cdk-nag)
- [AWS MCP Servers](https://awslabs.github.io/mcp/)

## Contributing

This skill is part of the AISkills collection. For improvements or issues:

1. Test changes thoroughly with real CDK projects
2. Follow the existing documentation structure
3. Update CHANGELOG.md for any changes
4. Ensure validation script passes

## License

MIT License - See LICENSE file for details.

Original repository: [zxkane/aws-skills](https://github.com/zxkane/aws-skills)

---

**Version**: 1.0.0
**Last Updated**: 2025-11-16
**Maintained By**: AISkills Collection
