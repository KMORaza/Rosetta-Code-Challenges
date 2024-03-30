# Last letter-first letter
def find_max_sequence(words):
    def find_sequence(word, remaining_words, memo):
        if word in memo:
            return memo[word]
        max_seq = []
        for next_word in remaining_words:
            if next_word[0] == word[-1]:
                new_remaining = remaining_words.copy()
                new_remaining.remove(next_word)
                seq = find_sequence(next_word, new_remaining, memo)
                if len(seq) > len(max_seq):
                    max_seq = seq
        max_seq = [word] + max_seq
        memo[word] = max_seq
        return max_seq
    max_sequence = []
    memo = {}
    for word in words:
        seq = find_sequence(word, words.copy(), memo)
        if len(seq) > len(max_sequence):
            max_sequence = seq
    return max_sequence
input_words = ["apple", "elephant", "tiger", "rabbit", "lion", "newt", "turtle", "eagle"]
print(find_max_sequence(input_words))