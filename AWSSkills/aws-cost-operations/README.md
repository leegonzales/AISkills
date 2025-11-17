# AWS Cost & Operations Skill

Expert guidance for AWS cost optimization, monitoring, observability, and operational excellence with integrated MCP servers for comprehensive cloud operations management.

## Overview

This skill provides best practices and patterns for managing AWS costs, implementing monitoring and observability, conducting security audits, and achieving operational excellence. It integrates with **eight powerful MCP servers** covering billing, cost analysis, monitoring, observability, and security assessment.

## When to Use This Skill

Use this skill when you need to:

- Optimize AWS costs and reduce spending
- Estimate costs before deploying resources
- Monitor application and infrastructure performance
- Set up observability and alerting systems
- Analyze spending patterns and identify cost anomalies
- Investigate operational issues and performance bottlenecks
- Audit AWS activity and track resource changes
- Assess security posture against Well-Architected Framework
- Implement operational excellence practices
- Track CloudWatch metrics and logs
- Monitor containerized applications with Prometheus
- Review CloudTrail audit logs

**Keywords**: cost optimization, billing, cost explorer, CloudWatch, monitoring, observability, CloudTrail, audit, security assessment, operations, alarms, metrics, logs, Prometheus

## Integrated MCP Servers

This skill works with **eight specialized MCP servers** organized into three categories:

### Cost Management Servers

#### 1. AWS Billing and Cost Management MCP Server

**Real-time billing and cost management:**

- View current AWS spending and trends
- Analyze billing details across services
- Track budget utilization
- Monitor cost allocation tags
- Review consolidated billing for organizations

**Use for:**
- Monthly spending reviews
- Budget tracking
- Cost allocation analysis
- Billing detail investigation

#### 2. AWS Pricing MCP Server

**Pre-deployment cost estimation and optimization:**

- Estimate costs before deploying resources
- Compare pricing across regions
- Calculate Total Cost of Ownership (TCO)
- Evaluate different service options for cost efficiency
- Get current pricing information for AWS services

**Use for:**
- Pre-deployment cost estimation
- Regional pricing comparison
- Service option evaluation
- TCO calculations

#### 3. AWS Cost Explorer MCP Server

**Detailed cost analysis and reporting:**

- Analyze historical spending patterns
- Create custom cost reports
- Identify cost anomalies and trends
- Forecast future costs
- Analyze cost by service, region, or tag
- Generate cost optimization recommendations

**Use for:**
- Historical cost analysis
- Anomaly detection
- Cost forecasting
- Optimization recommendations
- Custom reporting

### Monitoring & Observability Servers

#### 4. Amazon CloudWatch MCP Server

**Metrics, alarms, and logs analysis:**

- Query CloudWatch metrics and logs
- Create and manage CloudWatch alarms
- Analyze application performance metrics
- Troubleshoot operational issues
- Set up custom dashboards
- Monitor resource utilization

**Use for:**
- Performance monitoring
- Log analysis and troubleshooting
- Alarm configuration
- Dashboard creation
- Resource utilization tracking

#### 5. Amazon CloudWatch Application Signals MCP Server

**Application monitoring and performance insights:**

- Monitor application health and performance
- Analyze service-level objectives (SLOs)
- Track application dependencies
- Identify performance bottlenecks
- Monitor service map and traces

**Use for:**
- Application performance monitoring (APM)
- SLO tracking
- Dependency analysis
- Performance optimization
- Service health monitoring

#### 6. AWS Managed Prometheus MCP Server

**Prometheus-compatible monitoring for containers:**

- Query Prometheus metrics
- Monitor containerized applications
- Analyze Kubernetes workload metrics
- Create PromQL queries
- Track custom application metrics

**Use for:**
- Container monitoring
- Kubernetes metrics
- PromQL query execution
- Custom metric tracking
- EKS/ECS observability

### Audit & Security Servers

#### 7. AWS CloudTrail MCP Server

**AWS API activity and audit analysis:**

