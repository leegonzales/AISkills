# Example Datasets and Expected Output

This directory contains sample CSV files for testing and demonstrating the CSV Data Summarizer skill.

## Included Examples

### 1. showcase_financial_pl_data.csv

**Description**: 15 months of Profit & Loss financial data for a SaaS business

**Characteristics**:
- **Rows**: 15 (monthly records)
- **Columns**: 25+ financial metrics
- **Product Lines**: 3 (SaaS, Enterprise, Services)
- **Time Period**: 15-month trend
- **Data Types**: Mixed (dates, revenue figures, percentages, metrics)

**Key Metrics Include**:
- Revenue by product line
- Cost of Goods Sold (COGS)
- Gross margin and profit
- Operating expenses
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)
- Churn rates
- Monthly Recurring Revenue (MRR)

**Expected Analysis Output**:

```
============================================================
📊 DATA OVERVIEW
============================================================
Rows: 15 | Columns: 26

📋 DATA TYPES:
  • Month: object (temporal)
  • SaaS_Revenue: float64
  • Enterprise_Revenue: float64
  • Services_Revenue: float64
  • Total_Revenue: float64
  • COGS: float64
  • Gross_Margin_%: float64
  • [... 19 more metrics]

🔍 DATA QUALITY:
✓ No missing values - dataset is complete!

📈 NUMERICAL ANALYSIS:
Key statistics for 25 numeric columns:
- Revenue trending upward (growth visible)
- Margins improving over time
- CAC decreasing (efficiency improving)
- LTV increasing (customer value growing)

🔗 CORRELATIONS:
Strong correlations identified:
- Marketing spend vs Revenue: 0.87 (strong positive)
- CAC vs MRR: -0.65 (inverse as expected)
- Customer count vs Revenue: 0.92 (very strong)

📅 TIME SERIES ANALYSIS:
Date range: 15 months of monthly data
Clear quarterly trends visible
Q4 shows seasonal strength

📊 VISUALIZATIONS CREATED:
  ✓ correlation_heatmap.png - Shows relationships between 25 metrics
  ✓ time_series_analysis.png - Revenue and margin trends over 15 months
  ✓ distributions.png - Distribution of key metrics
  ✓ categorical_distributions.png - Product line breakdown
```

**Best For**: Demonstrating time-series analysis, financial metrics, correlation detection

---

### 2. sample.csv

**Description**: Basic example dataset with mixed data types

**Characteristics**:
- **Rows**: ~100-500 records
- **Columns**: 5-10 columns
- **Data Types**: Mix of numeric, categorical, and date columns
- **Purpose**: Testing basic functionality

**Typical Structure**:
```csv
date,product,revenue,quantity,customer_segment,region
2024-01-05,Widget A,1250.00,15,Enterprise,North
2024-01-05,Widget B,850.00,8,SMB,South
...
```

**Expected Analysis Output**:

```
============================================================
📊 DATA OVERVIEW
============================================================
Rows: 100 | Columns: 6

📋 DATA TYPES:
  • date: object
  • product: object
  • revenue: float64
  • quantity: int64
  • customer_segment: object
  • region: object

🔍 DATA QUALITY:
✓ No missing values - dataset is complete!

📈 NUMERICAL ANALYSIS:
Revenue: mean=$1,050, median=$950, std=$320
Quantity: mean=12, median=10, std=5

🔗 CORRELATIONS:
Revenue vs Quantity: 0.78 (strong positive correlation)

📊 CATEGORICAL ANALYSIS:
Product distribution:
  • Widget A: 35 (35%)
  • Widget B: 40 (40%)
  • Widget C: 25 (25%)

Customer Segment distribution:
  • Enterprise: 30 (30%)
  • SMB: 45 (45%)
  • Mid-Market: 25 (25%)

Region distribution:
  • North: 28 (28%)
  • South: 23 (23%)
  • East: 25 (25%)
  • West: 24 (24%)

📅 TIME SERIES ANALYSIS:
Date range: 2024-01-05 to 2024-04-11
Span: 97 days

📊 VISUALIZATIONS CREATED:
  ✓ correlation_heatmap.png
  ✓ time_series_analysis.png
  ✓ distributions.png
  ✓ categorical_distributions.png
```

