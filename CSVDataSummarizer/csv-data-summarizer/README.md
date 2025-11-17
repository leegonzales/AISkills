# CSV Data Summarizer

**A proactive Claude skill that automatically analyzes CSV files and generates comprehensive insights with visualizations - no questions asked.**

**Score: 93/100** | **Category: Data Analysis** | **Pattern: Proactive/Automatic**

---

## Overview

The CSV Data Summarizer is an exemplary skill that demonstrates the "DO NOT ASK" proactive design pattern. When you provide a CSV file, it immediately executes a comprehensive analysis without asking what you want - it intelligently adapts to your data type and delivers complete insights in one response.

This skill is valuable for two reasons:
1. **Functionality**: Fast, comprehensive CSV analysis with visualizations
2. **Design Reference**: Exemplary pattern for proactive AI behavior (see `references/proactive-design-principles.md`)

## Key Features

- **Fully Automatic** - No prompting needed, just upload CSV and get complete analysis
- **Intelligent Adaptation** - Detects data type (sales, financial, customer, etc.) and applies relevant analyses
- **Comprehensive Output** - Statistics, distributions, correlations, time-series, and quality checks
- **Smart Visualizations** - Generates 3-5 charts based on what's actually in your data
- **No Decision Paralysis** - Eliminates "What would you like to do?" friction
- **Quality Checks** - Automatically identifies missing data and data type issues
- **Multi-Industry Support** - Adapts to e-commerce, finance, healthcare, operations, surveys, etc.

## The "DO NOT ASK" Pattern

Most AI assistants default to asking questions:
> "What would you like me to do with this data?"
> "Here are some options: 1) Summary, 2) Visualization, 3) Trends..."

This creates decision paralysis and delays value.

This skill does the opposite:
> "I'll analyze this data comprehensively right now."
> [Immediately shows complete analysis with all visualizations]

The result: **Instant "wow" factor** from thoroughness and decisiveness.

See `references/proactive-design-principles.md` for a detailed extraction of how this pattern works and how to apply it to other skills.

## When to Use

Use this skill whenever you need to:
- Quickly understand what's in a CSV file
- Explore data structure and quality
- Generate summary statistics and distributions
- Identify trends and patterns in tabular data
- Create visualizations for reporting
- Perform initial exploratory data analysis (EDA)
- Check data quality before further processing

## How It Works

### 1. Intelligent Data Detection

The skill first inspects your CSV to understand what type of data it is:

```python
# Detects:
- Column types (numeric, categorical, date/time)
- Data domains (sales, financial, customer, operational)
- Relevant analyses for this specific dataset
```

### 2. Adaptive Analysis

Based on what it finds, it applies appropriate analyses:

**Sales/E-commerce Data** (dates, revenue, products):
- Time-series revenue trends
- Product performance analysis
- Seasonal patterns
- Customer segment breakdowns

**Financial Data** (transactions, amounts):
- Transaction trend analysis
- Statistical summaries with quartiles
- Correlation analysis between metrics
- Outlier detection

**Customer Data** (demographics, segments):
- Demographic distributions
- Geographic patterns
- Segmentation analysis
- Categorical breakdowns

**Operational Data** (timestamps, metrics):
- Time-series performance metrics
- Status distributions
- Efficiency measurements

**Survey Data** (responses, ratings):
- Response frequency analysis
- Rating distributions
- Cross-tabulations
- Sentiment patterns

### 3. Smart Visualization

Creates visualizations **only when they make sense**:

- **Time-series plots** - ONLY if date/timestamp columns exist
- **Correlation heatmaps** - ONLY if multiple numeric columns exist
- **Category distributions** - ONLY if categorical columns exist
- **Histograms** - For numeric distributions when relevant

This prevents broken or meaningless charts.

### 4. Complete Output

Delivers everything in one comprehensive response:

