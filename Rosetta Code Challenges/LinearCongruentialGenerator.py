# Linear Congruential Generator
def linear_congruential_generator(r0, a, c, m, n):
    rn = r0
    for _ in range(n):
        rn = (a * rn + c) % m
    return rn
r0 = 5
a = 7
c = 3
m = 11
n = 5
result = linear_congruential_generator(r0, a, c, m, n)
print("Result:", result)