**Best For**: Testing basic CSV analysis, verifying installation

---

## Creating Your Own Test Data

### Sales Data Template

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate 365 days of sales data
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]

np.random.seed(42)  # For reproducibility

data = {
    'date': dates,
    'order_id': range(1, 366),
    'product': np.random.choice(['Widget A', 'Widget B', 'Widget C', 'Widget D'], 365),
    'revenue': np.random.normal(1000, 300, 365).round(2),
    'quantity': np.random.randint(1, 50, 365),
    'customer_segment': np.random.choice(['Enterprise', 'SMB', 'Mid-Market'], 365),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 365),
    'customer_type': np.random.choice(['New', 'Returning'], 365, p=[0.3, 0.7])
}

df = pd.DataFrame(data)

# Add some realistic patterns
df.loc[df['customer_segment'] == 'Enterprise', 'revenue'] *= 1.5
df.loc[df['product'] == 'Widget A', 'revenue'] *= 1.2

# Add seasonal pattern (Q4 boost)
df.loc[df['date'].dt.quarter == 4, 'revenue'] *= 1.15

df.to_csv('test_sales_data.csv', index=False)
print(f"Created test_sales_data.csv with {len(df)} rows")
```

### Financial Metrics Template

```python
import pandas as pd
import numpy as np

# Generate 24 months of financial data
months = pd.date_range('2023-01-01', periods=24, freq='MS')

np.random.seed(42)

# Base metrics with growth trend
base_revenue = 100000
growth_rate = 0.03  # 3% monthly growth

data = {
    'month': months,
    'total_revenue': [base_revenue * (1 + growth_rate) ** i + np.random.normal(0, 5000)
                      for i in range(24)],
}

# Calculate derived metrics
df = pd.DataFrame(data)
df['cogs'] = df['total_revenue'] * 0.30  # 30% COGS
df['gross_profit'] = df['total_revenue'] - df['cogs']
df['gross_margin_pct'] = (df['gross_profit'] / df['total_revenue'] * 100).round(1)
df['operating_expenses'] = df['total_revenue'] * 0.45
df['net_profit'] = df['gross_profit'] - df['operating_expenses']
df['net_margin_pct'] = (df['net_profit'] / df['total_revenue'] * 100).round(1)

# Round revenue figures
for col in ['total_revenue', 'cogs', 'gross_profit', 'operating_expenses', 'net_profit']:
    df[col] = df[col].round(2)

df.to_csv('test_financial_data.csv', index=False)
print(f"Created test_financial_data.csv with {len(df)} months")
```

### Customer Demographics Template

```python
import pandas as pd
import numpy as np

np.random.seed(42)

n_customers = 1000

data = {
    'customer_id': range(1, n_customers + 1),
    'age': np.random.randint(18, 75, n_customers),
    'gender': np.random.choice(['Male', 'Female', 'Other'], n_customers, p=[0.48, 0.48, 0.04]),
    'income_bracket': np.random.choice(['<30k', '30-50k', '50-75k', '75-100k', '>100k'],
                                       n_customers, p=[0.15, 0.25, 0.30, 0.20, 0.10]),
    'region': np.random.choice(['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West'],
                               n_customers, p=[0.20, 0.18, 0.22, 0.15, 0.25]),
    'customer_segment': np.random.choice(['Budget', 'Standard', 'Premium'],
                                         n_customers, p=[0.40, 0.45, 0.15]),
    'lifetime_value': np.random.lognormal(7, 1, n_customers).round(2),
    'months_active': np.random.randint(1, 60, n_customers),
    'purchase_count': np.random.randint(1, 50, n_customers)
}

df = pd.DataFrame(data)

# Add correlations
df.loc[df['customer_segment'] == 'Premium', 'lifetime_value'] *= 1.8
df.loc[df['income_bracket'] == '>100k', 'lifetime_value'] *= 1.5

df.to_csv('test_customer_data.csv', index=False)
print(f"Created test_customer_data.csv with {len(df)} customers")
```

### Survey Responses Template

```python
import pandas as pd
import numpy as np

np.random.seed(42)

n_responses = 500

