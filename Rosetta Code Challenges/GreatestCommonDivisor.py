# Greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
num1 = 48
num2 = 18
print("GCD of", num1, "and", num2, "=", gcd(num1, num2))