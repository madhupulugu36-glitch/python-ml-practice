
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Prepare dates
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")

df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Metal columns
metals = {
    "Gold 999": "Gold_999_PM_Rs_per_10g",
    "Platinum 999": "Platinum_999_PM_Rs_per_10g"
}

# Calculate monthly standard deviation
monthly = (
    df.groupby("Month")
    .agg({
        "Gold_999_PM_Rs_per_10g": "std",
        "Platinum_999_PM_Rs_per_10g": "std"
    })
    .reset_index()
)

# Rename columns
monthly.rename(
    columns={
        "Gold_999_PM_Rs_per_10g": "Gold Volatility",
        "Platinum_999_PM_Rs_per_10g": "Platinum Volatility"
    },
    inplace=True
)

print("\nMONTHLY PRICE STABILITY RANKING")
print("=" * 65)

fig = go.Figure()

volatility_columns = {
    "Gold 999": "Gold Volatility",
    "Platinum 999": "Platinum Volatility"
}

for metal, column in volatility_columns.items():

    # Lower volatility means higher stability
    monthly[f"{metal} Rank"] = (
        monthly[column]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    # Print ranking
    ranked = monthly.sort_values(
        column,
        ascending=True
    )

    print(f"\n{metal}")
    print("-" * 45)

    for _, row in ranked.iterrows():

        rank = row[f"{metal} Rank"]

        if rank == 1:
            status = "Most Stable"
        elif rank == len(monthly):
            status = "Most Volatile"
        else:
            status = "Stable Rank"

        print(
            f"Rank {rank} | {row['Month']} | "
            f"Standard Deviation: ₹{row[column]:,.2f} | "
            f"{status}"
        )

    # Prepare hover details
    customdata = []

    for _, row in monthly.iterrows():
        rank = row[f"{metal} Rank"]

        if rank == 1:
            status = "Most Stable Month"
        elif rank == len(monthly):
            status = "Most Volatile Month"
        else:
            status = "Stable Rank"

        customdata.append([rank, status])

    # Add chart
    fig.add_trace(
        go.Bar(
            x=monthly["Month"],
            y=monthly[column],
            name=metal,
            customdata=customdata,
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Metal: " + metal + "<br>"
                "Standard Deviation: ₹%{y:,.2f}<br>"
                "Stability Rank: #%{customdata[0]}<br>"
                "Status: %{customdata[1]}"
                "<extra></extra>"
            )
        )
    )

fig.update_layout(
    title="Gold vs Platinum - Monthly Stability Ranking",
    xaxis_title="Month",
    yaxis_title="Price Volatility (₹ per 10 grams)",
    barmode="group",
    template="plotly_white",
    height=650,
    hovermode="closest"
)

fig.show()

print("\nMonthly stability ranking completed!")