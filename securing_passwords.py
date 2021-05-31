import base64
import hashlib

iterations = 45454

salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
password = "password".encode()

value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
value = base64.b64encode(value)
print('Alice Password: ')
print(password)
print()
print('Alice Password Hash value: ')
print(value)

print('\n')

salt_1 = base64.b64encode("dghiSD563rd3*^i=bFHBFfc+-kFVbjh!2@#DESV457&".encode())
password_1 = "password".encode()

value_1 = hashlib.pbkdf2_hmac("sha512", password_1, salt_1, iterations, dklen=128)
value_1 = base64.b64encode(value_1)
print('Bob Password: ')
print(password_1)
print()
print('Bob password Hash value: ')
print(value_1)

print('\n')

if value == value_1:
    print('Same Hash value')
else:
    print('Different Hash value')

if password == password_1:
    print('Same password')
else:
    print('Different password')
