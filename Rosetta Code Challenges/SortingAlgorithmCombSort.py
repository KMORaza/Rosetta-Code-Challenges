# Sorting algorithms/Comb sort
def combsort(array):
    gap = len(array)
    shrink_factor = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1
        swapped = False
        i = 0
        while i + gap < len(array):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
            i += 1
    return array
arr = [9, 1, 5, 6, 2, 0, 3, 8, 7, 4]
sorted_arr = combsort(arr)
print(sorted_arr)