#!/usr/bin/python3
"""find_peak"""


def find_peak(list_of_integers):
    """ Function to find peak in array """
    peak = 0
    if len(list_of_integers) == 0:
        return None

    for i in range(len(list_of_integers) - 1):
        next_int = i + 1
        if list_of_integers[next_int] >= list_of_integers[i]:
            if len(list_of_integers) <= 3\
               and list_of_integers[next_int] >= list_of_integers[i]:
                peak = list_of_integers[next_int]
            if i != 0 and next_int != len(list_of_integers) - 1:
                peak = list_of_integers[next_int]
        else:
            continue
    return peak
