import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page setup
# -------------------------------------------------
st.set_page_config(
    page_title="Beginner Investor Comparison Dashboard",
    layout="wide"
)

# -------------------------------------------------
# Data
# -------------------------------------------------
data = [
    # McDonald's
    {"company": "McDonald's", "year": 2019, "sale": 21076.5, "ni": 6025.4, "at": 47510.8, "ceq": -8210.3, "dltt": 46875.9,
     "roa": 0.126822, "roe": -0.733883, "profit_margin": 0.285882, "leverage": 0.986637, "revenue_growth": None},
    {"company": "McDonald's", "year": 2020, "sale": 19207.8, "ni": 4730.5, "at": 52626.8, "ceq": -7824.9, "dltt": 48518.1,
     "roa": 0.089888, "roe": -0.604544, "profit_margin": 0.246280, "leverage": 0.921928, "revenue_growth": -0.088663},
    {"company": "McDonald's", "year": 2021, "sale": 23222.9, "ni": 7545.2, "at": 53854.3, "ceq": -4601.0, "dltt": 48643.6,
     "roa": 0.140104, "roe": -1.639904, "profit_margin": 0.324903, "leverage": 0.903244, "revenue_growth": 0.209035},
    {"company": "McDonald's", "year": 2022, "sale": 23182.6, "ni": 6177.4, "at": 50435.6, "ceq": -6003.4, "dltt": 48037.9,
     "roa": 0.122481, "roe": -1.028984, "profit_margin": 0.266467, "leverage": 0.952460, "revenue_growth": -0.001735},
    {"company": "McDonald's", "year": 2023, "sale": 25493.7, "ni": 8468.8, "at": 56146.8, "ceq": -4706.7, "dltt": 50210.6,
     "roa": 0.150833, "roe": -1.799307, "profit_margin": 0.332192, "leverage": 0.894274, "revenue_growth": 0.099691},
    {"company": "McDonald's", "year": 2024, "sale": 25920.0, "ni": 8223.0, "at": 55182.0, "ceq": -3797.0, "dltt": 51312.0,
     "roa": 0.149016, "roe": -2.165657, "profit_margin": 0.317245, "leverage": 0.929868, "revenue_growth": 0.016722},

    # RBI
    {"company": "Restaurant Brands International", "year": 2019, "sale": 5603.0, "ni": 643.0, "at": 22360.0, "ceq": 2490.0, "dltt": 13136.0,
     "roa": 0.028757, "roe": 0.258233, "profit_margin": 0.114760, "leverage": 0.587478, "revenue_growth": None},
    {"company": "Restaurant Brands International", "year": 2020, "sale": 4968.0, "ni": 486.0, "at": 22777.0, "ceq": 2167.0, "dltt": 13794.0,
     "roa": 0.021337, "roe": 0.224273, "profit_margin": 0.097826, "leverage": 0.605611, "revenue_growth": -0.113332},
    {"company": "Restaurant Brands International", "year": 2021, "sale": 5739.0, "ni": 838.0, "at": 23246.0, "ceq": 2237.0, "dltt": 14319.0,
     "roa": 0.036049, "roe": 0.374609, "profit_margin": 0.146018, "leverage": 0.615977, "revenue_growth": 0.155193},
    {"company": "Restaurant Brands International", "year": 2022, "sale": 6505.0, "ni": 1008.0, "at": 22746.0, "ceq": 2499.0, "dltt": 14177.0,
     "roa": 0.044315, "roe": 0.403361, "profit_margin": 0.154958, "leverage": 0.623274, "revenue_growth": 0.133473},
    {"company": "Restaurant Brands International", "year": 2023, "sale": 7022.0, "ni": 1190.0, "at": 23391.0, "ceq": 2866.0, "dltt": 14225.0,
     "roa": 0.050874, "roe": 0.415213, "profit_margin": 0.169467, "leverage": 0.608140, "revenue_growth": 0.079477},
    {"company": "Restaurant Brands International", "year": 2024, "sale": 8406.0, "ni": 1021.0, "at": 24632.0, "ceq": 3110.0, "dltt": 15511.0,
     "roa": 0.041450, "roe": 0.328296, "profit_margin": 0.121461, "leverage": 0.629709, "revenue_growth": 0.197095},

    # Yum Brands
    {"company": "Yum Brands", "year": 2019, "sale": 5597.0, "ni": 1294.0, "at": 5231.0, "ceq": -8016.0, "dltt": 10771.0,
     "roa": 0.247371, "roe": -0.161427, "profit_margin": 0.231195, "leverage": 2.059071, "revenue_growth": None},
    {"company": "Yum Brands", "year": 2020, "sale": 5652.0, "ni": 904.0, "at": 5852.0, "ceq": -7891.0, "dltt": 11095.0,
     "roa": 0.154477, "roe": -0.114561, "profit_margin": 0.159943, "leverage": 1.895933, "revenue_growth": 0.009827},
    {"company": "Yum Brands", "year": 2021, "sale": 6584.0, "ni": 1575.0, "at": 5966.0, "ceq": -8373.0, "dltt": 11971.0,
     "roa": 0.263996, "roe": -0.188105, "profit_margin": 0.239216, "leverage": 2.006537, "revenue_growth": 0.164897},
    {"company": "Yum Brands", "year": 2022, "sale": 6842.0, "ni": 1325.0, "at": 5846.0, "ceq": -8876.0, "dltt": 12184.0,
     "roa": 0.226651, "roe": -0.149279, "profit_margin": 0.193657, "leverage": 2.084160, "revenue_growth": 0.039186},
    {"company": "Yum Brands", "year": 2023, "sale": 7076.0, "ni": 1597.0, "at": 6231.0, "ceq": -7858.0, "dltt": 11899.0,
     "roa": 0.256299, "roe": -0.203232, "profit_margin": 0.225692, "leverage": 1.909645, "revenue_growth": 0.034201},
    {"company": "Yum Brands", "year": 2024, "sale": 7567.0, "ni": 1486.0, "at": 6727.0, "ceq": -7648.0, "dltt": 12168.0,
     "roa": 0.220901, "roe": -0.194299, "profit_margin": 0.196379, "leverage": 1.808830, "revenue_growth": 0.069389},
]

