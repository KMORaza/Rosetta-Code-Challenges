# Longest string challenge
def longest_strings(strings):
    max_length = max(len(s) for s in strings)
    return [s for s in strings if len(s) == max_length]
input_strings = ["apple", "pomegranate", "orange", "kiwi", "grape"]
result = longest_strings(input_strings)
print(result)