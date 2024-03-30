# Taxicab numbers
def find_taxicab_numbers(n):
    taxicab_numbers = []
    found_pairs = {}
    for a in range(1, 1000):
        for b in range(a, 1000):
            pair_sum = a**3 + b**3
            if pair_sum in found_pairs:
                taxicab_numbers.append((pair_sum, (a, b), found_pairs[pair_sum]))
            found_pairs[pair_sum] = (a, b)
    taxicab_numbers.sort(key=lambda x: x[0])
    return taxicab_numbers[:n]
def display_taxicab_numbers(n):
    taxicab_list = find_taxicab_numbers(n)
    for idx, taxicab in enumerate(taxicab_list):
        taxicab_sum, (a, b), (c, d) = taxicab
        print(f"Taxicab number {idx+1} = {taxicab_sum}")
        print(f"Constituent cubes: ({a}^3 + {b}^3) = ({c}^3 + {d}^3)")
        print()
n = 5
display_taxicab_numbers(n)