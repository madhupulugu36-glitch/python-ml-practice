import pandas as pd

# Sample categorical data
data = {
    "City": ["Hyderabad", "Chennai", "Bangalore", "Chennai", "Hyderabad"],
    "Education": ["Degree", "Masters", "PhD", "Degree", "Masters"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Label Encoding
education_mapping = {
    "Degree": 1,
    "Masters": 2,
    "PhD": 3
}

df["Education_Encoded"] = df["Education"].map(education_mapping)

print("\nAfter Label Encoding:")
print(df)

# One-Hot Encoding

df_encoded = pd.get_dummies(df, columns=["City"], dtype=int)

print("\nAfter One-Hot Encoding:")
print(df_encoded)