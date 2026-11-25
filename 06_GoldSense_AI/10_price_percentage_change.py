
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Sort by date
df = df.sort_values("Date")

# Calculate daily percentage changes
df["Gold_Percentage_Change"] = (
    df["Gold_999_PM_Rs_per_10g"].pct_change() * 100
)

df["Platinum_Percentage_Change"] = (
    df["Platinum_999_PM_Rs_per_10g"].pct_change() * 100
)

# Create interactive chart
fig = go.Figure()

# Gold percentage change
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Gold_Percentage_Change"],
        mode="lines+markers",
        name="Gold 999",
        hovertemplate="Date: %{x|%d-%m-%Y}<br>Change: %{y:.2f}%<extra></extra>"
    )
)

# Platinum percentage change
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Platinum_Percentage_Change"],
        mode="lines+markers",
        name="Platinum 999",
        hovertemplate="Date: %{x|%d-%m-%Y}<br>Change: %{y:.2f}%<extra></extra>"
    )
)

# Chart layout
fig.update_layout(
    title="Gold vs Platinum Daily Percentage Price Change",
    xaxis_title="Date",
    yaxis_title="Daily Percentage Change (%)",
    template="plotly_white",
    hovermode="x unified",
    height=650
)

# Zero reference line
fig.add_hline(y=0, line_dash="dash", line_color="gray")

# Display chart
fig.show()

# Summary
print("\nDaily Percentage Change Summary")
print("--------------------------------")

print(
    "Gold Average Change:",
    round(df["Gold_Percentage_Change"].mean(), 2), "%"
)

print(
    "Platinum Average Change:",
    round(df["Platinum_Percentage_Change"].mean(), 2), "%"
)

print(
    "Gold Maximum Increase:",
    round(df["Gold_Percentage_Change"].max(), 2), "%"
)

print(
    "Gold Maximum Decrease:",
    round(df["Gold_Percentage_Change"].min(), 2), "%"
)

print(
    "Platinum Maximum Increase:",
    round(df["Platinum_Percentage_Change"].max(), 2), "%"
)

print(
    "Platinum Maximum Decrease:",
    round(df["Platinum_Percentage_Change"].min(), 2), "%"
)