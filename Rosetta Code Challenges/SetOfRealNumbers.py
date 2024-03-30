# Set of real numbers
class SetRange:
    def __init__(self, low, high, range_type):
        self.low = low
        self.high = high
        self.range_type = range_type
    def contains(self, x):
        if self.range_type == 0:
            return self.low <= x <= self.high
        elif self.range_type == 1:
            return self.low < x < self.high
        elif self.range_type == 2:
            return self.low <= x < self.high
        elif self.range_type == 3:
            return self.low < x <= self.high
def perform_operation(set1, set2, operation, values):
    result = []
    if operation == "union":
        for value in values:
            if set1.contains(value) or set2.contains(value):
                result.append(True)
            else:
                result.append(False)
    elif operation == "intersect":
        for value in values:
            if set1.contains(value) and set2.contains(value):
                result.append(True)
            else:
                result.append(False)
    elif operation == "subtract":
        for value in values:
            if set1.contains(value) and not set2.contains(value):
                result.append(True)
            else:
                result.append(False)
    return result
set1 = SetRange(0, 2, 1)
set2 = SetRange(1, 3, 3)
operation = "union"
values = [1, 2, 3, 4, 5]
result = perform_operation(set1, set2, operation, values)
print(result)