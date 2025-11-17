# AWS Serverless & Event-Driven Architecture Skill

Expert guidance for building serverless applications and event-driven architectures on AWS based on the Well-Architected Framework principles.

## Overview

This skill provides comprehensive patterns and best practices for designing and implementing serverless applications using AWS Lambda, API Gateway, EventBridge, Step Functions, and other managed services. It's grounded in the AWS Well-Architected Serverless Lens and includes integration with five powerful MCP servers for complete serverless development lifecycle management.

## When to Use This Skill

Use this skill when you need to:

- Build serverless APIs with Lambda and API Gateway
- Design event-driven architectures with EventBridge
- Implement microservices patterns
- Create asynchronous processing workflows
- Orchestrate multi-service transactions with Step Functions
- Build real-time data processing pipelines
- Implement saga patterns for distributed transactions
- Design for scale, resilience, and cost efficiency
- Work with serverless messaging (SQS, SNS)

**Keywords**: serverless, Lambda, API Gateway, event-driven, async processing, EventBridge, Step Functions, microservices, queues, pub/sub, SQS, SNS, REST APIs, HTTP APIs, DynamoDB, serverless patterns

## Integrated MCP Servers

This skill works with **five specialized MCP servers** for complete serverless development:

### 1. AWS Documentation MCP Server

**Use to verify AWS service information before implementation:**

- Search AWS documentation for latest serverless features
- Check regional availability of Lambda runtimes and services
- Verify service limits (Lambda concurrency, API Gateway limits, etc.)
- Confirm API specifications and parameters
- Access up-to-date AWS service information

**Example queries:**
- "Check Lambda memory and timeout limits"
- "Verify EventBridge schema registry features"
- "What are SQS FIFO queue limitations?"
- "Latest API Gateway HTTP API features"

### 2. AWS Serverless MCP Server (SAM CLI)

**Complete serverless application lifecycle:**

- Initialize new serverless applications with SAM templates
- Deploy serverless applications
- Test Lambda functions locally
- Generate and validate SAM templates
- Manage serverless application lifecycle
- Package and deploy with SAM

**Use for:**
- Local testing before deployment
- SAM-based project initialization
- Serverless application packaging
- Rapid prototyping

### 3. AWS Lambda Tool MCP Server

**Execute Lambda functions as tools:**

- Invoke Lambda functions directly
- Test Lambda integrations end-to-end
- Execute workflows requiring private resource access
- Run Lambda-based automation tasks
- Test function responses and error handling

**Use for:**
- Integration testing
- Workflow validation
- Function invocation testing
- Private resource access

### 4. AWS Step Functions MCP Server

**Execute complex workflows and orchestration:**

- Create and manage state machines
- Execute workflow orchestrations
- Handle distributed transactions
- Implement saga patterns with compensation
- Coordinate microservices
- Manage long-running workflows

**Use for:**
- Multi-step workflows
- Distributed transaction coordination
- Saga pattern implementation
- Service orchestration

### 5. Amazon SNS/SQS MCP Server

**Event-driven messaging and queue management:**

- Publish messages to SNS topics
- Send/receive messages from SQS queues
- Manage event-driven communication
- Implement pub/sub patterns
- Handle asynchronous processing
- Test message routing

**Use for:**
- Message publishing/consumption testing
- Queue depth monitoring
- Fan-out pattern validation
- Event routing verification

## AWS Well-Architected Serverless Design Principles

This skill is based on the seven core principles from the AWS Well-Architected Serverless Lens:

### 1. Speedy, Simple, Singular

**Functions should be concise and single-purpose.**

```typescript
// ✅ GOOD - Single purpose, focused function
export const processOrder = async (event: OrderEvent) => {
  const order = await validateOrder(event);
  await saveOrder(order);
  await publishOrderCreatedEvent(order);
  return { statusCode: 200, body: JSON.stringify({ orderId: order.id }) };
};

// ❌ BAD - Function does too much
export const handleEverything = async (event: any) => {
  // Handles orders, inventory, payments, shipping...
  // Too many responsibilities
};
```

**Keep functions environmentally efficient:**
- Minimize cold start times
- Optimize memory allocation
- Use provisioned concurrency only when needed
- Leverage connection reuse

