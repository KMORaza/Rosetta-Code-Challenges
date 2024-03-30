# Sum to 100
def sum_to_target(target):
    def generate_expressions(curr_expr, index):
        if index == len(num_str):
            if eval(curr_expr) == target:
                solutions.append(curr_expr)
            return
        digit = num_str[index]
        generate_expressions(curr_expr + '+' + digit, index + 1)
        generate_expressions(curr_expr + '-' + digit, index + 1)
        generate_expressions(curr_expr + digit, index + 1)
    num_str = '123456789'
    solutions = []
    generate_expressions(num_str[0], 1)
    return sorted(solutions)
target_sum = 100
result = sum_to_target(target_sum)
for expression in result:
    print(expression)