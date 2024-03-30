# Sorting algorithms/Strand sort
def strand_sort(arr):
    def merge_sorted_arrays(arr1, arr2):
        merged_array = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged_array.append(arr1[i])
                i += 1
            else:
                merged_array.append(arr2[j])
                j += 1
        merged_array.extend(arr1[i:])
        merged_array.extend(arr2[j:])
        return merged_array
    def strand_sort_helper(arr):
        if len(arr) <= 1:
            return arr
        sorted_array = []
        sub_array = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if arr[i] >= sub_array[-1]:
                sub_array.append(arr.pop(i))
            else:
                i += 1
        sorted_array = merge_sorted_arrays(sub_array, strand_sort_helper(arr))
        return sorted_array
    return strand_sort_helper(arr)
unsorted_array = [3, 1, 4, 2]
strandsorted_array = strand_sort(unsorted_array)
print(strandsorted_array)