
import pandas as pd
import plotly.graph_objects as go

# Load comparison dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Sort dates
df = df.sort_values("Date")

# Create interactive chart
fig = go.Figure()

# Gold price
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Gold_999_PM_Rs_per_10g"],
        mode="lines+markers",
        name="Gold 999",
        line=dict(width=2),
        hovertemplate="Date: %{x|%d-%m-%Y}<br>Gold: ₹%{y:,.2f}<extra></extra>"
    )
)

# Platinum price
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Platinum_999_PM_Rs_per_10g"],
        mode="lines+markers",
        name="Platinum 999",
        line=dict(width=2),
        hovertemplate="Date: %{x|%d-%m-%Y}<br>Platinum: ₹%{y:,.2f}<extra></extra>"
    )
)

# Chart layout
fig.update_layout(
    title="Gold vs Platinum Daily Purchase Price Trend",
    xaxis_title="Date",
    yaxis_title="Price (₹ per 10 grams)",
    template="plotly_white",
    hovermode="x unified",
    legend_title="Metal",
    height=650
)

# Add date range slider
fig.update_xaxes(rangeslider_visible=True)

# Display graph
fig.show()

print("Interactive Plotly chart created successfully!")