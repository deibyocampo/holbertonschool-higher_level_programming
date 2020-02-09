#!/usr/bin/python3
"""find_peak"""


def find_peak(list_of_integers):
    """ Function to find peak in array """
    if list_of_integers:
        peak = list_of_integers[0]
        return peak

    for i in range(len(list_of_integers)):
        if i != len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
        else:
            if list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]
