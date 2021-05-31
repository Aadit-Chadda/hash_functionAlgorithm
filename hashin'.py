import hashlib


def hashing(message):
    msg = message.encode()
    sha = hashlib.sha256()
    sha.update(msg)
    digester = sha.digest()
    return digester


message = input("Enter your password here: ")

password_hash = hashing(message)
print(password_hash)
