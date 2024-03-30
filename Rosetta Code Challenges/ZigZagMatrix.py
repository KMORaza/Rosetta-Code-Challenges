# Zig-zag matrix
def generate_zigzag_array(n):
    result = [[0] * n for _ in range(n)]
    i, j = 0, 0
    num = 0
    for d in range(n * 2 - 1):
        if d % 2 == 0:
            while i >= 0 and j < n:
                result[i][j] = num
                num += 1
                i -= 1
                j += 1
            i += 1
            if j == n:
                i += 1
                j -= 1
        else:
            while j >= 0 and i < n:
                result[i][j] = num
                num += 1
                i += 1
                j -= 1
            j += 1
            if i == n:
                j += 1
                i -= 1
    return result
size = 7
zigzag_array = generate_zigzag_array(size)
for row in zigzag_array:
    print(" ".join(map(str, row)))