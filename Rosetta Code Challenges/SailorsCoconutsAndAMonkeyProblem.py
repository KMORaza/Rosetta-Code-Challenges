# Sailors, coconuts and a monkey problem
def find_initial_pile_size(n):
    if n == 1:
        return 1
    pile_size = n + 1
    while True:
        remaining = pile_size
        valid = True
        for _ in range(n):
            remaining -= 1
            if remaining % n != 0:
                valid = False
                break
            remaining -= remaining // n
        if valid and remaining % n == 0:
            return pile_size
        pile_size += 1
n = 5
initial_pile_size = find_initial_pile_size(n)
print("Minimum initial pile size for", n, "sailors is", initial_pile_size)