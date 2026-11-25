
import pandas as pd

# Load Gold dataset
file_path = "data/gold_999_historical.csv"
df = pd.read_csv(file_path)

# Convert Date column
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d-%m-%Y"
)

# Check duplicate dates
duplicate_dates = df[df.duplicated(subset=["Date"], keep=False)]

# Convert price from 10 grams to 1 gram
df["Gold_999_PM_Rs_per_gram"] = (
    df["Gold_999_PM_Rs_per_10g"] / 10
)

# Sort dates
df = df.sort_values("Date")

# Display validation results
print("\n========== GOLD DATA VALIDATION ==========")

print("\nTotal Records:", len(df))
print("Start Date:", df["Date"].min().date())
print("End Date:", df["Date"].max().date())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Dates:", len(duplicate_dates))

print("\nGold Price Summary (Rs per 10 grams):")
print(df["Gold_999_PM_Rs_per_10g"].describe())

print("\nGold Price Summary (Rs per gram):")
print(df["Gold_999_PM_Rs_per_gram"].describe())

# Save validated dataset
df.to_csv(
    "data/gold_999_validated.csv",
    index=False
)

print("\nValidated dataset saved successfully!")