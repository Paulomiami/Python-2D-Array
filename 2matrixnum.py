import numpy as np

#Define two matrices A and B of 3*3 order
A = np.array([[1,2,3],[0,1,4],[5,6,0]])
B = np.array([[2,1,3],[4,5,6],[7,8,9]])

#Find inverse of matrix A
A_inverse = np.linalg.inv(A)
print ("Inverse of matrix A:\n", A_inverse)
print (A_inverse)

#Find the determinant of matrix B
B_determinant = np.linalg.det(B)
print("Determinant of matrix B:", B_determinant)
print (B_determinant)

#Print the result of A.A^-1
result = np.dot(A, A_inverse)
print("A.A^-1:")
print(result)