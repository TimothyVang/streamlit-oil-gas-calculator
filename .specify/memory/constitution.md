<!--
SYNC IMPACT REPORT:
Version change: INITIAL → 1.0.0
Modified principles: N/A (Initial constitution creation)
Added sections: All sections (complete constitution)
Removed sections: N/A
Templates requiring updates: ✅ All templates reviewed for consistency
Follow-up TODOs: None
-->

# Streamlit Oil & Gas Financial Model Constitution

## Core Principles

### I. Financial Accuracy First
All financial calculations MUST be mathematically correct and auditable. Monte Carlo simulations require minimum 1000 iterations. NPV, IRR, and payback calculations must use industry-standard formulas. No approximations in financial metrics presented to investors.

### II. Real-Time Interactive Analysis
User interface MUST provide instant feedback on parameter changes. All charts and metrics update dynamically without page refresh. Interactive controls for all key variables (oil/gas prices, production rates, costs). Streamlit's reactive model ensures immediate calculation updates.

### III. Professional Investment Grade Output
All visualizations and reports MUST meet professional investment presentation standards. Executive summaries include P10/P50/P90 risk metrics. Export capabilities to Excel/CSV required for investor due diligence. Charts use financial industry color schemes and formatting.

### IV. Risk Analysis Completeness
Monte Carlo risk analysis MUST be comprehensive and statistically valid. Sensitivity analysis on all major variables required. Probability distributions for key uncertainties properly modeled. Risk metrics (VaR, confidence intervals) clearly presented to investors.

### V. Data Validation & Error Prevention
All user inputs MUST be validated for reasonable ranges. Error handling prevents application crashes from invalid data. Input constraints based on industry norms (oil prices $20-150/barrel, decline rates 5-50%). Clear error messages guide users to correct inputs.

## Performance Standards

Streamlit application MUST load within 5 seconds on standard internet connections. Monte Carlo simulations complete within 10 seconds for 1000+ iterations. Charts render smoothly without lag during parameter adjustments. Memory usage remains efficient for extended analysis sessions.

## Code Quality Requirements

Python code follows PEP 8 standards with proper documentation. Financial formulas include source references and validation tests. Plotly charts use consistent styling and professional themes. Dependencies limited to essential packages in requirements.txt.

## Governance

Constitution supersedes all development practices. Code changes require validation against financial accuracy principles. Monte Carlo implementations must be peer-reviewed for statistical correctness. Investment-grade output standards apply to all user-facing content.

**Version**: 1.0.0 | **Ratified**: 2025-09-28 | **Last Amended**: 2025-09-28