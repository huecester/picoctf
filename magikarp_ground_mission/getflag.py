#!/usr/bin/env python3
from pwn import *
import sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <host> <port>')

host = sys.argv[1]
port = int(sys.argv[2])

conn = ssh(user='ctf-player',host=host,port=port,password='b60940ca')
data = conn.system('echo $(cat ~/drop-in/1of3.flag.txt)$(cat /2of3.flag.txt)$(cat ~/3of3.flag.txt)').recvall()
print(data.decode('utf-8').strip())
