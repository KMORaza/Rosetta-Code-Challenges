# Sum digits of an integer
def sum_of_digits_in_base(number_str):
    base_values = {str(i): i for i in range(10)}
    base_values.update({chr(ord('a') + i): i + 10 for i in range(26)})
    total_sum = 0
    for digit in number_str:
        total_sum += base_values[digit.lower()]
    return total_sum
print(sum_of_digits_in_base("1"))
print(sum_of_digits_in_base("1234"))
print(sum_of_digits_in_base("fe"))
print(sum_of_digits_in_base("f0e"))