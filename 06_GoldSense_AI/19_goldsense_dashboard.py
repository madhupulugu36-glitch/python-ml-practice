
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# GOLDSENSE AI - GOLD vs PLATINUM ANALYSIS DASHBOARD
# ==========================================================

st.set_page_config(
    page_title="GoldSense AI",
    page_icon="🥇",
    layout="wide"
)

DATA_PATH = "data/gold_platinum_daily_comparison.csv"

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    return df

df = load_data()

# ==========================================================
# PREPARE MONTHLY ANALYSIS
# ==========================================================

monthly = df.copy()

monthly["Month"] = monthly["Date"].dt.to_period("M").astype(str)

monthly_data = monthly.groupby("Month").agg(
    Gold_Avg=("Gold_999_PM_Rs_per_10g", "mean"),
    Gold_Volatility=("Gold_999_PM_Rs_per_10g", "std"),
    Platinum_Avg=("Platinum_999_PM_Rs_per_10g", "mean"),
    Platinum_Volatility=("Platinum_999_PM_Rs_per_10g", "std"),
    Records=("Date", "count")
).reset_index()

monthly_data["Gold_Price_Rank"] = (
    monthly_data["Gold_Avg"].rank(method="min").astype(int)
)

monthly_data["Gold_Stability_Rank"] = (
    monthly_data["Gold_Volatility"].rank(method="min").astype(int)
)

monthly_data["Platinum_Price_Rank"] = (
    monthly_data["Platinum_Avg"].rank(method="min").astype(int)
)

monthly_data["Platinum_Stability_Rank"] = (
    monthly_data["Platinum_Volatility"].rank(method="min").astype(int)
)

monthly_data["Gold_Recommendation_Score"] = (
    monthly_data["Gold_Price_Rank"]
    + monthly_data["Gold_Stability_Rank"]
)

monthly_data["Platinum_Recommendation_Score"] = (
    monthly_data["Platinum_Price_Rank"]
    + monthly_data["Platinum_Stability_Rank"]
)

monthly_data["Gold_Recommendation_Rank"] = (
    monthly_data["Gold_Recommendation_Score"]
    .rank(method="min").astype(int)
)

monthly_data["Platinum_Recommendation_Rank"] = (
    monthly_data["Platinum_Recommendation_Score"]
    .rank(method="min").astype(int)
)

# ==========================================================
# BUYING SIGNALS
# ==========================================================

def buying_signal(price_rank, stability_rank):
    if price_rank <= 2 and stability_rank <= 2:
        return "Strong Buying Opportunity"
    elif price_rank <= 2:
        return "Buying Opportunity"
    elif stability_rank <= 2:
        return "Monitor - Stable Price"
    else:
        return "Caution"

monthly_data["Gold_Buying_Signal"] = monthly_data.apply(
    lambda row: buying_signal(
        row["Gold_Price_Rank"],
        row["Gold_Stability_Rank"]
    ),
    axis=1
)

monthly_data["Platinum_Buying_Signal"] = monthly_data.apply(
    lambda row: buying_signal(
        row["Platinum_Price_Rank"],
        row["Platinum_Stability_Rank"]
    ),
    axis=1
)

# ==========================================================
# HEADER
# ==========================================================

st.title("🥇 GoldSense AI")
st.subheader("Gold vs Platinum | Purchase Price & What-If Analysis")

st.markdown(
    """
    **Objective:** Analyze historical Gold 999 and Platinum 999 prices,
    understand monthly price behavior, identify purchase opportunities,
    and explore hypothetical buying scenarios.
    """
)

st.caption(
    "Analysis is based on the currently available dataset. "
    "Historical patterns are not guaranteed to repeat."
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("Dashboard Controls")

metal = st.sidebar.selectbox(
    "Select Metal",
    ["Gold 999", "Platinum 999"]
)

if metal == "Gold 999":
    price_col = "Gold_999_PM_Rs_per_10g"
    avg_col = "Gold_Avg"
    volatility_col = "Gold_Volatility"
    price_rank_col = "Gold_Price_Rank"
    stability_rank_col = "Gold_Stability_Rank"
    recommendation_rank_col = "Gold_Recommendation_Rank"
    signal_col = "Gold_Buying_Signal"
else:
    price_col = "Platinum_999_PM_Rs_per_10g"
    avg_col = "Platinum_Avg"
    volatility_col = "Platinum_Volatility"
    price_rank_col = "Platinum_Price_Rank"
    stability_rank_col = "Platinum_Stability_Rank"
    recommendation_rank_col = "Platinum_Recommendation_Rank"
    signal_col = "Platinum_Buying_Signal"

selected_data = df[["Date", price_col]].copy()

# ==========================================================
# KEY METRICS
# ==========================================================

latest_price = selected_data.iloc[-1][price_col]
first_price = selected_data.iloc[0][price_col]
highest_price = selected_data[price_col].max()
lowest_price = selected_data[price_col].min()

price_change = latest_price - first_price

if first_price != 0:
    price_change_percent = (price_change / first_price) * 100
else:
    price_change_percent = 0

total_records = len(df)
start_date = df["Date"].min().strftime("%d %b %Y")
end_date = df["Date"].max().strftime("%d %b %Y")

# ==========================================================
# TOP METRIC CARDS
# ==========================================================

st.markdown("### 📊 Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Latest Price (per 10g)",
    f"₹{latest_price:,.2f}"
)

col2.metric(
    "Dataset Price Change",
    f"₹{price_change:,.2f}",
    f"{price_change_percent:.2f}%"
)

col3.metric(
    "Highest Recorded Price",
    f"₹{highest_price:,.2f}"
)

col4.metric(
    "Lowest Recorded Price",
    f"₹{lowest_price:,.2f}"
)

st.info(
    f"Dataset period: {start_date} to {end_date} | "
    f"Total records: {total_records}"
)

# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Price Trends",
    "📅 Monthly Analysis",
    "💰 What-If Analysis",
    "🎯 Purchase Strategy",
    "📋 Dataset"
])

