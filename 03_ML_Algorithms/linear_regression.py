
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Step 1: Load dataset
df = pd.read_csv("melb_data.csv")

# Step 2: Select features and target
# Step 2: Select features and target
features = [
    "Rooms",
    "Distance",
    "Bedroom2",
    "Bathroom",
    "Landsize",
    "Propertycount",
    "Type",
    "Suburb"
]

X = df[features]

# Convert categorical features into numerical columns
X = pd.get_dummies(
    X,
    columns=["Type", "Suburb"],
    drop_first=True,
    dtype=int
)

y = df["Price"]

print("Total input features:", X.shape[1])
print("Encoded feature names:")
print(X.columns.tolist())

# Step 3: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Step 4: Display dataset sizes
print("Total dataset rows:", len(df))
print("Training input shape:", X_train.shape)
print("Testing input shape:", X_test.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)

# Step 5: Create the Model:
LR = LinearRegression()

# Step 6: Train the Model
LR.fit(X_train, y_train)

print("\nModel training completed successfully!")
print("Number of training samples:", len(X_train))
print("Number of input features:", X_train.shape[1])

# Step 7: Predict house prices
y_pred = LR.predict(X_test)

# Compare actual and predicted prices
results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted price":y_pred
})

print("\nFirst 10 Actual vs Predicted Prices:")
print(results.head(10).round(2))

print("\nTotal predictions:", len(y_pred))

# Step 8: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print(f"MAE: ${mae:,.2f}")
print(f"MSE: {mse:,.2f}")
print(f"RMSE: ${rmse:,.2f}")
print(f"R2 Score: {r2:.4f}")

# Step 9: Display model coefficients

# Display feature coefficients
print("\nFeature Coefficients")
print("--------------------")

for feature, coefficient in zip(X.columns, LR.coef_):
    print(f"{feature}: {coefficient:,.2f}")

print(f"\nIntercept: {LR.intercept_:,.2f}")

# Step 10: Analyze prediction errors
results["Error"] = results["Predicted price"] - results["Actual Price"]
results["Absolute Error"] = results["Error"].abs()

print("\nPrediction Error Analysis")
print("-------------------------")
print(f"Mean Error: ${results['Error'].mean():,.2f}")
print(f"Largest Absolute Error: ${results['Absolute Error'].max():,.2f}")

print("\nFive Largest Prediction Errors:")
print(
    results.nlargest(5, "Absolute Error")[
        ["Actual Price", "Predicted price", "Error", "Absolute Error"]
    ].round(2).to_string(index=False)
)

# Step 11: Investigate the largest prediction errors

# Restore the original test-row indices
results.index = y_test.index

# Add original property details
results["Suburb"] = df.loc[results.index, "Suburb"].values
results["Rooms"] = df.loc[results.index, "Rooms"].values
results["Type"] = df.loc[results.index, "Type"].values

print("\nProperties with the 5 Largest Prediction Errors")
print("-----------------------------------------------")

print(
    results.nlargest(5, "Absolute Error")[
        [
            "Suburb",
            "Rooms",
            "Type",
            "Actual Price",
            "Predicted price",
            "Absolute Error",
        ]
    ].round(2).to_string(index=False)
)

import matplotlib.pyplot as plt

# Actual prices vs predicted prices
plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred, alpha=0.4)

# Perfect prediction reference line
minimum = min(y_test.min(), y_pred.min())
maximum = max(y_test.max(), y_pred.max())

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--"
)

plt.xlabel("Actual Price (AUD)")
plt.ylabel("Predicted Price (AUD)")
plt.title("Linear Regression: Actual vs Predicted Prices")
plt.tight_layout()
plt.show()