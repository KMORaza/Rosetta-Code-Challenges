# Comma quibbling
def generate_output(words):
    if not words:
        return "{}"
    elif len(words) == 1:
        return "{" + words[0] + "}"
    elif len(words) == 2:
        return "{" + " and ".join(words) + "}"
    else:
        all_but_last = ", ".join(words[:-1])
        last = " and " + words[-1]
        return "{" + all_but_last + last + "}"
test_cases = [
    [],
    ["ABC"],
    ["ABC", "DEF"],
    ["ABC", "DEF", "G", "H"]
]
for case in test_cases:
    print(generate_output(case))