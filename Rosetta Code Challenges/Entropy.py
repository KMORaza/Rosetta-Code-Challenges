# Entropy
import math
from collections import Counter
def shannon_entropy(input_string):
    char_counts = Counter(input_string)
    total_chars = len(input_string)
    probabilities = {char: count / total_chars for char, count in char_counts.items()}
    entropy = -sum(prob * math.log2(prob) for prob in probabilities.values())
    return entropy
input_string = "abbcccdddd"
entropy = shannon_entropy(input_string)
print("Shannon Entropy = ", entropy)