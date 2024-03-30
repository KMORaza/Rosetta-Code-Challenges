# Tokenize a string with escaping
def split_string(string, separator, escape):
    result = []
    escaped = False
    current_field = ''
    for char in string:
        if char == escape:
            escaped = not escaped
        elif char == separator and not escaped:
            result.append(current_field)
            current_field = ''
        else:
            current_field += char
    result.append(current_field)
    return result
input_string = 'one^|uno||three^^^^|four^^^|^cuatro|'
separator_char = '|'
escape_char = '^'
output = split_string(input_string, separator_char, escape_char)
print(output)