
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Sort by date
df = df.sort_values("Date")

# Calculate daily price changes
df["Gold_Daily_Change"] = df["Gold_999_PM_Rs_per_10g"].diff()
df["Platinum_Daily_Change"] = df["Platinum_999_PM_Rs_per_10g"].diff()

# Create interactive chart
fig = go.Figure()

# Gold daily fluctuation
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Gold_Daily_Change"],
        mode="lines+markers",
        name="Gold Daily Change",
        hovertemplate="Date: %{x|%d-%m-%Y}<br>Change: ₹%{y:,.2f}<extra></extra>"
    )
)

# Platinum daily fluctuation
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Platinum_Daily_Change"],
        mode="lines+markers",
        name="Platinum Daily Change",
        hovertemplate="Date: %{x|%d-%m-%Y}<br>Change: ₹%{y:,.2f}<extra></extra>"
    )
)

# Chart layout
fig.update_layout(
    title="Gold vs Platinum Daily Price Fluctuations",
    xaxis_title="Date",
    yaxis_title="Daily Price Change (₹ per 10 grams)",
    template="plotly_white",
    hovermode="x unified",
    height=650
)

# Zero reference line
fig.add_hline(y=0, line_dash="dash", line_color="gray")

# Display chart
fig.show()

# Summary
print("\nDaily Price Fluctuation Summary")
print("--------------------------------")
print("Gold Average Daily Change:", round(df["Gold_Daily_Change"].mean(), 2))
print("Platinum Average Daily Change:", round(df["Platinum_Daily_Change"].mean(), 2))
print("Gold Maximum Increase:", round(df["Gold_Daily_Change"].max(), 2))
print("Gold Maximum Decrease:", round(df["Gold_Daily_Change"].min(), 2))
print("Platinum Maximum Increase:", round(df["Platinum_Daily_Change"].max(), 2))
print("Platinum Maximum Decrease:", round(df["Platinum_Daily_Change"].min(), 2))