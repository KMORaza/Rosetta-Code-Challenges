# Y combinator
def Y_combinator(f):
    return (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
def factorial_recursive(f):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * f(n - 1)
    return factorial
factorial = Y_combinator(factorial_recursive)
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(10))