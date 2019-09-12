#!/usr/bin/python3
def uppercase(str):
    letters = ""
    for let in str:
        if ord(let) in range(97, 123):
            letters += chr(ord(let) - 32)
        else:
            letters += let
    print("{:s}".format(letters))
