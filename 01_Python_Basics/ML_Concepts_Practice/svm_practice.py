import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Dataset
Dataset = r"iris.csv"

df = pd.read_csv(Dataset)

print(df.shape)
print(df.head())
print(df.columns)

print(df["species"].unique())

# Features and Target
y = df["species"]
x = df.drop(columns=["species"])

print("\nTarget Value Counts:")
print(y.head())

print("\nFeature Columns:")
print(x.head())

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("\nX_Train data Shape:")
print(x_train.shape)

print("\nX_Test data Shape:")
print(x_test.shape)

print("\nY_Train data Shape:")
print(y_train.shape)

print("\nY_Test data Shape:")
print(y_test.shape)


# Create SVM Model
models = {
    "Limear": SVC(kernel="linear", C=1),
    "RBF": SVC(kernel="rbf", C=1, gamma=1),
    "Polynomial": SVC(kernel="poly", C=1)
    }
for name, model in models.items():
    #Train the model
    model.fit(x_train, y_train)
    
    #Prediction
    y_pred = model.predict(x_test)
    
    #Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n{name} SVM Model Accuracy:")
    print(accuracy)

# Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Classification Report

report = classification_report(y_test, y_pred)

print("\nClassification Report:")
print(report)

# Visualize Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["setosa", "versicolor", "virginica"],
            yticklabels=["setosa", "versicolor", "virginica"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("SVM Confusion Matrix")
plt.show()

# Actual vs Predicted

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nActual vs Predicted:")
print(comparison)