# Pythagorean Means
from math import prod
def arithmetic_mean(arr):
    return sum(arr) / len(arr)
def geometric_mean(arr):
    return prod(arr) ** (1 / len(arr))
def harmonic_mean(arr):
    return len(arr) / sum(1 / num for num in arr)
def compute_means(arr):
    A = arithmetic_mean(arr)
    G = geometric_mean(arr)
    H = harmonic_mean(arr)
    means = {
        "values": {
            "Arithmetic": A,
            "Geometric": G,
            "Harmonic": H
        },
        "test": "yes" if A >= G >= H else "no"
    }
    return means
arr = list(range(1, 11))
result = compute_means(arr)
print(result)