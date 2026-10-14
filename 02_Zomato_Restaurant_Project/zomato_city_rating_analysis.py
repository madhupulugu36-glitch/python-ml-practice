
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

# Remove rows with missing city or rating
df = df.dropna(subset=["City", "Aggregate rating"])

# Exclude unrated restaurants (rating 0)
df = df[df["Aggregate rating"] > 0]

# Calculate average rating and restaurant count by city
city_analysis = (
    df.groupby("City")
    .agg(
        Average_Rating=("Aggregate rating", "mean"),
        Restaurant_Count=("Aggregate rating", "count")
    )
    .reset_index()
)

# Keep cities with at least 10 rated restaurants
city_analysis = city_analysis[
    city_analysis["Restaurant_Count"] >= 10
]

# Get top 10 cities by average rating
top_cities = city_analysis.sort_values(
    "Average_Rating", ascending=False
).head(10)

print("----- TOP 10 CITIES BY AVERAGE RATING -----")
print(top_cities.to_string(index=False))

# Plot the results
plt.figure(figsize=(10, 6))
plt.barh(
    top_cities["City"][::-1],
    top_cities["Average_Rating"][::-1]
)

plt.title("Top 10 Cities by Average Restaurant Rating")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.xlim(0, 5)
plt.tight_layout()

plt.savefig("top_10_cities_by_rating.png", dpi=300)
plt.show()

print("City rating analysis completed successfully!")
