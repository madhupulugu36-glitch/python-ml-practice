
import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================
# 1. FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

AUDIT_FILE = DATA_DIR / "platinum_999_provenance_audit.csv"
BACKUP_FILE = DATA_DIR / "platinum_999_historical.csv"

UNKNOWN_REPORT = DATA_DIR / "platinum_unknown_records_investigation.csv"
SUMMARY_REPORT = DATA_DIR / "platinum_investigation_summary.csv"

PRICE_COLUMN = "Platinum_999_PM_Rs_per_10g"

# ============================================================
# 2. LOAD DATA
# ============================================================

if not AUDIT_FILE.exists():
    raise FileNotFoundError(f"Missing audit file: {AUDIT_FILE}")

if not BACKUP_FILE.exists():
    raise FileNotFoundError(f"Missing backup file: {BACKUP_FILE}")

df = pd.read_csv(AUDIT_FILE)
backup = pd.read_csv(BACKUP_FILE)

df["Date_Parsed"] = pd.to_datetime(
    df["Date"], dayfirst=True, errors="coerce"
)

df[PRICE_COLUMN] = pd.to_numeric(
    df[PRICE_COLUMN], errors="coerce"
)

backup[PRICE_COLUMN] = pd.to_numeric(
    backup[PRICE_COLUMN], errors="coerce"
)

# ============================================================
# 3. CHECK BACKUP CONSISTENCY
# ============================================================

current = df[["Date", PRICE_COLUMN]].copy()
original = backup[["Date", PRICE_COLUMN]].copy()

current["Date"] = current["Date"].astype(str)
original["Date"] = original["Date"].astype(str)

backup_matches = current.equals(original)

# ============================================================
# 4. IDENTIFY UNKNOWN RECORDS
# ============================================================

unknown_mask = df["Verification_Status"].str.contains(
    "origin unknown",
    case=False,
    na=False
)

unknown = df[unknown_mask].copy()

unknown["Investigation_Status"] = (
    "Unknown origin - investigation required"
)

# ============================================================
# 5. SORT ALL DATA BY DATE
# ============================================================

df = df.sort_values("Date_Parsed").reset_index(drop=True)

df["Previous_Price"] = df[PRICE_COLUMN].shift(1)

df["Daily_Change"] = (
    df[PRICE_COLUMN] - df["Previous_Price"]
)

df["Daily_Change_Percent"] = (
    df["Daily_Change"] / df["Previous_Price"]
) * 100

# ============================================================
# 6. MERGE DAILY CHANGE INFORMATION
# ============================================================

unknown = unknown.merge(
    df[
        [
            "Date",
            "Previous_Price",
            "Daily_Change",
            "Daily_Change_Percent"
        ]
    ],
    on="Date",
    how="left"
)

# ============================================================
# 7. DETECT UNUSUAL PRICE MOVEMENTS
# ============================================================

unknown["Unusual_Movement_Flag"] = False

valid_changes = df["Daily_Change_Percent"].dropna()

if len(valid_changes) > 0:

    mean_change = valid_changes.mean()
    std_change = valid_changes.std()

    upper_limit = mean_change + (3 * std_change)
    lower_limit = mean_change - (3 * std_change)

    unknown["Unusual_Movement_Flag"] = (
        (unknown["Daily_Change_Percent"] > upper_limit)
        |
        (unknown["Daily_Change_Percent"] < lower_limit)
    )

else:
    upper_limit = np.nan
    lower_limit = np.nan

# ============================================================
# 8. PRICE RANGE ANALYSIS
# ============================================================

unknown_prices = unknown[PRICE_COLUMN].dropna()

if len(unknown_prices) > 0:

    unknown_min = unknown_prices.min()
    unknown_max = unknown_prices.max()
    unknown_mean = unknown_prices.mean()
    unknown_median = unknown_prices.median()
    unknown_std = unknown_prices.std()

else:

    unknown_min = np.nan
    unknown_max = np.nan
    unknown_mean = np.nan
    unknown_median = np.nan
    unknown_std = np.nan

# ============================================================
# 9. CHECK VALUE DISTRIBUTION
# ============================================================

unknown["Rounded_To_100"] = (
    unknown[PRICE_COLUMN] % 100 == 0
)

unknown["Rounded_To_500"] = (
    unknown[PRICE_COLUMN] % 500 == 0
)

unknown["Rounded_To_1000"] = (
    unknown[PRICE_COLUMN] % 1000 == 0
)

# ============================================================
# 10. SAVE UNKNOWN RECORD REPORT
# ============================================================

unknown.drop(
    columns=["Date_Parsed"],
    errors="ignore",
    inplace=True
)

unknown.to_csv(
    UNKNOWN_REPORT,
    index=False
)

# ============================================================
# 11. CREATE INVESTIGATION SUMMARY
# ============================================================

summary = pd.DataFrame({

    "Metric": [
        "Total historical records",
        "Unknown-origin records",
        "Other records",
        "Backup matches current dataset",
        "Unknown records with prices",
        "Unknown minimum price",
        "Unknown maximum price",
        "Unknown average price",
        "Unknown median price",
        "Unknown price standard deviation",
        "Unknown values rounded to 100",
        "Unknown values rounded to 500",
        "Unknown values rounded to 1000",
        "Unusual daily movements in unknown records",
        "Daily percentage change upper threshold",
        "Daily percentage change lower threshold"
    ],

    "Value": [
        len(df),
        len(unknown),
        len(df) - len(unknown),
        backup_matches,
        len(unknown_prices),
        unknown_min,
        unknown_max,
        unknown_mean,
        unknown_median,
        unknown_std,
        int(unknown["Rounded_To_100"].sum()),
        int(unknown["Rounded_To_500"].sum()),
        int(unknown["Rounded_To_1000"].sum()),
        int(unknown["Unusual_Movement_Flag"].sum()),
        upper_limit,
        lower_limit
    ]
})

summary.to_csv(
    SUMMARY_REPORT,
    index=False
)

# ============================================================
# 12. DISPLAY INVESTIGATION RESULTS
# ============================================================

print("\nPLATINUM UNKNOWN RECORD INVESTIGATION")
print("=" * 65)

print("\nDATASET INFORMATION")

print("Total records:", len(df))
print("Unknown-origin records:", len(unknown))
print("Other records:", len(df) - len(unknown))

print("\nBACKUP CHECK")

print("Backup matches current dataset:", backup_matches)

print("\nUNKNOWN PRICE STATISTICS")

print("Minimum:", unknown_min)
print("Maximum:", unknown_max)
print("Average:", round(unknown_mean, 2))
print("Median:", round(unknown_median, 2))
print("Standard deviation:", round(unknown_std, 2))

print("\nPRICE PATTERN CHECK")

print(
    "Rounded to 100:",
    int(unknown["Rounded_To_100"].sum())
)

print(
    "Rounded to 500:",
    int(unknown["Rounded_To_500"].sum())
)

print(
    "Rounded to 1000:",
    int(unknown["Rounded_To_1000"].sum())
)

print("\nUNUSUAL DAILY MOVEMENTS")

print(
    "Unusual unknown records:",
    int(unknown["Unusual_Movement_Flag"].sum())
)

print("\nOUTPUT FILES")

print("Unknown records report:", UNKNOWN_REPORT.name)
print("Summary report:", SUMMARY_REPORT.name)

print("\nINVESTIGATION COMPLETED")
print("=" * 65)

print(
    "\nNote: Statistical patterns cannot prove that a price "
    "was randomly generated. Source evidence is still required."
)