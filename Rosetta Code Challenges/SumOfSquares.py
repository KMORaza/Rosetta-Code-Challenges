# Sum of squares
def sum_of_squares(arr):
    return sum(x**2 for x in arr)
my_array = [1, 2, 3, 4, 5]
result = sum_of_squares(my_array)
print("Sum of squares:", result)