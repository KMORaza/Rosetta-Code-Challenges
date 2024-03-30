# Longest increasing subsequence
def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(dp)
    lis = []
    max_index = dp.index(max_length)
    lis.insert(0, nums[max_index])
    max_length -= 1
    for i in range(max_index - 1, -1, -1):
        if dp[i] == max_length and nums[i] < lis[0]:
            lis.insert(0, nums[i])
            max_length -= 1
    return lis
array = [3, 10, 2, 1, 20]
print(longest_increasing_subsequence(array)) 