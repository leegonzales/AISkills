# Gemini API Reference for Peer Review

Complete reference for Google Gemini API usage patterns relevant to peer review workflows.

---

## Overview

This reference provides API-level guidance for integrating Gemini models into peer review workflows. Unlike CLI-based tools, Gemini API integration requires programmatic implementation in Python or TypeScript/Node.js.

**Purpose:** Enable automated peer review through Gemini's powerful models with 1M+ token context windows

**Primary Use Cases:**
- Architecture review and validation
- Security vulnerability analysis
- Design decision evaluation
- Performance bottleneck identification
- Testing strategy assessment
- Code quality review

---

## API Basics

### Authentication Methods

#### Option 1: Gemini API Key (Recommended for Development)

**Obtain API Key:**
1. Visit Google AI Studio: https://aistudio.google.com/apikey
2. Create or select project
3. Generate API key

**Set Environment Variable:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Pros:**
- Simple setup
- Free tier: 100 requests/day
- No Google Cloud account required

**Cons:**
- Lower rate limits than Vertex AI
- Manual key management

---

#### Option 2: Vertex AI (Recommended for Production)

**Setup Application Default Credentials:**
```bash
# Set project and region
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"

# Authenticate
gcloud auth application-default login
```

**Service Account (Production):**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

**Pros:**
- Enterprise security
- Higher rate limits
- Pay-as-you-go scaling
- SLA guarantees

**Cons:**
- Requires Google Cloud account
- More complex setup

---

### Available Models

#### Gemini 2.5 Pro (`gemini-2.5-pro`)
- **Context:** 1,048,576 input tokens / 65,536 output tokens
- **Inputs:** Text, images, video, audio, PDF
- **Best For:** Complex reasoning, large codebases, multi-step analysis
- **Key Features:** Advanced reasoning, code execution, function calling
- **Use Case:** Deep architecture reviews, complex security analysis

#### Gemini 2.5 Flash (`gemini-2.5-flash`)
- **Context:** 1,048,576 input tokens / 65,536 output tokens
- **Inputs:** Text, images, video, audio
- **Best For:** Fast processing, high-throughput scenarios
- **Key Features:** Thinking mode, function calling, code execution
- **Use Case:** Quick code reviews, batch processing

#### Gemini 2.5 Flash-Lite (`gemini-2.5-flash-lite`)
- **Context:** 1,048,576 input tokens / 65,536 output tokens
- **Inputs:** Text, image, video, audio, PDF
- **Best For:** Cost-efficient high-volume processing
- **Key Features:** Function calling, code execution, structured outputs
- **Use Case:** Lightweight analysis, cost-sensitive applications

**Model Selection Guide:**
- **Pro:** Use for deep architectural analysis requiring complex reasoning
- **Flash:** Use for standard peer reviews requiring fast turnaround
- **Flash-Lite:** Use for simple checks or high-volume batch processing

---

### Rate Limits

#### Free Tier (API Key - Unpaid)
```
Rate Limits:
- 10 requests per minute
- 250 requests per day

Models:
- Flash models only
```

#### Free Tier (Google Account Login)
```
Rate Limits:
- 60 requests per minute
- 1,000 requests per day

Models:
- Gemini 2.5 Pro
- Gemini 2.5 Flash
```

#### Paid Tier (Pay-As-You-Go)
```
Billing:
- $1.25 per million input tokens
- $5.00 per million output tokens
- 64% reduction for cached tokens

Rate Limits:
- Variable by project quota
- Scale to production needs
```

**Cost Optimization Tips:**
- Use Flash for simple reviews (same context, lower cost)
- Cache common context (architecture docs, style guides)
- Batch similar requests
- Monitor token usage

---

## Core API Calls

### Basic Text Generation (Python)

```python
import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate response
prompt = """
Review this code for security vulnerabilities:

def authenticate_user(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return db.execute(query)
"""

response = model.generate_content(prompt)
print(response.text)
```

**Output:**
```
CRITICAL SECURITY VULNERABILITY: SQL Injection

The code is vulnerable to SQL injection attacks...
[detailed analysis]
```

---

### Basic Text Generation (TypeScript/Node.js)

```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";

// Initialize client
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY!);

// Get model
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

// Generate response
const prompt = `
Review this architecture for scalability issues:

[architecture description]
`;

const result = await model.generateContent(prompt);
const response = await result.response;
const text = response.text();

console.log(text);
```

---

### Multi-Turn Conversations (Python)

```python
import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.5-flash")

# Start chat session
chat = model.start_chat(history=[])

# First turn: Initial review
response1 = chat.send_message("""
Review this microservices architecture:

Services:
- API Gateway (Node.js)
- User Service (Python)
- Order Service (Go)
- PostgreSQL databases per service
""")
print("Turn 1:", response1.text)

# Second turn: Follow-up question
response2 = chat.send_message("""
What are the data consistency risks with this approach?
""")
print("Turn 2:", response2.text)

# Third turn: Design alternative
response3 = chat.send_message("""
Propose an alternative that reduces consistency risks.
""")
print("Turn 3:", response3.text)
```

