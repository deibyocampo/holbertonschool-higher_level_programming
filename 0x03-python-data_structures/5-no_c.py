#!/usr/bin/python3
def no_c(my_string):
    strc = ""
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            continue
        else:
            strc += my_string[i]
    return strc
