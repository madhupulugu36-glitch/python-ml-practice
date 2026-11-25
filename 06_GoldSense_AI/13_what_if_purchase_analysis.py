
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Prepare dates
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")

# Calculate monthly average prices
df["Month"] = df["Date"].dt.to_period("M")

monthly = (
    df.groupby("Month")
    .agg({
        "Gold_999_PM_Rs_per_10g": "mean",
        "Platinum_999_PM_Rs_per_10g": "mean"
    })
    .reset_index()
)

monthly["Month"] = monthly["Month"].astype(str)

metals = {
    "Gold 999": "Gold_999_PM_Rs_per_10g",
    "Platinum 999": "Platinum_999_PM_Rs_per_10g"
}

results = []

print("\nWHAT-IF PURCHASE ANALYSIS")
print("=" * 65)

for metal, column in metals.items():

    # Find lowest and highest average-price months
    lowest_row = monthly.loc[monthly[column].idxmin()]
    highest_row = monthly.loc[monthly[column].idxmax()]

    lowest_price = lowest_row[column]
    highest_price = highest_row[column]

    lowest_month = lowest_row["Month"]
    highest_month = highest_row["Month"]

    # Calculate potential savings per 10 grams
    savings = highest_price - lowest_price

    savings_percentage = (
        savings / highest_price
    ) * 100

    results.append({
        "Metal": metal,
        "Lowest Month": lowest_month,
        "Lowest Price": lowest_price,
        "Highest Month": highest_month,
        "Highest Price": highest_price,
        "Potential Savings": savings,
        "Savings Percentage": savings_percentage
    })

    print(f"\n{metal}")
    print("-" * 45)

    print(
        f"Lowest-price month: {lowest_month} "
        f"(₹{lowest_price:,.2f})"
    )

    print(
        f"Highest-price month: {highest_month} "
        f"(₹{highest_price:,.2f})"
    )

    print(f"Potential savings per 10g: ₹{savings:,.2f}")
    print(f"Potential savings percentage: {savings_percentage:.2f}%")

# Create results DataFrame
summary = pd.DataFrame(results)

# Interactive What-If chart
customdata = summary[
    [
        "Lowest Month",
        "Lowest Price",
        "Highest Month",
        "Highest Price",
        "Potential Savings"
    ]
].values

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=summary["Metal"],
        y=summary["Savings Percentage"],
        text=[
            f"{value:.2f}%"
            for value in summary["Savings Percentage"]
        ],
        textposition="outside",
        customdata=customdata,
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Potential Savings: %{y:.2f}%<br>"
            "Lowest-price month: %{customdata[0]}<br>"
            "Lowest average price: ₹%{customdata[1]:,.2f}<br>"
            "Highest-price month: %{customdata[2]}<br>"
            "Highest average price: ₹%{customdata[3]:,.2f}<br>"
            "Savings per 10g: ₹%{customdata[4]:,.2f}"
            "<extra></extra>"
        )
    )
)

fig.update_layout(
    title="What-If Analysis - Potential Purchase Savings",
    xaxis_title="Metal",
    yaxis_title="Potential Savings (%)",
    template="plotly_white",
    height=600,
    hovermode="closest"
)

fig.show()

print("\nWhat-If purchase analysis completed!")