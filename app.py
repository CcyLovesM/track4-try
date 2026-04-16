import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Beginner Investor Dashboard",
    layout="wide",
)


COMPANY_COLORS = {
    "McDonald's": "#c1121f",
    "Yum Brands": "#1d3557",
    "Restaurant Brands International": "#2a9d8f",
}

METRIC_LABELS = {
    "ROA": "ROA",
    "ROE": "ROE",
    "Profit Margin": "Profit Margin",
    "Revenue Growth": "Revenue Growth",
    "Leverage": "Leverage",
}

PERCENT_METRICS = {"ROA", "ROE", "Profit Margin", "Revenue Growth"}


def load_data() -> pd.DataFrame:
    records = [
        {"company": "McDonald's", "year": 2019, "sale": 21076.5, "ni": 6025.4, "at": 47510.8, "ceq": -8210.3, "dltt": 46875.9},
        {"company": "McDonald's", "year": 2020, "sale": 19207.8, "ni": 4730.5, "at": 52626.8, "ceq": -7824.9, "dltt": 48518.1},
        {"company": "McDonald's", "year": 2021, "sale": 23222.9, "ni": 7545.2, "at": 53854.3, "ceq": -4601.0, "dltt": 48643.6},
        {"company": "McDonald's", "year": 2022, "sale": 23182.6, "ni": 6177.4, "at": 50435.6, "ceq": -6003.4, "dltt": 48037.9},
        {"company": "McDonald's", "year": 2023, "sale": 25493.7, "ni": 8468.8, "at": 56146.8, "ceq": -4706.7, "dltt": 50210.6},
        {"company": "McDonald's", "year": 2024, "sale": 25920.0, "ni": 8223.0, "at": 55182.0, "ceq": -3797.0, "dltt": 51312.0},
        {"company": "Restaurant Brands International", "year": 2019, "sale": 5603.0, "ni": 643.0, "at": 22360.0, "ceq": 2490.0, "dltt": 13136.0},
        {"company": "Restaurant Brands International", "year": 2020, "sale": 4968.0, "ni": 486.0, "at": 22777.0, "ceq": 2167.0, "dltt": 13794.0},
        {"company": "Restaurant Brands International", "year": 2021, "sale": 5739.0, "ni": 838.0, "at": 23246.0, "ceq": 2237.0, "dltt": 14319.0},
        {"company": "Restaurant Brands International", "year": 2022, "sale": 6505.0, "ni": 1008.0, "at": 22746.0, "ceq": 2499.0, "dltt": 14177.0},
        {"company": "Restaurant Brands International", "year": 2023, "sale": 7022.0, "ni": 1190.0, "at": 23391.0, "ceq": 2866.0, "dltt": 14225.0},
        {"company": "Restaurant Brands International", "year": 2024, "sale": 8406.0, "ni": 1021.0, "at": 24632.0, "ceq": 3110.0, "dltt": 15511.0},
        {"company": "Yum Brands", "year": 2019, "sale": 5597.0, "ni": 1294.0, "at": 5231.0, "ceq": -8016.0, "dltt": 10771.0},
        {"company": "Yum Brands", "year": 2020, "sale": 5652.0, "ni": 904.0, "at": 5852.0, "ceq": -7891.0, "dltt": 11095.0},
        {"company": "Yum Brands", "year": 2021, "sale": 6584.0, "ni": 1575.0, "at": 5966.0, "ceq": -8373.0, "dltt": 11971.0},
        {"company": "Yum Brands", "year": 2022, "sale": 6842.0, "ni": 1325.0, "at": 5846.0, "ceq": -8876.0, "dltt": 12184.0},
        {"company": "Yum Brands", "year": 2023, "sale": 7076.0, "ni": 1597.0, "at": 6231.0, "ceq": -7858.0, "dltt": 11899.0},
        {"company": "Yum Brands", "year": 2024, "sale": 7567.0, "ni": 1486.0, "at": 6727.0, "ceq": -7648.0, "dltt": 12168.0},
    ]
    df = pd.DataFrame(records).sort_values(["company", "year"]).reset_index(drop=True)
    df["ROA"] = df["ni"] / df["at"]
    df["ROE"] = df["ni"] / df["ceq"]
    df["Profit Margin"] = df["ni"] / df["sale"]
    df["Leverage"] = df["dltt"] / df["at"]
    df["Revenue Growth"] = df.groupby("company")["sale"].pct_change()
    return df


