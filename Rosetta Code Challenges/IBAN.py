# IBAN
def validate_IBAN(IBAN):
    IBAN = IBAN.replace(" ", "").upper()
    if len(IBAN) < 5 or len(IBAN) > 34:
        return False
    if not IBAN[:2].isalpha():
        return False
    if not IBAN[2:].isalnum():
        return False
    IBAN = IBAN[4:] + IBAN[:4]
    IBAN_digits = ""
    for char in IBAN:
        if char.isdigit():
            IBAN_digits += char
        else:
            IBAN_digits += str(ord(char) - 55)
    IBAN_number = int(IBAN_digits)
    if IBAN_number % 97 == 1:
        return True
    else:
        return False
IBAN = "GB82 WEST 1234 5698 7654 32"
print(validate_IBAN(IBAN))