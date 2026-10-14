import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# ============================================================
# 1. Load Dataset
# ============================================================

df = pd.read_csv(r"student_placement_200.csv")


# ============================================================
# 2. Remove Unnecessary Column
# ============================================================

df.drop(["student_id"], axis=1, inplace=True)


# ============================================================
# 3. Check Missing Values
# ============================================================

print("Missing Values:")
print(df.isna().sum())


# ============================================================
# 4. Convert Target Column into Numbers
# ============================================================

d = {
    "Not Placed": 0,
    "Placed": 1
}

df["placement_status"] = df["placement_status"].map(d)


# Check unique target values
print("\nUnique Target Values:")
print(df["placement_status"].unique())


# ============================================================
# 5. Display Dataset
# ============================================================

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 6. Check Non-Numeric Columns
# ============================================================

print("\nNon-Numeric Columns:")
print(df.select_dtypes(exclude="number"))


# ============================================================
# 7. Separate Features (X) and Target (y)
# ============================================================

y = df["placement_status"]

print("\nTarget Values:")
print(y.head(2))


x = df.drop(columns=["placement_status"])

print("\nFeatures:")
print(x.head(2))


# ============================================================
# 8. Train-Test Split
# ============================================================

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=77
)


print("\nDataset Shapes:")
print("X Train:", x_train.shape)
print("X Test :", x_test.shape)
print("Y Train:", y_train.shape)
print("Y Test :", y_test.shape)


# ============================================================
# 9. Create Decision Tree Model
# ============================================================

DT = DecisionTreeClassifier(
    class_weight="balanced",
    random_state=77
)


# ============================================================
# 10. Train Model
# ============================================================

model_train = DT.fit(x_train, y_train)

print("\nDecision Tree Model:")
print(model_train)


# ============================================================
# 11. Predictions
# ============================================================

test_predictions = DT.predict(x_test)

train_predictions = DT.predict(x_train)


print("\nTest Predictions:")
print(test_predictions)


# ============================================================
# 12. Accuracy
# ============================================================

train_accuracy = accuracy_score(
    y_train,
    train_predictions
)

test_accuracy = accuracy_score(
    y_test,
    test_predictions
)


print("\nTraining Accuracy:")
print(train_accuracy)

print("\nTesting Accuracy:")
print(test_accuracy)


# ============================================================
# 13. Test Confusion Matrix
# ============================================================

cm_test = confusion_matrix(
    y_test,
    test_predictions
)

print("\nTest Confusion Matrix:")
print(cm_test)


# ============================================================
# 14. Test Classification Report
# ============================================================

report_test = classification_report(
    y_test,
    test_predictions
)

print("\nTest Classification Report:")
print(report_test)


# ============================================================
# 15. Training Confusion Matrix
# ============================================================

cm_train = confusion_matrix(
    y_train,
    train_predictions
)

print("\nTraining Confusion Matrix:")
print(cm_train)


# ============================================================
# 16. Training Classification Report
# ============================================================

report_train = classification_report(
    y_train,
    train_predictions
)

print("\nTraining Classification Report:")
print(report_train)

# ============================================================
# 17. Random Forest Classifier
# ============================================================

RF = RandomForestClassifier(n_estimators = 99, class_weight= "balanced")
RF.fit(x_train, y_train)

test_predictions = RF.predict(x_test)

train_predictions = RF.predict(x_train)


print("\nTest Predictions:")
print(test_predictions)