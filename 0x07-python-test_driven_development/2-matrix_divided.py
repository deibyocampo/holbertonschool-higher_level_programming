#!usr/bin/python3
def matrix_divided(matrix, div):
    """ matrix divided will first """
    new_matrix = []
    new_list = []
    list_size = 0
    i = 0
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    strerr = "matrix must be a matrix (list of lists) of integers/floats"
    strexcep = "Each row of the matrix must have the same size"
    for lists in matrix:
        if i > 0:
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError(strexcep)
        if not isinstance(lists, list):
            raise TypeError(strerr)
        for num in lists:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(strerr)
            new_list.append(round(num / div, 2))
        new_matrix.append(new_list.copy())
        new_list.clear()
        i += 1
    return new_matrix
