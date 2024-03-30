# Sorting algorithms/Bead sort
def bead_sort(arr):
    max_val = max(arr)
    matrix = [[0] * len(arr) for _ in range(max_val)]
    for num in arr:
        for j in range(num):
            matrix[max_val - 1 - j][arr.index(num)] += 1
    sorted_arr = []
    for i in range(max_val):
        sum_col = sum(matrix[i])
        sorted_arr.extend([max_val - i] * sum_col)
    return sorted_arr
arr = [5, 3, 9, 7, 1, 8, 4, 6, 2]
sorted_arr = bead_sort(arr)
print("Sorted array:", sorted_arr)