**Use Case:** Iterative architecture refinement with context preservation

---

### With Images/Files (Python)

```python
import google.generativeai as genai
from pathlib import Path

model = genai.GenerativeModel("gemini-2.5-pro")

# Upload architecture diagram
architecture_diagram = genai.upload_file(
    path="architecture-diagram.png",
    display_name="System Architecture"
)

# Wait for processing
import time
while architecture_diagram.state.name == "PROCESSING":
    time.sleep(1)
    architecture_diagram = genai.get_file(architecture_diagram.name)

# Review with image context
prompt = """
Analyze this architecture diagram.

Context:
- E-commerce platform
- 100K daily active users
- High availability requirements

Questions:
1. Single points of failure?
2. Scalability bottlenecks?
3. Data consistency issues?

Expected Output: Risk assessment with severity levels
"""

response = model.generate_content([architecture_diagram, prompt])
print(response.text)

# Clean up
genai.delete_file(architecture_diagram.name)
```

---

### With PDF Documents (Python)

```python
import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.5-pro")

# Upload design document
design_doc = genai.upload_file(
    path="system-design-doc.pdf",
    display_name="System Design"
)

# Wait for processing
import time
while design_doc.state.name == "PROCESSING":
    time.sleep(2)
    design_doc = genai.get_file(design_doc.name)

# Review design document
prompt = """
Review this system design document.

Focus areas:
- Architectural soundness
- Security considerations
- Scalability concerns
- Operational complexity

Expected Output: Structured review with recommendations
"""

response = model.generate_content([design_doc, prompt])
print(response.text)

# Clean up
genai.delete_file(design_doc.name)
```

---

## Key Parameters

### temperature

**Type:** Float (0.0 to 2.0)
**Default:** 1.0

**Description:** Controls randomness in responses

**Usage:**
```python
generation_config = {
    "temperature": 0.2,  # Low temperature for consistent, focused analysis
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)
```

**Recommended for Peer Review:**
- `0.1-0.3`: Security reviews, compliance checks (maximum consistency)
- `0.4-0.6`: Architecture reviews, design decisions (balanced)
- `0.7-1.0`: Creative solutions, alternative approaches (more variation)

---

### top_p (Nucleus Sampling)

**Type:** Float (0.0 to 1.0)
**Default:** 0.95

**Description:** Cumulative probability threshold for token selection

**Usage:**
```python
generation_config = {
    "top_p": 0.8,  # More focused token selection
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)
```

**Recommended for Peer Review:**
- `0.8-0.9`: Focused, high-confidence analysis
- `0.95-1.0`: Allow broader vocabulary and phrasing

---

### top_k

**Type:** Integer
**Default:** 40

**Description:** Limit token selection to top k most likely tokens

**Usage:**
```python
generation_config = {
    "top_k": 20,  # More deterministic responses
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)
```

**Recommended for Peer Review:**
- `20-30`: Highly consistent technical analysis
- `40-60`: Balance between consistency and natural language

---

### max_output_tokens

**Type:** Integer
**Default:** 8192
**Maximum:** 65,536 (for 2.5 series)

**Description:** Maximum length of generated response

**Usage:**
```python
generation_config = {
    "max_output_tokens": 4096,  # Moderate-length review
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)
```

**Recommended for Peer Review:**
- `2048-4096`: Quick reviews, focused analysis
- `4096-8192`: Comprehensive reviews
- `8192+`: Deep architectural analysis, detailed reports

---

### safety_settings

**Type:** Dictionary of safety categories and thresholds

**Description:** Content filtering controls

**Usage:**
```python
from google.generativeai.types import HarmCategory, HarmBlockThreshold

safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    safety_settings=safety_settings
)
```

**Recommended for Peer Review:**
- Generally use `BLOCK_NONE` to avoid false positives on technical content
- Code and security discussions may trigger filters inappropriately

---

### response_mime_type (Structured Outputs)

**Type:** String
**Options:** `"text/plain"`, `"application/json"`

**Description:** Force structured JSON responses

**Usage:**
```python
import json

generation_config = {
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)

prompt = """
Review this architecture and return JSON:

{
  "risk_level": "HIGH|MEDIUM|LOW",
  "concerns": ["concern1", "concern2"],
  "recommendations": ["rec1", "rec2"]
}

Architecture: [description]
"""

response = model.generate_content(prompt)
result = json.loads(response.text)
print(f"Risk: {result['risk_level']}")
```

**Recommended for Peer Review:**
- Structured reports for automation
- CI/CD integration
- Programmatic decision-making

---

### system_instruction

**Type:** String

**Description:** Persistent instructions for the model (role/behavior)

