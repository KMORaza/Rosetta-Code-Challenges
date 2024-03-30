# Element-wise operations
import numpy as np
def m_add(matrix1, matrix2):
    return np.add(matrix1, matrix2)
def m_sub(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)
def m_mul(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)
def m_div(matrix1, matrix2):
    return np.divide(matrix1, matrix2)
def m_exp(matrix, exponent):
    return np.power(matrix, exponent)
def s_add(scalar, matrix):
    return scalar + matrix
def s_sub(scalar, matrix):
    return scalar - matrix
def s_mul(scalar, matrix):
    return scalar * matrix
def s_div(scalar, matrix):
    return scalar / matrix
def s_exp(scalar, matrix):
    return np.power(scalar, matrix)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
scalar = 2
print("Matrix Addition:")
print(m_add(matrix1, matrix2))
print("\nMatrix Subtraction:")
print(m_sub(matrix1, matrix2))
print("\nMatrix Multiplication:")
print(m_mul(matrix1, matrix2))
print("\nMatrix Division:")
print(m_div(matrix1, matrix2))
print("\nMatrix Exponentiation:")
print(m_exp(matrix1, 2))
print("\nScalar Addition:")
print(s_add(scalar, matrix1))
print("\nScalar Subtraction:")
print(s_sub(scalar, matrix1))
print("\nScalar Multiplication:")
print(s_mul(scalar, matrix1))
print("\nScalar Division:")
print(s_div(scalar, matrix1))
print("\nScalar Exponentiation:")
print(s_exp(scalar, matrix1))