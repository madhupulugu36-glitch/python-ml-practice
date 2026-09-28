x1 = 5
y1 = x1 ** 2

derivative1 = 2 * x1

print("x1 =", x1)
print("y1 =", y1)
print("Derivative1 =", derivative1)
print("=============")

x2 = 3
y2 = 4

partial_x2 = 2 * x2
partial_y2 = 2 * y2
gradient = [partial_x2, partial_y2]

print("Partial derivative with respect to x2:", partial_x2)
print("Partial derivative with respect to y2:", partial_y2)
print("Gradient:", gradient)
print("=============")

x3 = 3
inside = 2 * x3 + 1
derivative2 = 4 * inside

print("Inside Values:", inside)
print("Derivative:", derivative2)
print("=============")

w1 = 5
loss1 = w1 ** 2

print("Weight1:", w)
print("Loss:", loss)