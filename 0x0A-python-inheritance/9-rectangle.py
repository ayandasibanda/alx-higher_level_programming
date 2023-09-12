#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
# Import the BaseGeometry class
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry as its base class.

    This class inherits from BaseGeometry and extends it to represent a
    rectangle with a specified width and height. It provides methods to
    calculate the area and a custom string representation.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle.

        Returns:
            str: A string in the format '[Rectangle] width/height'.
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)

