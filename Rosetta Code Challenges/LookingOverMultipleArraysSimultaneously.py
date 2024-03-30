# Loop over multiple arrays simultaneously
def concatenate_arrays(arrays):
    result = []
    length = len(arrays[0])
    for i in range(length):
        concatenated = ""
        for array in arrays:
            concatenated += str(array[i])
        result.append(concatenated)
    return result
arrays = [["a", "b", "c"], ["A", "B", "C"], [1, 2, 3]]
output = concatenate_arrays(arrays)
print(output) 