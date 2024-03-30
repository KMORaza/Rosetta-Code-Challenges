# Dot product
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
print("Dot product = ", dot_product(vector1, vector2))