- Analyze AWS API calls and user activity
- Track resource changes and modifications
- Investigate security incidents
- Audit compliance requirements
- Identify unusual access patterns
- Review who made what changes when

**Use for:**
- Security incident investigation
- Compliance auditing
- Change tracking
- Access pattern analysis
- Root cause analysis

#### 8. AWS Well-Architected Security Assessment Tool MCP Server

**Security assessment against Well-Architected Framework:**

- Assess security posture against AWS best practices
- Identify security gaps and vulnerabilities
- Get security improvement recommendations
- Review security pillar compliance
- Generate security assessment reports

**Use for:**
- Security posture assessment
- Gap analysis
- Compliance validation
- Security improvement planning
- Well-Architected reviews

## Cost Optimization Best Practices

### Pre-Deployment Cost Estimation

**Always estimate costs before deploying resources:**

1. Use **AWS Pricing MCP** to estimate resource costs
2. Compare pricing across different regions
3. Evaluate alternative service options
4. Calculate expected monthly costs
5. Plan for scaling and growth

**Example workflow:**

```
"Estimate the monthly cost of running a Lambda function with
1 million invocations, 512MB memory, 3-second duration in us-east-1"
```

**Response analysis:**
- Lambda compute cost
- Request cost
- Data transfer cost (if applicable)
- CloudWatch Logs cost
- Total estimated monthly cost

### Cost Analysis and Optimization

**Regular cost review process:**

1. **Weekly Reviews**: Use Cost Explorer MCP to analyze spending trends
2. **Anomaly Detection**: Identify unexpected charges and cost spikes
3. **Service Breakdown**: Review costs by service, region, and environment
4. **Budget Comparison**: Compare actual vs. budgeted costs
5. **Action Items**: Generate and implement cost optimization recommendations

**Cost optimization strategies:**

- **Right-sizing**: Match resources to actual usage patterns
- **Storage optimization**: Use appropriate S3 storage classes, delete old EBS snapshots
- **Auto-scaling**: Implement auto-scaling for dynamic workloads
- **Savings Plans**: Leverage Savings Plans and Reserved Instances for steady-state workloads
- **Resource cleanup**: Delete unused resources, stop non-production instances
- **Cost allocation tags**: Use consistent tagging for accurate cost attribution

### Budget Monitoring

**Proactive spending management:**

1. Use **Billing and Cost Management MCP** to monitor budgets
2. Set up budget alerts for threshold breaches
3. Review budget utilization weekly
4. Adjust budgets based on trends and forecasts
5. Implement cost controls and governance policies

**Budget alert thresholds:**
- 50% of budget (early warning)
- 80% of budget (action required)
- 100% of budget (critical alert)

## Monitoring and Observability Best Practices

### CloudWatch Metrics and Alarms

**Implement comprehensive monitoring:**

1. **Define Critical Metrics**: Identify business-critical metrics to monitor
2. **Set Up Alarms**: Use CloudWatch MCP to create alarms for:
   - CPU and memory utilization
   - Error rates and latency
   - Queue depths and processing times
   - API Gateway throttling and errors
   - Lambda errors, timeouts, and throttles
3. **Create Dashboards**: Visualize key metrics for stakeholders
4. **Log Insights**: Use CloudWatch Logs Insights for troubleshooting

**Example alarm scenarios:**

```typescript
// Lambda error rate alarm
new cloudwatch.Alarm(this, 'LambdaErrorAlarm', {
  metric: lambdaFunction.metricErrors({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 2,
  alarmDescription: 'Lambda function error rate exceeded threshold',
});

// API Gateway 5xx errors
new cloudwatch.Alarm(this, 'Api5xxAlarm', {
  metric: api.metricServerError({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 5,
  evaluationPeriods: 1,
  alarmDescription: 'API Gateway 5xx errors detected',
});

// DynamoDB throttled requests
new cloudwatch.Alarm(this, 'DynamoThrottleAlarm', {
  metric: table.metricSystemErrorsForOperations({
    operations: [dynamodb.Operation.PUT_ITEM, dynamodb.Operation.GET_ITEM],
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 1,
  evaluationPeriods: 1,
  alarmDescription: 'DynamoDB throttled requests detected',
});
```

