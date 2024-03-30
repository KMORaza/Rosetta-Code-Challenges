# Lucas-Lehmer test
def lucas_lehmer_test(p):
    if p == 2:
        return True
    s = 4
    m = 2 ** p - 1
    for _ in range(2, p):
        s = (s ** 2 - 2) % m
    return s == 0
def is_mersenne_prime(p):
    if p <= 1:
        return False
    if p == 2:
        return True
    m = 2 ** p - 1
    if lucas_lehmer_test(p):
        return True
    else:
        return False
p = 7
print(is_mersenne_prime(p))