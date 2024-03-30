# Define a primitive data type
class Num:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Not a Number')
        if value < 1 or value > 10:
            raise TypeError('Out of range')
        self.value = value
    def __repr__(self):
        return str(self.value)
    def __str__(self):
        return str(self.value)
    def __int__(self):
        return int(self.value)
    def __float__(self):
        return float(self.value)
    def __add__(self, other):
        result = self.value + other
        if result < 1 or result > 10:
            raise TypeError('Out of range')
        return Num(result)
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        result = self.value - other
        if result < 1 or result > 10:
            raise TypeError('Out of range')
        return Num(result)
    def __rsub__(self, other):
        return self.__sub__(other)
try:
    num1 = Num(5)
    print(num1)
    num2 = Num(11)
except TypeError as e:
    print(e)
try:
    num3 = Num('a')
except TypeError as e:
    print(e)
try:
    result = num1 + 3
    print(result)
    result = num1 + 6
except TypeError as e:
    print(e)