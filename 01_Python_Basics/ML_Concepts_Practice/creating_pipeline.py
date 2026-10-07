import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Dataset file path
DATA_PATH = r"D:\Python-ML-Practice\01_Python_Basics\ML_Concepts_Practice\melb_data.csv"

#Loading Data
df = pd.read_csv(DATA_PATH)

#Shape of Data
print("\nShape of Data:")
print(df.shape)

#Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

#Quick Inspection
print("\nInfo:")


#Numerical columns
print("\nNumerical Columns data:")
print(df.describe())

# Features
x = df.drop(columns=["Price"])

# Target
y = df["Price"]

# Remove unnecessary feature columns
x = x.drop(columns=["Address", "Propertycount", "SellerG"])

print("\nX Columns:")
print(x.columns)

print("\nY:")
print(y.head())

# Feature Engineering
# Convert date to datetime and extract useful components
x["Date"] = pd.to_datetime(x["Date"], errors= "coerce", dayfirst=True)
x["SoldYear"] = x["Date"].dt.year
x["SoldMonth"] = x["Date"].dt.month
x["SoldDay"] = x["Date"].dt.day

#Drop Raw data after extracting
x = x.drop(columns=["Date"])
print(x.columns)
print(x.head(2))

#Separation of Numarical data and Categorical data
x_num = x.select_dtypes(include= "number")
print(x_num.head(2))

x_cat = x.select_dtypes(exclude= "number")
print(x_cat.head(2))

#Processing Piprline (Impute + Encoded + Scale)
#Numaric: median impute + scale
num_transformations = Pipeline(steps= [("imputer", SimpleImputer(strategy= "median")),
                 ("scaling", StandardScaler())])

#Categorical: mode(most - frequent) impute + one-hot encode
cat_transformations = Pipeline(steps= [("imputer", SimpleImputer(strategy= "most_frequent")),
                 ("onehot", OneHotEncoder(handle_unknown= "ignore"))])

perprocessor = ColumnTransformer(transformers = [("num", num_transformations, x_num),
                                     ("cat", cat_transformations, x_cat)],
                    remainder= "drop")
print(perprocessor)

print(x_num.head())
print(x_cat.head())

#Train and test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.15)

print("\nShape of X_Train")
print(x_train.shape)
print("\nShape of X_Test")
print(x_test.shape)

#Train Lean