### Application Performance Monitoring

**Monitor application health with CloudWatch Application Signals:**

1. **Track SLOs**: Define and monitor service-level objectives
2. **Dependency Mapping**: Visualize application dependencies
3. **Bottleneck Identification**: Identify slow components and operations
4. **Distributed Tracing**: Trace requests across microservices
5. **Health Scores**: Monitor application health metrics

**Key SLO metrics:**
- Availability (uptime %)
- Latency (p50, p95, p99)
- Error rate (%)
- Throughput (requests/second)

### Container and Kubernetes Monitoring

**For containerized workloads with AWS Managed Prometheus:**

1. **Scrape Metrics**: Configure Prometheus to scrape container metrics
2. **Monitor Resources**: Track CPU, memory, and network for containers
3. **Pod Health**: Monitor pod and node health
4. **Custom Metrics**: Create PromQL queries for application-specific metrics
5. **Alert Configuration**: Set up alerts for container anomalies

**Example PromQL queries:**

```promql
# Container CPU usage
sum(rate(container_cpu_usage_seconds_total[5m])) by (pod)

# Pod memory usage
sum(container_memory_usage_bytes) by (pod) / 1024 / 1024

# Request rate per service
sum(rate(http_requests_total[5m])) by (service)

# Error rate per endpoint
sum(rate(http_requests_total{status=~"5.."}[5m])) by (endpoint)
```

## Audit and Security Best Practices

### CloudTrail Activity Analysis

**Comprehensive AWS activity auditing:**

1. Use **CloudTrail MCP** to analyze API activity
2. Track who made changes to resources
3. Investigate security incidents
4. Monitor for suspicious activity patterns
5. Audit compliance with organizational policies

**Common audit scenarios:**

- "Who deleted this S3 bucket?"
- "Show all IAM role changes in the last 24 hours"
- "List failed login attempts in the past week"
- "Find all actions performed by user X"
- "Track modifications to security group Y"
- "Review all resource deletions this month"

**CloudTrail query examples:**

```json
// Find all S3 bucket deletions
{
  "eventName": "DeleteBucket",
  "eventSource": "s3.amazonaws.com"
}

// Track IAM policy changes
{
  "eventSource": "iam.amazonaws.com",
  "eventName": ["PutRolePolicy", "AttachRolePolicy", "DetachRolePolicy"]
}

// Monitor failed authentication
{
  "errorCode": "AccessDenied",
  "errorMessage": "*authentication*"
}
```

### Security Assessment

**Regular security reviews with Well-Architected Security Assessment:**

1. **Baseline Assessment**: Run initial security assessment
2. **Gap Identification**: Identify security gaps and vulnerabilities
3. **Prioritization**: Prioritize security improvements based on risk
4. **Implementation**: Implement recommended security improvements
5. **Re-assessment**: Validate improvements and track progress

**Security assessment areas (AWS Well-Architected Security Pillar):**

- **Identity and Access Management (IAM)**
  - Least privilege access
  - Role-based access control (RBAC)
  - MFA enforcement
  - Access key rotation

- **Detective Controls**
  - CloudTrail logging
  - CloudWatch monitoring
  - GuardDuty threat detection
  - Security Hub findings

- **Infrastructure Protection**
  - VPC security and network isolation
  - Security group configuration
  - Network ACL rules
  - WAF protection

- **Data Protection**
  - Encryption at rest (S3, EBS, RDS)
  - Encryption in transit (TLS/SSL)
  - Key management (KMS)
  - Data classification and handling

- **Incident Response**
  - Incident response plan
  - Automated remediation
  - Forensic capabilities
  - Communication procedures

## Using MCP Servers Effectively

### Cost Management Workflow

