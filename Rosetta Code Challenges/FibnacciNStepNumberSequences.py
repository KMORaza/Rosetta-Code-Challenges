# Fibonacci n-step number sequences
def fibonacci_lucas_sequence(n, num_elements, sequence_type):
    sequence = []
    if sequence_type == "f":
        a, b = 0, 1
        for _ in range(num_elements):
            sequence.append(a)
            a, b = b, a + b
    elif sequence_type == "l":
        a, b = 2, 1
        for _ in range(num_elements):
            sequence.append(a)
            a, b = b, a + b
    else:
        print("Invalid sequence type. Choose 'f' for Fibonacci or 'l' for Lucas.")
        return None
    return sequence
fibonacci_result = fibonacci_lucas_sequence(2, 10, "f")
print("Fibonacci Sequence:", fibonacci_result)
lucas_result = fibonacci_lucas_sequence(2, 10, "l")
print("Lucas Sequence:", lucas_result)