# Emirp primes
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def reverse_num(num):
    return int(str(num)[::-1])
def find_emirps(n, return_array=True):
    emirps = []
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            reversed_num = reverse_num(num)
            if num != reversed_num and is_prime(reversed_num):
                count += 1
                if return_array:
                    emirps.append(num)
                else:
                    if count == n:
                        return num
        num += 1
    if return_array:
        return emirps
    else:
        return count
def emirps_in_range(range_arr, return_array=True):
    start, end = range_arr
    emirps = []
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            reversed_num = reverse_num(num)
            if num != reversed_num and is_prime(reversed_num):
                count += 1
                if return_array:
                    emirps.append(num)
    if return_array:
        return emirps
    else:
        return count
def nth_emirp(n):
    return find_emirps(n, return_array=False)
print("First 10 emirps = ", find_emirps(10))
print("Emirps in range [100, 200] = ", emirps_in_range([100, 200]))
print("Number of emirps in range [100, 200] = ", emirps_in_range([100, 200], return_array=False))
print("3rd emirp = ", nth_emirp(3))