**Usage:**
```python
system_instruction = """
You are a senior software architect conducting peer reviews.

Your analysis should:
- Prioritize security, scalability, and maintainability
- Provide specific, actionable recommendations
- Highlight trade-offs explicitly
- Use risk levels: CRITICAL, HIGH, MEDIUM, LOW
- Be concise but thorough

Always structure feedback with:
1. Summary
2. Key concerns (with severity)
3. Recommendations (prioritized)
"""

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=system_instruction
)

response = model.generate_content("Review this architecture: [content]")
```

**Recommended for Peer Review:**
- Set consistent review standards
- Define expected output format
- Establish expertise level and perspective

---

## API Patterns for Peer Review

### Pattern 1: Architecture Review

```python
import google.generativeai as genai
import os

def review_architecture(architecture_description: str, context: dict) -> dict:
    """
    Comprehensive architecture review with structured output.

    Args:
        architecture_description: Textual description or codex.md content
        context: Dict with scale, constraints, requirements

    Returns:
        Structured review with risk assessment
    """
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    system_instruction = """
    You are a senior software architect specializing in distributed systems.

    Review approach:
    - Assess scalability, security, reliability, operational complexity
    - Identify single points of failure
    - Evaluate technology choices
    - Consider team capabilities and constraints

    Output format:
    1. Risk Level: CRITICAL/HIGH/MEDIUM/LOW
    2. Key Concerns (with severity)
    3. Recommendations (prioritized by impact)
    4. Trade-offs to consider
    """

    generation_config = {
        "temperature": 0.3,  # Consistent, focused analysis
        "top_p": 0.8,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        "gemini-2.5-pro",  # Use Pro for complex reasoning
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    prompt = f"""
    [ARCHITECTURE REVIEW]

    System: {context.get('system_name', 'N/A')}
    Scale: {context.get('scale', 'N/A')}
    Users: {context.get('users', 'N/A')}
    Constraints: {context.get('constraints', 'None specified')}

    Architecture:
    {architecture_description}

    Focus Areas:
    - Service boundaries and dependencies
    - Data consistency approach
    - Scalability bottlenecks
    - Security boundaries
    - Operational complexity
    - Failure modes

    Provide comprehensive review with risk assessment.
    """

    response = model.generate_content(prompt)

    return {
        "review": response.text,
        "model": "gemini-2.5-pro",
        "timestamp": datetime.now().isoformat(),
        "context": context
    }


# Usage
context = {
    "system_name": "Multi-tenant SaaS Platform",
    "scale": "100-500 tenants",
    "users": "50-5K users per tenant",
    "constraints": "Strict tenant data isolation required"
}

architecture = """
Microservices architecture:
- API Gateway (Node.js) - public entry point
- Auth Service (Python) - JWT-based authentication
- Tenant Service (Go) - tenant management
- App Service (Node.js) - core business logic
- PostgreSQL with row-level security per service
- Redis for session storage
- BullMQ for background jobs
"""

review_result = review_architecture(architecture, context)
print(review_result["review"])
```

---

### Pattern 2: Security Review

```python
import google.generativeai as genai
from typing import List, Dict

def security_review(code: str, threat_model: List[str]) -> Dict:
    """
    Security-focused code review.

    Args:
        code: Source code to review
        threat_model: List of threats to check (e.g., ["SQL Injection", "XSS"])

    Returns:
        Structured vulnerability assessment
    """
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    system_instruction = """
    You are a security engineer conducting code security reviews.

    Analysis approach:
    - Identify vulnerabilities with OWASP classification
    - Assess severity: CRITICAL, HIGH, MEDIUM, LOW
    - Provide specific remediation steps
    - Include code examples for fixes

    Output structure:
    1. Vulnerability Summary (count by severity)
    2. Detailed Findings (CRITICAL first)
    3. Remediation Steps (prioritized)
    4. Security Best Practices Recommendations
    """

    generation_config = {
        "temperature": 0.1,  # Maximum consistency for security
        "top_p": 0.8,
        "max_output_tokens": 8192,
    }

    # Block none for technical content
    from google.generativeai.types import HarmCategory, HarmBlockThreshold
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    model = genai.GenerativeModel(
        "gemini-2.5-pro",
        generation_config=generation_config,
        system_instruction=system_instruction,
        safety_settings=safety_settings
    )

    prompt = f"""
    [SECURITY REVIEW]

    Threat Model:
    {chr(10).join(f"- {threat}" for threat in threat_model)}

    Code to Review:
    ```
    {code}
    ```

    Identify all security vulnerabilities with:
    - OWASP classification
    - Severity level (CRITICAL/HIGH/MEDIUM/LOW)
    - Exploit scenario
    - Remediation steps with code examples

    Prioritize findings by severity and exploitability.
    """

    response = model.generate_content(prompt)

    return {
        "vulnerabilities": response.text,
        "threat_model": threat_model,
        "model": "gemini-2.5-pro"
    }


# Usage
code_sample = """
def login(request):
    username = request.POST['username']
    password = request.POST['password']

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db.execute(query)

    if result:
        session['user_id'] = result['id']
        return redirect('/dashboard')
    else:
        return render('login.html', error="Invalid credentials")
"""

threat_model = [
    "SQL Injection",
    "Session Fixation",
    "Weak Password Storage",
    "Timing Attacks"
]

security_results = security_review(code_sample, threat_model)
print(security_results["vulnerabilities"])
```

