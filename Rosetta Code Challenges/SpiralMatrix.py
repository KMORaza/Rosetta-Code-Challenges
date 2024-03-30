# Spiral matrix
def generate_spiral_array(n):
    spiral_array = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row, col = 0, 0
    for num in range(1, n*n + 1):
        spiral_array[row][col] = num
        next_row = row + directions[0][0]
        next_col = col + directions[0][1]
        if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or spiral_array[next_row][next_col] != 0:
            directions.append(directions.pop(0))
        row += directions[0][0]
        col += directions[0][1]
    return spiral_array
n = 5
spiral_array = generate_spiral_array(n)
for row in spiral_array:
    print(' '.join(map(str, row)))