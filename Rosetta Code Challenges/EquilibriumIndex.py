# Equilibrium index
def equilibrium_indices(sequence):
    n = len(sequence)
    equilibrium_indexes = []
    total_sum = sum(sequence)
    left_sum = 0
    for i in range(n):
        total_sum -= sequence[i]
        if left_sum == total_sum:
            equilibrium_indexes.append(i)
        left_sum += sequence[i]
    return equilibrium_indexes
sequence = [-7, 1, 5, 2, -4, 3, 0]
print("Equilibrium indices = ", equilibrium_indices(sequence))