1. **Pre-deployment**: Use **Pricing MCP** to estimate costs
2. **Post-deployment**: Use **Billing MCP** to track actual spending
3. **Analysis**: Use **Cost Explorer MCP** for detailed cost breakdown and trends
4. **Optimization**: Implement recommendations from Cost Explorer
5. **Monitoring**: Set up budget alerts and review regularly

### Monitoring Workflow

1. **Setup**: Configure CloudWatch metrics and alarms
2. **Monitor**: Use **CloudWatch MCP** to track key metrics
3. **Analyze**: Use **Application Signals MCP** for APM insights
4. **Troubleshoot**: Query CloudWatch Logs Insights for issue resolution
5. **Container Monitoring**: Use **Prometheus MCP** for containerized workloads

### Security Workflow

1. **Audit**: Use **CloudTrail MCP** to review API activity
2. **Assess**: Use **Well-Architected Security Assessment MCP**
3. **Remediate**: Implement security recommendations
4. **Monitor**: Track security events via CloudWatch
5. **Review**: Regular security posture assessments

### MCP Usage Best Practices

1. **Cost Awareness**: Always check pricing before deploying new resources
2. **Proactive Monitoring**: Set up alarms for critical metrics before issues occur
3. **Regular Reviews**: Analyze costs and performance weekly
4. **Audit Trails**: Review CloudTrail logs regularly for compliance
5. **Security First**: Run security assessments quarterly or after major changes
6. **Optimize Continuously**: Act on cost and performance recommendations promptly

## Operational Excellence Guidelines

### Cost Optimization

- **Tag Everything**: Use consistent cost allocation tags across all resources
- **Review Monthly**: Analyze spending trends, anomalies, and optimization opportunities
- **Right-size**: Match resource sizes to actual usage patterns
- **Automate**: Use auto-scaling and scheduling to optimize costs
- **Monitor Budgets**: Set alerts for cost overruns and take corrective action

### Monitoring and Alerting

- **Critical Metrics**: Alert on business-critical metrics that require immediate action
- **Noise Reduction**: Fine-tune thresholds to reduce false positives
- **Actionable Alerts**: Ensure alerts have clear remediation steps and runbooks
- **Dashboard Visibility**: Create dashboards for key stakeholders
- **Log Retention**: Balance cost and compliance needs for log retention

### Security and Compliance

- **Least Privilege**: Grant minimum required permissions following IAM best practices
- **Audit Regularly**: Review CloudTrail logs for anomalies and suspicious activity
- **Encrypt Data**: Use encryption at rest and in transit for all sensitive data
- **Assess Continuously**: Run security assessments frequently, not just annually
- **Incident Response**: Have documented procedures for security events

## Real-World Examples

### Cost Optimization Example

```typescript
// Use Cost Explorer to identify high-cost resources
// Then implement optimizations:

// 1. Right-size over-provisioned EC2 instances
const instance = new ec2.Instance(this, 'WebServer', {
  instanceType: ec2.InstanceType.of(
    ec2.InstanceClass.T3,  // Changed from M5 to T3 based on usage
    ec2.InstanceSize.MEDIUM // Changed from LARGE to MEDIUM
  ),
  // ... other properties
});

// 2. Use S3 lifecycle policies for cost reduction
const bucket = new s3.Bucket(this, 'DataBucket', {
  lifecycleRules: [
    {
      transitions: [
        {
          storageClass: s3.StorageClass.INFREQUENT_ACCESS,
          transitionAfter: Duration.days(30),
        },
        {
          storageClass: s3.StorageClass.GLACIER,
          transitionAfter: Duration.days(90),
        },
      ],
      expiration: Duration.days(365),
    },
  ],
});

// 3. Implement auto-scaling to reduce costs
const autoScaling = asg.addToAutoScalingGroup(this, 'ASG', {
  minCapacity: 2,
  maxCapacity: 10,
  targetCpuUtilization: 70,
});
```

### Monitoring Example

