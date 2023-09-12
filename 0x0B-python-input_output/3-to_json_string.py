#!/usr/bin/python3
"""Defines a function to convert an object to its JSON representation."""
import json

def to_json_string(my_obj):
    """Convert an object to its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: A JSON string representing the input object.
    """
    return json.dumps(my_obj)

