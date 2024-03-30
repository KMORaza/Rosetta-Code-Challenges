# Farey sequence
def farey_sequence(n):
    sequence = [(0, 1)]
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k*c - a, k*d - b
        sequence.append((a, b))
    return sequence
n = 20
farey_seq = farey_sequence(n)
for fraction in farey_seq:
    print(f"{fraction[0]}/{fraction[1]}")