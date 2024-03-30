# I before E except after C
def follows_ie_rule(word):
    if 'cie' in word:
        return False
    if 'cei' in word or 'ei' in word and 'cei' not in word:
        return True
    return False
words = ["believe", "ceiling", "receive", "science", "weird", "receipt"]
for word in words:
    print(f"{word}: {follows_ie_rule(word)}")