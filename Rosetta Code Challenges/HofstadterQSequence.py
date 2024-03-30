# Hofstadter Q Sequence
def hofstadter_Q(n):
    if n <= 2:
        return 1
    else:
        q = [0] * (n + 1)
        q[1] = q[2] = 1
        for i in range(3, n + 1):
            q[i] = q[i - q[i - 1]] + q[i - q[i - 2]]
        return q[n]
print(hofstadter_Q(1))
print(hofstadter_Q(2))
print(hofstadter_Q(10))