import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Fast-Food Investor Dashboard",
    layout="wide",
)


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


df = load_data()

metric_meta = {
    "ROA": {
        "label": "ROA",
        "good": "higher",
        "as_pct": True,
        "explanation": """
**Return on Assets (ROA)** shows how efficiently a company turns its asset base into profit.
For beginner investors, a higher ROA usually signals stronger operating efficiency.
""",
        "takeaway": """
Yum Brands usually leads on ROA, which suggests strong efficiency. McDonald's is also strong,
while RBI stays lower, meaning its growth converts into profit less efficiently.
""",
    },
    "Profit Margin": {
        "label": "Profit Margin",
        "good": "higher",
        "as_pct": True,
        "explanation": """
**Profit Margin** measures how much of each dollar of revenue is kept as net income.
Higher margins often point to stronger pricing power, better cost control, or both.
""",
        "takeaway": """
McDonald's stands out for consistently high margins, which supports the idea that it has a mature,
profitability-driven business model. RBI's lower margin suggests weaker profit conversion.
""",
    },
    "ROE": {
        "label": "ROE",
        "good": "context-dependent",
        "as_pct": True,
        "explanation": """
**Return on Equity (ROE)** measures profit relative to shareholders' equity.
In this dataset, McDonald's and Yum Brands often show **negative ROE because equity is negative**,
not because profit is weak. That means ROE should be interpreted alongside net income and leverage.
""",
        "takeaway": """
RBI's ROE is easier to interpret because its equity stays positive. For McDonald's and Yum Brands,
ROE alone can mislead beginners because capital structure distorts the ratio.
""",
    },
    "Revenue Growth": {
        "label": "Revenue Growth",
        "good": "higher",
        "as_pct": True,
        "explanation": """
**Revenue Growth** tracks how quickly sales increase from one year to the next.
It is useful for spotting expansion potential, but strong growth is more convincing when it is supported by profitability.
""",
        "takeaway": """
RBI shows the strongest recent growth, but its lower ROA and margins suggest that not all growth is high quality.
Yum looks more balanced, while McDonald's combines uneven growth with very strong profits.
""",
    },
    "Leverage": {
        "label": "Leverage",
        "good": "lower",
        "as_pct": False,
        "explanation": """
**Leverage** here is measured as long-term debt divided by total assets.
Higher leverage can support growth, but it also raises financial risk because the company depends more on debt financing.
""",
        "takeaway": """
Yum Brands looks most debt-dependent, RBI most conservative, and McDonald's sits in the middle.
For beginners, the key idea is that debt risk should be judged together with profitability, not by itself.
""",
    },
}

company_colors = {
    "McDonald's": "#d62828",
    "Yum Brands": "#1d3557",
    "Restaurant Brands International": "#2a9d8f",
}


def format_value(metric: str, value: float) -> str:
    if pd.isna(value):
        return "N/A"
    if metric_meta[metric]["as_pct"]:
        return f"{value:.1%}"
    return f"{value:.2f}"


def leader_text(summary_df: pd.DataFrame, metric: str) -> str:
    valid = summary_df.dropna(subset=["mean"])
    if valid.empty:
        return "Not enough data to compare the selected metric."
    ascending = metric_meta[metric]["good"] == "lower"
    leader = valid.sort_values("mean", ascending=ascending).iloc[0]
    if metric == "ROE":
        return (
            "ROE needs extra caution here: RBI is the cleanest comparison because its equity is positive, "
            "while McDonald's and Yum Brands have negative equity that makes ROE less intuitive."
        )
    return (
        f"Based on the average selected-period {metric}, **{leader['company']}** looks strongest "
        f"for this metric at **{format_value(metric, leader['mean'])}**."
    )


