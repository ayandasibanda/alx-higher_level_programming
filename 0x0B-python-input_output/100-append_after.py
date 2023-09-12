#!/usr/bin/python3
"""Defines a function to insert text after each line containing a specific string in a text file."""

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a text file.

    Args:
        filename (str): The name of the text file.
        search_string (str): The string to search for within each line.
        new_string (str): The string to insert after each matching line.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

