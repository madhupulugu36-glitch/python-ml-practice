
import pandas as pd

# Load the Platinum template
file_path = "data/platinum_999_historical.csv"
df = pd.read_csv(file_path)

# Verified Platinum 999 PM rates (Rs per 10 grams)
# Source: India in Data and IBJA Daily Bullion Report
verified_prices = {
    "07-09-2026": 60837,
    "14-10-2026": 59147,
    "15-10-2026": 57649,
    "16-10-2026": 58484,
    "19-10-2026": 57026,
    "11-11-2026": 56150,
    "12-11-2026": 54850,
    "13-11-2026": 55940,
    "16-11-2026": 55547
}

# Normalize dates for matching
df["Date"] = pd.to_datetime(
    df["Date"], dayfirst=True, errors="raise"
)

matched = 0

for date, price in verified_prices.items():
    target_date = pd.to_datetime(date, dayfirst=True)
    mask = df["Date"] == target_date

    if mask.any():
        df.loc[mask, "Platinum_999_PM_Rs_per_10g"] = price
        matched += 1
    else:
        print("Date not found in Gold dataset:", date)

# Save in the original date format
df["Date"] = df["Date"].dt.strftime("%d-%m-%Y")
df.to_csv(file_path, index=False)

print("\nPlatinum prices updated successfully!")
print("Verified prices added:", matched)
print(
    "Remaining missing prices:",
    df["Platinum_999_PM_Rs_per_10g"].isna().sum()
)
print("\nUpdated records:")
print(df[df["Platinum_999_PM_Rs_per_10g"].notna()])