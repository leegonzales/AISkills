---
name: aws-cost-operations
description: This skill provides AWS cost optimization, monitoring, and operational best practices with integrated MCP servers for billing analysis, cost estimation, observability, and security assessment.
---

# AWS Cost & Operations

This skill provides comprehensive guidance for AWS cost optimization, monitoring, observability, and operational excellence with integrated MCP servers.

## Fidelity / Degraded Mode (no fabricated numbers)

**This skill is primarily a router to live AWS MCP servers. Billing and cost answers are decision-grade — a fabricated number here is materially harmful (wrong budget calls, wrong savings bets). The single most important rule in this skill:**

> **Every account-specific figure MUST come from an actual MCP/tool query you ran this session.** This includes any spend amount, cost, bill total, usage number (invocations, GB-seconds, requests, storage GB), savings/right-sizing estimate, forecast, budget-utilization percentage, or anomaly value.

**If the relevant MCP server is NOT available** (Billing, Cost Explorer, Pricing, CloudWatch, etc. — i.e. you have not actually called the tool this session and received a result):

- **You may NOT state a dollar figure, usage number, percentage, or any phrasing like "you're spending $X on Y", "Lambda is ~$N/month", "you could save about $Z."** Not as an estimate, not as an example, not "roughly," not "typically around." No invented numbers, ever — even to look helpful or complete.
- **Refuse and route to the data source.** Say plainly: *"I need the Billing / Cost Explorer / Pricing MCP server (or an exported Cost & Usage Report / CSV) to answer that with real numbers — here's how to get it: …"* Then state what's missing and how the user can provide it (enable the MCP server, attach a CUR export, paste Cost Explorer output).
- **Offer only GENERIC, clearly-labeled best-practice guidance** — e.g. "Generic guidance (not your account): Lambda cost is driven by invocations × (GB-seconds) plus request count; common levers are right-sizing memory, cutting duration, and Graviton/arm64." Label it explicitly as generic and structural, **never** present it as analysis of *this* account, and never let it collapse into a numbered listicle dressed up as findings.

**Self-check before sending any cost/usage answer:** "Did a tool call this session return this exact number?" If no → delete the number, name the missing data source, give labeled generic guidance only. A correct refusal beats a confident fabrication.

This gate applies equally to the Cost servers (Billing, Pricing, Cost Explorer) and to the monitoring/audit servers (CloudWatch metrics, Application Signals, Prometheus, CloudTrail) — utilization figures, error rates, and event counts are account-specific and follow the same rule.

## Server Routing — which server for which question

When a request involves money or usage, pick the server before answering. These three overlap; disambiguate as follows:

- **AWS Pricing MCP** → *forward-looking / hypothetical* cost of resources you don't have yet. List prices, "what would X cost," region/option comparison, pre-deployment TCO. No account access needed.
- **AWS Cost Explorer MCP** → *historical, analytical* questions about what you already spent. Trends over time, breakdown by service/region/tag, anomalies, forecasts, optimization/right-sizing recommendations. Use this for "analyze my spend on X last month."
- **AWS Billing and Cost Management MCP** → *current account state*: this/last bill total, invoices, budgets and budget-utilization, cost-allocation tag setup, consolidated/org billing. Use this for "what's my current bill / am I over budget."

Rule of thumb: **Pricing = future/hypothetical, Cost Explorer = past/analysis, Billing = now/invoices & budgets.** If none of these servers is available, do not answer with numbers — apply the Degraded Mode gate above.

## Integrated MCP Servers

This skill includes 8 MCP servers automatically configured with the plugin:

### Cost Management Servers

#### 1. AWS Billing and Cost Management MCP Server
**Purpose**: Real-time billing and cost management
- View current AWS spending and trends
- Analyze billing details across services
- Track budget utilization
- Monitor cost allocation tags
- Review consolidated billing for organizations

#### 2. AWS Pricing MCP Server
**Purpose**: Pre-deployment cost estimation and optimization
- Estimate costs before deploying resources
- Compare pricing across regions
- Calculate Total Cost of Ownership (TCO)
- Evaluate different service options for cost efficiency
- Get current pricing information for AWS services

