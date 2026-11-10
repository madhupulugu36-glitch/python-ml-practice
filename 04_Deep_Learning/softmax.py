import numpy as np

def softmax(x):
    exp_values = np.exp(x - np.max(x))
    return exp_values / np.sum(exp_values)

scores = np.array([2.0, 1.0, 0.5])

probabilities = softmax(scores)

print("Scores:", scores)
print("Probabilities:", probabilities)
print("Total:", np.sum(probabilities))

classes = ["Cat", "Dog", "Bird"]

for name, probability in zip(classes, probabilities):
    print(name, ":", round(probability * 100, 2), "%")