---

### Pattern 3: Performance Analysis

```python
import google.generativeai as genai

def performance_analysis(
    code: str,
    current_metrics: dict,
    target_metrics: dict,
    context: str
) -> dict:
    """
    Performance bottleneck identification and optimization.

    Args:
        code: Source code or file reference
        current_metrics: Current performance (e.g., {"latency_p99": "2s"})
        target_metrics: Target performance (e.g., {"latency_p99": "300ms"})
        context: Additional context (load, constraints)

    Returns:
        Optimization recommendations prioritized by impact
    """
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    system_instruction = """
    You are a performance engineering expert.

    Analysis approach:
    - Identify bottlenecks (database, network, CPU, memory)
    - Estimate optimization impact (effort vs. performance gain)
    - Consider trade-offs (complexity, maintainability)
    - Provide specific code improvements

    Output structure:
    1. Bottleneck Analysis (prioritized)
    2. Optimization Recommendations (impact/effort matrix)
    3. Implementation Examples
    4. Measurement Strategy
    """

    generation_config = {
        "temperature": 0.4,
        "top_p": 0.85,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        "gemini-2.5-flash",  # Flash sufficient for performance analysis
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    prompt = f"""
    [PERFORMANCE ANALYSIS]

    Current Performance:
    {chr(10).join(f"- {k}: {v}" for k, v in current_metrics.items())}

    Target Performance:
    {chr(10).join(f"- {k}: {v}" for k, v in target_metrics.items())}

    Context: {context}

    Code:
    ```
    {code}
    ```

    Identify performance bottlenecks and provide optimization recommendations.

    For each optimization:
    - Bottleneck identified
    - Expected performance improvement
    - Implementation effort (LOW/MEDIUM/HIGH)
    - Code example
    - Potential trade-offs

    Prioritize by impact/effort ratio.
    """

    response = model.generate_content(prompt)

    return {
        "analysis": response.text,
        "current_metrics": current_metrics,
        "target_metrics": target_metrics,
        "model": "gemini-2.5-flash"
    }


# Usage
slow_code = """
def get_user_orders(user_id):
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)
    orders = []

    for order_id in user['order_ids']:
        order = db.query("SELECT * FROM orders WHERE id = ?", order_id)

        # Get order items
        items = []
        for item_id in order['item_ids']:
            item = db.query("SELECT * FROM items WHERE id = ?", item_id)
            items.append(item)

        order['items'] = items
        orders.append(order)

    return orders
"""

perf_results = performance_analysis(
    code=slow_code,
    current_metrics={
        "latency_avg": "500ms",
        "latency_p99": "2s",
        "throughput": "100 req/s"
    },
    target_metrics={
        "latency_avg": "100ms",
        "latency_p99": "300ms",
        "throughput": "500 req/s"
    },
    context="1000 concurrent users, average 5 orders per user"
)

print(perf_results["analysis"])
```

---

### Pattern 4: Design Decision Evaluation