```
============================================================
📊 DATA OVERVIEW
============================================================
Rows: 5,000 | Columns: 8
Columns: date, product, revenue, quantity, customer_segment, region

📋 DATA TYPES:
  • date: object (detected as date)
  • revenue: float64
  • quantity: int64
  • customer_segment: object
  • region: object

🔍 DATA QUALITY:
✓ No missing values - dataset is complete!

📈 NUMERICAL ANALYSIS:
[Summary statistics for revenue, quantity, etc.]

🔗 CORRELATIONS:
[Correlation matrix showing relationships]

📅 TIME SERIES ANALYSIS:
Date range: 2024-01-01 to 2024-12-31
Span: 365 days
Revenue trend: +15% growth over period

📊 VISUALIZATIONS CREATED:
  ✓ correlation_heatmap.png
  ✓ time_series_analysis.png
  ✓ distributions.png
  ✓ categorical_distributions.png

============================================================
✅ COMPREHENSIVE ANALYSIS COMPLETE
============================================================
```

## Installation

### Quick Install

1. Download the skill package (pre-built zip available)
2. Upload to Claude.ai via Settings → Capabilities → Skills
3. Enable the skill
4. Done! Upload any CSV and watch it work

### From Source

```bash
cd /path/to/AISkills/CSVDataSummarizer/csv-data-summarizer

# Install dependencies
pip install -r requirements.txt

# Test with sample data
python analyze.py examples/showcase_financial_pl_data.csv
```

### Dependencies

- Python 3.8 or higher
- pandas 2.0.0 or higher
- matplotlib 3.7.0 or higher
- seaborn 0.12.0 or higher

## Usage Examples

### Example 1: Sales Data Analysis

**Input**: `sales_data.csv` (5,000 rows, 12 months of e-commerce transactions)

**User**: "Here's my sales data."

**Skill Output** (immediate, automatic):
- Data overview: 5,000 orders across 8 product categories
- Revenue trending upward (22% growth)
- Peak sales in Q4 (November-December account for 35% of annual revenue)
- Product category A drives 60% of revenue
- Customer retention: 78% repeat buyers
- **4 visualizations**: Revenue trend, product performance, customer segments, correlation matrix

**No questions asked. Complete analysis in first response.**

### Example 2: Financial P&L Data

**Input**: `financial_pl_data.csv` (15 months of profit & loss metrics)

**User**: Uploads file without any prompt

**Skill Output** (immediate, automatic):
- 25 financial metrics analyzed
- Quarterly trends showing business growth
- Gross margin improving from 65% to 72%
- CAC decreasing while LTV increasing (healthy unit economics)
- Strong correlation between marketing spend and revenue (r=0.87)
- **5 visualizations**: Time-series trends, correlation heatmap, metric distributions, quarterly comparisons

### Example 3: Customer Demographics

**Input**: `customer_data.csv` (10,000 customer records)

**User**: "Analyze this customer data."

**Skill Output** (immediate, automatic):
- 10,000 customers across 15 demographic attributes
- Age distribution: Primary segment 25-34 (42%)
- Geographic concentration: 60% in top 3 regions
- Segment breakdown with proportions
- Income distribution analysis
- **3 visualizations**: Demographic distributions, geographic breakdown, segment comparison

### Example 4: Survey Responses

**Input**: `survey_results.csv` (500 responses, 20 questions)

**User**: "What insights can you find?"

**Skill Output** (immediate, automatic):
- 500 complete responses (98% completion rate)
- Overall satisfaction: 4.2/5.0 average
- Top pain points identified from open responses
- Strong correlation between product quality rating and recommendation likelihood
- Demographic breakdowns showing segment differences
- **4 visualizations**: Rating distributions, cross-tabulations, satisfaction trends, segment comparisons

## Customization

While the skill is designed to be fully automatic, you can customize the analysis by modifying `analyze.py`:

### Adjust Analysis Depth

```python
# In analyze.py, modify the number of categories shown:
for col in categorical_cols[:5]:  # Change 5 to show more/fewer
    value_counts = df[col].value_counts()
```

### Add Custom Metrics

```python
# Add domain-specific calculations:
if 'revenue' in df.columns and 'cost' in df.columns:
    df['profit_margin'] = (df['revenue'] - df['cost']) / df['revenue']
    summary.append(f"Average profit margin: {df['profit_margin'].mean():.1%}")
```

