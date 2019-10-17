#!/usr/bin/python3
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


new_json_list = argv[1:]

try:
    my_obj = load_from_json_file("add_item.json")
    my_obj.extend(new_json_list)
    save_to_json_file(my_obj, "add_item.json")

except:
    save_to_json_file(new_json_list, "add_item.json")
