#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""
# Inherit from the int class
class MyInt(int):
    """Represents an integer with inverted equality operators.

    This class inherits from the int class but overrides the equality operators
    '==' and '!=' to have the opposite behavior. When comparing a MyInt object
    to another integer, '==' behaves like '!=' and '!=' behaves like '=='.
    """

    def __eq__(self, value):
        """Override '==' operator with '!=' behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override '!=' operator with '==' behavior."""
        return self.real == value

