# Factors of a Mersenne number
def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result
def find_factor_of_mersenne_prime(P):
    exponent = P
    modulus = 2 ** P - 1
    for k in range(1, P):
        potential_factor = 2 * k * P + 1
        if mod_pow(2, exponent, potential_factor) == 1:
            return potential_factor
    return None
P = 23
factor = find_factor_of_mersenne_prime(P)
if factor:
    print(f"A factor of 2^{P} - 1 = {factor}")
else:
    print(f"No factor found for 2^{P} - 1")