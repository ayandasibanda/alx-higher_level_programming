#!/usr/bin/python3
"""Defines a function to read a Python object from a JSON file."""
import json

def load_from_json_file(filename):
    """Read a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        Any: The Python object created from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)

