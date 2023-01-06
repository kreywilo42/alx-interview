#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    pt = []
    if type(n) is not int or n <= 0:
        return pt
    for x in range(n):  # 1
        ct = []
        for y in range(x+1):
            if y == 0 or y == x:
                ct.append(1)
            else:
                ct.append(pt[x-1][y]+pt[x-1][y-1])
        pt.append(ct)
    return pt