def company_snapshot(filtered_df: pd.DataFrame) -> pd.DataFrame:
    latest_year = int(filtered_df["year"].max())
    latest = filtered_df[filtered_df["year"] == latest_year].copy()
    latest = latest[["company", "ROA", "Profit Margin", "Revenue Growth", "Leverage", "ni"]]
    latest = latest.rename(columns={"ni": "Net Income"})
    return latest.sort_values("company")


st.title("Fast-Food Financial Dashboard for Beginner Investors")
st.markdown(
    """
This interactive dashboard compares **McDonald's**, **Yum Brands**, and
**Restaurant Brands International (RBI)** using a small set of key financial indicators.
The goal is to help **beginner investors** compare profitability, growth, and financial risk
without getting lost in too many metrics.

The data covers **2019 to 2024** and focuses on five ratios used in your notebook analysis:
`ROA`, `ROE`, `Profit Margin`, `Revenue Growth`, and `Leverage`.
"""
)

st.sidebar.header("Dashboard Controls")
selected_metric = st.sidebar.selectbox("Choose a metric", list(metric_meta.keys()))
selected_companies = st.sidebar.multiselect(
    "Choose companies",
    options=df["company"].unique().tolist(),
    default=df["company"].unique().tolist(),
)
year_range = st.sidebar.slider(
    "Choose year range",
    min_value=int(df["year"].min()),
    max_value=int(df["year"].max()),
    value=(int(df["year"].min()), int(df["year"].max())),
)

filtered_df = df[
    (df["company"].isin(selected_companies))
    & (df["year"].between(year_range[0], year_range[1]))
].copy()

if filtered_df.empty:
    st.warning("No data is available for the current filter selection.")
    st.stop()

summary = (
    filtered_df.groupby("company")[selected_metric]
    .agg(["mean", "median", "min", "max", "std"])
    .reset_index()
)

latest_year = int(filtered_df["year"].max())
latest_values = filtered_df[filtered_df["year"] == latest_year][["company", selected_metric]].copy()
latest_values = latest_values.sort_values(selected_metric, ascending=metric_meta[selected_metric]["good"] == "lower")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Companies Selected", len(selected_companies))
with col2:
    st.metric("Metric", selected_metric)
with col3:
    st.metric("Latest Year in View", latest_year)

st.subheader(f"What Does {selected_metric} Tell Investors?")
st.markdown(metric_meta[selected_metric]["explanation"])

insight_col, leader_col = st.columns([1.2, 1])
with insight_col:
    st.info(metric_meta[selected_metric]["takeaway"])
with leader_col:
    st.success(leader_text(summary, selected_metric))