def format_metric(metric: str, value: float) -> str:
    if pd.isna(value):
        return "N/A"
    if metric in PERCENT_METRICS:
        return f"{value:.1%}"
    return f"{value:.2f}"


def format_money(value: float) -> str:
    if pd.isna(value):
        return "N/A"
    return f"${value:,.0f}m"


def draw_line_chart(data: pd.DataFrame, metric: str, title: str, ylabel: str):
    fig, ax = plt.subplots(figsize=(8, 4.8))
    for company in data["company"].unique():
        subset = data[data["company"] == company]
        ax.plot(
            subset["year"],
            subset[metric],
            marker="o",
            linewidth=2.5,
            markersize=6,
            color=COMPANY_COLORS.get(company),
            label=company,
        )
    if metric == "Revenue Growth":
        ax.axhline(0, linestyle="--", linewidth=1, color="#7a7a7a")
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25)
    ax.legend()
    return fig


def draw_grouped_bar_chart(data: pd.DataFrame, metric: str, title: str, ylabel: str):
    pivot = data.pivot(index="year", columns="company", values=metric)
    fig, ax = plt.subplots(figsize=(10, 5))
    years = pivot.index.tolist()
    companies = pivot.columns.tolist()
    width = 0.22
    x_positions = list(range(len(years)))

    for idx, company in enumerate(companies):
        offsets = [x + (idx - (len(companies) - 1) / 2) * width for x in x_positions]
        ax.bar(
            offsets,
            pivot[company].values,
            width=width,
            label=company,
            color=COMPANY_COLORS.get(company),
        )

    ax.set_xticks(x_positions)
    ax.set_xticklabels(years)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=0.25)
    ax.legend()
    return fig


def draw_box_plot(data: pd.DataFrame, metric: str, title: str, ylabel: str):
    companies = data["company"].unique().tolist()
    values = [data[data["company"] == company][metric].dropna() for company in companies]
    fig, ax = plt.subplots(figsize=(9, 4.8))
    box = ax.boxplot(values, labels=companies, patch_artist=True)
    for patch, company in zip(box["boxes"], companies):
        patch.set_facecolor(COMPANY_COLORS.get(company, "#cccccc"))
        patch.set_alpha(0.65)
    ax.set_title(title)
    ax.set_xlabel("Company")
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25)
    ax.tick_params(axis="x", rotation=8)
    return fig


def build_summary_table(data: pd.DataFrame, selected_metrics: list[str]) -> pd.DataFrame:
    latest_year = int(data["year"].max())
    latest = data[data["year"] == latest_year].copy()
    summary = latest[["company"] + selected_metrics].copy().sort_values("company")
    for metric in selected_metrics:
        summary[metric] = summary[metric].apply(lambda value: format_metric(metric, value))
    return summary.rename(columns={metric: METRIC_LABELS[metric] for metric in selected_metrics})


def build_snapshot(data: pd.DataFrame) -> pd.DataFrame:
    latest_year = int(data["year"].max())
    latest = data[data["year"] == latest_year].copy().sort_values("company")
    snapshot = latest[["company", "ni", "ROA", "Profit Margin", "Revenue Growth", "Leverage"]].rename(
        columns={"ni": "Net Income"}
    )
    snapshot["Net Income"] = snapshot["Net Income"].apply(format_money)
    snapshot["ROA"] = snapshot["ROA"].apply(lambda value: format_metric("ROA", value))
    snapshot["Profit Margin"] = snapshot["Profit Margin"].apply(lambda value: format_metric("Profit Margin", value))
    snapshot["Revenue Growth"] = snapshot["Revenue Growth"].apply(lambda value: format_metric("Revenue Growth", value))
    snapshot["Leverage"] = snapshot["Leverage"].apply(lambda value: format_metric("Leverage", value))
    return snapshot


df = load_data()

st.sidebar.header("Controls")
selected_companies = st.sidebar.multiselect(
    "Select companies",
    options=df["company"].unique().tolist(),
    default=df["company"].unique().tolist(),
)
selected_years = st.sidebar.slider(
    "Select year range",
    min_value=int(df["year"].min()),
    max_value=int(df["year"].max()),
    value=(int(df["year"].min()), int(df["year"].max())),
)
summary_metrics = st.sidebar.multiselect(
    "Select metrics for the summary table",
    options=list(METRIC_LABELS.keys()),
    default=["ROA", "Profit Margin", "Revenue Growth", "Leverage"],
)
show_dataset = st.sidebar.checkbox("Show processed dataset", value=False)

