# Straddling checkerboard
def straddle(message, alphabet):
    code_map = {}
    for i, row in enumerate(alphabet):
        for j, char in enumerate(row):
            code_map[char] = str(i) + str(j)
    encrypted_message = ""
    for char in message:
        if char.isdigit():
            encrypted_message += "\\" + char
        elif char in code_map:
            encrypted_message += code_map[char]
        else:
            encrypted_message += char
    return encrypted_message
def unstraddle(message, alphabet):
    code_map = {}
    for i, row in enumerate(alphabet):
        for j, char in enumerate(row):
            code_map[str(i) + str(j)] = char
    decrypted_message = ""
    i = 0
    while i < len(message):
        if message[i] == "\\":
            decrypted_message += message[i + 1]
            i += 2
        elif message[i:i+2] in code_map:
            decrypted_message += code_map[message[i:i+2]]
            i += 2
        else:
            decrypted_message += message[i]
            i += 1
    return decrypted_message
message = "HELLO123"
alphabet = ["ABCDEF", "GHIJKL", "MNOPQR"]
encrypted = straddle(message, alphabet)
decrypted = unstraddle(encrypted, alphabet)
print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)