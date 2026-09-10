import numpy as np
from scipy import linalg

# Define a square matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
])

print("Original Matrix A:")
print(A)


# ==========================================
# i) QR Decomposition
# ==========================================

Q, R = linalg.qr(A)

print("\n--- QR Decomposition ---")

print("\nMatrix Q:")
print(Q)

print("\nMatrix R:")
print(R)

print("\nQ x R:")
print(Q @ R)


# ==========================================
# ii) Singular Value Decomposition (SVD)
# ==========================================

U, S, Vt = linalg.svd(A)

print("\n--- SVD ---")

print("\nMatrix U:")
print(U)

print("\nSingular Values:")
print(S)

print("\nMatrix V transpose:")
print(Vt)


# ==========================================
# iii) Least Squares
# ==========================================

# Equation: A X = b
b = np.array([6, 15, 25])

x, residuals, rank, singular_values = linalg.lstsq(A, b)

print("\n--- Least Squares ---")

print("\nSolution x:")
print(x)

print("\nResiduals:")
print(residuals)

print("\nRank:")
print(rank)

print("\nSingular Values:")
print(singular_values)