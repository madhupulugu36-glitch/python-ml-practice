
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Prepare data
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")
df["Month"] = df["Date"].dt.to_period("M").astype(str)

metals = {
    "Gold 999": "Gold_999_PM_Rs_per_10g",
    "Platinum 999": "Platinum_999_PM_Rs_per_10g"
}

print("\nSEASONALITY-BASED PURCHASE STRATEGY")
print("=" * 75)

fig = go.Figure()

for metal, column in metals.items():

    # Monthly price and volatility
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

    # Rank price: cheapest month gets Rank 1
    monthly["Price Rank"] = (
        monthly["Average Price"]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    # Rank stability: most stable month gets Rank 1
    monthly["Stability Rank"] = (
        monthly["Volatility"]
        .rank(method="min", ascending=True)
        .astype(int)
    )

    # Generate buying signal
    def generate_signal(row):

        if (
            row["Price Rank"] <= 2
            and row["Stability Rank"] <= 2
        ):
            return "Strong Buying Opportunity"

        elif row["Price Rank"] <= 2:
            return "Buying Opportunity"

        elif row["Stability Rank"] <= 2:
            return "Monitor - Stable Price"

        else:
            return "Caution"

    monthly["Buying Signal"] = monthly.apply(
        generate_signal,
        axis=1
    )

    # Display results
    print(f"\n{metal}")
    print("-" * 65)

    print(
        monthly[
            [
                "Month",
                "Average Price",
                "Volatility",
                "Price Rank",
                "Stability Rank",
                "Buying Signal"
            ]
        ].to_string(
            index=False,
            formatters={
                "Average Price": "₹{:,.2f}".format,
                "Volatility": "₹{:,.2f}".format
            }
        )
    )

    # Hover details
    customdata = monthly[
        [
            "Volatility",
            "Price Rank",
            "Stability Rank",
            "Buying Signal"
        ]
    ].values

    # Add chart
    fig.add_trace(
        go.Bar(
            x=monthly["Month"],
            y=monthly["Average Price"],
            name=metal,
            customdata=customdata,
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Metal: " + metal + "<br>"
                "Average Price: ₹%{y:,.2f}<br>"
                "Volatility: ₹%{customdata[0]:,.2f}<br>"
                "Price Rank: #%{customdata[1]}<br>"
                "Stability Rank: #%{customdata[2]}<br>"
                "Buying Signal: %{customdata[3]}"
                "<extra></extra>"
            )
        )
    )

fig.update_layout(
    title="Seasonality-Based Historical Purchase Signals",
    xaxis_title="Month",
    yaxis_title="Average Price (₹ per 10 grams)",
    barmode="group",
    template="plotly_white",
    height=700,
    hovermode="closest"
)

fig.show()

print("\nSeasonality purchase strategy analysis completed!")