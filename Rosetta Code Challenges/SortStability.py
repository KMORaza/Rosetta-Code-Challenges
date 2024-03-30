# Sort stability
def stable_sort(arr):
    def custom_key(item):
        return (item[0], item[1])
    sorted_arr = sorted(arr, key=custom_key)
    return sorted_arr
arr = [["UK", "London"], ["US", "New York"], ["US", "Birmingham"], ["UK", "Birmingham"]]
sorted_arr = stable_sort(arr)
print(sorted_arr)