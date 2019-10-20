#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keySet = []
    for keys in a_dictionary.keys():
        if value == a_dictionary[keys]:
            keySet.append(keys)
    for rm in keySet:
        a_dictionary.pop(rm)
    return a_dictionary
