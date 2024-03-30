# SEDOLs
def calculate_sedol_checksum(sedol):
    if not isinstance(sedol, str) or len(sedol) != 6:
        return None
    weights = (1, 3, 1, 7, 3, 9)
    checksum = sum((ord(s) - 48) * w if s.isdigit() else (ord(s) - 55) * w for s, w in zip(sedol, weights)) % 10
    return sedol + str(checksum)
test_cases = [
    ("710889", "7108899"),
    ("B0YBKJ", "B0YBKJ7"),
    ("406566", "4065663"),
    ("B0YBLH", "B0YBLH2"),
    ("228276", "2282765"),
    ("B0YBKL", "B0YBKL9"),
    ("557910", "5579107"),
    ("B0YBKR", "B0YBKR5"),
    ("585284", "5852842"),
    ("B0YBKT", "B0YBKT7"),
    ("B00030", "B000300")
]
for sedol, expected in test_cases:
    result = calculate_sedol_checksum(sedol)
    print(f"{sedol} => {result}, Expected: {expected}, Match: {result == expected}")