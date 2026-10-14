
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

# Remove rows with missing country or rating
df = df.dropna(subset=["Country Code", "Aggregate rating"])

# Country code to country name mapping
country_names = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zealand",
    162: "Philippines",
    166: "Qatar",
    184: "Singapore",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "United Kingdom",
    216: "United States"
}

df["Country"] = df["Country Code"].map(country_names)

  # Calculate average rating and restaurant count
country_rating = (
    df.groupby("Country")
    .agg(
        Average_Rating=("Aggregate rating", "mean"),
        Restaurant_Count=("Aggregate rating", "count")
    )
    .reset_index()
    .sort_values("Average_Rating", ascending=False)
)

print("----- COUNTRY-WISE RESTAURANT RATINGS -----")
print(country_rating.to_string(index=False))

# Plot average ratings
plt.figure(figsize=(12, 6))
plt.bar(
    country_rating["Country"],
    country_rating["Average_Rating"]
)

plt.title("Average Restaurant Rating by Country")
plt.xlabel("Country")
plt.ylabel("Average Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("country_wise_ratings.png", dpi=300)
plt.show()

print("Country analysis completed successfully!")