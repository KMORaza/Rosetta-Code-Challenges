# JortSort
def jortSort(arr):
    original_arr = arr.copy()
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != original_arr[i]:
            return False
    return True
array1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(jortSort(array1))
print(jortSort(array2))  