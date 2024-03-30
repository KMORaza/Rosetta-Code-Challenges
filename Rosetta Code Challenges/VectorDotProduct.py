# Vector dot product
def dot_product(vector1, vector2):
    if not (isinstance(vector1, list) and isinstance(vector2, list)):
        return None
    if len(vector1) != len(vector2):
        return None
    dot_product_result = sum(x * y for x, y in zip(vector1, vector2))
    return dot_product_result
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result = dot_product(vector1, vector2)
print("Dot Product:", result)