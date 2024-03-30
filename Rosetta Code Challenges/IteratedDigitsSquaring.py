# Iterated digits squaring
def square_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit * digit
        num //= 10
    return total
def process_number(num):
    while num != 1 and num != 89:
        num = square_of_digits(num)
    return num
number = int(input("Enter a natural number: "))
result = process_number(number)
print(f"The process ends in: {result}")