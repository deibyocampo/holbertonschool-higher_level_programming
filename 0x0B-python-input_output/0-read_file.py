#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as files:
        for line in files:
            print(line, end="")
