# Hailstone sequence
def hailstone_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
def longest_sequence_below_limit(limit):
    max_length = 0
    number_with_longest_sequence = 0
    for i in range(1, limit):
        length = len(hailstone_sequence(i))
        if length > max_length:
            max_length = length
            number_with_longest_sequence = i
    return number_with_longest_sequence, max_length
limit = 1000
result = longest_sequence_below_limit(limit)
print("Number with the longest hailstone sequence below", limit, ":", result[0])
print("Length of the sequence:", result[1])