# Word frequency
import re
from collections import Counter
def most_common_words(text, n):
    if not text:
        return []
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    most_common = word_counts.most_common(n)
    return most_common
text = "Hello hello goodbye"
n = 2
result = most_common_words(text, n)
print(result)