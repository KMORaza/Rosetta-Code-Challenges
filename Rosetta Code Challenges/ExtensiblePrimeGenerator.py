# Extensible prime generator
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def generate_primes(input_range, return_as_array=True):
    primes = []
    if isinstance(input_range, int):
        n = input_range
        num = 2
        while len(primes) < n:
            if is_prime(num):
                primes.append(num)
            num += 1
    elif isinstance(input_range, (list, tuple)):
        start, end = input_range
        for num in range(start, end + 1):
            if is_prime(num):
                primes.append(num)
    else:
        n = input_range
        num = 2
        while len(primes) < n:
            if is_prime(num):
                primes.append(num)
            num += 1
    if return_as_array:
        return primes
    else:
        return len(primes)
print(generate_primes(10, return_as_array=True))
print(generate_primes((10, 50), return_as_array=True))
print(generate_primes((10, 50), return_as_array=False))
print(generate_primes(100, return_as_array=False))