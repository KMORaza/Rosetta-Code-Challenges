# Sum multiples of 3 and 5
def sum_multiples_of_3_or_5(n):
    total_sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum
n = 20
result = sum_multiples_of_3_or_5(n)
print(f"The sum of all positive multiples of 3 or 5 below {n} = {result}")