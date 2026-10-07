import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Arjun", "Ravi", "Snehe"],
    "Age": [25, 28, None, 27, 26],
    "City": ["Hyderabad", "Chennai", "None", "Bangalure", "Chennai"],
    "Salary": [40000, 50000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

#Display Dataset
print("\nDataset:")
print(df.head())

#First 5 rows
print("\nFirst 5 rows")
print(df.head())

#Last 5 rows
print("\nLast 5 rows:")
print(df.tail())

#Shape of the Dataset
print("\nShape of data:")
print(df.shape)

#Info
print("\nDataset Information:")
print(df.info())

#statistical summary
print("\nStatistical summary")
print(df.describe())

#Checking Missing value
print("\nMissing Value:")
print(df.isnull().sum())

#Handling Missing Values with fillna()
print("\nBefore filling missing values:")
print(df)

#Fill using the Mean
# Handling missing Age using Mean

mean_age = df["Age"].mean()
print("\nMean Age:", mean_age)

df["Age"] = df["Age"].fillna(mean_age)

print("\nAfter Filling Missing Value:")
print(df)

#Fill using the Meaian
median_age = df["Age"].median()
print("\nMedian Age:", median_age)

#Missing Values — Mode
mode_city = df["City"].mode()[0]
print("\nMode City:", mode_city)

df["City"] = df["City"].fillna(mode_city)

print("\nAfter Filling City:")
print(df)