import numpy as np

values = np.array([-5, -2, 0, 2, 5])

# Relu
relu = np.maximum(0, values)

# Sigmoid
sigmoid = 1 / (1 + np.exp(-values))

# Tanh
tanh = np.tanh(values)


print("Input:", values)
print("ReLU:", relu)
print("Sigmoid:", sigmoid)
print("Tanh:", tanh)