```python
import google.generativeai as genai
from typing import List, Dict

def evaluate_design_options(
    decision: str,
    options: List[Dict[str, any]],
    criteria: List[str],
    context: str
) -> dict:
    """
    Compare design alternatives with structured evaluation.

    Args:
        decision: Decision being made
        options: List of options with pros/cons
        criteria: Evaluation criteria (prioritized)
        context: System context and constraints

    Returns:
        Comparative analysis with recommendation
    """
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    system_instruction = """
    You are a technical architect evaluating design decisions.

    Evaluation approach:
    - Score each option against criteria
    - Consider short-term vs. long-term implications
    - Assess risk and complexity
    - Provide clear recommendation with rationale

    Output structure:
    1. Option Comparison Matrix
    2. Criterion-by-Criterion Analysis
    3. Recommendation with Rationale
    4. Implementation Considerations
    5. Decision Risks (what could go wrong)
    """

    generation_config = {
        "temperature": 0.5,  # Balanced for comparative analysis
        "top_p": 0.85,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        "gemini-2.5-pro",
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    options_formatted = "\n\n".join([
        f"Option {i+1}: {opt['name']}\n"
        f"Pros: {', '.join(opt['pros'])}\n"
        f"Cons: {', '.join(opt['cons'])}"
        for i, opt in enumerate(options)
    ])

    criteria_formatted = "\n".join([
        f"{i+1}. {criterion}" for i, criterion in enumerate(criteria)
    ])

    prompt = f"""
    [DESIGN DECISION EVALUATION]

    Decision: {decision}

    Options:
    {options_formatted}

    Evaluation Criteria (in priority order):
    {criteria_formatted}

    Context:
    {context}

    Provide comprehensive comparison and recommendation.

    For each option, score against criteria and explain trade-offs.
    Recommend the best option with clear rationale.
    Identify key risks and mitigation strategies.
    """

    response = model.generate_content(prompt)

    return {
        "evaluation": response.text,
        "decision": decision,
        "options_count": len(options),
        "model": "gemini-2.5-pro"
    }


# Usage
decision = "Caching strategy for product catalog"

options = [
    {
        "name": "Redis with TTL-based invalidation",
        "pros": ["Fast", "Simple", "Horizontally scalable"],
        "cons": ["Stale data risk", "Invalidation complexity"]
    },
    {
        "name": "Event-driven cache invalidation",
        "pros": ["Always fresh data", "Precise control"],
        "cons": ["Complex implementation", "Event overhead"]
    },
    {
        "name": "Hybrid (Redis + event invalidation)",
        "pros": ["Fast + fresh", "Best of both worlds"],
        "cons": ["Most complex", "Higher operational overhead"]
    }
]

criteria = [
    "Data freshness",
    "Query performance",
    "Implementation complexity",
    "Operational overhead",
    "Team familiarity"
]

context = """
- 10K product SKUs
- Updates 100x/day
- Read-heavy (1M reads/day)
- Team familiar with Redis, less with event streaming
- Must support real-time inventory updates
"""

decision_results = evaluate_design_options(decision, options, criteria, context)
print(decision_results["evaluation"])
```

---

### Pattern 5: Testing Strategy Review

```python
import google.generativeai as genai

def review_testing_strategy(
    module: str,
    current_coverage: str,
    test_types: List[str],
    sample_tests: str,
    concerns: List[str]
) -> dict:
    """
    Evaluate testing strategy and suggest improvements.

    Args:
        module: Module or component being tested
        current_coverage: Current test coverage percentage
        test_types: Types of tests currently implemented
        sample_tests: Sample test code
        concerns: Known testing concerns or gaps

    Returns:
        Testing improvement recommendations
    """
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    system_instruction = """
    You are a QA engineering expert specializing in test strategy.

    Review approach:
    - Assess test coverage adequacy
    - Identify missing test scenarios
    - Evaluate test quality (brittleness, maintainability)
    - Recommend test types and priorities

    Output structure:
    1. Coverage Assessment
    2. Missing Test Scenarios (prioritized)
    3. Test Quality Issues
    4. Recommended Improvements (with examples)
    5. Testing Best Practices
    """

    generation_config = {
        "temperature": 0.4,
        "top_p": 0.85,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    prompt = f"""
    [TESTING STRATEGY REVIEW]

    Module: {module}
    Current Coverage: {current_coverage}
    Test Types: {', '.join(test_types)}

    Sample Tests:
    ```
    {sample_tests}
    ```

    Known Concerns:
    {chr(10).join(f"- {concern}" for concern in concerns)}

    Review testing strategy and recommend improvements.

    Focus on:
    - Missing edge cases
    - Test type gaps (unit, integration, e2e)
    - Test quality and maintainability
    - Coverage priorities

    Provide specific test examples for key improvements.
    """

    response = model.generate_content(prompt)

    return {
        "review": response.text,
        "module": module,
        "current_coverage": current_coverage,
        "model": "gemini-2.5-flash"
    }


# Usage
sample_tests = """
describe('UserAuth', () => {
  it('should authenticate valid user', async () => {
    const result = await authenticateUser('test@example.com', 'password123');
    expect(result.success).toBe(true);
  });

  it('should reject invalid password', async () => {
    const result = await authenticateUser('test@example.com', 'wrongpass');
    expect(result.success).toBe(false);
  });
});
"""

testing_results = review_testing_strategy(
    module="User Authentication Service",
    current_coverage="60%",
    test_types=["Unit tests"],
    sample_tests=sample_tests,
    concerns=[
        "Missing edge cases (password reset, token expiration)",
        "No integration tests for full auth flow",
        "Brittle mocks for JWT validation",
        "No security testing (brute force, timing attacks)"
    ]
)

print(testing_results["review"])
```

---

### Pattern 6: Code Review

