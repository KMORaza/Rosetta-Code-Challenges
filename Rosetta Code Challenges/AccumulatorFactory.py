# Accumulator Factory
def accumulator_factory(n):
    def accumulator(x):
        accumulator.total += x
        return accumulator.total
    accumulator.total = n
    return accumulator
acc1 = accumulator_factory(5)
print(acc1(3))
print(acc1(7))
acc2 = accumulator_factory(10)
print(acc2(2))
print(acc2(4)) 