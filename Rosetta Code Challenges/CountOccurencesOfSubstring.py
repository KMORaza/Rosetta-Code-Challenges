# Count occurrences of a substring
import re
def count_non_overlapping_substring(string, substring):
    pattern = re.compile(substring)
    matches = pattern.findall(string)
    return len(matches)
string = "abababab"
substring = "ab"
print(count_non_overlapping_substring(string, substring))  