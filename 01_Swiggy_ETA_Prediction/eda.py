
import pandas as pd

# Load the dataset
df = pd.read_csv("data/delivery_data.csv")

# 1. Dataset dimensions
print("\n--- DATASET SHAPE ---")
print(df.shape)

# 2. Column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 3. Data types and non-missing values
print("\n--- DATASET INFORMATION ---")
df.info()

# 4. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum().sort_values(ascending=False))

# 5. Duplicate rows
print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

# 6. Target variable statistics
target = "Time_taken (min)"

print("\n--- DELIVERY TIME STATISTICS ---")
print(df[target].describe())

# 7. Invalid delivery times
print("\n--- INVALID DELIVERY TIMES ---")
print("Zero or negative values:", (df[target] <= 0).sum())

print("\nEDA Step 1 completed successfully!")
