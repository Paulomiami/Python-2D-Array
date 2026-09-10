import numpy as np
from scipy import linalg

# -------------------------------
# Question 1: Linear Equations
# -------------------------------

# 2x + 3y = 8
# 4x + 5y = 14

A1 = np.array([
    [2, 3],
    [4, 5]
])

B1 = np.array([8, 14])

# Solve equations
X1 = linalg.solve(A1, B1)

print("Question 1:")
print("x =", X1[0])
print("y =", X1[1])


# -------------------------------
# Question 2: Two Cars
# -------------------------------

# Same direction: x - y = 1
# Opposite direction: x + y = 11

A2 = np.array([
    [1, -1],
    [1,  1]
])

B2 = np.array([1, 11])

# Solve equations
X2 = linalg.solve(A2, B2)

print("\nQuestion 2:")
print("Velocity of first car =", X2[0], "km/h")
print("Velocity of second car =", X2[1], "km/h")