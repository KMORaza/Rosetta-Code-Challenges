# S-Expressions
def parse_sexp(expression):
    stack = []
    current = []
    word = ''
    quoted = False
    for char in expression:
        if char == '(' and not quoted:
            if word:
                current.append(word)
                word = ''
            stack.append(current)
            current = []
        elif char == ')' and not quoted:
            if word:
                current.append(word)
                word = ''
            if current:
                stack[-1].append(current)
                current = stack.pop()
            else:
                return "Error: Unexpected ')'"
        elif char.isspace() and not quoted:
            if word:
                current.append(word)
                word = ''
        elif char == '"':
            if quoted:
                current.append(word)
                word = ''
                quoted = False
            else:
                if word:
                    return "Error: Unexpected '\"'"
                quoted = True
        else:
            word += char
    if quoted:
        return "Error: Unterminated string"
    if stack:
        return "Error: Unterminated S-Expression"
    if word:
        current.append(word)
    return current
input_str = '((data "quoted data" 123 4.5) (data (!@# (4.5) "(more" "data)")))'
result = parse_sexp(input_str)
print(result)