```typescript
// Comprehensive monitoring setup

// 1. CloudWatch Dashboard
const dashboard = new cloudwatch.Dashboard(this, 'AppDashboard', {
  dashboardName: 'application-metrics',
});

// 2. Add widgets for key metrics
dashboard.addWidgets(
  new cloudwatch.GraphWidget({
    title: 'Lambda Errors',
    left: [lambdaFunction.metricErrors()],
  }),
  new cloudwatch.GraphWidget({
    title: 'API Latency',
    left: [api.metricLatency()],
  })
);

// 3. Set up alarms with SNS notifications
const topic = new sns.Topic(this, 'AlarmTopic');
topic.addSubscription(new subscriptions.EmailSubscription('ops@example.com'));

const alarm = new cloudwatch.Alarm(this, 'HighErrorRate', {
  metric: lambdaFunction.metricErrors(),
  threshold: 10,
  evaluationPeriods: 2,
  alarmDescription: 'Lambda error rate is too high',
});

alarm.addAlarmAction(new cw_actions.SnsAction(topic));
```

## Comprehensive Reference Documentation

This skill includes two detailed reference files:

### 1. Operations Patterns (`references/operations-patterns.md`)

- Cost optimization strategies and patterns
- Monitoring and alerting best practices
- Observability implementation patterns
- Security and compliance guidelines
- Troubleshooting workflows
- Incident response procedures

### 2. CloudWatch Alarms Reference (`references/cloudwatch-alarms.md`)

Common alarm configurations for:
- Lambda functions (errors, duration, throttles)
- EC2 instances (CPU, memory, disk, status checks)
- RDS databases (CPU, connections, storage, replication lag)
- DynamoDB tables (throttles, errors, capacity)
- API Gateway (errors, latency, cache)
- ECS services (CPU, memory, running tasks)
- Application Load Balancers (targets, response time, errors)

## Prerequisites

### Required Tools

- AWS CLI with configured credentials
- CloudWatch CLI (included with AWS CLI)
- AWS Management Console access
- Optional: Prometheus for local testing

### AWS Credentials

Configure using AWS CLI, environment variables, or AWS SSO (see CDK skill README for details).

### IAM Permissions

Your AWS user/role needs permissions for:
- CloudWatch (read/write metrics, logs, alarms)
- Cost Explorer (read cost and usage data)
- Billing and Cost Management (read billing data)
- AWS Pricing (read pricing data)
- CloudTrail (read trail data, lookup events)
- Managed Prometheus (query metrics)
- IAM (read roles and policies for security assessment)

## Installation

### As a Claude Code Skill

```bash
# Copy to Claude Code skills directory
cp -r aws-cost-operations ~/.claude/skills/

# Or create a symlink
ln -s /path/to/aws-cost-operations ~/.claude/skills/aws-cost-operations
```

### MCP Server Configuration

Configure the eight MCP servers in your Claude Code MCP settings:
- AWS Billing and Cost Management MCP
- AWS Pricing MCP
- AWS Cost Explorer MCP
- Amazon CloudWatch MCP
- Amazon CloudWatch Application Signals MCP
- AWS Managed Prometheus MCP
- AWS CloudTrail MCP
- AWS Well-Architected Security Assessment Tool MCP

Refer to [AWS MCP Servers documentation](https://awslabs.github.io/mcp/) for setup.

## Resources

### Included Files

- `SKILL.md` - Concise skill definition and core principles
- `README.md` - This comprehensive guide
- `references/operations-patterns.md` - Operational patterns and best practices
- `references/cloudwatch-alarms.md` - CloudWatch alarm configurations
- `CHANGELOG.md` - Version history
- `LICENSE` - MIT License

### External Resources

- [AWS Cost Optimization](https://aws.amazon.com/pricing/cost-optimization/)
- [AWS Well-Architected Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/)
- [AWS Well-Architected Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/)
- [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Managed Prometheus](https://aws.amazon.com/prometheus/)

## Contributing

This skill is part of the AISkills collection. For improvements:
1. Test with real AWS environments
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
