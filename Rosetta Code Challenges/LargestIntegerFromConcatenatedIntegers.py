# Largest int from concatenated ints
from functools import cmp_to_key
def largest_number(nums):
    def compare(x, y):
        xy = int(str(x) + str(y))
        yx = int(str(y) + str(x))
        if xy < yx:
            return 1
        elif xy > yx:
            return -1
        else:
            return 0
    sorted_nums = sorted(nums, key=cmp_to_key(compare))
    return int(''.join(map(str, sorted_nums)))
nums = [3, 30, 34, 5, 9]
print(largest_number(nums))  