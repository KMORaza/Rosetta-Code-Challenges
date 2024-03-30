# Amicable Pairs
def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum
def find_amicable_pairs(limit):
    amicable_pairs = []
    for num in range(2, limit):
        sum_divisors = sum_of_divisors(num)
        if sum_divisors != num and sum_of_divisors(sum_divisors) == num:
            amicable_pairs.append((num, sum_divisors))
    return amicable_pairs
amicable_pairs = find_amicable_pairs(20000)
print("Amicable pairs below 20,000:")
for pair in amicable_pairs:
    print(pair)