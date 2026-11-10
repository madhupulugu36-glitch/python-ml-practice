import pandas as pd
import numpy as np
from pathlib import Path

#------------------
# FILE PATHS
#------------------

# This Script is inside the outputs folder.
# The data is inside the data folder.
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "delivery_data.csv"
OUTPUT_PATH = BASE_DIR / "data" / "delivery_data_cleaned.csv"

print("=" * 60)
print("SWIGGY ETA PREDICTION - DATA CLEANING")
print("=" * 60)

#----------------
# LOAD DATASET
#----------------
if not INPUT_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {INPUT_PATH}"
    )

df = pd.read_csv(INPUT_PATH)

print("\n---ORIGINAL DATASET---")
print("Dataset path:", INPUT_PATH)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

#-----------------------------------
# Keep the original data unchanged
#-----------------------------------
clean_df = df.copy()

#----------------------------
# VALIDATE REQUIRED COLUMNS
#----------------------------
coordinate_columns = [
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
]

required_columns = coordinate_columns + ["Time_taken (min)"]

missing_columns = [
    column
    for column in required_columns
    if column not in clean_df.columns
]

if missing_columns:
    raise ValueError(
        f"Required column not found: {missing_columns}"
    )

#----------------------------------------
# CONVERT COORDINATES TO NUMERIC VALUES
#----------------------------------------
for column in coordinate_columns:
    clean_df[column] = pd.to_numeric(
        clean_df[column],
        errors="coerce"
    )

print("\n---MISSING COORDINATES BEFORE CLEANING---")

for column in coordinate_columns:
    print(
        f"{column}: {clean_df[column].isna().sum()}"
    )

#------------------------------
# IDENTIFY INVALID COORDINATES
#------------------------------
# Broad geographic plausibility bounds for India
# These are checks, not exact delivery-area boundries.
coordinate_bounds = {
    "Restaurant_latitude": (6, 38),
    "Restaurant_longitude": (68, 98),
    "Delivery_location_latitude": (6, 38),
    "Delivery_location_longitude": (68, 98),
}

print("\n---INVALID COORDINATES---")

for column, (lower, upper) in coordinate_bounds.items():
    values = clean_df[column]

    invalid_mask = (
        values.notna()
        & ~values.between(lower, upper)
    )

    invalid_count = int(invalid_mask.sum())

    print(f"{column}: {invalid_count}")


    # Replace invalid values with missing values.
    # Do not delete the complete delivery record.
    clean_df.loc[invalid_mask, column] = np.nan

#-------------------------------
# CHECK PLACEHOLDER COORDINATES
#-------------------------------
print("\n---POSSIBLE PLACEHOLDER COORDINATES---")

for column in coordinate_columns:

    placeholedr_mask = np.isclose(
        clean_df[column].fillna(-999).to_numpy(),
        0.01
    )

    print(
        f"{column} equal to 0.01: "
        f"{int(placeholedr_mask.sum())}"
    )

#------------------------------
# CALCULATE HAVERSINE DISTANCE
#------------------------------

# Distance is calculated only when all four
# coordinates are available and pass validation.

valid_coordinates = clean_df[
    coordinate_columns
].notna().all(axis=1)

# Also exclude exact 0.01 placeholders.
for colunm in coordinate_columns:
    valid_coordinates &= ~np.isclose(
        clean_df[column].fillna(-999),
        0.01
    )

print("\n---DISTANCE CALCULATION---")
valid_count = int(valid_coordinates.astype(bool).sum())
invalid_count = len(clean_df) - valid_count

print("Rows with valid coordinates:", valid_count)
print("Rows without valid coordinates:", invalid_count)
print("Total rows:", len(clean_df))

clean_df["Distance_km"] = np.nan

if valid_coordinates.any():

    lat1 = np.radians(
        clean_df.loc[
            valid_coordinates, "Restaurant_latitude"
        ].to_numpy()
    )

    lon1 = np.radians(
        clean_df.loc[
            valid_coordinates, "Restaurant_longitude"
        ].to_numpy()
    )

    lat2 = np.radians(
        clean_df.loc[
            valid_coordinates, "Delivery_location_latitude"
        ].to_numpy()
    )

    lon2 = np.radians(
        clean_df.loc[
            valid_coordinates, "Delivery_location_longitude"
        ].to_numpy()
    )

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (
        np.sin(delta_lat / 2) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(delta_lon / 2) ** 2
    )

    # Protect against floating-point rounding errors.
    a = np.clip(a, 0, 1)

    earth_radius_km = 6371.0

    distances = (
        2
        * earth_radius_km
        * np.arctan2(
            np.sqrt(a),
            np.sqrt(1 - a)
        )
    )

    clean_df.loc[
        valid_coordinates, "Distance_km"
    ] = distances


#---------------------
# VALID TARGET COLUMN
#---------------------

clean_df["Time_taken (min)"] = pd.to_numeric(
    clean_df["Time_taken (min)"],
    errors="coerce"
)

invalid_target = (
    clean_df["Time_taken (min)"].isna()
    | (clean_df["Time_taken (min)"] <= 0)
)

print("\n---ETA TARGET VALIDATION---")
print("Missing or invalid ETA values:", int(invalid_target.sum()))

# Do not remove invalid target rows automatically.
# We will decide how to handle them during modeling.

#-------------------
# DISTANCE SUMMARY
#-------------------
print("\n---DISTANCE SUMMARY---")
print(clean_df["Distance_km"].describe())

print("\n---POSSIBLE EXTREME DISTANCE---")

extreme_distance_mask = clean_df["Distance_km"] > 100

print(
    "Distances above 100 km:",
    int(extreme_distance_mask.sum())
)

# Flag extreme distances for investigation
# Do not delete them automatically.
print("\n---Sample extreme-distances records---")

print(
    clean_df.loc[
        extreme_distance_mask,
        coordinate_columns + ["Distance_km", "Time_taken (min)"]
    ].head(10).to_string(index=False)
)

#-------------------------
# CHECK DUPLICATE RECORDS
#-------------------------

print("\n---DUPLICATE CHECK---")
print("Duplicate rows:", int(clean_df.duplicated().sum()))

#----------------------
# SAVE CLEANED DATASET
#----------------------

clean_df.to_csv(OUTPUT_PATH, index=False)

print("\n---CLEANING SUMMARY---")
print("Orginal rows:", len(df))
print("Cleaned rows:", len(clean_df))
print("Rows preserved:", len(df) == len(clean_df))
print("Original columns:", len(df.columns))
print("Cleaned columns:", len(clean_df.columns))
print("Distance column added:", "Distance_km" in clean_df.columns)
print("Output file:", OUTPUT_PATH)
print("\nData cleaning script completed successfully!")
print("=" * 60)
