#!/usr/bin/python3
for let in range(97, 123):
    if let == 101 or let == 113:
        continue
    else:
        print("{:s}".format(chr(let)), end="")