#### 3. AWS Cost Explorer MCP Server
**Purpose**: Detailed cost analysis and reporting
- Analyze historical spending patterns
- Create custom cost reports
- Identify cost anomalies and trends
- Forecast future costs
- Analyze cost by service, region, or tag
- Generate cost optimization recommendations

### Monitoring & Observability Servers

#### 4. Amazon CloudWatch MCP Server
**Purpose**: Metrics, alarms, and logs analysis
- Query CloudWatch metrics and logs
- Create and manage CloudWatch alarms
- Analyze application performance metrics
- Troubleshoot operational issues
- Set up custom dashboards
- Monitor resource utilization

#### 5. Amazon CloudWatch Application Signals MCP Server
**Purpose**: Application monitoring and performance insights
- Monitor application health and performance
- Analyze service-level objectives (SLOs)
- Track application dependencies
- Identify performance bottlenecks
- Monitor service map and traces

#### 6. AWS Managed Prometheus MCP Server
**Purpose**: Prometheus-compatible monitoring
- Query Prometheus metrics
- Monitor containerized applications
- Analyze Kubernetes workload metrics
- Create PromQL queries
- Track custom application metrics

### Audit & Security Servers

#### 7. AWS CloudTrail MCP Server
**Purpose**: AWS API activity and audit analysis
- Analyze AWS API calls and user activity
- Track resource changes and modifications
- Investigate security incidents
- Audit compliance requirements
- Identify unusual access patterns
- Review who made what changes when

#### 8. AWS Well-Architected Security Assessment Tool MCP Server
**Purpose**: Security assessment against Well-Architected Framework
- Assess security posture against AWS best practices
- Identify security gaps and vulnerabilities
- Get security improvement recommendations
- Review security pillar compliance
- Generate security assessment reports

## When to Use This Skill

Use this skill when:
- Optimizing AWS costs and reducing spending
- Estimating costs before deployment
- Monitoring application and infrastructure performance
- Setting up observability and alerting
- Analyzing spending patterns and trends
- Investigating operational issues
- Auditing AWS activity and changes
- Assessing security posture
- Implementing operational excellence

## Cost Optimization Best Practices

### Pre-Deployment Cost Estimation

**Always estimate costs before deploying**:
1. Use **AWS Pricing MCP** to estimate resource costs
2. Compare pricing across different regions
3. Evaluate alternative service options
4. Calculate expected monthly costs
5. Plan for scaling and growth

**Example workflow**:
```
"Estimate the monthly cost of running a Lambda function with
1 million invocations, 512MB memory, 3-second duration in us-east-1"
```

### Cost Analysis and Optimization

**Regular cost reviews**:
1. Use **Cost Explorer MCP** to analyze spending trends
2. Identify cost anomalies and unexpected charges
3. Review costs by service, region, and environment
4. Compare actual vs. budgeted costs
5. Generate cost optimization recommendations

**Cost optimization strategies**:
- Right-size over-provisioned resources
- Use appropriate storage classes (S3, EBS)
- Implement auto-scaling for dynamic workloads
- Leverage Savings Plans and Reserved Instances
- Delete unused resources and snapshots
- Use cost allocation tags effectively

### Budget Monitoring

**Track spending against budgets**:
1. Use **Billing and Cost Management MCP** to monitor budgets
2. Set up budget alerts for threshold breaches
3. Review budget utilization regularly
4. Adjust budgets based on trends
5. Implement cost controls and governance

## Monitoring and Observability Best Practices

### CloudWatch Metrics and Alarms

**Implement comprehensive monitoring**:
1. Use **CloudWatch MCP** to query metrics and logs
2. Set up alarms for critical metrics:
   - CPU and memory utilization
   - Error rates and latency
   - Queue depths and processing times
   - API gateway throttling
   - Lambda errors and timeouts
3. Create CloudWatch dashboards for visualization
4. Use log insights for troubleshooting

**Example alarm scenarios**:
- Lambda error rate > 1%
- EC2 CPU utilization > 80%
- API Gateway 4xx/5xx error spike
- DynamoDB throttled requests
- ECS task failures

### Application Performance Monitoring

