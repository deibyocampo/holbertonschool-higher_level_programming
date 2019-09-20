#!usr/bin/python3
def number_keys(a_dictionary):
    my_list = list(a_dictionary.values())
    count = 0
    for i in my_list:
        count += 1
    return count
