# Stern-Brocot sequence
def stern_brocot_position(n):
    if n == 1:
        return 1
    sequence = [1, 1]
    position = 2
    while True:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        position += 1
        if next_number == n:
            return position
        next_number = sequence[-1]
        sequence.append(next_number)
        position += 1
        if next_number == n:
            return position
number_to_find = 2
position = stern_brocot_position(number_to_find)
print(f"The position of {number_to_find} in the Stern-Brocot sequence is: {position}")