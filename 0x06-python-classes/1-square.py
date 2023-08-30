#!/usr/bin/python3

"""
Define a class Square.
"""

class Square:
    """
    Represent a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
