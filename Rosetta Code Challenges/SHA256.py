# SHA-256
import hashlib
def sha256_hash(input_string):
    encoded_string = input_string.encode('utf-8')
    sha256_hash_object = hashlib.sha256()
    sha256_hash_object.update(encoded_string)
    sha256_hash_hex = sha256_hash_object.hexdigest()
    return sha256_hash_hex
input_string = "Hello, World!"
hashed_result = sha256_hash(input_string)
print("SHA-256 hash of '{}': {}".format(input_string, hashed_result))