data = {
    'response_id': range(1, n_responses + 1),
    'product_quality': np.random.randint(1, 6, n_responses),  # 1-5 scale
    'customer_service': np.random.randint(1, 6, n_responses),
    'value_for_money': np.random.randint(1, 6, n_responses),
    'ease_of_use': np.random.randint(1, 6, n_responses),
    'overall_satisfaction': np.random.randint(1, 6, n_responses),
    'would_recommend': np.random.choice(['Yes', 'No', 'Maybe'], n_responses, p=[0.60, 0.15, 0.25]),
    'industry': np.random.choice(['Technology', 'Healthcare', 'Finance', 'Retail', 'Other'],
                                 n_responses, p=[0.25, 0.20, 0.20, 0.20, 0.15]),
    'company_size': np.random.choice(['1-10', '11-50', '51-200', '201-500', '500+'],
                                     n_responses, p=[0.15, 0.30, 0.25, 0.20, 0.10]),
    'product_used': np.random.choice(['Product A', 'Product B', 'Product C'],
                                     n_responses, p=[0.50, 0.30, 0.20])
}

df = pd.DataFrame(data)

# Add realistic correlations
df.loc[df['product_quality'] >= 4, 'overall_satisfaction'] = \
    np.minimum(5, df.loc[df['product_quality'] >= 4, 'overall_satisfaction'] + 1)

df.to_csv('test_survey_data.csv', index=False)
print(f"Created test_survey_data.csv with {len(df)} responses")
```

---

## Testing the Skill

### Quick Test

```bash
# From the skill directory
python analyze.py examples/sample.csv

# Or with the financial data
python analyze.py examples/showcase_financial_pl_data.csv
```

### Expected Files Generated

After running analysis, you should see:
- `correlation_heatmap.png` - Correlation matrix visualization
- `time_series_analysis.png` - Trends over time (if date columns present)
- `distributions.png` - Histograms of numeric columns
- `categorical_distributions.png` - Bar charts of categorical data

### Validation Checklist

After running analysis, verify:
- [ ] Console output includes data overview
- [ ] Data types are correctly identified
- [ ] Missing values are reported (or "complete" message shown)
- [ ] Numerical statistics are calculated
- [ ] Correlations are shown (if 2+ numeric columns)
- [ ] Time-series analysis appears (if date columns exist)
- [ ] Visualization files are created
- [ ] Charts are readable and properly labeled
- [ ] Analysis completes without errors

---

## Common Data Types and Expected Behavior

### E-commerce/Sales Data
**Triggers**: Columns like 'order_date', 'revenue', 'product', 'customer'
**Expected**: Time-series trends, product performance, customer segments

### Financial/Accounting Data
**Triggers**: Columns like 'date', 'amount', 'transaction', 'account'
**Expected**: Trend analysis, statistical summaries, correlations

### Customer/Demographics Data
**Triggers**: Columns like 'age', 'gender', 'region', 'segment'
**Expected**: Distribution analysis, segmentation, geographic patterns

### Operational/Metrics Data
**Triggers**: Columns like 'timestamp', 'metric', 'status', 'value'
**Expected**: Time-series, performance metrics, status distributions

### Survey/Feedback Data
**Triggers**: Columns like 'rating', 'response', 'satisfaction', 'question'
**Expected**: Frequency analysis, rating distributions, cross-tabs

---

## Tips for Creating Good Test Data

1. **Include dates** - Enables time-series analysis
2. **Mix data types** - Numeric, categorical, and temporal
3. **Add correlations** - Makes analysis more interesting
4. **Realistic distributions** - Use normal, lognormal, or real-world patterns
5. **Appropriate size** - 100-1000 rows for testing, larger for performance testing
6. **Complete data** - No missing values for initial testing
7. **Clear column names** - Descriptive names help adaptive analysis

---

## Troubleshooting Example Data

### Issue: No time-series analysis generated

**Cause**: No date column detected
**Solution**: Ensure column name contains 'date' or 'time'

### Issue: No correlation heatmap

**Cause**: Only one numeric column
**Solution**: Add more numeric columns for correlation analysis

### Issue: Too many/too few charts

**Cause**: Data structure determines charts generated
**Solution**: This is expected - skill adapts to data

---

**Examples provided for testing and demonstration purposes.**
**Create custom test data based on your specific use case.**
