import pandas as pd
study_hours = [1, 2, 3, 4, 5]
exam_score = [35, 40, 50, 60, 70]

df = pd.DataFrame({
    "study_hours": study_hours,
    "exam_score": exam_score
})

correlation = df["study_hours"].corr(df["exam_score"])

print("Correlation:", correlation)