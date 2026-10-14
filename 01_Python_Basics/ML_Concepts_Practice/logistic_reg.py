import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#--------------------------
# Load Dataset
#--------------------------

df = pd.read_csv(r"student_placement_200.csv")

#----------------------------
# Remove unnecessary columns
#----------------------------

df.drop(["student_id"], axis=1, inplace=True)

#----------------------------
# Check missing values
#----------------------------

print("Missing values")
print(df.isna().sum())

#------------------------------------
# Convert Target column into numbers
#------------------------------------
d = {
    "Not Placed": 0,
    "Placed": 1
}

df["placement_status"] = df["placement_status"].map(d)

#-----------------------------
# Check unique target values
#-----------------------------
print("\nUnique Target values:")
print(df["placement_status"].unique())

#-----------------------------
# Display dataset
#-----------------------------
print("\nFirst 5 rows:")
print(df.head())

#-----------------------------
# Check non-numerical columns
#-----------------------------
print("\n Non-Numerical columns:")
print(df.select_dtypes(exclude= "number"))

#--------------------------------------
# Separate Features (x) and Traget (y)
#--------------------------------------
y = df["placement_status"]
print("\nTarget values:")
print(y.head(2))

x = df.drop(columns= ["placement_status"])
print("\nFeatures values:")
print(x.head(2))

#--------------------------
# Train Test Spilt
#--------------------------
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.20, random_state=15)

print("\nDataset Shapes:")
print("x_train shape", x_train.shape)
print("x_test shape:", x_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

#-----------------------------------
# Create Logisitic Regression model
#-----------------------------------
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(x_train, y_train) #fit for train model

train_predictions = LR.predict(x_train) #predict for test model

print(confusion_matrix(y_train, train_predictions))

print(classification_report(y_train, train_predictions))