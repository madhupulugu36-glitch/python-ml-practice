
import pandas as pd

# Read Gold dataset
gold = pd.read_csv("data/gold_999_historical.csv")

# Convert dates from DD-MM-YYYY format
gold["Date"] = pd.to_datetime(
    gold["Date"],
    dayfirst=True,
    errors="raise"
)

# Create Platinum template using exact Gold dates
platinum = gold[["Date"]].copy()

platinum["Platinum_999_PM_Rs_per_10g"] = pd.NA

# Format dates consistently
platinum["Date"] = platinum["Date"].dt.strftime("%d-%m-%Y")

# Save template
platinum.to_csv(
    "data/platinum_999_historical.csv",
    index=False
)

# Validate date range
dates = pd.to_datetime(platinum["Date"], dayfirst=True)

print("Platinum template created successfully!")
print("Total matching Gold dates:", len(platinum))
print("Start date:", dates.min().strftime("%d-%m-%Y"))
print("End date:", dates.max().strftime("%d-%m-%Y"))
print("Missing Platinum prices:", platinum["Platinum_999_PM_Rs_per_10g"].isna().sum())