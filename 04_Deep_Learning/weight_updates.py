import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

tf.keras.utils.set_random_seed(42)

# Training data

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=np.float32)

y = np.array([0, 1, 1, 0], dtype=np.float32)

# Build MLP model

model = keras.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(4, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])


model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.01),
    loss="binary_crossentropy",
    metrics=["accuracy"]

)

# Initial Weights
initial_weights = model.get_weights()

print("INITIAL WEIGHTS")

for i, weight in enumerate(initial_weights):
    print(f"weight{i + 1}:")
    print(np.round(weight, 4))

# Train for one epoch
model.fit(X, y, epochs=1, batch_size=4, verbose=0)

# Weight after one epoch
updated_weights = model.get_weights()


print("\nWEIGHTS AFTER ONE EPOCH")
for i, weight in enumerate(updated_weights):
    print(f"Weight {i + 1}:")
    print(np.round(weight, 4))
# Calculate weight changes
print("\nWEIGHT CHANGES")
for i in range(len(initial_weights)):
    difference = updated_weights[i] - initial_weights[i]
    print(f"Change {i + 1}:")
    print(np.round(difference, 4))

# Continue training
model.fit(X, y, epochs=999, batch_size=4, verbose=0)

# Evaluate
loss, accuracy = model.evaluate(X, y, verbose=0)