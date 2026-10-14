import pandas as pd

# Load Clean dataset

df = pd.read_csv("zomato_cleaned.csv")

print("----- FEATURE ENGINEERING -----")

#check un rated restaurants
unrated = (df["Aggregate rating"] == 0).sum()
print("Restaurants with 0 rating:", unrated)

# created a rated only dataset for rating analysis
rated_df = df[df["Aggregate rating"] > 0].copy()

print("Total reastaurants:", len(df))
print("Restaurants with rating:"), len(rated_df)

# create a new feature: cuisine count

rated_df["Cuisine Count"] = (
    rated_df["Cuisines"]
    .apply(lambda x: 0 if x == "Unknown" else len(x.split(",")))
)