import numpy as np

# Creating NumPy Arrays
#======================
a1 = np.array([1, 2, 3]) # 1 Dimentional Array
a2 = np.array([[1, 2, 3],
              [4, 5, 6]]) # 2 Dimentional Array
a3 = np.array([[[1, 2], [3, 4]],
               [[5, 6], [7, 8]]]) # 3 Dimentional Array

print("a1:", a1)
print(".................")
print("a2:", a2)
print(".................")
print("a3:", a3)
print(".................")

# Using Numpy Functions
#======================
a0 = np.zeros((3, 3))

ao = np.ones((2, 2))

ar = np.arange(0, 10, 2)

print("a0:", a0)
print(".................")
print("ao:", ao)
print(".................")
print("ar:", ar)
print(".................")

# NumPy Array Indexing
#=====================

a4 = np.array([10, 20, 30, 40, 50])
print("single element:", a4[2])  # single element
print(".................")
print("last element:", a4[-1]) # last element
print(".................")
a5= np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("row1 and column 0 element:", a5[1, 0]) # row 1, column 0

# Basic Arithmetic Operations
#============================
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Addition of x and y:", x + y) # Addition
print(".................")
print("Subtraction of x and y:", x - y) # Subtraction
print(".................")
print("Multiplication of x and y:", x * y) # Multiplication
print(".................")
print("Matrix multiplication of x and y:", x @ y) # Matrix - Multiplication
print(".................")
print("Division of x and y:", x / y) # Division
print(".................")

# Unary Operation
#================
a7 = np.array([-3, -2, -1, 0, 1, 2, 3])
print(np.absolute(a7))
print(".................")

# Binary Operators
#=================
a8 = np.array([1, 2, 3])
a9 = np.array([4, 5, 6])

res = np.add(a8, a9) # Applying a binary operation: addition
print(res)
print(".................")

# Mathematical Functions
#=======================
b1 = np.array([0, np.pi/2, np.pi])
print(np.sign(b1)) # create an array of sine values
print(".................")
b2 = np.array([0, 1, 2, 3, 4]) 
print("exponential:", np.exp(b2)) # exponential values
print(".................")
print(np.sqrt(b2))
print(".................")
print("square root of b1:", np.sqrt(b1)) # square root of array values
print(".................")

# Sorting Arrays
#===============
import numpy as np

dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
vals  = [('Hrithik', 2009, 8.5),
         ('Ajay',    2008, 8.7),
         ('Pankaj',  2008, 7.9),
         ('Aakash',  2009, 9.0)]

a = np.array(vals, dtype=dtype)

print(np.sort(a, order='name'))
print(np.sort(a, order=['year', 'cgpa']))