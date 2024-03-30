# Identity matrix
def identity_matrix(n):
    if n <= 0:
        return "Invalid input: n must be a positive integer"
    else:
        identity = [[0] * n for _ in range(n)]
        for i in range(n):
            identity[i][i] = 1
        return identity
n = 5
print(identity_matrix(n))