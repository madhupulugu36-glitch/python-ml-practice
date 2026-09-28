import pandas as pd
import numpy as np

# Data file set path
DATA_PATH = r"D:\Python-ML-Practice\01_Python_Basics\Pandas\Data_Cleaning\melb_data.csv"

# Loading Data
df = pd.read_csv(DATA_PATH)

# Shape
print("\nShape of Data:")
print("Shape:", df.shape)

# First 5 rows
print("\nFirst five rows:")
print(df.head())

# Quick Inspection
print("\nInfo:")
print(df.info())

# Describe
print("\nDescription:")
print(df.describe())

# Target
y = df["Price"]
print("y:",y)

# Feature
x = df.drop(columns= ["Price"])
print("x:", x.head(2))

# Delete columns not related to Target
x = x.drop(columns=["Address", "Propertycount", "SellerG"])
print("\nX Columns:")
print(x.columns)

# Feature Engineering
# Convert date to datetime and extract useful components
x["Date"] = pd.to_datetime(x["Date"], errors= "coerce", dayfirst=True)
x["SoldYear"] = x["Date"].dt.year
x["SoldMonth"] = x["Date"].dt.month
x["SoldDay"] = x["Date"].dt.day

# Drop raw data after extracting
x = x.drop(columns=["Date"])
print(x.head(3))

num_x = x.select_dtypes(include="number")
cat_x = x.select_dtypes(exclude="number")

print(num_x)
print(cat_x)