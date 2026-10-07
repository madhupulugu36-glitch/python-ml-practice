import pandas as pd

#Sample data
data = {
    "Name": ["Rahul", "Priya", "Arjun", "Ravi", "Sneha", "Kiran"],
    "Age": [25, 28, None, 27, 26, 29],
    "City": ["Hyderabad", "Chennai", "Hyderabad", None, "Chennai", "Bangalore"],
    "Education": ["Degree", "Masters", "PhD", "Degree", None, "Masters"],
    "Salary": [40000, 50000, 60000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)
print("Orginal data:")
print(df)

#T1-1. Number of rows and columns
print("\nNumber of Columns:")
print(df.shape)

#T1-2. Data types
print("\nData types of data:")
print(df.dtypes)

#T1-3.Statistical summary
print("\nStatistical summary:")
print(df.describe())

#T1-4. Missing values
print("\nFind missing values:")
print(df.isnull().sum())

#T1-5. Columns Names
print("\nColumns names:")
print(df.columns)

#T2-1. Missing Age Value Handle by mean
mean_age = df["Age"].mean()
print("\nMeaan Age:", mean_age)
df["Age"] = df["Age"].fillna(mean_age)
print("\nAfter filling Missing Value:")
print(df)

#T2-2. Missing City Value Handle by Mode
mode_city = df["City"].mode()[0]
print("\nMode of City:", mode_city)
df["City"] = df["City"].fillna(mode_city)
print("\nAfter City replace with mode:")
print(df)

#T2-3. Missing Education Value Handle by Mode
mode_educ = df["Education"].mode()[0]
print("\nMode of Education:", mode_educ)
df["Education"] = df["Education"].fillna(mode_educ)
print("\nAfter Education replace with mode:")
print(df)

#T3-1. City One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=["City"], dtype=int)
print("\nAfter City Encoded")
print(df_encoded)

#T3-2. Education Label Encoding
education_mapping = {
    "Degree": 1,
    "Masters": 2,
    "PhD": 3
}

df_encoded["Education_Encoded"] = df_encoded["Education"].map(education_mapping)
print("\nAfter Education Lable Encoding:")
print(df_encoded)

#T4 checking null values
print(df_encoded.isnull().sum())

#T5. Check duplicate rows
print("\nNumber of Duplicate Rows:")
print(df_encoded.duplicated().sum())

#T6. Remove duplicate rows
df_encoded = df_encoded.drop_duplicates()
print("\nAfter Removing Duplicates:")
print(df_encoded)

#T7. Check unique values
print("\nUnique Cities:")
print(df["City"].unique())

print("\nUnique Education:")
print(df["Education"].unique())

#T8. Check value counts
print("\nCity Value Counts:")
print(df["City"].value_counts())

print("\nEducation Value Counts:")
print(df["Education"].value_counts())