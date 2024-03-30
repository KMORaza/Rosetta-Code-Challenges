# Root Mean Square
import math
def calculate_rms(numbers):
    sum_of_squares = sum(num ** 2 for num in numbers)
    mean_of_squares = sum_of_squares / len(numbers)
    rms = math.sqrt(mean_of_squares)
    return rms
numbers = list(range(1, 11))
rms = calculate_rms(numbers)
print("RMS = ", rms)