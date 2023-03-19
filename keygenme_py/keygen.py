#!/usr/bin/env python3
import hashlib
import sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <name>')
    sys.exit()

name = sys.argv[1]

sha256 = hashlib.sha256(name.encode()).hexdigest()
indexes = '45362718'

static_1 = 'picoCTF{1n_7h3_|<3y_of_'
static_2 = '}'

dynamic = ''
for i_str in indexes:
    i = int(i_str)
    dynamic += sha256[i]

print(static_1 + dynamic + static_2)
