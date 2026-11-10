
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("data/delivery_data.csv")

# 1. Analyze delivery time
print("\n--- DELIVERY TIME DISTRIBUTION ---")
print(df["Time_taken (min)"].value_counts().sort_index())

# 2. Check numeric feature statistics
print("\n--- NUMERIC FEATURE STATISTICS ---")
print(
    df[
        [
            "Delivery_person_Age",
            "Delivery_person_Ratings",
            "Vehicle_condition",
            "multiple_deliveries",
        ]
    ].describe()
)

# 3. Calculate restaurant-to-customer distance
def haversine_distance(lat1, lon1, lat2, lon2):
    earth_radius_km = 6371.0

    lat1, lon1, lat2, lon2 = map(
        np.radians, [lat1, lon1, lat2, lon2]
    )

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (
        np.sin(delta_lat / 2) ** 2
        + np.cos(lat1) * np.cos(lat2)
        * np.sin(delta_lon / 2) ** 2
    )

    a = np.clip(a, 0, 1)

    return 2 * earth_radius_km * np.arcsin(np.sqrt(a))


df["Distance_km"] = haversine_distance(
    df["Restaurant_latitude"],
    df["Restaurant_longitude"],
    df["Delivery_location_latitude"],
    df["Delivery_location_longitude"],
)

# 4. Inspect calculated distances
print("\n--- DISTANCE STATISTICS (KM) ---")
print(df["Distance_km"].describe())

# 5. Find suspicious coordinates and distances
invalid_coordinates = (
    ~df["Restaurant_latitude"].between(-90, 90)
    | ~df["Delivery_location_latitude"].between(-90, 90)
    | ~df["Restaurant_longitude"].between(-180, 180)
    | ~df["Delivery_location_longitude"].between(-180, 180)
)

print("\n--- COORDINATE QUALITY ---")
print("Invalid coordinate rows:", invalid_coordinates.sum())
print("Zero-distance rows:", (df["Distance_km"] == 0).sum())
print("Distances over 100 km:", (df["Distance_km"] > 100).sum())

print("\nFeature analysis completed!")
