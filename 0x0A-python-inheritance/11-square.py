#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
# Import the Rectangle class
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square, a specific type of Rectangle.

    This class inherits from Rectangle and represents a square with a specified
    size. It utilizes the Rectangle class to set both width and height attributes.
    """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)  # Validate the size parameter
        super().__init__(size, size)  # Call the constructor of the Rectangle class
        self.__size = size  # Set the size attribute

