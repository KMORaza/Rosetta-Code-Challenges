# Soundex
def soundex(name):
    name = name.upper()
    encoded_name = name[0]
    encode = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    for char in name[1:]:
        code = encode.get(char, '')
        if code != encoded_name[-1]:
            encoded_name += code
    encoded_name = (encoded_name + '0000')[:4]
    return encoded_name
print(soundex("Quenci"))
print(soundex("Tymczak"))
print(soundex("Ashcraft"))