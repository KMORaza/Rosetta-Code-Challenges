# Symmetric difference
def symmetric_difference(A, B):
    sym_diff_set = set(A) ^ set(B)
    sym_diff_list = sorted(sym_diff_set)
    return sym_diff_list
A = [1, 2, 3]
B = [1, 3, 4]
result = symmetric_difference(A, B)
print(result)