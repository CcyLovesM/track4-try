# Comparing Investment Attractiveness Using Financial Ratios

## 1. Overview

This project builds an **interactive financial dashboard** to help **beginner investors**
compare the investment attractiveness of companies using a small set of key financial ratios.

Instead of using complex valuation models, the project focuses on **clarity, intuition, and practical interpretation**.

The dashboard compares three global fast-food companies:

- McDonald's  
- Yum Brands(KFC, Pizza Hut, Taco Bell...)
- Restaurant Brands International (RBI)(Burger King, Tim Hortons, Popeyes...)

Users can explore how these firms differ in profitability, growth, and financial risk through an interactive Streamlit app.

The goal is to provide a clear and intuitive framework that helps beginner investors make informed comparisons across companies.

This project emphasizes clarity and interpretability over complexity.


## 2. Data Source

The dataset is constructed from **Compustat (via WRDS)** and includes:

- Net Income (`ni`)
- Total Assets (`at`)
- Shareholders’ Equity (`ceq`)
- Revenue (`sale`)
- Long-Term Debt (`dltt`)

Time period: **2019 – 2024**


## 3. Methodology

### Data Processing
- Cleaned and structured panel data by company and year
- Calculated financial ratios

### Key Financial Ratios

- **ROA (Return on Assets)** = Net Income / Total Assets  
- **ROE (Return on Equity)** = Net Income / Equity  
- **Profit Margin** = Net Income / Revenue  
- **Revenue Growth** = Year-over-year revenue change  
- **Leverage** = Long-Term Debt / Total Assets  

### Visualization

The app uses multiple chart types to improve interpretation:

- Line charts → trends over time  
- Grouped bar charts → cross-company comparison  
- Box plots → volatility and distribution  


## 4. Key Insights

### Profitability

- **Yum Brands** shows the highest and most consistent ROA → strong asset efficiency  
- **McDonald's** has the highest profit margin → strong pricing power  
- **RBI** remains structurally weaker in profitability  

### Growth

- **RBI** has the highest revenue growth → expansion-driven strategy  
- **McDonald's** shows volatile growth but strong earnings → profitability-driven model  
- **Yum Brands** demonstrates stable and balanced growth  

### Risk (Leverage)

- **Yum Brands** has the highest and most volatile leverage → higher financial risk  
- **McDonald's** maintains moderate leverage supported by strong profits  
- **RBI** has the lowest leverage but weaker performance  

### Key Investment Takeaway

- Strong growth does not guarantee profitability  
- High profitability can offset growth volatility  
- Leverage adds hidden risk  

**Beginner investors should always combine multiple ratios rather than rely on a single metric.**


## 5. Interactive App

This project includes a **Streamlit dashboard** that allows users to:

- Select companies to compare  
- Adjust the time range  
- Switch between analysis sections:
  - Profitability (ROA & Margin)
  - ROE & Net Income
  - Growth
  - Leverage (risk)
- View a latest-year snapshot table  

The app is designed to make financial analysis **interactive and beginner-friendly**.


## How to Run

```bash
streamlit run app.py
