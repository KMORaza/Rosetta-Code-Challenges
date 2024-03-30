# Generator/Exponential
def squares():
    n = 1
    while True:
        yield n * n
        n += 1
def cubes():
    n = 1
    while True:
        yield n * n * n
        n += 1
def filter_cubes(generator):
    for value in generator:
        if value % (value ** (1/3)) != 0:
            yield value
def nth_filtered_value(n):
    filtered_generator = filter_cubes(squares())
    for _ in range(n - 1):
        next(filtered_generator)
    return next(filtered_generator)
n = 7
result = nth_filtered_value(n)
print(f"The {n}th value of the filtered generator = {result}.")