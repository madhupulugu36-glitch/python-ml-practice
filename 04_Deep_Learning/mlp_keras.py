import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Set random seed
tf.keras.utils.set_random_seed(42)

# XOR input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=np.float32)

# Expected output
y = np.array([0, 1, 1, 0], dtype=np.float32)

# Create MLP model
model = keras.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(8, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

# Display model architecture
model.summary()

# Compile model
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train model
model.fit(
    X,
    y,
    epochs=1000,
    batch_size=2,
    verbose=0
)

# Evaluate model
loss, accuracy = model.evaluate(X, y, verbose=0)

print("Training completed!")
print("Loss:", loss)
print("Accuracy:", accuracy)

# Predictions
predictions = model.predict(X, verbose=0)

print("\nXOR Predictions:")

for i in range(len(X)):
    print(X[i], "->", round(float(predictions[i][0])))