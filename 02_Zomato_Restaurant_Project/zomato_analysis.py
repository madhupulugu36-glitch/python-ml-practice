"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Dataset
df = pd.read_csv(r"Zomato Restaurant Dataset.csv")

print("-----BEFORE CLEANING -----")
print("Shape:", df.shape)
print("Missing values:", df["Cuisines"].isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Handle missing Cuisines values
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

# Check cost values
print("\n-----COST ANALYSIS------")
print(df["Average Cost for two"].describe())

print("\nTop 10 heighest costs")
print(
    df.nlargest(10, "Average Cost for two")[
        ["Restaurant Name", "City",
         "Currency", "Average Cost for two"]
    ]
)

# Check rating values
print("\n------Rating Analysis-------")
print(df["Aggregate rating"].value_counts().sort_index())

# Verfy Cleaning
print("\n------After Cleaning--------")
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Save Cleande data
df.to_csv("zomato_cleaned.csv", index=False)

print("\nCleaned data Saved Successfully!")"""

# After Cleaned data saved successfulli

import pandas as pd
import matplotlib.pyplot as plt

# Load Clean dataset
df = pd.read_csv(r"zomato_cleaned.csv")

# Top 10 cities  by restaurent count
top_cities = df["City"].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_cities.plot(kind="bar")
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation = 45, ha="right")
plt.tight_layout()
plt.show()

# Restaurant rating distribution
plt.figure(figsize=(10, 5))
df["Aggregate rating"].hist(bins=20, edgecolor = "black")
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Aggregate rating")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# Votes vs rating
plt.figure(figsize=(10, 5))
plt.scatter(
    df["Votes"],
    df["Aggregate rating"],
    alpha=0.4
)

plt.title("Restaurant Votes vs Aggregate Rating")
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate Rating")
plt.tight_layout()
plt.show()

print("All three visualizations completed!")