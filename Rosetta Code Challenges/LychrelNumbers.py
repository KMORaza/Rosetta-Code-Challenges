# Lychrel numbers
def is_lychrel_number(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    def reverse_and_add(num):
        return num + int(str(num)[::-1])
    iterations = 0
    while iterations < 500:
        n = reverse_and_add(n)
        if is_palindrome(n):
            return False
        iterations += 1
    return True
print(is_lychrel_number(196))
print(is_lychrel_number(4994))
print(is_lychrel_number(89))