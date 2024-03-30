# Fractran
def fractran_first_10(program):
    fractions = [tuple(map(int, frac.split('/'))) for frac in program.split(',')]
    primes = []
    n = 2
    while len(primes) < 10:
        found = False
        for frac in fractions:
            if n * frac[0] % frac[1] == 0:
                n = n * frac[0] // frac[1]
                if n != 1:
                    primes.append(n)
                found = True
                break
        if not found:
            break
    return primes
program = "17/91,78/85,19/51,23/38,29/33,77/29,95/23,77/19,1/17,11/13,13/11,15/14,15/2,55/1"
print(fractran_first_10(program))