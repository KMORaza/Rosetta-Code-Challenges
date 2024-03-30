# Sort disjoint sublist
def sort_values_preserve_others(values, indices):
    sorted_values = [values[i] for i in sorted(indices)]
    sorted_values.sort()
    for i, index in enumerate(sorted(indices)):
        values[index] = sorted_values[i]
    return values
values = [7, 6, 5, 4, 3, 2, 1, 0]
indices = {6, 1, 7}
result = sort_values_preserve_others(values, indices)
print(result)