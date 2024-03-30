# Gray code
def gray_encode_decode(encode, num):
    if encode:
        gray = num ^ (num >> 1)
        return gray
    else:
        binary = 0
        while num:
            binary ^= num
            num >>= 1
        return binary
def display_binary_gray_decoded():
    print("Decimal\tBinary\t\tGray Code\tDecoded Gray")
    for num in range(32):
        binary = bin(num)[2:].zfill(5)
        gray = bin(gray_encode_decode(True, num))[2:].zfill(5)
        decoded_gray = gray_encode_decode(False, int(gray, 2))
        print(f"{num}\t{binary}\t\t{gray}\t\t{decoded_gray}")
display_binary_gray_decoded()