### 2. Think Concurrent Requests, Not Total Requests

**Design for concurrency, not volume.** Lambda scales horizontally.

Focus on:
- Concurrent execution limits
- Downstream service throttling
- Shared resource contention
- Connection pool sizing

```typescript
// Consider concurrent Lambda executions accessing DynamoDB
const table = new dynamodb.Table(this, 'Table', {
  billingMode: dynamodb.BillingMode.PAY_PER_REQUEST, // Auto-scales with load
});

// Enable auto-scaling for concurrent load
table.autoScaleReadCapacity({ minCapacity: 5, maxCapacity: 100 });
table.autoScaleWriteCapacity({ minCapacity: 5, maxCapacity: 100 });
```

### 3. Share Nothing

**Function runtime environments are short-lived.**

```typescript
// ❌ BAD - Relying on local file system
export const handler = async (event: any) => {
  fs.writeFileSync('/tmp/data.json', JSON.stringify(data)); // Lost after execution
};

// ✅ GOOD - Use persistent storage
export const handler = async (event: any) => {
  await s3.putObject({
    Bucket: process.env.BUCKET_NAME,
    Key: 'data.json',
    Body: JSON.stringify(data),
  });
};
```

**State management:**
- Use DynamoDB for persistent state
- Use Step Functions for workflow state
- Use ElastiCache for session state
- Use S3 for file storage

### 4. Assume No Hardware Affinity

**Applications must be hardware-agnostic.**

Infrastructure can change without notice:
- Lambda functions can run on different hardware
- Container instances can be replaced
- No assumption about underlying infrastructure

**Design for portability:**
- Use environment variables for configuration
- Avoid hardware-specific optimizations
- Test across different environments

### 5. Orchestrate with State Machines, Not Function Chaining

**Use Step Functions for orchestration.**

```typescript
// ❌ BAD - Lambda function chaining
export const handler1 = async (event: any) => {
  const result = await processStep1(event);
  await lambda.invoke({
    FunctionName: 'handler2',
    Payload: JSON.stringify(result),
  });
};

// ✅ GOOD - Step Functions orchestration
const stateMachine = new stepfunctions.StateMachine(this, 'OrderWorkflow', {
  definition: stepfunctions.Chain
    .start(validateOrder)
    .next(processPayment)
    .next(shipOrder)
    .next(sendConfirmation),
});
```

**Benefits of Step Functions:**
- Visual workflow representation
- Built-in error handling and retries
- Execution history and debugging
- Parallel and sequential execution
- Service integrations without code

### 6. Use Events to Trigger Transactions

**Event-driven over synchronous request/response.**

```typescript
// Pattern: EventBridge integration
const rule = new events.Rule(this, 'OrderRule', {
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
  },
});

rule.addTarget(new targets.LambdaFunction(processOrderFunction));
```

**Benefits:**
- Loose coupling between services
- Asynchronous processing
- Better fault tolerance
- Independent scaling

### 7. Design for Failures and Duplicates

**Operations must be idempotent.**

```typescript
// ✅ GOOD - Idempotent operation
export const handler = async (event: SQSEvent) => {
  for (const record of event.Records) {
    const orderId = JSON.parse(record.body).orderId;

    // Check if already processed (idempotency)
    const existing = await dynamodb.getItem({
      TableName: process.env.TABLE_NAME,
      Key: { orderId },
    });

    if (existing.Item) {
      console.log('Order already processed:', orderId);
      continue; // Skip duplicate
    }

    // Process order
    await processOrder(orderId);

    // Mark as processed
    await dynamodb.putItem({
      TableName: process.env.TABLE_NAME,
      Item: { orderId, processedAt: Date.now() },
    });
  }
};
```

## Event-Driven Architecture Patterns

### Pattern 1: Event Router (EventBridge)

Route events to multiple consumers based on event patterns:

