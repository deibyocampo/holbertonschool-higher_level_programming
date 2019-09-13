#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("{:d} arguments.".format(argc - 1))
    elif argc == 2:
        print("{} argument:".format(argc - 1))
        print("{}: {}".format(argc - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(argc - 1))

        for index, date in enumerate(sys.argv):
            if index != 0:
                print("{}: {}".format(index, date))

