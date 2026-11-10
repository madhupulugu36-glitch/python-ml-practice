
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "delivery_data.csv"

df = pd.read_csv(INPUT_PATH)

coordinate_columns = [
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
]

print("=" * 60)
print("SWIGGY ETA - COORDINATE VALIDATION")
print("=" * 60)

# 1. Inspect the raw coordinate values
print("\n--- COORDINATE RANGES ---")

for column in coordinate_columns:
    print(f"\n{column}")
    print(df[column].describe())
    print("Negative values:", (df[column] < 0).sum())
    print("Zero values:", (df[column] == 0).sum())
    print("Values equal to 0.01:", (df[column] == 0.01).sum())

# 2. Inspect records outside broad India bounds
print("\n--- SAMPLE INVALID COORDINATE RECORDS ---")

valid = (
    df["Restaurant_latitude"].between(6, 38)
    & df["Restaurant_longitude"].between(68, 98)
    & df["Delivery_location_latitude"].between(6, 38)
    & df["Delivery_location_longitude"].between(68, 98)
)

invalid_df = df.loc[~valid]

print("Records outside broad bounds:", len(invalid_df))

print(
    invalid_df[
        coordinate_columns + ["Time_taken (min)"]
    ].head(15).to_string(index=False)
)

# 3. Check how many rows have at least one invalid coordinate
print("\n--- VALIDATION SUMMARY ---")
print("Total rows:", len(df))
print("All coordinates within bounds:", int(valid.sum()))
print("At least one coordinate outside bounds:", int((~valid).sum()))

print("\nCoordinate validation completed.")