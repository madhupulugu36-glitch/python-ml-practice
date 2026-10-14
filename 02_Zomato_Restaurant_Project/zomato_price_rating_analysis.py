
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

# Remove rows with missing cost or rating
df = df.dropna(subset=["Average Cost for two", "Aggregate rating"])

# Group restaurants by average cost and calculate average rating
price_rating = (
    df.groupby("Average Cost for two")["Aggregate rating"]
    .mean()
    .reset_index()
)

# Display the first 10 price groups
print("----- PRICE VS AVERAGE RATING -----")
print(price_rating.head(10))

# Plot the relationship
plt.figure(figsize=(10, 6))
plt.scatter(
    price_rating["Average Cost for two"],
    price_rating["Aggregate rating"],
    alpha=0.6
)

plt.title("Average Cost for Two vs Average Rating")
plt.xlabel("Average Cost for Two")
plt.ylabel("Average Rating")
plt.tight_layout()

# Save chart
plt.savefig("price_vs_rating.png", dpi=300)
plt.show()

print("Price and rating analysis completed successfully!")
