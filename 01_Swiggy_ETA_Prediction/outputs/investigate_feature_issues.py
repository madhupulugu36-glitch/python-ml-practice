
import pandas as pd
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "delivery_data_cleaned.csv"

df = pd.read_csv(INPUT_PATH)

print("=" * 60)
print("SWIGGY ETA - INVESTIGATE FEATURE ISSUES")
print("=" * 60)

# 1. Investigate order-time formats
time_values = df["Time_Orderd"].dropna().astype(str)

standard_time = time_values.str.match(
    r"^(?:[01]?\d|2[0-3]):[0-5]\d$"
)

unusual_times = time_values[~standard_time]

print("\n1. ORDER-TIME FORMAT ANALYSIS")
print("Non-missing order-time values:", len(time_values))
print("Standard HH:MM values:", int(standard_time.sum()))
print("Unusual-format values:", len(unusual_times))

print("\nUnusual values and frequencies:")
print(unusual_times.value_counts().head(30).to_string())

# 2. Inspect records with a rating of 6
print("\n2. RECORDS WITH RATING 6.0")

rating_columns = [
    "Delivery_person_Age",
    "Delivery_person_Ratings",
    "Weather_conditions",
    "Road_traffic_density",
    "Vehicle_condition",
    "Type_of_order",
    "Type_of_vehicle",
    "multiple_deliveries",
    "City",
    "Time_taken (min)"
]

rating_six = df.loc[
    df["Delivery_person_Ratings"] == 6,
    rating_columns
]

print("Records with rating 6.0:", len(rating_six))
print(rating_six.head(15).to_string(index=False))

print("\nInvestigation completed.")