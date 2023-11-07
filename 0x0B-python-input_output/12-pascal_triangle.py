#!/usr/bin/python3
'''module for pascal_triangle'''


def pascal_triangle(n):
    ''' that returns a list of lists of integers'''
    if n <= 0:
        return ([])
    
    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return (triangle)
