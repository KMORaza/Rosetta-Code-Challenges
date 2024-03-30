# Sorting algorithms/Bogosort
import random
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
def bogosort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = bogosort(my_list)
print("Sorted list:", sorted_list)