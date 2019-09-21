#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orn = sorted(a_dictionary.keys())
    for i in orn:
        print("{}: {}".format(i, a_dictionary[i]))
