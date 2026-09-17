import pandas as pd
print("Pandas Version:", pd.__version__)

data = {
    "Name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "Age": [25, 28, 26, 24, 30],
    "Department": ["IT", "QA", "Data", "HR", "IT"],
    "Salary": [45000, 50000, 55000, 40000, 65000]
}
df = pd.DataFrame(data)
print("\nEmployee Data:")
print(df)
print("=============")

"""print("\nFirst 3 rows:")
print(df.head(3))
print("=============")

print("\nLast 2 rows:")
print(df.tail(2))
print("=============")

print("\nShape:")
print(df.shape)
print("=============")

print("\nColumns:")
print(df.columns)
print("=============")

print("\nData Types:")
print(df.dtypes)
print("=============")

print("\nInformation:")
df.info()
print("=============")


print("SELECTING COLUMNS:")
print("=============")

print("\nName Column:")
print(df["Name"])
print("=============")

print("\nSalary Column:")
print(df["Salary"])
print("=============")

print("\nName and Salary Columns:")
print(df[["Name", "Salary"]])
print("=============")

print("\nAge Column:")
print(df["Age"])
print("=============")

print("\nName and Department Columns:")
print(df[["Name", "Department"]])
print("=============")

print("\nAge and Salary Columns:")
print(df[["Age", "Salary"]])
print("================")


print("SELECTING ROWS")
print("================")

print("\nFirst row:")
print(df.iloc[0])
print("================")

print("\nSecond row:")
print(df.iloc[1])
print("================")

print("\nSelecting Multiple rows:")
print(df.iloc[0:3])
print("================")

print("\nSelect Last 2 rows:")
print(df.iloc[-2:])
print("================")

print("\nSelect rows 0, 2 and 4:")
print(df.iloc[[0, 2, 4]])
print("================")

print("\nFirst 3 Rows and First 2 Columns:")
print(df.iloc[0:3, 0:2])
print("================")

print("\nFirst 2 Rows and First 3 Columns:")
print(df.iloc[0:2, 0:3])
print("================")

print("\nRahul Details:")
print(df.iloc[0, [0, 2, 3]])
print("================")

print("\nName + Salary for Rahul, Priya, Arjun:")
print(df.iloc[0:3, [0, 3]])
print("================")

print("\nAge + Department for Arjun, Sneha, Kiran:")
print(df.iloc[2:5, [1, 2]])
print("================")

print("\nPriya's Name + Department + Salary:")
print(df.iloc[1, [0, 2, 3]])
print("================")

print("LOC PRACTICE")
print("================")

print("\nFirst Row:")
print(df.loc(0))
print("================")

print("\nRows 0 to 2:")
print(df.loc[0:2])

print("\nPrint Rahul and Arjun:")
print(df.loc[[0, 2]])
print("================")

print("\nName and Salary:")
print(df.loc[:, ["Name", "Salary"]])
print("================")

print("\nGet Priya's complete row using loc:")
print(df.loc[1])
print("================")

print("\nGet Rahul, Arjun and Kiran using loc:")
print(df.loc[[0, 2, 4]])
print("================")

print("\nGet Name and Salary for Arjun, Sneha and Kiran:")
print(df.loc[2:4, ["Name", "Salary"]])
print("================")

print("FILTERING")
print("================")

print("\nEmployees Olde than 25:")
print(df[df["Age"] > 25])
print("================")

print("\nEmployees whose salary is greater than 50000:")
print(df[df["Salary"] > 50000])
print("================")

print("\nEmployees whose age is less than 28:")
print(df[df["Age"] < 28])
print("================")

print("\nEmployees from the IT department:")
print(df[df["Department"] == "IT"])
print("================")

print("\nEmployees whose salary is exactly 50000:")
print(df[df["Salary"] == 50000])
print("================")

print("\nEmployees whose age is greater than 25 AND salary is greater than 50,000.")
print(df[(df["Age"] > 25) & (df["Salary"] > 50000)])
print("================")

print("\nEmployees from IT OR QA:")
print(df[(df["Department"] == "IT") | df["Department"] == "QA"])
print("================")


print(df[(df["Age"] >= 25) & (df["Salary"] >= 50000)])
print("================")

print(df[(df["Department"] == "IT") | (df["Department"] == "HR")])
print("================")

print(df[(df["Salary"] > 45000) & (df["Age"] < 30)])
print("================")

print(df[(df["Age"] > 25) & (df["Department"] == "IT")])
print("================")


#Sort by salary — ascending
#==========================

print(df.sort_values("Salary", ascending=False))
print("=============")

print(df.sort_values("Age", ascending=True))
print("=============")

print(df.sort_values(["Department", "Salary"], ascending=[True, False]))
print("=============")

print(df.sort_values("Name"))
print("=============")

print("ADDING COLUMNS")
print("================")
df["Annual Salary"] = df["Salary"] * 12
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

df["Total Compensation"] = df["Salary"] + df["Bonus"]
print(df)

df["Experience Level"] = "Junior"
print(df)

print(df[["Name", "Salary", "Bonus", "Total Compensation"]])

print("\n================")
print("MISSING VALUES")
print("================")

missing_data = {
    "Name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "Age": [25, 28, None, 24, 30],
    "Department": ["IT", "QA", "Data", None, "IT"],
    "Salary": [45000, 50000, 55000, 40000, None]
}
df_missing = pd.DataFrame(missing_data)
print(df_missing)

print(df_missing.isnull().sum())

print(df_missing[df_missing.isnull().any(axis=1)])

print("\n================")
print("DROP MISSING ROWS")
print("================")

print(df_missing.dropna())

print("\n================")
print("Replace missing values")
print("================")

print(df_missing["Age"].fillna(0))

print("\n================")
print("Fill missing Age with average age")
print("================")

average_age = df_missing["Age"].mean()
print("Average Age:", average_age)
df_missing["Age"] = df_missing["Age"].fillna(average_age)
print(df_missing)

df_missing["Department"] = df_missing["Department"].fillna("Unknown")

average_salary = df_missing["Salary"].mean()
print("Average Salary:", average_salary)
df_missing["Salary"] = df_missing["Salary"].fillna(average_salary)

print("\nFinal DataFrame:")
print(df_missing)

print("\nRemaining missing values:")
print(df_missing.isnull().sum())"""

