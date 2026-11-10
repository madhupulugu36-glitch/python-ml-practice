
import pandas as pd
import numpy as np

df = pd.read_csv("data/delivery_data.csv")

# Calculate distance again
def haversine_distance(lat1, lon1, lat2, lon2):
    radius = 6371.0

    lat1, lon1, lat2, lon2 = map(
        np.radians, [lat1, lon1, lat2, lon2]
    )

    a = (
        np.sin((lat2 - lat1) / 2) ** 2
        + np.cos(lat1) * np.cos(lat2)
        * np.sin((lon2 - lon1) / 2) ** 2
    )

    a = np.clip(a, 0, 1)
    return 2 * radius * np.arcsin(np.sqrt(a))


df["Distance_km"] = haversine_distance(
    df["Restaurant_latitude"],
    df["Restaurant_longitude"],
    df["Delivery_location_latitude"],
    df["Delivery_location_longitude"],
)

# 1. Inspect the 15 largest distances
print("\n--- 15 LARGEST DISTANCES ---")

columns = [
    "ID",
    "City",
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
    "Distance_km",
    "Time_taken (min)",
]

print(
    df.nlargest(15, "Distance_km")[columns].to_string(index=False)
)

# 2. Check records with unusual ratings
print("\n--- RATINGS OUTSIDE 1 TO 5 ---")

print(
    df.loc[
        (df["Delivery_person_Ratings"] < 1)
        | (df["Delivery_person_Ratings"] > 5),
        ["ID", "Delivery_person_Ratings", "City"],
    ].head(20).to_string(index=False)
)

# 3. Check coordinate ranges
coordinate_columns = [
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
]

print("\n--- COORDINATE RANGES ---")
print(df[coordinate_columns].describe())

# 4. Check vehicle condition values
print("\n--- VEHICLE CONDITION COUNTS ---")
print(df["Vehicle_condition"].value_counts().sort_index())

print("\nInvestigation completed!")
