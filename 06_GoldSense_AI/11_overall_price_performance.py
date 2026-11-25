
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Prepare data
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")

# Define price columns
metals = {
    "Gold 999": "Gold_999_PM_Rs_per_10g",
    "Platinum 999": "Platinum_999_PM_Rs_per_10g"
}

# Calculate overall performance
results = []

for metal, column in metals.items():

    starting_price = df[column].iloc[0]
    ending_price = df[column].iloc[-1]
    highest_price = df[column].max()
    lowest_price = df[column].min()

    # Calculate profit or loss
    profit_loss_amount = ending_price - starting_price

    profit_loss_percentage = (
        profit_loss_amount / starting_price
    ) * 100

    # Determine status
    if profit_loss_amount > 0:
        status = "Profit"
    elif profit_loss_amount < 0:
        status = "Loss"
    else:
        status = "No Change"

    results.append({
        "Metal": metal,
        "Starting Price": starting_price,
        "Ending Price": ending_price,
        "Highest Price": highest_price,
        "Lowest Price": lowest_price,
        "Profit/Loss Amount": profit_loss_amount,
        "Profit/Loss (%)": profit_loss_percentage,
        "Status": status
    })

# Create summary DataFrame
summary = pd.DataFrame(results)

# Display summary
print("\nOverall Price Performance")
print("--------------------------------")

print(summary.to_string(index=False, formatters={
    "Starting Price": "₹{:,.2f}".format,
    "Ending Price": "₹{:,.2f}".format,
    "Highest Price": "₹{:,.2f}".format,
    "Lowest Price": "₹{:,.2f}".format,
    "Profit/Loss Amount": "₹{:,.2f}".format,
    "Profit/Loss (%)": "{:+.2f}%".format
}))

# Create interactive chart
fig = go.Figure()

# Starting price bars
fig.add_trace(
    go.Bar(
        x=summary["Metal"],
        y=summary["Starting Price"],
        name="Starting Price",
        text=[
            f"₹{price:,.0f}"
            for price in summary["Starting Price"]
        ],
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Starting Price: ₹%{y:,.2f}"
            "<extra></extra>"
        )
    )
)

# Ending price bars
fig.add_trace(
    go.Bar(
        x=summary["Metal"],
        y=summary["Ending Price"],
        name="Ending Price",
        text=[
            f"₹{price:,.0f}"
            for price in summary["Ending Price"]
        ],
        textposition="outside",
        customdata=summary[
            ["Profit/Loss Amount", "Profit/Loss (%)", "Status"]
        ].values,
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Ending Price: ₹%{y:,.2f}<br>"
            "Price Difference: ₹%{customdata[0]:+,.2f}<br>"
            "Profit/Loss: %{customdata[1]:+.2f}%<br>"
            "Status: %{customdata[2]}"
            "<extra></extra>"
        )
    )
)

# Chart layout
fig.update_layout(
    title="Gold vs Platinum - Overall Price Performance",
    xaxis_title="Metal",
    yaxis_title="Price (₹ per 10 grams)",
    barmode="group",
    template="plotly_white",
    height=650,
    hovermode="closest"
)

# Display chart
fig.show()

print("\nOverall price performance analysis completed!")