# Sorting algorithms/Gnome sort
def gnome_sort(arr):
    size = len(arr)
    i = 1
    j = 2
    while i < size:
        if arr[i - 1] <= arr[i]:
            i = j
            j += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return arr
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = gnome_sort(arr)
print("Sorted array:", sorted_arr)