# ==========================================================
# TAB 1 - PRICE TRENDS
# ==========================================================

with tab1:

    st.markdown("### Historical Daily Price Trend")

    trend_fig = go.Figure()

    trend_fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["Gold_999_PM_Rs_per_10g"],
            name="Gold 999",
            mode="lines",
            line=dict(width=2)
        )
    )

    trend_fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["Platinum_999_PM_Rs_per_10g"],
            name="Platinum 999",
            mode="lines",
            line=dict(width=2)
        )
    )

    trend_fig.update_layout(
        title="Gold vs Platinum Daily Price",
        xaxis_title="Date",
        yaxis_title="Price (₹ per 10 grams)",
        hovermode="x unified",
        template="plotly_white",
        height=550
    )

    st.plotly_chart(trend_fig, use_container_width=True)

    st.markdown("### Selected Metal Price Movement")

    individual_fig = px.line(
        selected_data,
        x="Date",
        y=price_col,
        title=f"{metal} Daily Price",
        markers=True
    )

    individual_fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price (₹ per 10 grams)",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(individual_fig, use_container_width=True)

# ==========================================================
# TAB 2 - MONTHLY ANALYSIS
# ==========================================================

with tab2:

    st.markdown("### Monthly Average Price")

    gold_monthly_fig = px.bar(
        monthly_data,
        x="Month",
        y="Gold_Avg",
        title="Gold 999 Monthly Average Price",
        hover_data=[
            "Gold_Price_Rank",
            "Gold_Stability_Rank",
            "Gold_Recommendation_Rank",
            "Gold_Buying_Signal"
        ]
    )

    gold_monthly_fig.update_layout(
        yaxis_title="Price (₹ per 10 grams)",
        template="plotly_white"
    )

    st.plotly_chart(gold_monthly_fig, use_container_width=True)

    platinum_monthly_fig = px.bar(
        monthly_data,
        x="Month",
        y="Platinum_Avg",
        title="Platinum 999 Monthly Average Price",
        hover_data=[
            "Platinum_Price_Rank",
            "Platinum_Stability_Rank",
            "Platinum_Recommendation_Rank",
            "Platinum_Buying_Signal"
        ]
    )

    platinum_monthly_fig.update_layout(
        yaxis_title="Price (₹ per 10 grams)",
        template="plotly_white"
    )

    st.plotly_chart(platinum_monthly_fig, use_container_width=True)

    st.markdown("### Monthly Price & Stability Ranking")

    display_monthly = monthly_data.copy()

    display_monthly = display_monthly.rename(columns={
        "Month": "Month",
        "Gold_Avg": "Gold Average Price",
        "Gold_Volatility": "Gold Volatility",
        "Gold_Price_Rank": "Gold Price Rank",
        "Gold_Stability_Rank": "Gold Stability Rank",
        "Gold_Recommendation_Rank": "Gold Recommendation Rank",
        "Gold_Buying_Signal": "Gold Buying Signal",
        "Platinum_Avg": "Platinum Average Price",
        "Platinum_Volatility": "Platinum Volatility",
        "Platinum_Price_Rank": "Platinum Price Rank",
        "Platinum_Stability_Rank": "Platinum Stability Rank",
        "Platinum_Recommendation_Rank": "Platinum Recommendation Rank",
        "Platinum_Buying_Signal": "Platinum Buying Signal"
    })

    st.dataframe(
        display_monthly,
        use_container_width=True,
        hide_index=True
    )

# ==========================================================
# TAB 3 - WHAT-IF ANALYSIS
# ==========================================================

