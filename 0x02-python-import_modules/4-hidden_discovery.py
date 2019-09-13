#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    list.sort
    for names in list:
        if names[0] != '_' and names[1] != '_':
            print(names)
