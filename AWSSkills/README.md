# AWS Skills Collection

A comprehensive collection of three AWS development skills for Claude Code, covering infrastructure as code, serverless applications, and operational excellence. Integrated with **10+ AWS MCP servers** for complete AWS development lifecycle management.

## Overview

This collection provides expert guidance for building, deploying, and operating AWS applications following AWS Well-Architected Framework principles. Each skill focuses on a specific domain while working together to provide complete AWS development coverage.

## The Three Skills

### 1. AWS CDK Development
**Infrastructure as Code with AWS Cloud Development Kit**

Define cloud infrastructure using familiar programming languages (TypeScript, Python, Java, C#, Go) instead of YAML/JSON templates.

**Core Features:**
- CDK best practices and patterns
- Resource naming guidelines (no explicit names for reusability)
- Lambda function development (NodejsFunction, PythonFunction)
- Multi-layer validation strategy (cdk-nag, synthesis, pre-commit)
- Pre-deployment validation script
- Stack organization and composition patterns

**Integrated MCP Servers (2):**
- AWS Documentation MCP - Latest AWS service information
- AWS CDK MCP - CDK-specific guidance and patterns

**When to use:**
- Creating CDK stacks or constructs
- Defining infrastructure programmatically
- Refactoring existing CDK code
- Validating configurations before deployment
- Synthesizing CloudFormation templates

**Directory:** `aws-cdk-development/`

---

### 2. AWS Serverless & Event-Driven Architecture
**Serverless applications based on Well-Architected Framework**

Build scalable serverless applications using Lambda, API Gateway, EventBridge, Step Functions, and managed AWS services.

**Core Features:**
- Seven Well-Architected serverless design principles
- Event-driven architecture patterns (EventBridge, SQS, SNS)
- Serverless patterns (API microservices, stream processing, scheduled jobs)
- Saga patterns for distributed transactions
- Event sourcing patterns
- Complete lifecycle management with SAM

**Integrated MCP Servers (5):**
- AWS Documentation MCP - Service verification
- AWS Serverless MCP (SAM CLI) - Application lifecycle management
- AWS Lambda Tool MCP - Function execution and testing
- AWS Step Functions MCP - Workflow orchestration
- Amazon SNS/SQS MCP - Messaging and queue management

**When to use:**
- Building serverless APIs with Lambda and API Gateway
- Designing event-driven architectures
- Implementing microservices patterns
- Creating async processing workflows
- Orchestrating multi-service transactions
- Building real-time data pipelines

**Directory:** `aws-serverless-eda/`

---

### 3. AWS Cost & Operations
**Cost optimization, monitoring, and operational excellence**

Manage AWS costs, implement monitoring and observability, conduct security audits, and achieve operational excellence.

**Core Features:**
- Pre-deployment cost estimation
- Real-time billing and budget monitoring
- CloudWatch metrics, logs, and alarms
- Application performance monitoring (APM)
- Container monitoring with Prometheus
- CloudTrail security auditing
- Well-Architected security assessment

**Integrated MCP Servers (8):**
- AWS Billing and Cost Management MCP - Real-time billing
- AWS Pricing MCP - Cost estimation
- AWS Cost Explorer MCP - Cost analysis and optimization
- Amazon CloudWatch MCP - Metrics, logs, alarms
- CloudWatch Application Signals MCP - APM insights
- AWS Managed Prometheus MCP - Container monitoring
- AWS CloudTrail MCP - API activity auditing
- AWS Well-Architected Security Assessment Tool MCP - Security posture

**When to use:**
- Optimizing AWS costs
- Estimating costs before deployment
- Monitoring application performance
- Setting up observability
- Investigating operational issues
- Auditing AWS activity
- Assessing security posture

**Directory:** `aws-cost-operations/`

---

## How the Skills Work Together

### Complete AWS Development Workflow

```
1. DESIGN
   └─> Use CDK skill for infrastructure planning

2. ESTIMATE COSTS
   └─> Use Cost & Operations skill (Pricing MCP) for cost estimation

3. IMPLEMENT
   ├─> Use CDK skill for infrastructure code
   └─> Use Serverless skill for application code

4. VALIDATE
   ├─> Use CDK skill validation script
   └─> Use Serverless skill for local testing (SAM MCP)

5. DEPLOY
   ├─> Use CDK skill to deploy infrastructure
   └─> Use Serverless skill (SAM MCP) to deploy applications

6. MONITOR
   ├─> Use Cost & Operations skill to track costs (Billing MCP)
   ├─> Use Cost & Operations skill to monitor performance (CloudWatch MCP)
   └─> Use Cost & Operations skill for security audits (CloudTrail MCP)

7. OPTIMIZE
   ├─> Use Cost & Operations skill for cost analysis (Cost Explorer MCP)
   └─> Use Cost & Operations skill for performance optimization
```

### Example: Building a Serverless API

**Step 1: Design Infrastructure (CDK skill)**
```typescript
// Define API Gateway, Lambda, and DynamoDB
const api = new apigateway.RestApi(this, 'Api');
const handler = new NodejsFunction(this, 'Handler', {
  entry: 'lambda/api.ts',
});
const table = new dynamodb.Table(this, 'Table', {
  partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
  billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
});
```

**Step 2: Estimate Costs (Cost & Operations skill)**
```
Query Pricing MCP:
"Estimate monthly cost for:
- API Gateway with 10M requests
- Lambda with 10M invocations, 512MB, 200ms avg duration
- DynamoDB PAY_PER_REQUEST with 10M reads, 2M writes"
```

**Step 3: Implement Lambda Functions (Serverless skill)**
```typescript
// Follow Well-Architected principles:
// 1. Speedy, Simple, Singular
// 2. Design for failures and duplicates (idempotency)
// 3. Share nothing (use DynamoDB for state)
export const handler = async (event: APIGatewayEvent) => {
  // Single-purpose, idempotent function
  // ...
};
```

**Step 4: Validate and Deploy (CDK + Serverless skills)**
```bash
# Validate CDK
./scripts/validate-stack.sh
cdk synth

# Test locally with SAM
sam local invoke

# Deploy
cdk deploy
```

**Step 5: Monitor (Cost & Operations skill)**
```
Query CloudWatch MCP:
"Show me Lambda errors in the last hour"

Query Cost Explorer MCP:
"Analyze costs for the past week by service"

Query CloudTrail MCP:
"Show all API Gateway configuration changes today"
```

## Integrated MCP Servers (10 Total)

This collection integrates with 10+ AWS MCP servers across three categories:

### Development & Infrastructure (2 servers)
1. **AWS Documentation MCP** - Latest AWS service information
2. **AWS CDK MCP** - CDK construct guidance

### Application Lifecycle (5 servers)
3. **AWS Serverless MCP (SAM CLI)** - Serverless app lifecycle
4. **AWS Lambda Tool MCP** - Function execution
5. **AWS Step Functions MCP** - Workflow orchestration
6. **Amazon SNS MCP** - Pub/sub messaging
7. **Amazon SQS MCP** - Queue management

### Operations & Cost (8 servers)
8. **AWS Billing and Cost Management MCP** - Real-time billing
9. **AWS Pricing MCP** - Cost estimation
10. **AWS Cost Explorer MCP** - Cost analysis
11. **Amazon CloudWatch MCP** - Metrics and logs
12. **CloudWatch Application Signals MCP** - APM
13. **AWS Managed Prometheus MCP** - Container monitoring
14. **AWS CloudTrail MCP** - Audit logging
15. **AWS Well-Architected Security Assessment Tool MCP** - Security posture

**Note:** Some servers like AWS Documentation MCP are shared across skills.

## Installation

### Install All Three Skills

```bash
# Clone or download the AWSSkills collection
cd /path/to/AISkills/AWSSkills

# Copy all skills to Claude Code skills directory
cp -r aws-cdk-development ~/.claude/skills/
cp -r aws-serverless-eda ~/.claude/skills/
cp -r aws-cost-operations ~/.claude/skills/

# Or create symlinks
ln -s /path/to/AWSSkills/aws-cdk-development ~/.claude/skills/aws-cdk-development
ln -s /path/to/AWSSkills/aws-serverless-eda ~/.claude/skills/aws-serverless-eda
ln -s /path/to/AWSSkills/aws-cost-operations ~/.claude/skills/aws-cost-operations
```

### Install Individual Skills

You can also install skills individually based on your needs:

```bash
# Just infrastructure as code
cp -r aws-cdk-development ~/.claude/skills/

# Just serverless development
cp -r aws-serverless-eda ~/.claude/skills/

# Just operations and cost management
cp -r aws-cost-operations ~/.claude/skills/
```

### MCP Server Configuration

Each skill integrates with specific AWS MCP servers. Configure them in your Claude Code MCP settings.

**MCP Server Setup Resources:**
- [AWS MCP Servers Documentation](https://awslabs.github.io/mcp/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Claude Agent Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)

## Prerequisites

### Required Tools

**All Skills:**
- AWS CLI with configured credentials
- AWS account with appropriate permissions

**CDK Development:**
- AWS CDK CLI: `npm install -g aws-cdk`
- Node.js 18+ (for TypeScript/JavaScript)
- Python 3.9+ (for Python CDK)

**Serverless & EDA:**
- AWS SAM CLI: `pip install aws-sam-cli`
- Node.js 18+ or Python 3.9+

**Cost & Operations:**
- CloudWatch CLI (included with AWS CLI)
- Optional: Prometheus for local testing

### AWS Credentials

Configure AWS credentials using one of these methods:

```bash
# Method 1: AWS CLI configure
aws configure

# Method 2: Environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1

# Method 3: AWS SSO
aws sso login --profile my-profile
export AWS_PROFILE=my-profile
```

### IAM Permissions

Your AWS user/role needs permissions for the services you'll use:

**CDK Development:**
- CloudFormation (create/update/delete stacks)
- Services being deployed (Lambda, S3, DynamoDB, etc.)
- IAM (for creating roles and policies)
- S3 (for CDK asset storage)

**Serverless & EDA:**
- Lambda (create/update/invoke functions)
- API Gateway (create/update APIs)
- EventBridge (create/update rules)
- Step Functions (create/execute state machines)
- SQS/SNS (create queues/topics, send/receive)
- DynamoDB (create tables, read/write)

**Cost & Operations:**
- CloudWatch (read/write metrics, logs, alarms)
- Cost Explorer (read cost and usage data)
- Billing and Cost Management (read billing)
- AWS Pricing (read pricing data)
- CloudTrail (read trail data, lookup events)
- Managed Prometheus (query metrics)

## Usage Patterns

### Pattern 1: New Serverless Application

```
1. Use Cost & Operations skill to estimate costs
2. Use CDK skill to define infrastructure
3. Use Serverless skill to implement application logic
4. Use CDK skill to validate and deploy
5. Use Cost & Operations skill to monitor and optimize
```

### Pattern 2: Cost Optimization Initiative

```
1. Use Cost & Operations skill (Cost Explorer MCP) to analyze spending
2. Identify high-cost resources and services
3. Use CDK skill to implement optimizations (right-sizing, auto-scaling)
4. Use Serverless skill to optimize Lambda functions
5. Use Cost & Operations skill to track savings
```

### Pattern 3: Security Audit

```
1. Use Cost & Operations skill (CloudTrail MCP) to review API activity
2. Use Cost & Operations skill (Security Assessment MCP) to assess posture
3. Use CDK skill to implement security improvements
4. Use Serverless skill to add encryption and IAM controls
5. Use Cost & Operations skill to monitor security events
```

### Pattern 4: Event-Driven Architecture

```
1. Use Serverless skill to design event-driven workflow
2. Use CDK skill to define EventBridge rules, queues, and topics
3. Use Serverless skill to implement Lambda event handlers
4. Use Serverless skill (Step Functions MCP) to orchestrate complex flows
5. Use Cost & Operations skill to monitor event processing
```

## Key Principles Across All Skills

### From CDK Development
- **No explicit resource naming** - Let CDK generate names for reusability
- **Multi-layer validation** - IDE (cdk-nag) + synthesis + pre-commit
- **Use appropriate constructs** - NodejsFunction, PythonFunction for auto-bundling

### From Serverless & EDA
- **Speedy, Simple, Singular** - Focused, single-purpose functions
- **Think concurrent requests** - Design for concurrency, not volume
- **Share nothing** - Use external state stores
- **Orchestrate with state machines** - Use Step Functions, not function chaining
- **Design for failures** - Idempotency and retry logic

### From Cost & Operations
- **Estimate before deploying** - Use Pricing MCP for cost estimation
- **Monitor proactively** - Set up alarms before issues occur
- **Tag everything** - Use cost allocation tags consistently
- **Audit regularly** - Review CloudTrail logs for compliance
- **Optimize continuously** - Act on cost and performance recommendations

## Structure

```
AWSSkills/
├── README.md                           # This file
├── aws-cdk-development/                # CDK Development Skill
│   ├── SKILL.md                        # Skill definition (YAML frontmatter)
│   ├── README.md                       # Comprehensive CDK guide
│   ├── CHANGELOG.md                    # Version history
│   ├── LICENSE                         # MIT License
│   ├── references/
│   │   └── cdk-patterns.md             # CDK patterns and anti-patterns
│   └── scripts/
│       └── validate-stack.sh           # Pre-deployment validation
├── aws-serverless-eda/                 # Serverless & EDA Skill
│   ├── SKILL.md                        # Skill definition (YAML frontmatter)
│   ├── README.md                       # Comprehensive serverless guide
│   ├── CHANGELOG.md                    # Version history
│   ├── LICENSE                         # MIT License
│   └── references/
│       ├── serverless-patterns.md      # Serverless architecture patterns
│       ├── eda-patterns.md             # Event-driven patterns
│       ├── security-best-practices.md  # Security guidance
│       ├── observability-best-practices.md  # Monitoring and tracing
│       ├── performance-optimization.md      # Performance tuning
│       └── deployment-best-practices.md     # CI/CD and deployment
└── aws-cost-operations/                # Cost & Operations Skill
    ├── SKILL.md                        # Skill definition (YAML frontmatter)
    ├── README.md                       # Comprehensive operations guide
    ├── CHANGELOG.md                    # Version history
    ├── LICENSE                         # MIT License
    └── references/
        ├── operations-patterns.md      # Operational patterns
        └── cloudwatch-alarms.md        # CloudWatch alarm configurations
```

## Documentation Quality

Each skill includes:

- **SKILL.md** - Concise skill definition (<500 words) with YAML frontmatter
- **README.md** - Comprehensive user guide (2000-4000 words)
- **CHANGELOG.md** - Complete version history
- **LICENSE** - MIT License
- **Reference files** - Detailed patterns, best practices, and examples

## Real-World Applications

### E-Commerce Platform
- **CDK**: Define API Gateway, Lambda, DynamoDB, S3 infrastructure
- **Serverless**: Implement order processing workflow with Step Functions
- **Cost & Operations**: Monitor costs, track performance, audit transactions

### Data Processing Pipeline
- **CDK**: Define S3 buckets, Lambda functions, Kinesis streams
- **Serverless**: Implement event-driven processing with SQS/SNS
- **Cost & Operations**: Monitor processing metrics, optimize costs

### Multi-Region API
- **CDK**: Deploy same stack to multiple regions (enabled by no resource naming)
- **Serverless**: Implement API handlers with DynamoDB Global Tables
- **Cost & Operations**: Compare costs across regions, monitor latency

### Microservices Architecture
- **CDK**: Define service infrastructure with API Gateway and Lambda
- **Serverless**: Implement event-driven communication with EventBridge
- **Cost & Operations**: Track costs per service, monitor service health

## Resources

### Official AWS Resources
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [AWS Cost Optimization](https://aws.amazon.com/pricing/cost-optimization/)
- [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)

### AWS MCP Servers
- [AWS MCP Servers Documentation](https://awslabs.github.io/mcp/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)

### Learning Resources
- [AWS Workshops](https://workshops.aws/)
- [ServerlessLand Patterns](https://serverlessland.com/patterns)
- [CDK Patterns](https://cdkpatterns.com/)
- [AWS Well-Architected Labs](https://wellarchitectedlabs.com/)

## Contributing

This collection is part of the AISkills repository. For improvements:

1. Test changes thoroughly with real AWS projects
2. Follow the existing documentation structure
3. Update CHANGELOG.md for each affected skill
4. Ensure all validation scripts pass
5. Update this collection README if adding new features

## License

MIT License - See individual LICENSE files in each skill directory.

**Original Repository:** [zxkane/aws-skills](https://github.com/zxkane/aws-skills)

**Copyright:**
- Original Work: (c) 2025 Mengxin Zhu
- AISkills Integration: (c) 2025 Lee Gonzales

## Version Information

- **Collection Version**: 1.0.0
- **AWS CDK Development**: v1.0.0
- **AWS Serverless & EDA**: v1.0.0
- **AWS Cost & Operations**: v1.0.0
- **Last Updated**: 2025-11-16
- **Maintained By**: AISkills Collection

---

**Get Started:**

1. Install prerequisites (AWS CLI, CDK CLI, SAM CLI)
2. Configure AWS credentials
3. Install the three skills to your Claude Code skills directory
4. Configure MCP servers
5. Start building on AWS with expert guidance!
