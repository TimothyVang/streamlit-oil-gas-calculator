# 🛢️ Oil & Gas Investment Analysis - Streamlit App

## 🚀 Professional Financial Modeling Dashboard

This Streamlit application provides **investor-grade oil & gas financial analysis** with advanced Monte Carlo risk modeling - a superior alternative to Excel.

## ⚡ Quick Start

### Option 1: Simple Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Option 2: Using the Runner Script
```bash
# Install dependencies
pip install -r requirements.txt

# Run with the provided script
python run_app.py
```

### Option 3: Docker
```bash
# Build and run with Docker
docker build -t oil-gas-app .
docker run -p 8501:8501 oil-gas-app
```

## 🌐 Deploy to Streamlit Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set main file: `app.py`
5. Deploy and get a shareable URL!

## 📊 Features

### Real-Time Analysis
- ⚡ **Instant calculations** - No Excel formula errors
- 🎛️ **Interactive controls** - Adjust parameters in real-time
- 📈 **Professional charts** - Plotly visualizations

### Advanced Risk Analysis
- 🎲 **Monte Carlo simulation** - 1000+ scenarios
- 📊 **Risk metrics** - VaR, probability analysis
- 🎯 **Sensitivity analysis** - Parameter correlations
- 📈 **NPV distributions** - Investment confidence

### Professional Output
- 📋 **Executive summary** - Investment grade metrics
- 💾 **Export capabilities** - Excel, CSV downloads
- 🎯 **Scenario comparison** - Optimistic/Conservative/Base
- 🏢 **Investor presentations** - Professional dashboard

## 💰 Sample Results

**Base Case Analysis:**
- Oil: $65/barrel, Gas: $3.25/MCF
- Initial Production: 1,000 bbl/month
- **NPV @ 10%:** $317k
- **IRR:** 27.3%
- **Payback:** 30 months

**Monte Carlo Risk Assessment:**
- **P90 NPV:** $627k (optimistic)
- **P50 NPV:** $248k (expected)
- **P10 NPV:** -$246k (pessimistic)
- **Probability Positive:** 76%

## 🎯 Why Better Than Excel?

✅ **No formula errors** - Python handles all calculations reliably
✅ **Real-time updates** - Parameters change instantly
✅ **Advanced analytics** - Monte Carlo impossible in Excel
✅ **Professional charts** - Interactive Plotly visualizations
✅ **Easy sharing** - Web-based investor access
✅ **Scalable** - Handles complex scenarios efficiently

## 📁 Project Structure

```
├── app.py                     # Main Streamlit entry point
├── streamlit_oil_gas_app.py  # Core application logic
├── run_app.py                # Local development runner
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container deployment
├── README.md               # This file
├── .streamlit/             # Streamlit configuration
│   └── config.toml
├── docs/                   # Documentation
│   └── DEPLOYMENT_GUIDE.md
└── .gitignore             # Git ignore rules
```

### Key Features in Latest Update
- ✨ **Professional Excel Export** - Multi-sheet workbooks with formatting
- 📊 **Enhanced CSV Export** - Comprehensive reports with all metrics
- 🎨 **Styled Excel Output** - Headers, borders, colors, auto-sizing
- 📈 **Executive Summary Sheet** - Investment-grade summary
- 🎯 **Risk Assessment Export** - Monte Carlo results included

---

**Ready for professional oil & gas investment analysis!** 🎉