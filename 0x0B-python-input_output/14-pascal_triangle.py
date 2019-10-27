#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = []

    for place in range(n):
        temp = []
        for i in range(place + 1):
            if i == 0 or i == place:
                temp.append(1)
            else:
                num = triangle[place - 1][i - 1] + triangle[place - 1][i]
                temp.append(num)
        triangle.append(temp)
    return triangle