st.subheader(f"{selected_metric} Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
for company in selected_companies:
    company_df = filtered_df[filtered_df["company"] == company]
    ax.plot(
        company_df["year"],
        company_df[selected_metric],
        marker="o",
        linewidth=2.5,
        label=company,
        color=company_colors.get(company),
    )

if selected_metric == "Revenue Growth":
    ax.axhline(0, linestyle="--", linewidth=1, color="gray")

ax.set_xlabel("Year")
ax.set_ylabel(selected_metric)
ax.set_title(f"{selected_metric} Comparison by Company")
ax.grid(alpha=0.3)
ax.legend()
st.pyplot(fig)

st.subheader(f"{latest_year} Cross-Section Comparison")
fig_bar, ax_bar = plt.subplots(figsize=(10, 5))
bars = ax_bar.bar(
    latest_values["company"],
    latest_values[selected_metric],
    color=[company_colors.get(company) for company in latest_values["company"]],
)
ax_bar.set_title(f"{selected_metric} in {latest_year}")
ax_bar.set_ylabel(selected_metric)
ax_bar.grid(axis="y", alpha=0.3)
ax_bar.tick_params(axis="x", rotation=10)

for bar, value in zip(bars, latest_values[selected_metric]):
    text_y = value if value >= 0 else value - abs(value) * 0.08
    vertical_align = "bottom" if value >= 0 else "top"
    ax_bar.text(
        bar.get_x() + bar.get_width() / 2,
        text_y,
        format_value(selected_metric, value),
        ha="center",
        va=vertical_align,
        fontsize=9,
    )

st.pyplot(fig_bar)

st.subheader(f"Distribution and Volatility of {selected_metric}")
fig_box, ax_box = plt.subplots(figsize=(9, 5))
box_data = [
    filtered_df[filtered_df["company"] == company][selected_metric].dropna()
    for company in selected_companies
]
box = ax_box.boxplot(box_data, labels=selected_companies, patch_artist=True)
for patch, company in zip(box["boxes"], selected_companies):
    patch.set_facecolor(company_colors.get(company, "#cccccc"))
    patch.set_alpha(0.65)
ax_box.set_title(f"Box Plot of {selected_metric}")
ax_box.set_ylabel(selected_metric)
ax_box.grid(alpha=0.3)
ax_box.tick_params(axis="x", rotation=10)
st.pyplot(fig_box)

st.markdown(
    """
The **box plot** helps beginner investors judge how stable each company's performance is over time.
A narrower box usually means more consistency, while a wider box suggests greater fluctuation and uncertainty.
"""
)

st.subheader("Summary Table")
summary_display = summary.copy()
for column in ["mean", "median", "min", "max", "std"]:
    summary_display[column] = summary_display[column].apply(lambda x: format_value(selected_metric, x))
st.dataframe(summary_display, use_container_width=True)

st.subheader("Latest Company Snapshot")
snapshot = company_snapshot(filtered_df).copy()
for col in ["ROA", "Profit Margin", "Revenue Growth"]:
    snapshot[col] = snapshot[col].apply(lambda x: "N/A" if pd.isna(x) else f"{x:.1%}")
snapshot["Leverage"] = snapshot["Leverage"].apply(lambda x: f"{x:.2f}")
snapshot["Net Income"] = snapshot["Net Income"].apply(lambda x: f"${x:,.0f}m")
st.dataframe(snapshot, use_container_width=True)

st.subheader("Interpretation for Beginner Investors")
if selected_metric == "ROA":
    st.markdown(
        """
Yum Brands generally looks strongest on efficiency, McDonald's remains solid, and RBI trails behind.
For a beginner investor, this suggests Yum and McDonald's are better at turning resources into profit.
"""
    )
elif selected_metric == "Profit Margin":
    st.markdown(
        """
McDonald's usually leads on margin, which means it keeps more profit from each dollar of sales.
That makes its performance easier to defend even when revenue growth is not the most stable.
"""
    )
elif selected_metric == "ROE":
    st.markdown(
        """
ROE is useful, but here it can be misleading because McDonald's and Yum Brands have negative equity.
The safer lesson is to treat ROE as a starting point, then check net income and leverage before drawing conclusions.
"""
    )
elif selected_metric == "Revenue Growth":
    st.markdown(
        """
RBI offers the strongest growth story, but growth alone does not make it the best investment candidate.
Your notebook's key insight still holds: growth should be judged together with profitability and efficiency.
"""
    )
else:
    st.markdown(
        """
Leverage adds the risk dimension to the dashboard. Lower debt exposure is safer, but the best company is not always
the one with the lowest leverage; it is the one that balances debt, profitability, and growth most effectively.
"""
    )

st.subheader("Overall Conclusion")
st.markdown(
    """
Across the three companies, **no single firm dominates every dimension**.
**McDonald's** looks the most balanced overall, with strong profitability and manageable leverage.
**Yum Brands** appears efficient and relatively consistent, but it depends more heavily on debt.
**RBI** delivers stronger recent growth, yet its profitability remains weaker, which makes its growth quality less convincing.

For beginner investors, the main lesson is simple: **do not rely on just one ratio**.
Comparing profitability, growth, and risk together produces a much more reliable investment story.
"""
)

with st.expander("View Processed Dataset"):
    display_df = filtered_df.copy()
    st.dataframe(display_df, use_container_width=True)
