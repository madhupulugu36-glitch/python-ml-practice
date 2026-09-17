import pandas as pd
import numpy as np

# Make random data repeateable

np.random.seed(42)

# Number of Employees
number_of_employees =10000

# Employees Names
names = [f"employee_{i}" for i in range(1, number_of_employees + 1)]

# Departments
departments = np.random.choice(
    ["IT", "QA", "Data", "HR", "Finance", "Sales"],
    number_of_employees
)

# Age: 21 to 60
ages = np.random.randint(21, 61, number_of_employees)

# Salary: 25,000 to 1,20,000
salaries = np.random.randint(25000 , 120001, number_of_employees)

# Experience: 0 to 15 years
experience = np.random.randint(0, 16, number_of_employees)

# Cities
cities = np.random.choice(
    ["Hyderabad", "Bangalore", "Chennai", "Pune", "Mumbai", "Delhi"],
    number_of_employees
)

# Creating Data frames
df = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "Departments": departments,
    "Salary": salaries,
    "Experience": experience,
    "Cities": cities
})

print("Dataset Created Successfully!")

print("\nFirst 10 rows:")
print(df.head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\n==============================")
print("LARGE DATA EXPLORATION")
print("==============================")

print("\nFirst 20 Rows:")
print(df.head(20))

print("\nLast 10 Rows:")
print(df.tail(10))

print("\nRandom 10 Rows")
print(df.sample(10))

print("\n==============================")
print("BASIC STATISTICS")
print("==============================")

print(df.describe())

print("\nMinimum Salary:")
print(df["Salary"].min())

print("\nMaximum Salary:")
print(df["Salary"].max())

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nMedian Salary:")
print(df["Salary"].median())

print("\nMinimum Age:")
print(df["Age"].min())

print("\nMaximum Age:")
print(df["Age"].max())

print("/nAverage Age:")
print(df["Age"].mean())

print("\nMedian Age:")
print(df["Age"].median())

print("\n==============================")
print("LARGE DATA FILTERING")
print("==============================")

high_salary = df[df["Salary"] > 100000]
print("\nEmployees Earning more then 100000:")
print(high_salary)

print(high_salary.head(20))

print("\nNumber of Employees earn more then 100000:")
print(len(high_salary))

young_employees = df[df["Age"] < 30]
print("\nEmployees younger then 30:")
print(young_employees.head(20))

print("\nNumber of Young Employees:")
print(len(young_employees))

experienced_high_salary = df[(df["Salary"] > 100000) & (df["Experience"] > 10)]

print("\nHigh Salary and High Experience:")
print(experienced_high_salary.head(20))

print("\nNumber of High Salary and High Experience Employees:")
print(len(experienced_high_salary))

young_high_salary_experienced_employees = df[(df["Age"] < 30) & (df["Salary"] > 80000) & (df["Experience"] >= 5)]
print("\nyoung_high_salary_experienced_employees:")
print(young_high_salary_experienced_employees.head(20))

print("\nyoung_high_salary_experienced_employees:")
print(len(young_high_salary_experienced_employees))

print("\n==============================")
print("LARGE DATA SORTING")
print("==============================")
top_10_salary = df.sort_values(
     "Salary", ascending=False
     ).head(10)
print("\nTop 10 Heighest paid employees:")
print(top_10_salary)

top_10_experience = df.sort_values(
    "Experience", ascending=False
).head(10)
print("\nTop 10 Experienced Employees:")
print(top_10_experience)

youngest_10 = df.sort_values(
    "Age", ascending=True
).head(10)
print("\nYoungest 10 Employees:")
print(youngest_10)

department_salary = df.sort_values(
    ["Departments", "Salary"],
    ascending=[True, False]
)

print("\nDepartment + Salary Sorting:")
print(department_salary.head(20))

print("\n==============================")
print("GROUPBY PRACTICE")
print("==============================")

department_count = df.groupby("Departments")["Name"].count()
print("\nDepartments Count:")
print(department_count)

average_salary_department = df.groupby("Departments")["Salary"].mean()
print("\nAverage Salary by Departments:")
print(average_salary_department)

total_salary_department = df.groupby("Departments")["Salary"].sum()
print("\nTotal Salary by Department:")
print(total_salary_department)

salary_range_department = df.groupby("Departments")["Salary"].agg(
    ["min", "max"]
)
print("\nMinimum and Maximum Salary by Departments:")
print(salary_range_department)

department_summary = df.groupby("Departments").agg(
    Employee_Count = ("Name", "count"),
    Average_Salary = ("Salary", "mean"),
    Maximum_Salary = ("Salary", "max"),
    Minimum_Salary = ("Salary", "min"),
    Average_Experience = ("Experience", "mean")
)
print("\nDepartments Summary:")
print(department_summary)

print("\n==============================")
print("CITY ANALYSIS")
print("==============================")

city_count = df.groupby("Cities")["Name"].count()
print("\nEmployees by City:")
print(city_count)

city_average_salary = df.groupby("Cities")["Salary"].mean()
print("\nAverage Salary by City:")
print(city_average_salary)

city_total_salary = df.groupby("Cities")["Salary"].sum()
print("\nTotal Salary by City:")
print(city_total_salary)

city_summary = df.groupby("Cities").agg(
    Employee_Count = ("Name", "count"),
    Average_Salary = ("Salary", "mean"),
    Minimum_Salary = ("Salary", "min"),
    Maximum_Salary = ("Salary", "max"),
    Average_Experience = ("Experience", "mean")
)
print("\nCity Summary:")
print(city_summary)

department_city = df.groupby(
    ["Departments", "Cities"]
)["Salary"].mean()
print("\nAverage Salary by Department and City:")
print(department_city)

print("\n==============================")
print("CALCULATED COLUMNS")
print("==============================")

df["Annual_Salary"] = df["Salary"] * 12
print("\nAnnual Salary:")
print(df[["Name", "Salary", "Annual_Salary"]].head(10))

df["Bonus"] = df["Salary"] * 0.10
print('\nBonus')
print(df[["Name", "Salary", "Bonus"]].head(10))

df["Total_Compensation"] = df["Salary"] + df["Bonus"]
print("\nTotal Compensation:")
print(df[["Name", "Salary", "Bonus", "Total_Compensation"]].head(10))

def experience_level(exp):

    if exp <= 2:
        return "Fresher"

    elif exp <= 5:
        return "Junior"

    elif exp <= 10:
        return "Mid-level"

    else:
        return "Senior"


df["Experience_Level"] = df["Experience"].apply(experience_level)

print("\nExperience Level:")
print(df[["Name", "Experience", "Experience_Level"]].head(20))

print("\Experience Level Count:")
print(df["Experience_Level"].value_counts())

print("\n==============================")
print("SAVING DATA")
print("==============================")

df.to_csv("employees_10000.csv", index=False)

print("10,000 employee data saved successfully!")