```python
import google.generativeai as genai

def code_review(
    code: str,
    language: str,
    focus_areas: List[str],
    style_guide: str = None
) -> dict:
    """
    General code review for quality, style, and best practices.

    Args:
        code: Source code to review
        language: Programming language
        focus_areas: Specific areas to focus on
        style_guide: Optional style guide reference

    Returns:
        Code review findings and suggestions
    """
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    system_instruction = f"""
    You are a senior {language} developer conducting code review.

    Review approach:
    - Assess code quality, readability, maintainability
    - Check adherence to {language} best practices
    - Identify potential bugs and edge cases
    - Suggest refactoring opportunities

    Output structure:
    1. Summary (overall quality assessment)
    2. Issues (categorized: CRITICAL, MAJOR, MINOR)
    3. Suggestions (with code examples)
    4. Positive Observations
    """

    generation_config = {
        "temperature": 0.3,
        "top_p": 0.85,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    style_context = f"\n\nStyle Guide:\n{style_guide}" if style_guide else ""

    prompt = f"""
    [CODE REVIEW - {language}]

    Focus Areas:
    {chr(10).join(f"- {area}" for area in focus_areas)}
    {style_context}

    Code:
    ```{language.lower()}
    {code}
    ```

    Provide comprehensive code review covering focus areas.

    For each issue:
    - Severity (CRITICAL/MAJOR/MINOR)
    - Description
    - Suggested fix with code example

    Also highlight what the code does well.
    """

    response = model.generate_content(prompt)

    return {
        "review": response.text,
        "language": language,
        "focus_areas": focus_areas,
        "model": "gemini-2.5-flash"
    }


# Usage
code_sample = """
async function getUserData(userId) {
  const user = await db.query(`SELECT * FROM users WHERE id = ${userId}`);
  const orders = await db.query(`SELECT * FROM orders WHERE user_id = ${userId}`);

  return {
    ...user,
    orders: orders
  };
}
"""

code_review_results = code_review(
    code=code_sample,
    language="JavaScript",
    focus_areas=[
        "Security vulnerabilities",
        "Performance",
        "Error handling",
        "Code style"
    ],
    style_guide="Use async/await, avoid SQL injection, handle errors explicitly"
)

print(code_review_results["review"])
```

---

## Error Handling Strategies

### Common Errors

#### Invalid API Key
```python
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("Test prompt")
except Exception as e:
    if "API key not valid" in str(e):
        print("Error: Invalid API key. Check GEMINI_API_KEY environment variable.")
    else:
        raise
```

---

#### Rate Limit Exceeded
```python
import time
from google.api_core.exceptions import ResourceExhausted

def generate_with_retry(model, prompt, max_retries=3):
    """Generate content with exponential backoff retry."""
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"Rate limit hit. Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            else:
                print("Rate limit exceeded after retries. Upgrade plan or wait.")
                raise

# Usage
model = genai.GenerativeModel("gemini-2.5-flash")
result = generate_with_retry(model, "Review this architecture: [content]")
```

---

#### Content Safety Block
```python
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Disable safety filters for technical content
safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    safety_settings=safety_settings
)

try:
    response = model.generate_content(prompt)
except Exception as e:
    if "blocked" in str(e).lower():
        print("Content was blocked by safety filters despite settings.")
        print("Try rephrasing the prompt or use different model.")
    else:
        raise
```

---

#### File Processing Timeout
```python
import time

def upload_file_with_wait(file_path: str, max_wait: int = 60):
    """Upload file and wait for processing with timeout."""
    uploaded_file = genai.upload_file(path=file_path)

    start_time = time.time()
    while uploaded_file.state.name == "PROCESSING":
        if time.time() - start_time > max_wait:
            genai.delete_file(uploaded_file.name)
            raise TimeoutError(f"File processing exceeded {max_wait}s timeout")

        time.sleep(2)
        uploaded_file = genai.get_file(uploaded_file.name)

    if uploaded_file.state.name == "FAILED":
        raise ValueError(f"File processing failed: {uploaded_file.state}")

    return uploaded_file

# Usage
try:
    diagram = upload_file_with_wait("large-diagram.png", max_wait=120)
    # Use diagram...
finally:
    genai.delete_file(diagram.name)
```

---

## Best Practices

### 1. When to Use Which Model

**Use Gemini 2.5 Pro when:**
- Complex architectural analysis requiring deep reasoning
- Multi-step evaluation with trade-offs
- Large codebase comprehension (utilize 1M context)
- Critical security reviews
- Detailed design decision evaluation

**Use Gemini 2.5 Flash when:**
- Standard code reviews
- Performance analysis
- Testing strategy review
- Quick architectural assessments
- High-throughput batch processing

**Use Gemini 2.5 Flash-Lite when:**
- Simple code quality checks
- Linting-style reviews
- High-volume automated reviews
- Cost-sensitive applications

---

### 2. Context Management

**Provide Structured Context:**
```python
prompt = f"""
[REVIEW TYPE]

Context:
- System: {system_name}
- Scale: {scale}
- Constraints: {constraints}

[CONTENT TO REVIEW]

Focus Areas:
- Area 1
- Area 2

Expected Output: [format description]
"""
```