**Monitor application health**:
1. Use **CloudWatch Application Signals MCP** for APM
2. Track service-level objectives (SLOs)
3. Monitor application dependencies
4. Identify performance bottlenecks
5. Set up distributed tracing

### Container and Kubernetes Monitoring

**For containerized workloads**:
1. Use **AWS Managed Prometheus MCP** for metrics
2. Monitor container resource utilization
3. Track pod and node health
4. Create PromQL queries for custom metrics
5. Set up alerts for container anomalies

## Audit and Security Best Practices

### CloudTrail Activity Analysis

**Audit AWS activity**:
1. Use **CloudTrail MCP** to analyze API activity
2. Track who made changes to resources
3. Investigate security incidents
4. Monitor for suspicious activity patterns
5. Audit compliance with policies

**Common audit scenarios**:
- "Who deleted this S3 bucket?"
- "Show all IAM role changes in the last 24 hours"
- "List failed login attempts"
- "Find all actions by a specific user"
- "Track modifications to security groups"

### Security Assessment

**Regular security reviews**:
1. Use **Well-Architected Security Assessment MCP**
2. Assess security posture against best practices
3. Identify security gaps and vulnerabilities
4. Implement recommended security improvements
5. Document security compliance

**Security assessment areas**:
- Identity and Access Management (IAM)
- Detective controls and monitoring
- Infrastructure protection
- Data protection and encryption
- Incident response preparedness

## Using MCP Servers Effectively

### Cost Analysis Workflow

1. **Pre-deployment**: Use Pricing MCP to estimate costs
2. **Post-deployment**: Use Billing MCP to track actual spending
3. **Analysis**: Use Cost Explorer MCP for detailed cost analysis
4. **Optimization**: Implement recommendations from Cost Explorer

### Monitoring Workflow

1. **Setup**: Configure CloudWatch metrics and alarms
2. **Monitor**: Use CloudWatch MCP to track key metrics
3. **Analyze**: Use Application Signals for APM insights
4. **Troubleshoot**: Query CloudWatch Logs for issue resolution

### Security Workflow

1. **Audit**: Use CloudTrail MCP to review activity
2. **Assess**: Use Well-Architected Security Assessment
3. **Remediate**: Implement security recommendations
4. **Monitor**: Track security events via CloudWatch

### MCP Usage Best Practices

1. **Cost Awareness**: Check pricing before deploying resources
2. **Proactive Monitoring**: Set up alarms for critical metrics
3. **Regular Reviews**: Analyze costs and performance weekly
4. **Audit Trails**: Review CloudTrail logs for compliance
5. **Security First**: Run security assessments regularly
6. **Optimize Continuously**: Act on cost and performance recommendations

## Operational Excellence Guidelines

### Cost Optimization

- **Tag Everything**: Use consistent cost allocation tags
- **Review Monthly**: Analyze spending trends and anomalies
- **Right-size**: Match resources to actual usage
- **Automate**: Use auto-scaling and scheduling
- **Monitor Budgets**: Set alerts for cost overruns

### Monitoring and Alerting

- **Critical Metrics**: Alert on business-critical metrics
- **Noise Reduction**: Fine-tune thresholds to reduce false positives
- **Actionable Alerts**: Ensure alerts have clear remediation steps
- **Dashboard Visibility**: Create dashboards for key stakeholders
- **Log Retention**: Balance cost and compliance needs

### Security and Compliance

- **Least Privilege**: Grant minimum required permissions
- **Audit Regularly**: Review CloudTrail logs for anomalies
- **Encrypt Data**: Use encryption at rest and in transit
- **Assess Continuously**: Run security assessments frequently
- **Incident Response**: Have procedures for security events

## Additional Resources

For detailed operational patterns and best practices, refer to the comprehensive reference:

**File**: `references/operations-patterns.md`

This reference includes:
- Cost optimization strategies
- Monitoring and alerting patterns
- Observability best practices
- Security and compliance guidelines
- Troubleshooting workflows

## CloudWatch Alarms Reference

**File**: `references/cloudwatch-alarms.md`

Common alarm configurations for:
- Lambda functions
- EC2 instances
- RDS databases
- DynamoDB tables
- API Gateway
- ECS services
- Application Load Balancers
