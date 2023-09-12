#!/usr/bin/python3
"""Defines a function to write a Python object to a JSON file."""
import json

def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

