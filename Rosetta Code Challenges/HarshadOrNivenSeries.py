# Harshad or Niven series
def is_harshad(n):
    return n % sum(int(digit) for digit in str(n)) == 0
def next_harshad(n):
    n += 1
    while True:
        if is_harshad(n):
            return n
        n += 1
def generate_harshad_sequence(starting_number, count):
    harshad_sequence = []
    current_number = starting_number
    while len(harshad_sequence) < count:
        current_number = next_harshad(current_number)
        harshad_sequence.append(current_number)
    return harshad_sequence
starting_number = 42
count = 10
harshad_sequence = generate_harshad_sequence(starting_number, count)
print(harshad_sequence)