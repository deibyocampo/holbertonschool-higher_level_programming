#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        max = my_list[0]
        for i, val in enumerate(my_list):
            if val > max:
                max = val
        return max
    else:
        return None
