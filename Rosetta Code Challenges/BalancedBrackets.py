# Balanced Brackets
def is_balanced(string):
    stack = []
    bracket_pairs = {']': '[', '}': '{', ')': '('}
    for char in string:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    return not stack
test_cases = ["[]", "][", "[][]", "][", "[]][[]", "[[[[]]]]"]
for test_case in test_cases:
    print(test_case, "->", is_balanced(test_case))