# Changelog

All notable changes to the AWS Serverless & Event-Driven Architecture skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-16

### Added
- Initial release of AWS Serverless & Event-Driven Architecture skill
- Comprehensive SKILL.md based on AWS Well-Architected Serverless Lens
- Detailed README.md with extensive real-world patterns
- Seven Well-Architected serverless design principles
- Five event-driven architecture patterns
- Five serverless architecture patterns
- Integration with AWS Documentation MCP server
- Integration with AWS Serverless MCP server (SAM CLI)
- Integration with AWS Lambda Tool MCP server
- Integration with AWS Step Functions MCP server
- Integration with Amazon SNS/SQS MCP server
- Serverless patterns reference (references/serverless-patterns.md)
- Event-driven architecture patterns reference (references/eda-patterns.md)
- Security best practices reference (references/security-best-practices.md)
- Observability best practices reference (references/observability-best-practices.md)
- Performance optimization reference (references/performance-optimization.md)
- Deployment best practices reference (references/deployment-best-practices.md)
- MIT License

### Documentation

#### Well-Architected Principles
- Speedy, Simple, Singular (focused functions)
- Think Concurrent Requests, Not Total Requests
- Share Nothing (stateless functions)
- Assume No Hardware Affinity
- Orchestrate with State Machines, Not Function Chaining
- Use Events to Trigger Transactions
- Design for Failures and Duplicates (idempotency)

#### Event-Driven Patterns
- Event Router with EventBridge
- Queue-Based Processing with SQS
- Pub/Sub with SNS + SQS Fan-Out
- Saga Pattern with Step Functions
- Event Sourcing with DynamoDB Streams

#### Serverless Patterns
- API-Driven Microservices
- Stream Processing with Kinesis
- Scheduled Jobs with EventBridge
- Webhook Processing
- Async Task Processing

#### Best Practices
- Error handling with partial batch failures
- Dead Letter Queue configuration and monitoring
- Observability with X-Ray and CloudWatch
- Idempotency patterns
- Retry strategies with exponential backoff

### Features
- Support for TypeScript/JavaScript Lambda functions
- Support for Python Lambda functions
- EventBridge event routing and filtering
- Step Functions workflow orchestration
- SQS queue processing with DLQ
- SNS pub/sub messaging
- Lambda event source mappings
- API Gateway REST and HTTP APIs
- DynamoDB integration patterns
- Kinesis stream processing
- SAM-based local testing
- Complete MCP server integration workflow

### References
- Comprehensive serverless architecture patterns
- Event-driven architecture implementation guide
- Security best practices aligned with AWS Well-Architected
- Observability with metrics, logs, and traces
- Performance optimization techniques
- CI/CD and deployment strategies

[1.0.0]: https://github.com/leegonzales/AISkills/releases/tag/aws-serverless-eda-v1.0.0
