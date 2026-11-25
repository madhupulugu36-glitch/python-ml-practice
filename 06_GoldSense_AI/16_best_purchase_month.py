
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Prepare dates
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")
df["Month"] = df["Date"].dt.to_period("M").astype(str)

metals = {
    "Gold 999": "Gold_999_PM_Rs_per_10g",
    "Platinum 999": "Platinum_999_PM_Rs_per_10g"
}

print("\nBEST HISTORICAL PURCHASE MONTH ANALYSIS")
print("=" * 70)

fig = go.Figure()

for metal, column in metals.items():

    # Calculate monthly average price and volatility
    monthly = (
        df.groupby("Month")[column]
        .agg(["mean", "std"])
        .reset_index()
    )

    monthly.rename(
        columns={
            "mean": "Average Price",
            "std": "Volatility"
        },
        inplace=True
    )

    # Rank lower price and lower volatility first
    monthly["Price Rank"] = (
        monthly["Average Price"]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    monthly["Stability Rank"] = (
        monthly["Volatility"]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    # Combined score
    monthly["Combined Score"] = (
        monthly["Price Rank"] +
        monthly["Stability Rank"]
    )

    monthly["Recommendation Rank"] = (
        monthly["Combined Score"]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    # Sort by recommendation rank
    monthly = monthly.sort_values(
        ["Combined Score", "Average Price"]
    )

    print(f"\n{metal}")
    print("-" * 55)

    print(
        monthly[
            [
                "Month",
                "Average Price",
                "Volatility",
                "Price Rank",
                "Stability Rank",
                "Combined Score",
                "Recommendation Rank"
            ]
        ].to_string(
            index=False,
            formatters={
                "Average Price": "₹{:,.2f}".format,
                "Volatility": "₹{:,.2f}".format
            }
        )
    )

    best = monthly.iloc[0]

    print("\nBest historical purchase opportunity:")
    print(f"Month: {best['Month']}")
    print(f"Average Price: ₹{best['Average Price']:,.2f}")
    print(f"Price Rank: {best['Price Rank']}")
    print(f"Stability Rank: {best['Stability Rank']}")
    print(f"Combined Score: {best['Combined Score']}")

    # Add chart
    fig.add_trace(
        go.Bar(
            x=monthly["Month"],
            y=monthly["Combined Score"],
            name=metal,
            customdata=monthly[
                [
                    "Average Price",
                    "Volatility",
                    "Price Rank",
                    "Stability Rank",
                    "Recommendation Rank"
                ]
            ].values,
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Metal: " + metal + "<br>"
                "Combined Score: %{y}<br>"
                "Average Price: ₹%{customdata[0]:,.2f}<br>"
                "Volatility: ₹%{customdata[1]:,.2f}<br>"
                "Price Rank: #%{customdata[2]}<br>"
                "Stability Rank: #%{customdata[3]}<br>"
                "Recommendation Rank: #%{customdata[4]}"
                "<extra></extra>"
            )
        )
    )

fig.update_layout(
    title="Best Purchase Month - Combined Price and Stability Ranking",
    xaxis_title="Month",
    yaxis_title="Combined Score (Lower is Better)",
    barmode="group",
    template="plotly_white",
    height=650,
    hovermode="closest"
)

fig.show()

print("\nBest purchase month analysis completed!")