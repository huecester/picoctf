#!/usr/bin/env python3

# Original algorithm:
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
# 28777 = ord(flag[0] << 8) + ord(flag[i + 1])

ciphertext = None
with open('./enc', 'r') as f:
    ciphertext = f.read()

for c in ciphertext:
    print(chr(ord(c) >> 8) + chr(ord(c) & 0b11111111), end='')
