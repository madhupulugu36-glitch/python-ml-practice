
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

# Select numerical columns
columns = [
    "Aggregate rating",
    "Votes",
    "Average Cost for two"
]

numeric_df = df[columns].copy()

# Convert columns to numeric values if needed
for column in columns:
    numeric_df[column] = pd.to_numeric(
        numeric_df[column], errors="coerce"
    )

# Remove rows with missing values
numeric_df = numeric_df.dropna()

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

print("----- CORRELATION MATRIX -----")
print(correlation_matrix.round(2))

# Plot correlation matrix
plt.figure(figsize=(8, 6))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(columns)),
    columns,
    rotation=30,
    ha="right"
)

plt.yticks(range(len(columns)), columns)

# Display correlation values inside the chart
for i in range(len(columns)):
    for j in range(len(columns)):
        plt.text(
            j, i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Correlation Between Rating, Votes, and Cost")
plt.tight_layout()

plt.savefig("zomato_correlation_matrix.png", dpi=300)
plt.show()

print("Correlation analysis completed successfully!")