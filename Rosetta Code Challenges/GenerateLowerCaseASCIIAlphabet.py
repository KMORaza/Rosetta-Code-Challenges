# Generate lower case ASCII alphabet
def generate_lower_ascii_range(start_char, end_char):
    start_ascii = ord(start_char)
    end_ascii = ord(end_char)
    if start_ascii > end_ascii:
        return []
    result = [chr(i) for i in range(start_ascii, end_ascii + 1)]
    return result
range_start = 'a'
range_end = 'f'
result = generate_lower_ascii_range(range_start, range_end)
print(result)