df = pd.DataFrame(data)

metric_labels = {
    "roa": "ROA",
    "profit_margin": "Profit Margin",
    "roe": "ROE",
    "revenue_growth": "Revenue Growth",
    "leverage": "Leverage",
    "ni": "Net Income"
}

metric_explanations = {
    "roa": "ROA shows how efficiently a company uses its assets to generate profit.",
    "profit_margin": "Profit Margin shows how much profit a company keeps from its revenue.",
    "roe": "ROE shows how efficiently a company generates returns on shareholders’ equity.",
    "revenue_growth": "Revenue Growth measures how quickly a company increases its sales over time.",
    "leverage": "Leverage reflects the extent to which a company relies on debt financing.",
    "ni": "Net Income shows the absolute level of profit earned by the company."
}

metric_takeaways = {
    "roa": """
A higher and more stable ROA usually suggests stronger operating efficiency.  
For beginner investors, this helps show which company converts assets into earnings more effectively.
""",
    "profit_margin": """
A higher profit margin suggests stronger cost control and pricing power.  
For beginner investors, stable margins can signal business quality and resilience.
""",
    "roe": """
ROE can be useful, but it should not be read alone.  
If equity is negative, ROE may become misleading even when the company is profitable.
""",
    "revenue_growth": """
Revenue growth helps show expansion potential, but growth alone is not enough.  
Beginner investors should always compare growth with profitability and risk.
""",
    "leverage": """
Higher leverage may raise financial risk, especially if earnings weaken.  
For beginner investors, debt should be judged together with profitability, not on its own.
""",
    "ni": """
Net Income shows absolute earnings power.  
For beginner investors, it is useful for checking whether a company is truly profitable, especially when ratios look unusual.
"""
}

# -------------------------------------------------
# Helper functions
# -------------------------------------------------
def plot_line(dataframe, y_col, title, y_label):
    fig, ax = plt.subplots(figsize=(9, 5))
    for company in dataframe["company"].unique():
        subset = dataframe[dataframe["company"] == company]
        ax.plot(subset["year"], subset[y_col], marker="o", label=company)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(y_label)
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

def plot_grouped_bar(dataframe, y_col, title, y_label):
    pivot_df = dataframe.pivot(index="year", columns="company", values=y_col)
    fig, ax = plt.subplots(figsize=(10, 5))
    pivot_df.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(y_label)
    ax.legend(title="Company")
    ax.tick_params(axis="x", rotation=0)
    ax.grid(axis="y", alpha=0.3)
    st.pyplot(fig)