```typescript
const eventBus = new events.EventBus(this, 'AppEventBus', {
  eventBusName: 'application-events',
});

// Create rules for different consumers
new events.Rule(this, 'ProcessOrderRule', {
  eventBus,
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
  },
  targets: [new targets.LambdaFunction(processOrderFunction)],
});

new events.Rule(this, 'NotifyCustomerRule', {
  eventBus,
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
  },
  targets: [new targets.LambdaFunction(notifyCustomerFunction)],
});
```

### Pattern 2: Queue-Based Processing (SQS)

Reliable asynchronous processing with retry and DLQ:

```typescript
const dlq = new sqs.Queue(this, 'DLQ', {
  retentionPeriod: Duration.days(14),
});

const queue = new sqs.Queue(this, 'ProcessingQueue', {
  visibilityTimeout: Duration.seconds(300),
  retentionPeriod: Duration.days(14),
  deadLetterQueue: {
    queue: dlq,
    maxReceiveCount: 3,
  },
});

// Lambda consumer
new lambda.EventSourceMapping(this, 'QueueConsumer', {
  target: processingFunction,
  eventSourceArn: queue.queueArn,
  batchSize: 10,
  maxBatchingWindow: Duration.seconds(5),
});
```

### Pattern 3: Pub/Sub (SNS + SQS Fan-Out)

Fan-out pattern for multiple consumers:

```typescript
const topic = new sns.Topic(this, 'OrderTopic', {
  displayName: 'Order Events',
});

// Multiple queues subscribe to topic
const inventoryQueue = new sqs.Queue(this, 'InventoryQueue');
const shippingQueue = new sqs.Queue(this, 'ShippingQueue');
const analyticsQueue = new sqs.Queue(this, 'AnalyticsQueue');

topic.addSubscription(new subscriptions.SqsSubscription(inventoryQueue));
topic.addSubscription(new subscriptions.SqsSubscription(shippingQueue));
topic.addSubscription(new subscriptions.SqsSubscription(analyticsQueue));
```

### Pattern 4: Saga Pattern with Step Functions

Distributed transactions with compensation:

```typescript
const reserveFlight = new tasks.LambdaInvoke(this, 'ReserveFlight', {
  lambdaFunction: reserveFlightFunction,
  outputPath: '$.Payload',
});

const reserveHotel = new tasks.LambdaInvoke(this, 'ReserveHotel', {
  lambdaFunction: reserveHotelFunction,
  outputPath: '$.Payload',
});

const processPayment = new tasks.LambdaInvoke(this, 'ProcessPayment', {
  lambdaFunction: processPaymentFunction,
  outputPath: '$.Payload',
});

// Compensating transactions
const cancelFlight = new tasks.LambdaInvoke(this, 'CancelFlight', {
  lambdaFunction: cancelFlightFunction,
});

const cancelHotel = new tasks.LambdaInvoke(this, 'CancelHotel', {
  lambdaFunction: cancelHotelFunction,
});

// Define saga with compensation
const definition = reserveFlight
  .next(reserveHotel)
  .next(processPayment)
  .addCatch(cancelHotel.next(cancelFlight), {
    resultPath: '$.error',
  });

new stepfunctions.StateMachine(this, 'BookingStateMachine', {
  definition,
  timeout: Duration.minutes(5),
});
```

### Pattern 5: Event Sourcing

Store events as the source of truth:

```typescript
const eventStore = new dynamodb.Table(this, 'EventStore', {
  partitionKey: { name: 'aggregateId', type: dynamodb.AttributeType.STRING },
  sortKey: { name: 'version', type: dynamodb.AttributeType.NUMBER },
  stream: dynamodb.StreamViewType.NEW_IMAGE,
});

export const handleCommand = async (event: any) => {
  const { aggregateId, eventType, eventData } = event;

  // Get current version
  const items = await dynamodb.query({
    TableName: process.env.EVENT_STORE,
    KeyConditionExpression: 'aggregateId = :id',
    ExpressionAttributeValues: { ':id': aggregateId },
    ScanIndexForward: false,
    Limit: 1,
  });

  const nextVersion = items.Items?.[0]?.version + 1 || 1;

  // Append new event
  await dynamodb.putItem({
    TableName: process.env.EVENT_STORE,
    Item: {
      aggregateId,
      version: nextVersion,
      eventType,
      eventData,
      timestamp: Date.now(),
    },
  });
};
```

