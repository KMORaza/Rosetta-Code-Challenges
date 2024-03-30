# Kaprekar numbers
def is_kaprekar_number(n, bs):
    def split_number(num, base):
        num_str = str(num)
        num_len = len(num_str)
        split_index = 1
        while split_index < num_len:
            left_part = int(num_str[:split_index], base)
            right_part = int(num_str[split_index:], base)
            if left_part + right_part == n and left_part != 0 and right_part != 0:
                return True
            split_index += 1
        return False
    square = n * n
    return split_number(square, bs)
print(is_kaprekar_number(2223, 10))
print(is_kaprekar_number(9, 10))
print(is_kaprekar_number(45, 10))
print(is_kaprekar_number(55, 10))
print(is_kaprekar_number(5, 10)) 