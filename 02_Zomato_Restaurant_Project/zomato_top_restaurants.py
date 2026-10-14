
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

# Remove rows with missing values
df = df.dropna(
    subset=["Restaurant Name", "Votes", "Aggregate rating"]
)

# Convert votes and ratings to numeric
df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")
df["Aggregate rating"] = pd.to_numeric(
    df["Aggregate rating"], errors="coerce"
)

df = df.dropna(subset=["Votes", "Aggregate rating"])

# Group by restaurant name
restaurant_analysis = (
    df.groupby("Restaurant Name")
    .agg(
        Total_Votes=("Votes", "sum"),
        Average_Rating=("Aggregate rating", "mean"),
        Branch_Count=("Restaurant Name", "count")
    )
    .reset_index()
)

# Find top 10 restaurants by total votes
top_restaurants = restaurant_analysis.sort_values(
    "Total_Votes", ascending=False
).head(10)

print("----- TOP 10 RESTAURANTS BY VOTES -----")
print(top_restaurants.to_string(index=False))

# Plot total votes
plt.figure(figsize=(12, 6))
plt.barh(
    top_restaurants["Restaurant Name"][::-1],
    top_restaurants["Total_Votes"][::-1]
)

plt.title("Top 10 Restaurants by Total Votes")
plt.xlabel("Total Votes")
plt.ylabel("Restaurant Name")
plt.tight_layout()

plt.savefig("top_10_restaurants_by_votes.png", dpi=300)
plt.show()

print("Top restaurant analysis completed successfully!")