
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "delivery_data_cleaned.csv"

df = pd.read_csv(INPUT_PATH)

print("=" * 60)
print("SWIGGY ETA - MISSING VALUE ANALYSIS")
print("=" * 60)

print("\n1. DATASET SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n2. MISSING VALUES BY COLUMN")

missing = df.isnull().sum()
missing_percent = (missing / len(df) * 100).round(2)

missing_summary = pd.DataFrame({
    "Missing_Count": missing,
    "Missing_Percentage": missing_percent
})

missing_summary = missing_summary[
    missing_summary["Missing_Count"] > 0
].sort_values("Missing_Count", ascending=False)

print(missing_summary.to_string())

print("\n3. NUMERIC COLUMN SUMMARY")

numeric_columns = [
    "Delivery_person_Age",
    "Delivery_person_Ratings",
    "multiple_deliveries",
    "Distance_km",
    "Time_taken (min)"
]

print(df[numeric_columns].describe().round(2).to_string())

print("\n4. CATEGORICAL COLUMN SUMMARY")

categorical_columns = [
    "Weather_conditions",
    "Road_traffic_density",
    "Festival",
    "City",
    "Time_Orderd"
]

for column in categorical_columns:
    print(f"\n{column}")
    print(df[column].value_counts(dropna=False).head(10).to_string())

print("\nAnalysis completed.")
