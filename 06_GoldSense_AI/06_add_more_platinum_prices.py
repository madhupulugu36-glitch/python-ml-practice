
import pandas as pd

file_path = "data/platinum_999_historical.csv"

df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(
    df["Date"], dayfirst=True, errors="raise"
)

# Additional verified IBJA PM rates
verified_prices = {
    "06-10-2026": 61285,
    "07-10-2026": 56095,
    "28-10-2026": 61706,
    "05-11-2026": 56863,
    "06-11-2026": 55707
}

added = 0

for date, price in verified_prices.items():
    target_date = pd.to_datetime(date, dayfirst=True)
    mask = df["Date"] == target_date

    if not mask.any():
        print("Date not found in Gold dataset:", date)
    elif df.loc[mask, "Platinum_999_PM_Rs_per_10g"].isna().all():
        df.loc[mask, "Platinum_999_PM_Rs_per_10g"] = price
        added += 1
    else:
        print("Existing value preserved:", date)

df["Date"] = df["Date"].dt.strftime("%d-%m-%Y")
df.to_csv(file_path, index=False)

print("\nAdditional Platinum prices saved!")
print("New prices added:", added)
print(
    "Total available prices:",
    df["Platinum_999_PM_Rs_per_10g"].notna().sum()
)
print(
    "Remaining missing prices:",
    df["Platinum_999_PM_Rs_per_10g"].isna().sum()
)