## Serverless Architecture Patterns

### Pattern 1: API-Driven Microservices

REST/HTTP APIs with Lambda backend:

```typescript
const api = new apigateway.RestApi(this, 'Api', {
  restApiName: 'microservices-api',
  deployOptions: {
    throttlingRateLimit: 1000,
    throttlingBurstLimit: 2000,
    tracingEnabled: true,
  },
});

const users = api.root.addResource('users');
users.addMethod('GET', new apigateway.LambdaIntegration(getUsersFunction));
users.addMethod('POST', new apigateway.LambdaIntegration(createUserFunction));
```

### Pattern 2: Stream Processing

Real-time data processing with Kinesis:

```typescript
const stream = new kinesis.Stream(this, 'DataStream', {
  shardCount: 2,
  retentionPeriod: Duration.days(7),
});

new lambda.EventSourceMapping(this, 'StreamProcessor', {
  target: processFunction,
  eventSourceArn: stream.streamArn,
  batchSize: 100,
  maxBatchingWindow: Duration.seconds(5),
  parallelizationFactor: 10,
  startingPosition: lambda.StartingPosition.LATEST,
  retryAttempts: 3,
  bisectBatchOnError: true,
});
```

### Pattern 3: Scheduled Jobs

Periodic processing with EventBridge:

```typescript
// Daily cleanup job
new events.Rule(this, 'DailyCleanup', {
  schedule: events.Schedule.cron({ hour: '2', minute: '0' }),
  targets: [new targets.LambdaFunction(cleanupFunction)],
});

// Process every 5 minutes
new events.Rule(this, 'FrequentProcessing', {
  schedule: events.Schedule.rate(Duration.minutes(5)),
  targets: [new targets.LambdaFunction(processFunction)],
});
```

## Best Practices

### Error Handling

Implement partial batch failure handling:

```typescript
export const handler = async (event: SQSEvent) => {
  const failures: SQSBatchItemFailure[] = [];

  for (const record of event.Records) {
    try {
      await processRecord(record);
    } catch (error) {
      console.error('Failed to process record:', record.messageId, error);
      failures.push({ itemIdentifier: record.messageId });
    }
  }

  return { batchItemFailures: failures };
};
```

### Dead Letter Queues

Always configure DLQs with monitoring:

```typescript
const dlq = new sqs.Queue(this, 'DLQ', {
  retentionPeriod: Duration.days(14),
});

new cloudwatch.Alarm(this, 'DLQAlarm', {
  metric: dlq.metricApproximateNumberOfMessagesVisible(),
  threshold: 1,
  evaluationPeriods: 1,
  alarmDescription: 'Messages in DLQ require attention',
});
```

### Observability

Enable tracing and structured logging:

```typescript
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  tracing: lambda.Tracing.ACTIVE, // X-Ray tracing
  environment: {
    POWERTOOLS_SERVICE_NAME: 'order-service',
    POWERTOOLS_METRICS_NAMESPACE: 'MyApp',
    LOG_LEVEL: 'INFO',
  },
});
```

## Using MCP Servers Effectively

### Development Workflow with MCP Servers

1. **Initialize**: Use AWS Serverless MCP to scaffold new projects
2. **Develop**: Write Lambda functions and infrastructure code
3. **Test Locally**: Use SAM MCP for local testing
4. **Test Integration**: Use Lambda Tool MCP to invoke functions
5. **Test Workflows**: Use Step Functions MCP to test orchestrations
6. **Test Messaging**: Use SNS/SQS MCP to test event routing
7. **Verify Services**: Use AWS Docs MCP to confirm latest features
8. **Deploy**: Use SAM or CDK to deploy to AWS

### MCP Server Usage Patterns

- **Serverless MCP**: Project initialization and deployment
- **Lambda Tool MCP**: Integration testing and invocation
- **Step Functions MCP**: Workflow testing and validation
- **SNS/SQS MCP**: Message routing and queue testing
- **AWS Docs MCP**: Service verification and feature confirmation

## Comprehensive Reference Documentation

This skill includes six detailed reference files:

