# 📊 Comparing Investment Attractiveness Using Financial Ratios

## 🔍 Overview

This project builds an **interactive financial dashboard** to help **beginner investors**
compare the investment attractiveness of companies using a **small set of key financial ratios**.

Instead of using complex valuation models, the project focuses on **clarity, intuition, and practical interpretation**.

The dashboard compares three global fast-food companies:

- McDonald's  
- Yum Brands  
- Restaurant Brands International (RBI)  

Users can explore how these firms differ in **profitability, growth, and financial risk** through an interactive Streamlit app.

---

## 🎯 Objective

**How can beginner investors use a small set of financial ratios to compare companies?**

This project answers that question by transforming raw financial data into a structured, easy-to-interpret decision framework.

---

## 📂 Data Source

The dataset is constructed from **Compustat (via WRDS)** and includes:

- Net Income (`ni`)
- Total Assets (`at`)
- Shareholders’ Equity (`ceq`)
- Revenue (`sale`)
- Long-Term Debt (`dltt`)

Time period: **2019 – 2024**

---

## ⚙️ Methodology

### 1. Data Processing
- Cleaned and structured panel data by company and year
- Calculated financial ratios

### 2. Key Financial Ratios

- **ROA (Return on Assets)** = Net Income / Total Assets  
- **ROE (Return on Equity)** = Net Income / Equity  
- **Profit Margin** = Net Income / Revenue  
- **Revenue Growth** = Year-over-year revenue change  
- **Leverage** = Long-Term Debt / Total Assets  

### 3. Visualization

The app uses multiple chart types to improve interpretation:

- Line charts → trends over time  
- Grouped bar charts → cross-company comparison  
- Box plots → volatility and distribution  

---

## 📊 Key Insights

### 🔹 Profitability

- **Yum Brands** shows the highest and most consistent ROA → strong asset efficiency  
- **McDonald's** has the highest profit margin → strong pricing power  
- **RBI** remains structurally weaker in profitability  

---

### 🔹 Growth

- **RBI** has the highest revenue growth → expansion-driven strategy  
- **McDonald's** shows volatile growth but strong earnings → profitability-driven model  
- **Yum Brands** demonstrates stable and balanced growth  

---

### 🔹 Risk (Leverage)

- **Yum Brands** has the highest and most volatile leverage → higher financial risk  
- **McDonald's** maintains moderate leverage supported by strong profits  
- **RBI** has the lowest leverage but weaker performance  

---

### 🔹 Key Investment Takeaway

No single company dominates across all metrics.

👉 Strong growth does not guarantee profitability  
👉 High profitability can offset growth volatility  
👉 Leverage adds hidden risk  

**Beginner investors should always combine multiple ratios rather than rely on a single metric.**

---

## 🖥️ Interactive App

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

---

## ▶️ How to Run

```bash
streamlit run app.py
