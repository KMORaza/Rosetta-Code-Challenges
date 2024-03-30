# SHA-1
import hashlib
def sha1_digest(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    return sha1.hexdigest()
input_string = "Hello, world!"
sha1_hash = sha1_digest(input_string)
print("SHA-1 digest:", sha1_hash)