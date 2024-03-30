# General FizzBuzz
def generalized_fizzbuzz(rules, num):
    output = ""
    for rule in rules:
        if num % rule[0] == 0:
            output += rule[1]
    if output == "":
        output = str(num)
    return output
rules = [[3, "Fizz"], [5, "Buzz"]]
for i in range(1, 21):
    print(generalized_fizzbuzz(rules, i))