# Gaussian elimination
import numpy as np
def gaussian_elimination(A, b):
    n = len(b)
    s = np.max(np.abs(A), axis=1)
    Ab = np.column_stack((A.astype(np.float64), b.astype(np.float64)))
    for i in range(n):
        pivot_row = np.argmax(np.abs(Ab[i:, i]) / s[i]) + i
        Ab[[i, pivot_row]] = Ab[[pivot_row, i]]
        for j in range(i+1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]
    return x
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])
x = gaussian_elimination(A, b)
print("Solution x:", x)