filtered_df = df[
    (df["company"].isin(selected_companies))
    & (df["year"] >= selected_years[0])
    & (df["year"] <= selected_years[1])
].copy()

if filtered_df.empty:
    st.warning("No data is available for the current company and year selection.")
    st.stop()

latest_year = int(filtered_df["year"].max())
summary_table = build_summary_table(filtered_df, summary_metrics or ["ROA", "Profit Margin"])
snapshot_table = build_snapshot(filtered_df)

st.title("Interactive Financial Dashboard for Beginner Investors")
st.markdown(
    """
This dashboard compares **McDonald's**, **Yum Brands**, and **Restaurant Brands International (RBI)**
using a **small set of key financial ratios**. The purpose is to answer one practical question:

**How can beginner investors use a limited number of financial indicators to compare the investment attractiveness of companies?**

The focus is on **clarity and interpretation**, not on building a complicated valuation model.
All analysis is based on annual data from **2019 to 2024** and is organized around
**profitability, growth, and financial risk**.
"""
)

intro_col1, intro_col2, intro_col3 = st.columns(3)
with intro_col1:
    st.metric("Companies in View", len(filtered_df["company"].unique()))
with intro_col2:
    st.metric("Years in View", f"{selected_years[0]}-{selected_years[1]}")
with intro_col3:
    st.metric("Latest Year Used", latest_year)

st.subheader("Data and Variables")
st.markdown(
    """
The dataset comes from **Compustat via WRDS** and includes three global fast-food companies:
**McDonald's**, **Yum Brands**, and **Restaurant Brands International**.

The raw variables used in the notebook are:
`Net Income (ni)`, `Total Assets (at)`, `Shareholders' Equity (ceq)`,
`Revenue (sale)`, and `Long-Term Debt (dltt)`.

These variables are transformed into five ratios:

- `ROA = Net Income / Total Assets`
- `ROE = Net Income / Equity`
- `Profit Margin = Net Income / Revenue`
- `Revenue Growth = (Revenue_t - Revenue_(t-1)) / Revenue_(t-1)`
- `Leverage = Long-Term Debt / Total Assets`

This keeps the dashboard consistent with the ratios you calculated in the notebook.
"""
)

st.subheader("Latest-Year Summary Table")
st.dataframe(summary_table, use_container_width=True)

st.subheader("Latest Company Snapshot")
st.dataframe(snapshot_table, use_container_width=True)

st.markdown("---")
st.header("Step 1. Profitability Analysis: ROA and Profit Margin")
st.markdown(
    """
This section compares **ROA** and **Profit Margin** to show how the three firms differ in
profitability and operating efficiency.
"""
)

profit_col1, profit_col2 = st.columns(2)
with profit_col1:
    st.pyplot(draw_line_chart(filtered_df, "ROA", "ROA Over Time", "ROA"))
with profit_col2:
    st.pyplot(draw_line_chart(filtered_df, "Profit Margin", "Profit Margin Over Time", "Profit Margin"))

st.markdown(
    """
**Structural Differences in Performance**

- **Yum Brands** consistently operates at a higher level across both ROA and Profit Margin, suggesting a structurally stronger and more mature business model.
- **Restaurant Brands International** remains at the lower end throughout the period, indicating a persistent weakness in its profitability base rather than a temporary fluctuation.
- **McDonald's** stays in the middle-to-high range, reflecting solid but not extreme overall performance.

**Profitability vs Efficiency**

- Comparing the two charts highlights a useful distinction. **McDonald's** achieves relatively high profit margins but lower ROA, implying that its asset utilization is less efficient.
- **Yum Brands** maintains leading ROA despite not always having the highest margins, indicating a stronger ability to convert assets into returns.

**Resilience and Common Trends**

- All three firms decline around 2020, which points to a shared external shock rather than a purely firm-specific problem.
- **Yum Brands** then shows a sharp rebound in 2021, suggesting resilience and a mean-reversion pattern.
- **McDonald's** also recovers strongly, while **RBI** remains at a lower level, which suggests weaker internal resilience.
"""
)

st.markdown("---")
st.header("Step 2. ROE in Context: ROE and Net Income")
st.markdown(
    """
Return on Equity (ROE) gives a quick view of returns generated from shareholders' capital.
However, to interpret ROE properly, it needs to be read together with **Net Income**.
That is especially important when equity is unusual or negative.
"""
)