def plot_box(dataframe, y_col, title, y_label):
    fig, ax = plt.subplots(figsize=(8, 5))
    companies = dataframe["company"].unique().tolist()
    boxplot_data = [dataframe[dataframe["company"] == company][y_col].dropna() for company in companies]
    ax.boxplot(boxplot_data, tick_labels=companies)
    ax.set_title(title)
    ax.set_xlabel("Company")
    ax.set_ylabel(y_label)
    ax.grid(axis="y", alpha=0.3)
    st.pyplot(fig)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("📊 Beginner Investor Comparison Dashboard")
st.markdown("""
This app translates the notebook analysis into an interactive dashboard for **beginner investors**.  
It compares **McDonald's, Yum Brands, and Restaurant Brands International (RBI)** using a small set of financial ratios:
**ROA, Profit Margin, ROE, Revenue Growth, Leverage, and Net Income**.
""")

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.header("Dashboard Controls")

selected_metric = st.sidebar.selectbox(
    "Choose a metric for quick comparison:",
    ["roa", "profit_margin", "roe", "revenue_growth", "leverage", "ni"],
    format_func=lambda x: metric_labels[x]
)

selected_companies = st.sidebar.multiselect(
    "Choose companies:",
    options=df["company"].unique().tolist(),
    default=df["company"].unique().tolist()
)

filtered_df = df[df["company"].isin(selected_companies)].copy()

# -------------------------------------------------
# Interactive Overview
# -------------------------------------------------
st.header("1. Interactive Overview")

col1, col2 = st.columns([2, 1])

with col1:
    plot_line(
        filtered_df,
        selected_metric,
        f"{metric_labels[selected_metric]} Over Time",
        metric_labels[selected_metric]
    )

with col2:
    st.subheader("Quick Meaning")
    st.info(metric_explanations[selected_metric])

    st.subheader("Summary Statistics")
    summary = (
        filtered_df.groupby("company")[selected_metric]
        .agg(mean="mean", min="min", max="max")
        .round(3)
        .reset_index()
    )
    st.dataframe(summary, use_container_width=True, hide_index=True)

st.subheader(f"Why {metric_labels[selected_metric]} matters")
st.markdown(metric_takeaways[selected_metric])

st.subheader(f"{metric_labels[selected_metric]} Distribution")
plot_box(
    filtered_df,
    selected_metric,
    f"Distribution of {metric_labels[selected_metric]} by Company",
    metric_labels[selected_metric]
)

with st.expander("View processed data table"):
    st.dataframe(df, use_container_width=True)

st.markdown("---")

# -------------------------------------------------
# Step 1
# -------------------------------------------------
st.header("2. Step 1. Profitability: ROA and Profit Margin")
st.markdown("""
This section uses **ROA** and **Profit Margin** to provide a simple comparison of firms' profitability for beginner investors.
""")

st.latex(r"ROA = \frac{Net\ Income}{Total\ Assets}")
st.latex(r"Profit\ Margin = \frac{NI}{SALE}")

c1, c2 = st.columns(2)
with c1:
    plot_line(df, "roa", "ROA Over Time", "ROA")
with c2:
    plot_line(df, "profit_margin", "Profit Margin Over Time", "Profit Margin")

st.markdown("""
- **Structural Differences in Performance**  
  - **Yum Brands** consistently operates at a higher level across both ROA and Profit Margin, suggesting a structurally stronger and more mature business model.  
  - **Restaurant Brands International** remains at the lower end throughout the period, indicating a persistent weakness in its profitability base rather than temporary fluctuations.  
  - **McDonald’s** stays in the middle-to-high range, reflecting solid but not extreme overall performance.  

- **Profitability vs Efficiency**  
  Comparing the two metrics reveals a clear distinction between profitability and efficiency.  
  - **McDonald’s** achieves relatively high profit margins but lower ROA, implying that its asset utilization is less efficient.  
  - **Yum Brands** maintains leading ROA despite not always having the highest margins, indicating a stronger ability to convert assets into returns.  

- **Resilience and Mean Reversion**  
  **Yum Brands** shows a sharp decline in 2020 followed by a strong recovery in 2021, suggesting high resilience and a clear mean reversion pattern. This indicates that its performance is less affected by short-term shocks over the longer term.  

- **Common Trends and External Factors**  
  All three firms experience a decline around 2020, pointing to a shared external shock rather than firm-specific issues. However, the subsequent recovery differs: **McDonald’s** and **Yum Brands** rebound more strongly, while **Restaurant Brands International** remains at a lower level, suggesting weaker internal resilience despite facing similar external conditions.
""")

st.markdown("---")

