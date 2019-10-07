#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in ['.', '?', ':']:
        if i in text:
            text = text.replace(i, i + "@")

    new_list = text.split("@")

    for idx in range(len(new_list)):
        if new_list[idx] == "":
            del new_list[idx]

    for idx, line in enumerate(new_list):
        new_list[idx] = line.strip()

    new_str = ("\n\n".join(new_list))

    print(new_str)
