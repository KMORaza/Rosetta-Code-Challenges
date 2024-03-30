# Zeckendorf number representation
def fibonacci_numbers(n):
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]
def zeckendorf_representation(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    fib = fibonacci_numbers(n)
    representation = []
    while n > 0:
        idx = max(i for i, val in enumerate(fib) if val <= n)
        representation.append(1)
        n -= fib[idx]
        fib = fib[:idx]
    return representation[::-1]
n = 99
print("Zeckendorf representation of", n, "=", zeckendorf_representation(n))