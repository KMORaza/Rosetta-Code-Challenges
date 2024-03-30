# Greatest subsequential sum
def max_subsequence_sum(arr):
    if not arr:
        return 0
    max_sum = current_sum = arr[0]
    start_index = end_index = temp_index = 0
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_index = i
        else:
            current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_index
            end_index = i
    return max_sum, arr[start_index:end_index + 1]
sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subsequence = max_subsequence_sum(sequence)
print("Maximum subsequence sum:", max_sum)
print("Subsequence with maximum sum:", subsequence)