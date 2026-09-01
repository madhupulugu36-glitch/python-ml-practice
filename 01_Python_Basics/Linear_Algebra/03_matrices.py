import numpy as np


# ==========================================
# 1. CREATE A MATRIX
# ==========================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix:")
print(matrix)


# ==========================================
# 2. SHAPE
# ==========================================

print("\nShape:")
print(matrix.shape)


# ==========================================
# 3. NUMBER OF ROWS
# ==========================================

print("\nNumber of rows:")
print(matrix.shape[0])


# ==========================================
# 4. NUMBER OF COLUMNS
# ==========================================

print("\nNumber of columns:")
print(matrix.shape[1])


# ==========================================
# 5. NUMBER OF DIMENSIONS
# ==========================================

print("\nNumber of dimensions:")
print(matrix.ndim)


# ==========================================
# 6. ACCESS ELEMENTS
# ==========================================

print("\nFirst element:")
print(matrix[0, 0])

print("\nElement at row 2, column 3:")
print(matrix[1, 2])

print("\nLast element:")
print(matrix[2, 2])


# ==========================================
# 7. ACCESS ROWS
# ==========================================

print("\nFirst row:")
print(matrix[0])

print("\nSecond row:")
print(matrix[1])

print("\nThird row:")
print(matrix[2])


# ==========================================
# 8. ACCESS COLUMNS
# ==========================================

print("\nFirst column:")
print(matrix[:, 0])

print("\nSecond column:")
print(matrix[:, 1])

print("\nThird column:")
print(matrix[:, 2])


# ==========================================
# 9. MATRIX SIZE
# ==========================================

print("\nTotal number of elements:")
print(matrix.size)


# ==========================================
# 10. MATRIX DATA TYPE
# ==========================================

print("\nData type:")
print(matrix.dtype)

# ==========================================
# 11. MATRIX ADDITION
# ==========================================

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [10, 20],
    [30, 40]
])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nA + B:")
print(A + B)


# ==========================================
# 12. MATRIX SUBTRACTION
# ==========================================

print("\nA - B:")
print(A - B)

# ==========================================
# 13. MATRIX MULTIPLICATION
# ==========================================

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nShape of A:")
print(A.shape)

print("\nShape of B:")
print(B.shape)

print("\nA @ B:")
print(A @ B)

print("\nShape of result:")
print((A @ B).shape)

# ==========================================
# 14. MATRIX TRANSPOSE
# ==========================================

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal Matrix A:")
print(A)

print("\nShape of A:")
print(A.shape)

print("\nTranspose of A:")
print(A.T)

print("\nShape of Transpose:")
print(A.T.shape)

# ==========================================
# 15. IDENTITY MATRIX
# ==========================================

identity = np.eye(3)

print("\nIdentity Matrix (3x3):")
print(identity)

print("\nShape:")
print(identity.shape)


# ==========================================
# IDENTITY MATRIX PROPERTY
# A @ I = A
# ==========================================

A = np.array([
    [2, 3],
    [4, 5]
])

I = np.eye(2)

print("\nMatrix A:")
print(A)

print("\nIdentity Matrix I:")
print(I)

print("\nA @ I:")
print(A @ I)

print("\nIs A @ I equal to A?")
print(np.array_equal(A @ I, A))

# ==========================================
# 16. DETERMINANT
# ==========================================

A = np.array([
    [1, 2],
    [3, 4]
])

det_A = np.linalg.det(A)

print("\nMatrix A:")
print(A)

print("\nDeterminant of A:")
print(det_A)


# ==========================================
# 17. CHECK INVERTIBLE / SINGULAR
# ==========================================

if not np.isclose(det_A, 0):
    print("\nA is INVERTIBLE")
else:
    print("\nA is SINGULAR")

# ==========================================
# 18. SINGULAR MATRIX
# ==========================================

B = np.array([
    [1, 2],
    [2, 4]
])

det_B = np.linalg.det(B)

print("\nMatrix B:")
print(B)

print("\nDeterminant of B:")
print(det_B)

if not np.isclose(det_B, 0):
    print("B is INVERTIBLE")
else:
    print("B is SINGULAR")

# ==========================================
# 19. MATRIX INVERSE
# ==========================================

A = np.array([
    [1, 2],
    [3, 4]
])

print("\nMatrix A:")
print(A)

inverse_A = np.linalg.inv(A)

print("\nInverse of A:")
print(inverse_A)


# ==========================================
# VERIFY INVERSE
# A @ A^-1 = I
# ==========================================

print("\nA @ inverse(A):")
print(A @ inverse_A)

print("\nIdentity Matrix:")
print(np.eye(2))