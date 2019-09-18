#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print("")
    else:
        for x in matrix:
            for (y, z) in enumerate(x):
                if y < len(x) - 1:
                    print("{:d} ".format(z), end="")
                else:
                    print("{:d}".format(z))
