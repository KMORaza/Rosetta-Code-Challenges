# Cumulative standard deviation
import math
def calculate_standard_deviation(data):
    mean = sum(data) / len(data)
    squared_deviations = [(x - mean) ** 2 for x in data]
    variance = sum(squared_deviations) / len(data)
    standard_deviation = math.sqrt(variance)
    return standard_deviation
data = [2, 4, 4, 4, 5, 5, 7, 9]
print("σ =", calculate_standard_deviation(data))