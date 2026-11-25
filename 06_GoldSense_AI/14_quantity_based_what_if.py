
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

# Purchase quantities in grams
quantities = [10, 20, 50, 100]

results = []

print("\nQUANTITY-BASED WHAT-IF ANALYSIS")
print("=" * 70)

for metal, column in metals.items():

    lowest_row = monthly.loc[monthly[column].idxmin()]
    highest_row = monthly.loc[monthly[column].idxmax()]

    lowest_price = lowest_row[column]
    highest_price = highest_row[column]

    price_difference_per_10g = highest_price - lowest_price

    print(f"\n{metal}")
    print("-" * 50)

    print(f"Lowest-price month: {lowest_row['Month']}")
    print(f"Highest-price month: {highest_row['Month']}")

    for quantity in quantities:

        # Calculate potential savings for the quantity
        potential_savings = (
            price_difference_per_10g * quantity / 10
        )

        results.append({
            "Metal": metal,
            "Quantity (grams)": quantity,
            "Potential Savings (Rs)": potential_savings
        })

        print(
            f"{quantity:>3} grams | "
            f"Potential Savings: ₹{potential_savings:,.2f}"
        )

# Create results DataFrame
summary = pd.DataFrame(results)

# Create interactive chart
fig = go.Figure()

for metal in metals:

    metal_data = summary[summary["Metal"] == metal]

    fig.add_trace(
        go.Bar(
            x=metal_data["Quantity (grams)"],
            y=metal_data["Potential Savings (Rs)"],
            name=metal,
            text=[
                f"₹{value:,.0f}"
                for value in metal_data["Potential Savings (Rs)"]
            ],
            textposition="outside",
            hovertemplate=(
                "<b>" + metal + "</b><br>"
                "Purchase Quantity: %{x} grams<br>"
                "Potential Savings: ₹%{y:,.2f}"
                "<extra></extra>"
            )
        )
    )

fig.update_layout(
    title="What-If Analysis - Savings by Purchase Quantity",
    xaxis_title="Purchase Quantity (grams)",
    yaxis_title="Potential Savings (₹)",
    barmode="group",
    template="plotly_white",
    height=650,
    hovermode="closest"
)

fig.show()

print("\nQuantity-based What-If analysis completed!")