roe_col1, roe_col2 = st.columns(2)
with roe_col1:
    st.pyplot(draw_line_chart(filtered_df, "ROE", "Return on Equity (ROE) Over Time", "ROE"))
with roe_col2:
    st.pyplot(draw_line_chart(filtered_df, "ni", "Net Income Over Time", "Net Income ($m)"))

st.warning(
    """
McDonald's and Yum Brands show negative ROE in several years because their equity is negative.
That does **not** mean these firms are unprofitable. In the notebook data, both companies still report positive net income.
"""
)

st.markdown(
    """
**Why Are Some ROE Values Negative?**

The negative ROE observed for **McDonald's** and **Yum Brands** is **not driven by poor profitability**.
Both firms report positive net income throughout the period. Instead, the negative ROE is mainly caused by
their **negative equity base**, likely linked to high leverage and share repurchase activity.

**Comparison Across Firms**

- **RBI** maintains a positive equity base, so its ROE is more reliable and easier to interpret.
- The negative ROE of McDonald's and Yum Brands is better understood as a **structural artifact** than as evidence of weak operations.

**Implications for Beginner Investors**

- ROE is useful as a starting point, but it should not be used in isolation.
- A better comparison combines **ROE**, **Net Income**, and **Leverage**.
- This helps separate true profitability from financial-structure effects.

**Investment Perspective**

All three firms are profitable, but their financial structures differ sharply.
McDonald's and Yum Brands generate strong earnings, yet their capital structure can distort ROE and increase financial risk.
RBI has a more interpretable ROE profile, but that does not automatically make it the strongest investment.
"""
)

st.markdown("---")
st.header("Step 3. Growth Analysis: Revenue Growth")
st.markdown(
    """
Revenue growth measures how quickly sales expand over time and helps investors judge a firm's
expansion potential. But growth is most meaningful when it is read together with profitability and efficiency.
"""
)

st.pyplot(draw_line_chart(filtered_df, "Revenue Growth", "Revenue Growth Comparison", "Revenue Growth"))

growth_tab1, growth_tab2, growth_tab3 = st.tabs(
    ["RBI: Growth Story", "McDonald's: Profitability Story", "Yum: Balanced Story"]
)

with growth_tab1:
    st.markdown(
        """
### RBI: Growth Driven by Expansion, Not Efficiency

RBI maintains positive growth from 2021 to 2024 and reaches close to 20% in 2024.
On the surface, this makes it look like the strongest growth company in the sample.

However, when this is compared with **ROA**, **profit margin**, and **net income**, the picture changes:

- Its ROA stays the lowest among the three firms.
- Its profit margin also remains the lowest.
- Net income improves, but its absolute level remains far below McDonald's.

This suggests that RBI is expanding revenue, but it is less effective at converting that growth into profit and asset returns.
Its growth therefore looks more like **scale expansion** than **high-quality efficient growth**.
"""
    )

with growth_tab2:
    st.markdown(
        """
### McDonald's: Volatile Growth with Strong Profitability

McDonald's shows the most volatile revenue-growth pattern.
If growth were the only metric, it could appear less attractive.

But the earlier charts show a different story:

- Net income remains the highest across the sample.
- Profit margin is consistently the highest.
- ROA is clearly stronger than RBI.

This means McDonald's does not depend on smooth growth to produce strong performance.
Its investment profile is **profitability-driven**: strong earnings can offset growth volatility.
"""
    )

with growth_tab3:
    st.markdown(
        """
### Yum Brands: Balanced and Sustainable Growth

Yum Brands shows moderate growth without extreme swings.
Compared with the other two firms, it appears more balanced:

- It has the highest ROA.
- Profit margin is solid and relatively stable.
- Net income grows in a steady way.

This suggests Yum is not simply chasing aggressive expansion.
Instead, it combines growth, efficiency, and profitability in a more sustainable pattern.
For beginner investors, this can look more predictable than a pure growth story.
"""
    )

st.markdown(
    """
**Main Takeaway from Revenue Growth**

Revenue growth should not be interpreted mechanically. A high growth rate can be attractive,
but it does not guarantee strong investment quality unless the company can also turn that growth
into strong margins, efficient asset use, and reliable earnings.
"""
)

