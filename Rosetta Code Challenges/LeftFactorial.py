# Left factorials
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def left_factorial(n):
    left_fact_sum = 0
    for i in range(1, n + 1):
        left_fact_sum += factorial(i)
    return left_fact_sum
number = 5
print("Left factorial of", number, "=", left_factorial(number))