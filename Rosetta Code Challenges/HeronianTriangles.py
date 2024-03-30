# Heronian triangles
import math
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
def ordered_triangles(triangles, n):
    if n <= 0:
        return []
    def triangle_sort_key(triangle):
        return triangle_area(*triangle)
    sorted_triangles = sorted(triangles, key=triangle_sort_key)
    return sorted_triangles[:n]
triangles = [[3, 4, 5], [5, 12, 13], [6, 8, 10], [7, 24, 25]]
n = 3
ordered = ordered_triangles(triangles, n)
print("First", n, "ordered triangles:")
for triangle in ordered:
    print(triangle)