# Luhn test of credit card numbers
def luhn_validate(number):
    digits = [int(digit) for digit in reversed(str(number))]
    doubled_digits = [(digit * 2) if index % 2 else digit for index, digit in enumerate(digits)]
    subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]
    total = sum(subtracted_digits)
    return total % 10 == 0
print(luhn_validate(49927398716))
print(luhn_validate(49927398717)) 