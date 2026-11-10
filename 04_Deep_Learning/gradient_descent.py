# Gradient Descent from Scratch

# Initial parameter
w = 0

# Learning rate
learning_rate = 0.01

# Number of iterations
iterations = 50

# Loss function
def loss_function(w):
    return (w - 5) ** 2

# Gradient (derivative)
def gradient(w):
    return 2 * (w - 5)

# Gradient Descent
for i in range(iterations):
    loss = loss_function(w)
    grad = gradient(w)

    # Update parameter
    w = w - learning_rate * grad

    if i % 5 == 0:
        print(f"Iteration: {i}, Weight: {w:.4f}, Loss: {loss:.4f}")

print("\nFinal Weight:", round(w, 4))
print("Final Loss:", round(loss_function(w), 4))