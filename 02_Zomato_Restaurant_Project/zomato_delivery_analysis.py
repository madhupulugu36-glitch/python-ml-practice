
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

# Remove rows with missing delivery information or ratings
df = df.dropna(
    subset=["Has Online delivery", "Aggregate rating"]
)

# Group by online delivery availability
delivery_analysis = (
    df.groupby("Has Online delivery")
    .agg(
        Average_Rating=("Aggregate rating", "mean"),
        Restaurant_Count=("Aggregate rating", "count")
    )
    .reset_index()
)

print("----- ONLINE DELIVERY ANALYSIS -----")
print(delivery_analysis.to_string(index=False))

# Plot average ratings
plt.figure(figsize=(8, 5))
plt.bar(
    delivery_analysis["Has Online delivery"].astype(str),
    delivery_analysis["Average_Rating"]
)

plt.title("Average Rating: Online Delivery vs No Delivery")
plt.xlabel("Has Online Delivery")
plt.ylabel("Average Rating")
plt.tight_layout()

plt.savefig("delivery_vs_rating.png", dpi=300)
plt.show()

# Plot restaurant counts
plt.figure(figsize=(8, 5))
plt.bar(
    delivery_analysis["Has Online delivery"].astype(str),
    delivery_analysis["Restaurant_Count"]
)

plt.title("Restaurant Count by Online Delivery Availability")
plt.xlabel("Has Online Delivery")
plt.ylabel("Number of Restaurants")
plt.tight_layout()

plt.savefig("delivery_restaurant_count.png", dpi=300)
plt.show()

print("Delivery analysis completed successfully!")
