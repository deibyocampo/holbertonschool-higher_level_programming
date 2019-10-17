#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as files:
        line_count = 0
        for line in files:
            line_count += 1
        return line_count
