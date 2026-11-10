
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "delivery_data_cleaned.csv"

df = pd.read_csv(INPUT_PATH)

print("=" * 60)
print("SWIGGY ETA - FEATURE QUALITY CHECK")
print("=" * 60)

print("\n1. ORDER TIME DATA TYPES")
print(
    df["Time_Orderd"]
    .dropna()
    .map(lambda value: f"{value!r} ({type(value).__name__})")
    .head(15)
    .to_string(index=False)
)

print("\n2. MOST COMMON ORDER TIME VALUES")
print(df["Time_Orderd"].value_counts(dropna=False).head(20).to_string())

print("\n3. DELIVERY RATINGS")
print(df["Delivery_person_Ratings"].describe().to_string())

print("\nRating frequencies:")
print(
    df["Delivery_person_Ratings"]
    .value_counts(dropna=False)
    .sort_index()
    .to_string()
)

print("\n4. AGE AND MULTIPLE DELIVERIES")
for column in ["Delivery_person_Age", "multiple_deliveries"]:
    print(f"\n{column}:")
    print(
        df[column]
        .value_counts(dropna=False)
        .sort_index()
        .to_string()
    )

print("\nFeature quality check completed.")