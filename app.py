import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Beginner Investor Dashboard",
    layout="wide"
)

st.title("📊 Beginner Investor Comparison Dashboard")
st.markdown("""
This app helps beginner investors compare the investment attractiveness of  
**McDonald's, Yum Brands, and Restaurant Brands International (RBI)**  
using a small set of financial ratios.
""")

# -----------------------------
# Load data
# -----------------------------
# Option 1:
# If you already saved your processed data as a CSV file,
# put it in the same folder as app.py and use:
#
# df = pd.read_csv("financial_ratios.csv")
#
# The file should contain columns like:
# company, year, ROE, ROA, Revenue Growth, Leverage, Profit Margin

# -----------------------------
# Temporary sample data
# Replace this with your real data later
# -----------------------------
data = {
    "company": ["McDonald's"] * 5 + ["Yum Brands"] * 5 + ["RBI"] * 5,
    "year": [2020, 2021, 2022, 2023, 2024] * 3,
    "ROE": [0.12, 0.15, 0.18, 0.17, 0.16,
            0.25, 0.27, 0.26, 0.28, 0.29,
            0.08, 0.10, 0.09, 0.11, 0.12],
    "ROA": [0.06, 0.07, 0.08, 0.08, 0.07,
            0.09, 0.10, 0.10, 0.11, 0.11,
            0.04, 0.05, 0.05, 0.06, 0.06],
    "Revenue Growth": [-0.05, 0.10, 0.06, 0.03, 0.04,
                       0.02, 0.04, 0.05, 0.06, 0.03,
                       0.01, 0.08, 0.04, 0.12, 0.20],
    "Leverage": [2.1, 2.3, 2.4, 2.2, 2.1,
                 3.2, 3.4, 3.3, 3.5, 3.6,
                 2.8, 2.9, 3.0, 3.1, 3.2],
    "Profit Margin": [0.28, 0.30, 0.31, 0.29, 0.30,
                      0.33, 0.34, 0.35, 0.34, 0.33,
                      0.18, 0.20, 0.21, 0.22, 0.23]
}

df = pd.DataFrame(data)

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.header("Filter Options")

metric_list = ["ROE", "ROA", "Revenue Growth", "Leverage", "Profit Margin"]
selected_metric = st.sidebar.selectbox("Select a financial ratio:", metric_list)

company_list = df["company"].unique().tolist()
selected_companies = st.sidebar.multiselect(
    "Select companies:",
    options=company_list,
    default=company_list
)

# Filter data
filtered_df = df[df["company"].isin(selected_companies)]

# -----------------------------
# Show raw data
# -----------------------------
with st.expander("View Data Table"):
    st.dataframe(filtered_df)

# -----------------------------
# Ratio explanation
# -----------------------------
st.subheader(f"📘 What does {selected_metric} mean?")

explanations = {
    "ROE": """
**ROE (Return on Equity)** shows how effectively a company generates profit from shareholders' equity.  
A higher ROE may suggest stronger returns for investors, but it should be interpreted carefully if equity is unusually low.
""",
    "ROA": """
**ROA (Return on Assets)** measures how efficiently a company uses its assets to generate profit.  
A higher ROA usually suggests better operating efficiency.
""",
    "Revenue Growth": """
**Revenue Growth** shows whether a company's sales are expanding over time.  
Stable positive growth may indicate stronger business momentum and expansion potential.
""",
    "Leverage": """
**Leverage** reflects how much debt a company uses relative to its financial base.  
Higher leverage may increase financial risk, especially during uncertain periods.
""",
    "Profit Margin": """
**Profit Margin** shows how much profit a company keeps from its revenue.  
A higher margin suggests stronger cost control and profitability.
"""
}

st.markdown(explanations[selected_metric])

# -----------------------------
# Line chart
# -----------------------------
st.subheader(f"📈 Trend of {selected_metric} Over Time")

fig, ax = plt.subplots(figsize=(10, 5))

for company in selected_companies:
    company_data = filtered_df[filtered_df["company"] == company]
    ax.plot(company_data["year"], company_data[selected_metric], marker="o", label=company)

ax.set_xlabel("Year")
ax.set_ylabel(selected_metric)
ax.set_title(f"{selected_metric} Comparison")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# -----------------------------
# Simple investor takeaway
# -----------------------------
st.subheader("💡 Beginner Investor Takeaway")

if selected_metric == "ROE":
    st.markdown("""
A company with consistently high ROE may appear attractive because it generates stronger returns for shareholders.  
However, beginners should also check whether the result is supported by healthy fundamentals rather than unusually low equity.
""")

elif selected_metric == "ROA":
    st.markdown("""
A consistently higher ROA may suggest that a company uses its assets more efficiently.  
For beginner investors, this can be a useful sign of operational strength.
""")

elif selected_metric == "Revenue Growth":
    st.markdown("""
Stable positive revenue growth may indicate a stronger ability to expand over time.  
Large fluctuations, however, may suggest less predictable performance.
""")

elif selected_metric == "Leverage":
    st.markdown("""
Higher leverage can help growth, but it also increases financial risk.  
Beginner investors may prefer companies with more stable and manageable leverage levels.
""")

elif selected_metric == "Profit Margin":
    st.markdown("""
A higher profit margin may indicate stronger pricing power or better cost control.  
For beginner investors, stable margins can be a helpful sign of business quality.
""")

# -----------------------------
# Box plot for risk / volatility
# -----------------------------
st.subheader(f"📦 Distribution of {selected_metric}")

fig2, ax2 = plt.subplots(figsize=(8, 5))

boxplot_data = []
labels = []

for company in selected_companies:
    company_values = filtered_df[filtered_df["company"] == company][selected_metric].dropna()
    boxplot_data.append(company_values)
    labels.append(company)

ax2.boxplot(boxplot_data, labels=labels)
ax2.set_title(f"Box Plot of {selected_metric}")
ax2.set_ylabel(selected_metric)
ax2.grid(True)

st.pyplot(fig2)

st.markdown("""
A box plot helps beginner investors see whether a company's performance is **stable or volatile**.  
A narrower spread suggests more consistency, while a wider spread may indicate greater fluctuation and risk.
""")

# -----------------------------
# Summary table
# -----------------------------
st.subheader("📋 Summary Statistics")

summary_table = filtered_df.groupby("company")[selected_metric].agg(["mean", "min", "max"]).round(3)
st.dataframe(summary_table)

# -----------------------------
# Final note
# -----------------------------
st.markdown("---")
st.markdown("""
This dashboard is designed for educational purposes.  
Beginner investors should compare multiple financial ratios together rather than relying on one single indicator.
""")