**Use System Instructions for Consistency:**
```python
system_instruction = """
You are a [role] conducting [type] reviews.

Your analysis should:
- Point 1
- Point 2
- Point 3
"""

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=system_instruction
)
```

---

### 3. Token Optimization

**Monitor Token Usage:**
```python
response = model.generate_content(prompt)

# Access usage metadata
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Total tokens: {response.usage_metadata.total_token_count}")
```

**Use Context Caching (For Repeated Context):**
```python
# Cache common context (architecture docs, style guides)
# Reduces token costs by 64% for cached portions
# Note: Caching API varies by SDK version - check docs

# General approach: Include static context early in prompt
# Gemini automatically caches frequently-used content
```

**Batch Similar Requests:**
```python
import asyncio

async def batch_review(files: List[str]) -> List[dict]:
    """Review multiple files in parallel."""
    model = genai.GenerativeModel("gemini-2.5-flash")

    async def review_file(file_path: str):
        with open(file_path, 'r') as f:
            code = f.read()

        response = model.generate_content(f"Review this code:\n\n{code}")
        return {"file": file_path, "review": response.text}

    tasks = [review_file(f) for f in files]
    return await asyncio.gather(*tasks)

# Usage
results = asyncio.run(batch_review(["file1.py", "file2.py", "file3.py"]))
```

---

### 4. Response Parsing

**Structured JSON Output:**
```python
generation_config = {
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)

prompt = """
Review this code and return JSON:

{
  "risk_level": "HIGH|MEDIUM|LOW",
  "issues": [
    {
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "description": "...",
      "line": 10,
      "fix": "..."
    }
  ],
  "recommendations": ["..."]
}

Code: [code here]
"""

response = model.generate_content(prompt)
result = json.loads(response.text)

# Access structured data
print(f"Risk: {result['risk_level']}")
for issue in result['issues']:
    print(f"{issue['severity']}: {issue['description']}")
```

**Text Parsing with Regex:**
```python
import re

response = model.generate_content("Review architecture...")
text = response.text

# Extract risk level
risk_match = re.search(r'Risk Level:\s*(CRITICAL|HIGH|MEDIUM|LOW)', text)
if risk_match:
    risk_level = risk_match.group(1)

# Extract numbered recommendations
recommendations = re.findall(r'\d+\.\s*(.+)', text)
```

---

## Integration Examples

### Python Integration

**Complete Review Script:**
```python
#!/usr/bin/env python3
"""
Architecture review automation script using Gemini API.
"""

import google.generativeai as genai
import os
import sys
import json
from pathlib import Path

def load_architecture(file_path: str) -> str:
    """Load architecture description from file."""
    return Path(file_path).read_text()

def review_architecture(arch_content: str) -> dict:
    """Perform architecture review."""
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    system_instruction = """
    You are a senior software architect conducting peer reviews.
    Provide structured, actionable feedback focusing on:
    - Scalability
    - Security
    - Maintainability
    - Operational complexity
    """

    generation_config = {
        "temperature": 0.3,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        "gemini-2.5-pro",
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    prompt = f"""
    Review this architecture and return JSON:

    {{
      "risk_level": "CRITICAL|HIGH|MEDIUM|LOW",
      "concerns": [
        {{
          "severity": "CRITICAL|HIGH|MEDIUM|LOW",
          "category": "scalability|security|maintainability|operations",
          "description": "...",
          "impact": "..."
        }}
      ],
      "recommendations": [
        {{
          "priority": 1,
          "description": "...",
          "rationale": "..."
        }}
      ]
    }}

    Architecture:
    {arch_content}
    """

    response = model.generate_content(prompt)
    return json.loads(response.text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python review.py <architecture-file>")
        sys.exit(1)

    arch_file = sys.argv[1]
    arch_content = load_architecture(arch_file)

    print(f"Reviewing {arch_file}...")
    result = review_architecture(arch_content)

    print(f"\nRisk Level: {result['risk_level']}\n")

    if result['concerns']:
        print("Concerns:")
        for concern in result['concerns']:
            print(f"  [{concern['severity']}] {concern['category']}: {concern['description']}")
        print()

    if result['recommendations']:
        print("Recommendations:")
        for rec in result['recommendations']:
            print(f"  {rec['priority']}. {rec['description']}")
            print(f"     Rationale: {rec['rationale']}")
        print()

    # Exit with error code if HIGH or CRITICAL risk
    if result['risk_level'] in ['HIGH', 'CRITICAL']:
        sys.exit(1)

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
export GEMINI_API_KEY="your-api-key"
python review.py architecture.md
```

---

### TypeScript/Node.js Integration