# -------------------------------------------------
# Step 2
# -------------------------------------------------
st.header("3. Step 2. ROE")
st.markdown("""
Return on Equity (ROE) provides a quick measure of how efficiently a company generates returns on shareholders’ capital.  
To ensure a more accurate interpretation, this step complements **ROE** with **Net Income** to distinguish between true profitability and the effects of financial structure.
""")

st.latex(r"ROE = \frac{Net\ Income}{Equity}")

c3, c4 = st.columns(2)
with c3:
    plot_line(df, "roe", "Return on Equity (ROE) Over Time", "ROE")
with c4:
    plot_line(df, "ni", "Net Income Over Time", "Net Income")

st.markdown("""
- **Why Are Some ROE Values Negative?**  
  The negative ROE observed for **McDonald's** and **Yum Brands** is **not driven by poor profitability**. Both companies report **positive Net Income** throughout the period, meaning they are consistently profitable. However, their **equity (CEQ) is negative**, likely due to high leverage and significant share repurchase activities. This demonstrates that ROE can be misleading when capital structure is unusual.  

- **Comparison Across Firms**  
  Unlike McDonald’s and Yum Brands, **RBI** maintains a positive equity base, resulting in more reliable and interpretable ROE values. This suggests that:  
  - **RBI’s ROE** more accurately reflects its **true operating performance**.  
  - The negative ROE of the other firms is primarily a **structural artifact**, rather than a sign of weak performance.  

- **Implications for Beginner Investors**  
  ROE is a powerful starting point because it summarizes how efficiently a company generates returns for shareholders. However, ROE alone can be misleading, especially when firms have unconventional capital structures.  
  To make better investment comparisons, beginner investors should:  
  - Avoid relying on a **single ratio in isolation**.  
  - Combine ROE with complementary indicators such as **Net Income** (to assess profitability) and **Leverage** (to understand financial structure).  

- **Investment Perspective**  
  All three companies are consistently profitable, but differ in financial structure and risk. **McDonald’s** and **Yum Brands** generate strong earnings, yet their negative equity suggests higher reliance on leverage, which can distort ROE and increase financial risk. In contrast, **Restaurant Brands International** maintains a positive equity base and more stable, interpretable ROE, making its performance easier to evaluate. For beginner investors, this implies that while high returns may be attractive, it is equally important to consider how those returns are generated and the underlying financial risk.
""")

st.markdown("---")

# -------------------------------------------------
# Step 3
# -------------------------------------------------
st.header("4. Step 3. Revenue Growth")
st.markdown("""
Revenue growth measures how quickly a company increases its sales over time and reflects its expansion potential.
""")

st.latex(r"Revenue\ Growth = \frac{Revenue_t - Revenue_{t-1}}{Revenue_{t-1}}")

st.markdown("""
This metric helps investors assess whether a firm can sustain and grow its operations beyond current profitability.
""")

plot_line(df, "revenue_growth", "Revenue Growth Comparison", "Revenue Growth")

st.markdown("""
### RBI: Growth Driven by Expansion, Not Efficiency
From the revenue growth chart, **RBI** maintains positive growth from 2021 to 2024, reaching close to **20% in 2024**. On the surface, it appears to have the strongest growth among the three companies.

However, when we look at this together with **ROA, profit margin, and net income**, a different picture emerges:

- Its **ROA** is consistently the lowest, roughly around **2%–5%**
- Its **profit margin** is also the lowest, approximately **10%–17%**
- Although net income is increasing, its absolute level is significantly lower than McDonald’s

This suggests that RBI is indeed expanding its revenue, but it is less effective at converting that revenue into profit and asset returns. In other words, it has growth, but the **quality** of that growth is relatively low.

**From an investment perspective, this implies:**  
RBI’s growth is more likely driven by scale expansion rather than high-quality, efficient growth. Therefore, it is not sufficient to conclude that RBI is the most attractive investment simply because it has the highest growth, as this growth is not supported by strong profitability.

### McDonald’s: Volatile Growth with Strong Profitability
From the revenue growth chart, **McDonald’s** shows the most volatile pattern. If we only look at revenue growth, it may seem unstable. However, when we compare this with other metrics:

- **Net income** remains the highest across all years
- **Profit margin** is consistently the highest (around **25%–33%**)
- **ROA** is also clearly stronger than RBI

This suggests that McDonald’s issue is not weak profitability, but rather fluctuations in revenue growth. Revenue growth volatility in this case does not necessarily imply weaker investment attractiveness.

**From an investment perspective, this implies:**  
McDonald’s does not rely on stable growth to generate strong financial performance. It is able to maintain high profitability even when growth is unstable, which reflects a mature and highly efficient business model. McDonald’s offers a profitability-driven investment profile, where strong and consistent earnings can offset the impact of unstable revenue growth.

### Yum Brands: Balanced and Sustainable Growth
From the revenue growth chart, **Yum Brands** maintains moderate growth, generally between **3% and 7%**, without extreme fluctuations.

When combined with other metrics:

- It has the **highest ROA**
- Profit margin is at a **solid mid-to-high level**
- Net income shows **stable and consistent growth**

This indicates that Yum Brands is not focused on aggressive expansion, but instead achieves a balance between **growth, efficiency, and profitability**.

**From an investment perspective, this implies:**  
Yum Brands may be more suitable for beginner investors seeking a balance between growth and profitability, supported by relatively stable performance. Its moderate but consistent growth, combined with strong efficiency, suggests a more sustainable and predictable investment profile.
""")

