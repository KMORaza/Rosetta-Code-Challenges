# Semiprime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def is_semiprime(n):
    if n <= 3:
        return False
    count = 0
    i = 2
    while count < 2 and i * i <= n:
        if n % i == 0 and is_prime(i):
            count += 1
            n //= i
            if n != 1 and is_prime(n):
                count += 1
        i += 1
    return count == 2
num = 15
print(is_semiprime(num))