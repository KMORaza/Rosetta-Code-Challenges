# Sort using a custom comparator
def sort_strings(arr):
    arr.sort(key=lambda x: (-len(x), x))
    return arr
strings = ["banana", "apple", "pear", "grape", "kiwi", "orange"]
sorted_strings = sort_strings(strings)
print(sorted_strings)