with tab3:

    st.markdown("### Quantity-Based Purchase Analysis")

    quantity = st.slider(
        "Purchase Quantity (grams)",
        min_value=1,
        max_value=1000,
        value=10,
        step=1
    )

    monthly_prices = monthly_data[avg_col]

    cheapest_month = monthly_data.loc[
        monthly_prices.idxmin()
    ]

    expensive_month = monthly_data.loc[
        monthly_prices.idxmax()
    ]

    cheapest_price_per_10g = cheapest_month[avg_col]
    expensive_price_per_10g = expensive_month[avg_col]

    cheapest_cost = cheapest_price_per_10g * quantity / 10
    expensive_cost = expensive_price_per_10g * quantity / 10

    potential_savings = expensive_cost - cheapest_cost

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Cheapest Historical Month",
        cheapest_month["Month"]
    )

    col2.metric(
        "Potential Savings",
        f"₹{potential_savings:,.2f}"
    )

    col3.metric(
        "Quantity",
        f"{quantity} grams"
    )

    comparison_df = pd.DataFrame({
        "Scenario": [
            f"Cheapest Month ({cheapest_month['Month']})",
            f"Highest Price Month ({expensive_month['Month']})"
        ],
        "Purchase Cost": [
            cheapest_cost,
            expensive_cost
        ]
    })

    cost_fig = px.bar(
        comparison_df,
        x="Scenario",
        y="Purchase Cost",
        text_auto=".2f",
        title=f"{metal} - What-If Purchase Cost for {quantity}g"
    )

    cost_fig.update_layout(
        yaxis_title="Purchase Cost (₹)",
        template="plotly_white"
    )

    st.plotly_chart(cost_fig, use_container_width=True)

    st.markdown(
        f"""
        **What-If Result**

        - Cheapest month: **{cheapest_month['Month']}**
        - Cheapest monthly average: **₹{cheapest_price_per_10g:,.2f} per 10g**
        - Highest monthly average: **₹{expensive_price_per_10g:,.2f} per 10g**
        - Estimated difference for **{quantity}g**: **₹{potential_savings:,.2f}**
        """
    )

    st.warning(
        "This is a historical comparison, not a guaranteed future saving."
    )

    st.markdown("### Interactive Price Change Simulator")

    current_price = latest_price

    scenario_percentage = st.slider(
        "Hypothetical Price Change (%)",
        min_value=-50,
        max_value=50,
        value=0,
        step=1
    )

    scenario_price = current_price * (
        1 + scenario_percentage / 100
    )

    current_cost = current_price * quantity / 10
    scenario_cost = scenario_price * quantity / 10

    scenario_difference = scenario_cost - current_cost

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Current Price per 10g",
        f"₹{current_price:,.2f}"
    )

    col2.metric(
        "Scenario Price per 10g",
        f"₹{scenario_price:,.2f}",
        f"{scenario_percentage}%"
    )

    col3.metric(
        "Scenario Cost Difference",
        f"₹{scenario_difference:,.2f}"
    )

    scenario_range = [-10, -5, 0, 5, 10]

    scenario_data = []

    for pct in scenario_range:

        hypothetical_price = current_price * (1 + pct / 100)

        hypothetical_cost = hypothetical_price * quantity / 10

        scenario_data.append({
            "Price Change (%)": pct,
            "Price per 10g": hypothetical_price,
            "Purchase Cost": hypothetical_cost
        })

    scenario_df = pd.DataFrame(scenario_data)

    scenario_fig = px.line(
        scenario_df,
        x="Price Change (%)",
        y="Purchase Cost",
        markers=True,
        title=f"What-If Scenario for {quantity}g of {metal}"
    )

    scenario_fig.update_layout(
        template="plotly_white",
        yaxis_title="Purchase Cost (₹)"
    )

    st.plotly_chart(scenario_fig, use_container_width=True)

# ==========================================================
# TAB 4 - PURCHASE STRATEGY
# ==========================================================

with tab4:

    st.markdown("### Historical Purchase Strategy")

    strategy_data = monthly_data[[
        "Month",
        avg_col,
        volatility_col,
        price_rank_col,
        stability_rank_col,
        recommendation_rank_col,
        signal_col
    ]].copy()

    strategy_data.columns = [
        "Month",
        "Average Price",
        "Volatility",
        "Price Rank",
        "Stability Rank",
        "Recommendation Rank",
        "Buying Signal"
    ]

    strategy_data = strategy_data.sort_values(
        "Recommendation Rank"
    )

    st.dataframe(
        strategy_data,
        use_container_width=True,
        hide_index=True
    )

    best_month = strategy_data.iloc[0]

    st.success(
        f"Best historical combined recommendation for {metal}: "
        f"{best_month['Month']} "
        f"(Recommendation Rank: {best_month['Recommendation Rank']})"
    )

    st.markdown("### Buying Signal Explanation")

    st.markdown("""
    - **Strong Buying Opportunity:** Low price rank and high stability rank.
    - **Buying Opportunity:** Historically low monthly price.
    - **Monitor - Stable Price:** Historically stable price, but not among the cheapest.
    - **Caution:** Price and stability rankings are not favorable.
    """)

    st.info(
        "Signals are generated using historical price and volatility rankings. "
        "They are analytical indicators, not predictions."
    )

# ==========================================================
# TAB 5 - DATASET
# ==========================================================

with tab5:

    st.markdown("### Gold-Platinum Comparison Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Download Dataset")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Comparison CSV",
        data=csv_data,
        file_name="gold_platinum_daily_comparison.csv",
        mime="text/csv"
    )

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "GoldSense AI | Historical Gold 999 and Platinum 999 "
    "Purchase Price Analysis | Python + Pandas + Plotly + Streamlit"
)