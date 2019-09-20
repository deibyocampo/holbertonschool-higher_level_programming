#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_com = sorted(set_1.union(set_2))
    common_val = set_1 - (set(set_1) - set(set_2))
    for i in set_com:
        for x in common_val:
            if x == i:
                set_com.remove(i)
    return set_com
