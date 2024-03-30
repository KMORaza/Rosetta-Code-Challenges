# Sorting algorithms/Pancake sort
def pancake_sort(arr):
    def flip(arr, k):
        i = 0
        while i < k // 2:
            arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]
            i += 1
    n = len(arr)
    for size in range(n, 1, -1):
        max_index = arr.index(max(arr[:size]))
        if max_index != size - 1:
            flip(arr, max_index + 1)
            flip(arr, size)
    return arr
arr = [6, 7, 8, 9, 2, 5, 3, 4, 1]
sorted_arr = pancake_sort(arr)
print(sorted_arr)