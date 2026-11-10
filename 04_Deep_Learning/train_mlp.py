import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

tf.keras.utils.set_random_seed(42)

# 1. Training data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=np.float32)

y = np.array([0, 1, 1, 0], dtype=np.float32)

# 2. Build MLP model

model = keras.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(8, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

# 3. Compile model

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.01),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# 4. Train model
history = model.fit(
    X,
    y,
    epochs=1000,
    batch_size=2,
    verbosr=0
)

# 5. Evaluate model
loss, accuracy = model.evaluate(X, y, verbose=0)

print("Trining completed!")
print("Loss:", loss)
print("Accuracy:", accuracy)

# 6. Predictions
predictions = model.predict(X, verbose=0)

print("\nPredictions:")

for i in range(len(X)):
    print(X[i], "->", round(float(predictions[i][0])))