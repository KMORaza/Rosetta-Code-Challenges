# Hash join
def hash_join(A, B, jA, jB):
    MB = {}
    for b in B:
        key = b[jB]
        if key not in MB:
            MB[key] = []
        MB[key].append(b)
    C = []
    for a in A:
        key = a[jA]
        if key in MB:
            for b in MB[key]:
                c = {**a, **b}
                C.append(c)
    return C
A = [
    {"Age": 27, "Name": "Jonah"},
    {"Age": 18, "Name": "Alan"},
    {"Age": 28, "Name": "Glory"},
    {"Age": 18, "Name": "Popeye"},
    {"Age": 28, "Name": "Alan"}
]
B = [
    {"Character": "Jonah", "Nemesis": "Whales"},
    {"Character": "Jonah", "Nemesis": "Spiders"},
    {"Character": "Alan", "Nemesis": "Ghosts"},
    {"Character": "Alan", "Nemesis": "Zombies"},
    {"Character": "Glory", "Nemesis": "Buffy"}
]
jA = "Name"
jB = "Character"
output = hash_join(A, B, jA, jB)
for row in output:
    print(row)