#!/usr/bin/python3
n = 122
while (n > 96):
    lett = n
    if n % 2 != 0:
        lett = n - 32
    print('{}'.format(chr(lett)), end="")
    n -= 1
