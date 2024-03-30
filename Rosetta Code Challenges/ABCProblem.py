# ABC Problem
def can_spell_with_blocks(word, blocks):
    word = word.upper()
    used_blocks = set()
    for letter in word:
        found_block = False
        for block in blocks:
            if letter in block and block not in used_blocks:
                used_blocks.add(block)
                found_block = True
                break
        if not found_block:
            return False
    return True
blocks = [
    ('B', 'O'), ('X', 'K'), ('D', 'Q'), ('C', 'P'), ('N', 'A'),
    ('G', 'T'), ('R', 'E'), ('T', 'G'), ('Q', 'D'), ('F', 'S'),
    ('J', 'W'), ('H', 'U'), ('V', 'I'), ('A', 'N'), ('O', 'B'),
    ('E', 'R'), ('F', 'S'), ('L', 'Y'), ('P', 'C'), ('Z', 'M')
]
print(can_spell_with_blocks("Cat", blocks))
print(can_spell_with_blocks("Book", blocks))