#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function to convert a JSON string to a Python object."""
import json

def from_json_string(my_str):
    """Convert a JSON string to its Python object representation.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        Any: The Python object representation of the input JSON.
    """
    return json.loads(my_str)

