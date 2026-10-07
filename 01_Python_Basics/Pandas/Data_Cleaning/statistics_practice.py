import numpy as np
import pandas as pd

#Step 1 — Use this sample dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score": [40, 45, 50, 55, 60, 65, 70, 78, 85, 90]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

#Step 2 — First check the dataset
print("\nShape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nDescription:")
print(df.describe())

#Step 3 — Central tendency
print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nMode:")
print(df.mode(numeric_only=True))

#Step 4 — Variability

print("\nVariability:")
print(df.var())

print("\nStandard Deviation:")
print(df.std())

print("\nMean Absolute Deviation:")
for column in df.columns:
    mean_value = df[column].mean()
    mad = (df[column] - mean_value).abs().mean()
    print(column, ":", mad)
    

#Step 5 — Percentile and IQR

print("\n25th Percentile:")
print(df.quantile(0.25))

print("\n50th Percentile:")
print(df.quantile(0.50))

print("\n75th Percentile:")
print(df.quantile(0.75))

#Step 6 — Correlation

print("\nCorrelation:")
print(df.corr())

print("\nCovarience:")
print(df.cov())

#Step 8 — Box Plot

import matplotlib.pyplot as plt
df.boxplot(column="Exam_Score")

plt.title("Exam Score Box Plot")
plt.ylabel("Exam_Score")
plt.show()