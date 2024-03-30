# 24 Game
from itertools import permutations
def find_24(nums):
    ops = ['+', '-', '*', '/']
    def apply_op(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b != 0:
                return a / b
            else:
                return None
    for perm in permutations(nums):
        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    a, b, c, d = perm
                    res = apply_op(apply_op(apply_op(a, b, op1), c, op2), d, op3)
                    if res == 24:
                        return f"({a} {op1} {b}) {op2} {c} {op3} {d}"
                    res = apply_op(apply_op(a, b, op1), apply_op(c, d, op3), op2)
                    if res == 24:
                        return f"{a} {op1} {b} {op2} ({c} {op3} {d})"
                    res = apply_op(apply_op(a, apply_op(b, c, op2), op1), d, op3)
                    if res == 24:
                        return f"{a} {op1} ({b} {op2} {c}) {op3} {d}"
                    res = apply_op(a, apply_op(apply_op(b, c, op2), d, op3), op1)
                    if res == 24:
                        return f"{a} {op1} ({b} {op2} {c} {op3} {d})"
                    res = apply_op(apply_op(a, b, op1), apply_op(c, d, op3), op2)
                    if res == 24:
                        return f"({a} {op1} {b}) {op2} ({c} {op3} {d})"
    return "no solution exists"
print(find_24([1, 2, 3, 4]))