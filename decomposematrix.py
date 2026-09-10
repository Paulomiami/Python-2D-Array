import numpy as np
from scipy import linalg

# Define a 4x4 matrix
A = np.array([
    [1, 2, 3, 4],
    [2, 5, 7, 9],
    [1, 3, 4, 6],
    [3, 6, 8, 10]
])

print("Original Matrix A:")
print(A)

# Find P, L and U
P, L, U = linalg.lu(A)

print("\nPermutation Matrix P:")
print(P)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)