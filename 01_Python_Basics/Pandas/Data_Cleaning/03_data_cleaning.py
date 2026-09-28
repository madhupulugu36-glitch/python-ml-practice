import pandas as pd
import numpy as np

# Read Data
df = pd.read_csv(r"melb_data.csv")

#Info
print("Info:")
print(df.info())
# Shape
print("\nShape of data:")
print("Shape:", df.shape)

#print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

#Decription
print("\ndecription:")
print(df.describe())

#Target
y = df["Price"]
print("y:", y.head(2))

#Features
x = df.drop(columns= ["Price"])
print("x:", x.head(2))

#Delete columns not related to Target
x = x.drop(columns=["Address", "Propertycount", "SellerG"])
print("\nX Columns:", x.columns)

# Feature Engineering
# Convert date to datetime and extract useful components
x["Date"] = pd.to_datetime(x["Date"], errors= "coerce", dayfirst=True)
x["SoldYear"] = x["Date"].dt.year
x["SoldMonth"] = x["Date"].dt.month
x["SoldDay"] = x["Date"].dt.day

# Drop raw data after extracting
x = x.drop(columns= ["Date"])
print(x.head(2))