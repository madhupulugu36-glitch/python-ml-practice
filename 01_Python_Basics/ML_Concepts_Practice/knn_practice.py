import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#Load Dateset
CSV_Path = r"Student_Placement_Career_Prediction_Dataset.csv"
df = pd.read_csv(CSV_Path)
print(df)

#Quick Inspection
print("Shape of the Data:", df.shape)
print(df.info())
print("\nTarget Value counts:")
print(df["placement_status"].value_counts())

#Preprocessing
#-------------
#Split X and Y
y = df["placement_status"]
x = df.drop(columns= ["placement_status"])

#Drop Id Column
if "student_id" in x.columns:
    x = x.drop(columns= ["student_id"])
print(x.columns)
#One Hat Encoding for Categorical Columns
cat_cols = x.select_dtypes(include= ["object"]).columns.to_list()
print("Categorical columns:", cat_cols)

x_enc = pd.get_dummies(x, columns=cat_cols, drop_first=True)

#Encoded Traget labels (Placed/Not-Placed) -> (1/0)
le = LabelEncoder()
y_enc = le.fit_transform(y)

print("\nEncoded Features shape:")
print(x_enc)
print("\nTarget classes:")
print(list(le.classes_))

#Train Test Split
x_train, x_test, y_train, y_test = train_test_split(
    x_enc, y_enc,
    test_size=0.2,
    random_state=42,)
print("Train:", x_train.shape, "Test:", x_test.shape)

#Feature Scaling (important for K-NN)
scalr = StandardScaler()

x_train_scaled = scalr.fit_transform(x_train)
x_test_scaled = scalr.transform(x_test)

#--------------------
#Finding Best K Value
#--------------------
ks = range(1, 21)

scores = []

for k in ks:

    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(x_train_scaled, y_train)

    pred = model.predict(x_test_scaled)

    scores.append(accuracy_score(y_test, pred))

best_k = ks[int(np.argmax(scores))]

print("Best_k:", best_k, "Accuracy:", max(scores))


#------------------
#KNN model Training
#------------------
# n_neighbors: k=5
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(x_train_scaled, y_train)

y_pred = knn.predict(x_test_scaled)

#-----------
# Evaluation
#-----------
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=le.classes_)

print("\nAccuracy:", round(acc, 4))

print("\nConfusion Matrix:", cm)

print("\nClassification Reports:\n", report)