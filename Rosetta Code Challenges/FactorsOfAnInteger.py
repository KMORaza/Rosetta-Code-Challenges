# Factors of an integer
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
number = 144
print("Factors of", number, "=", find_factors(number))