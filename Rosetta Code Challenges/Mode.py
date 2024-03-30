# Mode
def mode(arr):
    if not arr:
        return None
    frequency = {}
    max_frequency = 0
    modes = []
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        max_frequency = max(max_frequency, frequency[num])
    for key, value in frequency.items():
        if value == max_frequency:
            modes.append(key)
    return modes
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Mode(s) of the array = ", mode(arr))