# 🚀 Oil & Gas Financial Modeling - Deployment Guide

## Overview

This project provides **two advanced Python-based alternatives to Excel** for oil & gas financial modeling:

1. **Interactive Jupyter Notebook** - Development environment with real-time controls
2. **Streamlit Web Application** - Professional investor presentation dashboard

Both solutions solve Excel's formula calculation limitations while providing superior interactivity and professional visualizations.

## 🏗️ Quick Start

### Prerequisites
- Python 3.11+
- `uv` package manager (recommended) or pip

### Installation

```bash
# Install all dependencies
uv sync

# Or with pip
pip install streamlit scipy plotly ipywidgets jupyter matplotlib pandas numpy openpyxl
```

## 📊 Usage Instructions

### 1. Interactive Jupyter Notebook

**Best for:** Development, analysis, and detailed exploration

```bash
# Launch Jupyter Lab
uv run jupyter lab

# Open: oil_gas_interactive_model.ipynb
```

**Features:**
- Real-time parameter controls with ipywidgets
- Interactive visualizations
- 60-month cash flow analysis
- NPV, IRR, and payback calculations
- Scenario comparison tools
- Export to Excel functionality

### 2. Streamlit Web Application

**Best for:** Investor presentations and professional dashboards

```bash
# Launch Streamlit app
uv run streamlit run streamlit_oil_gas_app.py
```

**Advanced Features:**
- Professional investor-grade dashboard
- Real-time parameter adjustments in sidebar
- Interactive charts with Plotly
- **Monte Carlo risk analysis** with 1000+ simulations
- Sensitivity analysis and correlation matrix
- Probabilistic NPV distributions
- Risk assessment metrics (VaR, probability analysis)
- Export capabilities (Excel with multiple sheets, CSV)
- Investment grade assessment

## 🎲 Advanced Analytics

### Monte Carlo Risk Analysis

The Streamlit application includes sophisticated risk analysis:

- **Probabilistic Modeling**: 1000+ Monte Carlo simulations
- **Volatility Controls**: Adjust uncertainty for each parameter
- **Risk Metrics**:
  - Value at Risk (5th percentile)
  - Expected NPV with confidence intervals
  - Probability of positive returns
  - Risk-adjusted return ratios
- **Visualizations**:
  - NPV probability distributions
  - Parameter correlation heatmaps
  - Sensitivity tornado charts
  - Percentile analysis tables

### Key Advantages Over Excel

✅ **Real-time calculations** - No formula dependency issues
✅ **Advanced risk analysis** - Monte Carlo simulations
✅ **Professional visualizations** - Interactive Plotly charts
✅ **Scenario modeling** - Instant parameter changes
✅ **Export capabilities** - Excel compatibility maintained
✅ **Investment grade** - Professional presentation ready

## 🌐 Deployment Options

### Option 1: Local Development
```bash
# Run locally for development/analysis
uv run streamlit run streamlit_oil_gas_app.py
```

### Option 2: Streamlit Cloud (Recommended)
1. Push code to GitHub repository
2. Connect to [share.streamlit.io](https://share.streamlit.io)
3. Deploy directly from GitHub
4. Get shareable public URL for investors

### Option 3: Docker Deployment
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "streamlit_oil_gas_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Option 4: Cloud Platforms
- **Heroku**: Easy deployment with git push
- **AWS/GCP/Azure**: Scalable cloud deployment
- **Railway/Render**: Modern deployment platforms

## 📈 Sample Analysis Results

**Base Case Scenario:**
- Oil Price: $65/barrel
- Gas Price: $3.25/MCF
- Initial Production: 1,000 bbl/month
- NPV @ 10%: ~$317k
- IRR: ~27.3%
- Payback: 30 months

**Monte Carlo Risk Analysis:**
- P90 NPV: ~$627k (optimistic)
- P50 NPV: ~$248k (expected)
- P10 NPV: ~-$246k (pessimistic)
- Probability of Positive NPV: 76%

## 🔧 Customization

### Adding New Parameters
1. Update the sidebar controls in `streamlit_oil_gas_app.py`
2. Modify the `calculate_oil_gas_model()` function
3. Add new parameters to Monte Carlo volatility settings

### Custom Visualizations
- Charts use Plotly for full interactivity
- Easy to add new chart types
- Supports 3D visualizations and animations

### Industry-Specific Modifications
- Adjust decline curve models
- Modify cost escalation assumptions
- Update tax and royalty calculations
- Add commodity price correlations

## 📊 File Structure

```
excel-megabuilder/
├── oil_gas_interactive_model.ipynb    # Jupyter notebook
├── streamlit_oil_gas_app.py           # Streamlit web app
├── DEPLOYMENT_GUIDE.md               # This guide
├── pyproject.toml                    # Dependencies
└── output/                           # Generated Excel files
```

## 🆘 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError`
**Solution**: Run `uv sync` to install all dependencies

**Issue**: Streamlit warnings about ScriptRunContext
**Solution**: These are harmless warnings when running calculations outside UI

**Issue**: Monte Carlo simulation slow
**Solution**: Reduce number of simulations or run on more powerful hardware

### Support

For technical support or feature requests:
1. Check this deployment guide
2. Review the code comments in both files
3. Test with smaller datasets first
4. Ensure all dependencies are installed correctly

---

## 🎯 Success Metrics

**vs Excel Limitations:**
- ✅ No formula calculation errors
- ✅ Real-time interactivity
- ✅ Advanced risk analysis capabilities
- ✅ Professional presentation quality
- ✅ Easy deployment and sharing
- ✅ Scalable for large datasets

**Business Value:**
- Faster investment decision making
- More accurate risk assessment
- Professional investor presentations
- Reduced modeling errors
- Enhanced scenario analysis

---

*Ready to revolutionize your oil & gas financial modeling with Python!* 🛢️📊