**Complete Review Module:**
```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";
import * as fs from "fs";

interface ReviewResult {
  riskLevel: "CRITICAL" | "HIGH" | "MEDIUM" | "LOW";
  concerns: Array<{
    severity: string;
    category: string;
    description: string;
    impact: string;
  }>;
  recommendations: Array<{
    priority: number;
    description: string;
    rationale: string;
  }>;
}

class ArchitectureReviewer {
  private genAI: GoogleGenerativeAI;
  private model: any;

  constructor(apiKey: string) {
    this.genAI = new GoogleGenerativeAI(apiKey);

    this.model = this.genAI.getGenerativeModel({
      model: "gemini-2.5-pro",
      generationConfig: {
        temperature: 0.3,
        maxOutputTokens: 8192,
        responseMimeType: "application/json",
      },
      systemInstruction: `
        You are a senior software architect conducting peer reviews.
        Provide structured, actionable feedback focusing on:
        - Scalability
        - Security
        - Maintainability
        - Operational complexity
      `,
    });
  }

  async reviewArchitecture(archContent: string): Promise<ReviewResult> {
    const prompt = `
      Review this architecture and return JSON:

      {
        "riskLevel": "CRITICAL|HIGH|MEDIUM|LOW",
        "concerns": [
          {
            "severity": "CRITICAL|HIGH|MEDIUM|LOW",
            "category": "scalability|security|maintainability|operations",
            "description": "...",
            "impact": "..."
          }
        ],
        "recommendations": [
          {
            "priority": 1,
            "description": "...",
            "rationale": "..."
          }
        ]
      }

      Architecture:
      ${archContent}
    `;

    const result = await this.model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();

    return JSON.parse(text) as ReviewResult;
  }

  async reviewFile(filePath: string): Promise<ReviewResult> {
    const content = fs.readFileSync(filePath, "utf-8");
    return this.reviewArchitecture(content);
  }
}

// Usage
async function main() {
  const apiKey = process.env.GEMINI_API_KEY!;
  const reviewer = new ArchitectureReviewer(apiKey);

  const archFile = process.argv[2];
  if (!archFile) {
    console.error("Usage: node review.js <architecture-file>");
    process.exit(1);
  }

  console.log(`Reviewing ${archFile}...`);
  const result = await reviewer.reviewFile(archFile);

  console.log(`\nRisk Level: ${result.riskLevel}\n`);

  if (result.concerns.length > 0) {
    console.log("Concerns:");
    result.concerns.forEach((concern) => {
      console.log(`  [${concern.severity}] ${concern.category}: ${concern.description}`);
    });
    console.log();
  }

  if (result.recommendations.length > 0) {
    console.log("Recommendations:");
    result.recommendations.forEach((rec) => {
      console.log(`  ${rec.priority}. ${rec.description}`);
      console.log(`     Rationale: ${rec.rationale}`);
    });
    console.log();
  }

  // Exit with error if HIGH or CRITICAL risk
  if (["HIGH", "CRITICAL"].includes(result.riskLevel)) {
    process.exit(1);
  }
}

main().catch(console.error);
```

**Usage:**
```bash
export GEMINI_API_KEY="your-api-key"
npx ts-node review.ts architecture.md
```

---

### Environment Variable Management

**Development (.env file):**
```bash
# .env
GEMINI_API_KEY=your-api-key-here
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

**Load with Python:**
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ["GEMINI_API_KEY"]
```

**Load with Node.js:**
```typescript
import * as dotenv from "dotenv";
dotenv.config();

const apiKey = process.env.GEMINI_API_KEY!;
```

**Production (Environment Variables):**
```bash
# Set in deployment environment
export GEMINI_API_KEY="production-key"

# Or use cloud secret managers
# AWS Secrets Manager, GCP Secret Manager, Azure Key Vault
```

---

## Quick Reference

### API Call Patterns

| Use Case | Model | Temperature | Max Tokens | Safety |
|----------|-------|-------------|------------|--------|
| Architecture Review | Pro | 0.3 | 8192 | BLOCK_NONE |
| Security Review | Pro | 0.1 | 8192 | BLOCK_NONE |
| Performance Analysis | Flash | 0.4 | 8192 | Default |
| Design Evaluation | Pro | 0.5 | 8192 | Default |
| Testing Strategy | Flash | 0.4 | 8192 | Default |
| Code Review | Flash | 0.3 | 8192 | BLOCK_NONE |

---

### Python Boilerplate

```python
import google.generativeai as genai
import os

# Configure
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create model
generation_config = {
    "temperature": 0.3,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)

# Generate
response = model.generate_content("Your prompt here")
print(response.text)
```

---

### TypeScript Boilerplate

```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";

// Initialize
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY!);

// Create model
const model = genAI.getGenerativeModel({
  model: "gemini-2.5-flash",
  generationConfig: {
    temperature: 0.3,
    maxOutputTokens: 8192,
  },
});

// Generate
const result = await model.generateContent("Your prompt here");
const response = await result.response;
console.log(response.text());
```

---

This API reference provides comprehensive guidance for integrating Gemini models into peer review workflows using Python and TypeScript/Node.js.
