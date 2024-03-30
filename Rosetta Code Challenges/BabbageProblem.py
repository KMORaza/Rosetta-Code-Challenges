# Babbage Problem
def babbage_problem():
    for i in range(1, 1000000):
        square = i * i
        if str(square)[-6:] == "269696":
            return i
    return None
result = babbage_problem()
if result is not None:
    print(f"The smallest positive integer whose square ends in the digits 269,696 is: {result}")
else:
    print("No such integer found within the given range.")