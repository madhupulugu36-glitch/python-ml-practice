
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Prepare dates
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")

# Create monthly average prices
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

fig = go.Figure()

print("\nMonthly Purchase Season Ranking")
print("=" * 65)

for metal, column in metals.items():

    # Rank months by average price
    monthly[f"{metal}_Rank"] = (
        monthly[column]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    # First available month becomes the base index (100)
    base_price = monthly[column].iloc[0]

    monthly[f"{metal}_Index"] = (
        monthly[column] / base_price
    ) * 100

    # Prepare hover details
    customdata = []

    for _, row in monthly.iterrows():

        rank = row[f"{metal}_Rank"]
        price = row[column]

        if rank == 1:
            opportunity = "Best observed buying opportunity"
        else:
            opportunity = f"Purchase rank: {rank}"

        customdata.append([
            price,
            rank,
            opportunity
        ])

    # Add chart bars
    fig.add_trace(
        go.Bar(
            x=monthly["Month"],
            y=monthly[f"{metal}_Index"],
            name=metal,
            customdata=customdata,
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Metal: " + metal + "<br>"
                "Average Price: ₹%{customdata[0]:,.2f}<br>"
                "Season Rank: #%{customdata[1]}<br>"
                "Buying Opportunity: %{customdata[2]}<br>"
                "Price Index: %{y:.2f}"
                "<extra></extra>"
            )
        )
    )

    print(f"\n{metal}")
    print("-" * 40)

    for _, row in monthly.iterrows():
        print(
            f"{row['Month']} | "
            f"Average Price: ₹{row[column]:,.2f} | "
            f"Purchase Rank: #{row[f'{metal}_Rank']}"
        )

# Chart layout
fig.update_layout(
    title="Gold vs Platinum - Monthly Purchase Season Ranking",
    xaxis_title="Month",
    yaxis_title="Price Index (First Month = 100)",
    barmode="group",
    template="plotly_white",
    hovermode="closest",
    height=650
)

fig.show()

print("\nMonthly purchase season ranking completed!")