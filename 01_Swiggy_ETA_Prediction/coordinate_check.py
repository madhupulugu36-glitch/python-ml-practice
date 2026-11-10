
import pandas as pd

df = pd.read_csv("data/delivery_data.csv")

print("\n--- NEGATIVE RESTAURANT LATITUDE ---")
print((df["Restaurant_latitude"] < 0).sum())

print("\n--- NEGATIVE RESTAURANT LONGITUDE ---")
print((df["Restaurant_longitude"] < 0).sum())

print("\n--- DELIVERY COORDINATES EQUAL TO 0.01 ---")
delivery_lat = (df["Delivery_location_latitude"] == 0.01).sum()
delivery_lon = (df["Delivery_location_longitude"] == 0.01).sum()

print("Delivery latitude = 0.01:", delivery_lat)
print("Delivery longitude = 0.01:", delivery_lon)

print("\n--- ROWS WITH NEGATIVE RESTAURANT LATITUDE ---")
columns = [
    "ID",
    "Restaurant_latitude",
    "Restaurant_longitude",
    "Delivery_location_latitude",
    "Delivery_location_longitude",
    "Time_taken (min)",
]

print(
    df.loc[df["Restaurant_latitude"] < 0, columns]
    .head(10)
    .to_string(index=False)
)

print("\nCoordinate check completed!")
