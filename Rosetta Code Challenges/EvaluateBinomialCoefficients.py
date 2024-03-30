# Evaluate binomial coefficients
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def binomial_coefficient(n, k):
    if k > n:
        return 0
    else:
        return factorial(n) // (factorial(n - k) * factorial(k))
n = 5
k = 2
result = binomial_coefficient(n, k)
print(f"C({n}, {k}) = {result}")