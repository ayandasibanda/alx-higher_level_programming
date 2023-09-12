#!/usr/bin/python3
"""Defines a function to convert a Python class instance to a JSON dictionary."""

def class_to_json(obj):
    """Convert a Python class instance to a JSON dictionary representation.

    Args:
        obj: The Python class instance to be converted.

    Returns:
        dict: A dictionary representing the attributes of the class instance.
    """
    return obj.__dict__

