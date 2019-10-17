#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as files:
        if nb_lines <= 0:
            print(files.read(), end="")
        else:
            for line in range(nb_lines):
                print(files.readline(), end="")
