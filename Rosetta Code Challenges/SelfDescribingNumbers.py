# Self Describing Numbers
def is_self_describing(number):
    num_str = str(number)
    length = len(num_str)
    digit_count = {}
    for digit in num_str:
        digit_count[digit] = digit_count.get(digit, 0) + 1
    for i in range(length):
        if str(digit_count.get(str(i), 0)) != num_str[i]:
            return False
    return True
print(is_self_describing(2020))
print(is_self_describing(3211000))
print(is_self_describing(12345))