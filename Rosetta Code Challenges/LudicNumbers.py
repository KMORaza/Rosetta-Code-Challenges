# Ludic numbers
def generate_ludic_numbers(limit):
    ludic_numbers = [1]
    index = 1
    num = 2
    while num <= limit:
        ludic_numbers.append(num)
        index += 1
        if index < len(ludic_numbers):
            num = ludic_numbers[index]
        else:
            break
        j = 0
        while j < len(ludic_numbers):
            if ludic_numbers[j] % num == 0:
                ludic_numbers.pop(j)
            else:
                j += 1
    return ludic_numbers
limit = 50
print(generate_ludic_numbers(limit))