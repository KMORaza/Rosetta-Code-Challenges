# Sorting algorithms/Stooge sort
def stoogesort(L, i=0, j=None):
    if j is None:
        j = len(L) - 1
    if L[j] < L[i]:
        L[i], L[j] = L[j], L[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stoogesort(L, i, j - t)
        stoogesort(L, i + t, j)
        stoogesort(L, i, j - t)
    return L
arr = [5, 3, 8, 2, 7, 1, 6, 4]
sorted_arr = stoogesort(arr)
print("Sorted array:", sorted_arr)