st.markdown("---")
st.header("Step 4. Risk Analysis: Leverage")
st.markdown(
    """
Leverage captures the financial-risk side of the dashboard.
In this project, the analysis focuses on both:

- the **level** of leverage across years, and
- the **stability** of leverage over time.

This is where the notebook moves beyond line charts and uses a **grouped bar chart** and a **box plot**.
"""
)

risk_col1, risk_col2 = st.columns(2)
with risk_col1:
    st.pyplot(
        draw_grouped_bar_chart(
            filtered_df,
            "Leverage",
            "Leverage Ratio by Company and Year",
            "Leverage (Long-Term Debt / Total Assets)",
        )
    )
with risk_col2:
    st.pyplot(
        draw_box_plot(
            filtered_df,
            "Leverage",
            "Distribution of Leverage by Company",
            "Leverage (Long-Term Debt / Total Assets)",
        )
    )

st.markdown(
    """
The **grouped bar chart** shows the level and trend of leverage over time.
The **box plot** shows volatility and distribution:

- the median line indicates the typical leverage level,
- the height of the box indicates stability versus fluctuation,
- and the whiskers capture more extreme values.
"""
)

st.markdown(
    """
**Basic Interpretation**

Higher leverage generally implies greater financial risk because a larger share of the firm's capital structure depends on debt.
From that perspective, **Yum Brands** appears the riskiest, **RBI** the most conservative, and **McDonald's** lies in between.

However, leverage should not be assessed in isolation.
Debt becomes more concerning when the company lacks the profitability and efficiency needed to support it.

### Yum Brands: Stable operations, but debt-dependent structure

Yum Brands looks stable in growth and reasonably strong in profitability.
But its consistently high leverage suggests that some of this stability is supported by a debt-heavy capital structure.

- Interest obligations can reduce financial flexibility.
- The company may be more exposed in economic slowdowns.
- Future expansion may depend more heavily on financing conditions.

### McDonald's: Moderate leverage supported by strong fundamentals

McDonald's has more volatile growth, but its leverage remains relatively controlled.
At the same time, it also shows the strongest profitability metrics in the sample.
That makes its leverage look **manageable rather than excessive**, because strong earnings provide a buffer.

### RBI: Conservative financing, but weaker efficiency

RBI has the lowest leverage, which lowers balance-sheet risk.
But low leverage does not automatically mean the best investment.
Its weaker profitability and lower returns show that conservative financing alone does not guarantee attractiveness.
"""
)

st.markdown(
    """
**What Does Leverage Volatility Indicate?**

Leverage volatility helps investors read more than just the average debt level.
It gives clues about:

- **Capital Structure Stability**: low volatility suggests a stable financing policy, while high volatility signals more change.
- **Financing Strategy**: stable leverage looks more deliberate; fluctuating leverage may reflect changing borrowing needs.
- **Financial Risk and Uncertainty**: high leverage combined with high volatility makes the risk profile less predictable.

The box plot shows a clear structural difference:

- **Yum Brands** combines the highest leverage with the widest distribution, meaning both debt dependence and variability are high.
- **McDonald's** sits in the middle, with moderate leverage and relatively stable dispersion.
- **RBI** has the lowest leverage and the narrowest distribution, suggesting a conservative financing approach.

When combined with the earlier profitability and growth charts, the leverage analysis leads to a more nuanced conclusion:

- Yum Brands looks operationally strong, but leverage introduces hidden risk.
- McDonald's combines strong profitability with manageable leverage, giving it a more balanced profile.
- RBI looks safer on debt, but weaker on performance.

For beginner investors, the key lesson is that leverage becomes meaningful only when it is interpreted together with growth and profitability.
"""
)

st.markdown("---")
st.header("Conclusion")
st.markdown(
    """
All three companies show very different financial profiles when profitability, growth, and risk are considered together.

- **Yum Brands** demonstrates strong profitability and efficiency, but its leverage is both higher and more variable, which adds financial risk beneath otherwise stable operating performance.
- **McDonald's** presents the most balanced profile. It combines strong profitability with moderate leverage, making it a relatively stable and predictable option.
- **Restaurant Brands International** stands out for growth, but its weaker profitability means that growth alone does not make it the most attractive investment candidate.

Overall, **no single company dominates in every category**.
The broader lesson for beginner investors is that **one ratio is never enough**.
The best comparison comes from combining a small set of metrics and asking whether a company's performance is supported by genuine operating strength or by a riskier financial structure.
"""
)

if show_dataset:
    st.markdown("---")
    st.subheader("Processed Dataset")
    st.dataframe(filtered_df, use_container_width=True)
