# Fibonacci word
import math
def fibonacci_words(n):
    fib_words = []
    def fibonacci_word(index):
        if index == 1:
            return '1'
        elif index == 2:
            return '0'
        else:
            fib_minus_1 = '1'
            fib_minus_2 = '0'
            fib_word = ''
            for _ in range(index - 2):
                fib_word = fib_minus_1 + fib_minus_2
                fib_minus_2 = fib_minus_1
                fib_minus_1 = fib_word
            return fib_word
    for i in range(1, n + 1):
        word = fibonacci_word(i)
        length = len(word)
        entropy = round(-sum((word.count(c)/length) * math.log2(word.count(c)/length) for c in set(word)), 8)
        fib_words.append({'N': i, 'Length': length, 'Entropy': entropy, 'Word': word})
    return fib_words
print(fibonacci_words(5))