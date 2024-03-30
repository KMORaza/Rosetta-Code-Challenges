# Least common multiple
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
def lcm_array(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    lcm_result = arr[0]
    for i in range(1, len(arr)):
        lcm_result = lcm(lcm_result, arr[i])
    return lcm_result
array = [4, 6, 8, 10]
print("LCM of", array, "=", lcm_array(array))