# Stream Merge
def merge_sorted_arrays(arrays):
    result = []
    pointers = [0] * len(arrays)
    while any(pointers[i] < len(arrays[i]) for i in range(len(arrays))):
        min_val = float('inf')
        min_index = None
        for i in range(len(arrays)):
            if pointers[i] < len(arrays[i]) and arrays[i][pointers[i]] < min_val:
                min_val = arrays[i][pointers[i]]
                min_index = i
        result.append(min_val)
        pointers[min_index] += 1
    return result
arrays = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]
sorted_result = merge_sorted_arrays(arrays)
print(sorted_result)