### Change Visualization Style

```python
# Modify seaborn style:
sns.set_style("whitegrid")  # Options: darkgrid, whitegrid, dark, white, ticks
sns.set_palette("husl")     # Change color palette
```

## Integration with Other Skills

The CSV Data Summarizer works well with:

- **Writing Skills** - Use analysis results in reports and presentations
- **Data Visualization** - Export charts for further refinement
- **Statistical Analysis** - Identify patterns for deeper investigation
- **Machine Learning Prep** - Understand data before modeling
- **Business Intelligence** - Quick insights for decision-making

## Design Philosophy

This skill embodies a key principle: **Proactive is better than reactive when the outcome is clear.**

Traditional AI workflow:
1. User provides data
2. AI asks "What would you like to do?"
3. User decides and responds
4. AI performs partial analysis
5. User asks for more
6. Multiple rounds of back-and-forth

Proactive workflow:
1. User provides data
2. AI immediately delivers comprehensive analysis
3. Done.

The key insight: For CSV analysis, users almost always want:
- Complete understanding of what's in the file
- Summary statistics
- Key patterns and trends
- Visualizations
- Data quality assessment

So why ask? Just deliver it all immediately.

This creates:
- **Faster time to value** - No decision-making delay
- **Better user experience** - "Wow" factor from thoroughness
- **Clear differentiation** - Doesn't feel like generic AI
- **Higher satisfaction** - Gets more than expected

For detailed analysis of how this pattern works and how to apply it to other skills, see `references/proactive-design-principles.md`.

## When NOT to Use This Pattern

The proactive pattern is NOT appropriate for:
- Creative tasks requiring user direction (style, tone, approach)
- Destructive operations requiring confirmation (deletion, overwriting)
- Ambiguous requests where clarification saves time
- Multi-path problems where user choice affects approach

For these cases, asking questions is still the right approach.

## Files and Structure

```
csv-data-summarizer/
├── SKILL.md                              # Skill definition (Claude.ai format)
├── README.md                             # This file
├── CHANGELOG.md                          # Version history
├── LICENSE                               # MIT License
├── analyze.py                            # Core analysis engine
├── requirements.txt                      # Python dependencies
├── examples/
│   ├── showcase_financial_pl_data.csv   # Demo P&L data (15 months, 25 metrics)
│   └── sample.csv                       # Basic example dataset
└── references/
    └── proactive-design-principles.md   # Design pattern extraction (CRITICAL)
```

## Technical Details

### Analysis Components

**Data Overview**:
- Row and column counts
- Column names and data types
- Data type detection (numeric, categorical, temporal)

**Data Quality**:
- Missing value detection and reporting
- Completeness percentage
- Data type consistency checks

**Numerical Analysis**:
- Descriptive statistics (mean, median, std dev, quartiles)
- Distribution analysis
- Outlier identification
- Correlation analysis (when 2+ numeric columns)

**Categorical Analysis**:
- Value frequency counts
- Category distributions
- Top values identification
- Percentage breakdowns

**Time Series Analysis** (when date columns present):
- Date range detection
- Temporal span calculation
- Trend analysis for numeric metrics over time
- Seasonal pattern identification

**Visualizations**:
- Correlation heatmaps (seaborn)
- Time-series line plots (matplotlib)
- Distribution histograms (matplotlib)
- Categorical bar charts (matplotlib)

### Performance Characteristics

- **Small datasets** (<1MB, <10K rows): Instant analysis
- **Medium datasets** (1-10MB, 10K-100K rows): 1-3 seconds
- **Large datasets** (10-50MB, 100K-500K rows): 3-10 seconds
- **Very large datasets** (>50MB, >500K rows): May require chunking or sampling

For very large datasets, the skill automatically samples to maintain performance while providing representative insights.

## Examples and Test Data

### Included Examples

**showcase_financial_pl_data.csv**:
- 15 months of P&L data
- 3 product lines (SaaS, Enterprise, Services)
- 25 financial metrics
- Perfect for demonstrating time-series, correlations, and growth analysis

