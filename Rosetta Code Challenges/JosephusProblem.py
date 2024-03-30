# Josephus problem
def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n - 1, k) + k) % n
n = 41
k = 3
survivor = josephus(n, k)
print("The survivor is prisoner #", survivor + 1)