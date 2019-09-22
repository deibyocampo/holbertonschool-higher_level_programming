#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    nm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) != str or roman_string is None:
        return 0
    for idx in range(len(roman_string)):
        if roman_string[idx] in nm.keys():
            if idx > 0 and nm[roman_string[idx]] > nm[roman_string[idx - 1]]:
                num += nm[roman_string[idx]] - 2 * nm[roman_string[idx - 1]]
            else:
                num += nm[roman_string[idx]]
    return num
