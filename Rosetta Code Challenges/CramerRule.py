# Cramer's rule
import numpy as np
def solve_system_cramers(A, b):
    n = A.shape[0]
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("The determinant of the coefficient matrix is zero, Cramer's rule cannot be applied.")
    solutions = []
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        det_Ai = np.linalg.det(Ai)
        xi = det_Ai / det_A
        solutions.append(xi)
    return np.array(solutions)
A = np.array([[2, -1, 5, 1],
              [3, 2, 2, -6],
              [1, 3, 3, -1],
              [5, -2, -3, 3]])
b = np.array([-3, -32, -47, 49])
solution = solve_system_cramers(A, b)
print("Solution for w, x, y, z:", solution)