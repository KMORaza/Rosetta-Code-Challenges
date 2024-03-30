# Letter frequency
def count_characters(string):
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    result = [[char, freq] for char, freq in char_freq.items()]
    return result
string = "ab"
print(count_characters(string))