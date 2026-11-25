
import pandas as pd
import plotly.express as px
import os

# Load dataset
df = pd.read_csv("data/gold_price_analysis.csv")
df["Date"] = pd.to_datetime(df["Date"])

price_col = "Gold_999_PM_Rs_per_10g"

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Interactive chart
fig = px.line(
    df,
    x="Date",
    y=price_col,
    markers=True,
    title="Gold 999 PM Price Trend (June–November 2026)",
    labels={
        "Date": "Date",
        price_col: "Gold Price (₹ per 10g)"
    },
    hover_data={
        "Date": "|%d-%b-%Y",
        price_col: ":,.2f"
    }
)

fig.update_traces(
    line=dict(width=2),
    marker=dict(size=6),
    hovertemplate=
    "<b>Date:</b> %{x|%d-%b-%Y}<br>" +
    "<b>Gold Price:</b> ₹%{y:,.2f} per 10g" +
    "<extra></extra>"
)

fig.update_layout(
    hovermode="closest",
    template="plotly_white",
    xaxis_title="Date",
    yaxis_title="Gold Price (₹ per 10g)",
    title_x=0.5
)

# Save interactive HTML
fig.write_html(
    "charts/gold_999_pm_interactive.html"
)

fig.show()

print("Interactive Gold chart saved successfully!")