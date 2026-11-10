
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "delivery_data.csv"

df = pd.read_csv(INPUT_PATH)

print("=" * 65)
print("SWIGGY ETA - COORDINATE ISSUE ANALYSIS")
print("=" * 65)

# Coordinate columns
rlat = df["Restaurant_latitude"]
rlon = df["Restaurant_longitude"]
dlat = df["Delivery_location_latitude"]
dlon = df["Delivery_location_longitude"]

# Identify individual issue patterns
restaurant_zero = (rlat == 0) | (rlon == 0)

restaurant_negative = (rlat < 0) | (rlon < 0)

delivery_placeholder = (dlat == 0.01) & (dlon == 0.01)

delivery_outside_bounds = (
    ~dlat.between(6, 38)
    | ~dlon.between(68, 98)
)

restaurant_outside_bounds = (
    ~rlat.between(6, 38)
    | ~rlon.between(68, 98)
)

any_issue = (
    restaurant_outside_bounds
    | delivery_outside_bounds
)

# Report overlapping issue categories
print("\n--- ISSUE COUNTS ---")
print("Total records:", len(df))
print("Restaurant zero coordinates:", int(restaurant_zero.sum()))
print("Restaurant negative coordinates:", int(restaurant_negative.sum()))
print("Delivery placeholder pairs:", int(delivery_placeholder.sum()))
print("Restaurant outside bounds:", int(restaurant_outside_bounds.sum()))
print("Delivery outside bounds:", int(delivery_outside_bounds.sum()))
print("Records with any coordinate issue:", int(any_issue.sum()))
print("Records with all coordinates within bounds:", int((~any_issue).sum()))

# Inspect restaurant zero-coordinate records
print("\n--- RESTAURANT ZERO-COORDINATE SAMPLES ---")

print(
    df.loc[
        restaurant_zero,
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude",
            "Time_taken (min)",
        ],
    ].head(10).to_string(index=False)
)

# Inspect placeholder delivery records
print("\n--- DELIVERY PLACEHOLDER SAMPLES ---")

print(
    df.loc[
        delivery_placeholder,
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude",
            "Time_taken (min)",
        ],
    ].head(10).to_string(index=False)
)

# Inspect negative restaurant latitude records
print("\n--- NEGATIVE RESTAURANT LATITUDE SAMPLES ---")

print(
    df.loc[
        rlat < 0,
        [
            "Restaurant_latitude",
            "Restaurant_longitude",
            "Delivery_location_latitude",
            "Delivery_location_longitude",
            "Time_taken (min)",
        ],
    ].head(10).to_string(index=False)
)

print("\nAnalysis completed.")