
import pandas as pd

# Load validated data
df = pd.read_csv("data/gold_999_validated.csv")

df["Date"] = pd.to_datetime(df["Date"])

price_col = "Gold_999_PM_Rs_per_10g"

# Sort data by date
df = df.sort_values("Date").reset_index(drop=True)

# Calculate daily price changes
df["Daily_Change"] = df[price_col].diff()

# Calculate daily percentage changes
df["Daily_Change_Percent"] = df[price_col].pct_change() * 100

# Calculate monthly average
df["Month"] = df["Date"].dt.to_period("M")

monthly_average = df.groupby("Month")[price_col].mean()

# Highest and lowest prices
highest = df.loc[df[price_col].idxmax()]
lowest = df.loc[df[price_col].idxmin()]

# Overall change
first_price = df.iloc[0][price_col]
last_price = df.iloc[-1][price_col]

overall_change = last_price - first_price
overall_change_percent = (overall_change / first_price) * 100

# Display results
print("\n========== GOLD PRICE ANALYSIS ==========")

print("\nHighest Price:")
print("Date:", highest["Date"].date())
print("Price:", highest[price_col])

print("\nLowest Price:")
print("Date:", lowest["Date"].date())
print("Price:", lowest[price_col])

print("\nOverall Price Change:", round(overall_change, 2))
print("Overall Change Percentage:", round(overall_change_percent, 2), "%")

print("\nMonthly Average Prices:")
print(monthly_average.round(2))

print("\nDaily Price Changes (Latest 10 Records):")
print(df[["Date", price_col, "Daily_Change",
          "Daily_Change_Percent"]].tail(10))

# Save analysis dataset
df.to_csv("data/gold_price_analysis.csv", index=False)

print("\nAnalysis dataset saved successfully!")