### 1. Serverless Patterns (`references/serverless-patterns.md`)
- Core serverless architectures
- API patterns (REST, HTTP, WebSocket)
- Data processing patterns
- Integration patterns
- Orchestration with Step Functions
- Anti-patterns to avoid

### 2. Event-Driven Architecture Patterns (`references/eda-patterns.md`)
- Event routing and processing
- Event sourcing patterns
- Saga patterns for distributed transactions
- Idempotency patterns
- Message ordering and deduplication
- Error handling strategies

### 3. Security Best Practices (`references/security-best-practices.md`)
- Shared responsibility model
- IAM least privilege patterns
- Data protection and encryption
- Network security with VPC
- API Gateway security
- Secret management

### 4. Observability Best Practices (`references/observability-best-practices.md`)
- Three pillars: metrics, logs, traces
- Structured logging with Lambda Powertools
- X-Ray distributed tracing
- CloudWatch alarms and dashboards
- Performance monitoring

### 5. Performance Optimization (`references/performance-optimization.md`)
- Cold start optimization techniques
- Memory and CPU optimization
- Package size reduction strategies
- Provisioned concurrency patterns
- Connection pooling and reuse

### 6. Deployment Best Practices (`references/deployment-best-practices.md`)
- CI/CD pipeline design
- Testing strategies (unit, integration, load)
- Deployment strategies (canary, blue/green)
- Rollback and safety mechanisms
- Infrastructure validation

## Prerequisites

### Required Tools

- AWS CLI with configured credentials
- AWS SAM CLI (for local testing): `pip install aws-sam-cli`
- Node.js 18+ (for TypeScript/JavaScript Lambda)
- Python 3.9+ (for Python Lambda)
- AWS CDK CLI (optional): `npm install -g aws-cdk`

### AWS Credentials

Configure using AWS CLI, environment variables, or AWS SSO (see CDK skill README for details).

### IAM Permissions

Your AWS user/role needs permissions for:
- Lambda (create/update/invoke functions)
- API Gateway (create/update APIs)
- EventBridge (create/update rules and event buses)
- Step Functions (create/execute state machines)
- SQS/SNS (create queues/topics, send/receive messages)
- DynamoDB (create tables, read/write data)
- CloudWatch (logs, metrics, alarms)
- IAM (create roles and policies)

## Installation

### As a Claude Code Skill

```bash
# Copy to Claude Code skills directory
cp -r aws-serverless-eda ~/.claude/skills/

# Or create a symlink
ln -s /path/to/aws-serverless-eda ~/.claude/skills/aws-serverless-eda
```

### MCP Server Configuration

Configure the five MCP servers in your Claude Code MCP settings:
- AWS Documentation MCP
- AWS Serverless MCP (SAM CLI)
- AWS Lambda Tool MCP
- AWS Step Functions MCP
- Amazon SNS/SQS MCP

Refer to [AWS MCP Servers documentation](https://awslabs.github.io/mcp/) for setup.

## Resources

### Included Files

- `SKILL.md` - Concise skill definition and Well-Architected principles
- `README.md` - This comprehensive guide
- `references/serverless-patterns.md` - Serverless architecture patterns
- `references/eda-patterns.md` - Event-driven architecture patterns
- `references/security-best-practices.md` - Security guidance
- `references/observability-best-practices.md` - Monitoring and tracing
- `references/performance-optimization.md` - Performance tuning
- `references/deployment-best-practices.md` - CI/CD and deployment
- `CHANGELOG.md` - Version history
- `LICENSE` - MIT License

### External Resources

- [AWS Well-Architected Serverless Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/)
- [ServerlessLand Patterns](https://serverlessland.com/patterns)
- [AWS Serverless Workshops](https://serverlessland.com/learn?type=Workshops)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/)

## Contributing

This skill is part of the AISkills collection. For improvements:
1. Test with real serverless applications
2. Follow existing documentation structure
3. Update CHANGELOG.md
4. Verify all reference files

## License

MIT License - See LICENSE file for details.

Original repository: [zxkane/aws-skills](https://github.com/zxkane/aws-skills)

---

**Version**: 1.0.0
**Last Updated**: 2025-11-16
**Maintained By**: AISkills Collection
