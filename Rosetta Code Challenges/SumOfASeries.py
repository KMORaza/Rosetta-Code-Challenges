# Sum of a series
def series_sum(a, b):
    def sum_of_first_n_terms(n):
        return sum(1/(k**2) for k in range(1, n+1))
    sum_b = sum_of_first_n_terms(b)
    if a > 1:
        sum_a_minus_1 = sum_of_first_n_terms(a - 1)
    else:
        sum_a_minus_1 = 0
    sum_a_to_b = sum_b - sum_a_minus_1
    return sum_a_to_b
a = 2
b = 5
result = series_sum(a, b)
print("The sum of terms from", a, "to", b, "=", result)