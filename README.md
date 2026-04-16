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


### I. Profitability: Efficiency vs Pricing Power

The three firms exhibit fundamentally different profitability structures.

- **Yum Brands** consistently achieves the highest ROA, indicating superior asset efficiency and a business model that converts resources into returns more effectively.
- **McDonald's** maintains the highest profit margin, suggesting strong pricing power and brand strength, but its lower ROA implies less efficient asset utilization.
- **RBI** lags behind in both metrics, pointing to a structurally weaker profitability base rather than temporary fluctuations.

**Investment Insight:**  
High margins do not necessarily mean high efficiency. Investors should distinguish between firms that generate profits through **pricing power** versus those that rely on **efficient operations**.


### II. Growth: Expansion vs Quality

Revenue growth patterns differ significantly across firms.

- **RBI** shows the strongest growth, especially post-2021, indicating aggressive expansion. However, this growth is not matched by improvements in profitability, suggesting **low-quality growth**.
- **McDonald's** exhibits volatile growth but consistently strong earnings, indicating a **profitability-driven model**.
- **Yum Brands** demonstrates moderate but stable growth, supported by strong operational efficiency.

**Investment Insight:**  
Growth alone is not sufficient. High growth without profitability may indicate expansion at the expense of efficiency.


### III. Risk: Leverage and Financial Structure

The firms also differ in their financial risk profiles.

- **Yum Brands** carries the highest and most volatile leverage, implying greater dependence on debt financing.
- **McDonald's** maintains moderate leverage, supported by strong and stable earnings.
- **RBI** has the lowest leverage, but also weaker returns.

**Investment Insight:**  
Leverage should be interpreted alongside profitability. High debt can amplify returns, but also increases vulnerability if earnings weaken.


### IV. Overall Comparison

Each company excels in different dimensions:

- **Yum Brands** → strongest efficiency, but higher financial risk  
- **McDonald's** → most balanced profile, combining profitability and manageable leverage  
- **RBI** → strongest growth, but weakest efficiency  

**Final Insight for Beginner Investors:**  
- No single ratio can determine investment attractiveness.  
- A meaningful comparison requires combining profitability, growth, and risk to understand whether performance is driven by operational strength or financial structure.


### V. Key Investment Takeaway

- Strong growth does not guarantee profitability  
- High profitability can offset growth volatility  
- Leverage adds hidden risk  


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
