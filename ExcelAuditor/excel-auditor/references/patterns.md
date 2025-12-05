# Common Excel Patterns Reference

## Financial Models

### DCF (Discounted Cash Flow)
**Indicators**:
- Sheet names: "DCF", "Valuation", "Cash Flows", "WACC"
- Named ranges containing: discount_rate, terminal_value, wacc, fcf
- Functions: NPV, XNPV, IRR, XIRR
- Time series columns (Year 1, Year 2... or FY2024, FY2025...)
- Rows labeled: Revenue, EBITDA, CAPEX, Working Capital

### Budget/Forecast
**Indicators**:
- Sheet names: "Budget", "Forecast", "Plan", "Actuals"
- Month/quarter columns
- Variance calculations (Actual - Budget)
- Functions: SUMIF by period
- Department or cost center breakdowns

### P&L / Income Statement
**Indicators**:
- Line items: Revenue, COGS, Gross Margin, Operating Expenses, EBITDA, Net Income
- Percentage calculations (margins)
- Period comparisons (YoY, MoM)
- Subtotal rows with SUM formulas

### Three Statement Model
**Indicators**:
- Sheets for: Income Statement, Balance Sheet, Cash Flow
- Cross-sheet references between the three
- Check rows (Assets = Liabilities + Equity)
- Circular references for interest calculations

## Operational Trackers

### Inventory Management
**Indicators**:
- Columns: SKU, Item, Quantity, Reorder Point, Lead Time
- Functions: MIN, MAX for stock levels
- Conditional formatting for low stock
- SUMIF/COUNTIF for category totals

### Project Timeline
**Indicators**:
- Columns: Task, Start Date, End Date, Duration, Owner, Status
- Date calculations: NETWORKDAYS, EDATE
- Gantt-chart style conditional formatting
- Dependency references between tasks

### CRM / Contact List
**Indicators**:
- Columns: Name, Email, Phone, Company, Status, Last Contact
- Data validation dropdowns for Status
- VLOOKUP for company info
- COUNTIF for pipeline stages

### Employee Roster
**Indicators**:
- Columns: Name, Department, Title, Start Date, Salary, Manager
- Org hierarchy (Manager references)
- Date calculations for tenure
- SUMIF for department totals

## Reporting Templates

### Dashboard
**Indicators**:
- Heavy use of charts
- KPI summary cells with SUMIF/AVERAGEIF
- Data pulling from hidden detail sheets
- Sparklines or in-cell visualizations

### Weekly/Monthly Report
**Indicators**:
- Period selector cells
- INDIRECT or OFFSET for dynamic ranges
- Print area defined
- Header/footer with dates

### Scorecard
**Indicators**:
- Metrics with targets and actuals
- RAG (Red/Amber/Green) conditional formatting
- Percentage to target calculations
- Trend indicators

## Data Transformation

### ETL Staging
**Indicators**:
- Raw data sheet with minimal formatting
- Processing sheet with heavy TEXT/VALUE functions
- Output sheet with clean structure
- TRIM, CLEAN, SUBSTITUTE usage

### Pivot Source
**Indicators**:
- Single table structure
- No merged cells
- Consistent data types per column
- Named Table object

### Lookup Reference
**Indicators**:
- Key-value pair structure
- Used as VLOOKUP target
- Named range definitions
- Static data (no formulas)

## Red Flags by Pattern

### Fragile Financial Model
- Hardcoded growth rates in formulas (not in assumption cells)
- Missing IFERROR on division formulas
- Manual overrides without documentation
- Broken cross-sheet references

### Unmaintainable Tracker
- Color-coding as logic (no legend)
- Multiple data entry points for same value
- Inconsistent date formats
- Hidden rows with active formulas

### Risky Report
- Volatile functions updating on every open
- External links to unavailable files
- Circular references without iteration settings
- Password-protected calculation sheets