st.markdown("---")

# -------------------------------------------------
# Step 4
# -------------------------------------------------
st.header("5. Step 4. Risk Analysis — Leverage")
st.markdown("""
Leverage is used to evaluate a company’s financial risk by showing how much debt it uses relative to its asset base.  
In general, a higher leverage ratio suggests greater financial risk, because the company may face stronger repayment pressure and higher sensitivity to changes in earnings or interest rates.
""")

st.latex(r"Leverage = \frac{Long\text{-}Term\ Debt}{Total\ Assets}")

st.subheader("5.1 Use Group Bar Chart to show risk level and risk trend")
plot_grouped_bar(
    df,
    "leverage",
    "Leverage Ratio by Company and Year",
    "Leverage (Long-Term Debt / Total Assets)"
)

st.markdown("""
A basic interpretation is that **higher leverage implies greater financial risk**, because a larger portion of the firm’s asset base is supported by debt. From this perspective, **Yum Brands** appears the riskiest, **RBI** the most conservative, and **McDonald’s** lies in between.

However, **leverage should not be assessed in isolation**. Debt becomes problematic only when a company lacks the profitability and efficiency needed to support it. Therefore, leverage must be interpreted together with the earlier results on revenue growth, profit margin, ROA, and net income.

### Yum Brands: Stable operations, but debt-dependent structure
Yum Brands appears relatively stable in revenue growth and shows moderate profitability. However, its consistently high leverage suggests that this stability is supported by a much more debt-heavy capital structure.

This matters because high leverage can enhance downside risk:

- interest obligations reduce financial flexibility;
- the company becomes more vulnerable during economic slowdowns;
- future expansion may rely more heavily on financing conditions.

> Therefore, while Yum Brands looks stable from a growth perspective, its balance sheet introduces an additional layer of financial risk that beginner investors should not ignore.

### McDonald’s: Moderate leverage supported by strong fundamentals
McDonald’s has more volatile revenue growth, but its leverage ratio remains relatively controlled and stable. More importantly, the company also shows the strongest profitability metrics in the group, including the highest profit margin, strong ROA, and the largest net income.

This combination changes the interpretation of leverage. Moderate debt is less concerning when the company has strong earnings power, because profits provide a buffer against financial obligations. In this sense, McDonald’s leverage appears **manageable rather than excessive**.

> For investors, this suggests that McDonald’s may be more resilient than its growth volatility initially implies. Its business model generates enough profit to support debt while still maintaining strong operating performance.

### RBI: Conservative financing, but weaker efficiency
RBI has the lowest leverage, which indicates a more conservative financing position and lower balance-sheet risk. This is a positive sign, especially for beginner investors who may prefer companies with less debt exposure.

However, **low leverage does not automatically make a company more attractive**. Earlier charts show that RBI has weaker profitability and efficiency compared with McDonald’s. This suggests that although its financing risk is lower, its operating quality is not as strong.

> In other words, RBI is less risky from a debt perspective, but it is also less impressive in turning growth into returns.

Overall, the most attractive company is not necessarily the one with the lowest leverage, but the one that balances debt, profitability, and growth most effectively.
""")

st.subheader("5.2 Use Box Plot to show risk volatility")
plot_box(
    df,
    "leverage",
    "Distribution of Leverage by Company",
    "Leverage (Long-Term Debt / Total Assets)"
)

