#!/usr/bin/env python3
from pwn import *

KEY_LEN = 50000
CHUNK_SIZE = 1000

r = remote('mercury.picoctf.net', 36449)

r.recvuntil(b'This is the encrypted flag!\n')
encrypted_flag = unhex(r.recvlineS(keepends=False))
required_bytes = KEY_LEN - len(encrypted_flag)
while required_bytes > 0:
    num_bytes_to_send = min(required_bytes, CHUNK_SIZE)
    r.sendlineafter(b'What data would you like to encrypt? ', b'A' * num_bytes_to_send)
    required_bytes -= num_bytes_to_send

r.sendlineafter(b'What data would you like to encrypt? ', encrypted_flag)
r.recvline()
print(unhex(r.recvlineS()))
