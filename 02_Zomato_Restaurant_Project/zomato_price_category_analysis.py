
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

# Keep Indian restaurants only (Country Code 1)
df = df[df["Country Code"] == 1].copy()

# Remove missing cost and rating values
df = df.dropna(
    subset=["Average Cost for two", "Aggregate rating"]
)

# Create price categories
def price_category(cost):
    if cost <= 300:
        return "Budget"
    elif cost <= 700:
        return "Moderate"
    elif cost <= 1500:
        return "Expensive"
    else:
        return "Premium"

df["Price Category"] = df["Average Cost for two"].apply(price_category)

# Calculate average rating and restaurant count
price_analysis = (
    df.groupby("Price Category")
    .agg(
        Average_Rating=("Aggregate rating", "mean"),
        Restaurant_Count=("Aggregate rating", "count")
    )
    .reindex(["Budget", "Moderate", "Expensive", "Premium"])
    .reset_index()
)

print("----- PRICE CATEGORY ANALYSIS (INDIA) -----")
print(price_analysis.to_string(index=False))

# Plot average ratings
plt.figure(figsize=(9, 5))
plt.bar(
    price_analysis["Price Category"],
    price_analysis["Average_Rating"]
)

plt.title("Average Restaurant Rating by Price Category")
plt.xlabel("Price Category")
plt.ylabel("Average Rating")
plt.tight_layout()

plt.savefig("price_category_ratings.png", dpi=300)
plt.show()

print("Price category analysis completed successfully!")
