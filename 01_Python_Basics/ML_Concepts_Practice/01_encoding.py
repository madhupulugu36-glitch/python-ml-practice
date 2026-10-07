import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Sample dataset

data = {
    "City": ["Hyderabad", "Chennai", "Bangalore", "Chennai", "Hyderabad"],
    "Education": ["Degree", "Masters", "PhD", "Degree", "Masters"]
}

df = pd.DataFrame(data)

print(df)


# Label Encoding for Education

le = LabelEncoder()

df["education_encoded"] = le.fit_transform(df["Education"])


# One-Hot Encoding for City

df = pd.get_dummies(df, columns=["City"])

print(df)