**sample.csv**:
- Basic example with mixed data types
- Good for testing basic functionality
- Includes numeric, categorical, and date columns

### Creating Custom Test Data

```python
import pandas as pd
import numpy as np

# Generate sample sales data
dates = pd.date_range('2024-01-01', periods=365)
data = {
    'date': dates,
    'revenue': np.random.normal(10000, 2000, 365),
    'orders': np.random.randint(50, 200, 365),
    'product': np.random.choice(['A', 'B', 'C'], 365),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 365)
}
df = pd.DataFrame(data)
df.to_csv('test_sales_data.csv', index=False)
```

## Validation and Testing

Before packaging, validate the skill:

```bash
# From AISkills root directory
./SkillTemplate/scripts/validate-skill.sh CSVDataSummarizer/csv-data-summarizer

# Expected: All checks pass
# - SKILL.md has valid YAML frontmatter
# - SKILL.md is under 500 words
# - README.md exists and is comprehensive
# - Required files present
# - No malformed content
```

## Packaging

To create a distributable skill package:

```bash
# From AISkills root directory
./SkillPackager/scripts/package-skill.sh CSVDataSummarizer/csv-data-summarizer

# Creates: CSVDataSummarizer/csv-data-summarizer.zip
# Includes: SKILL.md, analyze.py, requirements.txt, examples/
```

## Performance Tips

### For Large Files

If analyzing very large CSVs (>100MB):

```python
# Read in chunks
chunk_size = 10000
chunks = pd.read_csv(file_path, chunksize=chunk_size)

# Or sample the data
df = pd.read_csv(file_path, nrows=10000)  # First 10K rows
# or
df = pd.read_csv(file_path).sample(n=10000)  # Random 10K rows
```

### For Memory Constraints

```python
# Use appropriate dtypes
df = pd.read_csv(file_path, dtype={
    'id': 'int32',  # Instead of int64
    'category': 'category',  # Instead of object
})

# Or read specific columns only
df = pd.read_csv(file_path, usecols=['date', 'revenue', 'product'])
```

## Troubleshooting

### Issue: Skill doesn't activate automatically

**Solution**: Ensure the CSV file is actually attached/uploaded. The skill triggers on CSV file presence.

### Issue: Date columns not detected

**Solution**: Ensure date column names contain "date" or "time", or manually specify:
```python
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
```

### Issue: Too many visualizations

**Solution**: The skill adapts to data structure. If you have many numeric/categorical columns, it will create multiple charts. This is intentional for comprehensiveness.

### Issue: Missing dependencies

**Solution**: Install all requirements:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions welcome! Potential enhancements:

- **Additional chart types** - Box plots, scatter plots, pair plots
- **Statistical tests** - Normality tests, correlation significance
- **Anomaly detection** - Outlier identification with explanations
- **Export options** - PDF report generation, Excel output
- **Custom templates** - Industry-specific analysis templates
- **Interactive visualizations** - Plotly instead of matplotlib

## Credits and License

**Original Author**: coffeefuelbump (Corbin Brown)
**Source**: https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill
**License**: MIT License

**AISkills Integration**: Lee Gonzales
**Integration Date**: 2025-11-16
**Score**: 93/100
**Category**: Data Analysis, Proactive Design Pattern

This skill is part of the AISkills collection, a curated library of high-quality Claude skills with comprehensive documentation and testing.

## Related Resources

- **Design Principles**: See `references/proactive-design-principles.md` for detailed extraction of the "DO NOT ASK" pattern
- **Writing Skills**: Cross-referenced for persuasion principles that make this pattern work
- **Skill Template**: Use as reference for creating other proactive skills
- **AISkills Collection**: https://github.com/leegonzales/AISkills

## Version History

See CHANGELOG.md for detailed version history.

**Current Version**: 1.0.0 (AISkills Integration)
**Original Version**: 2.1.0 (coffeefuelbump)

---

**Made with data-driven insights and proactive design principles.**

**Part of the AISkills collection - High-quality Claude skills for real-world use.**
