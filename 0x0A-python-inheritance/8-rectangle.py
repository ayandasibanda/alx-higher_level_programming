#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
# Import the BaseGeometry class
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry as its base class.

    This class inherits from BaseGeometry and extends it to represent a
    rectangle with a specified width and height.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        # Validate and set the width and height attributes
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

