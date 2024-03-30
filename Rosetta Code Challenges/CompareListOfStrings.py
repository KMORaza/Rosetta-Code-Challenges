# Compare a list of strings
def are_all_strings_equal(lst):
    if len(lst) == 0:
        return True
    first_string = lst[0]
    return all(string == first_string for string in lst)
def is_strictly_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True
lst = [['AA', 'BB', 'CC'], ['DD', 'EE', 'FF'], ['GG', 'HH', 'II']]
print("Are all strings lexically equal?", are_all_strings_equal(lst))
print("Is the list in strict ascending order?", is_strictly_ascending([item for sublist in lst for item in sublist]))