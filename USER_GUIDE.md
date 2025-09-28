# 🛢️ Oil & Gas Investment Analysis - Complete User Guide

## 📋 Table of Contents
1. [What This Tool Does](#what-this-tool-does)
2. [Getting Started](#getting-started)
3. [Understanding the Interface](#understanding-the-interface)
4. [Step-by-Step Usage Guide](#step-by-step-usage-guide)
5. [Reading the Results](#reading-the-results)
6. [Advanced Features](#advanced-features)
7. [Export Options](#export-options)
8. [Common Use Cases](#common-use-cases)
9. [Troubleshooting](#troubleshooting)

---

## What This Tool Does

This **Oil & Gas Investment Analysis** tool helps you:

✅ **Evaluate oil and gas well investments** with professional financial modeling
✅ **Calculate key metrics** like NPV, IRR, and payback period
✅ **Analyze production decline** over 60 months
✅ **Assess investment risk** with Monte Carlo simulation
✅ **Generate investor-ready reports** in Excel and CSV formats
✅ **Compare different scenarios** (conservative, base case, optimistic)

**Perfect for:** Investors, analysts, operators, and anyone evaluating oil & gas opportunities.

---

## Getting Started

### Option 1: Use Online (Easiest)
1. Go to the deployed application URL (if available)
2. Start using immediately - no installation required!

### Option 2: Run Locally
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py

# Or use the runner script
python run_app.py
```

### Option 3: Docker (Recommended for consistent environment)
```bash
# Build and run with Docker
docker build -t oil-gas-app .
docker run -p 8501:8501 oil-gas-app

# Access at http://localhost:8501
```

---

## Understanding the Interface

### Main Sections

**🎛️ Sidebar Controls (Left)**
- Market parameters (oil price, gas price)
- Production profile settings
- Financial assumptions

**📊 Main Dashboard (Center)**
- Key investment metrics display
- Interactive charts and graphs
- Detailed analysis tables

**📈 Results Area**
- Investment grade assessment
- Risk analysis summary
- Export options

---

## Step-by-Step Usage Guide

### Step 1: Set Market Conditions 💰

**In the sidebar, adjust:**

- **Oil Price ($/barrel):** Current or expected oil price
  - *Typical range: $45-$80*
  - *Example: $65/barrel*

- **Gas Price ($/MCF):** Natural gas price per thousand cubic feet
  - *Typical range: $2.50-$5.00*
  - *Example: $3.25/MCF*

### Step 2: Configure Production Profile 📉

- **Initial Production (bbl/month):** How much oil the well produces in month 1
  - *Typical range: 500-2,000 bbl/month*
  - *Example: 1,000 bbl/month*

- **Monthly Decline Rate (%):** How much production decreases each month
  - *Typical range: 1.0%-3.0%*
  - *Example: 1.5% per month*

### Step 3: Set Financial Assumptions 📊

- **Discount Rate (%):** Required rate of return for the investment
  - *Typical range: 8%-15%*
  - *Example: 10% annual*

### Step 4: Review Key Metrics 🎯

The dashboard automatically calculates:

- **Total Investment:** How much money you need to invest
- **NPV (Net Present Value):** Profit after considering time value of money
- **Payback Period:** How long until you recover your investment
- **Final Cumulative Cash Flow:** Total profit over 60 months

### Step 5: Analyze Charts 📈

**Production Decline Chart:**
- Shows how oil and gas production decreases over time
- Blue line = Oil production
- Orange line = Gas production

**Revenue Stream Chart:**
- Green = Oil revenue over time
- Red = Gas revenue over time
- Shows which commodity drives your returns

**Cash Flow Chart:**
- Top chart = Monthly cash flow (positive/negative bars)
- Bottom chart = Cumulative cash flow (running total)
- Break-even point where line crosses zero

---

## Reading the Results

### Investment Grade Assessment

The tool automatically grades your investment:

🏆 **EXCELLENT** (NPV Return > 25%)
- Outstanding investment opportunity
- Very high returns expected

🥇 **VERY GOOD** (NPV Return 15-25%)
- Strong investment with good returns
- Above average opportunity

🥈 **GOOD** (NPV Return 5-15%)
- Decent investment with moderate returns
- Acceptable risk-adjusted returns

🥉 **ACCEPTABLE** (NPV Return 0-5%)
- Marginal investment
- Consider other opportunities

❌ **POOR** (NPV Return < 0%)
- Negative returns expected
- Avoid this investment

### Key Metric Explanations

**NPV (Net Present Value)**
- *What it means:* Profit in today's dollars after considering time value of money
- *Good result:* Positive NPV means profitable investment
- *Example:* NPV of $317k means $317,000 profit in present value

**IRR (Internal Rate of Return)**
- *What it means:* The percentage return your investment earns annually
- *Good result:* IRR higher than your required return rate
- *Example:* IRR of 27.3% means 27.3% annual return

**Payback Period**
- *What it means:* How long until you get your initial investment back
- *Good result:* Shorter payback is better (less risk)
- *Example:* 30 months = 2.5 years to break even

---

## Advanced Features

### Scenario Comparison 🎯

Click **"Run Scenario Analysis"** to compare three cases:

- **Conservative:** Lower prices, higher decline rate (pessimistic view)
- **Base Case:** Your current input parameters
- **Optimistic:** Higher prices, lower decline rate (best case scenario)

This helps you understand the range of possible outcomes.

### Monte Carlo Risk Analysis 🎲

Click **"Run Monte Carlo Analysis"** for advanced risk assessment:

**What it does:**
- Runs 1,000+ simulations with random price variations
- Shows probability distributions of outcomes
- Calculates risk metrics like Value at Risk

**Key Results:**
- **P90 NPV:** 90% chance results will be better than this (pessimistic)
- **P50 NPV:** 50% chance results will be better than this (expected)
- **P10 NPV:** 10% chance results will be better than this (optimistic)
- **Probability of Positive NPV:** Chance the investment will be profitable

**Example Interpretation:**
- P90: -$246k (10% chance of losing more than $246k)
- P50: $248k (expected profit of $248k)
- P90: $627k (10% chance of making more than $627k)
- 76% probability of positive returns

---

## Export Options

### Excel Export 📊
**Contains multiple professional sheets:**

1. **Executive Summary:** Key metrics and investment overview
2. **Monthly Analysis:** Detailed 60-month cash flow projection
3. **Investment Summary:** All calculated financial metrics
4. **Input Parameters:** Your assumptions for reference
5. **Monte Carlo Results:** Risk analysis data (if run)
6. **Risk Assessment:** Probability metrics and statistics

**Professional formatting with:**
- Headers and borders
- Currency formatting
- Auto-sized columns
- Corporate color scheme

### CSV Export 📋
**Comprehensive single-file report with:**

- Executive summary section
- Input parameters used
- Complete monthly analysis
- Risk metrics (if available)
- Easy to import into other tools

**Perfect for:**
- Data analysis in other software
- Creating custom reports
- Sharing with technical teams

---

## Common Use Cases

### 🏭 **For Operators**
*"Should we drill this well?"*

1. Set realistic production estimates and costs
2. Use current commodity prices
3. Run Monte Carlo analysis for risk assessment
4. Export results for management presentation

### 💼 **For Investors**
*"Is this a good investment opportunity?"*

1. Input operator's production forecasts
2. Use your required rate of return as discount rate
3. Compare multiple scenarios
4. Focus on NPV return percentage and risk metrics

### 🏦 **For Lenders**
*"What's the risk of this loan?"*

1. Use conservative assumptions
2. Run Monte Carlo analysis
3. Focus on probability of positive cash flow
4. Assess downside scenarios (P10 results)

### 📊 **For Analysts**
*"How does this compare to other opportunities?"*

1. Standardize assumptions across opportunities
2. Compare NPV returns and IRR
3. Use scenario analysis for sensitivity testing
4. Export data for portfolio analysis

---

## Troubleshooting

### Common Issues

**❓ "The NPV is negative"**
- Check if oil/gas prices are too low
- Verify initial production isn't too optimistic
- Consider if decline rate is too aggressive
- Review if discount rate is too high

**❓ "Payback period is very long"**
- Usually indicates low initial production or high costs
- Check if commodity prices are realistic
- Consider increasing initial production estimate

**❓ "Monte Carlo shows high risk"**
- Normal for volatile commodity markets
- Focus on probability of positive returns
- Consider if you're comfortable with the risk level

**❓ "Results seem unrealistic"**
- Double-check all input parameters
- Ensure production estimates are reasonable
- Verify commodity prices are current market rates

### Getting Help

**Check these first:**
1. Verify all input parameters are realistic
2. Compare results to similar wells in the area
3. Run scenario analysis to understand range of outcomes

**For technical issues:**
- Check browser console for errors
- Try refreshing the page
- Ensure stable internet connection

---

## 🎯 Quick Start Checklist

**For a typical evaluation:**

☐ Set oil price to current market rate (e.g., $65/bbl)
☐ Set gas price to current market rate (e.g., $3.25/MCF)
☐ Input realistic initial production (e.g., 1,000 bbl/month)
☐ Use typical decline rate (e.g., 1.5% per month)
☐ Set your required return rate (e.g., 10%)
☐ Review the investment grade assessment
☐ Run scenario analysis for sensitivity
☐ Export results for presentation

**You're ready to make informed oil & gas investment decisions!** 🚀

---

*This tool provides sophisticated financial analysis typically found in expensive petroleum software, accessible through an easy-to-use web interface. Perfect for due diligence, investment evaluation, and risk assessment in the oil & gas industry.*