# Split a character string based on change of character
def split_string(string):
    result = []
    current = ""
    for char in string:
        if current == "":
            current += char
        elif char != current[-1]:
            result.append(current)
            current = char
        else:
            current += char
    if current:
        result.append(current)
    return result
string = "gHHH5YY++///\\"
result = split_string(string)
print(result)