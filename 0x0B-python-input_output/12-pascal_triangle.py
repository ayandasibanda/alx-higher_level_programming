#!/usr/bin/python3
"""Defines a Pascal's Triangle generation function."""

def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
            Each inner list represents a row in the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles

