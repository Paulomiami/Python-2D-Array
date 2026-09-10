import numpy as np
from scipy import linalg

# ==========================================
# Question 1: 4x4 Matrix
# Find Transpose and Rank
# ==========================================

A = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [2, 5, 8, 11]
])

print("Original Matrix A:")
print(A)

# Transpose of matrix
transpose_A = A.T

print("\nTranspose of Matrix A:")
print(transpose_A)

# Rank of matrix using SciPy
rank_A = np.linalg.matrix_rank(A)

print("\nRank of Matrix A:")
print(rank_A)



# Question 2: 4x4 Square Matrix
# Find Eigen Values and Eigen Vectors

B = np.array([
    [4, 1, 0, 0],
    [1, 4, 0, 0],
    [0, 0, 3, 1],
    [0, 0, 1, 3]
])

print("\n\nOriginal Matrix B:")
print(B)

# Find eigenvalues and eigenvectors using SciPy
eigen_values, eigen_vectors = linalg.eig(B)

print("\nEigen Values of Matrix B:")
print(eigen_values)

print("\nEigen Vectors of Matrix B:")
print(eigen_vectors)