st.markdown("""
The median line shows the typical leverage level.  
The height of the box indicates how stable the leverage is over time: **shorter = stable, taller = more risk and uncertainty**.  
The whiskers reflect extreme values.

### What Does Leverage Volatility Indicate?
Leverage volatility reflects how a company’s capital structure (debt vs equity) changes over time. It provides important insights beyond the average level of debt.

There are three key dimensions to interpret leverage volatility:

- **Capital Structure Stability**  
  Low volatility suggests a stable and consistent financing policy, while high volatility indicates frequent changes in debt levels.

- **Financing Strategy**  
  Stable leverage implies long-term planning, whereas fluctuating leverage suggests that the firm actively adjusts its borrowing in response to expansion needs or financial conditions.

- **Financial Risk and Uncertainty**  
  Higher volatility increases uncertainty, especially when combined with high leverage. This can amplify financial risk because both the level and predictability of debt become concerns.

This distribution shows a clear structural difference in financial risk across the three firms. **Yum Brands** not only has the highest leverage level, but also the widest distribution, indicating both heavy reliance on debt and greater variation in its capital structure over time. In contrast, **Restaurant Brands International (RBI)** exhibits both the lowest leverage and the narrowest distribution, suggesting a consistently conservative financing approach. **McDonald’s** lies between the two, with moderate leverage and relatively low variability.

### Combined with other financial indicators
Yum Brands appears relatively stable in revenue growth and maintains moderate profit margins, but its high and variable leverage introduces a hidden risk. The firm’s performance may look stable from an operational perspective, yet its dependence on debt implies that part of this stability is supported by financial leverage. This means that in less favourable conditions, such as rising interest rates or declining earnings, its risk could materialise more quickly.

McDonald’s presents a contrasting case. Although its revenue growth is more volatile, it consistently achieves the highest profit margins and strong net income levels. When viewed alongside its moderate and stable leverage distribution, this suggests that its financial structure is well supported by strong earnings capacity. In other words, McDonald’s does not rely on increasing debt to sustain performance, making its overall risk profile more manageable despite fluctuations in growth.

RBI, on the other hand, shows the lowest financial risk from a leverage perspective, as indicated by both low levels and minimal variation. However, its weaker profitability and lower returns imply that this conservative structure does not translate into superior performance. This highlights an important limitation for investors: low leverage reduces financial risk, but does not necessarily enhance investment attractiveness if the firm cannot generate strong returns.

Overall, the leverage box plot helps investors distinguish between three fundamentally different profiles:

- A **high-leverage, variable structure (Yum Brands)**, where financial risk is elevated despite stable operations.
- A **moderate and stable leverage structure supported by strong profitability (McDonald’s)**, indicating a more balanced and resilient business model.
- A **low-risk but lower-return structure (RBI)**, where financial conservatism comes at the cost of weaker performance.

For beginner investors, this demonstrates that leverage should not be evaluated in isolation. Its true value lies in how it interacts with profitability and growth, helping to reveal whether a company’s performance is driven by operational strength or supported by financial risk.
""")

st.markdown("---")

# -------------------------------------------------
# Conclusion
# -------------------------------------------------
st.header("6. Conclusion")
st.markdown("""
All three companies' financial characteristics differ significantly when **profitability, growth, and risk** are considered together.

**Yum Brands** demonstrates strong overall performance in terms of profitability and efficiency, and its results are relatively consistent across time. However, its leverage shows noticeable volatility, indicating that its financial risk is not entirely stable. This suggests that while Yum Brands appears operationally strong, it may still carry underlying financial risk that beginner investors should be aware of.

**McDonald’s** presents a more balanced profile across the three dimensions. It maintains strong profitability and does not exhibit extreme behavior in either growth or leverage. Although some fluctuations exist, they are less pronounced compared to the other companies. This makes McDonald’s a relatively stable and predictable option when considering both return and risk together.

**Restaurant Brands International** stands out for its higher growth potential, but this comes with weaker profitability and greater overall risk. Its financial structure appears less stable, suggesting that its performance may be more sensitive to external factors. For beginner investors, this highlights the importance of not relying solely on growth indicators.

Overall, **no single company dominates across all dimensions**.

- **Yum Brands** is strong but carries leverage-related risk.  
- **McDonald’s** offers the most balanced risk-return profile.  
- **Restaurant Brands International** represents a higher-risk, higher-growth profile.
""")

st.success(
    "This dashboard is designed for educational purposes and shows why beginner investors should compare multiple financial ratios together rather than relying on one metric alone."
)
