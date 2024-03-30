# Abundant, deficient and perfect number classifications
def classify_integers(num):
    def sum_of_divisors(n):
        divisors_sum = 0
        for i in range(1, n):
            if n % i == 0:
                divisors_sum += i
        return divisors_sum
    deficient_count = 0
    perfect_count = 0
    abundant_count = 0
    for i in range(1, num + 1):
        div_sum = sum_of_divisors(i)
        if div_sum < i:
            deficient_count += 1
        elif div_sum == i:
            perfect_count += 1
        else:
            abundant_count += 1
    return [deficient_count, perfect_count, abundant_count]
num = 20
result = classify_integers(num)
print(result)