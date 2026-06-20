<<<<<<< HEAD
# 📊 N100 Financial Intelligence Platform

## Overview

The N100 Financial Intelligence Platform is an end-to-end Financial Analytics and Investment Intelligence project developed using Python, Pandas, and Streamlit.

The platform analyzes financial performance data of Nifty 100 companies and transforms raw financial statements into actionable insights through custom KPI calculations, financial health scoring, sector benchmarking, peer comparison, and investment screening.

This project demonstrates practical Data Analytics, Financial Analysis, Data Processing, Dashboard Development, and Business Intelligence skills.

---

# Project Objectives

The primary objective of this project is to:

* Analyze financial performance of Nifty 100 companies
* Build a Financial Health Scoring Engine
* Compare companies against sector benchmarks
* Identify high-quality investment opportunities
* Create investment screening models
* Develop an interactive dashboard for financial decision-making

---

# Dataset

The project uses company-level financial data including:

* Revenue
* Net Profit
* Operating Profit
* Return on Equity (ROE)
* Debt-to-Equity Ratio
* Interest Coverage Ratio
* Asset Turnover
* Free Cash Flow
* Capital Expenditure
* Earnings Per Share (EPS)
* Book Value Per Share
* Dividend Payout Ratio

The processed dataset contains:

* 92 Companies
* 1184 Financial Records
* Multiple sectors across the Nifty 100 universe

---

# Key Features

## 1. Financial KPI Engine

Calculated and analyzed important financial metrics including:

### Profitability KPIs

* Net Profit Margin
* Operating Profit Margin
* Return on Equity

### Leverage KPIs

* Debt-to-Equity Ratio
* Interest Coverage Ratio

### Efficiency KPIs

* Asset Turnover Ratio
* Cash Flow Metrics

---

## 2. Financial Health Score Engine

A custom scoring model was developed to evaluate company financial strength.

The health score combines:

* Profitability performance
* Capital efficiency
* Debt management
* Cash generation capability

Companies are categorized into:

* Excellent
* Good
* Average
* Weak

---

## 3. Sector Analytics

Sector-level benchmarking was performed to identify:

* Strongest sectors
* Weakest sectors
* Average health score by sector

### Sample Findings

| Rank | Sector                 | Average Health Score |
| ---- | ---------------------- | -------------------- |
| 1    | Information Technology | 83.52                |
| 2    | Consumer Staples       | 79.34                |
| 3    | Healthcare             | 71.54                |

---

## 4. Peer Comparison Engine

Each company is compared against its sector average.

Metrics generated:

* Company Health Score
* Sector Average Score
* Difference from Sector Average

This allows investors to identify outperforming and underperforming companies within the same industry.

---

## 5. Investment Screeners

### Quality Growth Screener

Identifies companies with:

* Health Score > 80
* ROE > 15%

### Debt-Free Screener

Identifies companies with:

* Debt-to-Equity Ratio < 0.5

### High ROE Screener

Identifies companies generating superior shareholder returns.

### Turnaround Screener

Identifies companies showing strong profit growth and improving financial health.

---

# Dashboard Features

An interactive Streamlit dashboard was developed with the following modules:

## Home Page

Displays:

* Total Companies
* Total Records
* Average Health Score
* Excellent Rated Companies

---

## Company Search

Allows users to:

* Search any company
* View historical financial health scores
* Analyze financial performance trends

---

## Sector Analytics

Provides:

* Sector Ranking Table
* Sector Health Score Visualization
* Top Performing Companies

---

## Investment Screeners

Interactive screening system for:

* Quality Growth Stocks
* Debt-Free Stocks
* High ROE Stocks
* Turnaround Opportunities

---

## Peer Comparison

Compare a company against its sector benchmark and identify relative strengths.

---

# Technologies Used

## Programming

* Python

## Data Processing

* Pandas
* NumPy

## Dashboard Development

* Streamlit

## Data Storage

* CSV Files

## Development Environment

* Visual Studio Code

---

# Project Structure

N100_Financial_Intelligence/

├── dashboards/

│ └── app.py

├── data/

│ ├── raw/

│ └── processed/

├── src/

│ ├── data_understanding.py

│ ├── financial_ratios_analysis.py

│ ├── health_score.py

│ ├── sector_analytics.py

│ ├── peer_comparison.py

│ ├── investment_screener.py

│ └── turnaround_screener.py

├── reports/

│ └── screenshots/

├── notebooks/

└── README.md

---

# Business Impact

This platform can assist:

* Retail Investors
* Financial Analysts
* Equity Researchers
* Investment Advisors

by providing a structured framework for evaluating financial performance and identifying potential investment opportunities.

---

# Future Enhancements

Planned improvements include:

* Real-time stock market integration
* Advanced valuation models
* Risk scoring framework
* Portfolio optimization module
* Predictive analytics using Machine Learning
* Cloud deployment

---

# Author

**Medhaswini**

Final Year B.Tech (ECE)

Aspiring Data Analyst | Financial Analytics Enthusiast

---

# Dashboard Preview

(Add dashboard screenshots here)

* Home Page
* Company Search
* Sector Analytics
* Investment Screeners
* Peer Comparison
=======
# N100_Financial_Intelligence
Financial analytics platform for Nifty 100 companies featuring health scoring, sector analytics, peer comparison, investment screeners, and interactive Streamlit dashboards.
>>>>>>> 2c62c4065202354fd267737975f40638de9941dc