print("\n================")
print("DUPLICATE DATA")
print("================")

duplicate_data = {
    "Name": ["Rahul", "Priya", "Arjun", "Rahul", "Kiran", "Priya"],
    "Age": [25, 28, 26, 25, 30, 28],
    "Department": ["IT", "QA", "Data", "IT", "IT", "QA"],
    "Salary": [45000, 50000, 55000, 45000, 65000, 50000]
}

df_duplicates = pd.DataFrame(duplicate_data)
print(df_duplicates)
print("================")

print("\nDuplicate rows:")
print(df_duplicates.duplicated())
print("================")

print("\nNumber of Duplicate rows:")
print(df_duplicates.duplicated().sum())
print("================")

print("\nOnly Duplicate rows:")
print(df_duplicates[df_duplicates.duplicated()])
print("================")

df_clean = df_duplicates.drop_duplicates()
print("\nAfter Removing Duplicates:")
print(df_clean)

print("\n================")
print("GROUPBY PRACTICE")
print("================")

department_groups = df.groupby("Department")
print(department_groups["Name"].count())
print(department_groups["Salary"].count())
print(department_groups["Salary"].sum())
print(department_groups["Salary"].mean())

df.groupby("Department")["Salary"].min()
df.groupby("Department")["Salary"].max()
df.groupby("Department")["Age"].mean()
df.groupby("Department")["Name"].count()
df.groupby("Department")["Salary"].agg(["min", "max"])