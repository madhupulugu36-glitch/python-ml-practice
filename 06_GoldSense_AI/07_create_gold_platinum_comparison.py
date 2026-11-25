
import pandas as pd

gold = pd.read_csv("data/gold_999_historical.csv")
platinum = pd.read_csv("data/platinum_999_historical.csv")

gold["Date"] = pd.to_datetime(gold["Date"], dayfirst=True)
platinum["Date"] = pd.to_datetime(platinum["Date"], dayfirst=True)

comparison = pd.merge(
    gold[["Date", "Gold_999_PM_Rs_per_10g"]],
    platinum[["Date", "Platinum_999_PM_Rs_per_10g"]],
    on="Date",
    how="inner"
)

comparison = comparison.sort_values("Date")

comparison["Date"] = comparison["Date"].dt.strftime("%d-%m-%Y")

comparison.to_csv(
    "data/gold_platinum_daily_comparison.csv",
    index=False
)

print("Gold-Platinum dataset created successfully!")
print("Total records:", len(comparison))
print("Columns:", list(comparison.columns))
print(comparison.head())