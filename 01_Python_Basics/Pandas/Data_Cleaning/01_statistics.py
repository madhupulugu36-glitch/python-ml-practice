import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Sample Data
data = np.array([2, 4, 6, 8, 10, 50])

#Mean
mean = np.mean(data)
print("Mean:", mean)

#Population Variance
variance = np.var(data)
print("Variance:", variance)

#Population Standard Deviation
std = np.std(data)
print("Standard Deviation:", std)

#Mean Absolute deviation
mad = np.mean(np.abs(data - np.mean(data)))
print("Mean Absolute deviation:", mad)

#Percentaile
p25 = np.percentile(data, 25)
p50 = np.percentile(data, 50)
p75 = np.percentile(data, 75)

print("25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th percentile", p75)

#Interquartile Range
iqr = p75 - p25
print("IQR:", iqr)

#Outlier boundaries
lower_bound = p25 - (1.5 * iqr)
upper_bound = p75 + (1.5 * iqr)

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

#Find outliers
outliers = data[(data<lower_bound)|(data>upper_bound)]
print("Outliers:", outliers)

#Box plot
plt.boxplot(data)
plt.title("Box plot")
plt.ylabel("Values")
plt.show()

#Positive Correlation
study_hours = np.array([1, 2, 3, 4, 5])
exam_score = np.array([50, 60, 70, 80, 90])

correlation = np.corrcoef(study_hours, exam_score)[0, 1]
print("Positive Correlation:", correlation)

#Negative Correlation
work_hours = np.array([1, 2, 3, 4, 5])
free_time = np.array([9, 8, 7, 6, 5,])

correlation = np.corrcoef(work_hours, free_time)[0, 1]

print("Negative Correlation:", correlation)

#Covariance
covariance_matrix1 = np.cov(study_hours, exam_score)
print("Covariance Matrix:", covariance_matrix1)

print("Covariance:", covariance_matrix1[0, 1])

covariance_matrix2 = np.cov(work_hours, free_time)
print("Covariance:", covariance_matrix2[0, 1])