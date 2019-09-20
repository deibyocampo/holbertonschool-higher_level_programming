#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_combo = sorted(set_1.union(set_2))
    common_val = set_1 - (set(set_1) - set(set_2))
    for i in set_combo:
        for x in common_val:
            if x == i:
                set_combo.remove(i)
    return set_combo
