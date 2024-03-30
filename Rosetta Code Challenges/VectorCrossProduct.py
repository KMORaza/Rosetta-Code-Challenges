# Vector cross product
def cross_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        return None
    x1, y1, z1 = vector1
    x2, y2, z2 = vector2
    cross_x = y1 * z2 - z1 * y2
    cross_y = z1 * x2 - x1 * z2
    cross_z = x1 * y2 - y1 * x2
    return [cross_x, cross_y, cross_z]
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
print(cross_product(vector1, vector2))