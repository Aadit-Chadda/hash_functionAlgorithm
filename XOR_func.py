def xor(x, s):
    print("Numerical: ")
    print(x, 'XOR', s, '=', x ^ s)
    print()
    print("Binary: ")
    print(bin(x), 'XOR', bin(s), '=', bin(x ^ s))


xor(4, 8)
print()
xor(4, 4)
print()
xor(255, 1)
print()
xor(255, 128)
print('\nThe End')
