# 9 Billion Names
def sum_of_nth_row(n):
    partitions = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        partitions[0][i] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            partitions[i][j] = partitions[i - j][j] + partitions[i][j - 1]
    return sum(partitions[n])
n = 6
print(f"The sum of the {n}ᵗʰ row = {sum_of_nth_row(n)}")