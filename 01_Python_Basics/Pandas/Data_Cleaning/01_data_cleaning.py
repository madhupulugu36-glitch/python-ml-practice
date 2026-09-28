import pandas as pd
import numpy as np

# Dataset File path
DATA_PATH = r"D:\Python-ML-Practice\01_Python_Basics\Pandas\Data_Cleaning\melb_data.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Shape
print("Shape:", df.shape)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Missing value percentage
missing_count = df.isnull().sum()
missing_percentage = (missing_count / len(df)) * 100

missing_data = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage
})

# Show only columns with missing values
print("\nMissing Value Analysis:")
print(missing_data[missing_data["Missing_Count"] > 0])

print("\nCar Statistics:")
print(df["Car"].describe())

print("\nBuildingArea Statistics:")
print(df["BuildingArea"].describe())

print("\nYearBuilt Statistics:")
print(df["YearBuilt"].describe())

print("\nCouncilArea Values:")
print(df["CouncilArea"].value_counts(dropna=False).head(10))

# Handle simple missing values

df["Car"] = df["Car"].fillna(df["Car"].median())

df["CouncilArea"] = df["CouncilArea"].fillna("Unknown")

print("\nMissing values after handling Car and CouncilArea:")
print(df[["Car", "CouncilArea"]].isnull().sum())


# Investigate YearBuilt
print("\nYearBuilt below 1800:")
print(df[df["YearBuilt"] < 1800][["YearBuilt", "Price", "Rooms", "Suburb"]])


# Investigate BuildingArea outliers
print("\nLargest BuildingArea values:")
print(df[["BuildingArea", "Price", "Rooms", "Suburb"]]
      .sort_values("BuildingArea", ascending=False)
      .head(10))

# Replace invalid YearBuilt values with NaN

df.loc[df["YearBuilt"] < 1800, "YearBuilt"] = np.nan

print("\nYearBuilt after removing invalid values:")
print(df["YearBuilt"].describe())

print("\nMissing YearBuilt:")
print(df["YearBuilt"].isnull().sum())