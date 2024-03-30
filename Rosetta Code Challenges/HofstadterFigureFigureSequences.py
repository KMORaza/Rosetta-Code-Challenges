# Hofstadter Figure-Figure sequences
def ffr(n):
    R = [0] * (n + 1)
    R[1] = 1
    for i in range(2, n + 1):
        R[i] = R[i - 1] + ffs(i - 1)
    return R[n]
def ffs(n):
    S = [0] * (n + 1)
    S[1] = 2
    for i in range(2, n + 1):
        if i not in S:
            S[i] = i
        else:
            S[i] = i + 1
    return S[n]
print("R(1) =", ffr(1))
print("R(5) =", ffr(5))
print("S(1) =", ffs(1))
print("S(5) =", ffs(5))  