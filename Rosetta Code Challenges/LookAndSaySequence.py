# Look and Say sequence
def look_and_say(s):
    result = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result += str(count) + s[i]
        i += 1
    return result
input_str = "1"
iterations = 5
for _ in range(iterations):
    input_str = look_and_say(input_str)
    print(input_str)