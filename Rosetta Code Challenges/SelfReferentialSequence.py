# Self-referential sequence
def generate_self_referential_sequence(seed):
    def summarize(term):
        counts = {}
        for digit in term:
            counts[digit] = counts.get(digit, 0) + 1
        summary = ''
        for digit in sorted(counts.keys(), reverse=True):
            if digit != '0':
                summary += str(counts[digit]) + digit
        return summary
    sequence = [str(seed)]
    seen = {sequence[0]}
    while True:
        next_term = summarize(sequence[-1])
        if next_term in seen:
            return sequence
        sequence.append(next_term)
        seen.add(next_term)
seed_value = 2
sequence = generate_self_referential_sequence(seed_value)
print(sequence)