#!/usr/bin/python3
def best_score(a_dictionary):
    if  a_dictionary is None:
        return None
    new_dic = list(a_dictionary.values())
    for key, val in a_dictionary.items():
        if val == max(new_dic):
            return key
