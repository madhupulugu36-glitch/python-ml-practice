import numpy as np

# ==========================================
# PART 1: PROBABILITY
# ==========================================

# Basic Probability
favorable_outcomes = 3
total_outcomes = 6
probability = favorable_outcomes/total_outcomes
print("Probability:", probability)
print("Percentage:", probability * 100)

# ==========================================
# Sample Space and Event
# ==========================================
sample_space = [1, 2, 3, 4, 5, 6]
even_numbers = [2, 4, 6]
print("Sample Space:", sample_space)
print("Even Number Events:", even_numbers)

# ==========================================
# Calculate Probability
# ==========================================
favorable_outcomes = len(even_numbers)
total_outcomes = len(sample_space)
probability = favorable_outcomes/total_outcomes
print("Favorable Outccomes:", favorable_outcomes)
print("Total Outcomes:", total_outcomes)
print("Probability:", probability)
print("Percentage:", probability*100)
# ==========================================
# Conditional Probability
# ==========================================
total_boys = 12
passed_bpys = 8

conditional_probability = passed_bpys / total_boys
print("Conditional Probability:", conditional_probability)
print("Percentage:", conditional_probability * 100)

# ==========================================
# PART 2: STATISTICS
# ==========================================

data = np.array([10, 20, 20, 30, 40, 50])
mean = np.mean(data)
variance = np.var(data)
standared_deviation = np.std(data)

print("Data:", data)
print("Mean of Data:", mean)
print("Variance of Data:", variance)
print("Standared_deviation:", standared_deviation)

#Mean
mean = np.mean(data)
#Median
median = np.median(data)
#Mode
values, counts = np.unique(data, return_counts=True)
mode = values[np.argmax(counts)]

print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)