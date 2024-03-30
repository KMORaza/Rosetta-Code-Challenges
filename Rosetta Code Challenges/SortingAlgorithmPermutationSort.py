# Sorting algorithms/Permutation sort
import itertools
def in_order(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr
def permutation_sort(arr):
    while not in_order(arr):
        arr = next_permutation(arr)
    return arr
arr = [3, 1, 4, 2]
sorted_arr = permutation_sort(arr)
print("Sorted array:", sorted_arr)