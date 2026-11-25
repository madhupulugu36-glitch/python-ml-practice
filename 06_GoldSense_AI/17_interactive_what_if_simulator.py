
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("data/gold_platinum_daily_comparison.csv")

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")

# Metal selection
metals = {
    "1": ("Gold 999", "Gold_999_PM_Rs_per_10g"),
    "2": ("Platinum 999", "Platinum_999_PM_Rs_per_10g")
}

print("\nINTERACTIVE WHAT-IF PRICE SIMULATOR")
print("=" * 50)

print("1. Gold 999")
print("2. Platinum 999")

choice = input("\nSelect metal (1 or 2): ")

if choice not in metals:
    print("Invalid selection!")
    exit()

metal_name, column = metals[choice]

# Latest available price
current_price = df[column].iloc[-1]
latest_date = df["Date"].iloc[-1]

print(f"\nSelected Metal: {metal_name}")
print(f"Latest available date: {latest_date.strftime('%d-%m-%Y')}")
print(f"Price per 10 grams: ₹{current_price:,.2f}")

# Purchase quantity
quantity = float(input("\nEnter purchase quantity in grams: "))

if quantity <= 0:
    print("Quantity must be greater than zero!")
    exit()

# Calculate current purchase cost
current_cost = current_price * quantity / 10

# Scenario percentage
change_percentage = float(
    input("\nEnter assumed price change percentage (e.g. -5 or 5): ")
)

# Calculate scenario price
scenario_price = current_price * (1 + change_percentage / 100)

scenario_cost = scenario_price * quantity / 10

cost_difference = scenario_cost - current_cost

# Results
print("\nWHAT-IF SIMULATION RESULTS")
print("=" * 50)

print(f"Metal: {metal_name}")
print(f"Quantity: {quantity:g} grams")
print(f"Current price per 10g: ₹{current_price:,.2f}")
print(f"Scenario price per 10g: ₹{scenario_price:,.2f}")

print(f"\nCurrent Purchase Cost: ₹{current_cost:,.2f}")
print(f"Scenario Purchase Cost: ₹{scenario_cost:,.2f}")

if cost_difference < 0:
    print(f"Potential Savings: ₹{abs(cost_difference):,.2f}")
elif cost_difference > 0:
    print(f"Additional Cost: ₹{cost_difference:,.2f}")
else:
    print("No cost difference.")

# Create scenario chart
scenario_percentages = [-10, -5, 0, 5, 10]

scenario_costs = [
    current_cost * (1 + percentage / 100)
    for percentage in scenario_percentages
]

cost_changes = [
    cost - current_cost
    for cost in scenario_costs
]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=[
            f"{percentage:+}%"
            for percentage in scenario_percentages
        ],
        y=scenario_costs,
        customdata=cost_changes,
        text=[
            f"₹{cost:,.0f}"
            for cost in scenario_costs
        ],
        textposition="outside",
        hovertemplate=(
            "Price Change: %{x}<br>"
            "Purchase Cost: ₹%{y:,.2f}<br>"
            "Cost Difference: ₹%{customdata:+,.2f}"
            "<extra></extra>"
        )
    )
)

fig.update_layout(
    title=f"What-If Purchase Cost Simulator - {metal_name}",
    xaxis_title="Assumed Price Change",
    yaxis_title="Purchase Cost (₹)",
    template="plotly_white",
    height=600,
    hovermode="closest"
)

fig.show()

print("\nInteractive What-If simulator completed!")