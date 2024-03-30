# Combinations
def generate_combinations(m, n):
    def backtrack(start, comb):
        if len(comb) == m:
            result.append(comb[:])
            return
        for i in range(start, n):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()
    result = []
    backtrack(0, [])
    return result
m = 3
n = 5
combinations = generate_combinations(m, n)
for comb in combinations:
    print(' '.join(str(num) for num in comb))