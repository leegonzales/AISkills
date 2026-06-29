---
name: aws-serverless-eda
description: AWS serverless and event-driven architecture expert based on Well-Architected Framework. Use when building serverless APIs, Lambda functions, REST APIs, microservices, or async workflows. Covers Lambda with TypeScript/Python, API Gateway (REST/HTTP), DynamoDB, Step Functions, EventBridge, SQS, SNS, and serverless patterns. Essential when user mentions serverless, Lambda, API Gateway, event-driven, async processing, queues, pub/sub, or wants to build scalable serverless applications with AWS best practices.
---

# AWS Serverless & Event-Driven Architecture

Guidance for building serverless applications and event-driven architectures on AWS based on Well-Architected Framework principles.

## When to Use This Skill

Use when building serverless apps with Lambda, designing event-driven architectures, implementing microservices, creating async processing workflows, orchestrating multi-service transactions, building real-time data pipelines, implementing saga patterns for distributed transactions, or designing for scale and resilience.

## Integrated MCP Servers

This skill includes 5 MCP servers. Use them as the primary tools for the tasks below.

- **AWS Documentation MCP** — ALWAYS verify AWS service info before implementation: latest features/best practices, regional availability, service limits/quotas, API specs and parameters.
- **AWS Serverless MCP** — full serverless lifecycle with SAM CLI: initialize, generate SAM templates, deploy, test Lambda locally before deploy.
- **AWS Lambda Tool MCP** — execute Lambda functions as tools: invoke directly, test integrations, run automation, access private resources.
- **AWS Step Functions MCP** — orchestration: create/manage state machines, run distributed transactions, implement saga patterns, coordinate microservices.
- **Amazon SNS/SQS MCP** — event-driven messaging: publish to SNS topics, send/receive SQS messages, implement pub/sub, debug message routing.

## Well-Architected Serverless Design Principles

The 7 design principles that drive every decision in this skill (apply them; reference files carry the implementation patterns):

1. **Speedy, Simple, Singular** — functions are concise and single-purpose. Minimize cold starts, optimize memory, reuse connections, use provisioned concurrency only when needed.
2. **Think Concurrent Requests, Not Total** — Lambda scales horizontally; design for concurrent-execution limits, downstream throttling, shared-resource contention, and connection-pool sizing (e.g. DynamoDB PAY_PER_REQUEST or provisioned + auto-scaling).
3. **Share Nothing** — runtime environments are short-lived; never rely on local FS (`/tmp` is ephemeral). Persist state in DynamoDB (data), Step Functions (workflow), ElastiCache (session), S3 (files).
4. **Assume No Hardware Affinity** — be hardware-agnostic and portable; configure via environment variables, avoid hardware-specific optimizations, test across environments.
5. **Orchestrate with State Machines, Not Function Chaining** — use Step Functions for sequencing, error handling/retries, execution history, and parallel/sequential flows instead of Lambda-invokes-Lambda.
6. **Use Events to Trigger Transactions** — prefer event-driven (S3 notifications, EventBridge rules) over synchronous request/response for loose coupling, async processing, fault tolerance, independent scaling.
7. **Design for Failures and Duplicates** — make operations idempotent (dedupe-check before processing); use retry with exponential backoff and DLQs.

## Core Pattern Catalog

Pattern implementations (CDK/TypeScript) live in reference files. Reach for:

- **Event-driven:** event router (EventBridge), queue-based processing (SQS), pub/sub fan-out (SNS+SQS), saga with Step Functions, event sourcing → `references/eda-patterns.md`
- **Serverless:** API-driven microservices, stream processing (Kinesis), async task processing, scheduled jobs (EventBridge cron/rate), webhook processing → `references/serverless-patterns.md`

## Key Operational Practices

- **Partial batch failure** — return `batchItemFailures` from SQS/stream handlers so only failed records retry; set `reportBatchItemFailures: true` on the event source mapping.
- **Dead Letter Queues** — always configure a DLQ (`maxReceiveCount`) and alarm on DLQ depth.
- **Observability** — enable X-Ray (`tracing: ACTIVE`) and Lambda Powertools env vars (`POWERTOOLS_SERVICE_NAME`, `POWERTOOLS_METRICS_NAMESPACE`, `LOG_LEVEL`).

Full implementations and deeper guidance are in the reference files below.

## Reference Files

- `references/serverless-patterns.md` — core serverless architectures, API patterns, data processing, Step Functions orchestration, anti-patterns, plus fan-out/scheduled/webhook trigger patterns.
- `references/eda-patterns.md` — event routing/processing, event sourcing, saga patterns, idempotency, ordering/deduplication, error handling.
- `references/security-best-practices.md` — shared responsibility model, IAM least privilege, data protection/encryption, VPC network security.
- `references/observability-best-practices.md` — metrics/logs/traces, structured logging with Powertools, X-Ray tracing, CloudWatch alarms/dashboards.
- `references/performance-optimization.md` — cold-start optimization, memory/CPU tuning, package-size reduction, provisioned concurrency.
- `references/deployment-best-practices.md` — CI/CD pipelines, testing (unit/integration/load), canary/blue-green strategies, rollback safety.

**External Resources:**
- AWS Well-Architected Serverless Lens: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/
- ServerlessLand.com — pre-built serverless patterns
- AWS Serverless Workshops: https://serverlessland.com/learn?type=Workshops
